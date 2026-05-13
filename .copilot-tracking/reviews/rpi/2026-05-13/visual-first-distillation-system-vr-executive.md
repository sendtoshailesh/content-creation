<!-- markdownlint-disable-file -->
# Visual Review: Executive Pack (Part 1)
**Date:** 2026-05-13
**Assets reviewed:** 11 PNGs from `content/visuals/distilled/part1-executive/`
**  All 11 assets blocked; same 2 systemic root causes as Practitioner packFAIL Verdict:** 

---

## Systemic Root Causes

### Root Cause  Font/DPI coordinate-system mismatch (affects all 11 assets)1 

Same issue as Practitioner pack. Pixel-space coordinate axis + point-unit fontsize at DPI=320 causes all large text to overflow canvas boundaries.

Example calculations for Executive pack:
```
fontsize=22 bold header:
   97.8 pxheight 
  "A 120x Cost Spread Arrives in Your Budget" ( 2,583 pxchars) 
 2.15 overflow

fontsize=13 bold header tag:
  "GitHub Copilot Billing Change - June  1,596 px2026" 
 1.46 overflow
```

**Required fix:** Same `def fs(pt): return pt * 72 / DPI` helper. Apply to all `fontsize=` calls.

### Root Cause  Design token palette mismatch2 

The executive renderer's local `TOKENS` dict has wrong hex values:

| Local key | Local value | System token | Issue |
|-----------|-------------|--------------|-------|
| `ACCENT` | `#0ea5e9` | `#1f6feb` | Wrong blue |
| `ACCENT_2` | `#10b981` | `#0d9488` | Wrong teal |
| `ACCENT_3` | `#f59e0b` (amber) | `#7c3aed` (purple) | Completely wrong |
| `WARN` | `#f59e0b` (amber) | `#dc2626` (red) | Semantic inversion |
| `DANGER` | `#ef4444` | *(not in system)* | Rogue token |
| `LIGHT_BG` | `#f1f5f9` | `#f8fafc` | Wrong |
|  |  | *(Executive extension)* |  Permitted |

**Required fix:** Remove local `TOKENS` dict. Import from canonical 15-token system. Keep `NAVY` as Executive-mode extension.

### Root Cause  LaTeX dollar-sign parsing3 

`x-exhibit-02.png` has `$` signs in rendered strings. matplotlib parses `$...$` as LaTeX math mode. `"$3,000/day"` renders as `"3,000/day"` (dollar sign dropped, comma and slash may render incorrectly).

**Required fix:** Add `matplotlib.rcParams['text.usetex'] = False` at top of script. Escape dollar signs: `\$3,000/day`.

---

## Dimension & DPI  All 11 PASS Verification 

| Asset | Expected | Actual | DPI |
|-------|----------|--------|-----|
| exhibit-01-context.png | 1200627 | 1200627 | 319.99 |  
| exhibit-02-evidence.png | 1200627 | 1200627 | 319.99 |  
| exhibit-03-framework.png | 1200627 | 1200627 | 319.99 |  
| exhibit-04-roi.png | 1200627 | 1200627 | 319.99 |  
| x-exhibit-01.png | 1600900 | 1600900 | 319.99 |  
| x-exhibit-02.png | 1600900 | 1600900 | 319.99 |  
| medium-hero.png | 1400800 | 1400800 | 319.99 |  
| medium-inline-01.png | 1200800 | 1200800 | 319.99 |  
| substack-hero.png | 1200630 | 1200630 | 319.99 |  
| linkedin-article-exhibit-01.png | 1200627 | 1200627 | 319.99 |  
| linkedin-article-exhibit-02.png | 1200627 | 1200627 | 319.99 |  

 

---

## Summary Table

| Asset | Grade | Primary Blocker |
|-------|-------|-----------------|
| exhibit-01-context. FAIL | Header clips; tier box labels collide; wrong WARN token |png | 
| exhibit-02-evidence. FAIL | "$3,000"/"$970" collide; "$740,000" out of bounds |png | 
| exhibit-03-framework. FAIL | Header clips; sub-headline clips; all tier headers collide |png | 
| exhibit-04-roi. FAIL | KPI numbers collide with roadmap text; right column clipped |png | 
| x-exhibit-01. FAIL | Header clips; model names clip left edge |png | 
| x-exhibit-02. FAIL | LaTeX dollar-sign parsing; "$970/day" clipped; 5 overlaps |png | 
| medium-hero. FAIL | "The 120x Problem" 1,844px overflow; 4 clip events |png | 
| medium-inline-01. FAIL | Header clips; sub-headline clips; wrong token colors |png | 
| substack-hero. FAIL | Hero text clips; stat line clips both sides |png | 
| linkedin-article-exhibit-01. FAIL | Zone headers collide; right zone clips canvas edge |png | 
| linkedin-article-exhibit-02. FAIL | Bar labels collide; duplicate label; source/category collision |png | 

**Severity count:** Critical: 46 | Important: 18 | Minor: 12

---

## Fix Priority

| Priority | Action | Assets fixed |
|----------|--------|-------------|
| **P0-A** | Add `def fs(pt): return pt * 72 / DPI`; apply to all fontsize calls | All 11 (~85% of criticals) |
| **P0-B** | Add `matplotlib.rcParams['text.usetex'] = False`; escape `$` as `\$` | x-exhibit-02 LaTeX bug |
| **P1** | Remove local TOKENS dict; use canonical 15-token hex values; keep NAVY | All 11 (token issues) |
| **P2** | Post-scaling: audit residual overlaps in exhibit-02, exhibit-04, x-exhibit-02 | 3 assets |
| **P3** | Right-margin clearance; bottom dead-zones; legend positions | All 11 (minor) |

Re-render and re-review required after P0+P1.
