<!-- markdownlint-disable-file -->
# Task Research: Visual-First Distillation System for Thought Leadership

Design a reusable visual-first distillation system that converts a base blog (single or series) into traffic-attracting, brand-building distilled posts across LinkedIn (post + Article), X/Twitter, Medium, and Substack. Distilled outputs must be predominantly VISUAL (carousels, infographic stacks, image cards, exhibits) with text reduced to a short intro/context block plus the canonical base-blog link. The system must support TWO selectable personas per run — **Practitioner mode** (Tech Lead / Senior Practitioner — Welsh / Lenny / Bloom carousel grammar) and **Executive mode** (Engineering Manager / Decision-Maker — HBR / McKinsey "exhibit" grammar) — and demo by regenerating the existing 12 distilled posts for the "AI Code Assistant Cost / Engineering Better AI Interactions" 3-part series.

## Task Implementation Requests

* Research and codify two distinct visual-thought-leadership frameworks:
  * **Practitioner carousel framework** (Justin Welsh / Lenny Rachitsky / Sahil Bloom mechanics — slide grammar, hook types, swipe-through cadence, save/share triggers)
  * **Executive exhibit framework** (HBR / McKinsey / FT mechanics — "exhibit" labeling, data-ink ratio, single-insight-per-exhibit, attribution conventions)
* Identify the historical thought-leadership marketing frameworks proven to drive traffic AND build brand authority (curiosity gap, IKEA effect, Zeigarnik effect, von Restorff isolation, AIDA, Heath brothers' SUCCESs, Cialdini influence triggers, ConvertKit/HBR data on visual-vs-text CTR).
* Map each platform's native visual format and platform-specific best-practice constraints (LinkedIn document/PDF carousel 8–10 slides, X image-thread up to 4 images per tweet, Medium hero-and-inline images with canonical-via-Import, Substack Note vs newsletter image constraints, LinkedIn Article inline images and Google indexing exposure).
* Define a slide-grammar template library (slide types: hook, problem, framework, data exhibit, before/after, quote, CTA) and how it maps across the two persona modes.
* Specify the new pipeline architecture: should a single `visual-distiller` agent replace/extend `social-linkedin`, `social-twitter`, and `platform-distiller`, or should we layer a `visual-pack-generator` skill that all three consume?
* Provide a concrete production plan for regenerating the AI Cost series demo (5 outputs × 3 parts × 2 modes = N artifacts; constrain to a tractable demo set).

## Scope and Success Criteria

* **In Scope**: visual-grammar research; framework selection per persona mode; platform-specific format research; new agent/skill architecture; demo regeneration plan for the AI Code Assistant Cost series (3 parts).
* **Out of Scope**: video reels / YouTube (separate agents already cover these); Reddit (text-first by platform norm); brand visual identity redesign (we reuse the existing design-token system and 22 PNG asset bank).
* **Assumptions**:
  * Existing 22 PNGs in `content/visuals/` are reusable as carousel/exhibit slides with minimal re-layout.
  * Existing visual-renderer agent (matplotlib + Pillow + Mermaid + 5-theme palette + 320 DPI) is the production engine — no new tooling required.
  * The 5 outputs in scope per part: LinkedIn Post (with carousel PDF), X/Twitter Thread (with image cards), Medium (hero + inline images), Substack Note (1 hero image + short excerpt), LinkedIn Article (text-first thought-leadership with 2–3 embedded exhibits — unique angle, NOT a blog republish).
  * Pipeline-config gains a new field `distillation_persona_mode: practitioner | executive` (default: ask).
  * Canonical-URL discipline preserved: every distilled post drives clicks back to the GitHub Pages canonical URL.
* **Success Criteria**:
  * Two persona-mode visual frameworks fully specified with slide-type taxonomy, hook patterns, color/typography rules, and CTA conventions.
  * Platform-by-platform visual specification (slide count, dimensions, format, copy budget) documented.
  * Architecture decision: single agent vs. layered skill — selected with rationale.
  * Demo plan: which of the 5×3×2 = 30 possible artifacts to regenerate first, with a clear acceptance test.
  * Research evidence is sourced from authoritative practitioners, published platform documentation, peer-reviewed marketing/psychology research, and observable case studies — not assertion-only.

## Outline

1. Why visual-first wins the click — psychology and engagement evidence
2. Persona Mode A — Practitioner Carousel Framework
3. Persona Mode B — Executive Exhibit Framework
4. Platform-by-platform visual format specifications
5. Slide grammar — the reusable template library
6. System architecture — single distiller vs. layered skill
7. Demo regeneration plan for AI Cost series
8. Risks, anti-patterns, and mitigation

## Potential Next Research

* Reference accounts to study: Justin Welsh, Lenny Rachitsky, Sahil Bloom, Packy McCormick, Alex Lieberman, Pat Walls (Practitioner mode); HBR Exhibits, McKinsey Insights, BCG slide formats, FT Visual Vocabulary (Executive mode).
* LinkedIn algorithm behavior on document posts (Hootsuite / SocialInsider / Buffer studies; LinkedIn engineering blog) — dwell time and reach signals.
* X/Twitter image-thread engagement data (post-2024 algorithm changes, image-vs-text CTR).
* Medium 2025/2026 algorithm changes affecting visual content surfacing.
* Substack Notes vs. newsletter visual norms.

## Research Executed

### File Analysis

* `content/ai-code-assistant-cost-part-1.md` (lines 1–261)
  * 3,200-word technical blog on GitHub Copilot model multipliers (0.25x–30x = 120x spread), task taxonomy (simple/moderate/complex), production case study ($3K/day → $970/day = 68% savings = $740K/yr annualized), RouteLLM (95% GPT-4 quality at 75% lower cost), CascadeFlow (69% savings + 96% quality retention).
  * Contains 3 inline image references: `model-multiplier-spectrum.png`, `task-routing-decision-tree.png`, `routing-savings-bar.png`.
  * Key data point inventory at lines 247–260 — every claim has a cited source.
* `content/ai-code-assistant-cost-part-2.md` (lines 1–213)
  * Caching + workflow discipline. Anthropic cache writes at 1.25x, cached reads 75–90% off; retry tax (1.4x at 40% retry rate, 1.5x at 50%); semantic caching (Redis 68.8% fewer API calls). 5 visuals referenced.
* `content/ai-code-assistant-cost-part-3.md` (lines 1–238)
  * Task taxonomy three-tier (60–70% / 20–30% / 5–10%), 0.55x effective average multiplier vs. 1x baseline = 45% savings, RouteLLM/CascadeFlow data, governance section (budget controls, pooled usage, cost-center allocation). 5 visuals referenced including team-governance-dashboard.png.
* Existing distilled posts — VERBOSE BUT TEXT-DOMINANT:
  * `content/linkedin-post-part1.md` (lines 1–107) — 600+ words, two versions (plain + Unicode). No carousel reference; relies entirely on inline text.
  * `content/linkedin-post-part2.md` (lines 1–95) — 540 words, plain+Unicode versions. Same anti-pattern: full-text rehash.
  * `content/linkedin-post-part3.md` (lines 1–112) — 660 words. Same pattern.
  * `content/x-twitter-thread.md` (lines 1–109) — 10-tweet thread, text-only, single image attachment noted only in "posting notes" footer.
  * `content/medium-post-part1.md` (lines 1–83) — ~800 words, zero visuals despite Medium fully supporting them.
  * `content/substack-post-part1.md` (lines 1–56) — 420 words, zero visuals.
  * `content/linkedin-article-part1.md` (lines 1–83) — 780 words, "unique angle" per platform-distiller spec, but text-only.
* Existing visual asset inventory — `content/visuals/` (22 PNGs)
  * Part 1 assets: `context-quality-paradox.png`, `context-engineering-framework.png`, `before-after-context.png`, `context-noise-breakdown.png`, `model-multiplier-spectrum.png`, `task-routing-decision-tree.png`, `routing-savings-bar.png`.
  * Part 2 assets: `prompt-structure-breakdown.png`, `caching-flow.png`, `retry-loop-anatomy.png`, `retry-tax-calculator.png`, `caching-comparison.png`.
  * Part 3 assets: `task-model-alignment.png`, `routing-decision-comparison.png`, `team-governance-dashboard.png`, `team-optimization-strategies.png`, `three-layer-stack.png`.
  * Production renderers: `render_part1.py`, `render_part2.py`, `render_part3.py`, `render_context_engineering.py`, `render_noise_breakdown.py`.
* `.github/agents/platform-distiller.agent.md` (lines 1–177)
  * CRITICAL CONSTRAINT in current spec at lines 14–28: "Prohibited in ALL outputs — zero exceptions: image markdown `![`, HTML `<img`, visual asset paths, Mermaid blocks, references to 'as shown in the diagram'." This is the explicit policy we are reversing.
  * Generates 3 outputs: Medium (700–900 words), Substack (300–500 words), LinkedIn Article (700–900 words, unique angle).
  * Does NOT generate the LinkedIn Post or X/Twitter Thread — those come from `social-linkedin.agent.md` and `social-twitter.agent.md` earlier in the pipeline.
* `.github/agents/visual-renderer.agent.md` (lines 1–150)
  * Provides matplotlib + Pillow + Mermaid generation with 5 themes (default, ocean, sunset, forest, midnight) and round-robin theme assignment per visual.
  * 320 DPI required, Helvetica Neue font, narrow-segment rule (<15% width → external labels), data-ink ratio (Tufte) and Gestalt grouping built into the design principles.
  * Existing capability is fully sufficient to produce carousel slides at 1080×1080 (LinkedIn square), 1080×1350 (LinkedIn portrait), and 1200×1500 PDF slides — no new tooling required.
* `content/pipeline-config.md` (lines 1–302)
  * Persona analysis (line 178–185): 4 personas — Senior Developer, Tech Lead, Engineering Manager, Platform Engineer. Tech Lead + Engineering Manager align directly with the two requested modes.
  * Publish sequence at lines 293–301: explicit cadence per platform (Day 0 = blog/Medium/LinkedIn; Day 1 = Twitter; Day 3–4 = Substack; Day 7+ = LinkedIn Article).
  * Step 12 = platform distillation (lines 51, 199–207) — only Medium / Substack / LinkedIn Article. The new system extends this to ALSO transform the Step 4–5 social outputs (LinkedIn Post + X Thread).

### External Research

All 5 subagent research documents completed — full details in `.copilot-tracking/research/subagents/2026-05-13/`:

* **Practitioner Carousel Framework** → `practitioner-carousel-framework.md` (695 lines)
  * Justin Welsh, Lenny Rachitsky, Sahil Bloom, Packy McCormick, Pat Walls mechanics
  * Canonical 10-slide template, 7 hook archetypes, typography grammar, CTA conventions
  * Key stat: LinkedIn carousels earn +278% engagement vs video, +596% vs text (Buffer 2025)
* **Executive Exhibit Framework** → `executive-exhibit-framework.md` (1413 lines)
  * HBR, McKinsey, BCG, FT Visual Vocabulary, Tufte data-ink principles
  * 4-zone exhibit anatomy, conclusion-as-title convention, 2-3 color discipline
  * Key stat: Executive briefings use 3-5 exhibits (not 10+ slides), one insight per exhibit
* **Platform Visual Specs** → `platform-visual-specs.md` (509 lines)
  * LinkedIn PDF carousel: 1080×1080px, max 300 slides, link in first comment (body link = reach penalty)
  * X/Twitter: 1600×900px, max 4 images/tweet, link in last tweet (body link penalty confirmed)
  * Medium Import tool sets `rel=canonical` → protects GitHub Pages SEO
  * Substack Notes: up to 6 images, don't email subscribers — serve discovery only
  * Cross-platform sequencing: Day 0 publish + Medium import + LinkedIn carousel + X thread → Day 3 Substack Note → Day 7+ LinkedIn Article (unique angle)
* **Thought-Leadership Psychology Frameworks** → `thought-leadership-psychology-frameworks.md` (460 lines)
  * 12 frameworks researched: Curiosity Gap, Zeigarnik, IKEA Effect, Von Restorff, Processing Fluency, AIDA, SUCCESs, Cialdini, Dual-Coding, Peak-End, Concrete Language, Big Idea
  * Weighted scoring rubric (12 dimensions, 1-5 scale) for evaluating distilled posts
  * Optimal psychology stack mapped to slide positions (hook → problem → solution → interrupt → CTA)
* **Visual Content Engagement Data** → `visual-content-engagement-data.md` (350+ lines)
  * LinkedIn carousel 7.00% engagement vs text 4.50% = 1.56x multiplier (SocialInsider 2026, 1.3M posts)
  * Image tweets +35–150% more retweets (Buffer, Twitter official, Sotrender — multiple studies)
  * Text+illustrations = 323% better comprehension (Springer academic study)
  * 73% of B2B decision-makers trust thought leadership over marketing (Edelman-LinkedIn 2024)
  * Developer audiences prefer functional visuals (diagrams, architecture) over decorative imagery

### Project Conventions

* Standards referenced:
  * Design token system documented in `.github/copilot-instructions.md` and `.github/agents/visual-renderer.agent.md` — 5-theme palette, Helvetica Neue, 320 DPI, no Unicode glyphs in matplotlib.
  * Social formatting in `.github/instructions/social-formatting.instructions.md` — LinkedIn/X use Unicode Mathematical Bold Sans-Serif and Italic; Reddit uses standard Markdown.
  * Content quality bar in `.github/instructions/content-quality.instructions.md` — every claim needs a number/model/benchmark; first-person customer voice; no corporate framing.
* Instructions followed:
  * Distilled posts must drive clicks to the GitHub Pages canonical URL.
  * Medium Import tool sets canonical automatically; Substack Notes avoid duplicate-content penalty by staying under 500 words; LinkedIn Article must be a UNIQUE ANGLE (not a republish) because Google indexes it without canonical protection.

## Key Discoveries

### 1. The Quantitative Case for Visual-First (Why This Matters)

| Format Comparison | Multiplier | Source | Date |
|---|---|---|---|
| LinkedIn carousel vs text | 1.56x engagement | SocialInsider (1.3M posts) | Mar 2026 |
| LinkedIn carousel vs link posts | 2.15x engagement | SocialInsider | Mar 2026 |
| LinkedIn carousel (Buffer dataset) | +596% vs text-only | Buffer (multi-million posts) | 2025 |
| Image tweets vs text tweets | +35% to +150% retweets | Twitter official, Buffer, Sotrender | 2024-2026 |
| Text + illustrations vs text only | +323% comprehension | Springer (academic) | Evergreen |
| LinkedIn dwell time (carousel) | 35-55 sec vs 8-12 sec text | Hootsuite 2026 | 2026 |

**Bottom line**: Switching from text-first to visual-first distilled posts should deliver **1.5-6x engagement uplift on LinkedIn** and **1.5-2.5x on X/Twitter**. The mechanism is processing fluency (visual content processed faster → judged more credible) + dwell time (swipe behavior feeds LinkedIn's algorithm).

### 2. Two Persona Modes — Fully Specified

**Practitioner Mode (Tech Lead audience)**:
* 10-slide PDF carousel, 1080×1080px, 4:5 portrait
* Slide grammar: Hook → Promise → Problem → Framework → 4-5 Steps → Recap → CTA
* 3-color palette: white BG + dark text (#1e293b) + ONE brand accent (#1f6feb)
* 30-50 words per slide max; hero text 48-72pt
* Hook archetype: Framework hook ("The N-step framework for [outcome]") — 60% of the time
* CTA: Final slide visual only; canonical link in FIRST COMMENT (<60 sec post-publish)
* X/Twitter analog: image-anchored thread (same PNG templates, 1-2 images per tweet)

**Executive Mode (Engineering Manager / Decision-Maker audience)**:
* 3-5 hero exhibits (NOT a 10-slide carousel)
* Exhibit anatomy: Exhibit label → Conclusion-as-title → Subtitle/source → Visual → Source attribution line
* Typography: serif headlines for gravitas + sans-serif exhibit chrome
* 2-3 color max per exhibit: navy (#051C2C) + one accent + gray series
* Chart-type-by-message: FT Visual Vocabulary (9 families: deviation, correlation, ranking, distribution, change-over-time, magnitude, part-to-whole, spatial, flow)
* Data-ink ratio: strip gridlines, 3D, legends; keep direct labels, annotations, source lines
* Hook pattern: Risk framing ("the bill nobody expected") or ROI framing ("68% cost reduction in 90 days")
* CTA: Discreet article link in caption, not a visual CTA slide

### 3. Platform Constraints Matrix

| Platform | Optimal Format | Dimensions | Max Visual | Copy Budget | CTA Location | Canonical Risk |
|---|---|---|---|---|---|---|
| LinkedIn Post | PDF carousel | 1080×1080 | 300 slides (10 optimal) | 20-50 words/slide | First comment | None |
| LinkedIn Article | Text + 2-3 embedded exhibits | 1200×627 hero | Unlimited inline | 800-2000 words | End of article | HIGH (no canonical) |
| X/Twitter | Image-anchored thread | 1600×900 or 1080×1080 | 4 per tweet | 200-240 chars/tweet | Last tweet | None |
| Medium | Import with hero + inline | 1400px wide | Unlimited | 800-3000 words | End of article | LOW (import sets canonical) |
| Substack Note | 1-3 images + teaser | 1200×630 | 6 | 150-300 chars | Inline link | None |

### 4. Psychology Stack Per Slide Position

| Position | Primary Frameworks | Secondary | Example Application |
|---|---|---|---|
| Slide 1 (Hook) | Curiosity Gap + Von Restorff + Peak-End (peak) | Processing Fluency | "Your AI bill is 3x what it should be" + giant "$3K" number |
| Slides 2-3 (Problem) | SUCCESs (Unexpected + Concrete) + Dual-Coding | AIDA (Interest) | Surprising data chart + one-sentence insight |
| Slides 4-6 (Solution) | Cialdini (Authority + Social Proof) + SUCCESs (Credible) | AIDA (Desire) | Named tools, case study snippet, team count |
| Slide 7 (Pattern Interrupt) | Von Restorff + SUCCESs (Emotional) | Concrete Language | Dark-BG pull-quote: "That $2K/day waste? It's someone's salary." |
| Final Slide (CTA) | Peak-End (end) + Cialdini (Commitment + Reciprocity) | Big Idea restatement | "Save this → Read the full guide → Link in comments" |

### 5. Cross-Platform Sequencing

```
Day 0: GitHub Pages publish (canonical URL established)
       + Medium Import (sets rel=canonical → safe)
       + LinkedIn PDF carousel (link in first comment)
       + X/Twitter image thread (link in last tweet)
Day 3: Substack Note (excerpt + 1 image + link)
Day 7+: LinkedIn Article (unique angle, >30% new material, link in body)
```

## Technical Scenarios

### Scenario 1: Single `visual-distiller` Agent (Replaces 3 Existing Agents)

**Description**: A single new agent `visual-distiller` replaces `social-linkedin`, `social-twitter`, and `platform-distiller`. It reads the base blog, selects persona mode from `pipeline-config.md`, generates the visual pack (carousel slides + exhibits) via `visual-renderer`, and emits all 5 distilled outputs.

**Requirements**:
* Agent reads `distillation_persona_mode` from `pipeline-config.md`
* Agent calls `visual-renderer` to produce carousel slides / exhibits
* Agent emits: LinkedIn Post + carousel PDF, X Thread + image cards, Medium text + images, Substack Note + hero image, LinkedIn Article + exhibits
* Agent respects platform constraints (dimensions, copy budgets, CTA placement)

**Preferred Approach**: ❌ NOT selected

**Advantages**:
* Single entry point — simpler orchestration
* Unified context about the base blog — no redundant reading
* Easy to add persona modes without touching multiple agents

**Limitations**:
* Violates separation of concerns — one agent doing 5 very different jobs
* Existing pipeline Steps 4-5 (social-linkedin, social-twitter) and Step 12 (platform-distiller) would be skipped entirely, breaking the pipeline sequence
* Agent prompt would be enormous (5 platform specs + 2 persona modes = 10 behavioral variants in one prompt)
* Hard to test or iterate on one platform without affecting others
* Regression risk: changes to LinkedIn format break Medium output

### Scenario 2: Layered `visual-pack-generator` Skill + Existing Agents Consume It

**Description**: A new **skill** (`visual-pack-generator`) generates the visual asset pack (carousel slides, exhibit images) from the base blog content and persona mode. The 3 existing agents (`social-linkedin`, `social-twitter`, `platform-distiller`) are UPDATED to consume the visual pack and embed images into their respective outputs.

**Requirements**:
* New skill: `.github/skills/visual-pack-generator.skill.md`
* Skill reads base blog + persona mode → produces `content/visuals/distilled/` directory with platform-specific assets
* `social-linkedin.agent.md` updated: consume carousel slides → emit LinkedIn Post with PDF carousel reference + first-comment CTA
* `social-twitter.agent.md` updated: consume image cards → emit image-anchored thread
* `platform-distiller.agent.md` updated: REVERSE the image prohibition (lines 14-28), consume exhibit/hero images → emit Medium, Substack, LinkedIn Article with embedded visuals
* `pipeline-config.md` gains `distillation_persona_mode: practitioner | executive`

**Preferred Approach**: ✅ SELECTED

```text
.github/
  skills/
    visual-pack-generator.skill.md   (NEW — visual asset generation skill)
  agents/
    social-linkedin.agent.md          (UPDATED — consume visual pack)
    social-twitter.agent.md           (UPDATED — consume visual pack)
    platform-distiller.agent.md       (UPDATED — reverse image prohibition, consume visual pack)
    visual-renderer.agent.md          (UNCHANGED — production engine)
content/
  visuals/
    distilled/                        (NEW — output directory for distilled visual assets)
      part1-practitioner/             (carousel slides, hero images per persona)
      part1-executive/
  pipeline-config.md                  (UPDATED — add distillation_persona_mode)
```

**Advantages**:
* Preserves pipeline architecture — Steps 4, 5, 12 continue to work
* Separation of concerns: skill generates visuals, agents compose platform-specific output
* Each agent can be updated and tested independently
* Visual pack is reusable across agents (same carousel slide used by LinkedIn + X)
* Incremental migration: update one agent at a time, not a big-bang replacement
* Visual pack can be regenerated without re-running all agents

**Limitations**:
* Slightly more complex architecture (skill + 3 agent updates vs 1 new agent)
* Agents must coordinate on the `content/visuals/distilled/` directory convention
* Two-step process: generate visual pack THEN run agents (not single invocation)

**Rationale for selection**: The layered approach follows the existing pipeline's separation-of-concerns pattern. Each agent already has a well-defined role (LinkedIn post composition, X thread composition, platform distillation). Adding visual awareness to each agent is a smaller, lower-risk change than replacing all three with a monolithic agent. The visual pack generation is the genuinely new capability — extracting it as a reusable skill maximizes reuse and testability.

#### Considered Alternative: Scenario 1 (Single Agent)

Rejected because it violates separation of concerns, creates an enormous prompt surface, and introduces regression risk when iterating on any single platform's output. The monolithic approach also breaks the existing pipeline step numbering (Steps 4, 5, 12), requiring a pipeline-wide refactor that isn't justified.

### Demo Regeneration Plan

**Constraint**: Full matrix is 5 outputs × 3 parts × 2 modes = 30 artifacts. For demo, constrain to **Part 1 only × both modes = 10 artifacts**.

| # | Artifact | Persona Mode | Key Visual Assets |
|---|---|---|---|
| 1 | LinkedIn Post + Carousel PDF | Practitioner | 10-slide carousel (model multiplier spectrum, routing decision tree, savings bar) |
| 2 | LinkedIn Post + Exhibit Pack | Executive | 3 hero exhibits (cost deviation chart, routing flow, ROI magnitude chart) |
| 3 | X Thread + Image Cards | Practitioner | 4-5 image cards matching carousel slides |
| 4 | X Thread + Exhibit Images | Executive | 2-3 exhibit images inline |
| 5 | Medium (import-ready) | Practitioner | Hero + 3 inline carousel-derived images |
| 6 | Medium (import-ready) | Executive | Hero + 2 inline exhibit images |
| 7 | Substack Note | Practitioner | 1 carousel cover image |
| 8 | Substack Note | Executive | 1 exhibit hero image |
| 9 | LinkedIn Article | Practitioner | 2 inline framework visuals (unique angle text) |
| 10 | LinkedIn Article | Executive | 2 inline exhibit visuals (unique angle text) |

**Acceptance test**: Each artifact can be directly copy-pasted (text) or uploaded (images/PDF) to its target platform with zero manual editing.

## Operational Constraints

* All file edits restricted to `.copilot-tracking/research/2026-05-13/`.
* Production renderers, distilled posts, and agent definitions are referenced but not modified during research.
* The selected approach in this document is the input to a subsequent `/task-plan` invocation that will modify the actual repo.
