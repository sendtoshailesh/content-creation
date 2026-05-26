# Substack Post — Part 3: Model Selection

> Platform: Substack
> Post type: Substack Note (NOT newsletter/email — ambient feed only)
> Word count: ~460 words (excerpt only — avoid duplicate content penalty)
> Canonical source: https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html

── START COPY ──

On June 1, 2026, GitHub Copilot retires Premium Request Units (PRUs) and switches to **[token-metered GitHub AI Credits](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)**. One AI Credit equals $0.01 USD. Every request is billed by tokens consumed.

A short Lightweight chat reply costs about $0.001. A deep agent-mode session on a Powerful model can cost $0.45. That is roughly a 450x per-request cost spread — and now it shows up on your bill in real dollars.

Most developers I talk to either ignore this (defaulting to the most capable model for everything) or overcorrect (restricting teams to the cheapest option). Neither is right.

[Apple ML Research](https://machinelearning.apple.com/research/illusion-of-thinking) found that reasoning models burn thousands of extra tokens on simple tasks — with zero quality improvement. Standard models actually delivered better accuracy on low-complexity items. The expensive model is not always the better choice, even if money is no object.

---

GitHub's [official model categories](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) — Lightweight, Versatile, Powerful — map cleanly to a three-tier task taxonomy:

**Lightweight (60-70% of daily interactions)**: variable renaming, boilerplate generation, test scaffolding, docstring writing, simple syntax questions. Lightweight models (per-1M-token rates around $0.20-$1.50 input, $1.25-$9 output) handle these with no quality loss.

**Versatile (20-30%)**: code review, multi-function refactoring, debugging with stack traces, architecture questions. Versatile models deliver the best quality-per-dollar ratio here.

**Powerful (5-10%)**: multi-file refactoring with complex dependencies, novel algorithm implementation, system design with competing constraints. Per-1M-token output rates of $10-$30 — only worth it where the answer quality genuinely warrants it.

If you route 100 daily requests by complexity (65 Lightweight at ~$0.001, 25 Versatile at ~$0.04, 10 Powerful at ~$0.30), your daily model cost is about **$4.07** — compared to ~$30 if you ran everything through a Powerful model. That is roughly 86% reduction while *using a more capable model for your hardest tasks*.

Production validation: [RouteLLM](https://lmsys.org/blog/2024-07-01-routellm/) achieved 95% of flagship-model quality using only 14% flagship calls. *(In the 2024 LMSYS paper, "flagship" refers to GPT-4 as the baseline at publication time.)* [CascadeFlow](https://arxiv.org/abs/2406.00073): 69% savings with 96% quality retention. One team profiled by [Towards Data Science](https://towardsdatascience.com/inference-scaling-test-time-compute-why-reasoning-models-raise-your-compute-bill/) dropped from $3,000/day to $970/day — 68% reduction, $740K/year annualized — through routing alone.

*(Specific model examples in this post — names, per-token rates, category mapping — are accurate as of May 2026 and will rotate. The Lightweight / Versatile / Powerful taxonomy is the durable framework.)*

---

For AI team leads and decision-makers: the billing change is not just a cost story. It is the first time you have granular visibility into AI tool consumption patterns — credits per developer, per project, per model. Annual Pro/Pro+ subscribers stay on PRU multipliers until plan expiry; everyone else moves to AI Credits on June 1.

The most important governance decision is not which models to allow. It is whether to invest in context engineering training or model restrictions. AI team leads who teach their teams context engineering get the cost reduction *and* better output quality. The ones who restrict model access get frustrated workarounds.

Invest in the skill. The savings follow.

---

Full breakdown with task taxonomy reference, per-1M-token pricing table, and team governance framework: https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html

Full series: https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html

── END COPY ──
