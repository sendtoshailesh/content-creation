# Codebase Architecture for Visual-First Distillation System

**Research Date**: 2026-05-13
**Status**: Complete
**Researcher**: Subagent

---

## Research Topics

1. Current agent definitions (social-linkedin, social-twitter, platform-distiller, visual-renderer, visual-reviewer)
2. Existing skills inventory and patterns
3. Pipeline configuration and step sequence
4. Content directory structure and existing distilled posts
5. GitHub instructions inventory
6. Agent naming and structure conventions

---

## 1. Agent Definitions

### 1.1 social-linkedin.agent.md

**File**: `.github/agents/social-linkedin.agent.md`

**Frontmatter**:
```yaml
description: "Use for creating LinkedIn posts from blog content. Produces both plain-text and Unicode-formatted versions optimized for LinkedIn's algorithm and audience."
tools: [read, edit, search]
argument-hint: "Provide the blog file path to adapt for LinkedIn"
```

**Inputs**: Published blog post (Markdown file path), key data points/case study/framework summary

**Procedure** (4 steps):
1. Read blog → identify strongest hook, data points, CTA
2. Write plain-text version → `content/linkedin-post.md`
3. Write Unicode-formatted version → `content/linkedin-post-formatted.md`
4. Verify formatting renders correctly

**Post Structure** (6 sections): Hook → Problem/Context → Key Insight/Framework (3-5 numbered) → Case Study → CTA → Hashtags

**Output files**:
- `content/linkedin-post.md` (plain text)
- `content/linkedin-post-formatted.md` (Unicode formatted)

**Key constraints**:
- ≤ ~3000 characters
- No Markdown formatting
- No self-promotional "I wrote a blog" framing
- Unicode bold (𝗕𝗼𝗹𝗱) and italic (𝘐𝘵𝘢𝘭𝘪𝘤) for formatted version
- ━━━ separators, ▸ sub-bullets, emoji anchors

**Notable**: No visual/image handling whatsoever. Purely text-only output.

---

### 1.2 social-twitter.agent.md

**File**: `.github/agents/social-twitter.agent.md`

**Frontmatter**:
```yaml
description: "Use for creating X/Twitter threads from blog content. Produces a numbered tweet thread with Unicode formatting plus a standalone single-tweet summary."
tools: [read, edit, search]
argument-hint: "Provide the blog file path to adapt for X/Twitter"
```

**Inputs**: Published blog post (Markdown file path), key data points/framework/case study

**Procedure** (5 steps):
1. Read blog → identify hook, framework steps, data points, CTA
2. Write standalone summary tweet (≤ 280 chars)
3. Write 10-12 tweet thread with Unicode formatting
4. Add posting notes (timing, image attachment, cadence)
5. Verify every tweet ≤ 280 characters

**Thread Structure** (12 tweets): Hook → Problem → Framework overview → Key tiers/data → Hidden costs → Case study → Latency angle → CTA → Engagement close

**Output file**: `content/x-twitter-thread.md`

**Key constraints**:
- Each tweet ≤ 280 characters (hard)
- URLs count as 23 chars (t.co wrapping)
- Unicode chars count as 1 character
- No Markdown, no self-promotional framing

**Notable**: Step 4 mentions "image attachment" in posting notes, but no image generation. Purely text-only output.

---

### 1.3 platform-distiller.agent.md — THE KEY AGENT FOR DISTILLATION

**File**: `.github/agents/platform-distiller.agent.md`

**Frontmatter**:
```yaml
description: "Generates text-only Medium excerpt, Substack excerpt, and LinkedIn Article summaries from a completed blog post. All outputs point to the GitHub Pages canonical URL and contain no images or media. Use after web-publisher (Step 10) and social-publisher (Step 11). This is Step 12."
tools: [read, edit, create]
argument-hint: "Provide the blog file path (e.g. content/blog-part1.md). Canonical URL is read automatically from content/publishing-log.md."
```

**Pipeline position**: Step 12 (final step, after web-publisher and social-publisher)

**Inputs**:
1. Blog file path
2. Canonical URL — auto-read from `content/publishing-log.md` by matching blog's `seo.slug` frontmatter

#### ⚠️ CRITICAL: IMAGE PROHIBITION (Lines 14-28)

Full prohibition text:

```
## Critical Constraint: Text-Only Output

**PROHIBITED in ALL outputs — zero exceptions:**
- Image markdown: `![`
- HTML image tags: `<img`
- Visual asset paths: `content/visuals/`, `.png`, `.svg`, `.jpg`, `.jpeg`, `.gif`, `.webp`
- Mermaid diagram blocks (` ```mermaid `)
- Any sentence like "as shown in the diagram above" or "see the chart below"

**Express all data as inline text instead:**
- Numbers and percentages: "reduced latency by 43%"
- Before/after: "Before: 8.2s cold start → After: 1.1s"
- Ratios: "3x throughput improvement at the same cost"
- Named benchmarks: "gpt-4o at $2.50/MTok vs claude-3-5-sonnet at $3.00/MTok"
- Named models, tools, APIs, and frameworks — always spell them out
```

This prohibition is the TARGET FOR REVERSAL in the visual-first distillation system.

#### Three Outputs

**Output 1: Medium Excerpt** (`content/medium-post-{slug}.md`)
- Word count: 700–900 words
- Purpose: Drive traffic to GitHub Pages with SEO-safe canonical via Medium Import tool
- Structure: Hook (2-3 sentences) → Core argument (3-4 paragraphs) → Key takeaways (3-5 bullets) → CTA
- Format: Standard Markdown (`**bold**`, `*italic*`, `##`, `-`, ` ```code``` `)
- No images. Code snippets acceptable if from blog.
- Wrapped in `── START COPY (Medium) ──` / `── END COPY (Medium) ──`
- Publishing note: Import via Medium Import tool (not paste) to preserve canonical URL

**Output 2: Substack Excerpt** (`content/substack-post-{slug}.md`)
- Word count: 300–500 words
- Purpose: Short hook for Substack Notes ambient feed (NOT emailed to subscribers)
- Structure: Hook (1 paragraph) → Key insights (3-5 bullets) → One concrete example → CTA
- Format: Standard Markdown only, no headers beyond title
- Wrapped in `── START COPY (Substack) ──` / `── END COPY (Substack) ──`
- Publishing note: Post as Substack NOTE (not newsletter)

**Output 3: LinkedIn Article** (`content/linkedin-article-{slug}.md`)
- Word count: 700–900 words
- Purpose: Native thought leadership on LinkedIn — indexed by Google, must be UNIQUE ANGLE
- CRITICAL: NOT a blog recap. Pick one unique angle:
  - "What I learned working with customers on [topic]"
  - "The [N] mistakes most teams make when [doing X]"
  - "Why [X] matters more than people think in [year]"
  - "The hidden cost of [common practice]"
  - "Unpopular opinion: [take on topic]"
- Structure: Hook → Context → Core insight (unique angle) → Practical implications → Link reference
- Format: Standard Markdown, no images
- Canonical URL in final paragraph only
- Wrapped in `── START COPY (LinkedIn Article) ──` / `── END COPY (LinkedIn Article) ──`

#### Validation Step (Lines 143-155)

Before writing any output, scans for prohibited strings:
```
Prohibited: ![  <img  .png  .svg  .jpg  .jpeg  content/visuals/  ```mermaid
```
If found → rewrite as inline text → rescan until clean.

#### Output Summary Table

Prints a summary table after saving with file path, word count, canonical URL, and text-only validation status.

---

### 1.4 visual-renderer.agent.md

**File**: `.github/agents/visual-renderer.agent.md`

**Frontmatter**:
```yaml
description: "Use for generating visual assets — PNG charts via matplotlib, SVG graphics, and Mermaid diagrams. Follows the shared design token system for consistent visuals across all content."
tools: [read, edit, search, execute]
argument-hint: "Describe visuals needed or provide the blog outline with visual markers"
```

**Inputs**: Blog outline with `[VISUAL: description]` markers OR specific visual request

**Capabilities**:
- PNGs via matplotlib (data charts, bar, line, scatter, pie)
- Infographic layouts via Pillow (PIL) (multi-panel, cards, dashboards)
- Flow diagrams via matplotlib patches + annotations (< 10 nodes)
- Comparison tables/matrices via Pillow (PIL)
- Architecture diagrams via Mermaid (.mmd)

**Design Token System**: Multi-theme palette (5 themes: default, ocean, sunset, forest, midnight). Base tokens stay constant; accent colors rotate round-robin per visual.

**Key rules**:
- No Unicode glyphs in matplotlib
- SVGs via Python only (never heredoc)
- 320 DPI mandatory for all PNGs
- Theme diversity: each visual in a post uses a different theme
- Each visual = one function in renderer script accepting `tokens` dict
- Narrow segment rule: < 15% width/height → external labels with leader lines
- Pillow for pixel-precise text placement (textbbox() for measurement before rendering)

**Output structure**:
```
content/visuals/
├── render_<topic>.py   # PNG renderer
├── write_svgs.py       # SVG generator
├── *.png               # Generated PNGs
├── *.svg               # Generated SVGs
└── *.mmd               # Mermaid diagrams
```

**Information design principles**: Data-ink ratio (Tufte), visual hierarchy, color semantics, annotation-first, Gestalt grouping, standalone clarity.

---

### 1.5 visual-reviewer.agent.md

**File**: `.github/agents/visual-reviewer.agent.md`

**Frontmatter**:
```yaml
description: "Visual QA critic agent. Reviews rendered visual assets (PNG, SVG, Mermaid) for layout defects, readability, design token compliance, and reader comprehension. Produces a findings report for visual-renderer to fix. Must run on a different LLM family than the model that generated the visuals (cross-model review)."
tools: [read, edit, search, execute, viewImage]
argument-hint: "Provide path to visuals directory or specific PNG/SVG files to review"
```

**Cross-model requirement**: Must use a different LLM family than the visual generator (Anthropic↔OpenAI↔Google).

**Review checklist** (6 categories):
1. Text Rendering (Critical): overflow, overlap, readability, fitting, line wrapping
2. Layout and Spacing (Critical): element clipping, margin sufficiency, whitespace balance, alignment, proportion
3. Data Accuracy (Critical): numbers match source, percentages sum, labels match content
4. Design Token Compliance (Important): color palette, font consistency, background, DPI, theme diversity
5. Reader Comprehension (Important): standalone clarity, visual hierarchy, color semantics, annotation quality, chart type fitness
6. Professional Polish (Nice-to-have): consistent spacing, edge cases, arrow/line quality, legend positioning

**Output**: Structured findings report with file, severity (critical/important/minor), category, finding, suggestion. Summary with pass/fail verdict.

**Handoff**: PASS → visuals ready. FAIL → findings sent to visual-renderer for fixes, then re-review cycle (max 3 cycles).

---

## 2. Existing Skills

### 2.1 Skills Inventory

**Directory**: `.github/skills/`

| Skill Directory | SKILL.md | Description |
|----------------|----------|-------------|
| `content-scope-assessment/` | Yes | Assess topic scope, recommend single vs multi-part series. 8 scoring signals (0-16 scale). |
| `feed-curation/` | Yes | Read blog rolls/feeds, classify articles, extract insights, rank for idea queue. |
| `multi-dimensional-analysis/` | Yes | Analyze topic across persona, best practice, and WAF pillar dimensions. |
| `reference-analysis/` | Yes | Fetch and synthesize online reference URLs from pipeline-config.md. |
| `unicode-formatting/` | Yes | Format text with Unicode Mathematical Bold/Italic for LinkedIn and X/Twitter. |
| `visual-rendering/` | Yes + `references/design-tokens.md` | Generate visual assets (PNG, SVG, Mermaid). Has a references subfolder. |
| `visual-review/` | Yes | Review rendered visuals for defects; cross-model critic pattern. |

### 2.2 Skill Naming Convention

- Directory name: `kebab-case` (e.g., `content-scope-assessment`)
- Main file: always `SKILL.md` (uppercase)
- Optional: `references/` subdirectory for supporting files (e.g., `design-tokens.md`)

### 2.3 Skill File Structure (Frontmatter)

```yaml
---
name: kebab-case-skill-name
description: 'Single sentence describing when to use this skill.'
argument-hint: 'Description of expected input'
---
```

Then Markdown body with:
- `# Skill Title` (H1)
- `## When to Use` — bullet list of triggers
- `## Procedure` — numbered steps
- `## Output Format` or `## Output` — what the skill produces
- `## Critical Rules` or `## Constraints` — hard requirements

### 2.4 How Skills Are Invoked by Agents

Skills are invoked implicitly by agents through their procedure steps. The content-pipeline orchestrator references skills by name in phase descriptions:
- "Use the `content-scope-assessment` skill to evaluate..."
- "Use the `multi-dimensional-analysis` skill to analyze..."
- "use the `reference-analysis` skill to fetch..."

The visual-renderer agent references the design token system from the `visual-rendering` skill's references folder. The visual-reviewer agent applies the review checklist from the `visual-review` skill.

---

## 3. Pipeline Configuration

### 3.1 Full Pipeline Step Sequence

**File**: `content/pipeline-config.md`

| Step | Description | Agent/Skill |
|------|-------------|-------------|
| -1 | Content discovery from feeds (optional) | feed-curator |
| 0a | Reference URL discovery | reference-discovery |
| 0b | Market intelligence + data points | trend-researcher |
| 1-2 | Strategy doc + outline | content-strategist |
| 2b | Scope assessment (single vs series) | content-scope-assessment skill |
| 2c | Multi-dimensional analysis | multi-dimensional-analysis skill |
| 3 | Blog post (or Part N) | blog-writer |
| 3b | Visual assets (PNGs, SVGs, Mermaid) | visual-renderer |
| 3c | Quality review (cross-model) | quality-reviewer |
| 3e | Grounded content review (live source check) | grounded-content-reviewer |
| 3d | SEO optimization | seo-optimizer |
| 4a | Cross-platform distribution plan | social-strategist |
| 4b | LinkedIn post (always generated) | social-linkedin |
| 4c | Platform selection (user choice) | (user prompt) |
| 5 | X/Twitter thread (if selected) | social-twitter |
| 6 | Reddit post (if selected) | social-reddit |
| 6b | Reel/Short video (if selected) | reel-video |
| 7 | Brand consistency audit | brand-guardian |
| 8 | YouTube script (if selected) | video-scriptwriter |
| 9 | Repurposing (optional) | content-repurposer |
| 10 | Publish to GitHub Pages | web-publisher |
| 10a | Inject canonical URLs into social posts | (manual/orchestrator) |
| 11 | Social media publishing (with approval) | social-publisher |
| 12 | Platform distillation (Medium, Substack, LinkedIn Article) | platform-distiller |

### 3.2 Where Steps 4, 5, and 12 Fit

- **Step 4b (social-linkedin)**: Phase 4 Distribution. Always generated. Primary distribution channel. Produces `linkedin-post.md` + `linkedin-post-formatted.md`.
- **Step 5 (social-twitter)**: Phase 4 Distribution. Conditionally generated if user selects X/Twitter. Produces `x-twitter-thread.md`.
- **Step 12 (platform-distiller)**: Final step of the entire pipeline. Runs AFTER web-publisher (Step 10) and social-publisher (Step 11). Produces Medium, Substack, LinkedIn Article text-only summaries.

**Key observation**: Step 12 has NO visual integration point. All visuals are generated at Step 3b and consumed by the blog at Step 3. The distilled outputs at Step 12 strip all visuals.

### 3.3 Persona Analysis Section (Lines ~177-185)

```markdown
### Dimension Analysis

| Field | Value |
|-------|-------|
| **Persona count** | 4 |
| **Personas** | Senior Developer, Tech Lead, Engineering Manager, Platform Engineer |
| **Technology practices** | 6 (model routing, prompt caching, context management, context cleanup, token compression, programmatic tool calling) |
| **Governance practices** | 5 (budget alerting, usage monitoring, team model guidelines, credit forecasting, cost center allocation) |
| **Total practices** | 11 |
| **Primary WAF pillars** | Cost Optimization |
| **Secondary WAF pillars** | Operational Excellence, Performance Efficiency |
| **Dimension breadth score** | 2/2 |
```

### 3.4 Publish Sequence/Cadence (Lines ~291-301)

```markdown
### Publish Sequence

| Day | Action | Platform | Notes |
|-----|--------|----------|-------|
| Day 0 | Blog already live | GitHub Pages | Canonical source; publishing-log.md populated |
| Day 0 | Import to Medium | Medium | Use Import tool — do NOT paste; preserves canonical attribution |
| Day 0 | LinkedIn post | LinkedIn | Canonical URL at end of post or first comment; never mid-body |
| Day 1 | X/Twitter thread | X/Twitter | Link in last tweet only; text-only thread (no images) |
| Day 3–4 | Substack excerpt | Substack | Post as Substack Note (not newsletter); excerpt only |
| Day 5–7 | Reddit text post | Reddit | Substantive 500–800 word text post; link at bottom only |
| Day 7+ | LinkedIn Article | LinkedIn | Unique angle ONLY — not a republish |
```

### 3.5 Configuration Fields Structure

Major sections in `pipeline-config.md`:
1. **Pipeline Status**: status, topic, started date, current step, series flag, step checklist
2. **Model Selection**: family detection, cross-model critic review, current run tracking
3. **Online References**: categorized reference URLs with notes
4. **Output Preferences**: blog target length, series configuration, dimension analysis, social platform selection, long-form platform distribution, canonical URL configuration, social posts format, target subreddits, YouTube/Reel settings
5. **Publishing Configuration**: publish mode (manual/confirm/auto), approach (per-platform/posteverywhere/postfast), published URLs tables, publish sequence

---

## 4. Content Directory Structure

### 4.1 Files in `content/` (excluding visuals/)

| File | Type | Description |
|------|------|-------------|
| `ai-code-assistant-cost-strategy.md` | Strategy | Original cost-first strategy doc |
| `ai-code-assistant-optimization-strategy.md` | Strategy | Revised optimization strategy doc |
| `ai-code-assistant-cost-part-1.md` | Blog | Blog Part 1 (context engineering) |
| `ai-code-assistant-cost-part-2.md` | Blog | Blog Part 2 (caching/workflow) |
| `ai-code-assistant-cost-part-3.md` | Blog | Blog Part 3 (model selection) |
| `context-engineering-part-1.md` | Blog | Context engineering blog Part 1 |
| `linkedin-post.md` | Social | LinkedIn post (optimization series) |
| `linkedin-post-part1.md` | Social | LinkedIn post Part 1 |
| `linkedin-post-part2.md` | Social | LinkedIn post Part 2 |
| `linkedin-post-part3.md` | Social | LinkedIn post Part 3 |
| `x-twitter-thread.md` | Social | X/Twitter thread (Part 1) |
| `medium-post-part1.md` | Distilled | Medium excerpt Part 1 |
| `medium-post-part2.md` | Distilled | Medium excerpt Part 2 |
| `medium-post-part3.md` | Distilled | Medium excerpt Part 3 |
| `substack-post-part1.md` | Distilled | Substack excerpt Part 1 |
| `substack-post-part2.md` | Distilled | Substack excerpt Part 2 |
| `substack-post-part3.md` | Distilled | Substack excerpt Part 3 |
| `linkedin-article-part1.md` | Distilled | LinkedIn Article Part 1 |
| `linkedin-article-part2.md` | Distilled | LinkedIn Article Part 2 |
| `linkedin-article-part3.md` | Distilled | LinkedIn Article Part 3 |
| `reel-script.md` | Video | Reel script (original) |
| `reel-script-part1.md` | Video | Reel script Part 1 |
| `reel-script-part2.md` | Video | Reel script Part 2 |
| `reel-script-part3.md` | Video | Reel script Part 3 |
| `youtube-script.md` | Video | YouTube script |
| `reference-brief.md` | Reference | Synthesized reference analysis |
| `pipeline-config.md` | Config | Pipeline configuration |
| `publishing-log.md` | Log | Published URL tracking |
| `feed-sources.md` | Config | Blog roll/feed source configuration |
| `idea-queue.md` | Config | Content idea queue |

### 4.2 Files in `content/visuals/`

**PNG visuals (13 files)**:
- `before-after-context.png` — Context engineering before/after
- `caching-comparison.png` — Caching strategies comparison
- `caching-flow.png` — Caching flow diagram
- `context-engineering-framework.png` — Framework overview
- `context-noise-breakdown.png` — Context noise analysis
- `context-quality-paradox.png` — Quality paradox visual
- `model-multiplier-spectrum.png` — Model multiplier spectrum
- `prompt-structure-breakdown.png` — Prompt structure analysis
- `retry-loop-anatomy.png` — Retry loop anatomy
- `retry-tax-calculator.png` — Retry tax calculator
- `routing-decision-comparison.png` — Routing decision comparison
- `routing-savings-bar.png` — Routing savings bar chart
- `task-model-alignment.png` — Task-model alignment
- `task-routing-decision-tree.png` — Task routing decision tree
- `team-governance-dashboard.png` — Team governance dashboard
- `team-optimization-strategies.png` — Team optimization strategies
- `three-layer-stack.png` — Three-layer stack

**Python renderers (5 files)**:
- `render_part1.py` — Part 1 PNG renderer
- `render_part2.py` — Part 2 PNG renderer
- `render_part3.py` — Part 3 PNG renderer
- `render_context_engineering.py` — Context engineering renderer
- `render_noise_breakdown.py` — Noise breakdown renderer

**Other**: `__pycache__/` directory

### 4.3 Existing Distilled Posts for AI Code Assistant Cost Series

All 9 distilled posts exist for the 3-part series:

| Platform | Part 1 | Part 2 | Part 3 |
|----------|--------|--------|--------|
| Medium | `medium-post-part1.md` | `medium-post-part2.md` | `medium-post-part3.md` |
| Substack | `substack-post-part1.md` | `substack-post-part2.md` | `substack-post-part3.md` |
| LinkedIn Article | `linkedin-article-part1.md` | `linkedin-article-part2.md` | `linkedin-article-part3.md` |

Social posts also exist per-part:
- `linkedin-post-part1.md`, `linkedin-post-part2.md`, `linkedin-post-part3.md`
- `x-twitter-thread.md` (single file, Part 1 only based on content header)

**Naming convention for distilled posts**: `{platform}-post-part{N}.md` or `{platform}-article-part{N}.md`

---

## 5. GitHub Instructions

### 5.1 Instruction Files Inventory

**Directory**: `.github/instructions/`

| File | Description | applyTo |
|------|-------------|---------|
| `social-formatting.instructions.md` | Platform-specific formatting rules, Unicode chars | (none — manual) |
| `content-quality.instructions.md` | Data specificity, volatile data caveats, structure, tone, visual density | `content/**/*.md` |
| `visual-standards.instructions.md` | Design tokens, rendering rules, narrow segment rule, tool selection, Pillow usage, information design principles | `content/visuals/**` |

### 5.2 Instruction Naming Convention

Pattern: `{concern}.instructions.md` (kebab-case)

### 5.3 social-formatting.instructions.md

Covers:
- LinkedIn & X/Twitter: Unicode Bold (𝗕𝗼𝗹𝗱), Unicode Italic (𝘐𝘵𝘢𝘭𝘪𝘤), ━━━ separators, ▸ sub-bullets, emoji anchors, START/END COPY markers
- X/Twitter: ≤ 280 chars per tweet, Unicode = 1 char, numbered thread format, standalone summary
- Reddit: Standard Markdown ONLY, no Unicode bold/italic, TL;DR at top, anti-promotional tone

### 5.4 content-quality.instructions.md

Key sections:
- **Data Specificity**: concrete numbers, real pricing, before/after metrics, specific model names
- **Volatile Data and Caveats**: check for "subject to change", include date caveats, never present volatile data as permanent, [VOLATILE] tag handling, "what if this changes" paragraph
- **Structure Requirements**: blog (hook, framework, tier breakdown, case study, playbook, checklist), social (story hook, not "I wrote a blog")
- **Tone**: first-person "sharing my learnings", conversational, data-driven, never corporate
- **Visual Density (Mandatory Pass)**: 
  - Word count is flexible (may exceed by 25-40%)
  - Every section >400 words without a visual must get one
  - Visuals explain same concept differently (alternative explanation path)
  - Visual type mapping by section pattern
  - Audit method: scan H2/H3 sections, add `[VISUAL: description]` markers

### 5.5 visual-standards.instructions.md

Covers:
- Full design token system (BASE_TOKENS + 5 THEMES)
- Theme usage with round-robin `get_tokens()` function
- Rendering rules (320 DPI, Helvetica Neue, no Unicode glyphs, SVGs via Python)
- Narrow segment rule (< 15% → external labels)
- Tool selection table (matplotlib vs Pillow vs Mermaid)
- Pillow (PIL) usage with textbbox() for measurement
- Information design principles (6 principles)
- Visual review requirement (cross-model critic)

---

## 6. Agent Naming and Structure Conventions

### 6.1 File Naming Pattern

Pattern: `{function}.agent.md` (kebab-case)

Examples from inventory:
- `social-linkedin.agent.md`
- `social-twitter.agent.md`
- `social-reddit.agent.md`
- `platform-distiller.agent.md`
- `visual-renderer.agent.md`
- `visual-reviewer.agent.md`
- `content-pipeline.agent.md`
- `blog-writer.agent.md`
- `quality-reviewer.agent.md`
- `brand-guardian.agent.md`
- `content-strategist.agent.md`
- `web-publisher.agent.md`
- `social-publisher.agent.md`
- `feed-curator.agent.md`

Full list (22 agents):
blog-writer, brand-guardian, content-pipeline, content-repurposer, content-strategist, feed-curator, grounded-content-reviewer, platform-distiller, quality-reviewer, reel-video, reference-discovery, seo-optimizer, social-linkedin, social-publisher, social-reddit, social-strategist, social-twitter, trend-researcher, video-scriptwriter, visual-renderer, visual-reviewer, web-publisher

### 6.2 Frontmatter Structure

All agents use YAML frontmatter with these fields:

```yaml
---
description: "Human-readable description of the agent's purpose and when to use it."
tools: [read, edit, search]          # Available tools (varies by agent)
argument-hint: "What the user should provide when invoking"
---
```

Some agents (like content-pipeline) also include:
```yaml
agents: [list, of, sub-agents, it, coordinates]
```

**Common tool sets observed**:
- Read-only + edit agents: `[read, edit, search]` (social-linkedin, social-twitter)
- Read + create agents: `[read, edit, create]` (platform-distiller)
- Full agents: `[read, edit, search, execute]` (visual-renderer)
- Full + viewImage: `[read, edit, search, execute, viewImage]` (visual-reviewer)
- Orchestrator: `[read, edit, search, execute, agent, todo, web]` (content-pipeline)

### 6.3 How Agents Reference Skills

Agents reference skills indirectly. The content-pipeline orchestrator mentions skills by name in its procedure:
- "Use the `content-scope-assessment` skill to evaluate..."
- "Use the `multi-dimensional-analysis` skill to analyze..."

Individual agents (like visual-renderer) implement the skill logic inline — the visual-renderer agent itself contains the design token system rather than referencing the skill file. The skill files exist as standalone documentation/invocable units.

### 6.4 How Agents Reference pipeline-config.md

- The content-pipeline orchestrator reads `content/pipeline-config.md` as its first action (Status Check) and updates it after each phase.
- Individual agents are told what to do by the orchestrator; they don't typically read pipeline-config directly.
- The platform-distiller reads `content/publishing-log.md` (not pipeline-config) for canonical URLs.
- The reference-analysis skill reads `content/pipeline-config.md` for reference URLs.

### 6.5 How Agents Reference Content Files

- Blog path is passed as an argument (e.g., `content/ai-code-assistant-cost-part-1.md`)
- Output paths are hardcoded in the agent definition (e.g., `content/linkedin-post.md`, `content/x-twitter-thread.md`)
- Series naming: agents append `part{N}` to output filenames (e.g., `content/linkedin-post-part1.md`)
- The platform-distiller uses `{slug}` placeholder in output paths: `content/medium-post-{slug}.md`
- Visual assets are always in `content/visuals/` with renderer scripts following `render_<topic>.py` pattern

---

## 7. Key Architectural Observations for Visual-First Distillation

### 7.1 The Gap

The visual-renderer generates high-quality PNGs (17 visuals exist for the current series) with a sophisticated design token system, theme rotation, and quality review process. However:

1. **Platform-distiller prohibits ALL visuals** (lines 14-28) — the prohibition is explicit and enforced via validation scan
2. **Social agents (LinkedIn, X/Twitter) have zero visual handling** — they produce text-only output
3. **No distilled visual generation** exists — no agent or skill creates platform-optimized visual summaries
4. **No per-platform image spec system** exists — no definition of image dimensions, aspect ratios, or format requirements per platform

### 7.2 Visual Assets That Exist (Potential Sources for Distillation)

The blog posts reference these 17 PNGs. These could serve as source material for distilled visuals, but they are 320 DPI publication-quality images sized for blog posts — not optimized for social media platforms.

### 7.3 Pipeline Integration Points

The logical insertion point for visual distillation would be:
- **Between Step 3b (visual-renderer) and Step 4b (social-linkedin)** — generate platform-optimized visual variants from the blog visuals
- **At Step 12 (platform-distiller)** — reverse the image prohibition and include distilled visuals in Medium, Substack, LinkedIn Article outputs

### 7.4 Existing Patterns to Leverage

- **Design token system**: Already shared across visual-renderer, visual-reviewer, and visual-standards instructions. A new distillation skill could reuse the same token system.
- **Round-robin theme rotation**: Already implemented. Distilled visuals should maintain theme consistency with their source blog visuals.
- **Cross-model review**: visual-reviewer already reviews rendered visuals. Could be extended to review distilled variants.
- **Pillow (PIL)**: Already documented as the tool for pixel-precise layouts, cards, and dashboards — perfect for social media image generation.

---

## Follow-on Questions (Directly Relevant)

1. What image dimensions does each social platform (LinkedIn, X/Twitter, Medium, Substack) require or recommend for in-feed display?
2. Should distilled visuals be newly generated summaries (e.g., single "key insight" card) or cropped/resized versions of existing blog PNGs?
3. Should the platform-distiller agent be modified to support visual mode, or should a new agent (e.g., `visual-distiller.agent.md`) be created?
4. How do the X/Twitter posting notes already mention "image attachment" (social-twitter line 19) — is there an existing image attachment workflow?

---

## Clarifying Questions

1. For the visual-first distillation system, should each distilled post (Medium, Substack, LinkedIn Article) get ONE hero visual or MULTIPLE visuals selected from the blog's visual set?
2. Should LinkedIn posts (Step 4b) also get visual attachments, or is the distillation only for Step 12 platforms?
3. For X/Twitter threads, should a single summary visual be attached to the first tweet, or should multiple tweets get individual visuals?
