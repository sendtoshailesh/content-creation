# Reddit Post — Model Selection Field Guide

> Reddit supports native Markdown. Use **bold**, *italic*, headers, and bullet lists.
> Do NOT use Unicode bold/italic (that's for LinkedIn/Twitter only).
> Tone: conversational, technically credible, anti-promotional.

---

## Suggested Subreddits & Titles

**r/MachineLearning:**
> [D] We cut inference costs 66% by stopping "just use the best model" — here's our framework

**r/ExperiencedDevs:**
> We burned $140K in 60 days on AI inference before we figured out model selection is a product decision, not a technical one

**r/artificial:**
> Why "which AI model is best?" is the wrong question — a field guide for teams shipping AI in production

**r/LocalLLaMA:**
> How tiered model routing (lightweight + mid + frontier) saved us $27K/month and improved latency 65%

---

## Post Body

**TL;DR:** Most teams pick one AI model and use it for everything. That's how you burn $140K in 60 days. The fix: treat model selection as an ongoing product decision, score tasks across 7 dimensions, and build a tiered model portfolio with routing rules. One of my customers went from $41K→$14K/month (−66%) and 5.1s→1.8s latency (−65%) by switching from single-model to tiered routing. Framework, case study, and 30-day playbook below.

---

### The mistake I keep seeing

While working with one of my customers, I saw them standardize on a frontier model across their entire product — autocomplete, email drafts, spam classification, the works.

The demos were great. Production was not:

- **4.2s latency** on autocomplete. Users literally typed over the AI suggestions.
- **$47K/month** inference bill — 3× their projected budget. Most of it was grammar corrections that a $0.15/M-token model could handle.
- **No fallback.** When their provider had a 40-minute degradation, the entire product went down.

Nothing catastrophically failed. It just became impossible to scale.

And this isn't a one-off. a16z's 2025 AI survey found **over 60% of teams using LLMs in production have switched their primary model at least once**, with a median time-to-switch of 4.5 months. The "pick GPT-4 and forget about it" era is over.

### The mindset shift

Teams that scale AI don't ask "which model is best?" — they ask "which model is best *for this task*?"

That's the difference between model monogamy and a model portfolio. Most products have 4–6 distinct AI task types. Using one model for all of them is like using a chef's knife for everything in the kitchen.

### The 7-dimension framework

Every AI task should be scored across:

1. **Task fit** — classify/extract vs. draft vs. reason vs. generate code. Each has different capability requirements.
2. **Quality bar** — defined in business terms, not vibes. "Good enough" for internal draft suggestions ≠ "good enough" for customer-facing support.
3. **Latency budget** — autocomplete needs <300ms, chat needs <2s TTFT, long-form can tolerate 8s. A frontier model averaging 3.8s on a 300ms task isn't "higher quality" — it's a UX regression.
4. **Cost envelope** — and I mean the *real* cost. Your actual inference bill is typically 1.5–2.5× the sticker price once you factor in verbose system prompts, retry loops, guardrail passes, and RAG context bloat.
5. **Data sensitivity** — map your data to three zones (public, internal, regulated) and pre-approve providers per zone. This prevents last-minute compliance blockers.
6. **Integration complexity** — structured output reliability, tool/function calling, streaming, SDK maturity, version pinning. A model that benchmarks well can still be expensive in eng time.
7. **Operational reliability** — historical uptime, degradation behavior, fallback paths, circuit breakers. Run your eval suite at 2 AM and 2 PM on the same day — if quality variance exceeds 10%, you have a reliability problem.

Miss any one of these and you're rewriting your pipeline within 90 days.

### The tier cheat sheet (2026 pricing)

Approximate per 1M tokens, input/output blended:

| Tier | Models | Cost Range | Best For |
|---|---|---|---|
| **Lightweight** | Haiku, Gemini Flash, GPT-4o mini | $0.10–$0.60 | Classification, extraction, triage |
| **Mid-tier** | Sonnet 3.5, GPT-4o, Gemini Pro | $2–$15 | Drafting, chat, general reasoning |
| **Frontier** | Opus, o1/o3, Gemini Ultra | $15–$60+ | Complex analysis, multi-step reasoning |

### The case study

One of my customers — a B2B SaaS company — launched an AI copilot for sales teams with three features: meeting summaries, email drafts, and deal-risk analysis. They standardized on Claude 3 Opus for everything.

What broke after 4 weeks:

- Email drafting hit **5.1s p95 latency** during peak hours (Opus throughput limits)
- Meeting summaries cost **$28K/month** for a feature users rated "nice to have"
- Deal-risk analysis had unpredictable cost spikes on quarter-end

They applied the framework and shifted to tiered routing:

- **Haiku** → meeting summary extraction
- **Sonnet 3.5** → email drafts (default), with confidence-based escalation to Opus
- **Opus** → deal-risk analysis only

Plus: automatic fallback, graceful degradation, and weekly cost-quality review.

**Results after 8 weeks:**

| Metric | Before | After | Change |
|---|---|---|---|
| Monthly cost | $41K | $14K | **−66%** |
| Email draft p95 latency | 5.1s | 1.8s | **−65%** |
| Meeting summary satisfaction | 3.8/5 | 4.1/5 | +8% |
| Deal-risk accuracy | 82% | 84% | +2% |

Quality stable or better across the board. The core pattern: **they stopped chasing "best model" and built a model portfolio with explicit routing rules.**

### The 30-day playbook

You can run this with any cross-functional team:

- **Week 1:** Define top 3–5 AI tasks, write quality rubrics (10 test prompts, 1–5 scoring), set latency budgets, define cost ceilings, map data sensitivity zones.
- **Week 2:** Evaluate 2–4 candidates (not 10+ — that's analysis paralysis). Same prompt set, same rubric, measure quality + p95 latency + cost per 100 requests.
- **Week 3:** Shadow deploy at 5–10% of real traffic. Monitor user-facing outcomes (completion rates, edit rates), not just API metrics. Keep fallback active.
- **Week 4:** Finalize task-to-model routing map, assign ownership, document swap triggers, set review cadence (weekly first month, biweekly after).

### The checklist (before you lock any model into production)

If you can't answer "yes" to at least 7 of these, your decision is premature:

- [ ] Task-specific quality thresholds with scoring rubric?
- [ ] Maximum acceptable latency per interaction pattern?
- [ ] Cost modeled under baseline, peak, and growth scenarios?
- [ ] Data handling validated per compliance zone?
- [ ] Fallback and escalation paths that activate automatically?
- [ ] Tested with representative prompts AND adversarial edge cases?
- [ ] Clear ownership for monitoring, tuning, and re-evaluation?
- [ ] Specific trigger points for model replacement or rerouting?

### The readiness test

If your model strategy has no explicit *downgrade path* (for when you're overspending) and no explicit *escalation path* (for when quality falls short), it's not ready for production scale.

---

I wrote this up as a longer field guide with all the diagrams, comparison matrices, and the full case study breakdown. Happy to share the link if anyone's interested — but mainly curious what frameworks or approaches others are using.

**What's your team running — single model or portfolio? What made you switch (or not)?**

---

## Posting Notes

- **Tone:** The post is written to feel like a practitioner sharing experience, not a marketer pushing content. The blog link is offered passively ("happy to share if interested") — this performs better on Reddit than a direct link.
- **If comments ask for the link**, reply with: `https://shailesh0.substack.com/publish/post/190276894`
- **Engage with comments.** Reddit rewards OPs who respond substantively. Have the framework details fresh so you can answer technical follow-ups.
- **Best time to post:** Weekdays 9–11 AM EST (peak Reddit traffic for technical subs)
- **Flair:** Use [D] (Discussion) flair on r/MachineLearning; no flair needed on other subs.
- **Cross-posting:** Post to one sub first. If it gains traction (>50 upvotes), cross-post to others after 24 hours. Don't spam all subs simultaneously.
