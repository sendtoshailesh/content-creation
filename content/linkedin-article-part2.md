# LinkedIn Article — Part 2: Engineering Discipline as Cost Strategy

> Platform: LinkedIn Article (Google-indexed, no canonical protection)
> Angle: UNIQUE — "Engineering discipline as invisible infrastructure" (tech lead / senior dev culture angle)
> NOT a republish of the blog — different frame, different entry point
> Word count: ~760 words
> Canonical blog: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

── START COPY ──

# The AI Cost Savings That Happen While You Sleep

The best cost optimizations are the ones that run in the background after a one-time setup. You configure them once. They compound across every interaction thereafter. You do not feel them in a single prompt. But over a week, a month, a quarter — the cumulative effect is substantial.

I have been working with engineering teams on GitHub Copilot optimization ahead of the June 1, 2026 usage-based billing change. The practices that deliver the most durable value are not the dramatic interventions — they are the boring structural habits that compound silently.

---

## Prompt Caching: The 90% Discount You Have Not Claimed

Here is what most developers do not know: under GitHub Copilot's usage-based billing, cached input tokens are charged at 75-90% less than regular input tokens.

And here is what most developers do not realize: roughly 90% of your AI prompt context is identical across every request in a working session.

Your system prompt does not change between prompts. Your .github/copilot-instructions.md is the same. The active file you are editing is the same. Only your specific question varies.

Which means that 90% of your input — the stable prefix — can be cached. When it is, you pay a fraction of the full rate for it.

The math for 100 requests per day with a 10,000-token stable prefix:
- Without caching: 1,000,000 prefix tokens at full rate
- With caching: approximately 109,000 tokens at effective rate
- Net savings on prefix cost: roughly 89%

By request 10, the prefix is essentially free. By request 100, you have saved the equivalent of 890,000 tokens worth of billing on prefix context alone.

---

## The Engineering Discipline Connection

Here is what matters for tech leads and senior engineers: you are already doing the behaviors that enable caching, if you are writing clean code.

Keeping your copilot-instructions.md stable — not editing it mid-session — preserves the prefix and keeps the cache warm. This is the same discipline as not modifying shared interfaces mid-sprint.

Grouping related questions in the same thread — not starting fresh for every question — extends the shared prefix across the session. This is the same discipline as maintaining context in a long pull request review rather than reopening closed comments.

Structuring context with stable elements first (instructions, then file content, then query) maximizes the cacheable prefix length. This is the same discipline as organizing function arguments from general to specific.

The five context engineering practices from Part 1 of my series are prerequisites for effective caching — because clean context is cacheable context. When you close irrelevant files, the prefix shrinks to only relevant content that stays stable across related prompts. The quality improvement and the cost reduction are the same action.

---

## The Retry Tax: The Cost Your Team Is Not Measuring

Caching reduces the cost of good requests. Workflow discipline reduces the number of bad requests. The combination is multiplicative.

If 40% of your team's AI code assistant requests need a follow-up clarification or correction, your effective token spend is 1.4x your baseline. At 50% retry rate: 1.5x. Most developers operate in the 30-50% retry range without realizing it.

The instinct when a response is wrong is to type "try again" or "that's not what I meant." The better discipline: stop and diagnose. Was the context insufficient? Was the prompt ambiguous? Did the model have conflicting signals from open files? Fix the root cause. A targeted follow-up costs fewer tokens and produces better results.

The framing that changes how teams think about this: measure cost per successful task, not cost per request. A $0.01 request that requires three retries costs $0.04 and produces one result. A $0.02 request that succeeds first attempt costs half as much for the same outcome. First-attempt accuracy is the most effective cost optimization — and it is entirely within the developer's control.

---

## What "Set and Forget" Actually Looks Like

The practices in Part 2 of my series share a property: once set up, they compound silently across every AI interaction. No ongoing effort. No per-prompt decisions.

Create or stabilize your copilot-instructions file. Stay in threads for related work. Structure context with stable elements first. Diagnose bad responses before retrying.

Each habit pays forward into every subsequent interaction. That is the invisible infrastructure of cost-effective AI development — not model restrictions, not credit caps, but discipline that makes every request better.

For the full data, per-request math, and five retry-reduction disciplines: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

── END COPY ──
