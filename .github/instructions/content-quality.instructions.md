---
description: "Use when writing or editing blog posts, social posts, or video scripts. Enforces content quality standards including data specificity, tone, and structure."
applyTo: "content/**/*.md"
---

# Content Quality Standards

## Data Specificity

- Every claim must include a concrete number, model name, or benchmark
- Use real pricing data (per-1M-token costs from provider pricing pages)
- Case studies require before/after metrics (cost, latency, accuracy)
- Reference specific model names: GPT-4o, Claude Opus/Sonnet/Haiku, Gemini, Llama 3, Mistral

## Volatile Data and Caveats

- When citing provider pricing, model availability, multipliers, or feature access, check if the source says "subject to change", "in preview", or "may change"
- If it does, include a caveat in the content: "as of [date]", "currently", or "at the time of writing — GitHub notes this is subject to change"
- Never present volatile pricing or feature data as permanent facts
- Never build the primary CTA on data tagged `[VOLATILE]` without acknowledging the risk — always provide a fallback recommendation that works even if the data changes
- When a content strategy depends on a specific pricing tier (e.g., "free models"), include a "what if this changes" paragraph with the alternative strategy

## Structure Requirements

- Blog posts: hook, framework, tier breakdown, case study, playbook, checklist
- Social posts: story hook opening, NOT "I wrote a blog"
- All content ends with a clear call-to-action

## Tone

- First-person: "sharing my learnings working with customers"
- Conversational but data-driven
- Never corporate/fundraising framing
- Lead with problems and insights
