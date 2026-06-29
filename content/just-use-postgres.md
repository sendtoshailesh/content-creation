---
title: 'Just Use Postgres — Until You Hit One of These Four Walls'
description: One ACID engine now absorbs vectors, time-series, queues, search, and documents. Here is the consolidation case for defaulting to Postgres — and the four specific walls where I still reach for a specialist.
author: Shailesh Mishra
ms.date: 2026-06-26
ms.topic: conceptual
---

# Just Use Postgres — Until You Hit One of These Four Walls

A team I worked with was running five moving parts to serve one product: Postgres for the
relational core, a standalone Redis for the hot path, Elasticsearch for search, a separate message
queue for background jobs, and a cron service to fire the scheduled work. Five datastores. Five
backup stories. Five things to monitor, patch, secure, and get paged about at 2 a.m.

We collapsed all of it into one Postgres.

Elasticsearch split into Postgres full-text search (`tsvector`) for lexical queries and
[pgvector](https://github.com/pgvector/pgvector) for semantic search. The message queue moved into
a Postgres-native queue. The cron service became `pg_cron`. Redis's hot path folded back into the
database it was caching in the first place. Five systems became one. The cloud bill went down,
because we stopped paying for four managed services — and, quietly, the architecture diagram
stopped being something you needed a meeting to explain.

That experience made me a believer. It also taught me exactly where the belief stops.

## "Just use Postgres" stopped being a meme

For years, "just use Postgres" was a half-joke developers told each other to push back on
résumé-driven database sprawl. It is not a joke anymore. It is the measured default.

In the [Stack Overflow 2024 Developer Survey](https://survey.stackoverflow.co/2024/technology),
PostgreSQL is the most-used database for the second year running at **48.7%** — ahead of MySQL
(40.3%), SQLite (33.1%), SQL Server (25.3%), and MongoDB (24.8%). That share climbed from **33% in
2018 to 48.7% in 2024**. It is also the **most-admired** database at 47.1% and the **most-desired**
at 74.5% — the database people use *and* the one they want to use next. The
[DB-Engines popularity trend](https://db-engines.com/en/ranking_trend/system/PostgreSQL) tells the
same story over a longer window: a steady multi-year climb while most conventional relational
engines flatten out.

And this is not nostalgia carrying an old engine. Postgres keeps absorbing serious systems work.
[PostgreSQL 18](https://www.postgresql.org/about/news/postgresql-18-released-3142/) (September 2025)
shipped an asynchronous I/O subsystem that delivers **up to 3× read throughput**, plus B-tree skip
scan, virtual generated columns, native `uuidv7()`, and OAuth 2.0 authentication. PostgreSQL 19 is
already in beta. The engine is getting *better* at precisely the workloads that used to push you off
it.

## The consolidation case: five systems, one engine

Here is the thesis in one line: most teams reaching for a second, third, or fourth datastore are
solving a problem Postgres can already handle — and they are buying an operational tax to do it.

![Five labeled workload boxes — vectors, queues, time-series, search, documents — converging into a single Postgres engine, each tagged with the extension that absorbs it: pgvector, pgmq, TimescaleDB, full-text, JSONB.](visuals/db1-five-to-one-consolidation-hero.svg)

*Five workloads, one engine — each specialist replaced by a Postgres extension.*

Walk the five workloads people most often spin up a separate system for, and look at the Postgres
answer and the operational consequence of *not* adding that system.

**Vectors → pgvector.** The moment you build anything with embeddings, the reflex is to stand up a
dedicated vector database and a sync pipeline to keep it aligned with your source-of-truth tables.
[pgvector](https://github.com/pgvector/pgvector) puts similarity search *next to* your relational
data: HNSW and IVFFlat indexes, exact and approximate nearest-neighbor, and — the part that matters
— full ACID transactions, JOINs, and point-in-time recovery. Your embeddings are backed up,
access-controlled, and consistent with the rows they describe, with no second system to keep in sync.

**Time-series → TimescaleDB.** Metrics, events, and IoT readings are the classic "you need a
purpose-built time-series database" case. [TimescaleDB](https://github.com/timescale/timescaledb)
turns a Postgres table into a hypertable with automatic time partitioning, a columnstore that
routinely hits **90%+ compression**, and continuous aggregates that maintain rollups incrementally.
You get time-series ergonomics without a second database to operate.

**Queues → pgmq.** Background jobs usually mean a broker — SQS, RabbitMQ, or Redis with a queueing
layer bolted on. [pgmq](https://github.com/pgmq/pgmq) gives you an SQS-style queue inside Postgres
with **exactly-once delivery within a visibility timeout**, no background worker and no external
dependency — and it is already run in production by teams like Supabase and Tembo. The decisive
detail: your job and the data it touches commit in the *same transaction*. No more "the row saved
but the job never fired" class of bug.

**Search → full-text (`tsvector` + GIN).** Real lexical search — ranking, stemming, phrase queries —
runs natively through [Postgres full-text search](https://www.postgresql.org/docs/current/textsearch.html)
with GIN indexes, no search cluster to provision. Pair it with pgvector and you get hybrid search:
lexical and semantic results fused with Reciprocal Rank Fusion, the pattern people reach for a
dedicated search platform to get.

**Documents → JSONB.** "We need a document database" almost always means "we need flexible,
queryable, indexed JSON." [Postgres `jsonb`](https://www.postgresql.org/docs/current/datatype-json.html)
is a binary document type with GIN indexing and a rich operator set — schemaless where you want it,
relational where you need it, in one engine.

![Five duplicated operational stacks — backup, HA/failover, security model, on-call, skills to hire — collapsing from five copies down to one of each.](visuals/db1-one-engine-one-story-ops.png)

*The consolidation dividend: one backup, one failover, one security model, one on-call rotation.*

Now the part that actually matters to whoever owns the budget and the pager. Five systems → one is
not a tidiness win. It is **one backup to test, one failover to rehearse, one security model to
audit, one on-call rotation, and one set of skills to hire for.** Every datastore you *don't* add is
a category of incident you will never have, a sync pipeline you will never debug, and a vendor
invoice you will never receive. That is the consolidation dividend, and it is why I default to
Postgres.

## Where the belief stops: the four breakpoints

Believer, not zealot. There are four walls where I reach for a specialist on purpose — not because
Postgres "failed," but because the workload genuinely lives outside what one ACID engine on one
primary node can do. If you cannot name which of these four you are hitting, you do not have one
yet.

![Four red-walled cards, each showing one ceiling number and the specialist it justifies: 7.5M inserts/sec at 4 ms P99 (ScyllaDB), all of YouTube for 5+ years (Vitess), single-digit-ms at 500k+ req/s and 99.999% (DynamoDB), ~1 billion rows/sec (ClickHouse).](visuals/db1-four-breakpoints-panel.png)

*The four walls — each named with the number that justifies a specialist.*

**1. Extreme write throughput → Cassandra / ScyllaDB.** A single Postgres primary funnels all writes
through one node. When sustained ingest is the whole game, that is the wall.
[ScyllaDB's published benchmark](https://www.scylladb.com/product/benchmarks/) claims a sustained
**7.5 million inserts/sec at 4 ms P99** and **2×–5× the throughput of Apache Cassandra** (ScyllaDB's
own figures, against Aerospike). *If you are on Azure*, the equal-footing managed option is
[Azure Managed Instance for Apache Cassandra](https://learn.microsoft.com/en-us/azure/managed-instance-apache-cassandra/introduction)
or [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction) — one cloud's
options among equals alongside the open-source and AWS/GCP paths.

**2. Planet-scale horizontal sharding → Spanner / CockroachDB / Vitess.** Postgres has no
transparent native sharding; you bolt it on. [Vitess](https://vitess.io/docs/overview/whatisvitess/)
exists precisely because MySQL and Postgres lack it — and it served **all of YouTube's database
traffic for more than five years**, and runs at Slack, Square, and JD.com. Spanner and CockroachDB
are built shard-native with global consistency from the ground up. *On Azure*, the equal options are
[Azure Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)
(turnkey global distribution, multi-region writes, 99.999% SLA) or
[Azure Database for PostgreSQL Elastic Clusters](https://learn.microsoft.com/en-us/azure/postgresql/elastic-clusters/concepts-elastic-clusters),
the Citus-powered horizontal scale-out that lets you *stay* Postgres.

**3. Sub-millisecond key-value → Redis / DynamoDB.** When you need a single-digit-millisecond floor
under heavy concurrency, connection and transaction overhead make Postgres the wrong tool.
[DynamoDB](https://aws.amazon.com/dynamodb/) advertises single-digit-millisecond performance at any
scale, 500,000+ requests/sec, 200 TB+ tables, and 99.999% availability (AWS's stated figures); Redis
serves from memory in the microsecond-to-low-millisecond band. *On Azure*, the equal options are
[Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview)
(the current successor to Azure Cache for Redis) or Cosmos DB.

**4. True OLAP at petabyte scale → ClickHouse / Snowflake.** Postgres is a row-oriented OLTP engine.
It can run analytics, but it cannot match a column store's scan rate.
[ClickHouse](https://clickhouse.com/docs/en/intro) documents a query processing **100 million rows
in 92 ms — roughly a billion rows/sec at about 7 GB/sec** — and routinely scans billions to
trillions of rows. *On Azure*, the equal options are
[Azure Data Explorer (Kusto)](https://learn.microsoft.com/en-us/azure/data-explorer/data-explorer-overview)
or Microsoft Fabric. (Tellingly, Microsoft's own Cosmos DB docs point you *away* from OLTP engines
and toward Fabric for petabyte analytics — the breakpoint is real across vendors.)

These are legitimate, correct choices for their case. Knowing exactly where the wall is — with a
number attached — is what makes "just use Postgres" a real engineering position instead of a slogan.

## The decision rule

![Decision strip: default to Postgres, then ask whether you are hitting one of the four walls with a number attached — if yes, specialize and name the wall; if no, just use Postgres.](visuals/db1-decision-rule-strip.svg)

*The whole decision in one rule: name the wall with a number, or default to Postgres.*

Default to Postgres. Reach for a specialist only when you can name which of the four walls you are
hitting and put a number on it: the write rate, the shard count, the latency floor, the scan size.
If you cannot name the wall with a number, you have not hit one — you have an itch to add a system.
And every system you do not add is a backup, a failover, and an on-call rotation you do not run.

## Build it yourself

The fastest way to internalize the consolidation thesis is to collapse one system yourself. Three
projects, scaling up — each one grounded in a real, open-source extension you can run today.

### Project 1 (beginner) — Semantic search over your own docs with pgvector

- **Goal:** Add semantic search to an existing Postgres table without standing up a vector database.
- **Prerequisites:** Postgres 14+, the [pgvector](https://github.com/pgvector/pgvector) extension, and
  any embedding model you can call (a local model or a hosted embeddings API).
- **Steps:**
  1. `CREATE EXTENSION vector;` and add an `embedding vector(N)` column to a table of text rows.
  2. Backfill embeddings for each row with your model of choice.
  3. Build an HNSW index: `CREATE INDEX ON docs USING hnsw (embedding vector_cosine_ops);`
  4. Query the nearest neighbors of a new embedding with the `<=>` cosine-distance operator.
- **Success signal:** A top-k similarity query returns ranked rows in **under 50 ms** on a
  10k-row table, and the results are obviously more relevant than a `LIKE '%term%'` scan.
- **Time:** ~1–2 hours.
- **Stretch goal:** Add `tsvector` full-text search to the same table and fuse the two result sets
  with Reciprocal Rank Fusion for true hybrid search — all in one query.

### Project 2 (intermediate) — Replace a Redis-backed job queue with pgmq + pg_cron

- **Goal:** Run background jobs transactionally inside Postgres, with no broker and no cron service.
- **Prerequisites:** Postgres 14+, the [pgmq](https://github.com/pgmq/pgmq) extension, and
  [pg_cron](https://github.com/citusdata/pg_cron).
- **Steps:**
  1. `CREATE EXTENSION pgmq;` then `SELECT pgmq.create('jobs');`
  2. In your application, enqueue work with `pgmq.send()` **inside the same transaction** that writes
     the business row, so the job and the data commit or roll back together.
  3. Write a consumer that reads with `pgmq.read()` (visibility timeout) and deletes on success.
  4. Schedule the consumer with `pg_cron` so it runs on a fixed interval — no external scheduler.
- **Success signal:** Force a failure between the data write and the enqueue; confirm that **neither**
  is committed (the "saved-but-never-fired" bug is now structurally impossible).
- **Time:** ~half a day.
- **Stretch goal:** Add a dead-letter queue and a retry counter, and chart queue depth over time.

### Project 3 (advanced) — Collapse a three-service stack into one Postgres

- **Goal:** Take a service that uses Postgres + a search engine + a time-series store and reduce it
  to a single Postgres instance — the consolidation capstone.
- **Prerequisites:** Postgres 14+, [pgvector](https://github.com/pgvector/pgvector),
  [TimescaleDB](https://github.com/timescale/timescaledb), and a representative slice of real data.
- **Steps:**
  1. Move lexical + semantic search into Postgres (Project 1's hybrid query) and retire the search
     engine.
  2. Convert your metrics/events table into a TimescaleDB hypertable, enable the columnstore, and
     define a continuous aggregate to replace the time-series store.
  3. Point the application at one connection string. Delete the other two services from your infra
     code.
  4. Run your existing integration test suite against the consolidated stack.
- **Success signal:** The full test suite passes against **one** datastore, search relevance is at
  or above the old engine on a held-out query set, and your infra diff shows **two services removed**.
- **Time:** ~2–4 days depending on data volume.
- **Stretch goal:** Write a one-page before/after that quantifies the win — services removed, monthly
  cost delta, and the number of backup/failover/on-call procedures eliminated.

## Before you add the sixth datastore

Pick the smallest version of the consolidation and do it this week: add pgvector to a table you
already own (Project 1) and feel how much simpler "next to the data" is than "synced from the data."

Then ask the only question that matters before adding any new system: **which of the four walls am I
actually hitting, and what is the number?** If you can name it, specialize with confidence. If you
cannot — just use Postgres. Tell me the consolidation (or specialization) call you made, and which
wall forced your hand.

## References

| # | Claim | Source |
|---|-------|--------|
| 1 | Postgres most-used DB 48.7% (2nd yr); 33%→48.7% since 2018; 47.1% admired; 74.5% desired | [Stack Overflow 2024 Developer Survey](https://survey.stackoverflow.co/2024/technology) |
| 2 | Postgres popularity trending up over a multi-year window | [DB-Engines trend](https://db-engines.com/en/ranking_trend/system/PostgreSQL) |
| 3 | PG18 async I/O up to 3× read throughput; skip scan; UUIDv7; OAuth 2.0 | [PostgreSQL 18 release](https://www.postgresql.org/about/news/postgresql-18-released-3142/) |
| 4 | pgvector — HNSW/IVFFlat ANN, ACID, JOINs, PITR | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) |
| 5 | TimescaleDB — hypertables, 90%+ columnstore compression, continuous aggregates | [github.com/timescale/timescaledb](https://github.com/timescale/timescaledb) |
| 6 | pgmq — exactly-once within visibility timeout; used by Supabase/Tembo | [github.com/pgmq/pgmq](https://github.com/pgmq/pgmq) |
| 7 | Postgres full-text search (`tsvector` + GIN) | [PostgreSQL FTS docs](https://www.postgresql.org/docs/current/textsearch.html) |
| 8 | Postgres `jsonb` document type + GIN indexing | [PostgreSQL JSON docs](https://www.postgresql.org/docs/current/datatype-json.html) |
| 9 | pg_cron — in-database job scheduling | [github.com/citusdata/pg_cron](https://github.com/citusdata/pg_cron) |
| 10 | ScyllaDB 7.5M inserts/s @ 4 ms P99; 2–5× Cassandra (vendor figures) | [ScyllaDB benchmarks](https://www.scylladb.com/product/benchmarks/) |
| 11 | Vitess ran all of YouTube's DB traffic 5+ yrs; Slack/Square/JD.com | [vitess.io](https://vitess.io/docs/overview/whatisvitess/) |
| 12 | DynamoDB single-digit ms, 500k+ req/s, 200 TB+, 99.999% (AWS figures) | [aws.amazon.com/dynamodb](https://aws.amazon.com/dynamodb/) |
| 13 | ClickHouse ~1B rows/s (100M rows in 92 ms), ~7 GB/s | [clickhouse.com/docs](https://clickhouse.com/docs/en/intro) |
| 14 | Azure Managed Instance for Apache Cassandra (managed OSS Cassandra) | [Microsoft Learn](https://learn.microsoft.com/en-us/azure/managed-instance-apache-cassandra/introduction) |
| 15 | Azure Cosmos DB (global distribution, single-digit ms, 99.999%) | [Microsoft Learn](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction) |
| 16 | Azure Database for PostgreSQL Elastic Clusters (Citus sharding) | [Microsoft Learn](https://learn.microsoft.com/en-us/azure/postgresql/elastic-clusters/concepts-elastic-clusters) |
| 17 | Azure Managed Redis (successor to Azure Cache for Redis) | [Microsoft Learn](https://learn.microsoft.com/en-us/azure/redis/overview) |
| 18 | Azure Data Explorer (Kusto) — petabyte OLAP, ms–sec queries | [Microsoft Learn](https://learn.microsoft.com/en-us/azure/data-explorer/data-explorer-overview) |

> Figures marked vendor/self-reported (Stack Overflow survey %, GitHub stars, ScyllaDB and DynamoDB
> benchmarks, version numbers, and Azure latency/throughput claims) are time-sensitive and were
> re-verified against primary sources on 2026-06-28. Re-check before redistributing.
