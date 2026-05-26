# Reddit Post — Part 3: Model Selection + The 120x Spread

## Subreddit Title Variants

- **r/ExperiencedDevs**: "The 120x cost spread in GitHub Copilot models — a task taxonomy for matching model to complexity"
- **r/programming**: "There's a 120x cost difference between GitHub Copilot's cheapest and most expensive model. Here's how to route by task complexity."
- **r/MachineLearning**: "[D] Apple ML Research found reasoning models perform worse than standard models on simple coding tasks — implications for model routing"

---

## Post Body (r/ExperiencedDevs)

── START COPY ──

**TL;DR**: GitHub Copilot's usage-based billing (June 1, 2026) introduces model multipliers from 0.25x to 30x — a 120x spread. Apple ML Research found expensive reasoning models perform worse than standard models on simple tasks. A 3-tier task taxonomy (simple/moderate/complex) cuts model costs 45-68% with zero quality loss. RouteLLM validated this at scale: 95% GPT-4 quality using only 14% GPT-4 calls.

---

I've been working through the implications of GitHub Copilot's billing change (flat-rate -> consumption-based, effective June 1, 2026) and wanted to share the model selection framework that came out of it.

**The problem**: Under the new billing, every model carries a multiplier. GPT-5.4 nano is 0.25x. Claude Opus 4.6 fast mode is 30x. Most developers either default to the most capable model for everything (expensive) or get restricted to the cheapest by their org (quality-destroying).

**What the research says**: Apple ML Research found that reasoning models burn thousands of extra tokens on simple tasks with zero quality improvement. Standard models actually provided better accuracy on low-complexity items. So "always use the best model" is genuinely bad advice, not just expensive advice.

**The 3-tier taxonomy that works**:

- **Simple (60-70% of daily interactions)**: Variable renaming, boilerplate, test scaffolding, docstrings, linting. Use included (0x) or budget (0.25x) models. Premium adds nothing measurable here.

- **Moderate (20-30%)**: Code review, refactoring, debugging with stack traces, architecture questions. The 1x tier (Claude Sonnet 4.5/4.6, Gemini 2.5 Pro, GPT-5.2) hits the sweet spot.

- **Complex (5-10%)**: Multi-file refactoring, system design, agent-mode sessions with constraint satisfaction. This is where 3x models genuinely outperform. Reserve 7.5x+ for cases where you can articulate why.

**The math**: 65% simple @ 0x + 25% moderate @ 1x + 10% complex @ 3x = 0.55x weighted average. That's 45% savings vs. using 1x for everything, while using a *more* expensive model for hard tasks.

**Production validation**:

- RouteLLM (LMSYS, 2024): 95% GPT-4 quality using only 14% GPT-4 calls — 75% cost reduction
- CascadeFlow (2024): 69% savings with 96% quality retention
- A coding team profiled by TDS: $3,000/day -> $970/day (68% reduction, $740K/year annualized) through routing alone

**For teams**: Usage-based billing introduces pooled credits, budget controls at enterprise/user levels, and usage visibility by developer and project. If you manage a team, document your task taxonomy before June 1 and set budget alerts at 50/75/90%.

This is Part 3 of a series. Part 1 covered context engineering (85% fewer tokens, better output). Part 2 covered prompt caching (75-90% savings on repeated context) and retry-tax elimination.

Full writeup with multiplier table and governance framework: https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html

Curious how others are thinking about model routing with the billing change. Anyone already doing task-based routing on their team?

── END COPY ──
