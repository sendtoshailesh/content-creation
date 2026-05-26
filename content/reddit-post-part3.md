# Reddit Post — Part 3: From PRUs to AI Credits

## Subreddit Title Variants

- **r/ExperiencedDevs**: "GitHub Copilot is retiring PRUs on June 1 — token-based billing means a ~450x per-request cost spread. Here's a category-based routing framework."
- **r/programming**: "PRUs are out, GitHub AI Credits are in (June 1, 2026). A short Lightweight chat costs $0.001; a Powerful agent session can cost $0.45 — same UI, very different bill."
- **r/MachineLearning**: "[D] Apple ML Research found reasoning models perform worse than standard models on simple coding tasks — implications for model routing under usage-based billing"

---

## Post Body (r/ExperiencedDevs)

── START COPY ──

**TL;DR**: GitHub Copilot's billing changes June 1, 2026: PRUs (with 0.25x/1x/3x/30x multipliers) are retired and replaced by [token-metered AI Credits](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) (1 credit = $0.01 USD). A short Lightweight reply costs ~$0.001; a deep Powerful agent session can cost ~$0.45 — a ~450x per-request spread. [Apple ML Research](https://machinelearning.apple.com/research/illusion-of-thinking) found expensive reasoning models perform worse than standard models on simple tasks. A category-based routing taxonomy (Lightweight/Versatile/Powerful) cuts model costs ~85% with zero quality loss. [RouteLLM](https://lmsys.org/blog/2024-07-01-routellm/) validated this at scale.

---

I have been working through the implications of GitHub's billing change and wanted to share the routing framework that came out of it.

**The change**: On June 1, 2026, Premium Request Units (PRUs) are gone. Token-metered AI Credits take over. Every model is now categorized as [Lightweight, Versatile, or Powerful](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) with per-1M-token input/output rates that vary by roughly 20x across categories. Add the typical token-volume difference between a quick chat and an agent-mode session and you get a ~450x per-request cost spread. *(Annual Pro/Pro+ subscribers stay on PRU multipliers until plan expiry; everyone else moves to AI Credits automatically.)*

**What the research says**: [Apple ML Research](https://machinelearning.apple.com/research/illusion-of-thinking) found that reasoning models burn thousands of extra tokens on simple tasks with zero quality improvement. Standard models actually provided better accuracy on low-complexity items. "Always use the best model" is bad advice, not just expensive advice.

**The 3-category taxonomy that works**:

- **Lightweight (60-70% of daily interactions)**: Variable renaming, boilerplate, test scaffolding, docstrings, linting. Per-1M-token rates ~$0.20-$1.50 input / ~$1.25-$9 output. *(May 2026 examples: GPT-5 mini, GPT-5.4 nano, Gemini 3.5 Flash.)*

- **Versatile (20-30%)**: Code review, refactoring, debugging with stack traces, architecture questions. ~$1-$3 input / ~$5-$15 output per 1M tokens. Best quality-per-dollar bucket. *(May 2026 examples: Claude Sonnet 4.x, GPT-4.1, GPT-5.4, Claude Haiku 4.5.)*

- **Powerful (5-10%)**: Multi-file refactoring, system design, novel algorithms, deep agent-mode sessions. ~$1.25-$5 input / ~$10-$30 output per 1M tokens. Reserve for cases where the answer quality genuinely warrants it. *(May 2026 examples: Claude Opus 4.x, GPT-5.5, Gemini 2.5 Pro.)*

**The math in dollars** (100 daily requests, realistic mix):

- 65 Lightweight at ~$0.001 = $0.065/day
- 25 Versatile at ~$0.04 = $1.00/day
- 10 Powerful at ~$0.30 = $3.00/day
- **Daily total: ~$4.07** — compared to ~$30/day if you ran everything Powerful

Plan allowances: Pro $10/mo, Pro+ $39/mo, Business $19/user/mo, Enterprise $39/user/mo (matching the subscription fee). Promotional bump June-August: Business $30/user, Enterprise $70/user. Code completions and Next Edit suggestions remain unmetered.

**Production validation**:

- [RouteLLM (LMSYS, 2024)](https://lmsys.org/blog/2024-07-01-routellm/): 95% flagship-model quality using only 14% flagship calls — 75% cost reduction. *(The paper's "GPT-4" was the 2024 baseline; the routing principle generalizes to whatever the current Powerful model is.)*
- [CascadeFlow (arXiv, 2024)](https://arxiv.org/abs/2406.00073): 69% savings with 96% quality retention
- A coding team profiled by [Towards Data Science](https://towardsdatascience.com/inference-scaling-test-time-compute-why-reasoning-models-raise-your-compute-bill/): $3,000/day -> $970/day (68% reduction, $740K/year annualized) through routing alone

**For teams**: This is the first time you'll have granular AI consumption data — credits per developer, per project, per model. If you are an AI team lead or decision-maker, document your task taxonomy before June 1 and set budget alerts at 50/75/90% of the **standard** allowance (not the promotional ceiling).

This is Part 3 of a series. Part 1 covered context engineering (50-85% fewer tokens, better output). Part 2 covered prompt caching (~10x cheaper than fresh input on most models) and retry-tax elimination. Layered together, you can comfortably stay inside Pro's $10/month credit allowance for typical individual use.

Full writeup with per-1M-token pricing table and governance framework: https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html

Curious how others are thinking about routing with the change. Anyone already doing category-based routing on their team?

── END COPY ──
