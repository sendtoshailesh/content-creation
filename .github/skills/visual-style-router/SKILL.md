---
name: visual-style-router
description: 'Deterministically pick a visual STYLE/MEDIUM (data-exhibit, typographic, hand-drawn, blueprint, editorial-illustration, diagram-as-code) per asset from its burning question, infographic type, and audience. Enforces package-level style diversity and surfaces a moderator move. Use when planning a visual pack so no two adjacent visuals share a look.'
argument-hint: 'Provide the planned visual list (id, burning question, infographic type, audience, platform, data density)'
---

# Visual Style Router Skill

Adds the missing **"how it looks"** axis to visual planning. The existing infographic-type
router decides *what* to communicate (process, comparison, timeline…); this skill decides the
*style/medium* it is rendered in, then guarantees package diversity. See
`agents-and-skills/visual-versatility-system.md` §3–6.

## When to Use

- After `visual-research` has written `content/visual-style-map.md` (or alongside the
  `visual-strategist` building `content/visual-opportunity-map.md`).
- Whenever a pack risks funneling every asset through the same `data-exhibit` look.

## The six styles

| `style_id` | Look | Renderer | Best for |
|---|---|---|---|
| `data-exhibit` | clean cards / bars / metrics | `scripts/visuals/html` | hard numbers, scorecards |
| `typographic` | text-as-art, oversized type | `scripts.visuals.styles.typographic` | quotes, single big ideas, hooks |
| `hand-drawn` | sketchy boxes / arrows / charts | `sketch_rough` (Rough.js) + `sketch_mpl` (xkcd) | concepts, napkin explainers |
| `blueprint` | dark schematic, grid paper, mono | `scripts.visuals.styles.blueprint` | system anatomy, "how it's built" |
| `editorial-illustration` | flat-vector metaphor, text overlaid | `scripts.visuals.styles.editorial` | mood, openers, metaphors |
| `diagram-as-code` | real flow/architecture graphs | `scripts.visuals.styles.diagram_as_code` | pipelines, dependency graphs |

## Procedure

1. Build one `AssetRequest` per planned visual:

   ```python
   from scripts.visuals.styles.router import AssetRequest, route, style_matrix, moderator_move

   assets = [
       AssetRequest(id="v01", burning_question="...", infographic_type="quote",
                    audience="broad", platform="linkedin", data_density="low"),
       # ...one per planned visual
   ]
   ```

   - `infographic_type` ∈ `process | comparison | timeline | hierarchy | statistical |
     concept | checklist | quote | architecture | mood`.
   - `audience` ∈ `developer | tech-lead | architect | manager | exec | broad`.
   - `data_density` ∈ `low | medium | high`.

2. Route the whole package at once (diversity is enforced across the list, not per asset):

   ```python
   decisions = route(assets)           # [StyleDecision(id, style_id, renderer, rationale, guardrails)]
   matrix = style_matrix(decisions)    # {style_id: count} — the diversity histogram
   overlooked = moderator_move(decisions)  # one unused style worth trying, or None
   ```

3. Apply the **router logic** (Section 6), which `route()` already encodes:
   - hard numbers / scorecard → `data-exhibit`
   - flow / architecture / dependency graph → `diagram-as-code`
   - single quote / one big idea / hook → `typographic`
   - concept / "napkin" mental model / checklist → `hand-drawn`
   - "how it's built" / system anatomy → `blueprint`
   - mood / opener / metaphor (no data) → `editorial-illustration`
   - audience affinity (§5) breaks ties; **adjacent visuals must differ in style**.

4. **Moderator move (Co-STORM).** Always report `moderator_move(decisions)`. If it returns a
   style, name the one *overlooked* style and propose the single asset that could adopt it — do
   not silently accept the default routing when an easy variety win exists.

5. **Emit the package style matrix** into `content/visual-style-map.md` so the renderer
   dispatches by `style_id` and the reviewer can verify diversity *before* anything is
   rasterized. Each row: `asset id | style_id | renderer | rationale | guardrails`.

## Guardrails the router attaches per style

`route()` returns per-asset guardrails (`StyleDecision.guardrails`). Carry them into the
art-direction brief — e.g. `editorial-illustration` → **NO baked text, overlay only**;
`diagram-as-code` → **pre-render to PNG, opt-in engine required**; `hand-drawn` → **crisp
digits via path-effect Normal, edge-to-edge arrows**.

## Diversity rules (blocking)

- A package may **not** be single-style.
- Adjacent visuals may **not** share a style *and* theme.
- A series picks a **palette of 2–4 styles** and rotates; it does not use one.

## Handoff

Write the style matrix + moderator note into `content/visual-style-map.md`, then hand to
`infographic-art-director` (briefs carry the `style_id`) and `style-rendering` (drives the
adapter). The `visual-reviewer` reads the matrix for its pre-render diversity gate.
