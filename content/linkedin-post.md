# LinkedIn Post: PostgreSQL EXPLAIN BUFFERS

> **Topic**: PostgreSQL EXPLAIN BUFFERS case study
> **Blog**: `content/explain-buffers-blog.md`
> **Generated**: 2026-04-26

---

## Version 1: Plain Text

Our checkout query went from 50ms to 1.2 seconds. Cart abandonment spiked 12 percentage points. Revenue leaked at $5,600 per minute.

The engineering team spent three days blaming the network.

They ran EXPLAIN ANALYZE repeatedly. Same Index Scan, same Nested Loop join, same estimated rows. Nothing looked wrong. So they tuned PgBouncer, added read replicas, and opened a cloud provider ticket.

None of it helped.

Then we added one word to the diagnostic command: BUFFERS.

EXPLAIN (ANALYZE, BUFFERS) told the entire story in seconds:

The query was reading 15,000 pages from disk and hitting only 50 pages in cache. A 0.3% buffer hit ratio on what should have been a 95%+ cached query.

Three days of debugging. The answer was right there in the I/O stats they never asked for.

The fix was three targeted changes -- zero application code:

1. VACUUM ANALYZE on the bloated orders table (15,000 pages back to 3,200)
2. work_mem increase from 256kB to 16MB (eliminated a 2,500-page disk spill)
3. shared_buffers from 2GB to 4GB (working set had outgrown the cache)

The results:

Execution time: 1,192ms to 42ms (96.5% reduction)
Buffer hit ratio: 0.3% to 97.3%
Temp pages spilled: 2,500 to 0
Cart abandonment: recovered to baseline within 48 hours

Starting with PostgreSQL 18, BUFFERS is included by default in EXPLAIN ANALYZE. Every developer will see I/O stats automatically. If you are on PG 17 or earlier, you have to ask for it.

Run EXPLAIN (ANALYZE, BUFFERS) on your slowest query today. The plan might look fine. The I/O profile might tell a completely different story.

Full case study with query plans and pg_stat_statements walkthrough: [link]

#PostgreSQL #DatabasePerformance #Engineering #ECommerce #SoftwareEngineering

---

## Version 2: Unicode Formatted (Copy-Paste Ready)

```
── START COPY ──

Our checkout query went from 𝟱𝟬𝗺𝘀 to 𝟭.𝟮 𝘀𝗲𝗰𝗼𝗻𝗱𝘀.
Cart abandonment spiked 𝟭𝟮 percentage points.
Revenue leaked at $𝟱,𝟲𝟬𝟬 per minute.

The engineering team spent three days blaming the network.

━━━

They ran EXPLAIN ANALYZE repeatedly. Same plan, same estimates, same node types. 𝘕𝘰𝘵𝘩𝘪𝘯𝘨 𝘭𝘰𝘰𝘬𝘦𝘥 𝘸𝘳𝘰𝘯𝘨.

So they tuned PgBouncer, added read replicas, opened a cloud provider ticket. None of it helped.

Then we added 𝗼𝗻𝗲 𝘄𝗼𝗿𝗱 to the diagnostic command: 𝗕𝗨𝗙𝗙𝗘𝗥𝗦.

━━━

⚠️ EXPLAIN (ANALYZE, BUFFERS) told the story in seconds:

▸ 𝟭𝟱,𝟬𝟬𝟬 pages read from disk
▸ Only 𝟱𝟬 pages found in cache
▸ A 𝟬.𝟯% buffer hit ratio on a query that should be 𝟵𝟱%+ cached

Three days of debugging. The answer was in the I/O stats 𝘵𝘩𝘦𝘺 𝘯𝘦𝘷𝘦𝘳 𝘢𝘴𝘬𝘦𝘥 𝘧𝘰𝘳.

━━━

📊 𝗧𝗵𝗿𝗲𝗲 𝗳𝗶𝘅𝗲𝘀. 𝗭𝗲𝗿𝗼 𝗰𝗼𝗱𝗲 𝗰𝗵𝗮𝗻𝗴𝗲𝘀.

1. 𝗩𝗔𝗖𝗨𝗨𝗠 𝗔𝗡𝗔𝗟𝗬𝗭𝗘 -- bloated table from 15,000 pages back to 3,200
2. 𝘄𝗼𝗿𝗸_𝗺𝗲𝗺 256kB -> 16MB -- eliminated a 2,500-page disk spill
3. 𝘀𝗵𝗮𝗿𝗲𝗱_𝗯𝘂𝗳𝗳𝗲𝗿𝘀 2GB -> 4GB -- working set had outgrown the cache

━━━

🎯 𝗥𝗲𝘀𝘂𝗹𝘁𝘀:

▸ Execution time: 𝟭,𝟭𝟵𝟮𝗺𝘀 -> 𝟰𝟮𝗺𝘀 (96.5% reduction)
▸ Buffer hit ratio: 𝟬.𝟯% -> 𝟵𝟳.𝟯%
▸ Temp pages spilled: 2,500 -> 𝟬
▸ Cart abandonment: recovered to baseline in 48 hours

PostgreSQL 18 now includes BUFFERS by default in EXPLAIN ANALYZE. 𝘌𝘷𝘦𝘳𝘺 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 𝘸𝘪𝘭𝘭 𝘴𝘦𝘦 𝘐/𝘖 𝘴𝘵𝘢𝘵𝘴 𝘢𝘶𝘵𝘰𝘮𝘢𝘵𝘪𝘤𝘢𝘭𝘭𝘺.

If you are on PG 17 or earlier -- 𝗿𝘂𝗻 𝗘𝗫𝗣𝗟𝗔𝗜𝗡 (𝗔𝗡𝗔𝗟𝗬𝗭𝗘, 𝗕𝗨𝗙𝗙𝗘𝗥𝗦) 𝗼𝗻 𝘆𝗼𝘂𝗿 𝘀𝗹𝗼𝘄𝗲𝘀𝘁 𝗾𝘂𝗲𝗿𝘆 𝘁𝗼𝗱𝗮𝘆.

The plan might look fine. The I/O profile might tell a completely different story.

Full case study with query plans and monitoring setup: [link]

#PostgreSQL #DatabasePerformance #Engineering #ECommerce #SoftwareEngineering

── END COPY ──
```
