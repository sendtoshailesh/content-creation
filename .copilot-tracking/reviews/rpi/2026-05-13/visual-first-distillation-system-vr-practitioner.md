<!-- markdownlint-disable-file -->
# Visual Review: Practitioner Pack (Part 1)
**Date:** 2026-05-13
**Assets reviewed:** 20 PNGs from `content/visuals/distilled/part1-practitioner/`
**Verdict:** ❌ FAIL — All 20 assets blocked; 2 systemic root causes affect every asset

---

## Systemic Root Causes

### Root Cause 1 — Font/DPI coordinate-system mismatch (affects all 20 assets)

`make_fig()` sets `ax.set_xlim(0, w_px)` / `ax.set_ylim(0, h_px)` — pixel-space coordinates. But Matplotlib `fontsize` is always in typographic points. At DPI=320, a 1080×1080 slide is 3.375 × 3.375 inches. A 108pt font = 1.5 inches tall. "120x" (4 chars) renders ≈1,248 px wide on a 1,080 px canvas — overflowing 84 px per side. Every large-fontsize element across all 20 assets has this defect.

| Text | fontsize (pt) | Rendered width (px) | Canvas (px) | Overflow |
|------|--------------|---------------------|-------------|---------|
| `"120x"` (slide-01) | 108 | 1,248 | 1,080 | **168 px** |
| `"120x Problem"` (medium-hero) | 52 | 3,244 | 1,400 | **~1,844 px** |
| `"Full 3-part cost…"` (x-card-04) | 26 | 2,427 | 1,600 | **827 px** |

**Required fix:** Add a DPI-aware font scaler to `render_distilled.py`:
```python
def fs(pt): return pt * 72 / DPI   # at DPI=320, multiplier ≈ 0.225
```
Replace every `fontsize=N` with `fontsize=fs(N)`. Resolves ~80% of critical findings.

### Root Cause 2 — Design token hex values do not match canonical system

The renderer's local `TOKENS` dict has wrong hex values vs. the canonical design token system:

| Key | Renderer value | Canonical value | Impact |
|-----|---------------|-----------------|--------|
| `ACCENT` | `#f97316` (orange, "sunset" theme) | `#1f6feb` | Wrong primary color |
| `WARN` | `#eab308` (amber, "sunset"/"forest") | `#dc2626` (red) | Semantic inversion — amber on "bad" items |
| `SUCCESS` | `#eab308` (amber, "sunset") | `#16a34a` (green) | Wrong success color |
| `ACCENT_2` | `#6366f1` (indigo, "midnight") | `#0d9488` (teal) | Wrong secondary color |

**Required fix:** Remove theme-rotation system. Use canonical hex values from `.github/copilot-instructions.md` directly. Add a note: `# Theme rotation removed — canonical design tokens enforced`

### Root Cause 3 — Unicode characters in rendered strings (Critical — violates platform spec)

Em dash `—` (U+2014) appears in rendered strings at: slide-01 tagline, slide-05 footer, slide-06 body, slide-08 body, slide-10 content. Matplotlib renders these as mojibake or empty boxes on platforms without full Unicode font support.

**Required fix:** Replace all `—` with ASCII ` - ` in all string literals in `render_distilled.py`.

---

## Dimension & DPI Verification — All 20 PASS ✅

| Asset | Expected | Actual | DPI |
|-------|----------|--------|-----|
| slide-01-hook.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-02-promise.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-03-problem.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-04-framework.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-05-step1.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-06-step2.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-07-step3.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-08-pattern-interrupt.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-09-recap.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| slide-10-cta.png | 1080×1080 | 1080×1080 ✅ | 319.99 ✅ |
| x-card-01.png | 1600×900 | 1600×900 ✅ | 319.99 ✅ |
| x-card-02.png | 1600×900 | 1600×900 ✅ | 319.99 ✅ |
| x-card-03.png | 1600×900 | 1600×900 ✅ | 319.99 ✅ |
| x-card-04.png | 1600×900 | 1600×900 ✅ | 319.99 ✅ |
| medium-hero.png | 1400×800 | 1400×800 ✅ | 319.99 ✅ |
| medium-inline-01.png | 1200×800 | 1200×800 ✅ | 319.99 ✅ |
| medium-inline-02.png | 1200×800 | 1200×800 ✅ | 319.99 ✅ |
| substack-hero.png | 1200×630 | 1200×630 ✅ | 319.99 ✅ |
| linkedin-article-exhibit-01.png | 1200×627 | 1200×627 ✅ | 319.99 ✅ |
| linkedin-article-exhibit-02.png | 1200×627 | 1200×627 ✅ | 319.99 ✅ |

`bbox_inches='tight'` — **ABSENT** from renderer ✅

---

## Summary Table

| Asset | Grade | Primary Blocker |
|-------|-------|-----------------|
| slide-01-hook.png | ❌ FAIL | "120x" 168px overflow; em dash |
| slide-02-promise.png | ❌ FAIL | All bullet items clip right |
| slide-03-problem.png | ❌ FAIL | Bar labels collide; WARN token semantic inversion |
| slide-04-framework.png | ❌ FAIL | Table columns illegible; all text clips |
| slide-05-step1.png | ❌ FAIL | 4 clip events; em dash in footer |
| slide-06-step2.png | ❌ FAIL | 3 clip events; em dash in body |
| slide-07-step3.png | ❌ FAIL | All routing rules clip right |
| slide-08-pattern-interrupt.png | ❌ FAIL | 160pt quote glyph clips brand bar; 5 clip events |
| slide-09-recap.png | ❌ FAIL | All checklist items clip; WARN amber semantic issue |
| slide-10-cta.png | ❌ FAIL | CTA "Save this post ->" clipped; URL overflows |
| x-card-01.png | ❌ FAIL | Hero stat clips; subtitle clips |
| x-card-02.png | ❌ FAIL | All text elements clip |
| x-card-03.png | ❌ FAIL | All text elements clip |
| x-card-04.png | ❌ FAIL | All text elements clip |
| medium-hero.png | ❌ FAIL | "120x Problem" 1,844px overflow |
| medium-inline-01.png | ❌ FAIL | Header clips; label starts at x=−137 |
| medium-inline-02.png | ❌ FAIL | Multiple clips |
| substack-hero.png | ❌ FAIL | Hero text clips; "$" stat clipped |
| linkedin-article-exhibit-01.png | ❌ FAIL | Zone headers collide |
| linkedin-article-exhibit-02.png | ❌ FAIL | Bar labels collide; duplicate label |

**Severity count:** Critical: 52 | Major: 14 | Minor: 8

---

## Fix Priority

| Priority | Action | Assets fixed |
|----------|--------|-------------|
| **P0-A** | Add `def fs(pt): return pt * 72 / DPI`; replace all `fontsize=N` with `fontsize=fs(N)` in `render_distilled.py` | All 20 (~80% of criticals) |
| **P0-B** | Replace all `—` (U+2014) with ASCII ` - ` in all string literals | slides 01, 05, 06, 08, 10 |
| **P1** | Remove theme-rotation; hardcode canonical token hex values | All 20 (token issues) |
| **P2** | Post-scaling: audit residual overlaps in slide-03, slide-04, slide-08, x-card-04 | 4 assets |
| **P3** | Fix decorative 160pt quote glyph (slide-08); fix label layout edge cases | 3 assets |

Re-render and re-review required after P0+P1.
