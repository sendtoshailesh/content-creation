---
description: "Use when generating or editing visual assets — PNGs, SVGs, Mermaid diagrams, or Python renderers. Enforces design token system and rendering standards."
applyTo: "content/visuals/**"
---

# Visual Asset Standards

## Design Tokens

```python
TOKENS = {
    'BG': '#ffffff',       'ACCENT': '#1f6feb',   'ACCENT_2': '#0d9488',
    'ACCENT_3': '#7c3aed', 'WARN': '#dc2626',     'SUCCESS': '#16a34a',
    'TEXT': '#1e293b',      'TEXT_2': '#475569',    'MUTED': '#94a3b8',
    'GRID': '#e5e7eb',      'LIGHT_BG': '#f8fafc',  'BLUE_BG': '#dbeafe',
    'TEAL_BG': '#ccfbf1',   'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2',
}
```

## Rendering Rules

- **DPI**: 320 for all PNG output
- **Font**: Helvetica Neue (fall back to sans-serif)
- **No Unicode glyphs** in matplotlib: use `->` not `→`, `[x]` not `✓`, `[ ]` not `✗`
- **SVGs**: Generate via Python script, never terminal heredoc
- **Mermaid**: Use `.mmd` extension, standard Mermaid syntax
- **All images** must share consistent color palette from tokens above
