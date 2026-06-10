---
name: visual-rendering
description: 'Generate visual assets for content — PNGs via matplotlib, SVGs via Python, and Mermaid diagrams. Use when creating charts, diagrams, infographics, or rebuilding visuals for blog posts and presentations.'
argument-hint: 'Describe the visuals needed (e.g., "comparison matrix for 5 model tiers")'
---

# Visual Rendering Skill

## When to Use

- Creating PNG charts/diagrams for blog posts or slides
- Generating SVG graphics for web embedding
- Building Mermaid flowcharts or timelines
- Rebuilding or updating existing visual assets

> **Not for AI-generated imagery.** This skill renders visuals **deterministically**. The one
> exception in the pipeline — AI-generated hero/illustrative imagery — is out of scope here and
> is handled by the `image-content-agent` (via the `vision-grounding` skill and
> `scripts.visuals.generated`), gated behind `image_generation: on`. Diagrams, infographics,
> charts, and exhibits are **always** programmatic and never AI-generated.

## Prerequisites

- Python 3.x with matplotlib installed
- Virtual environment at `.venv/` in workspace root

## Design Token System

All visuals MUST use the shared design token palette. See [token reference](./references/design-tokens.md) for the full color map.

## Preferred path: HTML/CSS + Chromium + browser-rendered QA (diagrams, flows, infographics, exhibits)

Hand-built coordinate/path math (Pillow polygons, SVG arc sweeps) is the root cause of recurring defects: inverted gauges, arrows that miss box edges, overlapping or clipped text, and type sizes wildly out of proportion with the article body. **Author these visuals as HTML/CSS and let Chromium's layout engine place everything, then gate through an automated Playwright/Chromium inspector before rasterizing to PNG.** CSS Flexbox/Grid removes the math; web fonts match the article; magnitude is shown with bars, never gauges.

Toolkit at `scripts/visuals/html/`:
- `design.py` — `css(theme)` (tokens as CSS vars + a fixed `TYPE_SCALE`) and `page(w, h, body_html, theme, pad)` wrapper. Every text element MUST carry a `data-role` (`display`/`title`/`value`/`subtitle`/`label`/`body`/`caption`); the role drives both its CSS size and the QA gate. Shared components: `.card`, `.bar-row`/`.bar-track`/`.bar-fill` (horizontal magnitude bars), `.badge`, `.flow`/`.connector` (straight line + CSS chevron), `.gap-callout`, `.eyebrow`, `.source`.
- `render.py` — `render_html_to_png` / `render_many`: clips the screenshot to `#stage` and rasterizes via Chromium at device scale 2, awaiting `document.fonts.ready` so Inter is loaded.
- `inspect.py` — `inspect_files(paths)` / CLI `python3 -m scripts.visuals.html.inspect <file.html> ...`: loads the DOM in Chromium and FAILS on: any computed font-size not in `TYPE_SCALE`, more than 7 distinct sizes, more than one focal `display` number, text that overflows its own box (clipped), content overflowing the canvas, stray internal labels (`02 / 10`, `EXHIBIT 1`, `Slide 3`), and a multi-step `.flow` with no connectors.

Mandatory rules (enforced by the inspector):
- **No gauges / no arcs.** Show magnitude with `.bar-row` horizontal bars or proportionate numbers. Semicircular gauges and hand-computed arcs are banned — they invert.
- **Typography is uniform and article-proportionate.** Only `TYPE_SCALE` roles; exactly one `display` focal number per asset; the largest non-focal text is the `title` (≈30px), sized so that at in-article display width (~1000px) diagram text is close to the article's 17px body / ~24px headings — never towering over it. Use Inter to match the blog.
- **Connectors mean transitions and stay flush.** Use `.flow .connector` (a strong-token line + chevron) attached directly to box edges. Never leave a gap between a box and its connector.
- **No internal numbering/labels.** Never emit slide counters (`02 / 10`), `EXHIBIT N`, or `Fig N` onto the image.

Workflow: author HTML via `design.page()` -> `inspect_files()` (must PASS) -> `render_many()` to PNG -> **view every PNG and zoom on bars/connectors** to confirm geometry (the inspector is necessary but not sufficient; a past inverted gauge passed DOM checks). A renderer that rasterizes before inspection PASSES is a process failure. Reference: `content/visuals/distilled/agent-eval-visual-first/render_html_pack.py`.

### Secondary path: SVG + browser QA (`scripts/visuals/svg/`)
Still available for cases that need explicit vector control (`python3 -m scripts.visuals.svg.inspect`). Same rules apply: `TYPE_SCALE` roles only, `connect()` for edge-to-edge arrows, no gauges, no stray labels. Prefer the HTML/CSS path for anything layout-heavy.

## Legacy path: Pillow/matplotlib (charts and comic/storyboard only)

## Procedure

### 1. Plan Visual Assets

Identify what's needed from the content outline:
- **PNGs** (320 DPI): comparison matrices, 2x2 tradeoff charts, timelines, frameworks, checklists
- **SVGs**: interactive/collapsible web graphics (tradeoff charts, decision funnels, checklist cards)
- **Mermaid** (`.mmd`): flowcharts, decision trees, process timelines
- **Comic/storyboard panels**: programmatic panel sequences, symbolic characters, speech bubbles, captions
- **Infographics/one-pagers**: metric cards, source lines, saveable summaries, LinkedIn cards

### 2. Generate PNGs with the right renderer

Use **Pillow (PIL)** for blog infographics, comparison panels, matrices, workflows, callout cards, and any visual with more than one text block. Use matplotlib only for true quantitative charts with axes.

For text-heavy blog visuals, create a Python renderer script at `content/visuals/render_<topic>.py` with measured text helpers (`textbbox`, wrapping, font fitting). Do not place text into a box unless it has been measured against that box first.

For new text-heavy or panel-based visuals, prefer reusable helpers from `scripts/visuals/`:
- `tokens.py` for palette and platform sizes
- `text_layout.py` for wrapping and font fitting
- `panels.py` for panel layouts
- `comic.py` for comic/storyboard primitives
- `infographic.py` for one-pager primitives
- `export.py` for DPI-safe PNG output

Mandatory for every renderer:
- Generate every `![...](visuals/*.png)` image referenced by the blog, not just the first few visuals.
- Use body labels >= 34 px for 320 DPI output, and bold all primary claims, labels, values, and section headers.
- Use a distinct composition pattern for adjacent visuals (split-screen, timeline, flow, scorecard, matrix, annotated scene, radial, dashboard). Reusing the same card grid/table pattern across a post is a review failure.
- Use high-contrast token combinations by default. Pale backgrounds are allowed only when paired with bold dark labels and strong borders.
- Keep one canonical series renderer when a multi-part series shares visuals. Per-part renderer files may exist only as compatibility wrappers that call the canonical renderer.
- Comic/storyboard visuals must be programmatic only. Use simple shapes, panels, captions, callouts, and speech bubbles; do not require external image generation.

### 3. Matplotlib template for quantitative charts only

Create a Python renderer script at `content/visuals/render_<topic>.py`:

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Base tokens (constant across all themes)
BASE_TOKENS = {
    'BG': '#ffffff', 'TEXT': '#1e293b', 'TEXT_2': '#475569',
    'MUTED': '#94a3b8', 'GRID': '#e5e7eb', 'LIGHT_BG': '#f8fafc',
}

# Theme palettes (cycle round-robin per visual)
THEMES = {
    'default':  {'ACCENT': '#1f6feb', 'ACCENT_2': '#0d9488', 'ACCENT_3': '#7c3aed',
                 'WARN': '#dc2626', 'SUCCESS': '#16a34a',
                 'BLUE_BG': '#dbeafe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2'},
    'ocean':    {'ACCENT': '#0ea5e9', 'ACCENT_2': '#06b6d4', 'ACCENT_3': '#155e75',
                 'WARN': '#f97316', 'SUCCESS': '#14b8a6',
                 'BLUE_BG': '#e0f2fe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#cffafe', 'RED_BG': '#ffedd5'},
    'sunset':   {'ACCENT': '#f97316', 'ACCENT_2': '#ef4444', 'ACCENT_3': '#b91c1c',
                 'WARN': '#dc2626', 'SUCCESS': '#eab308',
                 'BLUE_BG': '#fff7ed', 'TEAL_BG': '#fef3c7', 'PURPLE_BG': '#fee2e2', 'RED_BG': '#fef2f2'},
    'forest':   {'ACCENT': '#16a34a', 'ACCENT_2': '#65a30d', 'ACCENT_3': '#a16207',
                 'WARN': '#ca8a04', 'SUCCESS': '#15803d',
                 'BLUE_BG': '#f0fdf4', 'TEAL_BG': '#ecfccb', 'PURPLE_BG': '#fefce8', 'RED_BG': '#fef9c3'},
    'midnight': {'ACCENT': '#7c3aed', 'ACCENT_2': '#6366f1', 'ACCENT_3': '#8b5cf6',
                 'WARN': '#ec4899', 'SUCCESS': '#a78bfa',
                 'BLUE_BG': '#ede9fe', 'TEAL_BG': '#e0e7ff', 'PURPLE_BG': '#fae8ff', 'RED_BG': '#fce7f3'},
}

FONT = 'Helvetica Neue'
DPI = 320

def get_tokens(theme_name):
    return {**BASE_TOKENS, **THEMES[theme_name]}

# Each visual function accepts a tokens dict:
# def render_my_chart(tokens):
#     fig, ax = plt.subplots(...)
#     ax.set_facecolor(tokens['BG'])
#     ...
#     plt.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=tokens['BG'])

# Round-robin theme assignment:
# theme_names = list(THEMES.keys())
# for i, func in enumerate(visual_functions):
#     func(get_tokens(theme_names[i % len(theme_names)]))
```

Each visual gets its own function. Save with `plt.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])`.

### 4. Generate SVGs via Python

Create `content/visuals/write_svgs.py` — never use terminal heredoc for SVGs. Write SVG XML strings from Python using `with open(path, 'w') as f: f.write(svg_content)`.

### 5. Generate Mermaid Diagrams

Write `.mmd` files in `content/visuals/` using standard Mermaid syntax. Example:

```mermaid
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action]
    B -->|No| D[Alternative]
```

**MANDATORY — never ship a raw ` ```mermaid ` fence to a published page.** The
blog pages load no mermaid.js runtime, so a `<code class="language-mermaid">`
block renders as literal source text in the browser (this is a real defect that
shipped once). Always **pre-render the `.mmd` to a static, on-brand PNG** and
embed it as an `<img>`:

```bash
python3 -m scripts.visuals.html.render_mermaid \
  content/visuals/distilled/<dir>/<diagram>.mmd \
  content/visuals/distilled/<dir>/<diagram>.png
```

The renderer applies the design-token palette (use `classDef` in the `.mmd` for
gate/warn/success boxes) and rasterizes via our Chromium. In Markdown, replace
the fence with `![alt](visuals/.../<diagram>.png)`.

### 6. Run and Verify

```bash
cd content/visuals
python render_<topic>.py
python write_svgs.py
```

Verify:
- Every Markdown image reference resolves to an existing file.
- Every PNG is 320 DPI.
- Every referenced image was opened/inspected after rendering.
- No visible text overflow, clipping, overlap, tiny labels, or unbold primary labels.
- Adjacent visuals vary in theme and composition pattern.
- No Unicode glyph warnings.

**Published-page gate (run after web-publisher writes/updates any page):**

```bash
python3 -m scripts.visuals.html.check_published <pages-repo>/blog/*.html
```

Exit code is non-zero if any page contains a raw diagram fence/`language-*`
block with no matching runtime — i.e. anything that would show as code instead
of a rendered diagram. This closes the gap that the `#stage` inspector does not
cover (it only checks generated assets, never the published HTML).

## Critical Rules

- **No Unicode glyphs in matplotlib**: use `->` not `→`, `[x]` not `✓`
- **SVGs via Python only**: heredoc causes encoding corruption
- **Consistent palette**: every visual must use the shared tokens
- **320 DPI**: non-negotiable for all PNG output
- **Ask before assuming style**: if the user criticizes visual aesthetics or asks for creative improvement, ask for rebuild scope, design direction, color policy, diagram-pattern preferences, and typography density before rendering.
- **Text-heavy visuals use Pillow**: use `textbbox()`/font fitting for cards, tables, workflows, matrices, scorecards, and infographics. Do not approve matplotlib or unmeasured text placement for these.
- **Review is blocking**: visual review must fail on text overflow, clipped elements, small/unbold typography, excessive whitespace, or repetitive shape/color patterns.
