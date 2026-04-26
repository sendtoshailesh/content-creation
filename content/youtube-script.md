# YouTube Script: PostgreSQL EXPLAIN BUFFERS -- How We Cut Checkout Latency 96%

> **Target duration**: 10-12 minutes (~1,500-1,800 words spoken)
> **Format**: On-camera + screen share (terminal/EXPLAIN output) + slides
> **Pacing**: ~150 words/minute

---

## Title Options

1. **PostgreSQL EXPLAIN BUFFERS: How We Cut Checkout Latency 96%** (primary -- matches blog SEO)
2. **One Word Fixed Our 1.2-Second Checkout Query | PostgreSQL BUFFERS**
3. **Stop Ignoring BUFFERS in PostgreSQL EXPLAIN (Real Case Study)**
4. **Why Your PostgreSQL Queries Are Slow: The EXPLAIN Option Nobody Uses**

---

## Full Timed Script

### [0:00 - 0:30] Cold Open

**[ON CAMERA]**

**SCRIPT**:

Fifty milliseconds. That is how fast our customer's checkout query ran for months. Then it hit 1.2 seconds. Cart abandonment spiked 12 percentage points. The engineering team spent three days blaming the network, tuning PgBouncer, opening tickets with their cloud provider. None of it worked.

The fix? Adding one word to a SQL command. Let me show you exactly what happened.

**NOTES**: Deliver with urgency. Pause after "1.2 seconds" for emphasis. Hold eye contact on "one word."

*~75 words | 0:30*

---

### [0:30 - 2:00] Problem Setup

**[ON CAMERA]** -> **[SLIDE: shared-buffers-flow.png]** at 1:15

**SCRIPT**:

Here is the setup. Mid-size e-commerce platform running PostgreSQL 17. About 2 million rows in the orders table, 500,000 active users, hosted on a managed cloud instance with 32 gigs of RAM. The checkout flow joins orders, order items, and inventory to validate stock and calculate totals. Standard stuff.

For months, p95 latency sat at 50 milliseconds. Then it started creeping. Over two weeks, it drifted to 200, then 600 milliseconds. Nobody noticed until a flash sale pushed it past 1.2 seconds.

The team did what most of us would do -- they ran `EXPLAIN ANALYZE`. The plan looked identical every time. Same index scan, same nested loop joins, same estimated rows. Nothing looked wrong.

But here is the thing. `EXPLAIN ANALYZE` shows you the plan. It does not show you where the data is coming from -- memory or disk. Without that information, the I/O problem was completely invisible.

**NOTES**: Slow down on "creeping...200...600." Cut to shared-buffers-flow.png at "where the data is coming from" to set up the concept visually.

*~170 words | 1:08 segment*

---

### [2:00 - 4:00] Concepts: Shared Buffers, Hit Ratio, EXPLAIN BUFFERS

**[SCREEN SHARE: terminal with EXPLAIN output]**
**[SLIDE: shared-buffers-flow.png]** visible as reference overlay

**SCRIPT**:

Let me break down what PostgreSQL actually reports when you add `BUFFERS` to your `EXPLAIN ANALYZE`. There are four numbers that matter.

**Shared hit** -- pages found in the buffer cache. This is the fast path. No disk I/O, the data was already in memory.

**Shared read** -- pages fetched from disk. Every read adds latency. This is where slow queries hide.

**Shared dirtied** -- pages modified during the query. And yes, even `SELECT` queries can dirty pages. PostgreSQL updates hint bits during reads. That is completely normal.

**Shared written** -- pages synchronously written to disk during execution. If you see this on a `SELECT`, it means the background writer could not keep up. That is a warning sign.

The key formula is the buffer hit ratio: shared hit divided by shared hit plus shared read. So if you have 13 hits out of 870 total accesses, that is a 1.5% hit ratio. Terrible for an OLTP query -- but expected on a cold cache after a restart.

Now, one critical insight. The hit ratio is a diagnostic tool, not a scorecard. There is no universal "good" number. A reporting query scanning a large date range at 10-30% hit ratio -- that is fine. A checkout query dropping from 95% to 40%? Something broke.

There is one more thing to watch: `temp read` and `temp written`. These track when sorts or hash operations exceed `work_mem` and spill to disk. The default `work_mem` is a conservative 4 megabytes. At 256 kilobytes -- which some older configurations use -- a sort on 200,000 rows can force a 9.7-megabyte disk spill.

**NOTES**: Type out the hit ratio formula live in terminal. Pause after each of the four signals. Use the shared-buffers-flow diagram as a picture-in-picture reference during the first half.

*~275 words | 1:50 segment*

---

### [4:00 - 7:00] Investigation: EXPLAIN BUFFERS Output, pg_stat_statements

**[SCREEN SHARE: terminal -- live demo style]**
**[SLIDE: query-plan-tree.png]** at 5:00
**[SLIDE: buffer-hit-comparison.png]** at 6:15

**SCRIPT**:

OK, let me show you the actual investigation. We took the team's original `EXPLAIN ANALYZE` and added exactly one option:

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

And look at what came back. Right here at the top: `shared hit=50, shared read=15,000`. Let that sink in. Fifty pages from cache, 15,000 from disk. That is a 0.3% buffer hit ratio. This query was reading almost entirely from disk.

But there is more. Look at the sort node: `temp written=312`. The `work_mem` had been set to 256 kilobytes -- well below the default 4 megabytes. PostgreSQL was spilling an external merge sort to disk on every single execution.

And this one: `shared written=847`. The background writer was falling behind, and PostgreSQL was doing synchronous writes during a `SELECT`. That should not happen under normal load.

Now I want to zoom into the plan tree. Each node shows its own buffer stats. The index scan on the orders table -- that is where the damage is: `shared hit=12, shared read=14,800`. That is our bottleneck.

So we confirmed this was not a one-off. We checked `pg_stat_statements`:

```sql
SELECT query, calls, shared_blks_hit, shared_blks_read,
       round(shared_blks_hit::numeric /
             nullif(shared_blks_hit + shared_blks_read, 0), 4) AS hit_ratio
FROM pg_stat_statements
WHERE query LIKE '%orders%order_items%inventory%'
ORDER BY shared_blks_read DESC;
```

`shared_blks_read` had grown 30x over two weeks. `shared_blks_hit` stayed nearly flat. This was not a cold cache problem. The query was consistently reading from disk, execution after execution.

The root cause: during the promotional event, high insert volume outpaced autovacuum. Dead tuples accumulated, the orders table bloated from 857 pages to over 15,000. The working set no longer fit in the 2-gigabyte `shared_buffers`. The checkout query was evicting its own pages faster than it could reuse them.

**NOTES**: Walk through the EXPLAIN output line by line. Highlight the three critical numbers by circling or annotating them on screen. Cut to query-plan-tree.png at the "zoom into the plan tree" transition. Cut to buffer-hit-comparison.png when presenting the 0.3% vs 95% contrast. Keep energy high -- this is the detective reveal.

*~380 words | 2:32 segment*

---

### [7:00 - 9:00] The Fix: VACUUM, work_mem, shared_buffers

**[SCREEN SHARE: terminal]** -> **[SLIDE: before-after-metrics.png]** at 8:30

**SCRIPT**:

Three targeted fixes. No rewrite, no new hardware.

**Fix one -- immediate. Manual VACUUM ANALYZE.**

```sql
VACUUM (VERBOSE, ANALYZE) orders;
```

Autovacuum had fallen behind. The manual vacuum reclaimed dead tuples. The orders table shrank from 15,000 pages back to about 3,200 -- still larger than the original 857 because of legitimate growth, but no longer bloated with dead rows.

**Fix two -- immediate. SET LOCAL work_mem for the checkout session.**

```sql
BEGIN;
SET LOCAL work_mem = '16MB';
-- checkout query runs here
COMMIT;
```

`SET LOCAL` scopes the change to the current transaction. No risk to other queries. The 16 megabytes eliminated the temp spill entirely. The sort completed in memory.

**Fix three -- configuration. shared_buffers and autovacuum tuning.**

We bumped `shared_buffers` from 2 gigs to 4 gigs. On a 32-gig instance, that is 12.5% of RAM -- well within the recommended 25% guideline. And we tuned autovacuum to keep pace:

```
autovacuum_vacuum_cost_delay = '2ms'    -- down from 20ms
autovacuum_vacuum_scale_factor = 0.05   -- vacuum at 5% dead tuples
```

Then the moment of truth. We re-ran `EXPLAIN (ANALYZE, BUFFERS)` on the checkout query.

`shared hit=3,100, shared read=87`. That is a 97.3% hit ratio. `temp written=0`. Execution time: 42 milliseconds.

**NOTES**: Type each fix live in the terminal. Pause before the verification results for dramatic effect. Deliver "42 milliseconds" slowly with satisfaction. Transition to before-after-metrics.png for the full comparison.

*~250 words | 1:40 segment*

---

### [9:00 - 9:30] Results: Before and After Metrics

**[SLIDE: before-after-metrics.png]**

**SCRIPT**:

Let me put the full picture on screen. Execution time: 1,192 milliseconds down to 42. That is a 96.5% reduction. Buffer hit ratio: 0.3% up to 97.3%. Temp pages spilled: 312 down to zero. Checkout p95: 1,200 milliseconds down to 48.

Cart abandonment recovered to the baseline -- about 70% -- within 48 hours.

One word -- `BUFFERS` -- surfaced the root cause that three days of network debugging, PgBouncer tuning, and cloud provider tickets had missed.

**NOTES**: Let the slide do the work. Read the numbers calmly. Emphasize "one word" at the end.

*~90 words | 0:36 segment*

---

### [9:30 - 10:30] Version Compatibility: PG 8.4 Through PG 18

**[SLIDE: pg-version-timeline.png]**

**SCRIPT**:

Quick version rundown. `EXPLAIN BUFFERS` has been available since PostgreSQL 8.4 -- that is 2009. So everything I showed you works on basically any PostgreSQL version you are running.

But here are the milestones. PG 9.2 added `track_io_timing` so you get actual read and write times in milliseconds. PG 13 started reporting planning buffers -- reads of `pg_class` and `pg_statistic` during plan creation. PG 16 gave us the `pg_stat_io` view for system-wide I/O statistics. PG 17, which our case study ran on, added `pg_buffercache_evict` for controlled cache benchmarking.

And the big one: **PostgreSQL 18**, released in 2025, made `BUFFERS` the default in `EXPLAIN ANALYZE`. You no longer need to remember the flag. Every developer sees buffer statistics whether they ask for them or not.

PG 19, coming later this year, reduces EXPLAIN ANALYZE timing overhead itself, making it practical to run buffer diagnostics on more workloads.

**NOTES**: Point to each milestone on the timeline slide. Emphasize PG 18 as the inflection point. Keep pace brisk -- this is informational, not dramatic.

*~175 words | 1:10 segment*

---

### [10:30 - 12:00] Takeaways and CTA

**[ON CAMERA]**

**SCRIPT**:

Four takeaways.

One: add `BUFFERS` to every `EXPLAIN ANALYZE` you run. If you are on PostgreSQL 18 or later, you already get it. If you are on 17 or earlier, type `EXPLAIN (ANALYZE, BUFFERS)` instead of `EXPLAIN ANALYZE`. Make it muscle memory.

Two: learn the four signals. `hit` is good, `read` is expensive, `dirtied` on SELECTs is normal, `written` on SELECTs is a warning.

Three: bridge single-query diagnostics with workload monitoring. `EXPLAIN BUFFERS` shows you one execution. `pg_stat_statements` shows you the trend across all executions. Use both.

Four: tune autovacuum for your high-write tables. The defaults are conservative. If inserts outpace vacuuming, you get bloat, and bloat kills your cache hit ratio.

Here is what I want you to do right now. Open a terminal, connect to your database, and run `EXPLAIN (ANALYZE, BUFFERS)` on your slowest query. If the hit ratio is below 90% for an OLTP query, you have found your next optimization target. If you see `temp written` on any critical path, that is `work_mem` waiting to be tuned.

Drop a comment below with what you find. I have seen hit ratios as low as 0.1% in production. I want to hear your stories.

If this was useful, hit subscribe. I put out PostgreSQL performance content regularly. Link to the full blog post with all the SQL and configuration details is in the description.

Thanks for watching.

**NOTES**: Direct address to camera. Count off the four takeaways on fingers. Deliver the CTA with energy -- lean forward slightly. End with a nod and natural pause before cut.

*~260 words | 1:44 segment*

---

## Slide Map

| Timestamp | Visual | Filename | Description |
|-----------|--------|----------|-------------|
| 1:15-2:00 | Slide | shared-buffers-flow.png | Data path from query through shared buffer cache to disk; hit/read/dirtied/written labeled |
| 2:00-3:30 | PiP overlay | shared-buffers-flow.png | Reference diagram during buffer concepts explanation |
| 5:00-6:00 | Slide | query-plan-tree.png | EXPLAIN BUFFERS plan tree with I/O stats annotated at each node |
| 6:15-7:00 | Slide | buffer-hit-comparison.png | Side-by-side bars: before (0.3% hit ratio) vs. expected (95%+) |
| 8:30-9:30 | Slide | before-after-metrics.png | Horizontal bars comparing before (red) and after (green) across all metrics |
| 9:30-10:30 | Slide | pg-version-timeline.png | Horizontal timeline PG 8.4 through PG 19 with BUFFERS milestones |

---

## Thumbnail Concepts

### Option 1: "The One-Word Fix"

- **Background**: Split screen -- red (left) with "1.2s" and green (right) with "42ms"
- **Text overlay**: `BUFFERS` in monospace font, centered, large
- **Subtext**: "96% faster" in bold white
- **Face**: Surprised/pointing expression (if using creator's face)

### Option 2: "0.3% Hit Ratio"

- **Background**: Dark terminal screenshot showing EXPLAIN BUFFERS output, slightly blurred
- **Text overlay**: "0.3%" in large red text, arrow pointing down to "97.3%" in green
- **Subtext**: "PostgreSQL EXPLAIN BUFFERS" at top
- **Face**: Optional -- works without face as a data-driven thumbnail

### Option 3: "3 Days Debugging the Wrong Thing"

- **Background**: Gradient dark blue/purple
- **Text overlay**: "3 DAYS" crossed out in red, "5 MINUTES" in green below
- **Subtext**: "PostgreSQL EXPLAIN BUFFERS" at bottom
- **Icon**: Network cable crossed out, database checkmark

---

## YouTube Description

```
PostgreSQL EXPLAIN BUFFERS: How We Cut Checkout Latency 96%

A customer's e-commerce checkout query went from 50ms to 1.2 seconds. The team spent 3 days debugging the network. The real fix? Adding BUFFERS to EXPLAIN ANALYZE.

In this video, I walk through the full investigation: what EXPLAIN BUFFERS reveals, how we diagnosed a 0.3% buffer hit ratio, the three targeted fixes (VACUUM, work_mem, shared_buffers), and the result -- 42ms execution time with a 97.3% hit ratio.

Works on PostgreSQL 8.4+. On PG 18, BUFFERS is now included by default.

TIMESTAMPS
0:00 The 1.2-second checkout incident
0:30 Problem setup: why EXPLAIN ANALYZE wasn't enough
2:00 Concepts: shared buffers, hit ratio, temp spills
4:00 Investigation: EXPLAIN BUFFERS output walkthrough
5:00 Following the buffer trail with pg_stat_statements
7:00 Fix 1: VACUUM ANALYZE
7:30 Fix 2: work_mem tuning with SET LOCAL
8:00 Fix 3: shared_buffers and autovacuum configuration
9:00 Before/after results: 96.5% latency reduction
9:30 PostgreSQL version compatibility (PG 8.4 - PG 19)
10:30 4 takeaways and your next step

LINKS
Blog post (full SQL + config): [LINK]
PostgreSQL EXPLAIN docs: https://www.postgresql.org/docs/current/sql-explain.html
pg_stat_statements: https://www.postgresql.org/docs/current/pgstatstatements.html
auto_explain: https://www.postgresql.org/docs/current/auto-explain.html
boringSQL EXPLAIN BUFFERS reference: https://boringsql.com/posts/explain-buffers/
pev2 visual EXPLAIN analyzer: https://github.com/dalibo/pev2

RESOURCES MENTIONED
- pg_stat_monitor (Percona): https://github.com/percona/pg_stat_monitor
- pganalyze: https://pganalyze.com/

#PostgreSQL #EXPLAIN #BUFFERS #DatabasePerformance #SQL #QueryOptimization #ECommerce #DevOps #Backend #SoftwareEngineering
```

---

## YouTube Tags

1. PostgreSQL EXPLAIN BUFFERS
2. EXPLAIN ANALYZE BUFFERS
3. PostgreSQL performance tuning
4. PostgreSQL slow query
5. buffer cache hit ratio
6. shared_buffers tuning
7. work_mem PostgreSQL
8. VACUUM ANALYZE PostgreSQL
9. pg_stat_statements
10. PostgreSQL 18
11. database performance
12. query optimization
13. e-commerce database
14. PostgreSQL case study
15. auto_explain PostgreSQL

---

## Script Statistics

| Metric | Value |
|--------|-------|
| Total spoken words | ~1,675 |
| Estimated runtime | ~11:10 |
| On-camera segments | 3 (cold open, problem setup, takeaways) |
| Screen share segments | 3 (concepts, investigation, fixes) |
| Slide appearances | 6 |
| Unique PNGs used | 5/5 |
