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

## Tool Selection

| Visual type | Tool | When |
|------------|------|------|
| Data charts (bar, line, scatter, pie) | **matplotlib** | Quantitative data with axes |
| Infographic layouts, dashboards, cards | **Pillow (PIL)** | Pixel-precise text, complex multi-panel layouts |
| Simple flow diagrams (< 10 nodes) | **matplotlib** patches | Decision trees, process flows |
| Complex flowcharts (10+ nodes) | **Mermaid** (.mmd) | Architecture diagrams, dependency graphs |
| Comparison tables, matrices | **Pillow (PIL)** | Precise column alignment, cell backgrounds |

### Pillow (PIL) Usage

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
