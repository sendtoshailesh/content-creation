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
