# Platform Distillation — Medium / Substack / LinkedIn Article (Step 12)

> **One unified excerpt** — copy the same block to **Medium**, **Substack**, and **LinkedIn
> Article**. All three point to the GitHub Pages canonical URL (so the original keeps SEO credit).
> Visual-first: upload the referenced PNGs from `content/topics/postgresql/visuals/`.
>
> **Canonical URL:** https://sendtoshailesh.github.io/blog/ai-postgresql-performance.html
> **Medium:** use the Import tool (auto-sets `rel=canonical`) OR add the canonical link in story
> settings. **Substack:** post as a Note / short excerpt, link out. **LinkedIn Article:** use a
> distinct angle intro (below), link out at the top and bottom.

---

── START COPY ──

# How AI Actually Helps You Fix PostgreSQL Performance Problems (and Where It Lies)

*Originally published at [sendtoshailesh.github.io](https://sendtoshailesh.github.io/blog/ai-postgresql-performance.html) — this is a condensed version.*

![Fixing Postgres performance with AI — a DBA's field guide](visuals/hero.png)

It's 2 a.m. and p99 on the orders API just jumped from 90 ms to 6 seconds. You know the dance:
tail logs, pull the query, run `EXPLAIN`, form a theory, repeat. After a year of handing parts of
that loop to LLMs across customers' Postgres fleets, here's my honest verdict: **AI won't replace
your `EXPLAIN ANALYZE` instincts — but grounded in your real stats, it cuts the diagnose-to-fix loop
from an hour to minutes.**

## The one rule: an LLM can't see your database

It doesn't know your version, your buffers, your `pg_stat_statements`, or that one table that's 40%
dead tuples. On the [BIRD benchmark](https://bird-bench.github.io/) — text-to-SQL over 95 real
databases — GPT-4 scores just **54.89%** execution accuracy (and **34.88%** without curated
context) versus **92.96%** for humans. The lesson isn't "AI is useless"; it's that accuracy is
dominated by the real context you feed it. So **ground every prompt**: paste the actual
`EXPLAIN (ANALYZE, BUFFERS)`, the `pg_stat_statements` row, and `SELECT version();`.

## Where it helps — and where it lies

![Where AI helps vs hurts across the Postgres performance workflow](visuals/ai-help-matrix.png)

- **Triage & summarizing `pg_stat_statements` / Performance Insights — high.** Pattern-matching over
  real stats is exactly its strength.
- **Reading `EXPLAIN` plans in plain English — high** (as long as it's `ANALYZE`, not estimates).
- **Index & rewrite suggestions — medium.** A great candidate-generator, a terrible decision-maker.
  Validate every one.
- **Anomaly detection — high**, but that's classic ML (DevOps Guru for RDS, pganalyze), not chatbots.
- **Internals, DDL, "just run this" — low / risky.** Keep a human in front of anything that locks.

## One real example: the missing composite index

![Before/after latency: 4,200 ms vs 38 ms (~110x)](visuals/before-after-latency.png)

A multi-tenant query with `date_trunc('day', created_at) = $2` — non-sargable, ~4,200 ms. I fed the
plan to Claude; it spotted the seq scan and the missing `(tenant_id, created_at)` composite, and
proposed a sargable range rewrite. The part that matters: **I didn't run `CREATE INDEX` on its
say-so.** I validated with `hypopg` (a hypothetical index the planner costs without building),
confirmed the plan flipped to an Index Scan, then built it `CONCURRENTLY`. Result: **~38 ms, about
110× faster.** The AI got me to the right hypothesis in 30 seconds; `hypopg` made it safe.

## Even the AI workload itself lives in Postgres now

Via `pgvector`, and its indexes have a brutal trade-off: on a representative 500K×768 benchmark,
**HNSW** runs ~4 ms p50 at ~99% recall but builds in ~14 min; **IVFFlat** runs ~18 ms p50 but builds
~7× faster. "Which index?" has no universal answer — feed the model your row count, write rate, and
latency budget, and the same question becomes engineering instead of a horoscope.

## The playbook

**Ground it → Triage → Hypothesize → Validate (`hypopg`/replica) → Apply (human, `CONCURRENTLY`) →
Measure.** Wire AI in over a **read-only** role (e.g., a Postgres MCP server for live stats); never
auto-apply DDL. The DBAs winning with this didn't hand the keys to a chatbot — they turned it into a
very fast, very well-read junior who always shows their work, and still gets checked before prod.

**Read the full field guide** — with the SQL, the autovacuum and connection-storm examples, the tool
landscape (pganalyze vs DevOps Guru vs Postgres MCP), and all sources:
👉 https://sendtoshailesh.github.io/blog/ai-postgresql-performance.html

── END COPY ──

---

## Platform notes

- **Word count:** ~750 words (Medium/LinkedIn Article sweet spot). For **Substack**, post the first
  3 paragraphs as a Note with the canonical link.
- **Images to upload** (from `content/topics/postgresql/visuals/`): `hero.png`, `ai-help-matrix.png`,
  `before-after-latency.png`. If the practitioner carousel is ready
  (`visuals/distilled/postgresql-practitioner/`), Medium/LinkedIn Article can use those slides inline.
- **LinkedIn Article distinct intro** (avoid duplicate-content with the LinkedIn post): lead with the
  BIRD stat ("GPT-4 gets 54.89% on real SQL vs 92.96% for humans — here's what that means for tuning
  Postgres") rather than the 2 a.m. hook.
- **SEO:** canonical points to GitHub Pages on all three so the original ranks.
