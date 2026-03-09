# X/Twitter Thread — Model Selection Field Guide (Unicode Formatted)

> X/Twitter renders Unicode bold/italic natively. Copy each tweet between
> the ── markers and paste directly into the composer or Typefully/Buffer.
> Attach `visuals/tradeoff-2x2.png` to Tweet 1 or Tweet 5.

---

## Standalone Single-Tweet Summary

── START ──

Most teams pick 𝗢𝗡𝗘 AI model and use it for everything.

Top teams build a 𝗺𝗼𝗱𝗲𝗹 𝗽𝗼𝗿𝘁𝗳𝗼𝗹𝗶𝗼 — routing each task to the right tier.

One of my customers cut inference costs 𝟲𝟲% ($41K → $14K/mo) and latency 𝟲𝟱% by matching lightweight, mid-tier, and frontier models to task complexity.

Full field guide ↓
https://shailesh0.substack.com/publish/post/190276894

── END ──

---

## Tweet 1 / Hook

── START ──

One of my customers 𝗯𝘂𝗿𝗻𝗲𝗱 $𝟭𝟰𝟬𝗞 𝗶𝗻 𝗔𝗜 𝗶𝗻𝗳𝗲𝗿𝗲𝗻𝗰𝗲 𝗰𝗼𝘀𝘁𝘀 in 60 days.

They didn't pick a bad model.
They picked 𝗢𝗡𝗘 model for everything.

Here's the framework top teams use to build 𝗺𝗼𝗱𝗲𝗹 𝗽𝗼𝗿𝘁𝗳𝗼𝗹𝗶𝗼𝘀 instead 🧵👇

── END ──

---

## Tweet 2 / The Problem

── START ──

They used a frontier model for autocomplete, email drafts, 𝗔𝗡𝗗 spam classification.

Result:
⚠️ 𝟰.𝟮𝘀 latency on autocomplete — users typed over it
⚠️ 𝟯× budget overrun
⚠️ 40-min provider outage = 𝗲𝗻𝘁𝗶𝗿𝗲 𝗽𝗿𝗼𝗱𝘂𝗰𝘁 𝗱𝗼𝘄𝗻

The "best model" was the worst decision.

── END ──

---

## Tweet 3 / The Shift

── START ──

Teams that scale AI don't ask "which model is best?"

They ask: "which model is best 𝗙𝗢𝗥 𝗧𝗛𝗜𝗦 𝗧𝗔𝗦𝗞?"

That's the difference between 𝘮𝘰𝘥𝘦𝘭 𝘮𝘰𝘯𝘰𝘨𝘢𝘮𝘺 and a 𝗺𝗼𝗱𝗲𝗹 𝗽𝗼𝗿𝘁𝗳𝗼𝗹𝗶𝗼.

Here's how to build one ↓

── END ──

---

## Tweet 4 / The Framework

── START ──

Score every AI task across 𝟳 𝗱𝗶𝗺𝗲𝗻𝘀𝗶𝗼𝗻𝘀:

𝟭. Task fit
𝟮. Quality bar
𝟯. Latency budget
𝟰. Cost envelope
𝟱. Data sensitivity
𝟲. Integration complexity
𝟳. Operational reliability

Miss any one → you're rewriting your pipeline in 90 days.

── END ──

---

## Tweet 5 / Model Tiers

── START ──

𝗖𝗵𝗲𝗮𝘁 𝘀𝗵𝗲𝗲𝘁 — 2026 pricing per 1M tokens:

🟢 𝗟𝗶𝗴𝗵𝘁𝘄𝗲𝗶𝗴𝗵𝘁 (Haiku, Flash): $0.10–$0.60
    ▸ classification, extraction, triage

🔵 𝗠𝗶𝗱-𝘁𝗶𝗲𝗿 (Sonnet, GPT-4o): $2–$15
    ▸ drafting, chat, reasoning

🔴 𝗙𝗿𝗼𝗻𝘁𝗶𝗲𝗿 (Opus, o3): $15–$60+
    ▸ complex analysis 𝘰𝘯𝘭𝘺

── END ──

---

## Tweet 6 / Hidden Costs

── START ──

Your 𝗥𝗘𝗔𝗟 inference cost is 𝟭.𝟱–𝟮.𝟱× the sticker price.

Hidden multipliers:
▸ Verbose system prompts (2K+ tokens each)
▸ Retry loops on low-confidence outputs
▸ Guardrail/eval passes (second model call)
▸ Context bloat from RAG

𝗕𝘂𝗱𝗴𝗲𝘁 𝗳𝗼𝗿 𝗿𝗲𝗮𝗹𝗶𝘁𝘆, 𝗻𝗼𝘁 𝗱𝗲𝗺𝗼𝘀.

── END ──

---

## Tweet 7 / The Case Study

── START ──

One of my customers went from single-model to 𝘁𝗶𝗲𝗿𝗲𝗱 𝗿𝗼𝘂𝘁𝗶𝗻𝗴:

▸ Haiku → meeting summaries
▸ Sonnet → email drafts (escalate to Opus)
▸ Opus → deal-risk analysis 𝘰𝘯𝘭𝘺

📊 𝗥𝗲𝘀𝘂𝗹𝘁𝘀:
    $41K → $14K/mo  (−𝟲𝟲%)
    5.1s → 1.8s       (−𝟲𝟱%)
    Quality: 𝘀𝘁𝗮𝗯𝗹𝗲 or better

── END ──

---

## Tweet 8 / Latency Truth

── START ──

𝗟𝗮𝘁𝗲𝗻𝗰𝘆 𝗯𝘂𝗱𝗴𝗲𝘁𝘀 most teams ignore:

▸ Autocomplete: < 300ms
▸ Chat response: < 2s TTFT
▸ Long-form gen: < 8s
▸ Background batch: minutes

A frontier model averaging 𝟯.𝟴𝘀 on a 300ms task isn't "higher quality."

𝘐𝘵'𝘴 𝘢 𝘜𝘟 𝘳𝘦𝘨𝘳𝘦𝘴𝘴𝘪𝘰𝘯.

── END ──

---

## Tweet 9 / Routing Pattern

── START ──

𝗧𝗵𝗲 𝗮𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲 𝘁𝗵𝗮𝘁 𝘄𝗼𝗿𝗸𝘀:

Request → Task classifier → Route to tier

▸ Low complexity → lightweight
▸ Medium → mid-tier
▸ High stakes → frontier

Add:
✓ Confidence-based escalation
✓ Automatic fallback on provider issues
✓ Weekly cost-quality review

── END ──

---

## Tweet 10 / 30-Day Playbook

── START ──

You can run this in 𝟯𝟬 𝗱𝗮𝘆𝘀:

𝗪𝗸 𝟭: Define tasks + quality rubrics + latency budgets
𝗪𝗸 𝟮: Evaluate 2–4 candidates (𝘯𝘰𝘵 10+)
𝗪𝗸 𝟯: Shadow deploy at 5–10% traffic
𝗪𝗸 𝟰: Finalize routing + assign ownership + set swap triggers

No excuses. 𝗦𝘁𝗮𝗿𝘁 𝗠𝗼𝗻𝗱𝗮𝘆.

── END ──

---

## Tweet 11 / CTA

── START ──

I wrote a 𝗳𝘂𝗹𝗹 𝗳𝗶𝗲𝗹𝗱 𝗴𝘂𝗶𝗱𝗲 covering:

✦ 7-dimension selection framework
✦ Cost benchmarks across all tiers
✦ Before/after case study
✦ 30-day playbook with exit criteria
✦ Pre-launch checklist

📖 Read it here → https://shailesh0.substack.com/publish/post/190276894

── END ──

---

## Tweet 12 / Engagement Close

── START ──

What's your team running — single model or portfolio?

Drop your stack in the replies.

Genuinely curious what's working at scale 👇

── END ──

---

### Thread posting notes

- **Format:** Copy text between ── START ── and ── END ── for each tweet. Unicode bold (𝗯𝗼𝗹𝗱) and italic (𝘪𝘵𝘢𝘭𝘪𝘤) render natively on X — no Markdown needed.
- **Total tweets:** 12 (optimal length for engagement without drop-off)
- **Attach image to:** Tweet 1 (hook) or Tweet 5 (tiers cheat sheet) — use `visuals/tradeoff-2x2.png`
- **Best time to post:** Weekdays 12–1 PM or 5–6 PM ET
- **Self-reply cadence:** Post all 12 within 2–3 minutes for thread coherence, or schedule via Typefully/Buffer
- **Pin:** Tweet 1 to profile after posting
- **Quote-tweet:** Tweet 7 (case study results) as a standalone highlight the next day for extra reach
