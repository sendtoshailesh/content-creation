# Content Pipeline Configuration

> **Edit this file** to configure your content pipeline preferences. All pipeline agents read this config before starting work.

---

## Pipeline Status

> **Auto-updated by the pipeline orchestrator.** Check this to see where content creation stands.

| Field | Value |
|-------|-------|
| **Status** | `in-progress` |
| **Topic** | AI Agent Evals: Why SWE-bench Isn't Enough Before Production |
| **Started** | 2025-07-17 |
| **Current Step** | DONE (LinkedIn carousel + Medium published 2026-06-09). LinkedIn: ugcPost 7470133668175433728. Medium: ai-agent-evals-production-readiness-guide (canonical = GitHub Pages). Visual pack live + QA-clean. Optional remaining: X/Twitter, Substack, LinkedIn Article, Reel, YouTube — not yet posted. |
| **Series** | `yes (2 parts)` |
| **Current Part** | 1 |

### Step Checklist

- [x] Step 0: Reference analysis
- [x] Steps 1-2: Strategy + outline
- [x] Step 2b: Scope assessment (single vs. series)
- [x] Step 2c: Multi-dimensional analysis
- [x] Step 2d: Visual opportunity mapping
- [x] Step 2e: Infographic art direction
- [x] Step 3: Blog post refresh for visual-first strategy
- [x] Step 3b: Visual assets
- [x] Step 3c: Quality review
- [x] Step 3d: SEO optimization
- [x] Step 4a: Social distribution strategy refresh
- [x] Step 4a-visual: Visual-first asset pack
- [x] Step 4: LinkedIn post
- [x] Step 4c: Social platform selection
- [x] Step 5: X/Twitter thread
- [x] Step 6b: Reel/Short video
- [x] Step 7: Brand audit
- [x] Step 7b: Grounded content review
- [x] Step 8: YouTube script
- [x] Step 10: Web publishing refresh
- [ ] Step 11: Social publishing
- [x] Step 12: Platform distillation draft

> **Visual-first reset note (2026-06-08):** The content strategy changed materially from text-led to visual-first. Existing Part 1/Part 2 blog posts, LinkedIn posts, X/Twitter threads, reel scripts, YouTube/platform excerpts, and previously published pages must be considered stale until regenerated from `content/visual-opportunity-map.md` and the new visual asset pack.

**Series values:** `not-applicable` | `pending-assessment` | `yes (N parts)` | `no`

**Status values:** `not-started` | `in-progress` | `completed` | `blocked`

> **What to do:**
> - If Status is `not-started` → You're clear to start a new run. Edit references/preferences below, then run `@content-pipeline` or `/new-content-pipeline`
> - If Status is `in-progress` → Content creation is underway. Run `@content-pipeline` to resume from where it left off
> - If Status is `completed` → All steps done! Review the content, then run `/archive-content` to archive and start fresh
> - If Status is `blocked` → See Current Step for what needs attention
>
> **Rollback / redo rule:** If any agent goes back to rebuild an earlier phase, update this status before editing: set Status to `in-progress`, set Current Step to the earliest step being redone with the date and reason, uncheck that step and all downstream dependent steps, and mark published/social outputs stale until republished. Do not leave this file saying a later step is complete while earlier content is being regenerated.

---

## Model Selection

Choose which model to use for content generation. Select your model in the **VS Code Copilot model picker** before running agents.

### Model Family Detection

The pipeline uses the selected model for content generation and GitHub Copilot's **rubber-duck review** feature for adversarial review gates. No model-family switch is required before reviews.

| Family | Model name prefix |
|--------|------------------|
| `anthropic` | Claude * |
| `openai` | GPT-*, o* |
| `google` | Gemini * |

### Rubber-Duck Review

| Role | Selection Rule |
|------|---------------|
| **Content Creation** | User selects any model; pipeline records the family used |
| **Critic Review** | Use GitHub Copilot **rubber-duck review**; no model switch required |
| **Visual Generation** | User selects any model |

> **How it works**: After content is created, the orchestrator runs rubber-duck review as the adversarial critique gate, then routes findings to the appropriate reviewer/fixer agents.

### Current Run

| Field | Value |
|-------|-------|
| **Creation model family** | `anthropic` |
| **Review method** | `GitHub Copilot rubber-duck` |

### Current Selection

**Preferred model**: _(select any model in the VS Code Copilot picker — agents inherit your selection automatically)_

Review gates use GitHub Copilot rubber-duck review. No specific model versions are required — use whatever is available.

---

## Online References

List URLs below that agents should fetch, analyze, and synthesize during content creation. The pipeline will read these before writing.

### How to Use

1. Add URLs under the appropriate section below
2. Add a brief note on what to extract from each
3. Pipeline agents will fetch and analyze these during Steps 1-3

### Reference URLs

<!-- Add your reference URLs below. Format: - [description](URL) -->

**Agent Evaluation Frameworks & Platforms:**
- https://platform.openai.com/docs/guides/evals — OpenAI Evals: official guide for building custom evals with graders (text, model-graded, tool-constraint patterns)
- https://github.com/openai/evals — OpenAI Evals open-source framework — eval registry, YAML task definitions, community benchmarks
- https://www.anthropic.com/research/building-effective-agents — Anthropic's guide on building effective agents: workflows vs agents, composability, validation gates between steps

**Coding Agent Benchmarks (contrast with agent behavioral evals):**
- https://www.swebench.com/ — SWE-bench leaderboard: SOTA ~88% on Verified, but tests capability not behavior contracts
- https://presenc.ai/research/coding-agent-benchmarks-2026 — Coding Agent Benchmarks 2026: SWE-bench, TerminalBench, live PR acceptance rates (35-50% gap between benchmark and real-world)
- https://explainx.ai/blog/ai-benchmarks-complete-guide-2026 — Complete guide to AI benchmarks in 2026: MMLU, GPQA, SWE-bench — why they don't catch behavioral regressions

**Agent Failures & Silent Regressions:**
- https://github.com/vectara/awesome-agent-failures — Awesome Agent Failures: curated list of real production failure modes with mitigations and war stories
- https://softcery.com/lab/why-ai-agent-prototypes-fail-in-production-and-how-to-fix-it — Why AI Agents Fail in Production: 6 architecture patterns and fixes for common failure modes
- https://dev.to/thedailyagent/5-ai-agent-failures-in-production-and-how-to-fix-them-2nm0 — 5 AI Agent Failures in Production: hallucinations, incorrect tool use, plan generation failures
- https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures — AI Agent Regression Testing: catching silent failures, 78% of regressions undetected by common approaches
- https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage — Regression Testing for AI Agents: trace-driven debugging, semantic regression tests, pre/post-deploy gates

**GitHub Copilot Agent & Skills Documentation:**
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills — About agent skills: skill folder format, instructions/scripts/resources, project-specific and personal skills
- https://docs.github.com/en/copilot/reference/custom-agents-configuration — Custom agents configuration: YAML frontmatter, agent personas, tool access, invocation rules
- https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/ — Maximizing Copilot agentic capabilities: custom agents, skills, advanced workflows

**Industry Context & Market Data:**
- https://uptimerobot.com/knowledge-hub/monitoring/ai-agent-monitoring-best-practices-tools-and-metrics/ — AI Agent Monitoring: best practices, tools, behavioral metrics (step count, tool usage anomalies)
- https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith — Agent Failure Diagnosis: MAST taxonomy (NeurIPS 2025), 14 distinct failure modes in production

---

## Output Preferences

### Blog
- **Target length**: ~3,000 words per part (if series)
- **Output path**: `content/`

### Series Configuration

> Auto-populated by scope assessment. Edit manually to override.

| Field | Value |
|-------|-------|
| **Is Series** | `yes` |
| **Total Parts** | 2 |
| **Current Part** | 2 |
| **Part 1 Focus** | The Gap Nobody's Testing For — benchmark gap, failure taxonomy, Sourdough Test, minimum viable eval |
| **Part 2 Focus** | Build the Eval System — graders, task patterns, CI architecture, regressions, cost, gotchas, playbook |
| **Publishing Cadence** | 3-5 days between parts |

### Dimension Analysis

> Auto-populated by multi-dimensional analysis (Step 2c). Edit manually to override.

| Field | Value |
|-------|-------|
| **Persona count** | 5 |
| **Personas** | IC Engineer, Tech Lead, Engineering Manager, Platform Engineer, AI Team Decision-Maker |
| **Technology practices** | 10 |
| **Governance practices** | 6 |
| **Total practices** | 16 |
| **Primary WAF pillars** | Reliability, Security, Operational Excellence |
| **Secondary WAF pillars** | Cost Optimization |
| **Dimension breadth score** | 6/6 |

### Social Platform Selection

> The pipeline always generates LinkedIn. For other platforms, select which to include:

- [x] LinkedIn (always included)
- [x] X/Twitter thread
- [ ] Reddit post
- [x] Reel/Short video (60-90 sec)
- [x] YouTube long-form script (8-12 min)

> **Note:** Pipeline will ask for confirmation at Step 4c. Pre-check platforms above to skip the prompt.

### Long-Form Platform Distribution (Step 12)

> Generates platform-optimized excerpts for Medium, Substack, and LinkedIn Article. Visual-first when a `content/visuals/distilled/{slug}-{mode}/manifest.md` exists; text-only fallback otherwise.

- [x] Medium (700–900 words, Import tool auto-sets canonical URL — SEO safe)
- [x] Substack (300–500 words excerpt only — post as Substack Note, not newsletter)
- [x] LinkedIn Article (700–900 words, unique angle — NOT a republish of the blog)

### Canonical URL Configuration

| Field | Value |
|-------|-------|
| **GitHub Pages base** | `https://sendtoshailesh.github.io` |
| **Blog URL pattern** | `{base}/blog/{slug}.html` |
| **Series index URL** | `{base}/blog/series/{series-slug}.html` |
| **Publishing log** | `content/publishing-log.md` |

### Social Posts
- **LinkedIn**: Plain + Unicode formatted versions
- **X/Twitter**: 10-12 tweet thread + standalone summary (if selected)
- **Reddit**: Standard Markdown, target subreddits listed below (if selected)
- **Reel/Short video**: 60-90 sec script with screen recording cues + voiceover (if selected)

### Target Subreddits
- r/MachineLearning
- r/ExperiencedDevs
- r/artificial
- r/programming
- r/ChatGPTCoding
- r/CopilotForDevs

### YouTube
- **Target duration**: 8-12 minutes
- **Output path**: `content/youtube-script.md`

### Reel/Short Video
- **Target duration**: 60-90 seconds
- **Platforms**: Instagram Reels, YouTube Shorts, LinkedIn Video
- **Output path**: `content/reel-script.md`

---

## Distillation Settings

| Setting | Value | Description |
|---------|-------|-------------|
| `visual_strategy_mode` | `mandatory` | Visual opportunity mapping is required for every content run before blog writing. Read by: content-pipeline, visual-strategist, blog-writer, visual-renderer, social-strategist. |
| `visual_opportunity_map` | `content/visual-opportunity-map.md` | Planning artifact that maps text sections to blog companion visuals and standalone distribution assets. |
| `visual_first_platform_scope` | `blog, linkedin, medium, substack, linkedin-article` | First implementation platform scope. X/Twitter, Reddit, YouTube, and Reels remain follow-on unless selected elsewhere. |
| `visual_first_formats` | `architecture-flow, infographic-one-pager, comic-storyboard, linkedin-card-pack, executive-exhibit` | Mandatory first-milestone visual families. Comic/storyboard assets must be programmatic only. |
| `image_generation_policy` | `programmatic-only` | Use Python, Pillow, SVG via Python, Mermaid, and matplotlib only. Do not require external image generation. |
| `distillation_persona_mode` | `practitioner` | Visual pack persona mode. Options: `practitioner` (10-slide carousel, 1080×1080px, Welsh/Lenny/Bloom grammar), `executive` (3-5 exhibits, 1200×627px, HBR/McKinsey exhibit grammar), `ask` (prompt at runtime). Read by: visual-pack-generator skill, social-linkedin agent, social-twitter agent, platform-distiller agent. |
| `distillation_slug` | *(set per run)* | Part identifier used in visual pack directory naming, e.g., `part1`, `part2`. Results in `content/visuals/distilled/{slug}-{mode}/`. |

---

## Pipeline Steps Reference

> Distribution and publishing steps. Run in order. Visual opportunity mapping is mandatory before blog writing; Steps 4a-visual through 12 are post-content steps.

| Step | Agent / Skill | Trigger | Description |
|------|--------------|---------|-------------|
| Step 2d | visual-strategist / visual-content-planning | Mandatory | Creates `content/visual-opportunity-map.md` and adds P0 visual markers before blog writing. |
| Step 4a-visual | visual-pack-generator | Mandatory for visual-first distribution | Generates visual asset pack (PNGs + manifest + renderer) for selected platforms. Run BEFORE Steps 4, 5, 12. Invoked via visual-pack-generator skill with blog path + distillation_slug + distillation_persona_mode. |
| Step 4a-visual-plus | visual-strategist + visual-renderer | Mandatory when opportunity map has P0/P1 standalone visuals | Generates LinkedIn and long-form platform assets: architecture/flow diagrams, infographics/one-pagers, comic/storyboards, card packs, and executive exhibits. |
| Step 4 | social-linkedin | Manual | LinkedIn post generation. Output: `content/linkedin-post.md` |
| Step 5 | social-twitter | Manual | X/Twitter thread generation. Output: `content/x-twitter-thread.md` |
| Step 6 | social-reddit | Manual | Reddit post generation (if selected). Output: `content/reddit-post.md` |
| Step 6b | reel-video | Manual | Short video script (60-90 sec). Output: `content/reel-script.md` |
| Step 7 | brand-guardian | Manual | Brand audit across all generated content pieces |
| Step 10 | web-publisher | Manual | Publish to GitHub Pages; establish canonical URL; update index |
| Step 11 | social-publisher | Manual | Publish to social platforms (per publishing mode + approved platforms) |
| Step 12 | platform-distiller | Manual | Visual-first or text-only excerpts per platform-distiller |

---

## Publishing Configuration

> Controls how generated social content is published to platforms. See `docs/social-api-setup.md` for credential setup.

### Publishing Mode

| Field | Value |
|-------|-------|
| **Publish mode** | `confirm` |
| **Publish approach** | `per-platform` |

**Mode values:**
- `manual` — content generated only; user copy-pastes to platforms
- `confirm` — MCP servers preview content; user approves before posting
- `auto` — post immediately after generation (not recommended)

**Approach values:**
- `per-platform` — free MCP servers: reddit-mcp-server + mcp-linkedin + custom (X/YouTube). Cost: $0/mo
- `posteverywhere` — PostEverywhere SaaS MCP. Cost: $19-79/mo. Does NOT cover Reddit.
- `postfast` — PostFast SaaS MCP. Cost: paid. Does NOT cover Reddit.

### Published URLs

> Auto-populated after publishing. Cleared on archive.

#### GitHub Pages (Canonical)

| Part | URL | Published |
|------|-----|-----------|
| Part 1 | https://sendtoshailesh.github.io/blog/agent-eval-part-1.html | 2025-07-17 |
| Part 2 | https://sendtoshailesh.github.io/blog/agent-eval-part-2.html | 2025-07-17 |
| Series Index | https://sendtoshailesh.github.io/blog/series/agent-eval.html | 2025-07-17 |
| Visual-first Canonical | https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html | 2026-06-08 |

#### Social Media

| Platform | URL | Posted |
|----------|-----|--------|
| LinkedIn | https://www.linkedin.com/feed/update/urn:li:ugcPost:7470133668175433728/ | 2026-06-09 |
| X/Twitter | — | — |
| Reddit | — | — |

#### Long-Form Platforms

| Platform | URL | Posted |
|----------|-----|--------|
| Medium | https://medium.com/@shaileshkumarmishra/ai-agent-evals-production-readiness-guide-bd60e62f877a | 2026-06-09 |
| Substack | — | — |
| LinkedIn Article | — | — |

### Publish Sequence

| Day | Action | Notes |
|-----|--------|-------|
| Day 0 | Generate visual pack | Run visual-pack-generator (Step 4a-visual) with target slug + persona mode |
| Day 0 | GitHub Pages publish | Establishes canonical URL |
| Day 0 | Medium Import | Use Import tool — sets rel=canonical → protects SEO |
| Day 0 | LinkedIn Post | Upload carousel slides as PDF document post. Add canonical URL as FIRST COMMENT within 60 sec |
| Day 0 | X/Twitter thread | Upload image cards to tweet thread. Canonical URL in FINAL TWEET ONLY |
| Day 3-4 | Substack Note | Post as NOTE (not newsletter). Hero image + excerpt + canonical link |
| Day 7+ | LinkedIn Article | Unique angle (>30% new material). 2-3 inline exhibits. Google indexes this — must be unique. |
