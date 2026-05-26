# YouTube Script — Part 3: Model Selection + The 120x Spread

## Video Details

- **Target duration**: 8-10 minutes
- **Topic**: The 120x Spread — Model Selection, Task Taxonomy, and Team Governance
- **Source blog**: `content/ai-code-assistant-cost-part-3.md`
- **Published URL**: `https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html`

## Title Options

1. The 120x Cost Spread in GitHub Copilot: A Model Selection Guide (Part 3)
2. Stop Defaulting to the Expensive Model — Task Routing for AI Code Assistants
3. GitHub Copilot Model Multipliers: When to Use 0.25x vs 30x (Data-Backed)
4. AI Coding Costs Part 3: The Task Taxonomy That Cuts Spend by 68%

## Description

── START COPY ──

GitHub Copilot's cheapest model tier costs 0.25x. The most expensive: 30x. That's a 120x cost spread — and under usage-based billing (June 1, 2026), every model choice hits your budget.

In this video:
- Why the expensive tier isn't always better (Apple ML Research data)
- The 3-tier task taxonomy for matching tier to complexity
- The cost math: 0.55x weighted average with 45% savings
- RouteLLM: 95% flagship-tier quality at 75% lower cost
- Team governance playbook for AI team leads and decision-makers
- The complete 3-layer optimization stack from this series

TIMESTAMPS:
0:00 - The 120x problem
0:45 - Why the expensive tier fails on simple tasks
2:00 - 3-tier task taxonomy
3:30 - The cost math (0.55x weighted average)
4:30 - RouteLLM and smart routing evidence
5:45 - Team governance for AI team leads and decision-makers
7:15 - The complete 3-layer playbook (series recap)
8:30 - Action plan + what to do before June 1
9:30 - Close

Part 3 of 3 in the "Engineering Better AI Code Assistant Interactions" series.

Blog post: https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html
Series index: https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html

SOURCES (verify the ground rules):
- Apple ML Research, "The Illusion of Thinking": https://machinelearning.apple.com/research/illusion-of-thinking
- RouteLLM (LMSYS, 2024): https://lmsys.org/blog/2024-07-01-routellm/
- CascadeFlow (arXiv, 2024): https://arxiv.org/abs/2406.00073
- GitHub Copilot billing docs: https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests
- GitHub usage-based billing announcement: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
- Towards Data Science production case study: https://towardsdatascience.com/inference-scaling-test-time-compute-why-reasoning-models-raise-your-compute-bill/

Note: Specific model names mentioned in this video (e.g., GPT-5.4 nano at 0.25x, Claude Opus 4.6 fast mode at 30x) are accurate as of May 2026. Model lineups rotate; the multiplier tier structure is the durable framework.

#ModelRouting #GitHubCopilot #AIEngineering #DeveloperProductivity #ContextEngineering

── END COPY ──

## Thumbnail Concepts

1. **Giant number**: "120x" in bold white on dark background with "cost spread" subtitle — matches the blog hero visual
2. **Split comparison**: Budget tier (0.25x, green) vs flagship fast-mode tier (30x, red) side by side
3. **Three-tier columns**: Simple/Moderate/Complex stacked vertically with multiplier badges — clean taxonomy visual

## Script

### [0:00 - 0:45] Cold Open

**SLIDE**: `task-model-alignment.png`
**SCRIPT**: Zero-point-two-five x versus thirty x. That is a 120x cost difference between GitHub Copilot's cheapest budget tier and its most expensive flagship fast-mode tier. Starting June 1, 2026, every model choice lands on your bill. But here is what most people get wrong — the expensive tier is not always the better choice. Apple ML Research found that reasoning models actually perform worse than standard models on simple tasks, while burning thousands of extra tokens. Today I will show you exactly when to use each tier. The source links for everything I cite are in the description.
**NOTES**: Punch the "120x" number hard. Pause after the Apple ML Research finding — it is counterintuitive and hooks attention. Mention the description-link callout once at the top so viewers know where to verify.

### [0:45 - 2:00] Why the Expensive Tier Fails on Simple Tasks

**SLIDE**: `routing-decision-comparison.png`
**SCRIPT**: Let me explain the research. Apple ML Research tested reasoning models against standard models on low-complexity coding tasks — variable renaming, docstrings, import fixes. The reasoning models burned thousands of extra tokens on internal chain-of-thought. And the result? Zero quality improvement. On some benchmarks, the standard model was actually more accurate. The full paper from Apple ML Research is linked in the description. This is not about saving money. This is about using the right tool for the right job.
**NOTES**: Emphasize that this is a quality argument, not just a cost argument. The research shows the expensive tier can be genuinely worse on simple work.

### [2:00 - 3:30] The 3-Tier Task Taxonomy

**SLIDE**: `task-model-alignment.png`
**SCRIPT**: The research and production data converge on three tiers. Tier 1: simple tasks. Variable renaming, boilerplate generation, test scaffolding, doc writing. These are 60 to 70% of daily interactions. Use the included tier at 0x or the budget tier at 0.25x. Tier 2: moderate tasks. Code review, refactoring, debugging with stack trace correlation. 20 to 30% of interactions. The standard 1x tier — as of recording, that includes Claude Sonnet, Gemini Pro, and GPT-5.2 — gives the best quality per credit. The specific model names will rotate over time; the tier structure is what matters. Tier 3: complex tasks. Multi-file refactoring, system design, agent-mode sessions. Only 5 to 10% of interactions. This is where the premium reasoning tier at 3x genuinely outperforms. Reserve 7.5x and above for exceptional cases with a specific, articulable reason.
**NOTES**: Use the visual to walk through each tier. Point at the percentage breakdowns. This is the core framework of the video.

### [3:30 - 4:30] The Cost Math

**SLIDE**: `team-optimization-strategies.png`
**SCRIPT**: Let us run the numbers for 100 requests per day. 65% simple at 0x: zero weighted cost. 25% moderate at 1x: 0.25 weighted. 10% complex at 3x: 0.30 weighted. Total: 0.55x weighted average. Compared to using a 1x model for everything, that is 45% savings — while using a more expensive model for the hardest tasks. You are not downgrading. You are matching capability to need.
**NOTES**: Walk through the math on screen. The 0.55x result should feel surprising — you spend more on hard tasks but save overall.

### [4:30 - 5:45] RouteLLM and Production Evidence

**SLIDE**: `routing-decision-comparison.png`
**SCRIPT**: This is not just theory. RouteLLM from LMSYS achieved 95% of the flagship-tier quality while using the flagship for only 14% of calls — a 75% cost reduction. In the original RouteLLM paper, the flagship was GPT-4 as the 2024 baseline; the principle generalizes to whatever the current flagship is. CascadeFlow delivered 69% savings with 96% quality retention. And a real coding team profiled by Towards Data Science dropped from $3,000 per day to $970 per day — 68% reduction, $740,000 annualized — through model routing alone. All three sources are linked in the description. The pattern is consistent: smart routing preserves quality while cutting costs dramatically.
**NOTES**: These are the credibility numbers. Cite them clearly. The $3K to $970 case study is the most compelling for practitioners.

### [5:45 - 7:15] Team Governance for AI Team Leads and Decision-Makers

**SLIDE**: `team-governance-dashboard.png`
**SCRIPT**: If you are an AI team lead or decision-maker for a team on GitHub Copilot Business or Enterprise, the billing change introduces governance tools that did not exist before. Pooled credits shared across organizations instead of siloed per user. Budget controls at enterprise, cost center, and user levels. Usage visibility showing which developers, projects, and model tiers consume the most credits. Four actions before June 1. First, document your team's task taxonomy and recommended tier per task type — put it in your team wiki and your copilot-instructions file. Second, set budget alerts at 50, 75, and 90% of your allocation before the first bill. Third, review top-consuming projects monthly — agent-mode sessions are valuable but expensive. Fourth, invest in context engineering training, not model restrictions. AI team leads who restrict model access create frustration and workarounds. AI team leads who teach context engineering get the same savings with happier developers.
**NOTES**: This section speaks directly to AI team leads and decision-makers. Slow down on the four recommendations — these are the actionable takeaways.

### [7:15 - 8:30] The Complete 3-Layer Playbook (Series Recap)

**SLIDE**: `three-layer-stack.png`
**SCRIPT**: This is Part 3 of 3, and the three parts describe a compound optimization stack. Layer 1 from Part 1: context engineering. Give AI better input. 50 to 85% token reduction with quality improvements from three independent research studies. Layer 2 from Part 2: caching and workflow discipline. Avoid paying repeatedly for good input. 75 to 90% reduced rate on repeated context. Retry elimination cuts effective spend by 20 to 60%. Layer 3 from Part 3: model selection. Match model capability to task complexity. 45 to 75% reduction in model costs without quality loss. Combined potential across all three layers: 70 to 90% effective cost reduction with equal or better output quality.
**NOTES**: This is the series capstone. Walk through each layer with the visual. The compound effect is the key message.

### [8:30 - 9:30] Action Plan + What to Do Before June 1

**SCRIPT**: Here is your action plan. This week: switch your default model to the included tier or the cheapest one available in your plan. Enable auto-selection for a 10% multiplier discount. Document your task taxonomy: which tasks are simple, moderate, and complex for your team. Before June 1: set budget alerts, review your team's model usage patterns, and share Part 1 of this series with anyone who prompts AI code assistants without thinking about context. Start with context engineering. Everything else compounds on top of it.
**NOTES**: Keep the action items crisp. End with the "start with context" message that ties the whole series together.

### [9:30 - 10:00] Close

**SCRIPT**: The full 3-part blog series and every research source I cited today are linked in the description, along with the model multiplier table and task taxonomy reference card. If your team is navigating this billing change, share this video with your AI team lead or decision-maker — the governance section was written for them. See you in the comments.
**NOTES**: Direct CTA to share. Mention the description links twice — once for the series, once for sources.

## Slide Map

| Timestamp | Visual | Description |
|-----------|--------|-------------|
| 0:00 | `task-model-alignment.png` | 3-tier task taxonomy with model assignments |
| 0:45 | `routing-decision-comparison.png` | Manual vs auto routing comparison |
| 2:00 | `task-model-alignment.png` | Walk through each tier in detail |
| 3:30 | `team-optimization-strategies.png` | Cost math and weighted average |
| 4:30 | `routing-decision-comparison.png` | RouteLLM and production evidence |
| 5:45 | `team-governance-dashboard.png` | Budget controls and usage visibility |
| 7:15 | `three-layer-stack.png` | Complete 3-layer optimization stack |

## Tags

GitHub Copilot, model selection, AI coding costs, usage-based billing, model routing, task taxonomy, RouteLLM, AI code assistant, developer productivity, context engineering, prompt engineering, model multipliers, team governance, AI team leads, AI cost optimization
