# Slide Grammar Reference

Defines the reusable slide-type taxonomy for Practitioner (carousel) and Executive (exhibit) persona modes. Load this file in Step 3 of the Visual Pack Generator procedure.

---

## Practitioner Mode — 10-Slide Carousel Grammar

Each slide maps to a fixed position in the carousel narrative arc. Fill each position with content extracted from the source blog, applying the listed psychology frameworks and visual treatment.

| Position | Slide Type | Content | Psychology Framework | Visual Treatment |
|----------|-----------|---------|---------------------|-----------------|
| 1 | Hook | Surprising stat or bold claim drawn from the blog's strongest data point | Curiosity Gap + Von Restorff + Peak-End (peak) | Giant number (48–72 pt), dark background (`#1e293b`), minimal text (≤15 words total) |
| 2 | Promise | What the reader will learn across the next 8 slides — 3-5 bullet promises | Processing Fluency | Bullet promise list (3–5 items), clean white BG (`#ffffff`), readable at glance |
| 3 | Problem | The core pain point quantified with data from the blog | SUCCESs (Unexpected + Concrete) + Dual-Coding | Before/after split layout OR problem data bar chart; one number dominates |
| 4 | Framework | The blog's core taxonomy, model, decision tree, or step sequence | AIDA (Interest) + Dual-Coding | Diagram, tiered model, or labeled flow; visual encodes the structure |
| 5 | Step 1 | First actionable step with supporting data point | Cialdini (Authority) + SUCCESs (Credible) | Large step number (e.g. `01`), icon placeholder, data point, ≤20-word description |
| 6 | Step 2 | Second actionable step with supporting data point | Cialdini (Social Proof) | Same visual treatment as Step 1 — numbered `02`, data, brief description |
| 7 | Step 3 | Third actionable step with supporting data point | SUCCESs (Credible) | Same visual treatment as Step 1 — numbered `03`, data, brief description |
| 8 | Pattern Interrupt | Emotional pull-quote from the blog — human impact, cost, or stakes | Von Restorff + SUCCESs (Emotional) | Dark BG (`#1e293b`), large quote text (36–48 pt), contrasting accent color; intentional visual break |
| 9 | Recap | Summary checklist of 3–5 key takeaways from the blog | Peak-End (approach end) | Checklist card with `[x]` markers (ASCII), 3–5 items, white BG, muted divider lines |
| 10 | CTA | Save/share prompt + canonical URL pointer | Peak-End (end) + Cialdini (Commitment + Reciprocity) | "Save this", "Link in comments" text, visual pointer/arrow; accent color highlight on CTA phrase |

### Practitioner Narrative Arc

```
Hook (curiosity) -> Promise (what's coming) -> Problem (pain data)
-> Framework (model) -> Steps 1-3 (how-to)
-> Pattern Interrupt (emotional peak) -> Recap (checklist)
-> CTA (save/share)
```

### Practitioner Layout Conventions

- **Slide aspect ratio**: 1080×1080 px (square) — fits LinkedIn, Instagram
- **Safe zone**: 80 px margin on all sides
- **Font hierarchy**: Title 48–72 pt / Body 20–28 pt / Caption/source 14–16 pt
- **Palette**: White BG + dark text (`#1e293b`) + ONE brand accent (`#1f6feb`) per slide
  - Exception: Slide 1 (Hook) and Slide 8 (Pattern Interrupt) use dark BG (`#1e293b`) + white text + accent
- **Slide number indicator**: Small `01 / 10` counter in bottom-right corner on all slides

---

## Executive Mode — 3-5 Exhibit Grammar

Executive exhibits follow McKinsey/BCG visual communication conventions: conclusion-as-title, single insight per exhibit, clean data-ink ratio. Required exhibits: 1, 2, 3. Optional: 4, 5.

| Position | Exhibit Type | Content | Design Convention | Visual Treatment |
|----------|-------------|---------|-------------------|-----------------|
| 1 (required) | Context Exhibit | Problem framed as quantified risk, cost, or gap | Conclusion-as-title (the finding, not the topic). Lead with the stakes. | Deviation bar chart or cost waterfall; navy (`#051C2C`) background header + accent palette |
| 2 (required) | Evidence Exhibit | Data supporting the recommended solution — benchmarks, comparisons, before/after | Single-insight-per-exhibit rule. Title = the conclusion the data proves. | Horizontal bar or line chart with direct data labels; source attribution line at bottom |
| 3 (required) | Framework Exhibit | The decision model, routing logic, or prioritization framework from the blog | FT Visual Vocabulary mapping — match chart type to data relationship | Flow diagram or part-to-whole chart; muted color series with one accent highlight |
| 4 (optional) | ROI Exhibit | Quantified business impact — cost saved, time reduced, throughput gained | Magnitude comparison convention — show the delta explicitly | Before/after magnitude bars with labeled delta (`+68%`); one accent color for the positive bar |
| 5 (optional) | Action Exhibit | Recommended next steps or priority matrix | Concrete Language framework — no vague verbs | Timeline, 2×2 priority matrix, or ordered action list; clean layout, action-oriented labels |

### Exhibit Anatomy — All 5 Zones (required on every exhibit)

Every exhibit must contain all five zones in this vertical layout order:

```
+--------------------------------------------------+
| [1] EXHIBIT LABEL  (small caps, top-left)        |
|     e.g. "Exhibit 1"                             |
+--------------------------------------------------+
| [2] CONCLUSION-AS-TITLE  (18–24 pt, bold)        |
|     Insight statement, not a description label   |
|     e.g. "AI coding costs vary 120x across       |
|            model tiers"                          |
+--------------------------------------------------+
| [3] SUBTITLE / CONTEXT  (12 pt, muted)           |
|     e.g. "Based on 2025 model pricing data"      |
+--------------------------------------------------+
| [4] VISUAL BODY                                  |
|     Chart, diagram, matrix, or flow              |
|     (takes ~70% of total exhibit height)         |
+--------------------------------------------------+
| [5] ATTRIBUTION LINE  (10–12 pt, muted, bottom)  |
|     e.g. "Source: Anthropic / Google, 2025"      |
+--------------------------------------------------+
```

### Executive Layout Conventions

- **Exhibit aspect ratio**: 1200×627 px (landscape) — fits LinkedIn Article, Medium inline
- **Safe zone**: 60 px margin on all sides
- **Font hierarchy**: Exhibit label 11 pt small caps / Conclusion title 18–24 pt bold / Body text 14–16 pt / Attribution 10–12 pt muted
- **Palette**: Navy header (`#051C2C`) + one accent + gray series (`#475569`, `#94a3b8`) — max 3 colors per exhibit
- **Data-ink ratio**: Remove all non-essential chart elements (gridlines unless needed for reading, 3D effects, shadows, decorative fills)
- **No CTA on exhibit visuals**: CTA lives in post body copy and captions only

---

## Hook Archetypes

Select the strongest archetype for the blog's content type. Hook text appears on Slide 1 (Practitioner) or in the Context Exhibit title (Executive).

### Practitioner Hook Archetypes

| # | Archetype | Template | Best For |
|---|-----------|---------|---------|
| 1 | Framework Hook | "The [N]-step framework for [outcome]" | 60% of use cases — when the blog has a clear step sequence or model |
| 2 | Number Hook | "[N] [surprising fact about topic]" | When there is a dramatic data point (e.g. "120x cost spread") |
| 3 | Contrarian Hook | "You've been [doing X] wrong. Here's why." | When the blog challenges a common practice |
| 4 | Result Hook | "I [achieved X outcome] in [timeframe]. Here's how." | When the blog includes a case study with before/after data |
| 5 | Warning Hook | "Stop [common practice] before it costs you [specific loss]" | When the problem has a quantified cost consequence |
| 6 | Question Hook | "What if [surprising alternative to conventional wisdom]?" | When the blog introduces a counterintuitive insight |
| 7 | Story Hook | "Last [timeframe], [company/team] faced [problem]. [Resolution]." | When the blog leads with a narrative case study |

**Selection rule**: Choose the archetype that matches the blog's strongest data point or narrative structure. When in doubt, use archetype 1 (Framework) or archetype 2 (Number).

### Executive Hook Archetypes

| # | Archetype | Template | Leads To |
|---|-----------|---------|---------|
| 1 | Risk Framing | "The [cost/risk] nobody expected" | Context Exhibit (deviation or cost chart) |
| 2 | ROI Framing | "[N]% [metric] reduction in [timeframe] — the compound effect" | ROI Exhibit (before/after magnitude bars) |
| 3 | Contrast Framing | "[Industry norm] vs [evidence-backed alternative]" | Evidence Exhibit (comparison bars) |

---

## Shared Content Rules (Both Modes)

- **Body text limit**: 30–50 words maximum per slide/exhibit body — split content across two slides if it exceeds this
- **Hero/title font sizes**: 48–72 pt for Practitioner hook titles; 18–24 pt conclusion titles for Executive exhibits
- **Standalone comprehension**: Every slide/exhibit must be fully understandable in isolation — never write "as shown above", "from the previous slide", "as discussed earlier"
- **Source attribution**: Every statistic and data point must include source name and year directly on the slide/exhibit — no unattributed numbers
- **Color limit**: Max 3 colors per slide/exhibit (white background counts as one)
- **Number accuracy**: All numbers must exactly match the source blog — do not round, approximate, or extrapolate
- **One big idea**: Each slide/exhibit carries exactly one insight or action — no multi-point compositions except the Recap/checklist slide (position 9)
