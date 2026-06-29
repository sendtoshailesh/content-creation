---
title: Visual Opportunity Map — "Just Use Postgres" (DB-1)
description: Mandatory visual plan for the DB-1 single post. Four blog companion visuals (the four seeded markers) plus distribution reuse for LinkedIn + Reel + Slide deck. Programmatic only; vendor-neutral; design-token compliant.
author: Shailesh Mishra
ms.date: 2026-06-26
ms.topic: reference
---

# Visual Opportunity Map — "Just Use Postgres" (DB-1)

> **Fresh DB-1 run.** This overwrites the archived Loop Engineering map. Nothing here reuses the
> old loop visuals. Source artifact: `content/just-use-postgres.md` (finished draft). Grounding:
> `content/reference-brief.md`, `content/creative-brief.md`, `content/postgres-just-use-strategy.md`.
> Style decisions, perspectives, and the self peer-review live in `content/visual-style-map.md`.
> **Planning only — nothing is rendered yet.**

## Summary

The blog seeds **four** `[VISUAL: ...]` markers; this plan delivers exactly those four as the blog
companion pack, then reuses them (no new renders) for LinkedIn, the Reel, and the Slide deck.

- **The star (P0):** `v01` 5→1 consolidation hero — five specialist boxes collapsing into one
  Postgres, each tagged with the extension that absorbs it.
- **The leader's dividend (P1):** `v02` "one engine, one story" ops card — five backup/HA/security/
  on-call stacks → one.
- **The honest caveat (P0):** `v03` four-breakpoints panel — four red-walled cards, each with one
  ceiling number and the specialist it justifies (Azure as one cloud's equal option, secondary).
- **The rule (P1):** `v04` decision-rule strip — Default to Postgres → name the wall (with a
  number)? → specialize / just use Postgres.

**Package style diversity (from `visual-style-map.md`):** 4 assets, 4 distinct styles
(`diagram-as-code`, `hand-drawn`, `data-exhibit`, `typographic`) — palette of 4, no adjacent
repeat. Diversity gate: **PASS**.

**Design system (all assets):** BG `#ffffff`; ACCENT `#1f6feb` (default/spine); ACCENT_2 `#0d9488`;
ACCENT_3 `#7c3aed`; **WARN `#dc2626` reserved exclusively for the four walls**; **SUCCESS `#16a34a`
reserved exclusively for the consolidation win**; TEXT `#1e293b`; TEXT_2 `#475569`; MUTED `#94a3b8`;
GRID `#e5e7eb`; LIGHT_BG `#f8fafc`. Helvetica Neue. **320 DPI** for PNG. **ASCII glyphs only in
matplotlib** (`->`, `[x]`, `[ ]` — no Unicode arrows/checks).

**Vendor-neutrality contract:** specialists (Cassandra/ScyllaDB, Spanner/CockroachDB/Vitess,
Redis/DynamoDB, ClickHouse/Snowflake) are first-class equals and are the primary label on every
breakpoint card. Azure options (Managed Instance for Apache Cassandra, Cosmos DB, Azure Database
for PostgreSQL Elastic Clusters, Azure Managed Redis, Azure Data Explorer) appear **only** as a
small secondary "on Azure" line, never as the default and never larger than the specialist label.

**Volatility:** every `[VOLATILE]` figure (ScyllaDB 7.5M inserts/s, DynamoDB 500k+ req/s, ClickHouse
~1B rows/s, pgvector ~21.9k stars, version numbers) is time-sensitive and was verified 2026-06-26.
`grounded-content-reviewer` must re-pull before render and before publish.

## Opportunity table

| ID | Source section | Concept type | Audience | Visual family | `style_id` | Platform fit | Standalone | Required source data | Renderer | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `v01` | §3 The consolidation case (the star) | Architecture / convergence | Architect + leader (broad) | Architecture / flow diagram | `diagram-as-code` | Blog + LinkedIn + Reel + Deck | High | 5 workloads + 5 extensions; PG18 3× read | Python SVG | **P0** | planned (marker in draft) |
| `v02` | §3 ops payoff | Concept / before-after | Eng leader / CTO | Infographic / one-pager (napkin) | `hand-drawn` | Blog + LinkedIn + Deck | Medium | 5 ops stacks → 1 (qualitative; anecdote) | Rough.js → PNG | **P1** | planned (marker in draft) |
| `v03` | §4 The four breakpoints (the caveat) | Statistical / comparison scorecard | Architect | Executive exhibit / scorecard | `data-exhibit` | Blog + LinkedIn + Reel + Deck | High | 4 ceiling numbers + specialists + Azure secondary | matplotlib PNG | **P0** | planned (marker in draft) |
| `v04` | §5 The decision rule | Process / single big idea | Broad | Decision strip / one-pager | `typographic` | Blog + LinkedIn + Deck | High | 4 wall-tests (write rate, shard count, latency, scan) | Python SVG | **P1** | planned (marker in draft) |
| `v05` | §3 + §4 (follow-on) | System anatomy | Architect / DBA | Blueprint schematic | `blueprint` | Blog (deep-dive) | Medium | 5 extensions wired into one engine | `scripts.visuals.styles.blueprint` | **P2 (deferred)** | deferred (moderator move) |

---

## Blog Companion Visuals

### v01 — 5→1 consolidation hero (THE STAR, §3, P0)

- **Burning question:** "Which five separate systems does one Postgres now absorb — and what
  absorbs each?"
- **Audience:** architect + engineering leader (broad).
- **Platform:** Blog (hero) + reused on LinkedIn (carousel cover) + Reel (title card) + Deck.
- **Infographic type:** concept / architecture convergence (funnel of 5 → 1).
- **Visual metaphor:** five labeled specialist boxes flowing along brand-blue spines into one
  central **Postgres elephant** silhouette = "one ACID engine."
- **State change:** five distinct boxes on the left/perimeter → converging arrows → a single solid
  engine. The arrows and the collapse *are* the message.
- **Text budget:** hero title ≤ 9 words ("Five systems, one engine"); each box label ≤ 4 words +
  its extension tag; one footnote line.
- **Exact data / labels it must contain** (from `reference-brief.md` §B):
  - `Vector DB`  ->  **pgvector** (HNSW + IVFFlat; ACID + JOINs + PITR)
  - `Queue / broker`  ->  **pgmq** (SQS-style; exactly-once within visibility timeout)
  - `Time-series DB`  ->  **TimescaleDB** (hypertables; 90%+ columnstore compression)
  - `Search cluster`  ->  **Full-text** (`tsvector` + GIN)
  - `Document DB`  ->  **JSONB** (binary documents + GIN indexing)
  - Center node: **Postgres** — "One ACID engine: one backup, one failover, one security model."
  - Footnote: "PostgreSQL 18 async I/O -> up to 3x read throughput." Source line:
    `reference-brief.md` §A–B; verified 2026-06-26.
- **Icon/illustration plan:** simple geometric boxes (one accent-tinted per source, using ACCENT /
  ACCENT_2 / ACCENT_3 tints, NOT red/green), brand-blue convergence arrows, mono elephant
  silhouette as terminal node. SUCCESS-green only on the center "consolidation win" check.
- **Visual-reviewer acceptance criteria:** all five extension tags legible at phone width; the
  5→1 collapse readable in 3 seconds; no box tinted WARN-red (red is for walls only); elephant is
  a silhouette, not clip-art; ASCII `->` only.

### v02 — "one engine, one story" ops card (§3, P1)

- **Burning question:** "What does collapsing five systems into one actually remove for whoever
  owns the budget and the pager?"
- **Audience:** engineering leader / CTO.
- **Platform:** Blog + reused on LinkedIn (mid carousel slide) + Deck.
- **Infographic type:** concept / before-after (napkin sketch).
- **Visual metaphor:** left = a messy tangle of **five** stacked ops columns; right = **one** clean
  column. Hand-drawn warmth deliberately contrasts the precise hero.
- **State change:** five repeated stacks (Backup · HA/failover · Security · On-call · Skills) ×5
  systems  ->  one of each. The de-duplication is the visible change (not two static icons).
- **Text budget:** title ≤ 7 words ("Five systems -> one story"); each row label ≤ 3 words; one
  caption ≤ 20 words.
- **Exact data / labels it must contain** (from `creative-brief.md` §3 payoff + anecdote):
  - Five collapsing rows: `Backup` · `HA / failover` · `Security / access` · `On-call rotation` ·
    `Skills to hire`.
  - Left state: "5 systems -> 5 of each." Right state: "1 system -> 1 of each."
  - Anchor count (from the anecdote, not invented): "5 backup stories -> 1."
  - Caption: "Every datastore you don't add is an incident class you never have."
  - Source line: "Author consolidation win (sanitized) — `creative-brief.md` §9."
- **Icon/illustration plan:** Rough.js sketchy boxes; left tangle in MUTED/TEXT_2, right clean
  stack in ACCENT with a single SUCCESS-green "consolidated" check. No WARN-red.
- **Visual-reviewer acceptance criteria:** the 5→1 de-dup is unmistakable; qualitative (no
  fabricated $/%); hand-drawn style distinct from v01; crisp digits; SUCCESS-green used only on the
  win.

### v03 — four-breakpoints panel (THE CAVEAT, §4, P0)

- **Burning question:** "What are the four walls where I still leave Postgres — and the one number
  that proves each?"
- **Audience:** architect (the chart-skeptic).
- **Platform:** Blog + reused on LinkedIn (saveable payoff) + Reel (title card) + Deck.
- **Infographic type:** statistical / comparison scorecard (four cards: row of 4 or 2×2).
- **Visual metaphor:** four red-walled cards; each card's **hero figure is its ceiling number**.
  WARN-red signals "wall" but is always paired with a text label (not color-only).
- **State change:** uniform card frame, but each card's ceiling number + specialist differ — the
  contrast across cards is the comparison.
- **Text budget:** panel title ≤ 8 words ("Four walls where I leave Postgres"); per card: 1 wall
  name (≤ 4 words) + 1 hero number + specialist line + tiny Azure secondary line.
- **Exact data / labels it must contain** (from `reference-brief.md` §C — vendor figures, attribute
  as such):
  - **Card 1 — Extreme write throughput.** Hero: **7.5M inserts/s @ 4 ms P99** (ScyllaDB's
    published benchmark; "2–5x Apache Cassandra," vendor figure). Specialist: **Cassandra /
    ScyllaDB**. Azure (secondary): "on Azure: Managed Instance for Apache Cassandra / Cosmos DB."
    Why-Postgres-can't: "single primary funnels all writes through one node."
  - **Card 2 — Planet-scale horizontal sharding.** Hero: **Ran ALL of YouTube's DB traffic 5+
    years** (Vitess; also Slack / Square / JD.com). Specialist: **Spanner / CockroachDB / Vitess**.
    Azure (secondary): "on Azure: Cosmos DB for NoSQL / Azure Database for PostgreSQL Elastic
    Clusters (Citus)." Why-Postgres-can't: "no transparent native sharding — you bolt it on."
  - **Card 3 — Sub-millisecond key-value.** Hero: **single-digit ms, 500k+ req/s, 200 TB+,
    99.999%** (DynamoDB; AWS's stated figures). Specialist: **Redis / DynamoDB**. Azure
    (secondary): "on Azure: Azure Managed Redis / Cosmos DB." Why-Postgres-can't:
    "connection/transaction overhead can't hold that floor."
  - **Card 4 — True OLAP at petabyte scale.** Hero: **~1 billion rows/s** (ClickHouse: 100M rows
    in 92 ms, ~7 GB/s/query). Specialist: **ClickHouse / Snowflake**. Azure (secondary): "on
    Azure: Azure Data Explorer (Kusto) / Microsoft Fabric." Why-Postgres-can't: "row-oriented OLTP
    can't match a column store's scan rate."
  - Footer: "Specialists are legitimate equals. Vendor/self-reported figures; verified 2026-06-26
    — `reference-brief.md` §C."
- **Icon/illustration plan:** four cards, each with a thin WARN-red top border + a small ASCII
  wall/brick motif `[##]`; ceiling number in large TEXT; specialist in ACCENT; Azure line in MUTED
  small caps. No green anywhere (these are exits, not wins).
- **Visual-reviewer acceptance criteria:** specialist label is the primary, Azure label ≤ ~40% of
  its type weight and clearly secondary; every card carries a text wall-label (red is not the only
  signal); all four ceiling numbers traceable to §C; ASCII glyphs only; readable as four distinct
  ceilings in 3 seconds.

### v04 — decision-rule strip (§5, P1)

- **Burning question:** "How do I decide, in one line, whether to specialize or just use Postgres?"
- **Audience:** broad (decision-maker).
- **Platform:** Blog + reused on LinkedIn (CTA card) + Deck.
- **Infographic type:** process / single big idea (horizontal decision strip).
- **Visual metaphor:** a left-to-right manifesto strip with one yes/no fork. Oversized type breaks
  the diagram look (the pack's typographic outlier).
- **State change:** Default state -> decision diamond -> two divergent ends (specialize vs. just
  use Postgres).
- **Text budget:** ≤ 18 words of body type total; the three nodes carry the whole idea.
  - Node 1 (ACCENT blue): **"Default to Postgres"**
  - Decision (TEXT): **"Hitting one of the 4 walls — with a number?"** subtext: "write rate ·
    shard count · latency floor · scan size"
  - Yes branch (WARN red): **"-> Specialize. Name the wall."**
  - No branch (SUCCESS green): **"-> Just use Postgres."**
- **Icon/illustration plan:** big typographic nodes; one diamond fork; red for the specialize
  branch, green for the default-win branch, blue for the start. Mono-readable (works in print).
- **Visual-reviewer acceptance criteria:** reads as one sentence in 3 seconds; yes/no labeled in
  text (not color-only); the four wall-tests legible; ASCII `->` only; the green "just use
  Postgres" end is the visual resolution.

---

## Standalone Distribution Visuals

> Distribution scope for this run (per `pipeline-config.md`): **LinkedIn + Reel + Slide deck.**
> Medium / Substack / LinkedIn Article are **OFF**. Rule: **reuse the four blog visuals; do not
> render redundant standalone assets.** Only platform-native *reframes* are listed, and only as
> P1/P2 — render solely if the channel aspect ratio actually requires it.

### LinkedIn (practitioner carousel, `distillation_persona_mode = practitioner`)

The carousel is assembled from the existing four visuals — **no new core renders**:

| Carousel slot | Reuses | New render? |
|---|---|---|
| Cover / hook | `v01` (5→1 hero) | No — optional 1080×1080 square reframe only if the carousel needs native aspect (`db1-five-to-one-consolidation-hero-sq`, **P1**) |
| The dividend | `v02` (ops card) | No |
| The four walls (saveable) | `v03` (breakpoints panel) | No — optional 1080×1080 reframe (`db1-four-breakpoints-panel-sq`, **P1**) |
| The rule / CTA | `v04` (decision strip) | No |

LinkedIn single-image post (non-carousel fallback): use `v03` (highest standalone save value).

### Reel / Short (60–90s, screen-recording per creative brief)

The reel is primarily a **psql screen recording** (one instance doing vector search + a queue +
time-series). Visuals are reused as **vertical title/lower-third cards**, not new infographics:

| Reel beat | Reuses | New render? |
|---|---|---|
| Open: "5 systems → 1" | `v01` | Optional 1080×1920 vertical title card (`db1-five-to-one-consolidation-hero-vert`, **P2** — only if a static title card is wanted over the screen capture) |
| Caveat: "4 walls" | `v03` | Optional 1080×1920 vertical card (`db1-four-breakpoints-panel-vert`, **P2**) |

### Slide deck (PPTX + PDF, built by `deck-builder`)

`deck-builder` embeds the **existing four PNG/SVG exports** as 16:9 slide exhibits — **zero new
renders**. Mapping: title/consolidation slide ← `v01`; ops slide ← `v02`; breakpoints section ←
`v03`; decision/close ← `v04`.

---

## Rendering Handoff

> For `visual-renderer`. All filenames are kebab-case under `content/visuals/` with a `db1-` prefix
> (distinct from the archived loop-engineering assets). Programmatic only — no external image
> generation. Carry the per-style guardrails from `visual-style-map.md`.

### db1-five-to-one-consolidation-hero
- File: `content/visuals/db1-five-to-one-consolidation-hero.svg`
- Visual family: Architecture / flow diagram · `style_id`: `diagram-as-code`
- Renderer: Python SVG (`scripts.visuals.svg`) — bespoke convergence; export PNG @320 DPI too
- Size: 1600×900 (SVG scalable)
- Message: One ACID engine absorbs five specialist systems; each box tagged with its extension.
- Data: Vector→pgvector · Queue→pgmq · Time-series→TimescaleDB · Search→full-text (tsvector+GIN) ·
  Document→JSONB; center Postgres elephant; footnote PG18 async I/O up to 3× read throughput.
- Layout: five source boxes (perimeter) -> brand-blue convergence arrows -> central elephant.
- Guardrails: WARN-red forbidden here; SUCCESS-green only on the center win; ASCII `->`; elephant =
  silhouette. Must stand alone: yes.

### db1-one-engine-one-story-ops
- File: `content/visuals/db1-one-engine-one-story-ops.png`
- Visual family: Infographic / one-pager (napkin) · `style_id`: `hand-drawn`
- Renderer: Rough.js (`scripts.visuals.styles` `sketch_rough`) → PNG @320 DPI; xkcd `sketch_mpl`
  fallback
- Size: 1600×900
- Message: Five systems → one story = one backup, one failover, one security model, one on-call.
- Data: rows Backup · HA/failover · Security/access · On-call · Skills-to-hire; left "5×", right
  "1×"; anchor "5 backup stories -> 1"; caption "every datastore you don't add is an incident class
  you never have."
- Layout: left messy 5-stack tangle -> right single clean stack (visible de-dup state change).
- Guardrails: qualitative only (no invented $/%); crisp digits; SUCCESS-green only on the win; no
  red. Must stand alone: medium.

### db1-four-breakpoints-panel
- File: `content/visuals/db1-four-breakpoints-panel.png`
- Visual family: Executive exhibit / scorecard · `style_id`: `data-exhibit`
- Renderer: matplotlib PNG @320 DPI (or `scripts.visuals.html` card grid)
- Size: 1600×1000 (four cards: 1×4 row or 2×2)
- Message: Four walls where a specialist beats Postgres — each with one ceiling number.
- Data (vendor figures, attribute as such; from `reference-brief.md` §C):
  1. Write throughput — **7.5M inserts/s @ 4 ms P99** — Cassandra/ScyllaDB — *Azure:* Managed
     Instance for Apache Cassandra / Cosmos DB
  2. Sharding — **all YouTube DB traffic 5+ yrs** — Spanner/CockroachDB/Vitess — *Azure:* Cosmos DB
     for NoSQL / Azure DB for PostgreSQL Elastic Clusters (Citus)
  3. Sub-ms KV — **single-digit ms, 500k+ req/s, 200 TB+, 99.999%** — Redis/DynamoDB — *Azure:*
     Azure Managed Redis / Cosmos DB
  4. Petabyte OLAP — **~1B rows/s** (100M rows in 92 ms, ~7 GB/s) — ClickHouse/Snowflake — *Azure:*
     Azure Data Explorer (Kusto) / Microsoft Fabric
- Layout: four cards, WARN-red top border + ASCII wall motif, ceiling number as hero figure,
  specialist primary (ACCENT), Azure secondary (MUTED, small); footer source line.
- Guardrails: specialists primary, Azure ≤ ~40% type weight + clearly "on Azure" secondary; text
  wall-label on every card (not color-only); ASCII glyphs; no green. Must stand alone: yes.

### db1-decision-rule-strip
- File: `content/visuals/db1-decision-rule-strip.svg`
- Visual family: Decision strip / one-pager · `style_id`: `typographic`
- Renderer: Python SVG (`scripts.visuals.styles.typographic`); export PNG @320 DPI
- Size: 1600×500 (horizontal strip)
- Message: Default to Postgres; specialize only when you can name the wall with a number.
- Data: Node1 "Default to Postgres" (blue) -> Decision "Hitting one of the 4 walls — with a number?"
  (subtext: write rate · shard count · latency floor · scan size) -> Yes "Specialize. Name the
  wall." (red) / No "Just use Postgres." (green).
- Layout: left-to-right, one diamond fork, oversized type.
- Guardrails: mono-readable; yes/no labeled in text; ASCII `->`; green end = resolution. Must stand
  alone: yes.

---

## Deferred / Follow-On Visuals

- **`v05` db1-postgres-anatomy-blueprint (P2, deferred — moderator move).** `style_id`: `blueprint`
  (`scripts.visuals.styles.blueprint`). A dark grid-paper schematic showing the five extensions
  (pgvector, pgmq, TimescaleDB, full-text, JSONB) wired internally into one Postgres engine —
  "anatomy of one Postgres." Adds the one unused style from the diversity matrix. Render only if a
  deep-dive/engineering-anatomy companion is wanted; **not part of the core four-visual pack.**
- **Platform reframes (P1/P2).** Square (1080×1080) reframes of `v01`/`v03` for the LinkedIn
  carousel and vertical (1080×1920) reframes for the Reel — render **only** if the channel aspect
  ratio actually requires it; otherwise reuse the blog exports.
- **Hero/illustrative AI image:** OFF this run (`image_generation: programmatic`). If ever enabled:
  an abstract "many small boxes merging into one solid block," ~30% negative space, **no embedded
  text**, brand-color fidelity — mood only, never the diagrams.

---

## Status & handoff

- All four seeded `[VISUAL: ...]` markers in `content/just-use-postgres.md` are mapped 1:1 to
  `v01`–`v04`; no new markers needed.
- Next: `infographic-art-director` confirms the briefs above, then `visual-renderer` produces the
  four assets (programmatic, design-token compliant, ASCII glyphs, 320 DPI), then the deterministic
  inspector + `visual-reviewer` pre-render diversity gate (reads the self peer-review in
  `content/visual-style-map.md`) + REVR gate before any asset is marked publish-ready.
- `grounded-content-reviewer` must re-verify all `[VOLATILE]` figures at render time.
