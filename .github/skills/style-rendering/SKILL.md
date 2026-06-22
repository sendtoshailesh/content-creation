---
name: style-rendering
description: 'Drive the six style adapters (data-exhibit, typographic, hand-drawn via Rough.js/xkcd, blueprint, editorial-illustration, diagram-as-code via D2/Mermaid/Graphviz) with shared design tokens and the existing inspector/reviewer gates. Use when rendering a visual pack whose style_ids were chosen by visual-style-router.'
argument-hint: 'Provide the style matrix (asset id -> style_id) from content/visual-style-map.md'
---

# Style Rendering Skill

Turns a routed style matrix into PNGs. Each `style_id` maps to a concrete adapter under
`scripts/visuals/styles/`; all adapters share design tokens, render at device-scale 2, and pass
through the **same** gates as today (Chromium DOM inspector for HTML/SVG, view-and-zoom for
every PNG). This is the rendering half of the Visual Versatility System
(`agents-and-skills/visual-versatility-system.md` §4, §9). It does **not** replace
`visual-rendering` for plain data-exhibits — it adds the other five mediums behind the same gates.

## Dispatch table

```python
from scripts.visuals.styles import STYLE_REGISTRY  # style_id -> {renderer, module, entrypoints}
```

| `style_id` | Adapter entrypoint(s) | Install needed |
|---|---|---|
| `data-exhibit` | existing `scripts/visuals/html` `page()` builder | none |
| `typographic` | `styles.typographic.typographic_quote` | none |
| `hand-drawn` | `styles.sketch_rough.sketch_anatomy` / `sketch_flow_pipeline`; `styles.sketch_mpl.sketch_maturity_steps` / `sketch_checklist` | Rough.js: `npm install` in `scripts/visuals/charts_js` |
| `blueprint` | `styles.blueprint.blueprint_hub_and_beams` | none |
| `editorial-illustration` | `styles.editorial.editorial_guardrail` | none |
| `diagram-as-code` | `styles.diagram_as_code.render_diagram` | opt-in engine (see below) |

## Per-style how-to

### data-exhibit (HTML/CSS + Chromium)

Unchanged from `visual-rendering`: author with `scripts/visuals/html/design.py` (`page()`,
`css()`, `data-role` typography, `.bar-row`, `.flow`/`.connector`), inspect with
`python3 -m scripts.visuals.html.inspect <file.html>` (must PASS), rasterize with
`scripts/visuals/html/render.py`. Bars not gauges, one focal number.

### typographic (text-as-art)

`typographic_quote(out, kicker=, quote=, accent_word=, context=, source=, theme=)`. One giant
background glyph + one accent word; ≤ 12 words of quote; uses the `display` TYPE_SCALE role.

### hand-drawn (Rough.js + matplotlib xkcd)

- Diagrams/flows → Rough.js: `sketch_anatomy(...)`, `sketch_flow_pipeline(...)`. Rough.js loads
  as a **base64 `data:` module** (file:// ES-module imports are CORS-blocked — origin `null`;
  the `data:` scheme is allowed).
- Charts/checklists/steps → matplotlib `xkcd()`: `sketch_maturity_steps(...)`,
  `sketch_checklist(...)`.
- **xkcd digit fix (mandatory):** the sketch path-filter corrupts isolated bold digits. Disable
  the sketch per-artist for the digit only: `txt.set_path_effects([matplotlib.patheffects.Normal()])`.
  Do **not** use `set_sketch_params(None)` (= inherit) or global `rcParams['path.sketch']=None`
  (= flattens everything).

### blueprint (dark schematic)

`blueprint_hub_and_beams(out, title=, subtitle=, center_label=, beams=[(name,desc,metric)], source=, theme=)`.
Dark navy surface, SVG grid, mono labels. No baked slide numbers.

### editorial-illustration (metaphor scene)

`editorial_guardrail(out, kicker=, title=, formula=, gap_note=, source=, theme=)`. Flat-vector
metaphor lane on the left, copy panel on the right. **All text is real DOM / overlay — never
baked into pixels** (the AI-imagery rule applies to any illustration medium).

### diagram-as-code (D2 / Mermaid / Graphviz, opt-in)

```python
from scripts.visuals.styles.diagram_as_code import render_diagram, available_engine
render_diagram(out, source=<d2_or_dot_or_mermaid_text>, lang="d2", sketch=True, theme="default")
```

- Auto-detects an engine in preference order **d2 → dot → mmdc**; raises a clear install hint if
  none is present (`brew install d2` / `brew install graphviz` /
  `npm install -g @mermaid-js/mermaid-cli`). It never silently falls back to a different look.
- D2 `--sketch` gives a hand-drawn theme; Graphviz renders dense graphs at 320 DPI; Mermaid
  covers standard flow/sequence/class. All **pre-render to a static PNG** — no client JS ever
  ships to a published page.

## Shared gates (unchanged)

1. Design tokens only (`scripts/visuals/tokens.py`); Helvetica Neue; 320 DPI.
2. HTML/SVG-sourced assets: Chromium DOM inspector **must PASS** before rasterizing.
3. **View every PNG and zoom** on bars/connectors/digits — the inspector is necessary, not
   sufficient.
4. No stray internal labels (`02 / 10`, `EXHIBIT 1`); no gauges/arcs.

## Diversity check before finishing

Render the **whole routed matrix**, then confirm the package is multi-style and no two adjacent
visuals share style + theme. Hand the set to `visual-reviewer`, which runs the post-render
diversity + near-duplicate dedup gate.
