# YouTube Script — Part 3: From PRUs to AI Credits

## Video Details

- **Target duration**: 8-10 minutes
- **Topic**: PRUs retire June 1, 2026 — token-metered AI Credits, the Lightweight/Versatile/Powerful taxonomy, and team governance
- **Source blog**: `content/ai-code-assistant-cost-part-3.md`
- **Published URL**: `https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html`

## Title Options

1. From PRUs to AI Credits: GitHub Copilot's Token-Based Bill Is Already Here (Part 3)
2. Stop Defaulting to the Powerful Model — Category-Based Routing for AI Code Assistants
3. GitHub Copilot AI Credits Explained: When to Use Lightweight vs Versatile vs Powerful
4. AI Coding Costs Part 3: The Category Taxonomy That Cuts Spend ~86%

## Description

── START COPY ──

On June 1, 2026, GitHub Copilot retires Premium Request Units and switches to token-metered GitHub AI Credits (1 credit = $0.01). A short Lightweight chat costs ~$0.001. A deep Powerful agent session can cost ~$0.45 — a ~450x per-request spread, now visible on your bill in real dollars.

In this video:
- What changes on June 1, 2026 (PRUs out, AI Credits in)
- Why the Powerful category isn't always better (Apple ML Research data)
- The 3-category task taxonomy (Lightweight / Versatile / Powerful)
- The cost math in real dollars: ~$4/day vs ~$30/day for the same 100 requests
- RouteLLM: 95% flagship quality at 75% lower cost
- Team governance playbook for AI team leads and decision-makers
- The complete 3-layer optimization stack from this series

TIMESTAMPS:
0:00 - PRUs retire June 1, 2026
0:45 - Why Powerful isn't always better
2:00 - Lightweight / Versatile / Powerful taxonomy
3:30 - The cost math in real dollars
4:30 - RouteLLM and smart routing evidence
5:45 - Team governance for AI team leads and decision-makers
7:15 - The complete 3-layer playbook (series recap)
8:30 - Action plan + what to do before June 1
9:30 - Close

Part 3 of 3 in the "Engineering Better AI Code Assistant Interactions" series.

Blog post: https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html
Series index: https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html

SOURCES (verify the ground rules):
- GitHub Blog (usage-based billing): https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
- GitHub Docs (models and pricing): https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
- Annual subscriber edge case: https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing#model-multipliers-for-annual-copilot-pro-and-copilot-pro-subscribers
- Apple ML Research, "The Illusion of Thinking": https://machinelearning.apple.com/research/illusion-of-thinking
- RouteLLM (LMSYS, 2024): https://lmsys.org/blog/2024-07-01-routellm/
- CascadeFlow (arXiv, 2024): https://arxiv.org/abs/2406.00073
- Towards Data Science production case study: https://towardsdatascience.com/inference-scaling-test-time-compute-why-reasoning-models-raise-your-compute-bill/

Note: Specific model names mentioned in this video (e.g., GPT-5.4 nano in Lightweight, Claude Opus 4.x in Powerful) are accurate as of May 2026. Model lineups rotate; the Lightweight / Versatile / Powerful taxonomy is the durable framework.

#GitHubCopilot #AICredits #ModelRouting #AIEngineering #DeveloperProductivity

── END COPY ──

## Thumbnail Concepts

1. **PRU → AI Credit**: "PRUs" struck through; "$ AI Credits" rising next to it — matches the new framing
2. **Per-request spread**: "$0.001 → $0.45" giant text with "~450x" badge underneath
3. **Three-category columns**: Lightweight/Versatile/Powerful stacked vertically with $ badges — clean taxonomy visual

## Script

### [0:00 - 0:45] Cold Open

**SLIDE**: `task-model-alignment.png`
**SCRIPT**: On June first, twenty-twenty-six, GitHub Copilot retires Premium Request Units. The flat-multiplier system where a model cost zero-point-two-five x, one x, three x, or thirty x — gone. Token-metered GitHub AI Credits take over. A short chat reply on a Lightweight model costs about a tenth of a cent. A deep agent-mode session on a Powerful model can cost forty-five cents. That is roughly a four-hundred-fifty-x per-request spread — and starting June first, it shows up on your bill in real dollars. But here is what most people get wrong: the expensive category is not always the better choice. Apple ML Research found that reasoning models perform worse than standard models on simple tasks, while burning thousands of extra tokens. Today I will show you exactly when to use each category. Source links for everything are in the description.
**NOTES**: Punch the June 1 date and the ~450x number. Mention the description-link callout once at the top so viewers know where to verify.

### [0:45 - 2:00] Why Powerful Isn't Always Better

**SLIDE**: `routing-decision-comparison.png`
**SCRIPT**: Apple ML Research tested reasoning models against standard models on low-complexity coding tasks — variable renaming, docstrings, import fixes. The reasoning models burned thousands of extra tokens on internal chain-of-thought. And the result? Zero quality improvement. On some benchmarks, the standard model was actually more accurate. The full paper from Apple ML Research is linked in the description. This is not just a cost argument. It is a quality argument. Throwing the Powerful category at simple work can give you genuinely worse output, more slowly, for forty-five times the cost.
**NOTES**: Emphasize that this is a quality argument, not just a cost argument.

### [2:00 - 3:30] The 3-Category Task Taxonomy

**SLIDE**: `task-model-alignment.png`
**SCRIPT**: GitHub now categorizes every model into three durable buckets: Lightweight, Versatile, and Powerful. They map cleanly to a three-category task taxonomy. Lightweight: simple tasks. Variable renaming, boilerplate generation, test scaffolding, doc writing. Sixty to seventy percent of daily interactions. As of recording, that includes models like GPT-5 mini, GPT-5.4 nano, and Gemini 3.5 Flash. Versatile: moderate tasks. Code review, refactoring, debugging with stack-trace correlation. Twenty to thirty percent. As of recording, that's Claude Sonnet 4.x, GPT-4.1, GPT-5.4, and Claude Haiku 4.5. Best quality-per-dollar bucket. Powerful: complex tasks. Multi-file refactoring with dependencies, system design, agent-mode sessions on hard problems. Only five to ten percent. Examples: Claude Opus 4.x, GPT-5.5, Gemini 2.5 Pro. The specific model names will rotate over time. The Lightweight / Versatile / Powerful taxonomy is what stays durable.
**NOTES**: Use the visual to walk through each category. This is the core framework of the video.

### [3:30 - 4:30] The Cost Math

**SLIDE**: `team-optimization-strategies.png`
**SCRIPT**: Let me run the numbers for one hundred requests per day. Sixty-five Lightweight at about a tenth of a cent: six and a half cents. Twenty-five Versatile at about four cents: one dollar. Ten Powerful at about thirty cents: three dollars. Daily total: about four dollars and seven cents. Compare that to running every request through a Powerful model: about thirty dollars per day. That is roughly eighty-six percent saved. You are not downgrading. You are matching capability to need — and using a *more* expensive model for the hardest five to ten percent of tasks.
**NOTES**: Walk through the math on screen. The $4 vs $30 comparison is the punch line.

### [4:30 - 5:45] RouteLLM and Production Evidence

**SLIDE**: `routing-decision-comparison.png`
**SCRIPT**: This is not just theory. RouteLLM from LMSYS achieved ninety-five percent of the flagship-model quality while using the flagship for only fourteen percent of calls — a seventy-five percent cost reduction. In the original RouteLLM paper, the flagship was GPT-4 as the 2024 baseline; the principle generalizes to whatever the current Powerful model is. CascadeFlow delivered sixty-nine percent savings with ninety-six percent quality retention. And a real coding team profiled by Towards Data Science dropped from three thousand dollars per day to nine hundred seventy — a sixty-eight percent reduction, seven hundred forty thousand dollars annualized — through model routing alone. All three sources are linked in the description.
**NOTES**: These are the credibility numbers. The $3K to $970 case study is the most compelling for practitioners.

### [5:45 - 7:15] Team Governance for AI Team Leads and Decision-Makers

**SLIDE**: `team-governance-dashboard.png`
**SCRIPT**: If you are an AI team lead or decision-maker on Business or Enterprise, plan allowances match the subscription fee — nineteen dollars per user per month on Business, thirty-nine on Enterprise. Promotional credits in June through August bump Business to thirty per user and Enterprise to seventy. Plan around the standard allowance, not the promotional ceiling. Pooled credits are shared across organizations instead of siloed per user. Budget controls exist at enterprise, cost center, and user levels. Usage visibility shows which developers, projects, and model categories consume the most credits. Four actions before June 1. First, document your team's task taxonomy and recommended category per task type — put it in your team wiki and your copilot-instructions file. Second, set budget alerts at fifty, seventy-five, and ninety percent of the standard allocation. Third, review top-consuming workflows monthly — agent-mode sessions on Powerful models are valuable but expensive. Fourth, invest in context engineering training, not model restrictions. AI team leads who restrict model access create frustration and workarounds. AI team leads who teach context engineering get the same savings with happier developers. One edge case to flag: annual Pro and Pro+ subscribers stay on PRU multipliers until plan expiry, and the multipliers actually increase for them on June first. Plan renewals accordingly.
**NOTES**: This section speaks directly to AI team leads and decision-makers. Slow down on the four recommendations.

### [7:15 - 8:30] The Complete 3-Layer Playbook (Series Recap)

**SLIDE**: `three-layer-stack.png`
**SCRIPT**: This is Part 3 of 3, and the three parts describe a compound optimization stack. Layer 1 from Part 1: context engineering. Give AI better input. Fifty to eighty-five percent token reduction with quality improvements. Layer 2 from Part 2: caching and workflow discipline. Avoid paying repeatedly for good input. Cached input is roughly ten times cheaper than fresh input on most models. Retry elimination cuts effective spend further. Layer 3 from Part 3: category-based model selection. Match model capability to task complexity. About eighty-five percent reduction in model costs without quality loss. Combined potential across all three layers: roughly ninety percent effective cost reduction with equal or better output quality. Applied together, a typical individual developer can comfortably stay inside Pro's ten-dollar monthly credit allowance.
**NOTES**: This is the series capstone. Walk through each layer with the visual.

### [8:30 - 9:30] Action Plan + What to Do Before June 1

**SCRIPT**: Here is your action plan. This week: review your default model and consider switching to a Lightweight-category model for routine work. Document your task taxonomy: which tasks are Lightweight, Versatile, and Powerful for your team. Before June 1: set budget alerts at fifty, seventy-five, and ninety percent of the standard credit allowance; review your team's category-usage patterns; and share Part 1 of this series with anyone who prompts AI code assistants without thinking about context. The billing change is real. The urgency is valid. But the advice is durable. Better input produces better output whether you pay per token, per request, or nothing at all. Start with context engineering. Everything else compounds on top of it.
**NOTES**: Keep the action items crisp. End with the "start with context" message that ties the series together.

### [9:30 - 10:00] Close

**SCRIPT**: The full 3-part blog series and every research source I cited today are linked in the description — including the official GitHub docs page with the per-1M-token pricing table and the task taxonomy reference card. If your team is navigating this billing change, share this video with your AI team lead or decision-maker — the governance section was written for them. See you in the comments.
**NOTES**: Direct CTA to share. Mention the description links twice — once for the series, once for sources.

## Slide Map

| Timestamp | Visual | Description |
|-----------|--------|-------------|
| 0:00 | `task-model-alignment.png` | 3-category task taxonomy with model assignments |
| 0:45 | `routing-decision-comparison.png` | Manual vs auto routing comparison |
| 2:00 | `task-model-alignment.png` | Walk through each category in detail |
| 3:30 | `team-optimization-strategies.png` | Cost math in real dollars |
| 4:30 | `routing-decision-comparison.png` | RouteLLM and production evidence |
| 5:45 | `team-governance-dashboard.png` | Budget controls and usage visibility |
| 7:15 | `three-layer-stack.png` | Complete 3-layer optimization stack |

## Tags

GitHub Copilot, AI Credits, usage-based billing, PRU retirement, model selection, model routing, Lightweight Versatile Powerful, task taxonomy, RouteLLM, AI code assistant, developer productivity, context engineering, prompt engineering, team governance, AI team leads, AI cost optimization
