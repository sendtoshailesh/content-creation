# Substack Post — Part 2: Caching and Workflow

> Platform: Substack
> Post type: Substack Note (NOT newsletter/email — ambient feed only)
> Word count: ~390 words (excerpt only — avoid duplicate content penalty)
> Canonical source: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

── START COPY ──

A developer making 100 AI requests per day spends roughly 90% of those tokens on context that is identical across every request.

Same system prompt. Same copilot-instructions file. Same active file. Only the question changes.

Without caching, that repeated prefix costs full price 100 times. With caching, it costs full price once and 10% of full price for the remaining 99 requests. The math: roughly 89% reduction on prefix token cost.

GitHub Copilot's published rates make this concrete. GPT-4.1: $2.00/MTok regular vs. $0.50/MTok cached (75% off). Claude Sonnet 4.6: $3.00/MTok vs. $0.30/MTok cached (90% off). These are not future discounts — they are live today in the pricing documentation.

The catch: caching is automatic, but you can accidentally break it.

Every time you edit your copilot-instructions.md mid-session, the prefix invalidates. Every time you switch threads, the shared prefix resets. Every time you add and remove files from context repeatedly, portions of the cache fragment. The five context engineering practices from Part 1 protect the cache by keeping the prefix stable.

---

The second layer in Part 2 is the retry tax — a cost most developers never think to track.

If 40% of your AI code assistant requests need a follow-up clarification or correction, your effective token spend is 1.4x your baseline. At 50% retry rate: 1.5x. Retries are full-price requests that produced zero usable output.

Most developers operate in the 30-50% retry range without realizing it. Every vague prompt, every "try again," every follow-up that adds context you should have included originally — that is the retry tax compounding.

The fix is not to use a better model. The fix is to diagnose before retrying. Was the context insufficient? Was the prompt ambiguous? Fix the root cause. A targeted follow-up costs fewer tokens and produces better results than a blind retry. First-attempt accuracy is the most effective cost optimization.

---

These two layers — caching and retry elimination — compound silently across every session. No ongoing effort after setup. Just structural habits that accumulate savings.

Full breakdown with per-request math and five retry-reduction disciplines: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

── END COPY ──
