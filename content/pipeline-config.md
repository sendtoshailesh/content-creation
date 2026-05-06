# Content Pipeline Configuration

> **Edit this file** to configure your content pipeline preferences. All pipeline agents read this config before starting work.

---

## Pipeline Status

> **Auto-updated by the pipeline orchestrator.** Check this to see where content creation stands.

| Field | Value |
|-------|-------|
| **Status** | `in-progress` |
| **Topic** | Optimizing Cost While Using AI Code Assistants — Token Efficiency, Context Management & Smart Strategies |
| **Started** | 2026-05-06 |
| **Current Step** | Steps 1-2: Strategy + outline |

### Step Checklist

- [x] Step 0: Reference analysis
- [x] Steps 1-2: Strategy + outline
- [ ] Step 3: Blog post
- [ ] Step 3b: Visual assets
- [ ] Step 3c: Quality review
- [ ] Step 3d: SEO optimization
- [ ] Step 4: LinkedIn post
- [ ] Step 5: X/Twitter thread
- [ ] Step 6: Reddit post
- [ ] Step 7: Brand audit
- [ ] Step 8: YouTube script
- [ ] Step 10: Publish to GitHub Pages
- [ ] Final review complete

**Status values:** `not-started` | `in-progress` | `completed` | `blocked`

> **What to do:**
> - If Status is `not-started` → You're clear to start a new run. Edit references/preferences below, then run `@content-pipeline` or `/new-content-pipeline`
> - If Status is `in-progress` → Content creation is underway. Run `@content-pipeline` to resume from where it left off
> - If Status is `completed` → All steps done! Review the content, then run `/archive-content` to archive and start fresh
> - If Status is `blocked` → See Current Step for what needs attention

---

## Model Selection

Choose which model to use for content generation. Select your model in the **VS Code Copilot model picker** before running agents.

### Recommended Models by Task

| Task | Recommended | Why |
|------|-------------|-----|
| Content Strategy / Planning | Claude Sonnet 4 or o3 | Deep reasoning, nuanced audience analysis |
| Blog Writing | Claude Sonnet 4 or GPT-4.1 | Strong technical writing, data accuracy |
| Visual Generation | GPT-4.1 or Claude Sonnet 4 | Reliable code generation for Python renderers |
| Quality Review | Claude Sonnet 4 | Best at critical analysis and finding gaps |
| Social Posts (LinkedIn/Twitter) | Claude Sonnet 4 or GPT-4o | Good at concise, punchy copy |
| Reddit Posts | Claude Sonnet 4 | Natural conversational tone |
| Video Scripts | Claude Sonnet 4 or GPT-4.1 | Structured output with timing |

### Current Selection

**Preferred model**: _(select in VS Code Copilot picker — agents inherit your selection)_

### Available Models (GitHub Copilot)

Run `/configure-model` to see the latest available models and get recommendations.

**Flagship**: Claude Sonnet 4, Claude Sonnet 4.5, GPT-4.1, GPT-4o, Gemini 2.5 Pro
**Fast**: Claude Haiku 3.5, GPT-4o mini, GPT-4.1 mini, GPT-4.1 nano
**Reasoning**: o3, o4-mini, Claude Sonnet 4 (Extended Thinking)

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
- **Target length**: ~3,000 words
- **Output path**: `content/`

### Social Posts
- **LinkedIn**: Plain + Unicode formatted versions
- **X/Twitter**: 10-12 tweet thread + standalone summary
- **Reddit**: Standard Markdown, target subreddits listed below

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
