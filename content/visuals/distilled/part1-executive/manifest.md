# Visual Pack Manifest — Part 1 Executive
**Mode:** Executive (C-suite / EM / VP / Director audience)
**Source:** `content/ai-code-assistant-cost-part-1.md`
**Generated:** 2026-05-13
**Total assets:** 11 PNGs at 320 DPI

> **Executive style rules enforced:**
> - Navy `#051C2C` header bar on every exhibit
> - Conclusion stated as title (not a question)
> - No CTA on exhibit visuals
> - Max 3 colors per exhibit
> - Source attribution on every asset

---

## Core Exhibits (1200×627 px) — LinkedIn Article / Blog / Pitch Deck

| # | File | Dimensions | Conclusion-as-Title | Accent | Psychology Frame |
|---|------|-----------|---------------------|--------|-----------------|
| 1 | `exhibit-01-context.png` | 1200×627 | "GitHub Copilot Billing Change — June 1, 2026" | Sky #0ea5e9 | Context framing |
| 2 | `exhibit-02-evidence.png` | 1200×627 | "Routing Strategy: Documented Cost Reduction" | Ocean #0284c7 | Social proof / data |
| 3 | `exhibit-03-framework.png` | 1200×627 | "3-Tier Model Routing Framework" | Amber #f59e0b | Cognitive ease |
| 4 | `exhibit-04-roi.png` | 1200×627 | "ROI Summary: Model Routing Implementation" | Emerald #10b981 | Loss aversion / ROI |

---

## X / Twitter Exhibits (1600×900 px)

| # | File | Dimensions | Content Summary | Usage |
|---|------|-----------|-----------------|-------|
| 1 | `x-exhibit-01.png` | 1600×900 | Horizontal bar chart: all model multipliers from 0x to 30x | X/Twitter standalone post |
| 2 | `x-exhibit-02.png` | 1600×900 | Before/after cost breakdown by task category + ROI callout | X/Twitter ROI post |

---

## Medium / Blog Images

| # | File | Dimensions | Content Summary | Usage |
|---|------|-----------|-----------------|-------|
| 1 | `medium-hero.png` | 1400×800 | Dark navy hero — "The 120x Problem" + 3 executive data callouts | Blog/Medium hero |
| 2 | `medium-inline-01.png` | 1200×800 | Model multiplier reference table (executive format) | Inline after intro |

---

## Substack

| # | File | Dimensions | Content Summary | Usage |
|---|------|-----------|-----------------|-------|
| 1 | `substack-hero.png` | 1200×630 | Dark navy — "The 120x AI Cost Spread" + key stat line | Substack note hero |

---

## LinkedIn Article Exhibits (1200×627 px)

| # | File | Dimensions | Content Summary | Usage |
|---|------|-----------|-----------------|-------|
| 1 | `linkedin-article-exhibit-01.png` | 1200×627 | Flat-rate → transition → consumption billing timeline | Article section 1 |
| 2 | `linkedin-article-exhibit-02.png` | 1200×627 | Cost waterfall: $3,000 → $1,200 → $970/day with savings annotation | Article section 2 |

---

## Usage Notes

### Exec Briefing / Pitch Deck
- Use `exhibit-01-context.png` → `exhibit-04-roi.png` in sequence as a 4-slide exec summary
- Each exhibit stands alone as a single-data-point visual for board decks or budget discussions

### LinkedIn Article (C-suite)
- Use `linkedin-article-exhibit-01.png` + `linkedin-article-exhibit-02.png` as article body visuals
- Executive article must carry >30% original content vs. the practitioner blog post
- No "follow me" CTA inside the image — keep that in article copy

### X / Twitter (Executive Lens)
- `x-exhibit-01.png` — post as standalone with the multiplier data point
- `x-exhibit-02.png` — post as the ROI evidence visual

### Medium
- `medium-hero.png` as cover image
- `medium-inline-01.png` after the "pricing structure" section

---

## 5-Zone Exhibit Anatomy (per slide-grammar.md)

Every exhibit follows the executive 5-zone layout:

| Zone | Location | Content |
|------|----------|---------|
| Navy header | Top 72px | Conclusion-as-title + brand tag |
| Accent rule | Below header | 3px accent color stripe |
| Headline | Top-third body | Supporting context sentence |
| Data zone | Centre body | Chart / table / callouts |
| Footer strip | Bottom 4px | Accent rule (no CTA) |

Source attribution placed at `(W*0.04, 24px)` — bottom-left, italic, muted.

---

## Design Token Summary

| Token | Value | Role |
|-------|-------|------|
| NAVY | #051C2C | Header bar background |
| TEXT_INV | #f8fafc | Header text (on navy) |
| FONT | DejaVu Sans | All text — no Unicode glyphs |
| DPI | 320 | All renders |
| Accent rotation | Sky/Ocean/Amber/Emerald/Indigo | Cycles by exhibit index i%5 |
| Body BG | #ffffff | All exhibits |

## Source Attribution
All data points traced to:
- GitHub Copilot billing documentation (2025)
- Towards Data Science, May 2026 (case study: $3K→$970/day, $740K/yr)
- LMSYS RouteLLM paper (2024): 95% quality at 75% lower cost, routing only 14% to GPT-4
- CascadeFlow benchmark (2024): 69% savings, 96% quality retention
- Apple ML Research (2025): reasoning models burn extra tokens on simple tasks, zero quality gain
