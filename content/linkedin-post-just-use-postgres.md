# LinkedIn Post — "When Not to Use Postgres: A Decision Framework for the Four Walls Where One Engine Isn't Enough"

**Source blog:** [content/just-use-postgres.md](just-use-postgres.md)
**Canonical URL:** _(placeholder — replace with the GitHub Pages URL once published, then move it into the FIRST COMMENT)_

## Recommended image attachment order

1. **Lead image:** `content/visuals/db1-five-to-one-consolidation-hero.svg` — the 5→1 consolidation star (five datastores collapsing into one Postgres elephant). This is what the reader sees first, so the hook narrates it.
2. **Second image:** `content/visuals/db1-four-breakpoints-panel.png` — the four breakpoints panel, one ceiling number per card.

> Export the SVG hero to PNG (1080×1080 or 1200×1200) before upload if LinkedIn rejects the SVG. Post the two images as a multi-image post (hero first).

---

═══════════════════════════════
**START COPY (Plain Text)**
═══════════════════════════════

That diagram shows five datastores becoming one. That actually happened.

Across years of working with customers, I've watched team after team hit the same knot. One sticks with me: Postgres for the relational core, a standalone Redis for the hot path, Elasticsearch for search, a separate message queue for background jobs, and a cron service for scheduled work. Five backup stories. Five things to monitor, patch, and get paged about at 2 a.m. We collapsed all of it into one Postgres — and the cloud bill went down, because we stopped paying for four managed services.

That pattern — repeated across enough customers that I now expect it — made me a believer. It also taught me exactly where the belief stops.

"Just use Postgres" stopped being a meme and became the measured default:

- Most-used database two years running — 48.7%, up from 33% in 2018 (Stack Overflow 2024)
- Most-admired (47.1%) AND most-desired (74.5%) — the one people use and want to use next
- pgvector puts similarity search NEXT TO your relational rows — ACID, JOINs, point-in-time recovery, no second system to sync
- pgmq commits the job and the data in the SAME transaction — the "row saved but the job never fired" bug becomes impossible
- TimescaleDB hypertables hit 90%+ compression for metrics and events
- tsvector + JSONB cover real lexical search and queryable documents — no search cluster, no document database

Five systems to one is not a tidiness win. It is one backup to test, one failover to rehearse, one security model to audit, one on-call rotation, one set of skills to hire for. Every datastore you DON'T add is a category of incident you will never have.

Believer, not zealot. Four walls where I still reach for a specialist on purpose:

1. Extreme write throughput — ScyllaDB / Cassandra. One Postgres primary funnels every write through one node. ScyllaDB publishes 7.5M inserts/sec at 4 ms P99.
2. Planet-scale horizontal sharding — Vitess / Spanner / CockroachDB. Vitess ran ALL of YouTube's database traffic for 5+ years.
3. Sub-millisecond key-value at scale — Redis / DynamoDB. Single-digit-ms floor, 500k+ req/s, 99.999% availability.
4. True OLAP at petabyte scale — ClickHouse / Snowflake. ~1 billion rows/sec scan rate that a row store cannot match.

These are legitimate, correct choices for their case — open-source, AWS, GCP, Azure, or self-hosted are all equal-footing paths. The point is knowing WHICH wall, WITH a number.

So here is the whole decision in one rule:

Default to Postgres. When you hit a wall, name it with a number — write rate, shard count, latency floor, scan size. If you can't name the number, you don't have the wall yet — you have an itch to add a system.

This default keeps getting stronger, not weaker. Postgres 18 shipped async I/O for up to 3× read throughput; 19 is already in beta. The engine is improving at exactly the workloads that used to push you off it.

If you lead one of these teams, here's the rule I hand you. Make Postgres the default of record — new workloads land there unless a named wall is proven. Force every proposal for a new datastore to name its wall AND the number behind it. Price the operational tax — a specialist has to beat Postgres by enough to pay for its own backup, failover, and on-call overhead. And before you greenlight, spend a week proving the consolidation cheaply.

Run the one-line audit this week: for every datastore beyond Postgres, can your team name the wall it clears and the number? The ones that can't are consolidation candidates.

Which of the four walls have you actually hit — and what was the number? Full write-up and the decision framework in the first comment.

#PostgreSQL #Databases #SoftwareArchitecture #PlatformEngineering #DataEngineering

═══════════════════════════════
**END COPY**
═══════════════════════════════


═══════════════════════════════
**UNICODE VERSION**
═══════════════════════════════

═══════════════════════════════
**START COPY (Unicode Formatted)**
═══════════════════════════════

𝗧𝗵𝗮𝘁 𝗱𝗶𝗮𝗴𝗿𝗮𝗺 𝘀𝗵𝗼𝘄𝘀 𝗳𝗶𝘃𝗲 𝗱𝗮𝘁𝗮𝘀𝘁𝗼𝗿𝗲𝘀 𝗯𝗲𝗰𝗼𝗺𝗶𝗻𝗴 𝗼𝗻𝗲. That actually happened.

Across years of working with customers, I've watched team after team hit the same knot. One sticks with me: Postgres for the relational core, a standalone Redis for the hot path, Elasticsearch for search, a separate message queue for background jobs, and a cron service for scheduled work. Five backup stories. Five things to monitor, patch, and get paged about at 2 a.m. We collapsed all of it into one Postgres — and the cloud bill went down, because we stopped paying for four managed services.

That pattern — repeated across enough customers that I now expect it — made me a 𝘣𝘦𝘭𝘪𝘦𝘷𝘦𝘳. It also taught me exactly where the belief stops.

▸ 𝗪𝗵𝘆 "𝗷𝘂𝘀𝘁 𝘂𝘀𝗲 𝗣𝗼𝘀𝘁𝗴𝗿𝗲𝘀" 𝗶𝘀 𝘁𝗵𝗲 𝗺𝗲𝗮𝘀𝘂𝗿𝗲𝗱 𝗱𝗲𝗳𝗮𝘂𝗹𝘁 📊

 • 𝗽𝗴𝘃𝗲𝗰𝘁𝗼𝗿 puts similarity search 𝘯𝘦𝘹𝘵 𝘵𝘰 your relational rows — ACID, JOINs, PITR, no second system to sync
 • 𝗽𝗴𝗺𝗾 commits the job and the data in the 𝘴𝘢𝘮𝘦 transaction — "row saved but the job never fired" becomes impossible
 • 𝗧𝗶𝗺𝗲𝘀𝗰𝗮𝗹𝗲𝗗𝗕 hypertables hit 90%+ compression for metrics and events
 • 𝘁𝘀𝘃𝗲𝗰𝘁𝗼𝗿 + 𝗝𝗦𝗢𝗡𝗕 cover real lexical search and queryable documents — no search cluster, no document DB

▸ 𝗧𝗵𝗲 𝗰𝗼𝗻𝘀𝗼𝗹𝗶𝗱𝗮𝘁𝗶𝗼𝗻 𝗱𝗶𝘃𝗶𝗱𝗲𝗻𝗱 🧮

Five systems to one is not a tidiness win. It is 𝗼𝗻𝗲 𝗯𝗮𝗰𝗸𝘂𝗽 𝘁𝗼 𝘁𝗲𝘀𝘁, 𝗼𝗻𝗲 𝗳𝗮𝗶𝗹𝗼𝘃𝗲𝗿 𝘁𝗼 𝗿𝗲𝗵𝗲𝗮𝗿𝘀𝗲, 𝗼𝗻𝗲 𝘀𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝗺𝗼𝗱𝗲𝗹 𝘁𝗼 𝗮𝘂𝗱𝗶𝘁, 𝗼𝗻𝗲 𝗼𝗻-𝗰𝗮𝗹𝗹 𝗿𝗼𝘁𝗮𝘁𝗶𝗼𝗻. Every datastore you 𝘥𝘰𝘯'𝘵 add is a category of incident you will never have.

▸ 𝗪𝗵𝗲𝗿𝗲 𝘁𝗵𝗲 𝗯𝗲𝗹𝗶𝗲𝗳 𝘀𝘁𝗼𝗽𝘀 — 𝘁𝗵𝗲 𝗳𝗼𝘂𝗿 𝘄𝗮𝗹𝗹𝘀 🧱

Believer, not zealot. Four walls where I still reach for a specialist on purpose:

 𝟭. 𝗘𝘅𝘁𝗿𝗲𝗺𝗲 𝘄𝗿𝗶𝘁𝗲 𝘁𝗵𝗿𝗼𝘂𝗴𝗵𝗽𝘂𝘁 → ScyllaDB / Cassandra. One Postgres primary funnels every write through one node. ScyllaDB publishes 𝟳.𝟱𝗠 𝗶𝗻𝘀𝗲𝗿𝘁𝘀/𝘀𝗲𝗰 𝗮𝘁 𝟰 𝗺𝘀 𝗣𝟵𝟵.
 𝟮. 𝗣𝗹𝗮𝗻𝗲𝘁-𝘀𝗰𝗮𝗹𝗲 𝗵𝗼𝗿𝗶𝘇𝗼𝗻𝘁𝗮𝗹 𝘀𝗵𝗮𝗿𝗱𝗶𝗻𝗴 → Vitess / Spanner / CockroachDB. Vitess ran 𝗮𝗹𝗹 of YouTube's database traffic for 5+ years.
 𝟯. 𝗦𝘂𝗯-𝗺𝗶𝗹𝗹𝗶𝘀𝗲𝗰𝗼𝗻𝗱 𝗸𝗲𝘆-𝘃𝗮𝗹𝘂𝗲 𝗮𝘁 𝘀𝗰𝗮𝗹𝗲 → Redis / DynamoDB. Single-digit-ms floor, 𝟱𝟬𝟬𝗸+ 𝗿𝗲𝗾/𝘀, 99.999% availability.
 𝟰. 𝗧𝗿𝘂𝗲 𝗢𝗟𝗔𝗣 𝗮𝘁 𝗽𝗲𝘁𝗮𝗯𝘆𝘁𝗲 𝘀𝗰𝗮𝗹𝗲 → ClickHouse / Snowflake. ~𝟭 𝗯𝗶𝗹𝗹𝗶𝗼𝗻 𝗿𝗼𝘄𝘀/𝘀𝗲𝗰 scan rate a row store cannot match.

These are legitimate, correct choices — open-source, AWS, GCP, Azure, or self-hosted are all 𝘦𝘲𝘶𝘢𝘭-𝘧𝘰𝘰𝘵𝘪𝘯𝘨 paths. The point is knowing 𝘸𝘩𝘪𝘤𝘩 wall, 𝘸𝘪𝘵𝘩 a number.

▸ 𝗧𝗵𝗲 𝗱𝗲𝗰𝗶𝘀𝗶𝗼𝗻 𝗿𝘂𝗹𝗲 🎯

𝗗𝗲𝗳𝗮𝘂𝗹𝘁 𝘁𝗼 𝗣𝗼𝘀𝘁𝗴𝗿𝗲𝘀. When you hit a wall, name it with a number — write rate, shard count, latency floor, scan size. 𝗜𝗳 𝘆𝗼𝘂 𝗰𝗮𝗻'𝘁 𝗻𝗮𝗺𝗲 𝘁𝗵𝗲 𝗻𝘂𝗺𝗯𝗲𝗿, 𝘆𝗼𝘂 𝗱𝗼𝗻'𝘁 𝗵𝗮𝘃𝗲 𝘁𝗵𝗲 𝘄𝗮𝗹𝗹 𝘆𝗲𝘁 — you have an itch to add a system.

▸ 𝗧𝗵𝗶𝘀 𝗱𝗲𝗳𝗮𝘂𝗹𝘁 𝗸𝗲𝗲𝗽𝘀 𝗴𝗲𝘁𝘁𝗶𝗻𝗴 𝘀𝘁𝗿𝗼𝗻𝗴𝗲𝗿 ⏱️

Postgres 18 shipped async I/O for up to 3× read throughput; 19 is already in beta. The engine is improving at exactly the workloads that used to push you off it.

▸ �𝗵𝗲 𝗳𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸 𝗳𝗼𝗿 𝗱𝗲𝗰𝗶𝗱𝗶𝗻𝗴 🧭

If you lead one of these teams, here's the rule I hand you:
 • 𝗠𝗮𝗸𝗲 𝗣𝗼𝘀𝘁𝗴𝗿𝗲𝘀 𝘁𝗵𝗲 𝗱𝗲𝗳𝗮𝘂𝗹𝘁 𝗼𝗳 𝗿𝗲𝗰𝗼𝗿𝗱 — new workloads land there unless a named wall is proven.
 • 𝗗𝗲𝗺𝗮𝗻𝗱 𝗮 𝗻𝘂𝗺𝗯𝗲𝗿 — every proposal for a new datastore must name its wall and the threshold behind it.
 • 𝗣𝗿𝗶𝗰𝗲 𝘁𝗵𝗲 𝗼𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝘁𝗮𝘅 — a specialist must beat Postgres by enough to pay for its own backup, failover, and on-call overhead.
 • 𝗣𝗿𝗼𝘃𝗲 𝗶𝘁 𝗰𝗵𝗲𝗮𝗽𝗹𝘆 — spend a week consolidating one workload before you buy.

Run the one-line audit this week: for every datastore beyond Postgres, can your team name the wall and the number? The ones that can't are consolidation candidates.

Which of the four walls have you actually hit — and what was the number? Full write-up and the decision framework in the first comment. 👇

#PostgreSQL #Databases #SoftwareArchitecture #PlatformEngineering #DataEngineering

═══════════════════════════════
**END COPY**
═══════════════════════════════


═══════════════════════════════
**FIRST COMMENT COPY**
═══════════════════════════════

Full breakdown — the consolidation case, the four breakpoints with their numbers, and the default-to-Postgres decision framework: https://sendtoshailesh.github.io/content-creation/blog/just-use-postgres.html

#PostgreSQL #PlatformEngineering

═══════════════════════════════
**END FIRST COMMENT COPY**
═══════════════════════════════

Post the FIRST COMMENT within 60 seconds of publishing (link-in-body = reach penalty on LinkedIn).

IMAGE UPLOAD (multi-image post, hero first):
1. content/visuals/db1-five-to-one-consolidation-hero.svg — lead image (5→1 consolidation star)
2. content/visuals/db1-four-breakpoints-panel.png — second image (four ceiling numbers)
