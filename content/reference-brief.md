---
title: Reference Brief — Postgres Ate the Database Market ("Just Use Postgres" thesis)
description: Relevance-ranked, fetch-verified source brief for the DB-1 run. Sources are ranked by how authoritatively each one supports the specific claim it grounds — not by publisher. All vendors and independent writers are treated equally.
author: Shailesh Mishra
ms.date: 2026-06-26
ms.topic: reference
---

# Reference Brief — "Just Use Postgres" (consolidation case + four breakpoints)

> **Source ranking rule.** Every load-bearing number is cited to the best **primary** source
> (whoever built/ran/shipped the thing), backed by independent **measurement** and expert
> **synthesis**. PostgreSQL.org, GitHub project repos, AWS, ScyllaDB, ClickHouse, Vitess,
> Stack Overflow, and DB-Engines are all candidates on the same footing. Every URL below was
> fetched and verified on **2026-06-26**. Numbers tagged `[VOLATILE]` (GitHub stars, version
> numbers, survey percentages, vendor benchmark claims) must be re-pulled by
> `grounded-content-reviewer` before the blog is finalized.

## A. The consolidation case — Postgres core + popularity (the STAR of the post)

| Claim it grounds | Source (primary) | Verified detail | Tag |
|---|---|---|---|
| Postgres is the default database developers reach for | Stack Overflow 2024 Developer Survey — Databases | **PostgreSQL is the most-used database for the 2nd year running at 48.7%** (ahead of MySQL 40.3%, SQLite 33.1%, SQL Server 25.3%, MongoDB 24.8%, Redis 20%). Adoption climbed from **33% (2018) → 48.7% (2024)**. Also **most-admired DB at 47.1%** and **most-desired at 74.5%**. https://survey.stackoverflow.co/2024/technology | T1 measurement `[VOLATILE]` |
| Postgres popularity is still rising, not plateauing | DB-Engines Ranking — Trend of PostgreSQL Popularity (June 2026 snapshot) | The trend chart shows a steady multi-year climb (2014→2026) on a logarithmic score scale; Postgres is the only top-tier conventional RDBMS still trending up. Cite qualitatively (the page is a chart, not a table). https://db-engines.com/en/ranking_trend/system/PostgreSQL | T2 measurement |
| Postgres keeps absorbing serious engineering, fast | PostgreSQL 18 release announcement (2025-09-25) | **Async I/O (AIO) subsystem → up to 3× read throughput**; B-tree **skip scan**; **virtual generated columns**; **UUIDv7** (`uuidv7()`); **OAuth 2.0** auth; temporal constraints (`WITHOUT OVERLAPS`/`PERIOD`); checksums on by default. https://www.postgresql.org/about/news/postgresql-18-released-3142/ | T1 primary |
| The project ships on a predictable cadence | PostgreSQL 19 Beta 1 announcement | **PostgreSQL 19 Beta 1 released 2026-06-04** — annual major-release cadence holds; 19 is in beta as of this run. (linked from the PG18 news page) | T1 primary `[VOLATILE]` |

## B. The five extensions to feature (consolidation surface area)

| Extension (workload it absorbs) | Source (primary repo/docs) | Verified detail | Tag |
|---|---|---|---|
| **pgvector** — vector / similarity search | github.com/pgvector/pgvector | **v0.8.3**, **~21.9k stars**; HNSW + IVFFlat indexes; exact + approximate ANN; half/binary/sparse vectors; up to **2,000 dims** indexed (16,000 via halfvec/binary quantization); **ACID + PITR + JOINs** (the whole point — vectors live next to your relational data); 32 TB non-partitioned table limit. https://github.com/pgvector/pgvector | T1 primary `[VOLATILE]` |
| **TimescaleDB** — time-series / real-time analytics | github.com/timescale/timescaledb | **v2.28.1 (2026-06-23)**, **~23k stars**; hypertables (automatic time partitioning); **columnstore with 90%+ typical compression**; continuous aggregates (incremental materialized views); `time_bucket()`. https://github.com/timescale/timescaledb | T1 primary `[VOLATILE]` |
| **pgmq** — message queue | github.com/pgmq/pgmq | **v1.11.1**, **~5k stars**; "like AWS SQS/RSMQ but on Postgres"; **exactly-once delivery within a visibility timeout**; FIFO + topic routing; no background worker/external deps; **used in production by Supabase and Tembo**; supported on PG 14–18. https://github.com/pgmq/pgmq | T1 primary `[VOLATILE]` |
| **Full-text search** — search engine | PostgreSQL core docs (`tsvector`/`tsquery`, GIN) | Native FTS via `tsvector`/`tsquery` + GIN indexes; PG18 changed FTS to use the cluster default collation provider. Pairs with pgvector for **hybrid search** (BM25-style lexical + semantic, combined via Reciprocal Rank Fusion) — documented in the pgvector README. https://www.postgresql.org/docs/current/textsearch.html | T1 primary |
| **JSONB** — document store | PostgreSQL core (built-in, not an extension) | `jsonb` binary document type with GIN indexing and rich operators — covers the "I need a document DB" case without leaving Postgres. (Core feature; cite core docs.) https://www.postgresql.org/docs/current/datatype-json.html | T1 primary |

> **Framing note for the writer:** the load-bearing fact is not any single star count — it's that
> **one ACID engine now has credible, production-grade answers for vectors, time-series, queues,
> search, and documents simultaneously**, with one backup/replication/permissions story. That
> consolidation (5 systems → 1) is the star of the post. Star counts are color, not the argument.

## C. The four breakpoints — specialist ceilings (the honest caveat)

> These are the credibility-building limits, NOT the focus. Each row is the concrete ceiling that
> makes reaching for a specialist the right call. Vendor benchmark numbers are self-reported —
> cite them as the vendor's own published claim, with the comparison named.
>
> **Azure-native managed options (equal footing).** Because the author works hands-on with Azure,
> each breakpoint also names the Azure managed service a reader on Azure would reach for — presented
> as *one cloud's option among equals* (AWS/GCP/self-hosted are equally valid), never as the default.
> All Azure pages below were fetched and verified **2026-06-26**.

| Breakpoint | Specialist target(s) | Azure-native managed option (equal footing) | Source-verified ceiling that justifies leaving Postgres | Tag |
|---|---|---|---|---|
| **1. Extreme write throughput** | Cassandra / ScyllaDB | **Azure Managed Instance for Apache Cassandra** (fully managed pure open-source Cassandra on VM scale sets; supports Cassandra up to 5.0; hybrid on-prem/cloud rings) · **Azure Cosmos DB** (elastic high-throughput writes) | ScyllaDB's own published benchmark: **sustained 7.5 million inserts/sec at 4 ms P99** (vs Aerospike); claims **2×–5× better throughput than Apache Cassandra**. A single Postgres primary takes all writes through one node — this is the wall. https://www.scylladb.com/product/benchmarks/ · Azure: https://learn.microsoft.com/en-us/azure/managed-instance-apache-cassandra/introduction | T1 vendor-primary `[VOLATILE]` |
| **2. Planet-scale horizontal sharding** | Spanner / CockroachDB / Vitess | **Azure Cosmos DB for NoSQL** (turnkey global distribution, horizontal partitioning, **multi-region writes with automatic failover, 99.999% SLA**) · **Azure Database for PostgreSQL — Elastic Clusters** (Citus-powered transparent horizontal scale-out that *stays Postgres*) | **Vitess served ALL of YouTube's database traffic for 5+ years** and runs in production at **Slack, Square, JD.com**; it exists specifically because **MySQL/Postgres lack native transparent sharding** — you bolt it on. Spanner/CockroachDB are built shard-native with global consistency. https://vitess.io/docs/overview/whatisvitess/ · Azure: https://learn.microsoft.com/en-us/azure/cosmos-db/introduction | T1 primary |
| **3. Sub-millisecond key-value** | Redis / DynamoDB | **Azure Managed Redis** (in-memory, low-latency; the current successor to Azure Cache for Redis, which is on a retirement path) · **Azure Cosmos DB** (**single-digit-millisecond** response times at any scale) | DynamoDB: **single-digit-millisecond performance at any scale**, **½ million+ requests/sec for hundreds of customers**, **200 TB+ tables**, **99.999%** global-table availability. Redis serves from memory in the microsecond–low-ms band. Postgres + connection/transaction overhead can't reach that floor reliably. https://aws.amazon.com/dynamodb/ · Azure: https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview | T1 vendor-primary `[VOLATILE]` |
| **4. True OLAP at petabyte scale** | ClickHouse / Snowflake | **Azure Data Explorer (Kusto)** (fully managed big-data analytics: **ingest terabytes in minutes, query petabytes with results in ms–seconds, millions of events/sec**) · **Microsoft Fabric / Synapse Analytics** (lakehouse + warehouse) | ClickHouse (column-oriented OLAP): a documented query **processed 100 million rows in 92 ms ≈ 1 billion rows/sec, ~7 GB/sec per query**; analytics queries "routinely process billions and trillions of rows." Postgres is row-oriented OLTP — it can do analytics, but not at this scan rate/scale. https://clickhouse.com/docs/en/intro · Azure: https://learn.microsoft.com/en-us/azure/data-explorer/data-explorer-overview | T1 primary `[VOLATILE]` |

> **Azure verified details (fetched 2026-06-26):**
> - **Azure Cosmos DB** — fully managed NoSQL + vector DB; *single-digit-millisecond* response times; turnkey global distribution & **multi-region writes (99.999% SLA) with automatic failover**; instant/elastic autoscale. Microsoft's own example: *"OpenAI relies on Cosmos DB to dynamically scale their ChatGPT service."* Microsoft explicitly positions it as a **poor fit for OLAP** (directs you to Microsoft Fabric) — useful supporting evidence for breakpoint 4. https://learn.microsoft.com/en-us/azure/cosmos-db/introduction
> - **Azure Managed Instance for Apache Cassandra** — managed pure OSS Cassandra (up to 5.0) on VM scale sets; hybrid rings via ExpressRoute. https://learn.microsoft.com/en-us/azure/managed-instance-apache-cassandra/introduction
> - **Azure Data Explorer (Kusto)** — ingest TB in minutes, query **petabytes** in ms–seconds, **millions of events/sec**, linear scale; a cluster holds up to 10,000 DBs. https://learn.microsoft.com/en-us/azure/data-explorer/data-explorer-overview
> - **Azure Managed Redis / Azure Cache for Redis** — in-memory low-latency store; Microsoft now steers new work to **Azure Managed Redis** (Azure Cache for Redis is on a published retirement path). Cite the successor for any forward-looking recommendation. https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview
> - **Sharded Postgres on Azure** — **Azure Database for PostgreSQL Elastic Clusters** is the current Citus-powered horizontal-scale-out option; **Azure Cosmos DB for PostgreSQL is retiring** and should not be cited for new work. https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/introduction

## D. Source Map (best source per load-bearing claim)

| Claim in the post | Best source | Backed by |
|---|---|---|
| "Just use Postgres" is the default, and rising | SO 2024 survey (48.7%, 33%→48.7%) | DB-Engines rising trend |
| Postgres keeps absorbing real engineering | PG18 release (async I/O 3×, skip scan, UUIDv7) | PG19 Beta cadence |
| 5 systems → 1 (vectors/TS/queues/search/docs) | pgvector + TimescaleDB + pgmq repos + core FTS/JSONB docs | "who uses pgmq" (Supabase/Tembo) |
| Breakpoint 1: write throughput wall | ScyllaDB benchmark (7.5M inserts/s) | single-primary write model of Postgres; Azure: Managed Instance for Apache Cassandra / Cosmos DB |
| Breakpoint 2: sharding wall | Vitess (YouTube 5+ yrs) | Spanner/CockroachDB shard-native design; Azure: Cosmos DB for NoSQL / Azure Database for PostgreSQL Elastic Clusters (Citus) |
| Breakpoint 3: sub-ms KV floor | DynamoDB (single-digit ms, ½M+ rps) | Redis in-memory latency; Azure: Azure Managed Redis / Cosmos DB (single-digit ms) |
| Breakpoint 4: petabyte OLAP scan rate | ClickHouse (1B rows/s) | column vs row storage model; Azure: Azure Data Explorer (Kusto) / Microsoft Fabric |

## E. Gaps / flags for grounded review

- **Re-pull before finalizing:** all `[VOLATILE]` rows — GitHub stars (pgvector ~21.9k, Timescale
  ~23k, pgmq ~5k), versions (pgvector 0.8.3, Timescale 2.28.1, pgmq 1.11.1, PG19 beta), SO survey
  %, and the ScyllaDB/DynamoDB vendor benchmark claims. Vendor benchmarks are self-reported; cite
  as "ScyllaDB's published benchmark" / "AWS's stated figures," never as neutral fact.
- **DB-Engines** is a chart page — cite the *trend direction* qualitatively, do not invent a score.
- **Spanner / CockroachDB / Snowflake / Redis / Cassandra**: covered qualitatively via the named
  anchors (Vitess, DynamoDB, ClickHouse, ScyllaDB). If the draft makes a hard numeric claim about
  Spanner, CockroachDB, Snowflake, or Redis specifically, add a first-party citation first.
- **Azure-native options**: cited from official Microsoft Learn product pages (fetched 2026-06-26),
  framed as one cloud's equal-footing option per breakpoint — never the default. Two retirement
  caveats matter for forward-looking wording: **Azure Cache for Redis → Azure Managed Redis**, and
  **Azure Cosmos DB for PostgreSQL → Azure Database for PostgreSQL Elastic Clusters (Citus)**. Cite
  the successor service for any recommendation. Azure latency/throughput phrases ("single-digit
  millisecond," "petabytes in ms–seconds," "millions of events/sec") are Microsoft's own stated
  figures — attribute them as such, not as neutral fact, and re-pull before finalizing.
- **The anecdote** (`[[ANECDOTE: Postgres-consolidation-win]]`) is the author's own first-person
  evidence and is the strongest "primary source" for the consolidation thesis — but it is **not yet
  provided**. It must be filled (sanitized) before the draft is finalized; do not fabricate it.
