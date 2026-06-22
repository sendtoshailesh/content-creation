<!-- markdownlint-disable MD013 -->
# Visual Versatility System

A research-backed architecture for generating **stylistically diverse** visuals —
hand-drawn/pencil, artistic typographic, diagrammatic, blueprint/isometric, editorial
illustration, and clean data-viz — chosen by **content type** and **audience**, instead of
funneling every asset through one "data-exhibit" look.

> Status: design + working pilot. Pilot renderers live in `scripts/visuals/styles/` and
> `content/visuals/harness-engineering/pilot/`. Pipeline wiring is incremental.

---

## 1. Why current visuals look the same

The existing pipeline is excellent at *correctness* but funnels almost everything through a
single aesthetic:

| Constraint (today) | Effect |
|---|---|
| Text-heavy assets → HTML/CSS+Chromium "exhibit" | Every infographic is a card/grid/bar layout |
| Gauges and arcs banned; magnitude = horizontal bars only | One visual grammar for all magnitude |
| One fixed `TYPE_SCALE`, "article-proportionate", uniform | No expressive typographic range |
| AI imagery banned from text + diagrams | No illustrative or metaphor scenes carry meaning |
| Infographic **type** router exists, but all types render in the same look | Type varies; *style* never does |

There was a router for **what** to communicate (process, comparison, timeline…) but **no axis
for how it should look**. That missing axis is the root cause. This system adds it.

---

## 2. Research synthesis

Reusable, open-source, and compatible with the existing static-PNG / Chromium pre-render model
(no client JS ever ships to published pages):

| Tool | License / reach | What it unlocks | Integration |
|---|---|---|---|
| **Rough.js** | MIT, 21k★ | Hand-drawn/pencil SVG: hachure, cross-hatch, dots, dashed fills; `roughness`/`bowing` | JS lib via the existing `charts_js` Chromium bridge |
| **matplotlib `xkcd()`** | already installed | Sketch-style charts/diagrams, zero new dependency | Native Python renderer |
| **D2** | MPL-2.0, 24.5k★ | Text-to-diagram with **sketch mode** + many themes (ELK/dagre layout) | CLI → SVG/PNG (opt-in `brew install d2`) |
| **mingrammer/diagrams** | MIT, 42k★ | Diagram-as-Code with real cloud icons (AWS/Azure/GCP/K8s) | Python + Graphviz (opt-in `brew install graphviz`) |
| **Excalidraw** | MIT, 126k★ | Hand-drawn whiteboard, `.excalidraw` JSON, PNG/SVG export | Reference look; Rough.js is the engine underneath |
| **STORM / Co-STORM** | Stanford, 29k★ | Multi-perspective research + contradiction-aware synthesis + a hierarchical **mind map** + a **self peer-review** *before* generating | Reused as the four-phase "visual research" pre-stage (Section 7) |

**The STORM insight applied to visuals.** STORM's contribution is not its article output; it is
its *method*. STORM decomposes research into **perspective-guided question asking** + **simulated
conversation** grounded in sources, then **outline → article → polish**; Co-STORM adds a
**moderator** that surfaces overlooked angles and a **dynamic mind map** that reorganizes
findings. The widely-shared 4-prompt distillation adds the parts STORM itself lacks: a
**contradiction map**, an explicit **synthesis**, and a **self peer-review** (Stanford flagged
that STORM does not self-critique — source bias and fact misassociation leak in). We adopt the
**whole** method for visuals, not just "list some perspectives" (Section 7).

---

## 3. Core model: two orthogonal axes + audience

Every visual is now described by **two independent choices** plus the audience:

```text
            WHAT to say                         HOW it looks
    ┌───────────────────────┐         ┌───────────────────────────┐
    │  Infographic TYPE      │   ×     │  Visual STYLE / MEDIUM     │
    │  (existing router)     │         │  (NEW axis)                │
    └───────────────────────┘         └───────────────────────────┘
       process, comparison,              data-exhibit, hand-drawn,
       timeline, hierarchy,              typographic, blueprint,
       statistical, concept,             editorial-illustration,
       checklist, comic                  diagram-as-code
                         \              /
                          \            /
                       AUDIENCE + PLATFORM
              (developer, tech lead, exec; blog, LinkedIn, X)
```

A "process" diagram can be rendered as a clean data-exhibit **or** a hand-drawn sketch **or** an
isometric blueprint. Type and style are decoupled.

---

## 4. Style registry

Six styles (all selected in the scoping decision), each mapped to a renderer adapter and a
"best for" intent. Adapters live in `scripts/visuals/styles/`.

| Style id | Look | Primary renderer | Best for | Audience lean |
|---|---|---|---|---|
| `data-exhibit` | Clean cards, bars, metrics (today's look, refined) | HTML/CSS+Chromium (`scripts/visuals/html`) | Hard numbers, scorecards, exec exhibits | Exec, tech lead |
| `hand-drawn` | Sketchy/pencil boxes, arrows, charts | Rough.js (Chromium) **or** matplotlib `xkcd()` | Concepts, "napkin" explainers, approachable posts | Developer, broad |
| `typographic` | Text-as-art: oversized editorial type, asymmetric, pull-quotes | HTML/CSS+Chromium | Quotes, single big ideas, hooks, hero cards | Broad, LinkedIn |
| `blueprint` | Technical schematic / isometric, grid paper, mono labels | HTML/CSS+Chromium (SVG accents) | Architecture, systems, "how it's built" | Developer, tech lead |
| `editorial-illustration` | Metaphor scene, flat-vector shapes (no embedded text) | `scripts.visuals.generated.programmatic` + text overlay | Mood, openers, conceptual metaphors | Broad, exec |
| `diagram-as-code` | Real flow/architecture graphs, optional sketch theme | D2 (sketch) / Mermaid / mingrammer-diagrams | Pipelines, dependency graphs, cloud topo | Developer, tech lead |

Rules that keep variety honest:

- **Adjacent visuals must differ in style**, not just theme. A post may not be all `data-exhibit`.
- A series picks a **style palette of 2–4** styles and rotates; it does not use one.
- `editorial-illustration` keeps the existing hard rule: **no text baked into pixels** — text is
  overlaid programmatically over reserved negative space.

---

## 5. Audience → style affinity

Default affinities (the router can override per asset based on the burning question):

| Audience | Lead styles | Avoid |
|---|---|---|
| **Developer / IC** | `hand-drawn`, `diagram-as-code`, `blueprint` | Over-polished exec exhibits |
| **Tech lead / architect** | `blueprint`, `diagram-as-code`, `data-exhibit` | Cutesy cartoons for hard tradeoffs |
| **Engineering manager / exec** | `data-exhibit`, `typographic`, `editorial-illustration` | Dense code-style graphs |
| **Broad / social hook** | `typographic`, `hand-drawn`, `editorial-illustration` | Wall-of-text exhibits |

---

## 6. The style-selection router

A small, deterministic decision function (lives in the `visual-style-router` skill; the
`visual-strategist` agent calls it per asset):

```text
INPUT  per asset: burning_question, infographic_type, audience, platform, data_density
OUTPUT per asset: style_id, renderer, rationale, anti-pattern guardrails

1. If asset carries hard numbers / scorecard intent      -> prefer data-exhibit
2. Else if it is a flow / architecture / dependency graph -> diagram-as-code (sketch theme if audience=developer/broad)
3. Else if it is a single quote / one big idea / hook     -> typographic
4. Else if it explains a concept or "napkin" mental model -> hand-drawn
5. Else if it is "how it's built" / system anatomy        -> blueprint
6. Else if it sets mood / opener / metaphor (no data)     -> editorial-illustration
7. Apply audience affinity (Section 5) as a tie-breaker
8. Enforce package diversity: if this style already used by the
   previous asset, pick the next-best compatible style
```

The router emits a **package-level style matrix** so the renderer and reviewer can verify
diversity before anything is rasterized.

---

## 7. STORM-inspired visual research stage

A pre-stage (skill: `visual-research`) that runs once per content run **before** rendering and
writes `content/visual-style-map.md`. It mirrors STORM's full method — not just "list
perspectives." It runs in four phases (the STORM 4-prompt distillation), then a polish pass that
reuses STORM's `polish` + Co-STORM `reorganize()` ideas.

### Phase 1 — Perspective discovery + simulated questioning (STORM core)

- **Discover, don't hardcode.** STORM finds perspectives by surveying similar work rather than
  fixing them. The stage seeds from the run's audiences (dev, tech lead, exec) **and discovers
  reader-perspectives** that change what a visual must do — e.g. *the scanner* (3-second skim),
  *the chart-skeptic* (distrusts dashboards, wants the mechanism), *the visual learner* (needs a
  metaphor), *the accessibility-first reader* (contrast/standalone captions), *the printout
  reader* (mono, no color reliance).
- **Simulated questioning.** For each perspective, run a short writer↔design-expert exchange
  (2–3 follow-ups) grounded in the reference brief: *What does this reader need to see first?
  Which style earns their trust? What baked-in assumption fails them?* Answers cite reference-brief
  entries — grounding, not decoration.

### Phase 2 — Contradiction map (the STORM gap-finder)

The single most valuable step and the one most likely to prevent "every visual looks the same."
Map where the perspectives **conflict**:

1. **Direct clashes** — e.g. exec wants a quick-scan exhibit vs. developer wants the detailed
   mechanism; hand-drawn warmth vs. data precision; density vs. skimmability. Each clash names the
   two needs that collide.
2. **Strongest vs. weakest** style evidence per clash.
3. The **one decision** that resolves the biggest clash (often: split into two assets in two
   styles, one per audience — exactly the versatility the pack needs).
4. **Universal agreement** → what every perspective needs becomes a **hero** visual, rendered
   boldly.
5. **Blind spot** → a key claim **no** perspective would illustrate is the **missing visual**;
   add it (this is STORM's "unknown unknowns" applied to a visual pack).

### Phase 3 — Synthesis into a ranked visual plan

Pull Phases 1–2 into a plan (not a flat table): the one-line visual thesis for the pack; the
**5 key visual decisions ranked by confidence**, each noting which perspectives support/challenge
it; the **hidden connection** (a motif/palette/style rhythm that ties the pack together); the
**one actionable style decision**; and the **frontier/experimental** visual worth trying.

### Phase 4 — Self peer-review of the plan (STORM's explicit weakness, fixed)

Stanford flagged that STORM does not self-critique. Before any pixels are rendered, the plan
grades itself:

- **Confidence score (1–10)** per visual decision, with reasons.
- **Weakest link** — the least-justified style choice and what would justify it.
- **Bias / dominance check** — did one style or one audience dominate the matrix? (This is the
  early-warning for the "one-type" failure.)
- **Missing perspective** — is there a 6th reader-angle that would change the plan?
- **Overall grade** + the top fixes to apply before rendering.

### Phase 5 — Mind map + polish/dedup (Co-STORM reorganize + STORM polish)

- The map is **hierarchical**, not a flat list: `topic → sub-themes → visual slots → {type,
  style, renderer, audience, confidence}` — a concept tree that keeps a multi-part series coherent
  and reduces planning load (Co-STORM's mind map).
- A **polish/dedup** pass (post-render, in the reviewer) detects **near-duplicate compositions**
  (same grid/bar/card skeleton repeated) and forces a re-style, and optionally adds a cohesive
  **cover/summary** visual — STORM's `polish` (add summary, remove duplicates) and Co-STORM's
  `reorganize()` applied to a visual pack.

Every style choice in `visual-style-map.md` traces to a perspective, a contradiction resolution,
and a confidence score — auditable the way STORM grounds statements in citations.

### What each STORM component maps to

| STORM / Co-STORM | Visual equivalent | Where |
|---|---|---|
| Perspective-guided question asking | Discover reader-perspectives + simulated questioning | Phase 1 |
| Simulated conversation (follow-ups) | Writer↔design-expert exchange grounded in the brief | Phase 1 |
| (4-prompt) Contradiction map | Clash map + agreement→hero + blind-spot→missing visual | Phase 2 |
| Outline generation | Ranked visual plan (decisions by confidence) | Phase 3 |
| (4-prompt) Self peer-review | Plan self-critique before rendering | Phase 4 |
| Co-STORM moderator | Router/art-director propose an **overlooked** style/visual | Phase 2–3 + Section 6 |
| Co-STORM dynamic mind map | Hierarchical concept tree of slots | Phase 5 |
| STORM polish / `reorganize()` | Near-duplicate dedup + cohesive cover | Phase 5 + Section 10 |
| Grounded citations | Each style choice cites reference-brief entries | All phases |
| Multi-LM cost balancing | Light reasoning for routing; depth for briefs/QA | Operational note |

---

## 8. Agents and skills

### New

| Kind | Name | Responsibility |
|---|---|---|
| Skill | `visual-style-router` | The decision function in Section 6; outputs style + renderer + guardrails per asset and a package style matrix. Includes a **moderator move**: proposes one overlooked style/visual the default picks missed |
| Skill | `visual-research` | The four-phase STORM stage (Section 7): discovery + simulated questioning → contradiction map → ranked synthesis → self peer-review → hierarchical mind map. Writes `content/visual-style-map.md` |
| Skill | `style-rendering` | How to drive each new adapter (Rough.js, xkcd, D2, diagrams) with tokens + gates |

### Updated

| Kind | Name | Change |
|---|---|---|
| Agent | `visual-strategist` | Runs `visual-research` (all four phases) and `visual-style-router`; writes the ranked style matrix + self-critique into the visual opportunity map |
| Agent | `infographic-art-director` | Briefs specify **style id** + medium-specific direction, not just infographic type; consumes the contradiction map (split-audience clashes become two assets) |
| Agent | `visual-renderer` | Dispatches to a **style adapter** by `style_id`; no longer hard-defaults to HTML/CSS exhibits |
| Agent | `visual-reviewer` | Two gates: (1) **pre-render** runs the Phase-4 self-critique on the plan; (2) **post-render** runs the diversity + **near-duplicate dedup** + per-style acceptance checks |
| Skill | `visual-rendering` | Points at the adapter registry; keeps existing inspector/reviewer gates |
| Instr. | `visual-standards.instructions.md` | Adds the style axis + per-style rules; keeps token system, 320 DPI, no-baked-text for AI imagery |

### Unchanged guardrails

Design tokens, Helvetica Neue, 320 DPI, the Chromium DOM inspector, the rubber-duck visual
review, and "no text baked into AI pixels" all remain. New adapters plug in *behind* the same
gates.

---

## 9. Renderer stack additions

| Style | Stack | Install | Offline | Notes |
|---|---|---|---|---|
| `hand-drawn` (charts) | matplotlib `xkcd()` | none | yes | Zero-dependency sketch; wrap token palette |
| `hand-drawn` (diagrams/cards) | Rough.js in Chromium bridge | `npm i` in `charts_js` | yes after install | Reuses Playwright `#stage` pattern |
| `typographic` | HTML/CSS+Chromium | none | yes | New CSS module; large-type roles added to scale |
| `blueprint` | HTML/CSS+Chromium (+SVG) | none | yes | Grid-paper background, mono labels |
| `editorial-illustration` | `scripts.visuals.generated.programmatic` | none | yes | Text overlaid, never baked |
| `diagram-as-code` | D2 (sketch) / Mermaid / diagrams | `brew install d2` / `graphviz` | yes after install | Pre-render to PNG; never ship live JS |

All JS stays a **server-side pre-render to static PNG/SVG**; published pages load no client JS.

---

## 10. Anti-sameness enforcement

**Pre-render (plan self-critique, Phase 4).** Block the plan when the bias/dominance check shows
one style or one audience owns the matrix — the earliest catch for the "one-type" failure, before
any pixels are spent.

**Post-render (reviewer).** Block publishing when:

- A package is **single-style** (all `data-exhibit`, etc.).
- **Adjacent** visuals share a style *and* theme.
- Two visuals are **near-duplicate compositions** (same grid/bar/card skeleton) even across
  different styles — forces a re-style (STORM polish / Co-STORM `reorganize()`).
- A "concept/quote/hook" asset is rendered as a dense exhibit (style/intent mismatch).
- `editorial-illustration` has any baked-in text.
- A diagram ships as a raw fence instead of a pre-rendered PNG.

These join the existing checks (overflow, off-scale type, stray labels, missing connectors).

---

## 11. Pilot (this change)

All eight harness-engineering visuals re-rendered across **six distinct styles** (no two adjacent
visuals share a style), proving the rendering half of the system end-to-end:

| Source visual | New style | Renderer |
|---|---|---|
| `v01` harness quote | `typographic` (text-as-art) | HTML/CSS+Chromium |
| `v02` maturity arc | `hand-drawn` (sketch steps) | matplotlib `xkcd()` |
| `v03` harness anatomy | `hand-drawn` (sketch diagram) | Rough.js (Chromium bridge) |
| `v04` building blocks | `blueprint` (dark schematic) | HTML/CSS+SVG |
| `v05` context-switch cost | `data-exhibit` (the one refined exhibit) | HTML/CSS+Chromium |
| `v06` pipeline case study | `hand-drawn` (sketch flow) | Rough.js (Chromium bridge) |
| `v07` risk limits | `editorial-illustration` (metaphor lane) | HTML/CSS+SVG |
| `v08` playbook checklist | `hand-drawn` (sketch checklist) | matplotlib `xkcd()` |

Output: `content/visuals/harness-engineering/pilot/`. Adapters: `scripts/visuals/styles/`
(`typographic.py`, `sketch_mpl.py`, `sketch_rough.py`, `blueprint.py`, `editorial.py`).

> Scope note: the pilot proves the **renderer/style axis** (Sections 3–6). The **STORM research
> half** (Section 7: discovery, contradiction map, ranked synthesis, self peer-review,
> dedup/polish) is specified but not yet wired — that is the next-steps work below.

### Next steps after pilot sign-off

1. Promote the five adapters + add the `diagram-as-code` adapter (D2/Mermaid/diagrams).
2. Land the `visual-research` skill as the **full four-phase STORM stage** (Section 7), plus
   `visual-style-router` (with the moderator move) and `style-rendering`.
3. Update the four agents and `visual-standards.instructions.md` per Section 8 — including the
   reviewer's **pre-render self-critique** and **post-render dedup** gates.
4. Re-run the harness blog's full visual set through the router + STORM stage for a genuinely
   mixed, contradiction-aware, self-reviewed pack.
