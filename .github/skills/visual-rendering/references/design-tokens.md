# Design Token Reference

All visual assets in this project share a unified design token system for colors, typography, and output quality.

## Color Palette

| Token | Hex | Role |
|-------|-----|------|
| `BG` | `#ffffff` | Background |
| `ACCENT` | `#1f6feb` | Primary accent (blue) |
| `ACCENT_2` | `#0d9488` | Secondary accent (teal) |
| `ACCENT_3` | `#7c3aed` | Tertiary accent (purple) |
| `WARN` | `#dc2626` | Warning/attention (red) |
| `SUCCESS` | `#16a34a` | Positive indicator (green) |
| `TEXT` | `#1e293b` | Primary text |
| `TEXT_2` | `#475569` | Secondary text |
| `MUTED` | `#94a3b8` | Muted text/borders |
| `GRID` | `#e5e7eb` | Grid lines/dividers |
| `LIGHT_BG` | `#f8fafc` | Card/panel background |
| `BLUE_BG` | `#dbeafe` | Blue highlight region |
| `TEAL_BG` | `#ccfbf1` | Teal highlight region |
| `PURPLE_BG` | `#ede9fe` | Purple highlight region |
| `RED_BG` | `#fee2e2` | Red/warning highlight region |

## Python Dict (Copy-Paste)

```python
TOKENS = {
    'BG': '#ffffff',       'ACCENT': '#1f6feb',   'ACCENT_2': '#0d9488',
    'ACCENT_3': '#7c3aed', 'WARN': '#dc2626',     'SUCCESS': '#16a34a',
    'TEXT': '#1e293b',      'TEXT_2': '#475569',    'MUTED': '#94a3b8',
    'GRID': '#e5e7eb',      'LIGHT_BG': '#f8fafc',  'BLUE_BG': '#dbeafe',
    'TEAL_BG': '#ccfbf1',   'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2',
}
```

## Typography

- **Font**: Helvetica Neue (fallback: sans-serif)
- **Title size**: 16–18pt
- **Body size**: 10–12pt
- **Label size**: 8–9pt

## Output

- **DPI**: 320 (all PNGs)
- **Format**: PNG with transparent or white background
- **Save**: `plt.savefig(path, dpi=320, bbox_inches='tight', facecolor='#ffffff')`

## Known Issues

- **No Unicode glyphs in matplotlib**: Characters like →, ✓, ✗ cause rendering warnings. Use ASCII: `->`, `[x]`, `[ ]`
- **SVG via Python only**: Writing SVGs with shell heredoc causes encoding corruption. Always use Python `open()` + `write()`.
