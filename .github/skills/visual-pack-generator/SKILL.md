---
name: visual-pack-generator
description: 'Generate platform-optimized visual asset packs from blog content for visual-first distilled posts. Supports Practitioner (carousel) and Executive (exhibit) persona modes. Use when distillation_persona_mode is set in pipeline-config.md and distribution agents need visual assets.'
argument-hint: 'Provide the blog file path, part number (e.g. part1), and persona mode (practitioner or executive)'
---

# Visual Pack Generator Skill

## When to Use

- Generating visual asset packs for distilled social distribution of a blog post
- Creating LinkedIn carousel slides (Practitioner mode) or executive exhibit charts (Executive mode)
- Producing platform-specific hero images, inline images, and X/Twitter image cards
- When `distillation_persona_mode` is set to `practitioner` or `executive` in `content/pipeline-config.md`
- When distribution agents (social-linkedin, social-twitter, platform-distiller) request visual assets for a distilled post

## Inputs

- **Blog file path**: Path to the source blog post (e.g. `content/part1-blog.md`)
- **Part number / slug**: Short identifier used in output directory naming (e.g. `part1`)
- **Persona mode**: Read from `content/pipeline-config.md` key `distillation_persona_mode` — values: `practitioner`, `executive`, or `ask` (prompt user when `ask` is set)

## Procedure

### 1. Extract Content from Blog Post

Read the source blog post and extract:

- **Title** and **subtitle** (used for hook slide/exhibit label)
- **Key data points**: numbers, percentages, benchmarks, case study metrics (e.g. "68% cost reduction", "$2K/day waste")
- **Framework or taxonomy structure**: named models, step sequences, decision trees, priority matrices
- **Visual asset references**: file paths to existing PNGs already in `content/visuals/` that may be recomposed as source material

### 2. Read Persona Mode from Pipeline Config

Open `content/pipeline-config.md` and read the `distillation_persona_mode` key:

- `practitioner` → proceed with Practitioner mode (10-slide carousel grammar)
- `executive` → proceed with Executive mode (3-5 exhibit grammar)
- `ask` → pause and prompt the user: *"Which persona mode should I use for this distillation? Type `practitioner` (carousel for LinkedIn/X) or `executive` (exhibit charts for LinkedIn Article/Medium)."*

### 3. Load Slide Grammar

Load `.github/skills/visual-pack-generator/references/slide-grammar.md` and select the grammar table for the chosen persona mode:

- **Practitioner**: 10-slide carousel grammar (position, slide type, content, psychology framework, visual treatment)
- **Executive**: 3-5 exhibit grammar (position, exhibit type, content, design convention, visual treatment)

Use the hook archetypes section to select the strongest hook for the blog's content.

### 4. Load Platform Specs

Load `.github/skills/visual-pack-generator/references/platform-specs.md` and identify the required asset dimensions and file counts for each platform being generated:

| Mode | Platforms |
|------|-----------|
| Practitioner | LinkedIn carousel, X/Twitter image thread, Medium article, Substack Note |
| Executive | LinkedIn Article, X/Twitter image thread, Medium article, Substack Note |

### 5. Generate Visual Asset Pack

Invoke `visual-renderer` agent capabilities to generate all required assets. Use round-robin theme assignment from the 5 themes (`default`, `ocean`, `sunset`, `forest`, `midnight`) — assign sequentially to slides/exhibits.

**Practitioner mode — required assets:**

| Asset | Dimensions | Count | Purpose |
|-------|-----------|-------|---------|
| Carousel slides | 1080×1080 px | 10 | LinkedIn document post (carousel) |
| X/Twitter image cards | 1600×900 px | 4 | X/Twitter image thread |
| Medium hero | 1400×800 px | 1 | Medium article hero image |
| Medium inline images | 1200×800 px | 2 | Medium inline supporting visuals |
| Substack hero | 1200×630 px | 1 | Substack Note hero |
| LinkedIn Article exhibits | 1200×627 px | 2 | LinkedIn Article inline exhibits |

**Executive mode — required assets:**

| Asset | Dimensions | Count | Purpose |
|-------|-----------|-------|---------|
| Exhibits | 1200×627 px | 3–5 | LinkedIn Article inline + hero |
| X/Twitter exhibit images | 1600×900 px | 2 | X/Twitter image thread |
| Medium hero | 1400×800 px | 1 | Medium article hero image |
| Medium inline exhibit | 1200×800 px | 1 | Medium inline exhibit |
| Substack hero | 1200×630 px | 1 | Substack Note hero |

Apply psychology frameworks from `.github/skills/visual-pack-generator/references/psychology-stack.md` to each slide/exhibit position as specified in the grammar.

### 6. Save All Assets

Save all generated PNG files to:

```
content/visuals/distilled/{slug}-{mode}/
```

Where `{slug}` is the part identifier (e.g. `part1`) and `{mode}` is the persona mode (e.g. `practitioner` or `executive`).

Example: `content/visuals/distilled/part1-practitioner/`

File naming convention:

- Carousel slides: `slide-01-hook.png`, `slide-02-promise.png`, `slide-03-problem.png`, `slide-04-framework.png`, `slide-05-step1.png`, `slide-06-step2.png`, `slide-07-step3.png`, `slide-08-interrupt.png`, `slide-09-recap.png`, `slide-10-cta.png`
- X/Twitter cards: `x-card-01.png`, `x-card-02.png`, `x-card-03.png`, `x-card-04.png`
- Medium hero: `medium-hero.png`
- Medium inline: `medium-inline-01.png`, `medium-inline-02.png`
- Substack hero: `substack-hero.png`
- LinkedIn Article exhibits: `linkedin-exhibit-01.png`, `linkedin-exhibit-02.png`
- Executive exhibits: `exhibit-01.png`, …, `exhibit-05.png`

### 7. Generate Manifest and Renderer Script

**Manifest** — create `content/visuals/distilled/{slug}-{mode}/manifest.md`:

```markdown
# Visual Pack Manifest: {slug}-{mode}

Generated: {ISO date}
Blog source: {blog file path}
Persona mode: {practitioner | executive}

## Asset Inventory

| File | Dimensions | Platform | Slide/Exhibit Type |
|------|-----------|----------|--------------------|
| slide-01.png | 1080x1080 | LinkedIn carousel | Hook |
| ...           | ...        | ...      | ...  |

## Theme Assignment

| Asset | Theme |
|-------|-------|
| slide-01.png | default |
| ...           | ...     |

## Usage Notes

- LinkedIn: Upload slides as PDF document post. Place canonical URL in first comment within 60 sec.
- X/Twitter: Use x-card-*.png for image-anchored tweets. Canonical URL in last tweet only.
- Medium: Use medium-hero.png as hero. Import via https://medium.com/p/import to preserve rel=canonical.
- Substack: Post as Substack NOTE (not newsletter). Use substack-hero.png.
```

**Renderer script** — create `content/visuals/distilled/{slug}-{mode}/render_distilled.py`:

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BASE_TOKENS = {
    'BG': '#ffffff', 'TEXT': '#1e293b', 'TEXT_2': '#475569',
    'MUTED': '#94a3b8', 'GRID': '#e5e7eb', 'LIGHT_BG': '#f8fafc',
}

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

# Each visual is a standalone function accepting a tokens dict.
# Example structure (replace with actual generated functions):
# def render_slide_01(tokens):
#     fig, ax = plt.subplots(figsize=(10.8, 10.8))
#     ax.set_facecolor(tokens['TEXT'])   # dark background for hook
#     fig.patch.set_facecolor(tokens['TEXT'])
#     # ... draw content ...
#     plt.savefig('slide-01-hook.png', dpi=DPI, facecolor=tokens['TEXT'])  # bbox_inches omitted intentionally — causes dimension overflow at 320 DPI
#     plt.close()

if __name__ == '__main__':
    theme_names = list(THEMES.keys())
    # visual_functions list is populated by the generator
    visual_functions = []
    for i, func in enumerate(visual_functions):
        func(get_tokens(theme_names[i % len(theme_names)]))
    print(f"Rendered {len(visual_functions)} assets.")
```

## Output

After execution, the following directory structure is created:

```
content/visuals/distilled/
  {slug}-{mode}/                        # e.g. part1-practitioner/
    manifest.md                         # Asset inventory and usage notes
    render_distilled.py                 # Python renderer script (matplotlib)
    slide-01-hook.png                   # Hook slide (Practitioner)
    slide-02-promise.png                # Promise slide
    ...
    slide-10-cta.png                    # CTA slide
    x-card-01.png                       # X/Twitter image card 1
    x-card-02.png
    x-card-03.png
    x-card-04.png
    medium-hero.png                     # Medium hero image (1400x800)
    medium-inline-01.png                # Medium inline image 1
    medium-inline-02.png                # Medium inline image 2 (Practitioner)
    substack-hero.png                   # Substack Note hero (1200x630)
    linkedin-exhibit-01.png             # LinkedIn Article exhibit 1 (Practitioner)
    linkedin-exhibit-02.png             # LinkedIn Article exhibit 2 (Practitioner)
    exhibit-01.png                      # Executive exhibit 1 (Executive mode)
    ...                                 # exhibit-02 through exhibit-05 (Executive mode)
```

## Critical Rules

- **Design token system**: All visuals MUST use the 15 shared tokens from `.github/copilot-instructions.md` — never introduce ad-hoc hex colors
- **320 DPI mandatory**: All PNG output uses `dpi=320` in `plt.savefig()` — non-negotiable
- **Font**: Helvetica Neue throughout — no serif fonts, no system fallbacks
- **No Unicode glyphs in matplotlib**: Use ASCII equivalents (`->` not `→`, `[x]` not `✓`, `[ ]` not `☐`, `--` not `—`)
- **Standalone functions**: Each slide/exhibit is a standalone Python function accepting a `tokens` dict — no shared state between functions
- **Practitioner palette**: 3-color max per slide — white BG (`#ffffff`) + dark text (`#1e293b`) + ONE brand accent (`#1f6feb`). Pattern interrupt slides use dark BG (`#1e293b`) as an intentional exception
- **Executive palette**: 2-3 colors max per exhibit — navy (`#051C2C`) + one accent + gray series. No decorative color
- **Round-robin themes**: Assign themes sequentially from `[default, ocean, sunset, forest, midnight]` cycling — index `i % 5`
- **Standalone comprehension**: Every slide/exhibit must be fully comprehensible on its own — no cross-reference language ("as shown above", "from the previous slide", "as we discussed")
- **Source attribution**: Every data point and statistic on a slide/exhibit must include source and year (e.g. `Source: Anthropic, 2025`) — never an unattributed number
- **Executive mode CTA rule**: CTA copy never appears on Executive exhibit visuals — place CTA only in caption text or post body copy
- **Recomposition allowed**: Existing blog PNGs in `content/visuals/` may be used as source material for recomposition into new assets — do not duplicate renders when a base asset can be adapted
- **Body text limit**: Max 30-50 words per slide/exhibit body text — split into two slides if content exceeds this
- **One insight per slide**: Each slide/exhibit carries exactly one big idea — no multi-point slides outside the Recap position
