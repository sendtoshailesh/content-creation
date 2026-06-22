# Content Pipeline Configuration

> **Edit this file** to configure your content pipeline preferences. All pipeline agents read this config before starting work.

---

## Pipeline Status

> **Auto-updated by the pipeline orchestrator.** Check this to see where content creation stands.

| Field | Value |
|-------|-------|
| **Status** | `in-progress` |
| **Topic** | From Prompts to Harness Engineering — The Workflow Shift in AI-Native Development |
| **Started** | 2026-06-20 |
| **Current Step** | Step 3b redo — rebuilding visuals with the Visual Versatility System (2026-06-22, visuals rejected as single-style / text-heavy) |
| **Series** | `no` |
| **Current Part** | _(n/a)_ |

### Step Checklist

- [x] Step 0: Reference analysis
- [x] Steps 1-2: Strategy + outline
- [x] Step 2b: Scope assessment (single vs. series) — 5/14, single post
- [x] Step 2c: Multi-dimensional analysis
- [x] Step 2d: Visual opportunity mapping
- [x] Step 2e: Infographic art direction
- [x] Step 3: Blog post draft
- [ ] Step 3b: Visual assets — REDO: re-render across multiple styles via the Visual Versatility System (pilot proven: typographic, sketch, rough.js)
- [x] Step 3b-img: hero/illustrative imagery (optional — skipped; no separate hero slot planned)
- [ ] Step 3c: Quality review — re-run after visuals rebuilt
- [ ] Step 3d: SEO optimization — re-confirm after visuals rebuilt
- [ ] Step 4a: Social distribution strategy refresh — re-run after visuals rebuilt
- [ ] Step 4a-visual: Visual-first asset pack — STALE: regenerate from new visuals
- [ ] Step 4: LinkedIn post — STALE: references rejected visuals, regenerate
- [x] Step 4c: Social platform selection — LinkedIn + Reel/Short video only
- [x] Step 5: X/Twitter thread — skipped by user selection
- [ ] Step 6b: Reel/Short video — STALE: references rejected visuals, regenerate
- [ ] Step 7: Brand audit — re-run after visuals rebuilt
- [ ] Step 7b: Grounded content review — re-run after visuals rebuilt
- [x] Step 8: YouTube script — skipped by user selection
- [ ] Step 10: Web publishing refresh — blocked until visuals rebuilt
- [ ] Step 11: Social publishing
- [ ] Step 12: Platform distillation draft

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

**Harness Engineering — Core Thesis & Workflow Shift:**
- https://www.infoq.com/podcasts/mcp-vibe-coding-harness-engineering/ — Thoughtworks' Birgitta Böckeler: monolithic context files and MCP servers giving way to lazy-loaded skills, CLIs, and scripts; the "harness engineering" framing
- https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/ — Custom agents turn repeatable prompts into reusable terminal workflows
- https://towardsdatascience.com/how-to-navigate-the-shift-from-prompt-based-tools-to-workflow-driven-ai/ — The cost of constant tool/context switching and how workflows fix it
- https://towardsdatascience.com/automate-writing-your-llm-prompts/ — Writing robust, reliable prompts for unattended LLM applications (prompt-as-code)

**Skills, Lazy-Loading & Tooling Primitives:**
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills — About agent skills: folder format, instructions/scripts/resources, load-on-demand
- https://www.infoq.com/news/2026/06/angular-agent-skills/ — Angular's official Agent Skills using Anthropic's open Skills format (load-on-demand)
- https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers/ — LSP Setup skill: giving the CLI real code intelligence via language servers
- https://github.blog/ai-and-ml/github-copilot/getting-more-from-each-token-how-copilot-improves-context-handling-and-model-routing/ — Prompt caching + deferred tools + Auto model routing: the harness, not the model, doing the work

**Harness Mechanics — Delegation, Parallelism, Inner-Loop Validation:**
- https://github.blog/ai-and-ml/how-we-made-github-copilot-cli-more-selective-about-delegation/ — "Delegation isn't free": data-driven subagent tuning
- https://towardsdatascience.com/a-harness-for-every-task-putting-a-team-of-claudes-on-one-job/ — A harness for every task: orchestrating a team of agents on one job
- https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/ — Git worktrees for parallel agent workspaces
- https://www.infoq.com/news/2026/06/circleci-chunk-sidecars/ — CircleCI Chunk Sidecars: CI-style validation moved into the agent's inner loop so it self-corrects before commit
- https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-overview-of-common-slash-commands/ — Copilot CLI slash commands overview (workflow surface)

**First-Party Reference (this repo's own harness):**
- Local: `agents-and-skills/automation-architecture.md`, `agents-and-skills/agent-definitions.md`, `agents-and-skills/content-strategy-pipeline.md` — the agent/skill/instruction harness that runs this very content pipeline

---

## Output Preferences

### Blog
- **Target length**: ~3,000 words per part (if series)
- **Output path**: `content/`

### Image Generation (hybrid AI imagery)

> Controls the optional image step (Step 3b-img). Scope is **hero / backdrop / scene /
> conceptual-illustration** assets only — diagrams, infographics, flows, comparison
> matrices, and executive exhibits stay deterministic/programmatic.
>
> **Two modes, default is free + offline:**
> - `programmatic` — deterministic hero/backdrop rendered by `scripts.visuals.generated.programmatic`
>   (HTML/CSS+Chromium, brand tokens, reserved negative space). **No API key, no network, no
>   cost, fully reproducible.** This is the default.
> - `ai` — calls an external image model (OpenAI/Azure) for a photoreal/illustrative look.
>   Opt-in only; needs a key + network + spend. See `agents-and-skills/image-provider-comparison.md`.
> - `off` — skip image generation entirely.

| Field | Value |
|-------|-------|
| **mode** | `programmatic` |
| **provider** (ai mode only) | `openai` |
| **model** (ai mode only) | `gpt-image-1` |
| **size** | `1024x1024` |
| **quality** (ai mode only) | `medium` |
| **max_images_per_run** | `3` |
| **reference_images** | _(paths/URLs for grounding, optional)_ |

> Every generated image (either mode) is written to `content/visuals/generated/` with a sidecar
> JSON (mode, license, safety, and for `ai` the provider/model/prompt/seed), must pass the
> deterministic `scripts.visuals.generated.inspect_image` pre-screen (no-text, brand-color
> fidelity, negative-space), and then `visual-reviewer`.

### Series Configuration

> Auto-populated by scope assessment. Edit manually to override.

| Field | Value |
|-------|-------|
| **Is Series** | `pending-assessment` |
| **Total Parts** | _(tbd)_ |
| **Current Part** | _(tbd)_ |
| **Part 1 Focus** | _(tbd — set by scope assessment)_ |
| **Part 2 Focus** | _(tbd — set by scope assessment)_ |
| **Publishing Cadence** | _(tbd)_ |

### Dimension Analysis

> Auto-populated by multi-dimensional analysis (Step 2c). Edit manually to override.

| Field | Value |
|-------|-------|
| **Persona count** | _(tbd)_ |
| **Personas** | _(tbd — set by dimension analysis)_ |
| **Technology practices** | _(tbd)_ |
| **Governance practices** | _(tbd)_ |
| **Total practices** | _(tbd)_ |
| **Primary WAF pillars** | _(tbd — set by dimension analysis)_ |
| **Secondary WAF pillars** | Cost Optimization |
| **Dimension breadth score** | 6/6 |

### Social Platform Selection

> The pipeline always generates LinkedIn. For other platforms, select which to include:

- [x] LinkedIn (always included)
- [ ] X/Twitter thread
- [ ] Reddit post
- [x] Reel/Short video (60-90 sec)
- [ ] YouTube long-form script (8-12 min)

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
