---
title: Strategy & Outline - Postgres Ate the Database Market ("Just Use Postgres")
description: Strategy and section-by-section outline for the single ~1,800-word opinion post. Consolidation case is the spine; the four breakpoints are the honest caveat. Anchored on the author's consolidation-win anecdote.
author: Shailesh Mishra
ms.date: 2026-06-26
ms.topic: concept
---

# Strategy & Outline — "Just Use Postgres"

> Single post, ~1,800 words. Believer stance. Consolidation case = star; four breakpoints =
> credibility caveat. Grounded in `content/creative-brief.md` + `content/reference-brief.md`.
> **Scope:** treated as a single post; formal scope assessment (Step 2b) still runs next.

## Thesis (one sentence)

"Just use Postgres" is right ~90% of the time — one ACID engine now absorbs vectors, time-series,
queues, search, and documents, collapsing five systems into one operational story — and you should
only reach for a specialist at four specific walls: extreme write throughput, planet-scale
sharding, sub-millisecond key-value, and true petabyte-scale OLAP.

## Strategic decisions

- **Spine = consolidation (the star).** ~60% of word budget on "5 systems → 1 engine, one
  backup/HA/security/on-call story." ~30% on the four breakpoints. ~10% on the anecdote + decision
  rule.
- **Breakpoints earn trust.** Framed as "here's where I *don't* use Postgres" — concrete ceilings,
  legitimate specialists, no strawmen. This is what makes the 90% claim believable.
- **Serve both personas in every section:** technical ceiling (architect) + ops/cost consequence
  (leader).
- **Anchor on the anecdote.** Open on it (or open with the meme and cut to it in §2). The post is
  field-tested judgment, not a feature tour.
- **Numbers as punctuation, not flood.** One sharp number per claim; reference brief has the rest.

## Series Plan

None. Single post. (If Step 2b scope assessment scores into series territory, revisit — but the
~1,800-word punchy-opinion intent argues strongly for a single post.)

## Outline (section-by-section, with target word budget)

### 0. Title / hook options (pick one in draft)
- **"When Not to Use Postgres: A Decision Framework for the Four Walls Where One Engine Isn't Enough"** ← SELECTED (decision-maker hook; contrarian open, decision-framework spine)
- "Just Use Postgres — Until You Hit One of These Four Walls" (original; conversational)
- "Postgres Ate the Database Market. Here's the 10% It Can't Digest."
- "I Stopped Adding Databases. You Probably Can Too."

### 1. Cold open — the consolidation win (anecdote anchor) — ~200 words
- Open **on the anecdote** (sanitized, provided 2026-06-26): a team I worked with was running
  **five moving parts** — Postgres + a standalone Redis + Elasticsearch + a separate message queue
  + a cron service — and collapsed all of it into **one Postgres**: Elasticsearch → Postgres
  full-text (`tsvector`) + **pgvector** for semantic search; the queue → a Postgres queue
  (pgmq-style); the cron service → `pg_cron`; Redis's hot path → folded back into Postgres.
- The win to land: **five datastores → one**, and a **lower cloud bill** from retiring the separate
  managed services. Keep it qualitative — do not invent a precise % or $ the author didn't give.
- Land the thesis in one line: "That experience made me a believer — and taught me exactly where
  the belief stops."

### 2. "Just use Postgres" stopped being a meme — ~250 words
- Why now: **most-used DB 2nd year running, 48.7%** (SO 2024), **33% → 48.7% since 2018**, also
  **most-admired (47.1%) and most-desired (74.5%)**; **DB-Engines trend still rising**.
- It's not nostalgia — it keeps shipping: **PG18 async I/O → up to 3× read throughput** (Sept
  2025), skip scan, UUIDv7, OAuth 2.0; **PG19 already in beta**. The engine is getting *better*
  at the things that used to push you off it.

### 3. The consolidation case: five systems, one engine — ~650 words (THE STAR)
Five micro-sections, each: "the workload you'd add a system for" → "the Postgres answer" → "the
ops consequence." One number each, no benchmark flood.
- **Vectors → pgvector.** Similarity search lives *next to* your relational data — ACID, JOINs,
  PITR, hybrid search (FTS + vectors via RRF). No separate vector DB to sync. (~21.9k stars, HNSW.)
- **Time-series → TimescaleDB.** Hypertables + columnstore (**90%+ typical compression**),
  continuous aggregates — metrics/events without a second database.
- **Queues → pgmq.** SQS-style queue with **exactly-once delivery within a visibility timeout**,
  no broker to run; **Supabase and Tembo run it in production**. Your jobs and your data share a
  transaction.
- **Search → full-text (tsvector/GIN).** Real lexical search without standing up a search cluster;
  combine with pgvector for hybrid.
- **Documents → JSONB.** Binary documents + GIN indexing — the "I need a document DB" case, in core.
- **The payoff (leader framing):** 5 systems → 1 means **one backup, one failover, one security
  model, one on-call rotation, one set of specialists to hire.** That's the consolidation dividend
  — and it's why I default to Postgres.

### 4. Where the belief stops: the four breakpoints — ~500 words (THE CAVEAT)
Intro line: "Believer, not zealot. Here are the four walls where I reach for a specialist — on
purpose." Four tight cards, each: the wall → the ceiling number → the specialist → the honest
"why Postgres can't."
- **1. Extreme write throughput → Cassandra / ScyllaDB.** Single-primary write model is the wall.
  Ceiling: **ScyllaDB's published 7.5M inserts/sec at 4 ms P99** (vs Aerospike); 2–5× Cassandra.
  *On Azure (one cloud's equal option):* Azure Managed Instance for Apache Cassandra, or Cosmos DB.
- **2. Planet-scale sharding → Spanner / CockroachDB / Vitess.** Postgres has no transparent native
  sharding — you bolt it on. **Vitess ran *all* of YouTube's DB traffic for 5+ years**; Spanner/
  CockroachDB are shard-native with global consistency. *On Azure:* Cosmos DB for NoSQL (multi-region
  writes, 99.999% SLA), or Azure Database for PostgreSQL Elastic Clusters (Citus) to stay Postgres.
- **3. Sub-millisecond key-value → Redis / DynamoDB.** Connection/transaction overhead can't hit
  that floor. **DynamoDB: single-digit-ms at any scale, ½M+ req/s, 200 TB+ tables, 99.999%.**
  *On Azure:* Azure Managed Redis (successor to Azure Cache for Redis), or Cosmos DB.
- **4. True OLAP at petabyte scale → ClickHouse / Snowflake.** Row-oriented OLTP can't match
  column-store scan rates. **ClickHouse: ~1 billion rows/sec (100M rows in 92 ms), ~7 GB/s/query.**
  *On Azure:* Azure Data Explorer (Kusto) or Microsoft Fabric / Synapse.
- Note: these are *legitimate, correct* choices for their case — not Postgres failures. Knowing
  the wall is what makes "just use Postgres" a real engineering position, not a slogan. Azure names
  are listed as **one cloud's equal-footing option** per wall, never as the default over AWS/GCP/OSS.

### 5. The decision rule — ~150 words
- "Default to Postgres. Reach for a specialist only when you can name which of the four walls you're
  hitting — with a number." If you can't name the wall, you don't have one yet.
- Reinforce the consolidation dividend: every system you *don't* add is a backup/failover/on-call
  you don't run.

### 6. Close + CTA — ~50 words
- Callback to the anecdote's before/after win.
- CTA: "Before you add the sixth datastore, which of the four walls are you actually hitting? If you
  can't name it — just use Postgres. Tell me the consolidation (or specialization) call you made."

## Visual markers to seed for visual-strategist / blog-writer

- `[VISUAL: 5-to-1 consolidation hero — five labeled boxes (vector/queue/TSDB/search/document)
  collapsing into one Postgres elephant, each tagged with its extension]` (§3, P0 — the star)
- `[VISUAL: "one engine, one story" ops card — 5 backup/HA/security/on-call stacks -> 1]` (§3, P1)
- `[VISUAL: four-breakpoints panel — four red-accented cards, each with its one ceiling number and
  specialist target]` (§4, P0)
- `[VISUAL: decision-rule strip — Default to Postgres -> hit one of these 4 walls? -> specialize]`
  (§5, P1)

## Numbers ledger (all from reference-brief.md — re-verify [VOLATILE] before publish)

| # | Used in | Number | Source |
|---|---|---|---|
| 1 | §2 | 48.7% most-used, 2nd yr; 33%→48.7% since 2018; 47.1% admired; 74.5% desired | SO 2024 survey |
| 2 | §2 | PG18 async I/O up to 3× read throughput (2025-09-25); PG19 beta (2026-06-04) | postgresql.org |
| 3 | §3 | pgvector ~21.9k stars, HNSW, up to 2,000 dims | github.com/pgvector |
| 4 | §3 | TimescaleDB 90%+ typical compression | github.com/timescale |
| 5 | §3 | pgmq exactly-once within visibility timeout; Supabase/Tembo | github.com/pgmq |
| 6 | §4 | ScyllaDB 7.5M inserts/s @ 4 ms P99; 2–5× Cassandra | scylladb.com/benchmarks |
| 7 | §4 | Vitess ran all YouTube DB traffic 5+ yrs; Slack/Square/JD.com | vitess.io |
| 8 | §4 | DynamoDB single-digit ms, ½M+ req/s, 200 TB+, 99.999% | aws.amazon.com/dynamodb |
| 9 | §4 | ClickHouse ~1B rows/s (100M rows in 92 ms), ~7 GB/s | clickhouse.com/docs |

## Open items before blog draft (RESOLVED)

1. **Anecdote** — RESOLVED 2026-06-26. Sanitized consolidation-win story provided (five-part stack
   → one Postgres; win = five datastores → one + lower cloud bill). Locked into §1 and the brief.
2. **Scope assessment (Step 2b)** — RESOLVED. Vetting 4/4 pass, zero red flags; scope score ≈ 3/16
   → **single post** (one dominant arc, ~1,800-word core, 4 visuals, one CTA). No series.

**Draft:** `content/just-use-postgres.md` written 2026-06-26 (~2,300 words incl. mandatory
"Build it yourself" practitioner section).
