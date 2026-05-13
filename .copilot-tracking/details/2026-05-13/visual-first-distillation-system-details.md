<!-- markdownlint-disable-file -->
# Implementation Details: Visual-First Distillation System for Thought Leadership

## Context Reference

Sources: .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md, .copilot-tracking/research/subagents/2026-05-13/codebase-architecture-for-distillation.md, .copilot-tracking/research/subagents/2026-05-13/practitioner-carousel-framework.md, .copilot-tracking/research/subagents/2026-05-13/executive-exhibit-framework.md, .copilot-tracking/research/subagents/2026-05-13/platform-visual-specs.md, .copilot-tracking/research/subagents/2026-05-13/thought-leadership-psychology-frameworks.md

## Implementation Phase 1: Create Visual Pack Generator Skill

<!-- parallelizable: true -->

### Step 1.1: Create `.github/skills/visual-pack-generator/SKILL.md`

Create the core skill definition following the existing skill naming convention (kebab-case directory, `SKILL.md` uppercase file, optional `references/` subdirectory).

The skill definition must specify:

**Frontmatter**:
```yaml
---
name: visual-pack-generator
description: 'Generate platform-optimized visual asset packs from blog content for visual-first distilled posts. Supports Practitioner (carousel) and Executive (exhibit) persona modes.'
argument-hint: 'Provide the blog file path, part number, and persona mode (practitioner or executive)'
---
```

**When to Use**: Triggered by distribution agents (social-linkedin, social-twitter, platform-distiller) when `distillation_persona_mode` is set in pipeline-config.md.

**Procedure** (7 steps):
1. Read the base blog post and extract: title, key data points (numbers, percentages, case study metrics), framework/taxonomy structure, visual asset references (existing PNGs in `content/visuals/`)
2. Read `distillation_persona_mode` from `content/pipeline-config.md` — values: `practitioner`, `executive`, or `ask` (prompt user)
3. Load slide grammar from `references/slide-grammar.md` for the selected persona mode
4. Load platform specs from `references/platform-specs.md` for target dimensions
5. Generate the visual asset pack by invoking `visual-renderer` agent capabilities:
   - **Practitioner mode**: 10-slide carousel (1080×1080px) + 4-5 X image cards (1600×900px) + 1 hero image (1400×800px for Medium) + 1 Substack hero (1200×630px)
   - **Executive mode**: 3-5 exhibits (1200×627px for LinkedIn Article) + 2-3 X exhibit images (1600×900px) + 1 Medium hero (1400×800px) + 1 Substack hero (1200×630px)
6. Save visual pack to `content/visuals/distilled/{slug}-{mode}/` (e.g., `content/visuals/distilled/part1-practitioner/`)
7. Generate a manifest file `content/visuals/distilled/{slug}-{mode}/manifest.md` listing all generated assets with platform target, dimensions, and slide position

**Output directory structure**:
```
content/visuals/distilled/
  part1-practitioner/
    slide-01-hook.png              (1080×1080, LinkedIn carousel)
    slide-02-promise.png           (1080×1080, LinkedIn carousel)
    slide-03-problem.png           (1080×1080, LinkedIn carousel)
    slide-04-framework.png         (1080×1080, LinkedIn carousel)
    slide-05-step1.png             (1080×1080, LinkedIn carousel)
    slide-06-step2.png             (1080×1080, LinkedIn carousel)
    slide-07-step3.png             (1080×1080, LinkedIn carousel)
    slide-08-interrupt.png         (1080×1080, LinkedIn carousel)
    slide-09-recap.png             (1080×1080, LinkedIn carousel)
    slide-10-cta.png               (1080×1080, LinkedIn carousel)
    x-card-01.png                  (1600×900, X/Twitter)
    x-card-02.png                  (1600×900, X/Twitter)
    x-card-03.png                  (1600×900, X/Twitter)
    x-card-04.png                  (1600×900, X/Twitter)
    medium-hero.png                (1400×800, Medium)
    medium-inline-01.png           (1400×800, Medium)
    medium-inline-02.png           (1400×800, Medium)
    substack-hero.png              (1200×630, Substack)
    linkedin-article-exhibit-01.png (1200×627, LinkedIn Article)
    linkedin-article-exhibit-02.png (1200×627, LinkedIn Article)
    manifest.md                    (asset inventory)
    render_distilled.py            (Python renderer script)
  part1-executive/
    exhibit-01-cost-deviation.png  (1200×627, LinkedIn Article + Post)
    exhibit-02-routing-flow.png    (1200×627, LinkedIn Article + Post)
    exhibit-03-roi-magnitude.png   (1200×627, LinkedIn Article + Post)
    x-exhibit-01.png               (1600×900, X/Twitter)
    x-exhibit-02.png               (1600×900, X/Twitter)
    medium-hero.png                (1400×800, Medium)
    medium-inline-01.png           (1400×800, Medium)
    substack-hero.png              (1200×630, Substack)
    manifest.md
    render_distilled.py
```

**Critical Rules**:
- All visual assets use the existing design token system (15 tokens from .github/copilot-instructions.md)
- 320 DPI for all PNG output
- Helvetica Neue font (no serif fonts, per DD-03)
- No Unicode glyphs in matplotlib
- Each visual is a standalone function in the renderer script accepting `tokens` dict
- Practitioner mode: 3-color palette (white BG + dark text #1e293b + ONE brand accent #1f6feb)
- Executive mode: 2-3 color max per exhibit (navy #051C2C + one accent + gray series)
- Round-robin theme assignment from visual-renderer's 5 themes
- Existing blog PNGs in `content/visuals/` may be used as source material for recomposition

Files:
* `.github/skills/visual-pack-generator/SKILL.md` - New skill definition (create)
* `.github/skills/visual-pack-generator/references/` - References directory (create)

Success criteria:
* SKILL.md exists with correct frontmatter (name, description, argument-hint)
* Procedure covers all 7 steps with explicit inputs and outputs
* Output directory structure documented
* Critical rules section includes all design token and rendering constraints

Context references:
* .copilot-tracking/research/subagents/2026-05-13/codebase-architecture-for-distillation.md (Lines 252-298) - Skill naming conventions and structure
* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 223-267) - Architecture decision

Dependencies:
* None (first step)

### Step 1.2: Create `.github/skills/visual-pack-generator/references/slide-grammar.md`

Define the reusable slide-type taxonomy for both persona modes. This reference file maps each slide position to its content type, psychology framework, and visual treatment.

**Practitioner Mode — 10-Slide Carousel Grammar**:

| Position | Slide Type | Content | Psychology Framework | Visual Treatment |
|----------|-----------|---------|---------------------|-----------------|
| 1 | Hook | Surprising stat or bold claim | Curiosity Gap + Von Restorff | Giant number (48-72pt), dark background, minimal text |
| 2 | Promise | What reader will learn | Processing Fluency | 3-5 bullet promise list, clean white background |
| 3 | Problem | Pain point with data | SUCCESs (Unexpected + Concrete) | Before/after split or problem chart |
| 4 | Framework | The taxonomy/model | AIDA (Interest) + Dual-Coding | Diagram or tiered model visualization |
| 5-7 | Steps | 1-3 actionable steps | Cialdini (Authority) + SUCCESs (Credible) | Numbered steps with icon/data per step |
| 8 | Pattern Interrupt | Emotional pull-quote | Von Restorff + SUCCESs (Emotional) | Dark BG, large quote text, contrasting accent |
| 9 | Recap | Summary of key points | Peak-End (approach end) | Checklist or summary card |
| 10 | CTA | Save/share/link prompt | Peak-End (end) + Cialdini (Reciprocity) | Arrow to comments, "Link in comments" text, save icon |

**Executive Mode — 3-5 Exhibit Grammar**:

| Position | Exhibit Type | Content | Design Convention | Visual Treatment |
|----------|-------------|---------|-------------------|-----------------|
| 1 | Context Exhibit | The problem framed as risk/cost | Conclusion-as-title | Deviation chart or cost waterfall |
| 2 | Evidence Exhibit | Data supporting the solution | Single-insight-per-exhibit | Bar/line chart with direct labels, source attribution |
| 3 | Framework Exhibit | The decision model | FT Visual Vocabulary mapping | Flow or part-to-whole chart |
| 4 (optional) | ROI Exhibit | Business impact quantified | Magnitude comparison | Before/after magnitude bars |
| 5 (optional) | Action Exhibit | Recommended next steps | Concrete Language framework | Timeline or priority matrix |

**Slide content rules** (both modes):
- Max 30-50 words per slide/exhibit
- Hero text: 48-72pt (practitioner), 36-48pt (executive)
- Every slide must be comprehensible standalone (no "as we discussed" references)
- Data points must include source attribution on the slide
- CTA never appears on visual content in executive mode (CTA is in caption text only)

Files:
* `.github/skills/visual-pack-generator/references/slide-grammar.md` - New reference file (create)

Success criteria:
* Both persona mode grammars fully specified with all slide positions
* Psychology framework mapping for each position documented
* Visual treatment guidance for each slide type
* Word count and typography constraints specified

Context references:
* .copilot-tracking/research/subagents/2026-05-13/practitioner-carousel-framework.md - 10-slide carousel template and hook archetypes
* .copilot-tracking/research/subagents/2026-05-13/executive-exhibit-framework.md - 4-zone exhibit anatomy
* .copilot-tracking/research/subagents/2026-05-13/thought-leadership-psychology-frameworks.md - Framework-to-position mapping

Dependencies:
* Step 1.1 (directory structure created)

### Step 1.3: Create `.github/skills/visual-pack-generator/references/platform-specs.md`

Document per-platform visual format specifications as a quick-reference for the skill and consuming agents.

**Platform Specification Table**:

| Platform | Format | Dimensions (px) | Max Visuals | Copy Budget | CTA Location | File Format |
|----------|--------|-----------------|-------------|-------------|--------------|-------------|
| LinkedIn Post (carousel) | PDF carousel | 1080×1080 (square) or 1080×1350 (portrait) | 10 slides optimal, 300 max | 20-50 words/slide | First comment (post within 60 sec) | PNG slides → manual PDF assembly |
| LinkedIn Article | Inline exhibits | 1200×627 (hero), 1200×627 (inline) | 2-3 inline exhibits | 800-2000 words | End of article body | PNG |
| X/Twitter | Image cards per tweet | 1600×900 (landscape) or 1080×1080 (square) | 4 images per tweet | 200-240 chars/tweet | Last tweet in thread | PNG |
| Medium | Hero + inline images | 1400px wide (auto height) | Unlimited inline | 800-3000 words | End of article | PNG (via Import tool) |
| Substack Note | Hero + optional inline | 1200×630 | 1-3 images (6 max) | 150-300 chars | Inline link | PNG |

**Platform-specific rules**:
- LinkedIn: Link in body = reach penalty. Always use first comment for canonical URL.
- X/Twitter: Link in tweet body = engagement penalty. Place canonical URL in final tweet only.
- Medium: MUST use Import tool (not paste) to preserve `rel=canonical` to GitHub Pages.
- Substack: Post as NOTE (not newsletter) — Notes don't email subscribers, serve ambient discovery.
- LinkedIn Article: UNIQUE ANGLE required — Google indexes without canonical protection. Must have >30% new material vs blog.

Files:
* `.github/skills/visual-pack-generator/references/platform-specs.md` - New reference file (create)

Success criteria:
* All 5 platform specs documented with dimensions, limits, and format requirements
* CTA placement rules specified per platform
* Canonical URL protection rules documented
* File format requirements specified

Context references:
* .copilot-tracking/research/subagents/2026-05-13/platform-visual-specs.md - Full platform specifications
* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 166-174) - Platform constraints matrix

Dependencies:
* Step 1.1 (directory structure created)

### Step 1.4: Create `.github/skills/visual-pack-generator/references/psychology-stack.md`

Map the 12 researched psychology/marketing frameworks to specific slide positions and content patterns.

**Optimal Psychology Stack Per Slide Position** (from research):

| Position | Primary Frameworks | Secondary | Application Example |
|----------|-------------------|-----------|-------------------|
| Slide 1 (Hook) | Curiosity Gap + Von Restorff + Peak-End (peak) | Processing Fluency | "Your AI bill is 3x what it should be" + giant "$3K" number |
| Slides 2-3 (Problem) | SUCCESs (Unexpected + Concrete) + Dual-Coding | AIDA (Interest) | Surprising data chart + one-sentence insight |
| Slides 4-6 (Solution) | Cialdini (Authority + Social Proof) + SUCCESs (Credible) | AIDA (Desire) | Named tools, case study snippet, team count |
| Slide 7 (Pattern Interrupt) | Von Restorff + SUCCESs (Emotional) | Concrete Language | Dark-BG pull-quote: "That $2K/day waste? It's someone's salary." |
| Final Slide (CTA) | Peak-End (end) + Cialdini (Commitment + Reciprocity) | Big Idea restatement | "Save this → Read the full guide → Link in comments" |

**Framework Quick-Reference** (12 frameworks):
1. Curiosity Gap — open a question the reader must close
2. Zeigarnik Effect — incomplete information is more memorable
3. IKEA Effect — engagement through co-creation / interaction
4. Von Restorff Isolation — visually distinct elements are remembered
5. Processing Fluency — easier to process = judged more credible
6. AIDA — Attention → Interest → Desire → Action
7. SUCCESs — Simple, Unexpected, Concrete, Credible, Emotional, Stories
8. Cialdini Influence — Authority, Social Proof, Reciprocity, Commitment, Scarcity, Liking
9. Dual-Coding Theory — text + visuals = 323% better comprehension
10. Peak-End Rule — experiences judged by peak moment and ending
11. Concrete Language — specific details beat abstract claims
12. Big Idea — one memorable takeaway per piece

Files:
* `.github/skills/visual-pack-generator/references/psychology-stack.md` - New reference file (create)

Success criteria:
* All 12 frameworks listed with one-sentence description
* Framework-to-position mapping table complete
* Application examples using AI Cost series data points
* Both persona modes addressed (practitioner uses all 12; executive emphasizes Authority, Processing Fluency, Concrete Language)

Context references:
* .copilot-tracking/research/subagents/2026-05-13/thought-leadership-psychology-frameworks.md - Full framework research
* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 176-184) - Psychology stack per position

Dependencies:
* Step 1.1 (directory structure created)

## Implementation Phase 2: Update Existing Agents for Visual Consumption

<!-- parallelizable: true -->

### Step 2.1: Update `social-linkedin.agent.md`

Modify the LinkedIn post agent to consume visual packs and produce carousel/exhibit-referenced posts.

**Changes required**:

1. **Add visual-pack awareness to frontmatter description**: Update description to mention visual-first output capability.

2. **Add conditional visual-first path to Procedure**:
   - Before Step 1 (current: read blog), add: Check if `distillation_persona_mode` is set in `content/pipeline-config.md`. If set, check for visual pack at `content/visuals/distilled/{slug}-{mode}/manifest.md`.
   - If visual pack exists → use visual-first procedure (new)
   - If no visual pack → use existing text-only procedure (backward compatible)

3. **New visual-first procedure** (Practitioner mode):
   - Read manifest.md to identify carousel slides
   - Write LinkedIn post with SHORT intro text (100-150 words max, not 600+)
   - Reference carousel slides: "📎 Carousel: [slide-01-hook.png through slide-10-cta.png]"
   - Add posting instructions: "Upload slides as PDF document post. Add canonical URL as first comment within 60 seconds."
   - Wrap in `── START COPY (LinkedIn Post — Practitioner Visual) ──` markers

4. **New visual-first procedure** (Executive mode):
   - Read manifest.md to identify exhibits
   - Write LinkedIn post with context paragraph (100-200 words)
   - Reference exhibits inline: "📎 Exhibits: [exhibit-01.png, exhibit-02.png, exhibit-03.png]"
   - Add posting instructions: "Upload as multi-image post (not PDF carousel). Add canonical URL as first comment."
   - Wrap in `── START COPY (LinkedIn Post — Executive Visual) ──` markers

5. **Preserve backward compatibility**: The existing text-only path remains the default when no visual pack exists.

**Key constraint**: The agent itself does NOT generate visuals. It reads the pre-generated visual pack manifest and composes the text wrapper + posting instructions referencing the assets.

Files:
* `.github/agents/social-linkedin.agent.md` - Existing agent (modify)

Discrepancy references:
* Addresses DD-01: skill invocation within agent rather than standalone step
* Addresses DD-02: references individual PNGs rather than assembled PDF

Success criteria:
* Agent produces visual-first LinkedIn posts when visual pack exists
* Agent falls back to text-only when no visual pack exists
* Post text is ≤ 200 words (not 600+ as current text-only versions)
* Carousel/exhibit references are clear posting instructions
* First-comment CTA convention preserved

Context references:
* .copilot-tracking/research/subagents/2026-05-13/codebase-architecture-for-distillation.md (Lines 22-55) - Current social-linkedin agent structure
* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 147-154) - Practitioner LinkedIn specs
* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 156-164) - Executive LinkedIn specs

Dependencies:
* Phase 1 completion (visual-pack-generator skill and references exist for context)

### Step 2.2: Update `social-twitter.agent.md`

Modify the X/Twitter thread agent to consume image cards and produce image-anchored threads.

**Changes required**:

1. **Add visual-pack awareness to frontmatter description**: Update to mention image-anchored thread capability.

2. **Add conditional visual-first path to Procedure**:
   - Check for visual pack manifest before generating thread
   - If visual pack exists → image-anchored thread procedure
   - If no visual pack → existing text-only thread (backward compatible)

3. **New image-anchored thread procedure** (Practitioner mode):
   - Read manifest.md to identify X image cards (x-card-01.png through x-card-04.png)
   - Write hook tweet (tweet 1) with image reference: "📎 Image: x-card-01.png"
   - Write 3-5 content tweets with 1 image each (max 4 images per tweet)
   - Write final tweet with canonical URL + no image
   - Each tweet ≤ 280 characters (text portion)
   - Wrap in `── START COPY (X Thread — Practitioner Visual) ──` markers

4. **New image-anchored thread procedure** (Executive mode):
   - Read manifest.md to identify X exhibit images
   - Write hook tweet with exhibit-01 image reference
   - Write 2-3 content tweets with exhibit images
   - Write final tweet with canonical URL
   - Wrap in `── START COPY (X Thread — Executive Visual) ──` markers

5. **Preserve backward compatibility**: Text-only thread remains default.

**Key constraint**: URLs count as 23 characters (t.co wrapping). Each tweet must be ≤ 280 chars including the image attachment note.

Files:
* `.github/agents/social-twitter.agent.md` - Existing agent (modify)

Success criteria:
* Agent produces image-anchored threads when visual pack exists
* Falls back to text-only when no visual pack exists
* Every tweet ≤ 280 characters
* Image references are clear per-tweet posting instructions
* Canonical URL in final tweet only

Context references:
* .copilot-tracking/research/subagents/2026-05-13/codebase-architecture-for-distillation.md (Lines 58-88) - Current social-twitter agent structure
* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 154, 170) - X/Twitter platform specs

Dependencies:
* Phase 1 completion (visual-pack-generator skill exists for context)

### Step 2.3: Update `platform-distiller.agent.md`

This is the most significant agent change: REVERSE the explicit image prohibition and add visual asset consumption for all 3 outputs (Medium, Substack, LinkedIn Article).

**Changes required**:

1. **REVERSE the image prohibition (lines 14-28)**:
   - Remove the entire "Critical Constraint: Text-Only Output" section
   - Replace with a new "Visual-First Output" section that:
     - REQUIRES visual asset references when a visual pack exists
     - Specifies per-platform image embedding rules
     - Falls back to text-only (inline data) when no visual pack exists

2. **New "Visual-First Output" section**:
```markdown
## Visual-First Output

When a visual pack exists at `content/visuals/distilled/{slug}-{mode}/manifest.md`:

**REQUIRED in outputs — embed visual references per platform rules:**
- Medium: Hero image at top + 2-3 inline images at section breaks
- Substack Note: 1 hero image before the text excerpt
- LinkedIn Article: 2-3 inline exhibit images within the article body

**When NO visual pack exists** (backward-compatible fallback):
- Express all data as inline text (numbers, percentages, before/after, named benchmarks)
- This matches the previous text-only behavior
```

3. **Update Medium output** (Output 1):
   - Add hero image reference: `![Hero](content/visuals/distilled/{slug}-{mode}/medium-hero.png)`
   - Add 2-3 inline image references at section breaks
   - Preserve Import tool canonical instruction
   - Word count stays 700-900 words (images supplement, not replace text)

4. **Update Substack output** (Output 2):
   - Add hero image reference before text
   - Keep word count 300-500 words
   - Max 3 images (hero + 0-2 inline)

5. **Update LinkedIn Article output** (Output 3):
   - Add 2-3 inline exhibit images within article body
   - Preserve UNIQUE ANGLE requirement (>30% new material)
   - Word count stays 700-900 words
   - Hero image for Google search snippet visibility

6. **Update validation step** (lines 143-155):
   - Remove the prohibited-string scan for image references
   - Add a NEW validation: verify all referenced image paths exist in the visual pack manifest
   - Add fallback validation: when no visual pack exists, verify text-only data expression (original behavior)

Files:
* `.github/agents/platform-distiller.agent.md` - Existing agent (modify)

Discrepancy references:
* Addresses DD-01: skill invocation within agent
* Core requirement: reversing the image prohibition is the foundational change enabling visual-first distillation

Success criteria:
* Image prohibition section (lines 14-28) completely replaced with visual-first section
* Medium output includes hero + inline images when visual pack exists
* Substack output includes hero image when visual pack exists
* LinkedIn Article output includes 2-3 inline exhibits when visual pack exists
* Validation step updated to verify image references instead of prohibiting them
* Backward compatibility: text-only output when no visual pack exists
* All 3 outputs still wrapped in START/END COPY markers

Context references:
* .copilot-tracking/research/subagents/2026-05-13/codebase-architecture-for-distillation.md (Lines 92-177) - Current platform-distiller structure with prohibition text
* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 166-174) - Platform constraints matrix

Dependencies:
* Phase 1 completion (visual-pack-generator skill exists)

## Implementation Phase 3: Update Pipeline Configuration

<!-- parallelizable: false -->

### Step 3.1: Add `distillation_persona_mode` field to `content/pipeline-config.md`

Add the persona mode selection field to the Output Preferences section of pipeline-config.md.

**New field** (add to Output Preferences section, after social platform selection):

```markdown
### Visual Distillation

| Field | Value |
|-------|-------|
| **Persona mode** | `ask` |
| **Options** | `practitioner` (Tech Lead / Senior Practitioner — carousel grammar), `executive` (Engineering Manager / Decision-Maker — exhibit grammar), `ask` (prompt during run) |
| **Visual pack output** | `content/visuals/distilled/{slug}-{mode}/` |
```

**Default value**: `ask` — prompts the user to select persona mode at the start of each distillation run. This allows running both modes sequentially for the same content.

Files:
* `content/pipeline-config.md` - Existing config (modify)

Success criteria:
* `distillation_persona_mode` field exists in Output Preferences section
* Three valid values documented: practitioner, executive, ask
* Default is `ask`
* Visual pack output path convention documented

Context references:
* .copilot-tracking/research/subagents/2026-05-13/codebase-architecture-for-distillation.md (Lines 376-384) - Current pipeline-config structure
* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Line 25) - persona mode field spec

Dependencies:
* None (can be done independently but placed in Phase 3 for logical grouping)

### Step 3.2: Add visual-pack-generation step to pipeline step sequence

Add a documentation reference for the visual pack generation step in the pipeline step table.

**New step** (insert between Step 4a social-strategist and Step 4b social-linkedin):

| Step | Description | Agent/Skill |
|------|-------------|-------------|
| 4a-visual | Generate visual asset pack for distilled posts | visual-pack-generator skill |

**Note**: This step is invoked by distribution agents on-demand (per DD-01), not as a standalone orchestrated step. The table entry provides visibility into the pipeline sequence.

Files:
* `content/pipeline-config.md` - Existing config (modify)

Success criteria:
* Step 4a-visual appears in pipeline step table
* Description references visual-pack-generator skill
* Note clarifies on-demand invocation pattern

Context references:
* .copilot-tracking/research/subagents/2026-05-13/codebase-architecture-for-distillation.md (Lines 304-333) - Current pipeline step sequence

Dependencies:
* Step 3.1 completion (persona mode field exists)

### Step 3.3: Update publish sequence cadence

Update the publish sequence table to include visual asset upload alongside text distribution.

**Updated sequence**:

| Day | Action | Platform | Notes |
|-----|--------|----------|-------|
| Day 0 | Blog already live | GitHub Pages | Canonical source |
| Day 0 | Import to Medium (with images) | Medium | Import tool preserves canonical; hero + inline images included |
| Day 0 | LinkedIn carousel post | LinkedIn | Upload carousel PDF/slides as document post; canonical URL in first comment within 60 sec |
| Day 0 | X/Twitter image thread | X/Twitter | Image cards attached per tweet; canonical URL in last tweet only |
| Day 3-4 | Substack Note (with hero image) | Substack | Post as Note; hero image + excerpt |
| Day 7+ | LinkedIn Article (with exhibits) | LinkedIn | Unique angle; 2-3 inline exhibits; Google-indexed |

Files:
* `content/pipeline-config.md` - Existing config (modify)

Success criteria:
* Publish sequence reflects visual asset uploads
* Each platform entry specifies visual handling
* Canonical URL discipline preserved in updated sequence

Dependencies:
* Step 3.2 completion

## Implementation Phase 4: Demo — Regenerate Part 1 Visual Packs

<!-- parallelizable: false -->

### Step 4.1: Generate Practitioner-mode visual pack for Part 1

Using the visual-pack-generator skill, generate the full Practitioner-mode visual pack for `content/ai-code-assistant-cost-part-1.md`.

**Input data extraction from Part 1**:
- Hook data: "$3K/day → $970/day = 68% savings = $740K/yr annualized"
- Model multiplier spectrum: 0.25x–30x = 120x spread
- Task taxonomy: simple/moderate/complex
- Routing frameworks: RouteLLM (95% GPT-4 quality at 75% lower cost), CascadeFlow (69% savings + 96% quality)
- Existing PNGs to reference: model-multiplier-spectrum.png, task-routing-decision-tree.png, routing-savings-bar.png

**Expected output** (Practitioner mode — 10 carousel slides + supporting assets):
1. `slide-01-hook.png` — "Your AI bill is 120x what it needs to be" + giant "$3K/day" number (1080×1080)
2. `slide-02-promise.png` — "In the next 9 slides: the 3-step framework to cut 68%" (1080×1080)
3. `slide-03-problem.png` — Model multiplier spectrum visualization, recomposed from existing PNG (1080×1080)
4. `slide-04-framework.png` — Task taxonomy three-tier diagram (simple/moderate/complex) (1080×1080)
5. `slide-05-step1.png` — "Step 1: Task Classification" with data (1080×1080)
6. `slide-06-step2.png` — "Step 2: Model Routing" with RouteLLM data (1080×1080)
7. `slide-07-step3.png` — "Step 3: Cost Governance" with CascadeFlow data (1080×1080)
8. `slide-08-interrupt.png` — Dark BG pull-quote: "That $2K/day waste? It's someone's engineering salary." (1080×1080)
9. `slide-09-recap.png` — Summary checklist: ✓ Task classify ✓ Model route ✓ Govern spend (1080×1080)
10. `slide-10-cta.png` — "Save this → Read the full 3-part guide → Link in comments" (1080×1080)
11. `x-card-01.png` through `x-card-04.png` — Key slides adapted to 1600×900 landscape
12. `medium-hero.png` — Hook visual adapted to 1400×800
13. `medium-inline-01.png`, `medium-inline-02.png` — Framework + savings visuals for Medium inline
14. `substack-hero.png` — Hook visual adapted to 1200×630
15. `linkedin-article-exhibit-01.png`, `linkedin-article-exhibit-02.png` — Framework visuals for LinkedIn Article
16. `manifest.md` — Asset inventory
17. `render_distilled.py` — Python renderer script

Files:
* `content/visuals/distilled/part1-practitioner/` - New directory with all assets (create)

Success criteria:
* 10 carousel slides at 1080×1080px, 320 DPI
* 4 X image cards at 1600×900px
* Hero + inline images for Medium and Substack at specified dimensions
* 2 LinkedIn Article exhibits
* manifest.md listing all assets with platform targets
* render_distilled.py generates all assets reproducibly

Dependencies:
* Phase 1 completion (skill definition exists as reference)
* Phase 3 completion (pipeline-config has persona mode field)

### Step 4.2: Generate Executive-mode visual pack for Part 1

Generate the Executive-mode visual pack using the same Part 1 blog content but with exhibit grammar.

**Expected output** (Executive mode — 3 exhibits + supporting assets):
1. `exhibit-01-cost-deviation.png` — "AI coding costs vary 120x across model tiers" — deviation chart showing multiplier spread (1200×627)
2. `exhibit-02-routing-flow.png` — "Intelligent routing preserves 95% quality at 75% lower cost" — flow diagram (1200×627)
3. `exhibit-03-roi-magnitude.png` — "$740K annual savings from model routing discipline" — magnitude comparison (1200×627)
4. `x-exhibit-01.png`, `x-exhibit-02.png` — Key exhibits adapted to 1600×900
5. `medium-hero.png` — Lead exhibit adapted to 1400×800
6. `medium-inline-01.png` — Supporting exhibit for Medium inline
7. `substack-hero.png` — Lead exhibit adapted to 1200×630
8. `manifest.md` — Asset inventory
9. `render_distilled.py` — Python renderer script

**Executive exhibit conventions**:
- Conclusion-as-title (not descriptive title)
- Source attribution line on each exhibit
- 2-3 color max: navy (#051C2C) + one accent + gray
- No carousel — these are standalone exhibits

Files:
* `content/visuals/distilled/part1-executive/` - New directory with all assets (create)

Success criteria:
* 3 exhibits at 1200×627px, 320 DPI
* Conclusion-as-title convention applied
* Source attribution on each exhibit
* 2-3 color palette enforced
* manifest.md listing all assets
* render_distilled.py generates all assets reproducibly

Dependencies:
* Step 4.1 (validates the generation approach before applying to second mode)

### Step 4.3: Regenerate Part 1 distilled posts using both visual packs (10 artifacts)

Run the updated agents to produce 10 distilled posts (5 outputs × 2 modes) for Part 1.

**Artifact matrix**:

| # | Output | Mode | Agent | Key Visual Assets |
|---|--------|------|-------|-------------------|
| 1 | LinkedIn Post + Carousel | Practitioner | social-linkedin | 10 carousel slides |
| 2 | LinkedIn Post + Exhibits | Executive | social-linkedin | 3 exhibit images |
| 3 | X Thread + Image Cards | Practitioner | social-twitter | 4 image cards |
| 4 | X Thread + Exhibit Images | Executive | social-twitter | 2 exhibit images |
| 5 | Medium (import-ready) | Practitioner | platform-distiller | Hero + 2 inline images |
| 6 | Medium (import-ready) | Executive | platform-distiller | Hero + 1 inline exhibit |
| 7 | Substack Note | Practitioner | platform-distiller | 1 hero image |
| 8 | Substack Note | Executive | platform-distiller | 1 hero image |
| 9 | LinkedIn Article | Practitioner | platform-distiller | 2 inline framework visuals |
| 10 | LinkedIn Article | Executive | platform-distiller | 2 inline exhibit visuals |

**Output file naming**: `content/{platform}-post-part1-{mode}.md` (e.g., `content/linkedin-post-part1-practitioner.md`)

**Acceptance test**: Each artifact can be directly copy-pasted (text) or uploaded (images/PDF) to its target platform with zero manual editing.

Files:
* `content/linkedin-post-part1-practitioner.md` - New (create)
* `content/linkedin-post-part1-executive.md` - New (create)
* `content/x-twitter-thread-part1-practitioner.md` - New (create)
* `content/x-twitter-thread-part1-executive.md` - New (create)
* `content/medium-post-part1-practitioner.md` - New (create)
* `content/medium-post-part1-executive.md` - New (create)
* `content/substack-post-part1-practitioner.md` - New (create)
* `content/substack-post-part1-executive.md` - New (create)
* `content/linkedin-article-part1-practitioner.md` - New (create)
* `content/linkedin-article-part1-executive.md` - New (create)

Success criteria:
* 10 distilled posts generated
* Each references correct visual assets from the visual pack
* All wrapped in platform-specific START/END COPY markers
* LinkedIn posts ≤ 200 words (not 600+ like current text-only)
* X tweets ≤ 280 characters each
* Medium 700-900 words with Import tool instructions
* Substack 300-500 words as Note
* LinkedIn Article 700-900 words with unique angle

Dependencies:
* Steps 4.1 and 4.2 (visual packs exist)
* Phase 2 (agents updated to consume visual packs)

### Step 4.4: Run visual-reviewer on all generated assets

Submit all generated visual assets to the visual-reviewer agent for QA.

**Review scope**:
- All PNGs in `content/visuals/distilled/part1-practitioner/`
- All PNGs in `content/visuals/distilled/part1-executive/`

**Expected review criteria** (6 categories from visual-reviewer):
1. Text Rendering: overflow, readability, fitting within slide bounds
2. Layout and Spacing: element clipping, alignment, whitespace
3. Data Accuracy: numbers match source blog, percentages correct
4. Design Token Compliance: color palette, font, DPI, theme diversity
5. Reader Comprehension: standalone clarity, visual hierarchy
6. Professional Polish: consistent spacing, edge cases

**Acceptance**: PASS verdict with no critical findings. Important/minor findings documented but non-blocking.

Files:
* Visual assets in `content/visuals/distilled/` - Existing assets (review, no modify)

Success criteria:
* visual-reviewer runs on both persona mode directories
* No critical findings
* Important findings documented and addressed if feasible
* PASS verdict achieved

Dependencies:
* Steps 4.1 and 4.2 (visual assets exist to review)

## Implementation Phase 5: Validation

<!-- parallelizable: false -->

### Step 5.1: Verify all new/modified files

Validate structural integrity of all created and modified files:

* `.github/skills/visual-pack-generator/SKILL.md` — correct frontmatter, procedure steps, output spec
* `.github/skills/visual-pack-generator/references/slide-grammar.md` — both persona grammars complete
* `.github/skills/visual-pack-generator/references/platform-specs.md` — all 5 platforms documented
* `.github/skills/visual-pack-generator/references/psychology-stack.md` — 12 frameworks mapped
* `.github/agents/social-linkedin.agent.md` — visual-first path + backward compatibility
* `.github/agents/social-twitter.agent.md` — image-anchored path + backward compatibility
* `.github/agents/platform-distiller.agent.md` — image prohibition reversed, visual-first section added
* `content/pipeline-config.md` — persona mode field, step 4a-visual, updated publish sequence

### Step 5.2: Verify demo artifacts are complete

* 10 distilled posts exist with correct naming
* Each post references visual assets that exist in the visual pack directory
* Visual packs contain all expected assets per manifest
* render_distilled.py scripts are executable and reproduce assets

### Step 5.3: Report blocking issues

When validation failures require changes beyond minor fixes:
* Document the issues and affected files
* Provide the user with next steps
* Recommend additional research and planning rather than inline fixes
* Avoid large-scale refactoring within this phase

## Dependencies

* Python 3.x with matplotlib and Pillow (existing requirements.txt)
* Existing visual-renderer agent (production engine)
* Existing visual-reviewer agent (QA gating)
* Existing design token system (15 tokens)
* Published blog: content/ai-code-assistant-cost-part-1.md

## Success Criteria

* Visual-pack-generator skill produces reproducible visual asset packs in both persona modes
* All 3 distribution agents consume visual packs and produce visual-first distilled posts
* 10 demo artifacts for Part 1 are copy-paste/upload ready
* All visual assets pass visual-reviewer QA
* Pipeline configuration supports persona mode selection
* Backward compatibility preserved — all agents work in text-only mode when no visual pack exists
