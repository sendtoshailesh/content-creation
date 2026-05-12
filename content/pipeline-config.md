# Content Pipeline Configuration

> **Edit this file** to configure your content pipeline preferences. All pipeline agents read this config before starting work.

---

## Pipeline Status

> **Auto-updated by the pipeline orchestrator.** Check this to see where content creation stands.

| Field | Value |
|-------|-------|
| **Status** | `completed` |
| **Topic** | Engineering Better AI Code Assistant Interactions — Context Engineering, Workflow Discipline & Informed Model Selection |
| **Started** | 2026-05-06 |
| **Current Step** | All steps complete. Ready for publishing. |
| **Series** | `yes (3 parts)` |
| **Current Part** | All parts written |

### Step Checklist

- [x] Step 0: Reference analysis
- [x] Steps 1-2: Strategy + outline -> `content/ai-code-assistant-optimization-strategy.md` (replaces cost-first angle)
- [x] Step 2b: Scope assessment (single vs. series) -> **Series: 3 parts, score 16/16**
- [x] Step 2c: Multi-dimensional analysis -> **3 personas, 11 practices, 3 WAF pillars, score 2/2**
- [x] Step 3: Blog post (Part 1) -> `content/context-engineering-part-1.md`
- [x] Step 3b: Visual assets -> 3 PNGs (paradox, framework, before-after)
- [x] Step 3c: Quality review -> 14/14 claims verified, 1 minor fix (date precision)
- [x] Step 3e: Grounded content review -> all sources re-fetched, 0 corrections
- [x] Step 4: LinkedIn post -> `content/linkedin-post-part1.md`
- [x] Step 4c: Social platform selection -> Reel/Short video only
- [ ] Step 5: X/Twitter thread (if selected)
- [ ] Step 6: Reddit post (if selected)
- [x] Step 6b: Reel/Short video -> `content/reel-script-part1.md`
- [x] Step P2-3: Blog post (Part 2) -> `content/ai-code-assistant-cost-part-2.md`
- [x] Step P2-3b: Visual assets (Part 2) -> 2 PNGs (caching-flow, retry-tax-calculator)
- [x] Step P2-4: LinkedIn post (Part 2) -> `content/linkedin-post-part2.md`
- [x] Step P2-6b: Reel/Short video (Part 2) -> `content/reel-script-part2.md`
- [x] Step P3-3: Blog post (Part 3) -> `content/ai-code-assistant-cost-part-3.md`
- [x] Step P3-3b: Visual assets (Part 3) -> 3 PNGs (task-model-alignment, team-governance-dashboard, three-layer-stack)
- [x] Step P3-4: LinkedIn post (Part 3) -> `content/linkedin-post-part3.md`
- [x] Step P3-6b: Reel/Short video (Part 3) -> `content/reel-script-part3.md`
- [x] Cross-linking: All 3 parts linked in intro/CTA sections
- [x] Quality review (Parts 2-3): 27/27 claims verified, 1 fix (GPT-4o missing from included models), 1 clarification (Anthropic cache write cost). Created with Anthropic family.
- [x] Visual density pass (Parts 2-3): Added 3 new visuals to Part 2 (prompt-structure-breakdown, retry-loop-anatomy, caching-comparison) and 2 to Part 3 (routing-decision-comparison, team-optimization-strategies). Total visuals: Part 2 = 5, Part 3 = 5.
- [x] Step 3d: SEO optimization -> keyword placement in headings + opening paragraphs across all 3 parts
- [x] Step 7: Brand audit -> data consistency fix (80-90% -> 90%), hashtag normalization across LinkedIn posts
- [x] Step 10: Publish to GitHub Pages -> 3 HTML pages + index updated + visuals copied
- [x] Final review complete

**Series values:** `not-applicable` | `pending-assessment` | `yes (N parts)` | `no`

**Status values:** `not-started` | `in-progress` | `completed` | `blocked`

> **What to do:**
> - If Status is `not-started` → You're clear to start a new run. Edit references/preferences below, then run `@content-pipeline` or `/new-content-pipeline`
> - If Status is `in-progress` → Content creation is underway. Run `@content-pipeline` to resume from where it left off
> - If Status is `completed` → All steps done! Review the content, then run `/archive-content` to archive and start fresh
> - If Status is `blocked` → See Current Step for what needs attention

---

## Model Selection

Choose which model to use for content generation. Select your model in the **VS Code Copilot model picker** before running agents.

### Model Family Detection

The pipeline tracks which model family was used for content creation and ensures critic review uses a **different** family. No model versions are hardcoded — whatever the latest model is in each family within GitHub Copilot will be used.

| Family | Model name prefix |
|--------|------------------|
| `anthropic` | Claude * |
| `openai` | GPT-*, o* |
| `google` | Gemini * |

### Cross-Model Critic Review

| Role | Selection Rule |
|------|---------------|
| **Content Creation** | User selects any model; pipeline records the family used |
| **Critic Review** | Must use a model from a **different family** than creation |
| **Visual Generation** | User selects any model |

> **How it works**: After content is created, the orchestrator identifies the creation model family and prompts you to switch to any model from a different family before running quality review. This ensures adversarial diversity — different model families have different biases, blind spots, and strengths.

### Current Run

| Field | Value |
|-------|-------|
| **Creation model family** | _(auto-detected from VS Code picker during content creation)_ |
| **Critic model family** | _(switch to a different family before quality review)_ |

### Current Selection

**Preferred model**: _(select any model in the VS Code Copilot picker — agents inherit your selection automatically)_

The only constraint is cross-model critic review: the pipeline will ask you to switch to a **different model family** before quality review. No specific model versions are required — use whatever is available.

---

## Online References

List URLs below that agents should fetch, analyze, and synthesize during content creation. The pipeline will read these before writing.

### How to Use

1. Add URLs under the appropriate section below
2. Add a brief note on what to extract from each
3. Pipeline agents will fetch and analyze these during Steps 1-3

### Reference URLs

<!-- Add your reference URLs below. Format: - [description](URL) -->

**General content:**
- https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens/ — Token savings strategies for agentic AI workflows
- https://towardsdatascience.com/inference-scaling-test-time-compute-why-reasoning-models-raise-your-compute-bill/ — Why reasoning models cost more, task taxonomy (Use/Maybe/Avoid)
- https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/ — Context management best practices that reduce wasted tokens
- https://www.anthropic.com/engineering/advanced-tool-use — 85% token reduction via Tool Search, 37% via programmatic calling
- https://github.com/openai/openai-cookbook/blob/main/articles/openai-harmony.md — Model routing: Use/Maybe/Avoid taxonomy for reasoning models
- https://towardsdatascience.com/tool-masking-the-layer-mcp-forgot/ — Shaping MCP tool surfaces to cut tokens and improve accuracy

**Industry Reports & Benchmarks:**
- https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai — 2x speed gains, <10% on complex tasks, developer satisfaction data
- https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/ — RCT: 55% faster coding, 85% confidence, 30% acceptance rate
- https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests — Model multipliers (Opus=3x, nano=0.25x), 10% auto-selection discount
- https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ — June 2026 shift to per-token billing, why cost optimization matters NOW

**Competitor / Related Articles:**
- https://www.cursor.com/en/pricing — Pro $20, Pro+ $60, Ultra $200, Teams $40/user comparison
- https://www.arcade.dev/blog/anthropic-tool-search-4000-tools-test/ — Independent test of lazy-loading with 4000 tools, counterpoint to claims
- https://www.mindstudio.ai/blog/what-is-ai-model-router-optimize-cost-llm-providers — 68% cost reduction example ($3K→$970/day) via model routing

**Pricing Pages & Documentation:**
- https://openai.com/api/pricing/ — GPT-5.5 ($5/$30 MTok), cached input 90% discount, batch 50% off
- https://claude.com/pricing#api — Opus ($5/$25), Sonnet ($3/$15), Haiku ($1/$5), prompt caching 90% off reads
- https://docs.github.com/en/copilot/concepts/billing/copilot-requests#model-multipliers — Full multiplier table, auto-selection discount, free tier limits

**Case Studies & Examples:**
- https://github.blog/news-insights/research/survey-ai-wave-grows/ — 2000-person survey on AI tool adoption, satisfaction, and enterprise usage data

**Research Papers:**
- https://arxiv.org/abs/2310.06201 — Selective Context (EMNLP 2023): 50% context reduction, 36% memory savings, minimal quality loss
- https://arxiv.org/abs/2603.28119 — SWEzze: 6x compression, 51-71% token reduction + 5-9% better issue resolution
- https://lmsys.org/blog/2024-07-01-routellm/ — RouteLLM: 95% GPT-4 quality at 75% lower cost, outperforms commercial routers
- https://arxiv.org/abs/2601.07206 — LLMRouterBench: Counterpoint — many learned routers barely beat simple baselines

---

## Output Preferences

### Blog
- **Target length**: ~3,000 words per part (if series)
- **Output path**: `content/`

### Series Configuration

> Auto-populated by scope assessment. Edit manually to override.

| Field | Value |
|-------|-------|
| **Is Series** | `pending-assessment` |
| **Total Parts** | — |
| **Current Part** | — |
| **Part 1 Focus** | — |
| **Publishing Cadence** | — |

### Dimension Analysis

> Auto-populated by multi-dimensional analysis (Step 2c). Edit manually to override.

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

### Social Platform Selection

> The pipeline always generates LinkedIn. For other platforms, select which to include:

- [x] LinkedIn (always included)
- [x] X/Twitter thread
- [ ] Reddit post
- [x] Reel/Short video (60-90 sec)
- [x] YouTube long-form script (8-12 min)

> **Note:** Pipeline will ask for confirmation at Step 4c. Pre-check platforms above to skip the prompt.

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

| Platform | URL | Posted |
|----------|-----|--------|
| — | — | — |
