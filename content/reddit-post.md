# Reddit Posts -- PostgreSQL EXPLAIN BUFFERS

> Three subreddit-specific posts, each with a different angle.
> Standard Markdown only. No Unicode bold/italic. No emojis.

---

## Post 1: r/PostgreSQL

**Title**: How EXPLAIN (ANALYZE, BUFFERS) solved a checkout latency crisis: 1.2s to 42ms with three changes

---

**TL;DR**: A customer's checkout query regressed from 50ms to 1.2s over two weeks. `EXPLAIN ANALYZE` showed the same plan every time -- same index scan, same nested loop. Adding `BUFFERS` revealed a 0.3% buffer hit ratio (50 shared hits vs 15,000 shared reads). Three changes -- VACUUM ANALYZE, work_mem tuning, shared_buffers resize -- brought it down to 42ms with a 97.3% hit ratio. No application code changes.

---

I was working with a customer running a mid-size e-commerce platform on PostgreSQL 17 -- about 2 million rows in orders, 500K active users, 32GB RAM instance. Their checkout flow joins `orders`, `order_items`, and `inventory` to validate stock and calculate totals. For months p95 was ~50ms. Then it started creeping up over two weeks until a flash sale pushed it past 1.2 seconds.

The team ran `EXPLAIN ANALYZE` repeatedly. The plan was identical every time: Index Scan on `orders_user_id_idx`, Nested Loop joins, same estimated rows. So they tuned PgBouncer, added read replicas, opened a ticket with their cloud provider. Three days of debugging, none of it helped.

### What BUFFERS showed

We added one option to the command:

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT o.order_id, o.total, i.stock_available
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN inventory i ON i.product_id = oi.product_id
WHERE o.user_id = 8421
  AND o.status = 'pending'
ORDER BY o.created_at DESC
LIMIT 5;
```

Key lines from the output:

```
Buffers: shared hit=50 read=15000 written=847
...
Sort Method: external merge  Disk: 2500kB
Buffers: shared hit=48 read=14950, temp read=312 written=2500
...
Index Scan using orders_user_id_idx on orders o
  Buffers: shared hit=12 read=14800
```

Three immediate red flags:

1. **shared hit=50, shared read=15,000** -- that is a 0.3% buffer hit ratio on what should be a 95%+ cached OLTP query
2. **temp written=2,500** on the Sort node -- `work_mem` was set to 256kB (well below the PG 17 default of 4MB), forcing a 2,500-page external merge sort to disk
3. **shared written=847** -- background writer could not keep up, PostgreSQL was doing synchronous writes during a SELECT

### Confirming at the workload level

We checked pg_stat_statements to make sure this was not a one-off cold-cache read:

```sql
SELECT query,
       calls,
       shared_blks_hit,
       shared_blks_read,
       round(shared_blks_hit::numeric /
             nullif(shared_blks_hit + shared_blks_read, 0), 4) AS hit_ratio,
       temp_blks_written
FROM pg_stat_statements
WHERE query LIKE '%orders%order_items%inventory%'
ORDER BY shared_blks_read DESC
LIMIT 5;
```

`shared_blks_read` had grown 30x over two weeks while `shared_blks_hit` stayed flat. Consistently reading from disk, execution after execution.

### Root cause

The orders table had bloated from 857 pages to over 15,000 pages. During the promotional event, high insert volume outpaced autovacuum. Dead tuples accumulated, the table bloated, and hot checkout data spread across pages that no longer fit in the 2GB shared_buffers cache. The query was evicting its own pages faster than it could reuse them.

### Three fixes

**Fix 1: Manual VACUUM ANALYZE**

```sql
VACUUM (VERBOSE, ANALYZE) orders;
```

Reclaimed dead tuples. Table shrank from 15,000 to ~3,200 pages (still larger than original 857 due to legitimate order growth).

**Fix 2: SET LOCAL work_mem**

```sql
BEGIN;
SET LOCAL work_mem = '16MB';
-- checkout query here
COMMIT;
```

Eliminated the 2,500-page temp spill. Sort completed in memory.

**Fix 3: shared_buffers + autovacuum tuning**

```
shared_buffers = '4GB'                     -- up from 2GB (25% of 32GB RAM)
autovacuum_vacuum_cost_delay = '2ms'       -- down from 20ms
autovacuum_vacuum_scale_factor = 0.05      -- vacuum at 5% dead tuples, not 20%
```

### Before and after

| Metric | Before | After |
|--------|--------|-------|
| Execution time | 1,192ms | 42ms |
| Buffer hit ratio | 0.3% | 97.3% |
| Temp pages spilled | 2,500 | 0 |
| Shared pages written (sync) | 847 | 0 |
| Orders table pages | 15,000 | 3,200 |

### PG 18 note

Starting with PostgreSQL 18, `EXPLAIN ANALYZE` includes BUFFERS output by default. If you are on PG 17 or earlier, get in the habit of typing `EXPLAIN (ANALYZE, BUFFERS)` instead of `EXPLAIN ANALYZE`. The I/O profile is where the real performance story lives -- the plan alone does not tell you if your data is coming from cache or disk.

For ongoing monitoring, `pg_stat_statements` gives you workload-level buffer stats over time, and `auto_explain` with `log_buffers = on` captures EXPLAIN output for any query exceeding a latency threshold.

**Curious what buffer hit ratios others are seeing on their high-traffic OLTP queries. What is your typical baseline, and have you caught a regression through buffer stats before?**

I wrote up the full case study with all the EXPLAIN output, pg_stat_statements queries, and monitoring setup here: [full writeup](https://example.com/postgresql-explain-buffers-case-study?utm_source=reddit&utm_medium=social&utm_campaign=explain-buffers)

---

## Post 2: r/ExperiencedDevs

**Title**: We spent 3 days debugging 'network latency' on a slow query. Adding BUFFERS to EXPLAIN found the real problem in 5 minutes.

---

**TL;DR**: Checkout queries regressed from 50ms to 1.2 seconds over two weeks. The team blamed network latency for three days -- tuned PgBouncer, added read replicas, filed a cloud provider ticket. Adding one word (`BUFFERS`) to `EXPLAIN ANALYZE` revealed the query was reading 15,000 pages from disk with a 0.3% cache hit ratio. Three config-only changes brought it to 42ms. The query plan looked identical the entire time.

---

I want to share a debugging story because I think the failure mode is instructive -- not the PostgreSQL tuning itself, but how the team got stuck for three days chasing the wrong problem.

### The setup

Mid-size e-commerce platform, PostgreSQL 17, ~2M orders, 500K active users. The checkout flow runs a join across orders, order_items, and inventory. For months the p95 was around 50ms. Then it started creeping up. Over about two weeks it drifted to 200ms, then 600ms. Nobody noticed until a flash sale pushed it past 1.2 seconds. Cart abandonment spiked 12 percentage points. Revenue was leaking at roughly $5,600 per minute during checkout degradation.

### Where the investigation went wrong

The team did the reasonable things. They ran `EXPLAIN ANALYZE` on the checkout query. The plan was the same: same Index Scan, same Nested Loop joins, same row estimates. Nothing had changed in the plan. So they concluded the database was fine and looked elsewhere.

They tuned PgBouncer connection pooling. They checked the cloud provider's network health dashboard. They added a read replica. They opened a support ticket. Three days of work, none of it helped, because the hypothesis was wrong -- and they did not have the data to challenge it.

The core mistake: `EXPLAIN ANALYZE` shows you the *plan* and the *timing*, but it does not show you *where the data came from*. A query can have an optimal plan and still be catastrophically slow if every page is being read from disk instead of cache. Without I/O visibility, the team could not distinguish between "the database is doing the right thing slowly" and "the database is doing the wrong thing."

### What actually happened

When we ran `EXPLAIN (ANALYZE, BUFFERS)` -- literally one additional word in the command -- the output included lines like:

```
Buffers: shared hit=50 read=15000 written=847
```

50 pages from cache, 15,000 from disk. A 0.3% buffer hit ratio on a query that should be 95%+ cached. The query was doing the right thing (correct plan, correct indexes), but reading almost entirely from disk.

The root cause: table bloat. During a promotional surge, high insert volume had outpaced autovacuum. Dead tuples accumulated, the orders table bloated from ~850 pages to 15,000 pages, and the hot data spread across pages that no longer fit in the buffer cache. The working set had quietly outgrown the allocated memory.

### The fix

Three configuration changes, no application code:

1. **Manual VACUUM ANALYZE** -- reclaimed dead tuples, table shrank from 15,000 to 3,200 pages
2. **work_mem tuning** (256kB to 16MB via `SET LOCAL`) -- eliminated a 2,500-page temp spill during sorts
3. **shared_buffers resize** (2GB to 4GB) + autovacuum tuning -- cache now fits the working set, vacuum keeps pace with writes

Result: 1,192ms down to 42ms. Buffer hit ratio from 0.3% to 97.3%.

### The debugging lesson

What I took away from this -- and what I have seen at other customers:

- **EXPLAIN ANALYZE is not enough.** It shows the plan and the timing but hides the I/O. `EXPLAIN (ANALYZE, BUFFERS)` is the command you actually want. (PG 18+ includes BUFFERS by default, so this gap will close over time.)
- **"Same plan" does not mean "same performance."** The plan was identical before and after the regression. The I/O profile was catastrophically different. If your only diagnostic is the query plan, you will miss this class of problem entirely.
- **Gradual regressions are harder to catch.** This was not a sudden failure -- it drifted over two weeks. Nobody noticed until a load spike made it obvious. If the team had been monitoring buffer hit ratios via pg_stat_statements, they would have caught the regression when it was a 200ms problem, not a 1.2s emergency.
- **Teams default to infrastructure explanations.** "Must be the network" is a reasonable first hypothesis, but three days is too long to run with it without counter-evidence. The counter-evidence was one command away.

I am not saying this to criticize the team -- they did reasonable things with the information they had. The problem was that `EXPLAIN ANALYZE` without `BUFFERS` gives you an incomplete picture, and the incomplete picture led to an incorrect hypothesis.

**For teams that do production PostgreSQL troubleshooting: what is your go-to diagnostic sequence when a query regresses but the plan looks unchanged? Curious how others approach this.**

Wrote up the full technical walkthrough with all the SQL and EXPLAIN output here: [full writeup](https://example.com/postgresql-explain-buffers-case-study?utm_source=reddit&utm_medium=social&utm_campaign=explain-buffers)

---

## Post 3: r/programming

**Title**: Most developers have never added BUFFERS to PostgreSQL's EXPLAIN. Here's why you should.

---

**TL;DR**: PostgreSQL's `EXPLAIN ANALYZE` shows you the query plan and timing, but hides where the data actually comes from -- memory or disk. Adding `BUFFERS` reveals the I/O profile: cache hits vs disk reads. In a real case, a checkout query had an identical plan before and after a regression from 50ms to 1.2s. Only the buffer stats showed the problem: 0.3% cache hit ratio. Starting with PostgreSQL 18 (2025), BUFFERS is included by default.

---

If you use PostgreSQL and have ever run `EXPLAIN ANALYZE` on a slow query, you have probably looked at the plan -- Index Scan vs Seq Scan, Nested Loop vs Hash Join -- and tried to figure out where the time goes. That is useful, but it is only half the story.

There is an option most developers never add: `BUFFERS`. It turns EXPLAIN from a plan viewer into an I/O profiler.

### What BUFFERS tells you

When you run `EXPLAIN (ANALYZE, BUFFERS)`, PostgreSQL reports buffer activity at every node in the plan:

- **shared hit** -- pages found in the in-memory cache (fast)
- **shared read** -- pages read from disk (slow)
- **temp written** -- pages spilled to disk because an in-memory operation (sort, hash) ran out of memory

The key metric is the **buffer hit ratio**: `shared hit / (shared hit + shared read)`. If your OLTP query is at 95%+, it is well-cached. If it drops to single digits, almost every page access is going to disk, and your query will be slow no matter how good the plan is.

### Why this matters

I was working with a customer whose checkout query regressed from 50ms to 1.2 seconds over two weeks. The team ran `EXPLAIN ANALYZE` repeatedly -- the plan was identical every time. Same index scan, same joins. They spent three days debugging "network latency."

When we added `BUFFERS`, the output showed:

```
Buffers: shared hit=50 read=15000
```

50 pages from cache, 15,000 from disk. A 0.3% hit ratio on a query that should be near 100% cached. The database was doing the right thing (correct plan), but the data was not in memory.

The root cause turned out to be table bloat -- autovacuum had not kept up with a surge in writes, the table grew from ~850 pages to 15,000, and the working set no longer fit in the buffer cache. Three config changes (VACUUM, work_mem increase, shared_buffers resize) brought the query to 42ms with a 97.3% hit ratio. No code changes.

The plan was identical before and after the problem. Only the I/O statistics told the real story.

### PostgreSQL 18 changes the default

Here is why this is relevant right now: **PostgreSQL 18 (released 2025) includes BUFFERS output by default in EXPLAIN ANALYZE.** Before PG 18, you had to remember to type `EXPLAIN (ANALYZE, BUFFERS)` every time. Now every developer running `EXPLAIN ANALYZE` will see buffer stats automatically.

If you are on PG 17 or earlier, the fix is simple -- always use `EXPLAIN (ANALYZE, BUFFERS)` instead of plain `EXPLAIN ANALYZE`. The option has existed since PG 8.4 (2009). It just was not the default, so most people never knew it was there.

### The one-sentence version

Your query plan tells you *what* PostgreSQL is doing. The buffer stats tell you *how much I/O it costs*. If you are only looking at the plan, you are flying half-blind.

**Has anyone else run into a situation where the plan looked fine but the query was still slow? Curious what the diagnosis turned out to be.**

Wrote up the full case study with EXPLAIN output, pg_stat_statements queries, and version-by-version feature history here: [full writeup](https://example.com/postgresql-explain-buffers-case-study?utm_source=reddit&utm_medium=social&utm_campaign=explain-buffers)
