# Visual Style Map — "Just Use Postgres" (DB-1)

> STORM pre-stage for the DB-1 run. Grounds every style choice in a reader-perspective, a
> contradiction resolution, and a confidence score before any pixels are rendered. Source:
> `content/just-use-postgres.md`, `content/reference-brief.md`, `content/creative-brief.md`,
> `content/postgres-just-use-strategy.md`. Run audiences: staff/principal engineer + architect
> (primary), engineering leader / CTO (co-primary). Single post. Distribution: LinkedIn + Reel +
> Slide deck (Medium/Substack/LinkedIn Article OFF). Created 2026-06-26.
>
> **This supersedes the archived Loop Engineering style map.** Nothing here reuses that run.

## Visual thesis

One ACID engine quietly swallowing five specialist systems should *look* like convergence — warm,
clean, and inevitable — while the four exits should *look* like hard red walls with a number on
each, so the believer stance reads as field judgment, not a slogan.

## Perspectives discovered

- **The scanner (3-second skim).** Needs the 5→1 idea and the "four walls" count to land before
  reading a word. Brief: §A (consolidation is the star), §C (four breakpoints).
- **The chart-skeptic architect.** Distrusts a tidy diagram; wants the *mechanism* and the
  ceiling number that justifies each exit. Brief: §B (extensions), §C (ScyllaDB 7.5M inserts/s,
  Vitess 5+ yrs, DynamoDB 500k+ req/s, ClickHouse ~1B rows/s).
- **The budget-owner / eng leader.** Doesn't care about HNSW; cares that 5 systems → 1 means one
  backup, one failover, one on-call, one hire profile. Brief: §B framing note (consolidation
  dividend).
- **The visual learner.** Needs the Postgres-elephant metaphor and a napkin "one story" sketch to
  *feel* the simplification, not just read it. Brief: creative-brief §7 (whiteboard energy).
- **The accessibility-first / printout reader.** Red "wall" meaning must not be color-only; each
  breakpoint needs a text label and a standalone caption; the strip must read in mono. Brief:
  visual-research perspective set.
- **The vendor-neutrality watchdog (blind-spot reader).** Will bounce if Azure looks like the
  default. Specialists (Cassandra/ScyllaDB, Spanner/CockroachDB/Vitess, Redis/DynamoDB,
  ClickHouse/Snowflake) must read as first-class equals; Azure is one cloud's option in small
  secondary type. Brief: §C Azure-equal-footing note.

## Contradiction map

| Clash | Need A | Need B | Resolution | Hero? | Blind spot |
|---|---|---|---|---|---|
| Convergence warmth vs. data precision | Visual learner wants the elephant metaphor / napkin feel | Chart-skeptic wants exact ceilings | **Split by asset**: hero + ops card carry warmth (diagram-as-code convergence + hand-drawn napkin); breakpoints carry precision (data-exhibit scorecard) | v01 hero = universal agreement | — |
| Architect mechanism vs. leader ops framing | Architect: what each extension *does* | Leader: what 5→1 *saves* | Two assets, two styles: v01 names the extensions (mechanism); v02 names the ops stacks removed (dividend) | — | — |
| Specialist-as-equal vs. author-on-Azure | Vendor-neutral: specialists are the headline | Author works on Azure | Azure appears **only** as a small secondary label under each card, never as the card's primary target | — | Azure-as-default trap |
| Skim count vs. depth | Scanner needs "4 walls" instantly | Skeptic needs the number | v03 leads with the count (4 red cards) and puts the ceiling number as the card's hero figure | v03 | — |
| Color-as-meaning vs. accessibility | WARN-red signals "wall" fast | Printout/AccessibilityFirst reader loses color | Every red card keeps a text label + standalone caption; decision strip reads in mono | — | color-only meaning |

**Universal agreement (→ hero):** every perspective needs the 5→1 convergence. That is v01.
**Blind spot (→ missing visual):** no perspective spontaneously illustrates *what consolidation
removes operationally* — the leader's dividend. v02 ("one engine, one story" ops card) is that
deliberately-added visual.

## Ranked visual plan

| # | Slot | Type | Style | Renderer | Audience | Confidence | Supports / Challenges |
|---|---|---|---|---|---|---|---|
| 1 | v01 — 5→1 consolidation hero | concept / architecture convergence | `diagram-as-code` | Python SVG (`scripts.visuals.svg`) | architect + leader (broad) | **9/10** | Supports: scanner, visual learner, both personas. Challenges: chart-skeptic (mitigated by tagging each box with its real extension) |
| 2 | v03 — four-breakpoints panel | statistical / comparison scorecard | `data-exhibit` | matplotlib PNG (`scripts.visuals.html` alt) | architect | **9/10** | Supports: chart-skeptic, scanner (count). Challenges: vendor-neutrality watchdog (mitigated: specialists primary, Azure secondary) |
| 3 | v02 — "one engine, one story" ops card | concept / before-after | `hand-drawn` | Rough.js `sketch_rough` → PNG (xkcd `sketch_mpl` fallback) | eng leader | **8/10** | Supports: leader, visual learner. Challenges: skeptic wants numbers (intentionally qualitative — ops dividend, not a benchmark) |
| 4 | v04 — decision-rule strip | process / single big idea | `typographic` | Python SVG (`scripts.visuals.styles.typographic`) | broad | **8/10** | Supports: scanner, decision-maker. Challenges: accessibility (mitigated: mono-readable, yes/no labeled not color-only) |

**Hidden connection (pack motif):** the Postgres elephant silhouette + the brand-blue ACCENT spine
recur as the through-line; WARN-red is reserved *exclusively* for the four exits, SUCCESS-green
*exclusively* for the consolidation win. Color itself encodes the thesis (blue = default, green =
win, red = wall).

**One actionable style decision:** reserve red for walls and green for the win across the whole
pack — never decorative — so a reader who only sees thumbnails still reads "default → win, exit →
wall."

**Frontier / experimental:** v04 as oversized typographic strip (text-as-art) rather than a boxed
flowchart — the one asset that breaks the diagram look and reads like a manifesto line.

## Self peer-review

- **Weakest link:** v02 (hand-drawn ops card, 8/10). It is the only asset carrying no external
  number, so it leans on craft. Justification: it is the *deliberately added* blind-spot visual
  for the leader persona, and the ops dividend is qualitative by design (creative-brief §9 says
  keep the win qualitative). What would raise confidence: a single concrete count ("5 backup
  procedures → 1") used as the card's anchor figure — sourced from the anecdote, not invented.
- **Bias / dominance check:** **PASS.** Four assets, four distinct styles (diagram-as-code,
  data-exhibit, hand-drawn, typographic) — a palette of 4, no style repeats, every adjacent pair
  differs. Audience balance: v01 broad, v02 leader, v03 architect, v04 broad — neither persona
  dominates. No single-style funnel.
- **Missing perspective:** considered a 6th angle — *the data-platform / DBA reader* who would
  contest "Postgres can do time-series at all." Covered implicitly by the breakpoint honesty
  (v03) and the TimescaleDB tag on v01; does not change the plan.
- **Overall grade: A−.** Plan is diverse, grounded, and vendor-neutral. Top fixes before
  rendering: (1) give v02 one anchor count from the anecdote; (2) verify Azure secondary labels
  never exceed ~40% of a breakpoint card's type weight; (3) re-pull all `[VOLATILE]` figures
  (ScyllaDB, DynamoDB, ClickHouse, pgvector stars) at render time.

## Package style matrix

| Asset | `style_id` | Renderer | Rationale | Guardrails |
|---|---|---|---|---|
| v01 | `diagram-as-code` | Python SVG (bespoke convergence) | 5 source nodes → 1 engine is structural/flow | Edge-to-edge convergence arrows; elephant silhouette as terminal node; tag each source with its extension |
| v02 | `hand-drawn` | Rough.js (`sketch_rough`) → PNG | napkin "one story" concept, warmth for leader | Crisp digits via path-effect; messy 5-stack vs. one clean stack must read as state change, not two static icons |
| v03 | `data-exhibit` | matplotlib PNG @320 DPI | four hard ceiling numbers, scorecard | One hero figure per card; WARN-red accent + text label (not color-only); Azure as small secondary line |
| v04 | `typographic` | Python SVG | one decision rule, manifesto line | Mono-readable; yes/no branches labeled in text; big type, minimal chrome |

**Diversity gate:** PASS — 4 styles / 4 assets, palette of 4, no adjacent repeat.

**Moderator move (one overlooked style):** `blueprint` is unused. The single asset that could
adopt it is a *follow-on* "anatomy of one Postgres" schematic (dark grid, mono) showing the five
extensions wired into one engine internally — deferred (P2) so the core pack stays at four. Not
forced into the main pack; logged as a deferred variety win.

## Mind map

```
Just Use Postgres (DB-1)
├── Consolidation case (the star, §3)
│   ├── v01 5→1 hero {concept/convergence, diagram-as-code, Python SVG, broad, 9}
│   │   ├── source: Vector DB → pgvector
│   │   ├── source: Queue → pgmq
│   │   ├── source: Time-series → TimescaleDB
│   │   ├── source: Search → full-text (tsvector+GIN)
│   │   └── source: Document → JSONB
│   └── v02 one-engine-one-story ops card {before-after, hand-drawn, Rough.js, leader, 8}
│       └── 5 backup/HA/security/on-call/skills stacks → 1
├── Four breakpoints (the caveat, §4)
│   └── v03 four-breakpoints panel {statistical, data-exhibit, matplotlib, architect, 9}
│       ├── write throughput → Cassandra/ScyllaDB (7.5M inserts/s @ 4ms P99)
│       ├── sharding → Spanner/CockroachDB/Vitess (YouTube 5+ yrs)
│       ├── sub-ms KV → Redis/DynamoDB (single-digit ms, 500k+ req/s)
│       └── petabyte OLAP → ClickHouse/Snowflake (~1B rows/s)
├── Decision rule (§5)
│   └── v04 decision-rule strip {process/big-idea, typographic, Python SVG, broad, 8}
│       └── Default → name the wall (with a number)? → specialize | just use Postgres
└── Distribution reuse (no redundant renders)
    ├── LinkedIn carousel ← v01 (cover) + v03 (payoff) + v04 (CTA) + v02 (mid)
    ├── Reel ← v01 + v03 as vertical title cards over psql screen-recording
    ├── Slide deck ← all four embedded 16:9 by deck-builder
    └── Deferred (P2): blueprint "anatomy of one Postgres" (moderator move)
```
