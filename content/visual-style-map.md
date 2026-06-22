---
title: "Visual Style Map — From Prompts to Harness Engineering"
description: "STORM visual-research output plus visual-style-router style matrix for the harness engineering blog visual rebuild (Step 3b)"
author: Shailesh Mishra
ms.date: 2026-06-22
ms.topic: concept
keywords:
  - visual research
  - STORM
  - style router
  - harness engineering
  - visual versatility
estimated_reading_time: 9
---

<!-- markdownlint-disable MD013 -->

# Visual Style Map

> Stage: Step 3b redo — visuals rejected as single-style / text-heavy, rebuilt across the
> Visual Versatility System.
> Source artifacts: `content/from-prompts-to-harness-engineering.md` (blog draft),
> `content/harness-engineering-strategy.md`, `content/visual-opportunity-map.md`,
> `content/reference-brief.md`, `content/pipeline-config.md`.
> Style evidence: `content/visuals/harness-engineering/pilot/` (8 PNGs, 5 styles proven to render).
> Router: `scripts/visuals/styles/router.py` via `scripts/visuals/styles/route_harness.py`.
> No PNGs rendered in this stage.

## Visual thesis

The model is not the agent — the *harness* is. The visual pack must make that one reframe
unmistakable by rotating mediums so the look itself signals the argument: a typographic hook,
a hand-drawn maturity arc and napkin flows, a blueprint anatomy of "how it's built", a
data-exhibit metric board, and an editorial metaphor for the honest limits. The medium changes
every adjacent slot; the palette and the harness motif stay constant.

## Perspectives discovered

Seeded from the run audiences (AI-fluent IC engineer, tech lead, engineering manager) and
expanded into reader-perspectives that change what a visual must *do*:

- **The scanner (3-second skim)** — needs one focal idea per asset, no paragraph cards.
  (brief: v01 quote card; v05 hero-number exhibit.)
- **The chart-skeptic / mechanism reader (developer)** — distrusts dashboards, wants the
  feed-forward/feedback mechanism and the real repo wiring. (brief: v03 anatomy; v06 case study.)
- **The economics reader (manager/exec)** — wants the hard numbers: 40% context-switch tax,
  72.5% routing savings, 23% fewer tool failures. (brief: v04 building blocks; v05 cost exhibit.)
- **The visual learner** — needs a metaphor and a sketch, not a spec. (brief: v02 maturity arc;
  v07 risk/limits metaphor.)
- **The accessibility-first / print reader** — needs contrast, standalone captions, no
  color-only meaning, mono-readable. (blueprint + typographic carry the print case.)
- **The doer (practitioner)** — wants the one shippable step. (brief: v08 playbook checklist.)

### Simulated questioning (condensed writer ↔ design-expert)

- *Scanner → v01:* "What do I see first?" → the Böckeler line as type-as-art, nothing else.
  Style that earns trust: **typographic**. Failing assumption: a decorated card buries the quote.
- *Mechanism reader → v03:* "Show me how it's built, not a logo soup." → centred model core
  with two labelled rails. Style: **blueprint** (schematic, mono labels). Hand-drawn would read
  as too casual for "anatomy".
- *Economics reader → v04/v05:* "Where are the numbers?" → v04 holds four metric badges
  (data-exhibit precision); v05 isolates a single 40% (oversized type beats a one-bar chart).
- *Visual learner → v02/v06:* "Give me a napkin." → hand-drawn maturity rail and a hand-drawn
  repo flow; the sketch medium signals "mental model", not "dashboard".
- *Doer → v08:* "What do I ship?" → hand-drawn step ladder with a loop-back arrow.

## Contradiction map

| Clash | Need A | Need B | Resolution | Hero? | Blind spot |
|-------|--------|--------|------------|-------|------------|
| Quick-scan vs. mechanism | Exec wants one number (v05) | Developer wants the loop (v03) | Split by asset + medium: v05 **typographic** hero-number, v03 **blueprint** mechanism | — | — |
| Warmth vs. precision | Napkin/hand-drawn concept | Hard-number exactness | Reserve **hand-drawn** for concept/flow/checklist (v02, v06, v08); use **data-exhibit** for the metric board (v04) | — | — |
| Pilot's hand-drawn dominance | Pilot used 4/8 hand-drawn | Anti-sameness adjacency rule | Spread hand-drawn to **non-adjacent** slots; reassign v03 anatomy to **blueprint** | — | — |
| Ideal flow vs. installed engine | v06 wants a real graph (diagram-as-code) | d2/dot/mmdc **not installed** | Render v06 as **hand-drawn flow** (pilot-proven `v06-rough-flow`); diagram-as-code **blocked** | — | v06 |
| Hook universality | Every reader needs the reframe | — | v01 quote is the **hero** — first thing every perspective sees | **v01** | — |
| Limits credibility | Skeptic wants honesty shown | Data readers want a formula | v07 **editorial-illustration** metaphor with the risk formula overlaid (no baked text) | — | s02 storyboard / cover summary not yet planned |

- **Universal agreement → hero:** v01 typographic quote — the one asset every perspective needs.
- **Blind spot → missing visual:** a cohesive cover/summary and the `s02` reel storyboard are
  not in the blog companion set; flagged for the standalone pass, not this rebuild.

## Ranked visual plan

Five key style decisions, ranked by confidence, each traced to a perspective / contradiction
and cross-checked against the pilot's proven renders.

| # | Slot | Type | Style | Renderer | Audience | Confidence | Supports / Challenges |
|---|------|------|-------|----------|----------|------------|-----------------------|
| 1 | v01-harness-quote | quote | typographic | html-css-chromium | broad | 9 | Supports scanner + hero agreement; pilot `v01-typographic` proven. No challenge. |
| 2 | v02-maturity-arc | timeline | hand-drawn | rough.js / matplotlib-xkcd | developer | 9 | Supports visual learner; pilot `v02-sketch` proven. Challenged by print reader (mono) — caption mitigates. |
| 3 | v08-playbook-checklist | checklist | hand-drawn | rough.js / matplotlib-xkcd | developer | 9 | Supports doer; pilot `v08-sketch-checklist` proven. |
| 4 | v06-pipeline-case-study | concept/flow | hand-drawn | rough.js / matplotlib-xkcd | developer | 9 | Supports mechanism reader; pilot `v06-rough-flow` proven. Ideal diagram-as-code **blocked** (no engine). |
| 5 | v03-harness-anatomy | architecture | blueprint | html-css-chromium+svg | architect | 8 | Supports mechanism reader; blueprint renderer proven on pilot `v04-blueprint`. Diverges from pilot's `v03-rough` to break hand-drawn adjacency. |
| 6 | v04-building-blocks | comparison | data-exhibit | html-css-chromium | tech-lead | 8 | Supports economics reader (four hard numbers); data-exhibit proven on pilot `v05-exhibit`. Diverges from pilot `v04-blueprint`. |
| 7 | v05-context-switch-cost | statistical | typographic | html-css-chromium | exec | 8 | Single 40% as type-as-art; typographic proven. Router forced off data-exhibit by adjacency with v04 — defensible (one dramatic stat). Weakest-justified choice. |
| 8 | v07-risk-limits | mood/metaphor | editorial-illustration | html-css-chromium+svg | tech-lead | 8 | Supports skeptic; pilot `v07-editorial` proven. Guardrail: NO baked text — overlay the risk formula. |

- **Hidden connection (the motif):** the harness loop + the shared design-token palette
  (ACCENT blue, ACCENT_2 teal, ACCENT_3 purple, WARN red) recur across every medium, so the
  pack reads as one argument despite five looks.
- **One actionable style decision:** rotate the medium on every adjacent slot; never let two
  neighbours share a look — the exact failure the rejected single-style pass had.
- **Frontier / experimental:** v07 editorial metaphor (flat-vector "honest limits" scene with
  the risk formula overlaid) is the highest-variance bet; pilot evidence de-risks it.

## Self peer-review

- **Weakest link:** v05 → typographic. It is the router's *diversity-forced* choice (first-pick
  was data-exhibit, displaced because v04 is data-exhibit and adjacents must differ). Justified
  because v05 carries a single hero number (up to **40%** context-switch tax), which reads
  strongest as oversized type rather than a one-bar chart; typographic is pilot-proven. What
  would raise confidence to 9: a one-line trend sub-label under the 40% so the exec gets
  direction, not just magnitude.
- **Bias / dominance check: PASS.** hand-drawn is the most-used style at 3/8 (37.5%), well under
  the >50% single-style failure threshold. Five distinct styles are represented and **no two
  adjacent visuals share a style** (typographic → hand-drawn → blueprint → data-exhibit →
  typographic → hand-drawn → editorial-illustration → hand-drawn). No audience dominates: the
  matrix spans broad, developer, architect, tech-lead, and exec.
- **Missing perspective:** the accessibility-first / print reader is the 6th angle that most
  changes the plan. Mitigation: every asset ships a standalone caption, blueprint and
  typographic carry the mono/print case, and no asset encodes meaning by colour alone.
- **Overall grade: A−.** Every style choice traces to a perspective, a contradiction
  resolution, a confidence score, and a pilot-proven renderer. The one soft spot (v05) is
  documented and de-risked. Top fixes before render: (1) add the v05 trend sub-label; (2) keep
  v07 text as overlay only; (3) confirm v03/v04 divergence from the pilot is intentional (it is —
  to break hand-drawn adjacency).

## Style matrix (router.py — verbatim)

Produced by `PYTHONPATH=. python3 scripts/visuals/styles/route_harness.py`, which builds one
`AssetRequest` per blog visual from the opportunity-map briefs and calls `route()`,
`style_matrix()`, `moderator_move()`, and `available_engine()` from
`scripts/visuals/styles/router.py`:

```text
=== Per-asset style decisions ===
asset id                 style_id               renderer
------------------------------------------------------------------------------
v01-harness-quote        typographic            html-css-chromium
v02-maturity-arc         hand-drawn             rough.js / matplotlib-xkcd
v03-harness-anatomy      blueprint              html-css-chromium+svg
v04-building-blocks      data-exhibit           html-css-chromium
v05-context-switch-cost  typographic            html-css-chromium
v06-pipeline-case-study  hand-drawn             rough.js / matplotlib-xkcd
v07-risk-limits          editorial-illustration html-css-chromium+svg
v08-playbook-checklist   hand-drawn             rough.js / matplotlib-xkcd

=== Package style matrix (histogram) ===
blueprint                1
data-exhibit             1
editorial-illustration   1
hand-drawn               3
typographic              2

styles represented: 5 of 6

=== Moderator move (overlooked style) ===
diagram-as-code

=== diagram-as-code engine availability ===
None installed (d2 / dot / mmdc all absent)
```

### Diversity verdict (reviewer pre-render gate)

- **Not single-style:** PASS — 5 distinct styles.
- **No adjacent repeats:** PASS — every neighbouring pair differs (verified above).
- **Palette of 2–4 styles for a series:** N/A (single post); the package rotates 5 styles, well
  above the 2-style floor.
- **6 styles represented?** No — **5 of 6**, justified: the 6th is `diagram-as-code`, which the
  router itself surfaces as the moderator move but which is **blocked** because no engine
  (d2 / graphviz / mermaid) is installed. We deliberately do **not** assign it.

### Moderator move (Co-STORM)

The router's overlooked style is **`diagram-as-code`** — the natural fit would be v06
(the repository harness flow). **Rejected for this rebuild: blocked — install engine**
(`brew install d2` / `brew install graphviz` / `npm i -g @mermaid-js/mermaid-cli`). Until an
engine is installed, v06 stays **hand-drawn flow**, which the pilot already proved renders
(`v06-rough-flow.png`). Revisit diagram-as-code for v06 only after an engine is wired.

## Final per-visual style assignments

| ID | style_id | Confidence | Renderer | Guardrails (carry to art-direction) | Pilot evidence |
|----|----------|------------|----------|-------------------------------------|----------------|
| v01-harness-quote | typographic | 9 | html-css-chromium | TYPE_SCALE display role; ≤12 words | `v01-typographic.png` (match) |
| v02-maturity-arc | hand-drawn | 9 | rough.js / matplotlib-xkcd | crisp digits (path-effect Normal); edge-to-edge arrows | `v02-sketch.png` (match) |
| v03-harness-anatomy | blueprint | 8 | html-css-chromium+svg | mono labels; no baked slide numbers | `v04-blueprint.png` (renderer proven) |
| v04-building-blocks | data-exhibit | 8 | html-css-chromium | bars not gauges; one focal number per beam | `v05-exhibit.png` (renderer proven) |
| v05-context-switch-cost | typographic | 8 | html-css-chromium | one focal number (40%); add trend sub-label | `v01-typographic.png` (renderer proven) |
| v06-pipeline-case-study | hand-drawn | 9 | rough.js / matplotlib-xkcd | edge-to-edge arrows; readable repo filenames | `v06-rough-flow.png` (match) |
| v07-risk-limits | editorial-illustration | 8 | html-css-chromium+svg | NO baked text — overlay formula only; ~30% negative space | `v07-editorial.png` (match) |
| v08-playbook-checklist | hand-drawn | 9 | rough.js / matplotlib-xkcd | crisp digits; loop-back arrow Step 5 → Step 2 | `v08-sketch-checklist.png` (match) |

### Standalone visuals (noted, not in this blog rebuild)

- **s01-linkedin-card-pack** — mixed narrative sequence; reuses the blog assets' style language
  cropped to 1080×1350. Style is per-card (typographic quote → hand-drawn arc → blueprint frame →
  data-exhibit stat → hand-drawn repo map → editorial risk → hand-drawn checklist). Planned for
  the LinkedIn pass after blog visuals are rebuilt.
- **s02-reel-storyboard** — SVG storyboard; deferred to the Reel pass. Candidate **blind-spot
  cover/summary** visual also belongs here.

## Mind map

```text
From Prompts to Harness Engineering (visual pack)
├── Reframe the model is not the agent
│   ├── v01 hook            {quote,        typographic,            html-css-chromium,      broad,     conf 9}  [HERO]
│   └── v05 cost of ad-hoc  {statistical,  typographic,            html-css-chromium,      exec,      conf 8}
├── How we got here / mental models
│   ├── v02 maturity arc    {timeline,     hand-drawn,             rough.js/mpl-xkcd,      developer, conf 9}
│   └── v06 repo case study {concept/flow, hand-drawn,             rough.js/mpl-xkcd,      developer, conf 9}  [ideal diagram-as-code BLOCKED]
├── How it is built
│   ├── v03 harness anatomy {architecture, blueprint,              html-css-chromium+svg,  architect, conf 8}
│   └── v04 building blocks {comparison,   data-exhibit,           html-css-chromium,      tech-lead, conf 8}
├── Honest limits
│   └── v07 risk & limits   {mood/metaphor,editorial-illustration, html-css-chromium+svg,  tech-lead, conf 8}
├── Do this now
│   └── v08 playbook        {checklist,    hand-drawn,             rough.js/mpl-xkcd,      developer, conf 9}
└── Standalone (later passes)
    ├── s01 LinkedIn cards  {sequence,     mixed per-card,         html-css-chromium,      broad}
    └── s02 reel storyboard {narrative,    editorial/diagram TBD,  svg,                    practitioner}  [+ cover/summary blind spot]
```

## Handoff

Pass this file to `infographic-art-director` (briefs inherit each `style_id` + guardrails) and
to `style-rendering` (dispatches the adapter by `style_id`). `visual-reviewer` reads the
**Self peer-review** and **Diversity verdict** above as its pre-render gate. Reproduce the
matrix at any time with `PYTHONPATH=. python3 scripts/visuals/styles/route_harness.py`.
