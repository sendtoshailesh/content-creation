---
title: Creative Brief - Postgres Ate the Database Market ("Just Use Postgres")
description: Creative brief for a single ~1,800-word opinion post making the Postgres-consolidation case and naming the four honest breakpoints where a specialist database still wins.
author: Shailesh Mishra
ms.date: 2026-06-26
ms.topic: concept
keywords:
  - just use postgres
  - postgres consolidation
  - pgvector
  - timescaledb
  - pgmq
  - database consolidation
estimated_reading_time: 8
---

## Creative Brief

> Status: `approved` (decisions locked by user 2026-06-26 from clarifying-question answers)
> Run topic: Postgres Ate the Database Market — The "Just Use Postgres" Thesis and Where It Breaks (idea DB-1)
> Created: 2026-06-26. Source of truth: `content/reference-brief.md`, `content/pipeline-config.md`

## 1. Overview

"Just use Postgres" went from a meme to an architectural default. With extensions covering
vectors (pgvector), time-series (TimescaleDB), queues (pgmq), full-text search, and documents
(JSONB), one ACID engine now credibly absorbs workloads that a few years ago demanded five
separate systems — each with its own backup story, failover model, access-control surface, and
on-call rotation. **Why now:** Postgres is the most-used database for the second year running
(48.7%, Stack Overflow 2024, up from 33% in 2018), it's also the most-admired and most-desired,
and it keeps shipping serious engineering on an annual cadence (PG18's async I/O delivered up to
3× read throughput in Sept 2025; PG19 is already in beta). The consolidation case is strong enough
that the interesting question is no longer "can Postgres do it?" — it's "when should I still *not*
use it?" This post makes the believer's case for consolidation, then names the four honest places
where a specialist is still the right call.

## 2. Objectives

- **Primary job-to-be-done:** Convince a staff/principal engineer or architect that "just use
  Postgres" is the correct *default* (~90% of the time) by showing how much one engine now
  absorbs — and earn that confidence by naming, specifically, the four workloads where it breaks.
- **Secondary jobs:**
  - Give the eng leader / CTO the consolidation framing they care about: fewer systems → lower
    cost, smaller operational surface, one backup/HA/security story, fewer specialists to hire.
  - Make the reader trust the recommendation *because* it admits limits — the four breakpoints are
    credibility, not hedging.
  - Anchor the whole argument in a real, first-person consolidation win (the anecdote) so it reads
    as field-tested judgment, not a listicle.

## 3. Target audience

- **Primary persona — staff / principal engineer & architect (the "one DB vs. specialist"
  decider):** Owns the build-vs-buy and consolidate-vs-specialize call. Pain: stack sprawl, five
  datastores to operate, "do we really need Kafka + Redis + Pinecone + a warehouse for *this*?"
  Wants architect-level technical substance: what each extension actually does, where the real
  ceiling is, and a defensible decision rule.
- **Co-primary persona — engineering leader / CTO (consolidation for cost & ops simplicity):**
  Weighing the org cost of running many specialized systems. Pain: tooling/licensing spend,
  headcount for niche systems, operational risk of a sprawling data tier. Wants the
  cost/ops/consolidation framing and a clear "default to one, specialize on exception" heuristic.
- **Write so both get value in the same piece:** lead each breakpoint with the technical ceiling
  (architect) *and* the consolidation/ops consequence (leader). Neither audience should feel the
  post is "for the other one."

## 4. Key message

**"Just use Postgres" is right about 90% of the time: one ACID engine now absorbs vectors,
time-series, queues, search, and documents — collapsing five systems into one backup, one
failover, one security model — and you should only reach for a specialist at four specific
breakpoints: extreme write throughput, planet-scale sharding, sub-millisecond key-value, and
true petabyte-scale OLAP.**

## 4b. Content hypothesis

**We believe** staff/principal engineers and eng leaders currently treat each new workload
(vectors, queues, time-series, search) as a reason to add another specialized datastore, and will
shift to **defaulting to Postgres and only specializing at four named, defensible breakpoints**
**because** the post shows — with real numbers and a first-person consolidation win — that one
engine now covers the common cases and that the exceptions are specific and recognizable, not
vague.

**We will know we are right when**, within 7 days of publishing:
- ≥ 8% save/repost rate on the LinkedIn post (above the channel's recent median), OR
- ≥ 5 qualified comments that engage the actual argument — naming one of the four breakpoints,
  defending or contesting the "90%" claim, or sharing their own consolidation/specialization call
  (not just "great post"), OR
- ≥ 3 practitioners say the four-breakpoint rule changed or confirmed a real architecture decision.

**We will know we are wrong when** engagement sits at or below the last 3 posts' median AND there
are no qualified comments — meaning the consolidation thesis read as obvious/old news and the
breakpoints didn't earn trust; the fix is a sharper, more contrarian angle, not a repost.

**Riskiest assumption:** that the audience finds the four breakpoints *non-obvious and useful*. If
senior engineers already know exactly when to leave Postgres, the post is just a louder version of
consensus. The draft must defend this by making each breakpoint concrete (real ceilings, real
specialist, real consolidation cost) rather than hand-wavy.

## 5. Tone & style

- **Stance: BELIEVER.** "Just use Postgres" is right ~90% of the time; here are the rare
  exceptions. Confident, opinionated, first-person — but earns trust by naming the real limits.
  Not a neutral survey, not a vendor pitch, not a "it depends" cop-out.
- First-person practitioner: "what I've seen consolidating real stacks onto Postgres." Anchor on
  the anecdote.
- Conversational but data-anchored: every consolidation claim and every breakpoint carries a
  concrete number or named source — but **lighter on exhaustive benchmarks**. Use real numbers as
  punctuation, don't drown the reader in them.
- Lead with the consolidation case (the star); treat the four breakpoints as the honest,
  credibility-building caveat — not the focus.
- **Format & length: punchy opinion piece, ~1,800 words** (overrides the prior ~3,000-word
  default). Single post, not a series (formal scope assessment still runs at Step 2b).

## 6. Deliverables (this run)

- **Blog (primary):** single ~1,800-word opinion post, `content/postgres-just-use-it.md` (or
  similar slug). Opens or anchors on the consolidation-win anecdote.
- **LinkedIn post (always-on):** believer-angled, Unicode-formatted, hooks on "stop adding
  databases — just use Postgres (until these 4 walls)."
- **Reel/Short script:** 60–90s, screen-recording cues over a single Postgres instance doing
  vector search + a queue + time-series in one `psql` session; voiceover walks the 5→1
  consolidation and the four breakpoints.
- **Slide deck (PPTX + PDF):** built by `deck-builder` from the finalized blog + LinkedIn, humor +
  intellectual speaker notes, tagged by section (consolidation case / each breakpoint).
- **NOT in scope this run:** X/Twitter, Reddit, YouTube, Medium, Substack, LinkedIn Article.

## 7. Visual guidelines

- Clean, technical, confident mood — whiteboard/architecture-diagram energy, not stock-photo gloss.
- **Palette / type:** repository design tokens (ACCENT `#1f6feb`, ACCENT_2 `#0d9488`, ACCENT_3
  `#7c3aed`, WARN `#dc2626` for the breakpoints, SUCCESS `#16a34a` for the consolidation win),
  Helvetica Neue, 320 DPI, ASCII glyphs only in matplotlib (`->`, `[x]`, `[ ]`).
- **Deterministic diagrams/infographics (programmatic) — candidate set:**
  - **5→1 consolidation diagram (hero):** five labeled boxes (vector DB, queue, TSDB, search,
    document store) collapsing into one Postgres elephant, each with the extension that absorbs it
    (pgvector / pgmq / TimescaleDB / FTS / JSONB). This is the star visual.
  - **"One engine, one story" ops card:** 5 backup/HA/security/on-call stacks → 1 (the leader's
    cost/ops framing).
  - **The four breakpoints panel:** four red-accented cards — write throughput (→ Cassandra/Scylla),
    sharding (→ Spanner/CockroachDB/Vitess), sub-ms KV (→ Redis/DynamoDB), petabyte OLAP (→
    ClickHouse/Snowflake) — each with its one concrete ceiling number.
  - **Decision rule strip:** "Default to Postgres → hit one of these 4 walls? → specialize." A
    simple flow.
- **AI hero/illustrative image:** OFF/optional (programmatic mode default). If used: an abstract
  "many small boxes merging into one solid block" scene, ~30% negative space, **no embedded text**,
  brand-color fidelity. Diagrams stay programmatic.
- **Reference images for vision-grounding:** none required; the Postgres elephant motif + the
  repo's design tokens are sufficient.

## 8. Call to action

- **Blog:** "Before you add the sixth datastore, ask which of the four walls you're actually
  hitting. If you're not hitting one, just use Postgres." Invite readers to share the consolidation
  (or specialization) call they made and how it played out.
- **LinkedIn/Reel/Deck:** same spine, channel-tuned — provoke the "what would you add / what did
  you consolidate?" comment.

## 9. Constraints & guardrails

- **No fabricated benchmarks.** Every number traces to `content/reference-brief.md`; vendor
  benchmark figures (ScyllaDB, DynamoDB) are cited as the vendor's own published claim, with the
  comparison named. `[VOLATILE]` numbers re-verified by `grounded-content-reviewer` before publish.
- **Vendor-neutral on specialists.** The four breakpoints name specialists as legitimate, correct
  choices for their case — not strawmen. Postgres-believer ≠ Postgres-zealot.
- **ANECDOTE — PROVIDED (sanitized, 2026-06-26):** a real consolidation win the author lived.
  - **Stack replaced (five moving parts):** Postgres + a standalone Redis + Elasticsearch + a
    separate message queue + a cron service.
  - **What one Postgres absorbed it into:** Elasticsearch's search split between Postgres full-text
    (`tsvector`) and **pgvector** for semantic/vector search; the message queue moved to a Postgres
    queue (pgmq-style); the cron service moved to `pg_cron`; Redis's hot-path caching folded back
    into Postgres. **Five datastores/services → one Postgres.**
  - **Before/after win:** fewer moving parts (five → one), and a **lower cloud bill** from retiring
    the separate managed services. (Keep qualitative unless the author supplies an exact % / $.)
  - Sanitized framing for the draft: "On a recent project, a team I worked with was running five
    datastores …" — first-person, illustrative, no invented precise numbers.
- **Keep the extension set tight:** pgvector, TimescaleDB, pgmq, full-text search, JSONB. Do not
  sprawl into PostGIS, Citus, pg_cron, etc. (mention-in-passing at most).
- First-person practitioner voice; no corporate/fundraising framing; earn the believer stance
  through specifics, not volume.
