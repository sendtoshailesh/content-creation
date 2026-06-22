---
description: "Use when generating or editing visual assets — PNGs, SVGs, Mermaid diagrams, or Python renderers. Enforces design token system and rendering standards."
applyTo: "content/visuals/**"
---

# Visual Asset Standards

## Design Tokens

### Base Tokens (shared across all themes)

```python
BASE_TOKENS = {
    'BG': '#ffffff',       'TEXT': '#1e293b',      'TEXT_2': '#475569',
    'MUTED': '#94a3b8',    'GRID': '#e5e7eb',      'LIGHT_BG': '#f8fafc',
}
FONT = 'Helvetica Neue'
DPI = 320
```

### Theme Palettes

Each visual in a post should use a **different** theme. Cycle through themes round-robin (theme index = visual number % theme count). Base tokens (BG, TEXT, TEXT_2, MUTED, GRID, LIGHT_BG, FONT, DPI) stay constant across all themes for readability.

```python
THEMES = {
    'default': {
        'ACCENT': '#1f6feb', 'ACCENT_2': '#0d9488', 'ACCENT_3': '#7c3aed',
        'WARN': '#dc2626', 'SUCCESS': '#16a34a',
        'BLUE_BG': '#dbeafe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2',
    },
    'ocean': {
        'ACCENT': '#0ea5e9', 'ACCENT_2': '#06b6d4', 'ACCENT_3': '#155e75',
        'WARN': '#f97316', 'SUCCESS': '#14b8a6',
        'BLUE_BG': '#e0f2fe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#cffafe', 'RED_BG': '#ffedd5',
    },
    'sunset': {
        'ACCENT': '#f97316', 'ACCENT_2': '#ef4444', 'ACCENT_3': '#b91c1c',
        'WARN': '#dc2626', 'SUCCESS': '#eab308',
        'BLUE_BG': '#fff7ed', 'TEAL_BG': '#fef3c7', 'PURPLE_BG': '#fee2e2', 'RED_BG': '#fef2f2',
    },
    'forest': {
        'ACCENT': '#16a34a', 'ACCENT_2': '#65a30d', 'ACCENT_3': '#a16207',
        'WARN': '#ca8a04', 'SUCCESS': '#15803d',
        'BLUE_BG': '#f0fdf4', 'TEAL_BG': '#ecfccb', 'PURPLE_BG': '#fefce8', 'RED_BG': '#fef9c3',
    },
    'midnight': {
        'ACCENT': '#7c3aed', 'ACCENT_2': '#6366f1', 'ACCENT_3': '#8b5cf6',
        'WARN': '#ec4899', 'SUCCESS': '#a78bfa',
        'BLUE_BG': '#ede9fe', 'TEAL_BG': '#e0e7ff', 'PURPLE_BG': '#fae8ff', 'RED_BG': '#fce7f3',
    },
}
```

### How to Use Themes in Renderers

```python
import random

def get_tokens(theme_name=None):
    \"\"\"Return merged BASE_TOKENS + theme palette.\"\"\"
    theme = THEMES.get(theme_name or random.choice(list(THEMES.keys())))
    return {**BASE_TOKENS, **theme}

# Round-robin for multiple visuals in a post:
theme_names = list(THEMES.keys())
for i, visual_func in enumerate(visual_functions):
    tokens = get_tokens(theme_names[i % len(theme_names)])
    visual_func(tokens)
```

## Rendering Rules

- **DPI**: 320 for all PNG output
- **Font**: Helvetica Neue (fall back to sans-serif)
- **No Unicode glyphs** in matplotlib: use `->` not `→`, `[x]` not `✓`, `[ ]` not `✗`
- **SVGs**: Generate via Python script, never terminal heredoc
- **Mermaid**: Use `.mmd` extension, standard Mermaid syntax
- **Theme diversity**: Each visual in a blog post uses a different theme from the palette list. Cycle round-robin.
- **Base tokens are constant**: BG, TEXT, TEXT_2, MUTED, GRID, LIGHT_BG, FONT, DPI never change between themes
- **Text-heavy visuals use Pillow**: Comparison panels, matrices, workflows, scorecards, tables, and infographics must use Pillow or another measured-text renderer. Matplotlib is only for true quantitative charts.
- **Measured text is mandatory**: Use `textbbox()`/wrapping/font-fitting before drawing text into any bounded area.
- **Large bold typography**: Body labels should be >= 34 px at 320 DPI. Primary claims, values, labels, and section headers must be bold.
- **Pattern diversity blocks publishing**: A post must not repeat the same card grid/table/flow pattern across multiple visuals. Adjacent visuals must differ in composition and theme.
- **Series renderer consistency**: Multi-part series should use one canonical renderer for all shared visuals; per-part renderers should wrap the canonical renderer rather than diverging.

## Narrow Segment Rule

For any chart element that occupies < 15% of total width/height:
- Do NOT place text labels inside the segment (they will overflow or be unreadable)
- Use external labels with leader lines (thin connecting lines from label to segment)
- Only short values (numbers) go inside narrow segments; descriptive labels go outside
- For pie chart slices < 5%, use a legend table

## AI-Generated Imagery (scoped exception to programmatic-only rendering)

Visuals in this pipeline are rendered **deterministically/programmatically** (HTML/CSS+Chromium,
SVG, matplotlib, Pillow). The **only** exception is the `AI-generated imagery` visual family,
used **solely** for hero / backdrop / scene / conceptual-illustration assets that carry mood,
not information. It is produced by `image-content-agent` via `scripts.visuals.generated` and the
`vision-grounding` + `creative-brief` skills, and is gated behind `image_generation: on` in
`content/pipeline-config.md`.

Hard rules for AI-generated images (all enforced at `visual-reviewer`):
- **Never** use AI generation for diagrams, charts, infographics, comparison matrices,
  comic/storyboards, card packs, or executive exhibits — those stay programmatic and keep their
  inspector gates.
- **No embedded text** of any kind in the generated pixels. Text/labels are overlaid
  programmatically over the reserved ~30% negative space.
- **Brand-color fidelity**: honor the design-token palette; no hue substitution.
- Every generated image lives in `content/visuals/generated/` with a sidecar JSON (provider,
  model, prompt, size, quality, cache key/seed) for reproducibility, and must pass
  `visual-reviewer` section 9 (`image-no-text`, `image-fidelity`, `safety`) before publishing.

## Stack Selection (Python vs JS, per visual type)

> Decided by web research + an empirical head-to-head render test (see plan/session evidence).
> The pipeline already renders via headless Chromium, so JS frameworks are allowed **only** as a
> server-side pre-render to static PNG/SVG — **never** as client JS on published pages.

| Visual type | Primary stack | Notes |
|------------|---------------|-------|
| Data charts (bar, line, scatter, pie) | **matplotlib** | Convention; native export; no animation trap |
| Advanced charts (sankey, treemap, network/graph, calendar/heatmap, non-gauge radial) | **JS bridge** — `scripts.visuals.charts_js.echarts_render` (ECharts → Chromium PNG) | Opt-in; `animation:false` enforced; matplotlib does these poorly |
| Infographics / one-pagers / exhibits / layouts | **HTML/CSS + Chromium** (`scripts/visuals/html/`) | Best text fidelity; not Pillow |
| Comparison tables, matrices | **HTML/CSS + Chromium** | CSS grid/flex; not hand-math |
| Architecture / flow / sequence diagrams | **Mermaid (.mmd) → PNG**; **Graphviz (DOT) → PNG** for dense/complex | D3 never (interactive only) |
| Hero / backdrop / illustrative | **`scripts.visuals.generated.programmatic`** (default) or AI (opt-in) | Text overlay composited as a CSS layer, not baked into pixels |
| Comics / storyboards | **HTML/CSS + Chromium** for caption/speech text; SVG/CSS shapes for panels | Pillow only for pure raster shape work |

### Hard rules

- **Static-only:** every visual is pre-rendered to PNG/SVG; published GitHub Pages load no client JS (Mermaid is pre-rendered, never shipped as a live `mermaid` fence).
- **JS charts must set `animation:false`** (an animated chart screenshotted mid-flight exports silently-wrong bar heights) and pass the deterministic guard in the bridge.
- **Text-heavy → browser text** (HTML/CSS + Chromium). Do not place complex text with Pillow or hand-authored SVG math.
- **Compositing:** overlay hero/illustrative text as a CSS layer in the same Chromium render (e.g. `programmatic.render_hero(..., title=...)`), never re-typeset over a raster with Pillow.
- **matplotlib stays the default** for standard quantitative charts.

### Diagrams: Mermaid vs Graphviz

- **Mermaid** (`.mmd` → PNG via `scripts.visuals.html.render_mermaid`): default for standard flowcharts/sequence/architecture; quick and version-controllable.
- **Graphviz/DOT** (`dot -Tpng`): use for **dense or complex** static graphs where Mermaid's layout control is insufficient. Requires the `graphviz` system package (`brew install graphviz` / `apt-get install graphviz`). Author the `.dot`, render to PNG, then gate through `visual-reviewer`.

## Visual Style Axis (how it looks, not just what it says)

Every visual carries **two independent choices**: the infographic **TYPE** (process, comparison,
timeline, hierarchy, statistical, concept, checklist, quote — the existing router) **×** the
visual **STYLE / MEDIUM**. Type and style are decoupled: a process diagram can render as a clean
exhibit, a hand-drawn sketch, or an isometric blueprint. The `visual-style-router` skill assigns
a `style_id` per asset; the `visual-renderer` dispatches via `scripts.visuals.styles.STYLE_REGISTRY`.
See `agents-and-skills/visual-versatility-system.md`.

| `style_id` | Renderer / adapter | Best for | Hard rule |
|---|---|---|---|
| `data-exhibit` | `scripts/visuals/html` (Chromium) | hard numbers, scorecards | bars not gauges; one focal number |
| `typographic` | `scripts.visuals.styles.typographic` | quotes, single big ideas, hooks | `display` TYPE_SCALE role; ≤ 12 words |
| `hand-drawn` | `sketch_rough` (Rough.js) + `sketch_mpl` (xkcd) | concepts, napkin explainers | crisp digits (`patheffects.Normal()`); edge-to-edge arrows |
| `blueprint` | `scripts.visuals.styles.blueprint` | system anatomy, "how it's built" | mono labels; no baked slide numbers |
| `editorial-illustration` | `scripts.visuals.styles.editorial` | mood, openers, metaphors | **NO baked text — overlay only**; ~30% negative space |
| `diagram-as-code` | `scripts.visuals.styles.diagram_as_code` | pipelines, dependency graphs | opt-in engine; **pre-render to PNG**, no live JS |

### Style rules (blocking at `visual-reviewer`)

- **Adjacent visuals must differ in style**, not just theme. A package may **not** be all
  `data-exhibit` (single-style is a critical failure).
- A series picks a **style palette of 2–4** and rotates; it never uses one.
- Two **near-duplicate compositions** (same grid/bar/card skeleton) are blocked even across
  different styles — force a re-style (STORM polish / Co-STORM `reorganize()`).
- `diagram-as-code` engines are **opt-in / offline once installed** (`brew install d2` /
  `brew install graphviz` / `npm install -g @mermaid-js/mermaid-cli`); the adapter raises a clear
  install hint rather than silently changing the look.
- The Rough.js bridge loads its ES module as a base64 `data:` URL (file:// module imports are
  CORS-blocked); the xkcd path-filter corrupts isolated bold digits, so disable the sketch
  per-digit with `text.set_path_effects([matplotlib.patheffects.Normal()])`.

## Legacy tool notes (Pillow / matplotlib)

Use Pillow when text placement precision is critical. Key advantage: `textbbox()` measures exact pixel dimensions BEFORE rendering, preventing overflow.

```python
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 3200, 2080  # 320 DPI = 10" x 6.5"
img = Image.new('RGB', (WIDTH, HEIGHT), '#ffffff')
draw = ImageDraw.Draw(img)

# Measure text before placing
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
# Now verify it fits the container before committing
```

## Information Design Principles

1. **Data-ink ratio** (Tufte): Maximize data ink, minimize chartjunk
2. **Visual hierarchy**: Most important insight = largest/boldest treatment
3. **Color semantics**: Green = positive, Red = warning, Blue = neutral (consistent across all visuals)
4. **Annotation-first**: Key takeaways directly on the visual, not left to inference
5. **Standalone clarity**: Every visual understandable without reading the blog section
6. **Gestalt grouping**: Proximity and enclosure for related elements; whitespace separates concepts

## Visual Review

All rendered visuals must pass rubber-duck review by the `visual-reviewer` agent before publishing. The reviewer must open and inspect every Markdown-referenced image, verify it exists at 320 DPI, and fail the review for text overflow, overlap, clipping, tiny/unbold typography, excessive whitespace, or repetitive color/shape/layout patterns. See `visual-review` skill for the full checklist.

## Visual Diversity and Typography

- Ask clarifying questions before rebuilding visuals when the user is asking for aesthetic changes; do not assume style direction.
- Every visual in a post should have a distinct layout pattern or composition. Avoid repeated card grids, repeated row tables, and same-looking color themes across a series.
- Use large, bold typography for primary claims and labels. Body labels should generally be at least 11pt equivalent; reduce copy before reducing readability.
- Measure text before rendering. For infographic layouts, prefer Pillow with `textbbox()` so text cannot overflow boxes.
