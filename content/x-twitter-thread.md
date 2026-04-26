# X/Twitter Thread: PostgreSQL EXPLAIN BUFFERS

> **Source**: `content/explain-buffers-blog.md`
> **Generated**: 2026-04-26
> **Platform**: X/Twitter
> **Format**: 12-tweet thread + standalone summary tweet

---

## Standalone Summary Tweet

── START COPY ──

A checkout query went from 50ms to 1.2s. Team blamed the network for 3 days.

Adding 𝗕𝗨𝗙𝗙𝗘𝗥𝗦 to EXPLAIN ANALYZE revealed a 0.3% cache hit ratio. Three config fixes, no code changes: 42ms, 97.3% hit ratio.

One word. 96% faster.

── END COPY ──

> Character count: ~220

---

## Thread (12 Tweets)

### Tweet 1/12 — Hook

── START COPY ──

Most engineers ignore 𝗕𝗨𝗙𝗙𝗘𝗥𝗦 in EXPLAIN output.

That's why their queries are slow.

Same plan. Same index scan. Same joins. But the I/O profile? 𝗖𝗮𝘁𝗮𝘀𝘁𝗿𝗼𝗽𝗵𝗶𝗰𝗮𝗹𝗹𝘆 different.

🧵

── END COPY ──

> Character count: ~175

---

### Tweet 2/12 — Incident Setup

── START COPY ──

A customer's checkout query went from 𝟱𝟬𝗺𝘀 to 𝟭.𝟮 𝘀𝗲𝗰𝗼𝗻𝗱𝘀.

Cart abandonment spiked 12 percentage points. Revenue leaking at ~$5,600/min.

The team ran EXPLAIN ANALYZE for 𝘁𝗵𝗿𝗲𝗲 𝗱𝗮𝘆𝘀. Blamed the network. Tuned PgBouncer. Filed a cloud provider ticket.

Nothing helped.

── END COPY ──

> Character count: ~268

---

### Tweet 3/12 — The Gap

── START COPY ──

EXPLAIN ANALYZE showed the 𝘀𝗮𝗺𝗲 𝗽𝗹𝗮𝗻 every time.

Same Index Scan. Same Nested Loop. Same row estimates.

The plan doesn't show 𝘸𝘩𝘦𝘳𝘦 data comes from -- memory or disk.

Without BUFFERS, the I/O problem was 𝗶𝗻𝘃𝗶𝘀𝗶𝗯𝗹𝗲.

── END COPY ──

> Character count: ~220

---

### Tweet 4/12 — Four Buffer Signals

── START COPY ──

EXPLAIN (ANALYZE, 𝗕𝗨𝗙𝗙𝗘𝗥𝗦) adds four I/O signals:

▸ 𝘀𝗵𝗮𝗿𝗲𝗱 𝗵𝗶𝘁 -- pages in cache (fast)
▸ 𝘀𝗵𝗮𝗿𝗲𝗱 𝗿𝗲𝗮𝗱 -- from disk (slow)
▸ 𝘀𝗵𝗮𝗿𝗲𝗱 𝗱𝗶𝗿𝘁𝗶𝗲𝗱 -- modified pages
▸ 𝘀𝗵𝗮𝗿𝗲𝗱 𝘄𝗿𝗶𝘁𝘁𝗲𝗻 -- sync writes (warning)

Key formula: hit_ratio = hit / (hit + read)

── END COPY ──

> Character count: ~250

---

### Tweet 5/12 — Diagnostic Moment

── START COPY ──

We ran EXPLAIN (ANALYZE, 𝗕𝗨𝗙𝗙𝗘𝗥𝗦).

𝘀𝗵𝗮𝗿𝗲𝗱 𝗵𝗶𝘁=𝟱𝟬, 𝗿𝗲𝗮𝗱=𝟭𝟱,𝟬𝟬𝟬

A 𝟬.𝟯% buffer hit ratio on a query that should be 95%+ cached.

Three days debugging the network. The answer was in the I/O stats the team never asked for.

── END COPY ──

> Character count: ~222

---

### Tweet 6/12 — pg_stat_statements

── START COPY ──

pg_stat_statements confirmed it wasn't a cold-cache fluke.

𝘀𝗵𝗮𝗿𝗲𝗱_𝗯𝗹𝗸𝘀_𝗿𝗲𝗮𝗱 had grown 𝟯𝟬𝘅 over two weeks.
𝘀𝗵𝗮𝗿𝗲𝗱_𝗯𝗹𝗸𝘀_𝗵𝗶𝘁 stayed flat.

The query was consistently reading from disk, execution after execution. Not a one-off -- a trend.

── END COPY ──

> Character count: ~235

---

### Tweet 7/12 — Root Cause

── START COPY ──

Root cause -- three problems compounding:

𝟭. 𝗧𝗮𝗯𝗹𝗲 𝗯𝗹𝗼𝗮𝘁: orders grew from 857 to 15,000 pages. Promo inserts outpaced autovacuum.

𝟮. 𝗨𝗻𝗱𝗲𝗿𝘀𝗶𝘇𝗲𝗱 𝘀𝗵𝗮𝗿𝗲𝗱_𝗯𝘂𝗳𝗳𝗲𝗿𝘀: 2GB couldn't hold the bloated working set.

𝟯. 𝘄𝗼𝗿𝗸_𝗺𝗲𝗺 𝘀𝗽𝗶𝗹𝗹: 256kB forced a 2,500-page sort to disk.

── END COPY ──

> Character count: ~270

---

### Tweet 8/12 — Fix 1

── START COPY ──

𝗙𝗶𝘅 𝟭: VACUUM ANALYZE (immediate)

Manual vacuum reclaimed dead tuples. Orders table shrank from 𝟭𝟱,𝟬𝟬𝟬 pages to 𝟯,𝟮𝟬𝟬.

Autovacuum had fallen behind during the promo surge. One command, 78.7% table size reduction.

── END COPY ──

> Character count: ~218

---

### Tweet 9/12 — Fix 2 + 3

── START COPY ──

𝗙𝗶𝘅 𝟮: SET LOCAL work_mem = '16MB'

Eliminated the 2,500-page temp spill. Sort completed in memory. SET LOCAL scopes it to one transaction -- zero risk to other queries.

𝗙𝗶𝘅 𝟯: shared_buffers 2GB -> 4GB + aggressive autovacuum tuning.

No application code changes.

── END COPY ──

> Character count: ~265

---

### Tweet 10/12 — Before/After Results

── START COPY ──

📊 𝗕𝗲𝗳𝗼𝗿𝗲 𝘃𝘀 𝗔𝗳𝘁𝗲𝗿:

▸ Execution: 1,192ms -> 𝟰𝟮𝗺𝘀 (96.5% faster)
▸ Hit ratio: 0.3% -> 𝟵𝟳.𝟯%
▸ Temp spill: 2,500 pages -> 𝟬
▸ Sync writes: 847 -> 𝟬
▸ Checkout p95: 1,200ms -> 48ms

Cart abandonment recovered to ~70% baseline within 48 hours.

── END COPY ──

> Character count: ~260

---

### Tweet 11/12 — PG 18

── START COPY ──

PostgreSQL 18 now includes 𝗕𝗨𝗙𝗙𝗘𝗥𝗦 by default in EXPLAIN ANALYZE.

Every developer sees hit/read/dirtied/written stats 𝘸𝘪𝘵𝘩𝘰𝘶𝘵 𝘢𝘴𝘬𝘪𝘯𝘨.

On PG 17 or earlier? Just type:
EXPLAIN (ANALYZE, BUFFERS)
instead of EXPLAIN ANALYZE.

That one word changes everything.

── END COPY ──

> Character count: ~265

---

### Tweet 12/12 — CTA

── START COPY ──

One word turned 3 days of debugging into a 5-minute diagnosis.

EXPLAIN (ANALYZE, 𝗕𝗨𝗙𝗙𝗘𝗥𝗦).

Full case study with query plans, pg_stat_statements queries, and monitoring setup:

[blog link]

#PostgreSQL #EXPLAIN

── END COPY ──

> Character count: ~210 (URL counts as 23 chars)

---

## Posting Notes

**Timing**: Tuesday 12:00 PM ET (developer lunch-scroll window)

**Image attachments**:
- Tweet 5 or 10: attach the buffer hit comparison visual (0.3% vs 97.3%)
- Tweet 10: before/after metrics chart works as a standalone image

**Engagement strategy**:
- Quote-tweet the hook (tweet 1) on Day 2 with the before/after visual
- Reply to technical questions with specific pg_stat_statements queries from the blog
- If a tweet gets traction, post the tuning levers table as a follow-up image

**Day 4 follow-up**: Post the standalone summary tweet with a link back to the thread

**Cadence**: Post all 12 tweets in a single thread. Do NOT space them out -- X/Twitter threads perform best as a batch.
