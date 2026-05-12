# Medium Post — Part 3: Model Selection

> Platform: Medium
> Import URL: https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html
> Action: Use Medium's Import tool (Settings > Import a story) — do NOT paste. This preserves canonical attribution to GitHub Pages.
> Word count: ~850 words

── START COPY ──

# The 120x Spread: A Developer's Guide to GitHub Copilot Model Selection

Under GitHub Copilot's usage-based billing (effective June 1, 2026), every model carries a multiplier. GPT-5.4 nano: 0.25x. Claude Opus 4.6 fast mode: 30x. That is a 120x cost difference for the same interaction pattern.

But this is not a "use cheap models" story. This is a "understand when expensive models add genuine value" story. Because here is what the research shows: Apple ML Research found that reasoning models burn thousands of extra tokens on simple tasks — with zero quality improvement. Standard models actually provided better accuracy on low-complexity items. The expensive model is not always the better choice, even if money is no object.

Having spent time working with engineering teams navigating this billing change, I see two failure modes: defaulting to the most capable model for everything (expensive, often worse on simple tasks), and restricting teams to the cheapest model for everything (cost-effective, quality-destroying). The answer is a task taxonomy.

---

## Three Tiers of Task Complexity

The research and production data converge on a simple three-tier model.

**Tier 1: Simple tasks — 60-70% of daily interactions**

Variable renaming. Boilerplate generation. Test scaffolding. Docstring writing. Import fixing. Linting explanations. Simple API usage questions.

These tasks require pattern matching and recall, not multi-step reasoning. Premium models add no measurable quality here. At current pricing, included models (GPT-4.1, GPT-4o on paid plans) handle this at 0x — no additional credits. Even if included models change, budget-tier models (GPT-5.4 nano at 0.25x, Claude Haiku 4.5 at 0.33x) deliver equivalent results at a fraction of premium cost.

**Tier 2: Moderate tasks — 20-30% of daily interactions**

Code review with contextual understanding. Refactoring suggestions spanning multiple functions. Debugging assistance that requires correlating stack traces with code. Architecture questions. Multi-file reasoning where the model needs to understand relationships between components.

These tasks benefit from stronger reasoning but don't require frontier capability. The 1x multiplier tier offers the best quality-per-credit ratio here: Claude Sonnet 4.5/4.6, Gemini 2.5 Pro, GPT-5.2.

**Tier 3: Complex tasks — 5-10% of daily interactions**

Multi-file refactoring with complex dependency chains. Novel algorithm implementation. System design with constraint satisfaction across performance, security, and maintainability. Deep architectural reasoning.

These are the only tasks where premium models demonstrably outperform standard models. Use them deliberately. Claude Opus 4.5 (3x) for genuinely complex work. Reserve the 7.5x+ tier for exceptional cases where you have a specific, articulable reason.

---

## The Cost Math

If a developer makes 100 AI requests per day and routes by task complexity:

- Simple (65% of requests, included/0x): $0.00
- Moderate (25% of requests, 1x): 0.25x weighted contribution
- Complex (10% of requests, 3x): 0.30x weighted contribution
- Effective average multiplier: 0.55x

Compared to using a 1x model for everything, routing by task complexity cuts model costs by 45% — while using a more expensive model for the hardest tasks. You are not downgrading. You are matching capability to need.

The production case study that validates this at scale: RouteLLM achieved 95% of GPT-4 quality using only 14% GPT-4 calls. CascadeFlow delivered 69% savings with 96% quality retention. A coding team profiled by TDS dropped from $3,000/day to $970/day (68% reduction, $740K/year annualized) through routing alone.

---

## For Engineering Managers: The Team Governance Angle

If you manage a team of 5-20 developers on GitHub Copilot Business or Enterprise, the billing change introduces governance visibility that didn't exist before.

New capabilities under usage-based billing: pooled credits shared across organizations rather than siloed per user; budget controls at enterprise, cost center, and user levels; usage visibility that shows which developers, projects, and models consume the most credits.

Four recommended actions for engineering managers before June 1:

First, document your team's task taxonomy (simple/moderate/complex) and recommended models for each tier. Put it in your team wiki and in your .github/copilot-instructions.md.

Second, set budget alerts at 50%, 75%, and 90% of your credit allocation — before the first bill. Business plans include $19 credits/user ($30/month promotional June-August). Enterprise: $39/user ($70/month promotional).

Third, review top-consuming projects monthly. High consumption often comes from agent-mode sessions — valuable but expensive. Ensure these run with clean context and caching-friendly structure.

Fourth, invest in context engineering training, not model restrictions. The managers who restrict model access create frustration and workarounds. The managers who teach context engineering get the same cost reduction — or better — with happier developers.

---

## The Complete Three-Layer Playbook

The three parts of this series describe an optimization stack that compounds multiplicatively:

Layer 1 (Part 1): Context engineering — give AI better input. 50-85% token reduction, with quality improvements from independent research.
Layer 2 (Part 2): Caching and workflow discipline — avoid paying repeatedly for good input. 75-90% reduced rate on repeated context; retry elimination cuts effective spend by 20-60%.
Layer 3 (Part 3): Model selection — match model capability to task complexity. 45-75% reduction in model costs without quality loss.

Combined potential across all three layers: 70-90% effective cost reduction with equal or better output quality. Start with context engineering. Everything else compounds on top of it.

Full article with model multiplier table, task taxonomy reference, and governance framework: https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html

Series index: https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html

── END COPY ──
