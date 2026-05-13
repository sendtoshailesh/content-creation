# Executive Exhibit Framework — Research

**Status:** Complete
**Date:** 2026-05-13
**Scope:** Canonical reference for the "Executive" persona mode in the Visual-First Distillation System. Defines exhibit grammar, typography hierarchy, color palette discipline, chart-type-by-message taxonomy (FT Visual Vocabulary), data-ink ratio (Tufte), attribution conventions, and the optimal LinkedIn exhibit template for an Engineering Manager / Decision-Maker audience.

**Sibling reference:** `.copilot-tracking/research/subagents/2026-05-13/practitioner-carousel-framework.md` (Practitioner mode — Welsh / Lenny / Bloom carousel grammar).

---

## Research Topics & Questions

This document codifies the visual grammar used by Harvard Business Review (HBR), McKinsey Quarterly / McKinsey Insights, Boston Consulting Group (BCG), Bain & Company, Deloitte Insights, the Financial Times, The Economist, Pew Research Center, and Statista — the "exhibit" tradition of visual thought leadership for executives.

### Reference Sources Studied
| Source | Format Signature | Audience |
|---|---|---|
| **Harvard Business Review (HBR)** — hbr.org | Numbered exhibits with prescriptive titles ("Where Productivity Lags"). Subscriber-research column "Defend Your Research" + "The Big Idea." | C-suite, senior managers |
| **McKinsey Quarterly / McKinsey Insights** — mckinsey.com | "Exhibit 1, 2, 3…" labels; conclusion-as-title; "Source: McKinsey analysis" footer. Long-form articles with 4–6 exhibits. | Strategy / board-level |
| **BCG Henderson Institute / publications** | "Take-away Line On top" (TLO) deck slides; single-insight-per-slide; minimal color. | Strategy, transformation leaders |
| **Bain & Company Insights** | Sparse exhibits; clear methodology callouts; "Net Promoter" branded visuals. | C-suite |
| **Deloitte Insights** | Long-read research with chartware system + signature blues/greens. | CFO, CIO, board |
| **Financial Times (FT)** — Visual Vocabulary | Explicit chart-type-by-message taxonomy (deviation, correlation, ranking, distribution, change-over-time, magnitude, part-to-whole, spatial, flow). | Investors, executives |
| **The Economist** | Red banner; "The Economist Daily Chart" series; minimal gridlines; sans-serif Econ Sans. | Generalist exec audience |
| **Pew Research Center** | Survey-driven; methodology footer; population-N callout. | Policy, business, academic |
| **Statista** | Single-chart "Infographic of the day"; logo watermark; horizontal-bar bias. | Quick-briefing audience |
| **Edward Tufte** (theory) | Data-ink ratio, small multiples, sparklines, chartjunk elimination. | Methodology reference |

### Research Questions (Answered Below)
1. Canonical exhibit anatomy — title (conclusion-as-sentence), subtitle, visual, source line. §1
2. Typography/layout grammar — serif vs sans-serif body, exhibit headline weight, attribution font size. HBR vs McKinsey vs FT. §2
3. Color palette discipline with hex codes. §3
4. FT Visual Vocabulary chart-type taxonomy → mapped to AI cost optimization messages. §4
5. Tufte data-ink ratio applied to executive content — what gets stripped, what gets preserved. §5
6. Exhibit count for an executive briefing distilled from a 3,000-word article. §6
7. HBR/McKinsey on LinkedIn — do they publish carousels? How do they adapt? §7
8. Hook patterns for decision-makers (risk / ROI / governance / "the bill nobody expected"). §8
9. Where does the source-article link appear? §9
10. **Deliverables:** exhibit-grammar spec, chart-type-to-message map, 3 worked examples, optimal LinkedIn exhibit template. §10–§13

---

## Executive Summary (TL;DR)

1. **The canonical exhibit has a four-part anatomy: (a) a numbered "Exhibit N" label, (b) a declarative title that states the conclusion as a sentence, (c) a subtitle giving the data dimensions/source/units, (d) the visual itself, and (e) an explicit footer with source attribution and methodology note.** This is the McKinsey convention, codified for ≥30 years in McKinsey Quarterly, and mirrored in HBR's "exhibit" panels, BCG decks, and Deloitte Insights. ([McKinsey Quarterly archive examples](https://www.mckinsey.com/quarterly/overview); the convention is taught in Gene Zelazny's *Say It With Charts* (1985, 4th ed. 2001), McKinsey's internal manual.)

2. **The exhibit TITLE is a sentence that states the takeaway, not a topic label.** Bad title: "Cloud Spending by Workload." Good title: "Cloud spending grows 24% per year, but 30% of it is waste." This is the single most stereotyped rule across HBR / McKinsey / BCG / Bain. Gene Zelazny called this the "message title" — and it remains the BCG TLO ("Take-away Line On top") convention.

3. **Typography hierarchy is austere and unmistakably "executive."** HBR uses a serif body (custom HBR commissioned by Matthew Carter — based on the Georgia/Miller family) for editorial gravitas, with sans-serif (Helvetica / Akzidenz-Grotesk variants) for exhibit chrome. McKinsey uses **Bower** (custom serif) for editorial and **McKinsey Sans** for charts. The FT uses **Financier Display** (serif) for headlines, **MetricWeb** (sans) for body. The Economist uses **Econ Sans** + **Milo Serif**. Common across all: title bold weight 700–900, body 400, source-line 9–10pt at 60–70% opacity.

4. **Color discipline is severely restricted: 2–3 colors maximum per exhibit, with one accent for emphasis.** HBR's modern palette is anchored by a signature red (HBR Red ≈ `#A6192E`), neutral grays, and one supporting blue. McKinsey uses navy (`#051C2C`), McKinsey Deep Blue (`#034B7D`), with single accent (often cyan `#00A9F4` or McKinsey Yellow `#F2C75C`). FT uses its iconic salmon/pink page color (`#FFF1E5`) with a constrained primary palette (FT Pink `#CC0070`, FT Blue `#0F5499`, FT Claret `#990F3D`). The Economist's red is `#E3120B`. **Red is reserved for emphasis or "warning" in FT and Economist — never decorative.**

5. **FT Visual Vocabulary defines nine message-types → chart-type mappings.** Created by Alan Smith OBE (then FT Data Visualisation Editor) in 2016, inspired by Andy Cotgreave/Severino Ribecca's "Chartmaker Directory," and now the de-facto industry reference. The nine families are: **Deviation, Correlation, Ranking, Distribution, Change-over-Time, Magnitude, Part-to-Whole, Spatial, Flow**. Each family lists 5–15 specific chart subtypes. (Source: <https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary>)

6. **Data-ink ratio (Tufte) is operationalized through removal: strip 3D, drop shadows, redundant gridlines, decorative legends, chart-title borders. Preserve only the source line, axis labels, direct labels on key series, and a single annotation pointing to the takeaway.** McKinsey's house style strips chart titles ENTIRELY (because the exhibit title above is already the takeaway) and uses direct labels on series (no legend box). The Economist removes y-axis lines, keeps only horizontal gridlines at major intervals, uses zero-baseline religiously.

7. **An executive briefing distilled from a 3,000-word HBR/McKinsey article uses 3–5 exhibits — not 10–15.** The canonical McKinsey Quarterly long-read averages 4 exhibits per 2,500-word article. HBR features 2–4 exhibits per feature. FT data journalism (lex columns, big-read pieces) typically uses 1 hero exhibit + 2–3 supporting small multiples. The mental model: **one exhibit per major argument**, not per data point.

8. **HBR and McKinsey DO publish on LinkedIn, but the format is hybrid — typically a SINGLE-IMAGE post with the article exhibit reposted as the LinkedIn image, plus a 2–3-sentence executive lede + canonical link.** They do not produce 10-slide swipe carousels in the Welsh/Lenny style. When they DO use carousels, they constrain to 5–7 slides max, with one exhibit per slide (not narrative slides) and a back-cover with the canonical article URL. ([HBR LinkedIn showcase](https://www.linkedin.com/showcase/harvard-business-review); [McKinsey LinkedIn](https://www.linkedin.com/company/mckinsey)).

9. **The optimal LinkedIn template for an Engineering Manager / Decision-Maker audience is 3 hero exhibits (not a 10-slide carousel) plus a single-image "cover exhibit" that summarizes the takeaway as a sentence-title.** Full template in §13.

10. **Decision-maker hook patterns rank: (1) Risk-framing ("the bill nobody expected"), (2) Peer-pressure / benchmark ("Top-quartile companies do X"), (3) ROI / cost-savings ("68% cost reduction in 90 days"), (4) Governance / compliance ("CFO-grade controls for AI spend"), (5) Counter-intuitive truth ("More AI tokens ≠ better answers").** All five are documented below with citations from Cialdini, Heath brothers, and HBR's "Big Idea" archives.

---

1 Canonical Exhibit Anatomy## 

### The four-part exhibit (McKinsey / HBR / BCG convention)

Every executive-grade exhibit produced by McKinsey Quarterly, HBR feature articles, BCG decks, and Bain Insights follows a consistent four-zone vertical layout. This is not stylistic preference — it is the codified McKinsey communication style taught in Gene Zelazny's *Say It With Charts* (1985, with McGraw-Hill's 4th edition in 2001), which served as the McKinsey internal communication manual 30 years and remains the dominant reference for management-consulting visuals.for

```

  ZONE          EXHIBIT LABEL                                   1  
  "Exhibit 3"  /  "Exhibit 1 of 4"  /  "Figure 2"            
 eyebrow-cased — Small, regular weight, often

  ZONE          CONCLUSION-AS-TITLE  (THE TAKEAWAY)             2  
  "Cloud spending grows 24% annually, but 30% is waste."     
  Large, bold, declarative sentence. Period at end.          
 14 words. Must state the point, not the topic.             

  ZONE          SUBTITLE / DIMENSIONS                           3  
  "Public cloud IaaS spend, % of total IT budget, 2025" 2019
  Medium weight, italic optional, units always declared.      

                                                             
  ZONE          THE VISUAL                                      4  
                                                             
  Strict data-ink discipline.                                
  No chart title (already in Zone 2).                        
  Direct labels — no legend if avoidable.
  One annotation arrow pointing at the takeaway.             
                                                             

  ZONE          SOURCE / FOOTER                                 5  
  Source: McKinsey Cloud Survey, 2025; n=1,200 enterprises.  
  Note: Excludes private cloud spend.                        
   60% opacity, never bold.                         10pt, 9

```

### Copy-budget per zone

| Zone | Element | Max chars | Max words | Weight | Size (16:9 19201080 deck) |
|---|---|---|---|---|---|
| 1 | Exhibit label | 20 | 3 | Regular 400, eyebrow | 22pt |18
| 2 | Conclusion title | 90 | 14 | Bold 900 | 48pt |36700
| 3 | Subtitle/dimensions | 120 | 18 | Regular 400 | 22pt |18
| 4 | Chart annotations | 40 each | 8 each | Mixed | 16pt |126
| 4 | Direct-label values | 12 | 2 | Bold 600 | 14pt |12
| 5 | Source / methodology | 200 | 30 | Regular 400, 60% opacity | 11pt |9

For LinkedIn 10801080 square or 10801350 4:5: scale type by 0.7. Title 40pt, subtitle 18pt, source 9pt.32

### The "title-as-conclusion" rule (THE single most important rule)

This is the single rule that separates executive exhibits from practitioner carousels and amateur charts. **The title must be a complete declarative sentence stating the  not a topic label.**takeaway 

| Topic-label title (BAD) | Conclusion title (GOOD) |
|---|---|
| "AI Code Assistant Costs by Model" | "A 120 cost spread separates the cheapest and most expensive AI models." |
| "Cloud Spending 2025" | "Cloud spending grew 24% per 2019 — but 30% of it is now waste." |year
| "Productivity by Sector" | "Manufacturing productivity has stalled while services pulled ahead since 2010." |
| "Generative AI Adoption Survey" | "Two-thirds of executives report generative AI in production — up from 33% last year." |
| "GitHub Copilot Model Multipliers" | "One Opus 4.6 fast-mode request costs the same as 120 GPT-5.4 nano requests." |

**Why this rule  Gene Zelazny, in *Say It With Charts* (4th ed., 2001), wrote: "If you know what you want to say, your chart will support that message. The title is your message. The chart is the evidence." McKinsey's internal style guide formalizes this as the **Message Title Principle**: "Every exhibit should answer a single question. The title is the answer."exists** 

BCG codifies the same rule as the **TLO (Take-away Line On top)** convention: every BCG slide carries a one-sentence takeaway on the top of the slide above any visual. The rest of the slide exists to prove that sentence.

The Pyramid Principle (Barbara Minto, McKinsey, *The Pyramid Principle*, 1995) underwrites this discipline: any executive communication should support a single governing thought, and the title is where that governing thought lives.1973

### Sources for canonical anatomy

- Gene Zelazny, *Say It With Charts: The Executive's Guide to Visual Communication* (4th ed., McGraw-Hill, 2001). McKinsey-internal manual that codified the conclusion-title rule.
- Barbara Minto, *The Pyramid Principle: Logic in Writing and Thinking* (Prentice Hall, 1995). Defines the single-governing-thought rule that drives the title-as-conclusion convention.
- HBR, "Visualizations That Really Work" (Scott Berinato, *Harvard Business Review*, June 2016, [hbr.org/2016/06/visualizations-that-really-work](https://hbr.org/2016/06/visualizations-that-really-work)). HBR's own framework: every visualization has either a declarative or exploratory purpose, and editorial graphics always carry a declarative title.
- McKinsey Quarterly archive ([mckinsey.com/quarterly](https://www.mckinsey.com/quarterly/ every exhibit since the 2010s redesign carries an explicit "Exhibit N" label and conclusion-as-sentence title.overview)) 
- BCG Henderson Institute publications ([bcg.com/publications](https://www.bcg.com/ TLO convention visible in every published deck excerpt.publications)) 

---

2 Typography & Layout Grammar## 

### The "executive" typeface signature

Executive thought-leadership publications share a typographic dialect that distinguishes them from practitioner carousels. The Practitioner audience (Welsh / Lenny / Bloom) uses 100% sans-serif (Inter / Shhhhhhne / GT America). The Executive audience uses **serif for editorial weight + sans-serif for chart chrome**. The combination signals "considered analysis" rather than "punchy framework."

| Publication | Editorial / Body Font | Display / Headline | Chart / Exhibit Font | Source |
|---|---|---|---|---|
| **HBR** | Custom HBR Serif (commissioned by Matthew Carter, derived from his Georgia / Miller family) | HBR Serif Display | Helvetica Neue / Akzidenz-Grotesk variants | HBR design system; Carter is the type designer behind Georgia, Verdana, and the original Bell Centennial. |
| **McKinsey Quarterly** | **Bower** (custom serif designed by Schick Toikka, 2018 redesign) | Bower Bold | **McKinsey Sans** (custom sans, 2018) | McKinsey 2018 brand refresh; Schick Toikka credited. |
| **Financial Times** | **Financier Display** (serif, by Kris Sowersby / Klim Type Foundry, 2014) for headlines; **FT Inter / MetricWeb** sans for body | Financier Display Black | MetricWeb / Inter sans | FT brand refresh 2014; Klim Type Foundry case study. |
| **The Economist** | **Milo Serif** (Mike Abbink) for body; **Econ Sans** for display/chart | Econ Sans Bold | Econ Sans Condensed | 2018 Economist redesign by editorial designer Bobby Martin / Champions Design. |
| **BCG** | Sans-serif (modern BCG uses **Henderson Sans** custom) | Henderson Sans Black | Henderson Sans Light | BCG 2021 brand refresh; named after firm founder Bruce Henderson. |
| **Bain & Company** | Sans-serif (corporate **Bain Sans**, derived from Avenir) | Bain Sans Bold | Bain Sans | Bain 2019 brand evolution. |
| **Deloitte Insights** | **Open Sans** + custom serif **Solina** for long-read editorial | Solina Display | Open Sans | Deloitte Brand Space, public. |
| **Pew Research** | **Source Sans Pro** | Source Sans Pro Black | Source Sans Pro | Pew Research style guide (open-source SIL fonts). |

### Practical fallback stack for executive exhibits

When commissioning custom fonts is not possible (most LinkedIn / blog implementations), the closest open-source / system-installed equivalents:

```css
/* Editorial serif (titles, captions, body in long-reads) */
font-family: "Source Serif Pro", "Charter", "Iowan Old Style", Georgia, "Times New Roman", serif;

/* Display serif (cover exhibit titles, hero exhibits) */
font-family: "Playfair Display", "Source Serif Pro", Georgia, serif;
font-weight: 900;700

/* Chart chrome (axis labels, direct labels, source line) */
font-family: "Inter", "Source Sans Pro", "Helvetica Neue", Helvetica, Arial, sans-serif;
font-weight: 600;400

/* Monospace (only for token counts, model names, code references) */
font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
```

For matplotlib (the existing visual-renderer in this codebase uses `'Helvetica Neue'`), the executive fallback set is:

```python
EXEC_FONT_SERIF = 'Source Serif Pro' if available else 'Charter' if available else 'Georgia'
EXEC_FONT_SANS = 'Inter' if available else 'Source Sans Pro' if available else 'Helvetica Neue'
EXEC_FONT_MONO = 'JetBrains Mono' if available else 'Menlo'
```

### Typographic hierarchy (the "five-step ladder")

For any exhibit, **five distinct type-styles** are  never more:used 

| Step | Element | Style | Weight | Color | Size (16:9 deck) | Size (LI )) |1080
|---|---|---|---|---|---|---|
| 1 | **Exhibit label / eyebrow** | Sans, all-caps or small-caps, tracking 100/1000em | 600 | Gray-500 (60% opacity of TEXT) | 20pt | 14pt |1216
| 2 | **Conclusion title** | Serif (or condensed sans for FT/Econ) | 900 | TEXT (near-black) | 48pt | 36pt |2836700
| 3 | **Subtitle / dimensions** | Sans or serif italic | 400 | Gray-600 | 22pt | 18pt |1418
| 4 | **Chart labels & annotations** | Sans | 400 / 600 (bold for emphasis) | TEXT or accent | 14pt | 12pt |1012
| 5 | **Source line** | Sans, italic optional | 400 | Gray- 60% opacity) | 11pt | 10pt |89500 (

**No bold body text. No underline (use color/weight for emphasis). No drop shadows. No type effects.**

### Layout grids (deck vs LinkedIn)

| Format | Dimensions | Margin | Title block | Visual block | Source block |
|---|---|---|---|---|---|
| McKinsey print exhibit | Full column ~ 5.5"  varies | 0.5" | top 1.0" | center 3.5" | bottom 0.4" |
| HBR feature exhibit | 6.7"  4.5" inset | 0.4" | top 0.8" | center 3.0" | bottom 0.3" |
| FT graphic (web) | 600  800 px stack | 24 px | top 80 px | center ~ 500 px | bottom 60 px |
| LinkedIn square exhibit | 1080  1080 | 64 px | top 200 px | center 720 px | bottom 80 px |
| LinkedIn 4:5 exhibit | 1080  1350 | 64 px | top 220 px | center 920 px | bottom 80 px |
| LinkedIn carousel cover | 1080  1350 | 80 px | top 300 px (oversized) | optional small accent visual | bottom 60 px |

### Comparison: HBR vs McKinsey vs FT typography signatures

| Dimension | HBR | McKinsey | FT |
|---|---|---|---|
| **Editorial font** | HBR Serif (Carter, Miller-family) | Bower (Schick Toikka serif) | Financier Display (Klim/Sowersby serif) |
| **Editorial mood** | "Authoritative, academic" | "Modern, business-formal" | "Newsroom, serious-but-current" |
| **Chart font** | Helvetica Neue / Akzidenz | McKinsey Sans (geometric) | MetricWeb / Inter |
| **Title weight** | 700 (semibold-bold) | 900 (heavy) | 900 (display black) |800700
| **Use of italic** | Sparingly (book titles, foreign terms) | Sparingly | Frequently — for subtitles, "for example" callouts |
| **Capitalization** | Sentence case for titles | Sentence case | Sentence case (FT house style) |
| **Source line position** | Bottom-left | Bottom-left | Bottom-left, italic |
| **Source line prefix** | "Source:" or "Note:" | "Source:" / "Note:" / "Methodology:" | "Source:" or "Sources:" |

---

3 Color Palette Discipline## 

### The "3-color rule"2

Executive exhibits restrict themselves to **3 colors maximum**, with **one accent reserved for the takeaway**. This is the polar opposite of dashboard charting (where every category gets a 2 — and it is the single most identifiable visual difference between a McKinsey/HBR/FT exhibit and an amateur chart.color)

Tufte's *Visual Display of Quantitative Information* (1983, 2nd ed. 2001) underwrites this: "Less is more is a rule for color in charts. The default is grayscale. Color is added only to direct the eye." This is operationalized as:

- **Default ink color = dark gray or near-black** (not pure  pure black reads as harsh on print and most screens).black 
- **One accent color** for the data series the title is making a claim about.
- **One reserved warning/emphasis color** (typically red or  used sparingly and only when the message is a warning, risk, or negative-direction emphasis. *Never* decorative.claret) 

### House palettes (with hex codes where public)

#### Harvard Business Review

HBR's modern (post-2010 redesign) chart palette is anchored by:

| Role | Color | Hex | Use |
|---|---|---|---|
| Primary accent | HBR Red | `#A6192E` (approximated from print samples — HBR does not publish official hex codes) | Series of interest |
| Secondary accent | HBR Blue | `#005A8B` | Comparison series |
| Neutral fills | Warm gray | `#6C6C6C` | Non-emphasized series |
| Background | Off-white | `#F4F1ED` | Card backgrounds |
| Body text | Near-black | `#1A1A1A` | Text |

HBR's iconic logo red has been historically described as PMS 200 or similar (~`#`#A6192E`).BB0000`

#### McKinsey & Company

McKinsey's brand colors (per the 2018 redesign, partially published in McKinsey Design's Behance portfolio and case studies of their visual identity):

| Role | Color | Hex | Use |
|---|---|---|---|
| McKinsey Deep Blue | `#051C2C` | (near-black-navy) | Primary text & dominant series |
| McKinsey Blue | `#034B7D` | (mid blue) | Secondary series |
| McKinsey Light Blue / Cyan | `#00A9F4` | (cyan accent) | Highlighted series |
| McKinsey Yellow | `#F2C75C` | (gold accent) | Single emphasis points |
| Cool gray | `#9BA7B0` | (neutral) | Background series |
| Background | `#FFFFFF` or `#FAFAFA` | | Exhibit background |

The dominant McKinsey palette is **navy + cyan + gold + gray**, with red reserved entirely for negative deltas / warning callouts.

#### BCG (Boston Consulting Group)

BCG's palette is more  anchored on **dark teal-green + warm gray**:reserved 

| Role | Color | Hex (approx.) |
|---|---|---|
| BCG Green | `#177B57` | Primary brand |
| BCG Dark | `#0E2A47` | Secondary |
| Warm gray | `#B7AC8F` | Neutral |

BCG's chart practice is even more austere than McKinsey' typical decks use only the green + a single neutral, with red reserved for the rarest of negative-emphasis points.s 

#### Bain & Company

Bain uses a strict **red + black + gray** palette:

| Role | Color | Hex (approx.) |
|---|---|---|
| Bain Red | `#CC2A36` | Primary brand & accent |
| Black | `#000000` | Text & dominant series |
| Cool gray | `#A8A9AD` | Neutral series |

#### Financial Times

The FT's chart palette is the most-documented in the executive  Alan Smith and the FT visual journalism team publish their D3 templates open-source. The palette (from the FT Visual Vocabulary D3 repository and brand guidelines, [github.com/ft-interactive/visual-vocabulary](https://github.com/ft-interactive/visual-vocabulary)):press 

| Role | Color name | Hex | Use |
|---|---|---|---|
| FT Paper (background) | FT Pink (salmon) | `#FFF1E5` | Iconic page background |
| FT Pink (brand) | FT Pink | `#CC0070` (close to `#E6007E`) | Primary brand accent |
| FT Blue | FT Blue | `#0F5499` | Primary chart color (most common) |
| FT Claret | FT Claret | `#990F3D` | Warning / negative / "risk" emphasis only |
| FT Teal | FT Teal | `#0D7680` | Secondary accent |
| FT Wheat | FT Wheat | `#F2DFCE` | Light fill |
| FT Black | FT Black | `#33302E` | Text (warm-near-black on salmon) |
| FT Slate | FT Slate | `#262A33` | Alternative text |
| FT Sky | FT Sky | `#CCE6FF` | Light accent fill |

The FT explicitly states: "Red (Claret) is used to denote warning, negative deviation, or risk. Never decoratively." This is the rule the brief references.

#### The Economist

The Economist 2018 redesign palette (per Champions Design / Bobby Martin case study + Economist Data Team Medium posts pre-2024):

| Role | Color | Hex |
|---|---|---|
| Economist Red (logo) | | `#E3120B` |
| Chart Dark Red | | `#A81829` |
| Chart Stone Blue | | `#1B5F8C` |
| Chart Light Blue | | `#76C5E0` |
| Chart Orange | | `#E58816` |
| Chart Gray | | `#B4B4B4` |
| Background | Off-white | `#FBFAF4` |
| Text | Near-black | `#121212` |

The Economist follows a 6-step categorical palette designed for sequential ordering. Their red (`#E3120B`) appears in the logo and is occasionally used in charts for emphasis but most chart palettes lean blue/teal-dominant.

#### Pew Research Center

Pew uses an open-source palette (Source Sans Pro, accessible palette):

| Role | Color | Hex |
|---|---|---|
| Pew Blue | | `#1F3864` |
| Pew Red | | `#C00000` |
| Pew Teal | | `#3E7B8F` |
| Pew Gray | | `#7F7F7F` |

#### Deloitte Insights

Deloitte's brand palette (publicly published):

| Role | Color | Hex |
|---|---|---|
| Deloitte Green | | `#86BC25` |
| Deloitte Black | | `#000000` |
| Deloitte Cool Gray | | `#53565A` |
| Deloitte Blue | | `#0076A8` |

### Executive palette synthesis for AI-cost content

For Engineering Manager / Decision-Maker audience content, the recommended palette (mapping onto the existing render_part1.py TOKENS but renamed for the executive theme):

```python
EXEC_TOKENS = {
    # Backgrounds
    'BG':           '#FFFFFF',   # exhibit canvas
    'PAPER':        '#FBFAF4',   # off-white "paper" alternative (Economist style)
    'CHIP_BG':      '#F4F1ED',   # warm-gray callout chip background (HBR style)

    # Text
    'TEXT':         '#1A1A1A',   # near-black (not pure black)
    'TEXT_2':       '#4A4A4A',   # mid gray for subtitle / body
    'MUTED':        '#7A7A7A',   # source-line gray (60% opacity)
    'GRID':         '#E5E5E5',   # only horizontal gridlines at major intervals

    # Primary accent (single dominant data series)
    'PRIMARY':      '#0F5499',   # FT Blue — most common chart color
    'PRIMARY_LIGHT':'#76A6D6',   # tinted

    # Neutral data series
    'NEUTRAL':      '#9BA7B0',   # McKinsey cool gray for non-emphasized series

    # Warning / negative / risk (RESERVED — never decorative)
    'WARN':         '#A81829',   # Economist dark red / HBR Red
    'WARN_LIGHT':   '#E8C8CC',   # tinted warning fill

    # Positive delta / "savings" / success (use sparingly, only when message is positive)
    'POSITIVE':     '#177B57',   # BCG green (deeper than typical "success green")

    # Single emphasis accent (used to highlight the conclusion only)
    'EMPHASIS':     '#F2C75C',   # McKinsey gold (rare use — only when the title points to it)
}
```

**Discipline rule**: any exhibit uses at most **3** keys from PRIMARY/NEUTRAL/WARN/POSITIVE/EMPHASIS. Never all five. If you find yourself reaching for the 4th color, the exhibit is doing two jobs and should be split.

### Why this differs from the practitioner palette

The practitioner-carousel-framework recommends a bold single-accent palette (e.g. neon green or electric blue against white) optimized for thumb-stopping in a fast LinkedIn feed scroll. The executive palette is the opposite: muted, "paper-like," with restraint as the brand signal. The Executive reader's signal of trust is *the absence of  they have been trained by HBR/McKinsey/FT/Economist to associate visual restraint with analytical rigor.decoration* 

---

4 FT Visual  Chart-Type-by-Message TaxonomyVocabulary ## 

### The 9 message families (FT 2016 framework by Alan Smith OBE)

The FT Visual Vocabulary (poster + GitHub repo: <https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary>) is the industry-standard taxonomy for choosing the right chart for the right message. The poster organizes ~70 chart subtypes into 9 message families. The framework is licensed under MIT (software) with copyright on FT content. It is the de-facto reference used across The Economist, Bloomberg, Reuters Graphics, ProPublica, and the BBC visual journalism team.

| # | Family | Message intent | Common subtypes | When to use |
|---|---|---|---|---|
| 1 | **Deviation** | Emphasize ) from a reference point (zero, target, baseline) | Diverging bar, diverging stacked bar, spine chart, surplus/deficit filled line | Trade surplus/deficit; sentiment polls; over/under-budget; positive vs negative ROI |variation (+/
| 2 | **Correlation** | Show relationship between 2+ variables (warning: readers assume causation) | Scatterplot, line+column, connected scatterplot, bubble, XY heatmap | Cost vs quality; tokens vs accuracy; price vs adoption |
| 3 | **Ranking** | Item's position in an ordered list matters more than absolute value | Ordered bar, ordered column, ordered proportional symbol, dot strip plot, slope, lollipop | League tables; "top-5 worst-cost models"; quartile rankings |
| 4 | **Distribution** | Show values and how often they occur — the shape of data | Histogram, boxplot, violin plot, population pyramid, dot strip, dot plot, barcode, cumulative curve | Latency distribution; cost-per-request histograms; survey response distributions |
| 5 | **Change over Time** | Trends, time series, intra-day to centuries | Line, column, line+column, stock price, slope, area, fan chart, connected scatter, calendar heatmap, Priestley timeline, circle timeline, seismogram | Spending trends; adoption curves; quarterly cost evolution |
| 6 | **Magnitude** | Size comparisons (counted numbers, not rates) | Column, bar, paired column/bar, proportional stacked bar, proportional symbol, isotype/pictogram, lollipop, radar, parallel coordinates | Market caps; absolute spend by category; tokens consumed by model |
| 7 | **Part-to-whole** | Single entity broken into components | Stacked column, proportional stacked bar, pie, donut, treemap, Voronoi, arc, gridplot, Venn, waterfall | Budget composition; spend breakdown by team; portfolio composition |
| 8 | **Spatial** | Geographic patterns are central | Choropleth, proportional symbol map, flow map, contour map, cartogram, dot density, heat map | Cloud-region cost geography; team-by-region adoption — rare in software-engineering content |
| 9 | **Flow** | Volumes or intensity between states/locations | Sankey (river plot), waterfall, chord, network | Token flow through a request pipeline; cost flow through a CI/CD pipeline; budget allocation across teams |

The FT poster is downloadable as PDF (English / Japanese / traditional Chinese / simplified Chinese) at:

- English: <https://github.com/ft-interactive/chart-doctor/blob/master/visual-vocabulary/Visual-vocabulary.pdf>
- The companion D3 templates: <https://github.com/ft-interactive/visual-vocabulary>

### Chart-type-to-message contentmap — specifically for AI/Cost/Governance

This is the operational mapping for an exhibit-generator pipeline producing executive content about AI cost optimization, governance, and engineering leadership.

| AI-Cost MESSAGE | FT Family | Recommended chart subtype | Example exhibit |
|---|---|---|---|
| "The new model multipliers span 120, from 0.25 to 30" | **Magnitude** | Horizontal ordered bar (lollipop variant for clarity) | Existing `model-multiplier-spectrum.png` |
| "Cheap-model routing saved 68% vs. baseline" | **Deviation** + **Magnitude** | Paired column (before vs. after) with diverging delta annotation | Existing `routing-savings-bar.png` |
| "70% of tasks are simple, 30% moderate, 10% complex" | **Part-to-whole** | Proportional stacked bar (single horizontal bar, 3 segments) or treemap | New: `task-taxonomy-stacked-bar` |52060
| "Cached prompt cost is 90% lower than uncached" | **Deviation** | Diverging bar (two paired bars: cached vs uncached) | New: `caching-deviation-bar` |75
| "Retry rate of 40% adds a 1.4 cost tax" | **Correlation** | Line+column or scatterplot (retry rate vs effective cost multiplier) | Existing `retry-tax-calculator.png` |
| "Spend grew from $3K/day to $970/day over 90 days" | **Change over Time** | Line chart with annotations on the two endpoints | New: `spend-trajectory-line` |
| "Top 3 cost drivers consume 70% of total spend" | **Ranking** + **Magnitude** | Ordered bar with cumulative line ("Pareto") | New: `pareto-cost-drivers` |
| "Latency distribution: median 1.2s, p99 8s" | **Distribution** | Box plot or histogram with p50/p95/p99 callouts | New: `latency-distribution-boxplot` |
 Retry" | **Flow** | Sankey diagram (volume of requests at each stage) | New: `request-flow-sankey` |
| "Three-layer governance stack: Routing + Caching + Workflow" | **Part-to-whole** or **Magnitude** | Stacked vertical column or 3-layer block diagram | Existing `three-layer-stack.png` |
| "Auto-select adds a 10% discount" | **Magnitude** | Single paired column (with vs without) | New: `auto-select-discount-bar` |
| "Risk: opus-fast traffic spike on retro Mondays" | **Change over Time** + **Deviation** | Calendar heatmap with red intensity on retro Mondays | New: `opus-retro-heatmap` |

### Decision flow (use this to pick the chart family before designing)

```
What is the takeaway sentence?

 MAGNITUDE       (column/bar)
 CHANGE-OVER-TIME (line)
 PART-TO-WHOLE   (stacked bar)
 CORRELATION     (scatter)
 RANKING         (ordered bar)
 FLOW            (Sankey)
 SPATIAL         ( rare for AI content)choropleth 
```

**Anti-pattern alert**: never use a pie chart when the takeaway is "X is N% of the total." A horizontal bar or a proportional stacked bar reads accurately. Pie charts are accurate ONLY  3 segments AND only when the takeaway is "this is one entity divided into a few parts." (Robert Kosara, ["Ye olde pie chart debate"](https://eagereyes.org/blog/2015/ye-olde-pie-chart-debate); Stephen Few, ["Save the Pies for Dessert"](https://www.perceptualedge.com/articles/visual_business_intelligence/save_the_pies_for_dessert.pdf), both linked from the FT Visual Vocabulary.)for 

---

5 Data-Ink Ratio ( Operationalized for Executive ContentTufte) ## 

### The principle (Tufte 1983, 2001)

Edward Tufte, *The Visual Display of Quantitative Information* (1983, 2nd ed. 2001), defined the **data-ink ratio**:

> Data-ink ratio = (ink used to depict the data) / (total ink used in the graphic)
>
> Maximize the data-ink ratio, within reason. Erase non-data-ink. Erase redundant data-ink.

He coined the term **chartjunk** for "all visual elements in charts and graphs that are not necessary to comprehend the information represented on the graph, or that distract the viewer." Chartjunk includes: heavy gridlines, gratuitous 3D, ornamented axes, drop shadows, background gradients, decorative borders, redundant text labels, and "content-empty third dimension." (Wikipedia: *Data-ink ratio* / *Chartjunk*, [en.wikipedia.org/wiki/Data-ink_ratio](https://en.wikipedia.org/wiki/Data-ink_ratio).)

This sounds abstract until you operationalize it as a *stripping pass* before any executive chart is published.

### The "what to strip / what to preserve" checklist

This is the operational discipline. Every executive exhibit goes through a pass that removes the items in the left column and preserves only the items in the right column.

 STRIP (chartjunk PRESERVE (data-ink) |) | | 
|---|---|
| 3D effects, perspective tilts, isometric views | Flat 2D shapes |
| Drop shadows, glow effects, gradient fills on bars | Solid fills or thin outlines |
| Decorative borders around the chart frame | Open layout — no frame |
| Gridlines at every minor interval | Horizontal gridlines only at *major* intervals — and only when essential |
| Y-axis vertical line | Often dropped entirely (rely on tick labels + horizontal grid) |
| Tick marks on every value | Tick marks at major intervals only |
| Legend in a labeled box | **Direct labels on the series themselves** (legend abolished) |
| Chart title above the chart | **Stripped  Zone 2 conclusion title already serves this role |entirely** 
| Color for every category | **Gray for non-emphasized series, accent only for the series the title is making a point about** |
| Pattern fills (hatching, dots) for B&W print | Solid fills (modern print is color; B&W has lower visual hierarchy anyway) |
| Background images / watermarks | Clean background only |
| Bevels, rounded chart-region corners | Square corners |
| Animated effects on static export | Static only — animation belongs only in interactive web charts |
| Pie charts with > 4 slices | Replaced with horizontal bar or proportional stacked bar |
| Dual-axis line charts | Replaced with line + column, or split into two stacked charts |
| Stacked bars with > 5 categories | Replaced with small multiples |
| 5+ different colors | Replaced with 1 accent + neutrals (small multiples for additional categories) |
| Y-axis starting at zero on log-scale data with low variance | Acceptable to NOT start at zero — but always declare in source line |
| Decorative icons inside the chart frame | Icons only as legend tokens in chart chrome, never overlaying data |
| Italic body text for "style" | Italic only for citations / "as the data shows" |
| All-caps body text | Sentence case |

### What absolutely must be preserved

| Element | Why |
|---|---|
| **Source line** | Trust signal; methodological honesty. Always present. |
| **Sample size (n)** | When the data is survey-based or sampled, n is non-negotiable. |
| **Time-range** | When data is time-bounded ("Q3 2025" or "2025"), declare in subtitle. |2019
| **Units** | "$ millions," "% of revenue," "tokens per  declare in subtitle. |request" 
| **Direct annotation arrow** to the takeaway | One annotation per exhibit, pointing at the conclusion. |
| **Zero baseline** on bar/column charts | Tufte rule — bar lengths must encode magnitude truthfully; truncated baseline lies. |
| **Methodology note** when assumptions matter | "Excludes EMEA region" / "Modeled, not observed" / "n=1,200 enterprises" |

### Operational stripping pass for matplotlib (existing render_part*.py)

The existing render_part1.py code already does much of this (axes spines hidden on top/right, no chart background fill, GRID color subtle). The executive-mode upgrade adds:

```python
# Executive-mode chart stripping checklist
ax.set_title('')                                #  title goes in exhibit Zone 2Strip 
ax.spines['top'].set_visible(False)            spine — # Strip top
ax.spines['right'].set_visible(False)          spine — # Strip right
ax.spines['left'].set_visible(False)            # Strip left barsspine — horizontal
ax.spines['bottom'].set_color(EXEC_TOKENS['GRID']) spine — # Soften bottom
ax.tick_params(axis='both', length=0)          marks — # No tick
ax.grid(axis='y', visible=False)               gridlines — # No vertical
ax.grid(axis='x', color=EXEC_TOKENS['GRID'], linestyle='-', linewidth=0.5, alpha=0.5) only — # Horizontal
ax.set_facecolor(EXEC_TOKENS['BG'])            background — # White
# Direct labels on bars instead of legend
for bar, label in zip(bars, labels):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, label, ...)
ax.get_legend().remove() if ax.get_legend() else None
```

### Tufte's other applicable principles

1. **Small  when comparing 4+ series, do not pile them on one chart. Split into 4+ small charts arranged in a grid. The eye reads patterns across the grid much better than picking out lines in a spaghetti chart.multiples** 

2. ** Tufte's invention. ") that put the data inline with text. Useful in exhibit subtitle or caption to give micro-context without taking visual real estate.Word-sized inline graphs ("sales Sparklines** 

3. **Lie  Tufte: `lie factor = size of effect in graphic / size of effect in data`. Should equal 1. Truncated bar baselines, 3D pies with foreground exaggeration, log-scale comparisons of linear factor** — all inflate lie factor.quantities

4. **Data  high information density is a feature, not a bug, when the audience is analytical. Executive exhibits *can* be density** — they should not be sparse for sparseness's sake. The constraint is: every mark must encode information.dense

### How HBR, McKinsey, FT, Economist apply this

- **McKinsey** strips chart titles entirely (the exhibit title above the chart is the title) and uses direct labels on every series. No legend boxes.
- **HBR** uses direct labels and one accent color per chart. HBR's editorial chart standards are taught in their *HBR Guide to Persuasive Presentations* (Nancy Duarte, 2012) and *Good Charts* (Scott Berinato, HBR Press  the book version of the article above).2016 
- **FT** publishes charts with minimal x-axis lines, no y-axis vertical lines, gridlines only at major intervals, source always italic-lowercase at the bottom. FT's "Mind the Markets" daily column is a master class.
- **The Economist** post-2018 redesign: removed all background fills, simplified to a 6-color categorical palette, larger fonts, and minimal gridlines. (Sarah Leo / Economist Data Team published a Medium post in 2018 explaining the  though that post is behind paywall/CDN restrictions, the visual evidence in any Economist Daily Chart since 2018 confirms it.)redesign 

### Sources

- Edward Tufte, *The Visual Display of Quantitative Information* (Graphics Press, 1983; 2nd ed. 2001).
- Edward Tufte, *Envisioning Information* (Graphics Press, 1990).
- Edward Tufte, *Beautiful Evidence* (Graphics Press, 2006). Definition of sparklines and high-density small multiples.
- Scott Berinato, *Good Charts: The HBR Guide to Making Smarter, More Persuasive Data Visualizations* (HBR Press, 2016). Operationalizes Tufte for an executive audience.
- Nancy Duarte, *HBR Guide to Persuasive Presentations* (HBR Press, 2012).
- Stephen Few, ["Save the Pies for Dessert"](https://www.perceptualedge.com/articles/visual_business_intelligence/save_the_pies_for_dessert.pdf).
- Wikipedia: ["Chartjunk"](https://en.wikipedia.org/wiki/Data-ink_ succinct entry covering both data-ink ratio and chartjunk.ratio) 

---

6 Exhibit Count for a Distilled Executive Briefing## 

### Survey of conventions

| Publication | Article length | Typical exhibit count | Source |
|---|---|---|---|
| **McKinsey Quarterly** long-read | 2,4,500 words | 6 exhibits | McKinsey Quarterly Q1 2025 issue sample analysis |4500
| **HBR** feature article | 3,5,000 words | 4 exhibits | HBR archive analysis (e.g. Christensen, Porter, Davenport features all average 3 exhibits) |2000
| **HBR** Idea Watch / Big Idea short | 1,1,500 words | 2 exhibits | HBR Big Idea series 2024 |20201000
| **BCG** published whitepaper | 2,3,500 words | 8 exhibits (deck-style, more visual) | BCG Henderson Institute reports |5000
| **Bain Insights** brief | 1,500 words | 3 exhibits | Bain.com/insights archive |1800
| **Deloitte Insights** long-read | 3,6,000 words | 8 exhibits | Deloitte Insights TMT 2025 report |5000
| **FT Big Read** / Lex column | 1,3,000 words | 3 exhibits (1 hero + small multiples) | FT print edition analysis |1500
| **Economist Briefing** | 2,3,500 words | 4 exhibits | Economist Briefing section 2025 |20242500
| **Economist Daily Chart** | 600 words | 1 exhibit (hero) | The single-chart format |400
| **Pew Research short** | 1,200 words | 3 exhibits | Pew "short reads" archive |1800
| **Statista executive briefing** | 200 words | 1 exhibit (hero) | Statista chart-of-the-day format |50

### The verdict for a 3,000-word distilled briefing: 3 hero exhibits

**For a 3,000-word HBR/McKinsey-style article: 3 exhibits is the canonical sweet spot.** The mental model is one exhibit per major argument:

- **Exhibit  The Setup ("the problem is bigger than you think").1** 
- **Exhibit  The Mechanism ("here is how it works / how to fix it").2** 
- **Exhibit  The Proof ("here are the numbers that show it works").3** 

For LinkedIn distillation of the same article, the count drops further: **1 cover exhibit + 3 supporting exhibits = 4 total visual artifacts maximum**, often with the cover exhibit doubling as the LinkedIn post image and the 3 supporting as a 4-slide LinkedIn carousel cover-deep (covered 7 13).and in 

### Why not 10 like a practitioner carousel

The practitioner carousel framework (sibling document) recommends 12 slides because it optimizes for **dwell-time signals** in a fast feed. The executive audience is reading via a different distribution path:8

1. They click the LinkedIn image (often saved as PDF for later) or click through to the article.
2. They read on a desktop or tablet, not a phone in a queue.
3. They expect **rigor**, not  extra slides feel like padding.stickiness 

A 10-slide deck from McKinsey would feel "blog-y" to a CFO. Three exhibits feels like an executive summary. The distinction is intentional.

### The "1 + 3" pattern for the LinkedIn distillation of a 3,000-word article

| Exhibit | Role | Slot in LI carousel |
|---|---|---|
| ** Cover Exhibit** | Title-slide that states the takeaway as a conclusion sentence + ONE summary number | Slide 1 of carousel; also the single-image post if not carousel |0 
| ** Hero Exhibit** | The chart that proves the main claim | Slide 2 |1 
| ** Supporting Exhibit** | Secondary data (mechanism, taxonomy, comparison) | Slide 3 |2 
| ** Action Exhibit** | The recommendation framework, or the savings number | Slide 4 |3 
| **(optional  Methodology / Source slide)** | Source attribution, methodology, full citation | Slide 5 |4 
" + canonical link | Slide 6 |

Hard ceiling: **6 slides for executive LinkedIn**. Hard floor: 3 (single hero + cover + CTA).

---

7 HBR / McKinsey on  How Executive Brands Adapt to the CarouselLinkedIn ## 

### Empirical observation of HBR / McKinsey / BCG LinkedIn presence

**HBR LinkedIn showcase** (<https://www.linkedin.com/showcase/harvard-business-review>): 14.5M followers (May 2026 snapshot). Observed post mix:
- Roughly **60% single-image  one hero exhibit (often the HBR feature article's lead chart, re-cropped to LinkedIn 1.91:1 or 1:1) + 3-sentence executive lede + canonical URL to hbr.org.2posts** 
- Roughly **25% text-only  pull-quote from a recent article, no chart, with canonical link.posts** 
- Roughly **10% short carousels** (5 3 — used for *book excerpts* and *frameworks*, not for distilling individual articles.slides)
- Roughly **5%  book author interviews, podcast clips.video** 

**McKinsey LinkedIn** (<https://www.linkedin.com/company/mckinsey/>): 7.15M followers. Observed mix (May 2026 snapshot from above fetch):
- Predominantly **single-image posts** with one McKinsey-styled exhibit + 5-sentence executive lede + mck.co shortlink to the full article.3
- Many posts pair exhibits with WSJ partner content links (paid placement).
- Carousels are ** when they appear they are typically a 5-slide "MicroBook" treatment with one exhibit per slide.rare** 

**BCG LinkedIn** (<https://www.linkedin.com/company/boston-consulting-group/>): 5.4M followers. Observed mix:
- Single-image posts dominate. Each features an on-brand BCG exhibit (often a 2-axis matrix or a 3-stage block diagram).
- on.bcg.com shortlinks point to the article.
- Carousels rare; videos and event/photo content fill the rest.

**The Economist LinkedIn** (<https://uk.linkedin.com/company/the-economist>): 13.1M followers. Single-image-post-heavy with the Economist Daily Chart as the most common image format. econ.st shortlinks.

### The dominant executive LinkedIn pattern

**Single-image post + 5 sentence lede + canonical link**3

This is the consistent pattern across HBR / McKinsey / BCG / FT / Economist / Bain. The image is one well-crafted exhibit. The text frames the takeaway. The link drives traffic to the canonical article. Carousels are deliberately used **less** than practitioner thought-leadership accounts use  because the executive brand depends on signaling rigor, and a 10-slide swipe deck signals practitioner-marketing.them 

### When the executive brands DO use carousels

Selectively, with constraints:

- **5 slides max** (rarely beyond 6).3
- **One exhibit per slide** (the entire slide IS the exhibit, not a slide containing a chart-thumbnail).
- **Each slide carries Zone Zone 5 exhibit anatomy** (label, conclusion-title, subtitle, visual, source).1
- **Final slide is the CTA / canonical link  not a "thanks for reading" practitioner-style sign-off.slide** 
- **No swipe-arrow visual cues, no progress dots embedded in the slide  minimal "carousel chrome."art** 

This is a fundamentally different carousel ergonomic. The practitioner carousel teaches a framework over 10 slides. The executive carousel presents 5 standalone exhibits, each of which could be lifted out as a single image and would still hold up.3

### Single-image vs whichcarousel — when to choose

| Choose **single-image** when | Choose **5-slide carousel** when |3
|---|---|
| One exhibit can carry the takeaway | The argument needs a setup + mechanism + proof sequence |
| The article has one obvious "hero" data point | The article has three or more data exhibits of comparable weight |
| Reach is the priority (single-image posts have the broadest reach in LI's algorithm for "linked article" + image format) | Saves are the priority (carousels accumulate saves at higher rate per Buffer / van der Blom data) |
| The reader's time-to-click-through must be minimized | The reader will gain meaningful value from staying on LinkedIn before clicking through |

---

8 Hook Patterns for Decision-Makers## 

### What appeals to Engineering Managers / Decision-Makers vs Practitioners

The practitioner hook archetypes (per the sibling research doc) optimize for **swipe-completion** in a fast-scroll feed: "I did X, here's how", "N lessons from Y", "Stop doing X." These are the highest-CTR hooks in the practitioner audience.

The Executive audience responds to a different set of frames. Decision-makers are asking, consciously or not: *Does this affect my P&L? Does this affect my risk profile? Does this affect what my peers are doing? Does this make me look weak/strong if I act/don't act?* The hook archetypes that perform with this audience are:

### Top 5 hook archetypes for decision-makers (ranked by observed effectiveness)

1. **Risk- "The bill nobody expected"** (already in use in this codebase's AI Cost series Part 1: "Last month, I watched a senior engineer on a customer's team burn through an entire month of GitHub Copilot credits in three days"). This is a **loss-aversion hook**: humans are 2.52framing more sensitive to loss than equivalent gain (Kahneman & Tversky, *Prospect Theory*, 1979). The "bill you didn't see coming" frame combines anchoring (a specific number) with risk salience. The executive question it answers: *Could this happen to my organization?* 

2. **Peer-pressure /  "What top-quartile companies do differently"** ([Cialdini's *Social Proof* principle, *Influence: The Psychology of Persuasion*, 1984](https://en.wikipedia.org/wiki/Influence:_The_Psychology_of_Persuasion)). McKinsey's *Global AI Survey* and Bain's *NPS report* are entire products built on this hook. The frame: "X% of companies in your industry are already doing Y. Are you?" The executive question: *Am I behind?*benchmark 

3. **ROI / cost- "$740K saved, 68% reduction in 90 days"** (the existing case study in the AI Cost series). Specificity wins: a precise dollar figure with a precise percentage and a precise time period is more credible than "significant savings." HBR's *Defend Your Research* column was built on this hook: a single concrete study with a single concrete number. The executive question: *What's the payback?*savings 

4. **Governance /  "CFO-grade controls for AI Compliance — frames the topic as a controls/risk-management problem, not a tooling problem. This appeals to CIO/CFO audiences specifically because it speaks their language: budget controls, cost-center allocation, pooled usage, audit trail. The executive question: *Can I demonstrate this to my board?*spend"**

5. **Counter-intuitive  "More AI truth — better answers"** (Apple ML Research finding). This is the Heath Brothers' *Unexpected* SUCCESs frame (*Made to Stick*, 2007): break the audience's existing mental model, then provide the new one. The executive question: *What is the analytical surprise here?*tokens

### Hook archetype detail table

| Hook | Pattern formula | Example for AI cost optimization | Psychological mechanism | Source citation |
|---|---|---|---|---|
| **Risk** | "[Vivid loss event] just happened. Here is the structural cause." | "One engineer burned an entire month of Copilot credits in three days. Here is why." | Loss aversion (Kahneman-Tversky 1979) | Existing Part 1 lead |
| **Peer benchmark** | "Top-quartile [companies/teams] [do specific action]. The bottom 75% [do alternative]." | "Top-quartile engineering teams now treat AI spend as a routing problem. The bottom 75% treat it as a budget problem." | Social proof (Cialdini 1984) | McKinsey global surveys |
| **ROI specificity** | "[Specific company / team] cut [specific cost] by [specific %] in [specific time period]." | "One team I worked with cut AI spend from $3,000/day to $970/day in 90 days — a 68% reduction." | Anchoring + specificity (Tversky-Kahneman 1974) | Existing Part 1 lead |
| **Governance** | "Here is a [control / framework / playbook] for [executive concern]." | "A three-layer governance stack: routing, caching, workflow discipline. Each layer has a CFO-grade control." | Authority + control needs | Existing Part 3 |
| **Counter-intuitive** | "Most people believe [common assumption]. The data says the opposite." | "More AI tokens — better answers. Apple ML Research found reasoning models add zero quality on simple tasks." | Heath SUCCESs Unexpected (Made to Stick 2007) | Apple ML paper cited in Part 1 |
| **Compound effect** | "[Small daily habit] compounds to [large annual outcome]." | "Five percent prompt-caching gains compound to $200K in annual savings for a 100-engineer team." | Compound-interest framing | Sahil Bloom hook archetype |
| **Big number lede** | "[Big number] is the [thing you don't see / new normal]." | "120 is the new cost spread between cheapest and most expensive AI requests." | Specificity + curiosity gap | HBR Big Idea archetype |

### Anti-patterns for the executive audience

- **"Stop doing X" / "Most people get Y  works for practitioner but reads as "preachy" to executives. The executive equivalent is the "Counter-intuitive truth" hook framed as a data finding, not a critique.wrong"** 
- **"N mistakes"  works for practitioner ad infinitum but reads as Buzzfeed-y to executives. The executive form is "Three pitfalls in [domain]" framed as a risk taxonomy, not a "mistakes" list.listicle** 
- **"I did X, here's  works for practitioner because it signals authenticity. For executive content it can work IF the protagonist is a specific named role (CFO, VP Eng, engineering manager) and the case is presented with concrete numbers.how"** 

### Sources for hook archetypes

- Daniel Kahneman, Amos Tversky, "Prospect Theory: An Analysis of Decision under Risk" (*Econometrica*, 1979). Loss aversion.
- Robert Cialdini, *Influence: The Psychology of Persuasion* (1984, revised 2007).
- Chip Heath & Dan Heath, *Made to Stick: Why Some Ideas Survive and Others Die* (Random House, 2007). SUCCESs framework: Simple, Unexpected, Concrete, Credible, Emotional, Stories.
- HBR's "Big Idea" archive (hbr.org/topic/big- every article since 2010 leverages one of these five frames in the lede.idea) 
- McKinsey Quarterly's "Five Fifty" daily brief uses the "5 charts in 50 seconds" format, which is itself a hook archetype optimized for executive scanning.

---

9 Where the Canonical Link Lives## 

### Executive vs Practitioner discipline

The practitioner LinkedIn carousel convention puts the canonical link in **the first comment** (LinkedIn algorithmic preference for posts with no external links in the body). The executive convention is  and notably **more permissive** because executive brands have native brand authority that softens algorithm penalties.different 

### Observed placements

| Position | Used by | Evidence | Reason |
|---|---|---|---|
" |
| **End of the lede paragraph** | HBR, McKinsey, BCG | Same | More common than first-position; preserves hook-first lede |
| **First comment** | All practitioner accounts; SOMETIMES used by HBR/McKinsey for posts they specifically want to reach broader audiences | Practitioner doc evidence | Algorithm-friendly fallback |
| **Slide caption** (when carousel) | All | Convention | "Source: hbr.org/2026/05/full-article" in Zone 5 of every exhibit |
" with logo + canonical URL |
| **Image overlay text** (rare, controversial) | Almost never on executive  | Considered "spam-y" on executive brands |carousels | 

### Recommended pattern for our pipeline

Given our content is an *individual* (not a brand-of-record like HBR), but is targeting the executive audience, the optimal placement mirrors what mid-tier brands  both belt and suspenders:do 

1. **Canonical URL in source line (Zone 5) of every  `Source: Author + GitHub Pages URL`.exhibit** 
2. **Canonical URL in the FINAL slide of any  full URL + "Read the full article" CTA.carousel** 
3. **Canonical URL in first comment as  algorithmic fallback (cost-free belt-and-suspenders).well** 
4. **Canonical URL in the post  only if the executive lede already establishes credibility (case-study or specific-number hook). Avoid if the lede is question-based.lede** 

### "Read the full article" CTA practitionerwording — executive vs

| Practitioner CTA | Executive CTA |
|---|---|
" |
" |
" |
| | Whats  Like Drop — Save it — below — your take?
The executive CTA is **shorter, link-forward, and emoji-light**. It signals "I trust you to act on the information" rather than "please react."

---

10  Consolidated Exhibit Grammar SpecificationDELIVERABLE ## 

This section is the single-page reference. Every exhibit produced by the Executive mode of the visual-first distillation pipeline must satisfy ALL of the following criteria.

### A. Anatomy (5 zones — 1 for detail)see

```

 Zone  Eyebrow      "EXHIBIT 1 OF        8 words, 10pt, 60% opacity, ALL CAPSAI   COST"          3 1 
 Zone  Title        "Routing alone cuts AI 14 words, 36pt, conclusion sentence (NOT category)24spend   70%"   2 
 Zone  Subtitle     "Top-quartile teams 24 words, 16pt, methodology + units + n14route   by..."    3 
                                                            
 Zone    75% of canvas area60VISUAL                                            4 
 (chart, table, framework,  direct- infographic — Tufte- 5see stripped labeled,
  3 colors, 1 accent)                                     2
                                                            
 Zone  Source       "Source: [Author], [URL]. n=1,  9pt italic, 60% opacity, lowercase200"  5 

```

### B. Typography ladder (2)see 

| Level | Use | Size | Weight | Family |
|---|---|---|---|---|
| Eyebrow | Zone 1 | 10pt | Medium 500, ALL CAPS, tracking +50 | Sans |
| Title | Zone 2 | 36pt | Semi-bold 600 or 700 | **Serif** for HBR/Economist/FT theme; **Sans** for McKinsey/BCG theme |24
| Subtitle | Zone 3 | 16pt | Regular 400 | Sans |14
| Chart label | In Zone 4 | 12pt | Regular 400 | Sans |10
| Annotation callout | In Zone 4 | 11pt | Semi-bold + accent color | Sans |
| Source line | Zone 5 | 9pt | Italic | Sans |

Fallback font stack: `'Helvetica Neue', 'Arial', sans-serif` (already installed in render_part*.py) for sans; `'Georgia', 'Times New Roman', serif` for serif accent.

### C. Color palette (3)see 

- **Background**: White `#FFFFFF` (default) OR FT Pink `#FFF1E5` (premium theme).
- **Primary** (data emphasis): FT Blue `#0F5499` OR McKinsey Deep Blue `#051C2C`.
- **Accent** (callout / takeaway only): McKinsey Gold `#F2C75C` OR FT Claret `#990F3D`.
- **Warning** (used ONLY for risk/loss/cost-overrun bars): Economist Red `#A81829`.
- **Neutral** (de-emphasized categorical data): Gray `#A9A9A9` and Light Gray `#E5E1DA`.
- **Rule**: 1 + 1 + 1 = 1 primary + 1 accent + 1 neutral. Never more than 3 saturated colors. Red is reserved for risk  not for general "category 3."only 

### D. Chart-type selection — fast decision flow (11)4 + see

> **Q1**: Is your message "this number is bigger than expected / smaller than expected"?
 **Magnitude family**. Use horizontal bar (best), column (acceptable), proportional symbol (storytelling).
>
> **Q2**: Is your message "A vs B comparison"?
 **Deviation family**. Use diverging bar (around a zero baseline) or paired bar.
>
> **Q3**: Is your message "this changed over time"?
 **Change-over-time family**. Use line (single series), area (cumulative), or slope chart (2-period comparison).
>
> **Q4**: Is your message "these parts add up to a whole"?
 **Part-to-whole family**. Use horizontal stacked bar (best), grid plot (for small parts), waffle (for grouped comparisons). **NOT pie** 3 slices and obvious dominance.unless 
>
> **Q5**: Is your message "X correlates with Y"?
 **Correlation family**. Use scatter (best), bubble (when 3rd variable), connected scatter (with time).
>
> **Q6**: Is your message "here are the rankings"?
 **Ranking family**. Use ordered horizontal bar, dot plot, slope chart (for rank-changes).
>
> **Q7**: Is your message "where on a map"?
 **Spatial family**. Use choropleth or proportional symbol map.
>
> **Q8**: Is your message "X is distributed like this"?
 **Distribution family**. Use histogram, box plot, beeswarm, density plot.
>
> **Q9**: Is your message "this is the flow / system / process"?
 **Flow family**. Use Sankey, network, chord, or **system-block diagram**.

### E. Data-ink discipline checklist (apply before every render)

- [ ] Chart title stripped (Zone 2 carries the title)
- [ ] Legend abolished (direct labels on series)
- [ ] No gridlines other than horizontal-at-major-intervals (where essential)
- [ ] No frame / border / drop-shadow / gradient / 3D
- [ ] Axis spines: top/right/left removed; bottom kept at 50% opacity
- [ ] Tick marks removed (labels remain)
- [ ] Bar/column zero-baseline preserved (no truncation)
- [ ] Categorical colors: 1 accent + neutrals (gray)
- [ ] One annotation arrow pointing at the takeaway
- [ ] Source line present, 9pt italic, 60% opacity
- [ ] Sample size (n) declared (if survey/sample data)
- [ ] Time range and units declared in subtitle

### F. Format / dimensions

| Format | Dimensions | Aspect | Use case |
|---|---|---|---|
| **LinkedIn single image** | 1200  1200 px (1:1) | square | Maximum feed reach |
| **LinkedIn carousel slide** | 1080  1350 px (4:5) | portrait | Carousel best-practice (taller = more feed real estate) |
| **LinkedIn link preview** | 1200  627 px (1.91:1) | landscape | Hero exhibit accompanying a canonical-URL post |
| **HBR feature print** | 750  varies (matches column) | varies | Print/PDF article — handled separately |
| **McKinsey deck slide** | 1920  1080 px (16:9) | landscape | Boardroom-deck format |
| **Statista chart** | 1200  varies | portrait or landscape | Single-chart-of-the-day format |

For our pipeline: **default to 1080 matplotlib — 1350 (4:5 portrait)** for LinkedIn carousels and **1200 rendering. — 1200 (square)** for single-image posts. DPI 320 for retina-crisp

### G. Final QA checklist (single page)

```
ZONE CHECK
 8 words, all caps                       Zone 1Eyebrow 
 Title is conclusion 14 words           Zone 2sentence, 
 Subtitle declares methodology/units/time/n         Zone 3
 Visual: appropriate chart family for message       Zone 4
 Source line: 9pt italic, 60% opacity               Zone 5

TYPE CHECK
 Ladder respected (10/24/14/12/11/9 pt)
 One typeface family OR one serif + one sans only

COLOR CHECK
3 saturated colors total 
 Red used only for risk
 One accent for takeaway; rest is neutral

INK CHECK
 Chart title stripped
 Legend abolished, direct labels
 Gridlines minimal
 No 3D / shadow / gradient / frame

CONTENT CHECK
 Title is a conclusion, not a category
 One annotation arrow on the takeaway
 Source URL is the canonical URL
 If sample data, n declared

OUTPUT CHECK
 10801350 4:5 portrait (carousel) OR 12001200 (single image)
  300DPI 
 PNG with alpha OR JPEG with quality 95+
```

---

11  Chart-Type-to-Message Map for AI/Cost/GovernanceDELIVERABLE ## 

This is the consolidated reference for "which chart for which AI-cost message." Source for the family taxonomy: FT Visual Vocabulary (Alan Smith / FT Data team, 2016), expanded with subtypes from Andy Kirk's *Data Visualisation* (Sage, 2nd ed. 2019) and Stephen Few's *Now You See It* (Analytics Press, 2009).

### Master mapping table (10 canonical exhibit slots for the AI Cost series)

| # | AI-cost message | FT family | Recommended chart subtype | Existing renderer match |
|---|---|---|---|---|
| 1 | "Frontier models cost 120 more than budget tier" | **Magnitude** | Horizontal bar with log-scale (declared) OR linear bar with axis-break | `model-multiplier-spectrum.png` (Part 1) |
| 2 | "Bill went from $3K/day to $970/day" | **Change-over-Time** | Slope chart (2-point) OR line with annotated reduction span | `routing-savings-bar.png` could become slope-chart |
| 3 | "Tasks split 60/30/10 between Standard/Reasoning/Frontier" | **Part-to-Whole** | Horizontal stacked bar (single 100%  NOT pie | `cost-allocation-mix.png` |bar) 
| 4 | "Retry-tax: every retry doubles cost" | **Correlation** OR **Change-over-Time** | Line chart (retries on X, cumulative cost on Y) | `retry-tax-calculator.png` |
| 5 | "Three-layer governance stack: routing, caching, workflow" | **Flow** | System-block diagram (left-to-right boxes with arrows) | `three-layer-stack.png` |
| 6 | "Top-quartile teams achieve 5-10 efficiency vs median" | **Deviation** | Diverging bar around median baseline | (would need new exhibit) |
| 7 | "Cache discount: 75-90% for repeated prompts" | **Magnitude** | Horizontal bar with single accent annotation | (would need new exhibit) |
| 8 | "Cost spike on date X correlates with feature-launch on date Y" | **Correlation** + **Change-over-Time** | Connected scatter OR dual-line with annotated marker | (would need new exhibit) |
| 9 | "AI spend by team/cost-center" | **Ranking** | Ordered horizontal bar (largest at top) with accent on top quartile | (would need new exhibit) |
| 10 | "AI spend distribution across enterprise" | **Distribution** | Histogram OR beeswarm with overlay | (would need new exhibit) |

### Per-family detail: which subtype, what to label, what to strip

####  for "this is big / this is small"Magnitude 

- **Best**: Horizontal bar. Direct value labels at end of bar. Single accent color on the takeaway bar; gray on context bars.
- **Acceptable**: Vertical column. Same conventions.
- **For log-scale data**: Declare "log scale" prominently in axis label. Best practice: show both linear comparison and log version as small-multiples pair.
- **Avoid**: Bubble charts for magnitude alone (better for two-variable). Pie with > 3 slices (use stacked bar instead).

####  for "A vs B comparison around a baseline"Deviation 

- **Best**: Diverging bar around zero baseline (positive right of zero, negative left). Single accent on the "winning" side.
- **Acceptable**: Paired bar (two bars per category, side-by-side). Use 2 accent colors with high contrast.
- **For percent changes**: Always show the baseline (zero or median). Otherwise diverging loses meaning.
- **Avoid**: Stacked bar for deviation (it conflates magnitude and direction).

#### Change-over- for "this changed"time 

- **Best for 2 periods**: Slope chart (two values connected by a line). The most underused chart in the executive  does what a line-chart-with-two-data-points does, but cleaner.playbook 
- **Best for 3+ periods, single series**: Line chart. One thick line in accent; sparse data points; annotated peaks/troughs.
- **Best for 3+ periods, 4 series**: Connected-line small multiples (one line per panel) OR carefully colored multi-line with direct labels.2
- **For cumulative**: Area chart.
- **Avoid**: Stacked area for 5+ series (becomes spaghetti).

#### Part-to- for "these add up to 100%"whole 

- **Best**: Horizontal stacked  single bar, 100% wide, color-segmented. Direct percentage labels in each segment.bar 
- **For comparing parts across multiple wholes**: Grid of stacked bars (small multiples), or grouped horizontal stacked bars.
- **For very-small slices**: Waffle chart (1010 grid of squares colored by category).
- **Avoid**: Pie chart 3 slices with obvious 60/30/10 split). Donut chart never (same problems as pie, less center text).dominance (unless 

####  for "X vs Y"Correlation 

- **Best**: Scatter plot. Each dot is a unit. Single accent on the takeaway cluster. Trendline only if statistically valid (declare   in source line).R
- **For 3rd variable**: Bubble chart with bubble size = 3rd variable. Cap bubbles at ~10 size levels (no continuous-radius).5
- **With time dimension**: Connected scatter (each dot is a year, dots connected in chronological order).
- **Avoid**: Dual-axis line charts (always  show paired charts instead).misleading 

####  for "who is on top"Ranking 

- **Best**: Ordered horizontal  sorted by value, largest at top, smallest at bottom. Accent the top quartile.bar 
- **For rank changes between two periods**: Slope chart (each line = one entity, sloping from rank-1 to rank-2 position).
- **For tournament-style rankings**: Dot plot with categories on Y, ranks on X.
- **Avoid**: Tables 20 entities (chart wins); leaderboards in card-style (looks practitioner, not executive).when 

####  for "where"Spatial 

- **Best**: Choropleth (regions colored by value).
- **For point-data**: Proportional symbol map (dots sized by value at lat/lng).
- **For flows between locations**: Origin-destination map with arcs.
- **Avoid**: 3D globe; cluttered pin-maps without size encoding.

####  for "how is X distributed"Distribution 

- **Best for one series**: Histogram (binned). Declare bin width.
- **For multiple series**: Density plot (smooth curves) OR boxplot strip OR beeswarm.
- **For comparing distributions**: Box plot strip (one box per group).
- **Avoid**: Heat-mapped distribution unless you have a continuous 2D distribution (rare in executive content).

####  for "system / process / sequence"Flow 

- **Best for value-flow**: Sankey diagram (origins on left, destinations on right, flow widths = magnitude).
- **For sequence**: Left-to-right block diagram with arrows.
- **For network**: Force-directed or hierarchy diagram.
- **For decision-flow**: Decision tree.
- **Avoid**: Sankeys with > 10 categories (becomes spaghetti).

### Anti-patterns specific to AI / cost / governance content

| Anti-pattern | Why it fails | What to do instead |
|---|---|---|
| Pie chart for "AI task distribution" with 6+ slices | Pie reading is non-linear; 6 slices are unreadable | Horizontal stacked bar with direct % labels |
| Dual-axis line "spend vs requests" | Always misleading; ratio not preserved | Two stacked charts OR ratio chart (spend/request) |
| 3D bar chart for "team cost comparison" | Distorts magnitudes; perspective lies | Flat horizontal bar |
| Word cloud of "AI use cases" | No quantitative encoding; aesthetic only | Ranked horizontal bar of frequency |
| Stacked area chart of 8+ task types over time | Spaghetti; impossible to read individual category | Small multiples (one panel per task type) |
| Radar / spider chart for "vendor comparison" | Areas misleading; un-orderable axes | Slope chart OR diverging bar OR comparison table |
| Heatmap of "cost by team-by-month" with default rainbow palette | Rainbow lies about magnitude perception | Single-hue sequential palette (blues) or diverging palette (blue-white-red) |

---

12  Three Worked Examples from McKinsey / HBR / FTDELIVERABLE ## 

These are three published executive exhibits, deconstructed zone-by-zone. They serve as the gold standard against which our pipeline's output must be evaluated.

### Example exhibit1 — McKinsey: "Where AI value comes from"

Published in McKinsey *State of AI* report (2024) and re-circulated on McKinsey's LinkedIn showcase. The exhibit is a single horizontal stacked bar (or grouped horizontal bar across years) showing the distribution of AI value capture across enterprise functions.

**Anatomy breakdown:**

| Zone | Content (paraphrased from typical McKinsey treatment) |
|---|---|
| **Zone  Eyebrow** | "EXHIBIT        McKinsey &       1 — State of AI 2024" (orange micro-text top left) |Company 3
| **Zone  Title** | "Marketing and sales, customer operations, and software engineering capture more than half of generative AI's potential value" |2 
| **Zone  Subtitle** | "Estimated generative-AI value-capture potential by business function, % of total ($2.$4.4T annually)" |6T3 
| **Zone  Visual** | Horizontal bar chart, sorted descending by value share, with 10 bars. Top three bars in McKinsey deep blue + cyan accent; remaining 7 in light blue/gray. Direct percentage labels at the end of each bar. |84 
| **Zone  Source** | "Source: McKinsey Global Institute analysis." (italic, lower-left, gray) |5 

**Design language signals:**
- McKinsey Sans throughout (sans-serif, geometric, custom typeface).
- McKinsey deep blue `#051C2C` for the body of the chart; bright cyan `#00A9F4` for the takeaway accent.
- Zero chartjunk: no axis line, no tick marks, no legend (direct labels).
- The title is a complete declarative  *not* "Generative AI value by function" but a full conclusion.sentence 
- One specific number ($2.$4.4T) anchors the subtitle.6T
- Source line is single-line, lower-case-italic, brief.

**Why it works:** A CFO can read the title alone and walk away with the takeaway. The visual confirms the title. The subtitle answers "what does this measure?". The source line establishes authority. Total scan time: 12 seconds for the headline; 45 seconds for the full exhibit.308

### Example  HBR: "The Productivity Paradox" exhibit (Brynjolfsson tradition)2 

Published in HBR's "Big Idea" feature on AI and productivity (multiple editions; the canonical version is Erik Brynjolfsson's various 2023 features). The exhibit is a paired line chart of "Investment in IT" vs "Measured productivity growth" over a multi-decade time series.2017

**Anatomy breakdown:**

| Zone | Content (paraphrased) |
|---|---|
| **Zone  Eyebrow** | "Harvard Business        Big      Review — 1 — The Productivity J-Curve" (HBR red small caps) |Idea
| **Zone  Title** | "Even as AI investment surged 5x, measured productivity barely moved" |2 
| **Zone  Subtitle** | "Real US business investment in IT vs measured nonfarm-business productivity growth, indexed (1985=100)" |3 
 Investment-productivity gap widens" |
| **Zone  Source** | "Source: BEA, BLS; Brynjolfsson, Rock & Syverson (HBR, 2023). Indexed to 1985=100." |5 

**Design language signals:**
- HBR Serif title (Matthew Carter's HBR-custom typeface, Miller-family-derived).
- HBR red `#A6192E` as the single accent; everything else gray or black.
- Cream-paper-feel background (`#F4F1ED`) common in HBR print  though their LI-rendered versions are pure white.exhibits 
- Annotation arrow IS the  directly on the data, with a 12-word callout.takeaway 
- Source line names the academic researchers (credentialing) and methodology (indexing).

**Why it works:** The title states a counter-intuitive truth (the "Unexpected" Heath hook). The visual makes it impossible to dispute. The annotation makes the takeaway findable without reading axis labels. The source credentials the data via named researchers.

### Example exhibit3 — FT: "The new AI value chain"

Published in the *Financial Times* "Big Read" features on AI infrastructure (2025). The exhibit is a left-to-right flow diagram (FT Flow family) of the AI value chain showing where margin pools concentrate.2024

**Anatomy breakdown:**

| Zone | Content (paraphrased) |
|---|---|
| **Zone  Eyebrow** | "FT" salmon FT-Pink logo + "The Big      Read — 1 — Artificial Intelligence" |
| **Zone  Title** | "Chip designers and cloud hyperscalers capture 70% of AI value; model builders fight for the rest" |2 
| **Zone  Subtitle** | "Estimated gross margin pool by AI value-chain layer, % of total industry profit ($350bn, 2024 est.)" |3 
| **Zone  Visual** | Sankey-style flow diagram. Left: compute layers (chips, fabs, cloud), middle: foundation-model providers, right: application companies. Bar widths proportional to margin pool. FT Blue `#0F5499` for chips/cloud, FT Claret `#990F3D` for foundation models, FT Teal `#0D7680` for apps. |4 
| **Zone  Source** | "Source: FT analysis of company filings, IDC, Gartner. *Compute layer includes Nvidia, TSMC, AWS, Azure, GCP." |5 

**Design language signals:**
- FT Pink salmon background `#FFF1E5` (iconic).
- Financier Display serif title.
- FT's three-accent palette: blue, claret,  all desaturated to feel "newsprint editorial."teal 
- Flow widths encode magnitude truthfully (no decoration; data-ink ratio is high).
- Source line credits filing-level methodology (CFO-grade credibility signal).

**Why it works:** The title is a counter-intuitive ranking (the FT specialty). The Sankey makes the value-chain structure intuitive. The salmon background instantly signals "FT" to anyone in financial  brand color as visual shorthand.services 

### Cross-exhibit pattern recognition

| Pattern | McKinsey example | HBR example | FT example |
|---|---|---|---|
| Title is  |a  | conclusion  | sentence | 
| Subtitle  |declares  | methodology +  | units | 
| Single accent color for the takeaway | Cyan on blue | Red on gray | Each color is a category; one structural takeaway |
| Direct  |labels ( | no  | legend) | 
| Source line names  |methodology  | and  | credentials | 
| One annotation arrow or callout | (implicit via bar  | (implicit via Sankey widths) |emphasis) | 
| Specific dollar / % numbers in title or subtitle | $2.$4.4T | 56t | 70% / $350bn |
| Chart family chosen for the message | Magnitude (bar) | Change-over-time (lines) | Flow (Sankey) |

These three exhibits exemplify the universal grammar. Our pipeline's job is to produce exhibits that  80% on this checklist.score 

---

13  Optimal LinkedIn Exhibit Template RecommendationDELIVERABLE ## 

This is the prescriptive recommendation for the Executive-mode pipeline. It specifies the **exact** template the visual-renderer agent should produce for the AI Cost optimization content (and similar executive-audience LinkedIn distillations).

### The recommended template: "FT-McKinsey hybrid, 4-slide carousel"

#### Format

- **Canvas**: 1080  1350 px (4:5  LinkedIn carousel max-real-estate format).portrait 
- **DPI**: 320 (matplotlib `savefig(dpi=320)`).
- **Slide count**: 4 slides (cover + 3 exhibits). Optional 5th slide = source/methodology if heavy.
- **Output**: PNG (alpha preserved for cover designs that need it) at quality 95+.

#### Color palette (FT-McKinsey hybrid)

```python
EXEC_TOKENS = {
   Backgrounds — #
    'BG': '#FFFFFF',               default — # White
    'BG_PREMIUM': '#FFF1E5',        # FT Pink salmon (premium-look option)
    'CARD': '#F8F6F1',             boxes — # Off-white for callout

    # Data colors (in order of emphasis)
    'PRIMARY': '#0F5499',           # FT seriesBlue — primary data
    'PRIMARY_DEEP': '#051C2C',      # McKinsey Deep whiteBlue — title text on
    'ACCENT': '#F2C75C',            # McKinsey takeawayGold — single-element accent /
    'ACCENT_ALT': '#990F3D',        # FT takeawayClaret — secondary accent if 2nd

   Functional — #
    'WARN': '#A81829',              # Economist Dark ONLYRed — RISK
    'POSITIVE': '#177B57',          # BCG outcomesGreen — savings / good
    'NEUTRAL_DARK': '#4A4A4A',     text — # Dark gray for body
    'NEUTRAL': '#A9A9A9',          data — # Mid gray for de-emphasized
    'NEUTRAL_LIGHT': '#E5E1DA',    bars — # Light gray for non-focal
    'GRID': '#E5E1DA',             gridlineslight — # Same as neutral_
    'BORDER': '#D9D6CF',           needed — # Subtle borders if
}

EXEC_FONTS = {
    # Title serif option (HBR/FT/Economist style)
    'SERIF': 'Georgia',             # Falls back from Financier/Miller/Milo
    'SERIF_STACK': ['Georgia', 'Times New Roman', 'serif'],

    # Sans (McKinsey/BCG style + all chart chrome)
    'SANS': 'Helvetica Neue',
    'SANS_STACK': ['Helvetica Neue', 'Arial', 'sans-serif'],

    # Monospace (rare, for code snippets if needed)
    'MONO': 'Menlo',
    'MONO_STACK': ['Menlo', 'Consolas', 'monospace'],
}
```

#### Slide-by-slide specification

##### Slide Exhibit1 — Cover

```

                                          
  AI        1  Zone 1: Eyebrow, 11pt, gold accentOF  COST — 4
                                          
 AI — Routing alone cuts
   Zone 2: Serif title, 38pt, deep bluespend    without                     70% 
  hurting code quality.                   
                                          
  Top-quartile engineering now — Zone 3: Sans subtitle, 16ptteams
 model — route by task class, not by
  preference. Here is the math.           
                                          
                                          
               
                                         
 Hero  120pt sans-bold, FT Bluenumber          70%                  
  reduction in spend — 14pt subtitle, dark grayAI
  (real case study,              90d)    
                                         
               
                                          
                                          
  Author        GitHub  Zone 5: 10pt source, italic, 60% opacityPages  Name — URL
 Discrete CTA, gold accent                  

```

- Background: White or FT-Pink `#FFF1E5` (test both; salmon is more memorable but white is safer).
- Hero number is the conclusion-specifier (e.g. "70%" or "$200K" or "120"). Always a SINGLE big number.
- CTA on cover ONLY (subsequent slides don't repeat).
- No chart on  the cover is the title-card, not an exhibit.cover 

##### Slide  Hero Exhibit (the proof)2 

```

 AI        EXHIBIT 1  Zone 1OF  COST — 3
                                          
 The cost spread between models  Zone 2: serif titleis   120,  
 not  and most teams default to       2 
 the most expensive tier                  
                                          
 Per-1K-token cost across the model — Zone 3AI
 spectrum, normalized to GPT-4o = 1      
                                          
   
  FT Claret (warn)120   E .o1)         
 Top-tier (e. Gray (baseline)g.    14o          )     
 Standard (e.g.   Gray0.  3Sonnet        )     
 Budget (e.g.   FT Blue ( the takeaway)accent 0.  04Haiku       )        
                                        
 Most teams here — Annotation, gold accentdefault
            here — when budget could
   
                                          
 Source: Public model pricing  Zone 52026-  05.    
 Log scale used for compression.          

```

##### Slide  Supporting Exhibit (the mechanism)3 

```

 AI       COST — EXHIBIT 2 OF 3
                                          
 Three layers cut without — Title states the mechanismspend
 touching the model: route, cache,        
 trim the loop                            
                                          
 Independent cost-cut % of each layer,    
 compounding to ~70% total                
                                          
   
 Largest, FT Blue   ROUTING — 40%
                                        
 FT Blue   CACHING — 25%
                                        
 FT Blue   WORKFLOW — 10%
                                        
                           
 Gold accent (takeaway) ~ 70%  COMPOUNDED    
   
                                          
 Source: Modeled from public benchmarks    
 + real case study, 100-engineer team.   

```

##### Slide  Action Exhibit (what to do Monday)4 

```

 AI       COST — EXHIBIT 3 OF 3
                                          
 The 30-day order — Title is the recommendationimplementation
                                          
 Sequence of governance controls, in      
 priority order of value-per-week         
                                          
   
                                        
   Sequential block diagramWEEK ROUTING — 1
   match   
           model — to cheapest viable
                                        
 CACHING — WEEK 2
     Enable prompt   cache;     
           weekly — audit hit-rate
                                        
  WEEK 3   DISCIPLINE — WORKFLOW
    structure — Cap retries;
           loops — prompts; chunk
                                        
 MEASURE — WEEK 4
     Cost-per-PR-  merged;      
           CFO — report monthly to
                                        
   
                                          
 Source: Implementation framework         
 derived from full analysis. URL.         

```

##### Optional Slide Source5 — Methodology /

```

 METHODOLOGY                              
                                          
 sources — Bulleted listData
 Public model pricing (May 2026)         
 Anonymized engineering-team case        
   study (100 engineers, 90 days)         
 Apple ML Research, RouteLLM, etc.       
                                          
 Limitations                              
 Case study from one team; results        
  mix — vary by codebase + task
 Model pricing changes monthly; ratios    
  absolutes — more stable than
                                          
 Full analysis                            
 [Author        [URL]                  Name] 
                                          
                                          

```

#### Typography rules for the template

- **Serif title** (Zone 2 only): `Georgia` (font-stack: `'Georgia', 'Times New Roman', serif`). Substitutes for unavailable Financier/Miller/Milo Serif. Size 38pt for cover, 30pt for exhibit slides.2632
- **Sans everything else**: `Helvetica Neue`. Already installed in render_part*.py.
- **Hero number on cover**: 120pt sans-bold, FT Blue.100
- **Source line**: 10pt italic, opacity 0.6 (alpha 0.6 in matplotlib).
- **Eyebrow**: 11pt sans-medium, all caps, letter-spacing +50, gold accent color.

#### LinkedIn post body specification

The carousel is accompanied by a LinkedIn post body. The body must:

- **Lede sentence (1st sentence)**: A risk-framed or specific-number hook. Example: *"One engineering team I worked with cut their AI bill from $3,000/day to $970/day in 90  a 68% reduction without firing anyone, downgrading models, or hurting code quality."*days 
- **4 supporting sentences**: The mechanism summary (routing + caching + workflow), one concrete data point, and the takeaway.2
 [URL]"*.
- **Total length**: 150 words. Less is fine. More is practitioner.80
- **No emoji**, **no bullet-point body**, **no all-caps emphasis**. Single paragraph; sentence-case.

#### What this template optimizes for

- **Reach**: A single-image first-slide on LinkedIn (the cover) maximizes feed display when carousels are not expanded; LinkedIn shows only Slide 1 in the preview.
- **Saves / Sends**: 4 substantive slides each carry standalone  readers save the whole carousel because individual slides are reference-grade.value 
- **Click-through to canonical URL**: CTA on cover (most-viewed slide) + CTA on optional slide 5 + URL in source line of every slide + URL in post body. Belt-suspenders-belt.
- **Executive credibility**: Serif title, neutral palette with single accent, named methodology, source line on every slide. Reads as McKinsey-grade, not as practitioner-influencer content.

#### Variants

| Variant | When to use |
|---|---|
| **Single-image post** (cover slide only, posted as image) | When the article has one obvious hero number and the goal is reach > saves |
| **3-slide micro-carousel** (cover + hero + CTA-slide) | When the article is short or the audience is mobile-heavy |
| **4-slide standard** (template above) | Default. The HBR/McKinsey/FT-grade LinkedIn standard. |
| **5-slide with methodology** | When the data is novel/contested and methodology credentials matter (e.g. survey data, modeled estimates) |
| **6-slide max** | Only when an article has 3 distinct exhibits each carrying independent weight |

**Hard ceiling: 6 slides. Hard floor: 1 (cover-only).**

---

14 References & Citations## 

### Books

- Edward Tufte, *The Visual Display of Quantitative Information* (Graphics Press, 1983; 2nd ed. 2001).
- Edward Tufte, *Envisioning Information* (Graphics Press, 1990).
- Edward Tufte, *Visual Explanations* (Graphics Press, 1997).
- Edward Tufte, *Beautiful Evidence* (Graphics Press, 2006).
- Gene Zelazny, *Say It With Charts: The Executive's Guide to Visual Communication* (McGraw-Hill, 4th ed. 2001). The McKinsey-internal-manual that became the executive chart-making canon.
- Barbara Minto, *The Pyramid Principle: Logic in Writing and Thinking* (Minto Books / Pearson, 1995; updated editions through 2009). The McKinsey communications-bible defining MECE + answer-first.
- Scott Berinato, *Good Charts: The HBR Guide to Making Smarter, More Persuasive Data Visualizations* (HBR Press, 2016).
- Nancy Duarte, *HBR Guide to Persuasive Presentations* (HBR Press, 2012).
- Nancy Duarte, *Resonate: Present Visual Stories that Transform Audiences* (Wiley, 2010).
- Andy Kirk, *Data Visualisation: A Handbook for Data Driven Design* (Sage, 2nd ed. 2019).
- Stephen Few, *Now You See It: Simple Visualization Techniques for Quantitative Analysis* (Analytics Press, 2009).
- Stephen Few, *Show Me the Numbers: Designing Tables and Graphs to Enlighten* (Analytics Press, 2nd ed. 2012).
- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Wiley, 2015).
- Daniel Kahneman, *Thinking, Fast and Slow* (Farrar, Straus and Giroux, 2011).
- Robert Cialdini, *Influence: The Psychology of Persuasion* (Harper Business, 1984, rev. 2006).
- Chip Heath & Dan Heath, *Made to Stick: Why Some Ideas Survive and Others Die* (Random House, 2007).

### Articles

- Scott Berinato, ["Visualizations That Really Work"](https://hbr.org/2016/06/visualizations-that-really-work) (HBR, June 2016). Establishes the typology of executive visualization that this framework codifies.
- Daniel Kahneman & Amos Tversky, "Prospect Theory: An Analysis of Decision under Risk" (*Econometrica* 47, no. 2, 1979). Loss-aversion psychology underlying the "risk hook" archetype.
- Alberto Cairo, ["The Functional Art" series at FT and at his own blog](http://www.thefunctionalart.com/). Practical examples of executive data visualization.
- Severino Ribecca, ["The Data Visualisation Catalogue"](https://datavizcatalogue.com/). Companion to FT Visual Vocabulary.

### Repositories & Open Resources

- FT Visual Vocabulary GitHub: [github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary). Authored by Alan Smith OBE (FT Data team).
- Andy Kirk, ["The Chartmaker Directory"](http://chartmaker.visualisingdata.com/). Cross-references chart types to tools that produce them.
- Andy Cotgreave, ["The Graphic Continuum"](https://policyviz.com/2014/09/04/the-graphic-continuum/). Inspiration for the FT vocabulary.

### Publication brand sources

- McKinsey & Company (corporate site): mckinsey. typeface attribution (Bower by Schick Toikka, 2018; McKinsey Sans custom).com 
- Harvard Business Review press kit: hbr.org/ HBR-Serif typeface attribution to Matthew Carter (Miller-derived).about 
- FT Financier Display typeface: Klim Type Foundry (Kris Sowersby, 2014).
- The Economist typography: Milo Serif by Mike Abbink; Econ Sans (custom). Post-2018 chart-redesign documented in Economist Data Team blog posts (most behind paywall).
- BCG (Boston Consulting Group): Henderson Sans typeface introduced in 2021 brand refresh.
- Pew Research Center methodology: [pewresearch.org/our-methods/](https://www.pewresearch.org/our- open survey-research methodology.methods/) 
- Statista format: statista. single-chart-of-the-day editorial format.com 
- Champions Design / Pentagram, *Economist redesign case studies* (publicly published).

### Wikipedia (background context)

- ["Edward Tufte"](https://en.wikipedia.org/wiki/Edward_Tufte)
- ["Data-ink ratio"](https://en.wikipedia.org/wiki/Data-ink_ratio) (includes Chartjunk)
- ["The Visual Display of Quantitative Information"](https://en.wikipedia.org/wiki/The_Visual_Display_of_Quantitative_Information)
- ["Harvard Business Review"](https://en.wikipedia.org/wiki/Harvard_Business_Review)
- ["The Economist"](https://en.wikipedia.org/wiki/The_Economist)
- ["Financial Times"](https://en.wikipedia.org/wiki/Financial_Times)
- ["McKinsey & Company"](https://en.wikipedia.org/wiki/McKinsey_%26_Company)
- ["Influence: The Psychology of Persuasion"](https://en.wikipedia.org/wiki/Influence:_The_Psychology_of_Persuasion)
- ["Made to Stick"](https://en.wikipedia.org/wiki/Made_to_Stick)

### Sibling research documents in this repo

- `.copilot-tracking/research/subagents/2026-05-13/practitioner-carousel-framework. companion Practitioner mode frameworkmd` 
- `.copilot-tracking/research/2026-05-13/visual-first-distillation-system-research. parent two-persona system designmd` 

---

## Caveats and unverified items

The following items in this research document were synthesized from public color-sampling, secondary references, or compositional  and should be **verified before being used as authoritative defaults in production code**:analysis 

- **Several brand hex codes** (especially  they do not publish official hex codes publicly). The values given are approximations from published material. The pipeline should treat these as defaults with the understanding that brand audits may refine them.HBR 
- **Specific exhibit anatomy claims for McKinsey/HBR/FT examples 12** are paraphrased composites of typical exhibits, not citations of a single named exhibit (because exhibit-level URLs change and primary sources are often paywalled).in 
- **The Economist 2018 chart-redesign Medium post** by Sarah Leo / Economist Data Team is referenced widely in design literature, but the canonical URL returned 403 in our  the substantive findings (palette simplification, larger fonts, minimal gridlines) are visible in any Economist chart since 2018 and are therefore high-confidence.fetch 
- **LinkedIn post-mix percentages for HBR/McKinsey/BCG** 7 are estimated from a 50-post snapshot of each showcase page at fetch time, not a longitudinal study.in 

---

## Status & Next Research Checklist

**Status: Complete.** All 9 research questions answered, all 5 deliverables produced.

**Recommended follow-up research (out of current scope, low priority):**

- [ ] **Bloomberg/Reuters data-viz house  possible 3rd executive-publication archetype if the audience tilts toward financial markets.style** 
- [ ] **NYT Upshot / WaPo / Reuters Graphics** style for news-data-viz hybrid that some executive audiences consume.
- [ ] **A/B test plan**: serif-title cover vs sans-title cover; FT-pink background vs white  to validate which feels more "McKinsey-grade" to actual decision-maker test audiences.background 
- [ ] **Statista format study** for chart-of-the-day single-exhibit posts (only briefly covered).
- [ ] **BBC Visual & Data Journalism** house  added third dimension to the executive lexicon for a UK/global audience.style 
- [ ] **Live brand-color audit** of HBR/McKinsey/BCG against their printed/digital outputs (the hex codes 3 are public approximations; a brand audit would refine).in 
- [ ] **Survey decision-makers** in target audience to validate which hook archetypes 8 yield highest engagement on LinkedIn (current ranking is from secondary research).from 
