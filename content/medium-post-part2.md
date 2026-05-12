# Medium Post — Part 2: Caching and Workflow

> Platform: Medium
> Import URL: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html
> Action: Use Medium's Import tool (Settings > Import a story) — do NOT paste. This preserves canonical attribution to GitHub Pages.
> Word count: ~820 words

── START COPY ──

# The Invisible Savings in Your AI Code Assistant: Caching and Workflow Discipline

Here is something most developers do not know: under GitHub Copilot's usage-based billing (effective June 1, 2026), cached input tokens are charged at 75-90% less than regular input tokens.

And here is the thing most developers do not realize: roughly 90% of your AI prompt context is identical across every request in a working session.

Your system prompt doesn't change between prompts. Your copilot-instructions.md is the same. The active file you're editing is the same. Only your specific question varies. Which means that 90% of your input — the stable prefix — can be cached. And when it is, you pay a fraction of the full rate for it.

I've been tracking this as GitHub Copilot teams move to usage-based billing, and the math is striking. Let me show you.

---

## The Caching Math

Suppose your stable prefix is 10,000 tokens — a reasonable estimate for system prompt plus copilot-instructions plus active file context. Over 100 requests in a day:

Without caching: 10,000 x 100 = 1,000,000 prefix tokens at full rate.
With caching: 10,000 (first request) + 10,000 x 99 x 0.1 (90% cached) = 109,000 tokens at effective rate.

That's roughly 89% reduction on your prefix token cost. By request 10, the prefix is essentially free. By request 100, you have saved roughly 890,000 tokens worth of billing on prefix context alone.

The specific rates from GitHub's published pricing: GPT-4.1 charges $0.50/MTok for cached input vs. $2.00/MTok for regular input (75% off). GPT-5 mini: $0.025/MTok cached vs. $0.25/MTok regular (90% off). Claude Sonnet 4.6: $0.30/MTok cached vs. $3.00/MTok regular (90% off).

---

## How to Maximize Cache Hits

The good news: prefix caching is largely automatic. You don't need to configure it. What you need to do is avoid destroying it.

Keep your copilot-instructions file stable. If you edit it mid-session, the prefix changes, the cache invalidates, and the next request pays full price for a new cache write. Write your instructions file once. Update it when your tech stack changes — not per task.

Group related questions in the same thread. Each message in a thread extends the shared prefix. Switching threads resets the prefix. If you're working through a multi-step feature, stay in one thread rather than starting fresh for each question.

Structure context with stable elements first: system prompt, then project instructions, then file content, then your specific query. This ordering maximizes the prefix length that remains constant across requests.

Here is the connection to Part 1: the five context engineering practices enable better caching. When you close irrelevant files, you shrink the prefix to only relevant content — content that stays stable across related prompts. When you maintain a clean copilot-instructions file, that file becomes a consistent, cacheable prefix. Clean context is cacheable context.

---

## The Retry Tax: The Cost You're Not Tracking

Caching reduces the cost of good requests. Workflow discipline reduces the number of bad requests. The combination is multiplicative.

The retry tax is the cost most developers never see: if 40% of your AI code assistant requests need a follow-up clarification or correction, your effective token spend is 1.4x your baseline. At 50% retry rate, it's 1.5x. Retries are the most expensive form of wasted tokens because they represent full-price requests that produced zero usable output.

The math by retry rate:
- 0% retry: 1.0x effective cost
- 20% retry: 1.2x effective cost
- 40% retry: 1.4x effective cost
- 60% retry: 1.6x effective cost

Most developers operate in the 30-50% retry range without realizing it. Every vague prompt, every "try again," every follow-up that adds context you should have included originally — that is the retry tax.

Five disciplines that reduce retries: (1) one task per prompt, (2) diagnose before retrying (fix the root cause, not the symptom), (3) use structured commit messages that become better AI context later, (4) maintain clean project structure so the model can infer architecture, (5) measure cost per successful task, not cost per request.

The last point matters most. A $0.01 request that requires three retries costs $0.04 and produces one result. A $0.02 request that succeeds first attempt costs half as much for the same outcome. First-attempt accuracy is the most effective cost optimization.

---

## What This Looks Like Together

The two layers of Part 2 — caching and retry elimination — compound with the five context engineering practices from Part 1. Clean context enables caching. Good prompts eliminate retries. Each layer amplifies the others.

Part 3 adds the third layer: matching the model to the task. There is a 120x cost difference between GitHub Copilot's cheapest and most expensive models. The question is not "which model is best" but "which model is right for this task."

Full article with data tables and detailed retry reduction framework: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

── END COPY ──
