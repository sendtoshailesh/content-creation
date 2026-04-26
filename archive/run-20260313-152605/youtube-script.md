# YouTube Script — Which AI Model Should You Use, and When?

> **Target length:** 10–12 minutes
> **Tone:** Conversational expert sharing learnings from real customer work
> **Visual assets:** Use existing PNGs from `content/visuals/` as slides
> **Pace:** ~150 words/minute spoken

---

## THUMBNAIL CONCEPTS

**Option A:** Text: "STOP using ONE model" | Background: tradeoff-2x2.png | Your face with surprised/pointing expression
**Option B:** Text: "$140K WASTED" | Red arrow down | Cost comparison graphic from case study
**Option C:** Text: "AI Model Tier List" | 🟢🔵🔴 tier badges | Model logos (Haiku, GPT-4o, Opus)

---

## TITLE OPTIONS

1. Which AI Model Should You Actually Use? (A Field Guide)
2. Stop Using One AI Model for Everything — Here's Why
3. How One Team Cut AI Costs 66% With This Simple Framework
4. The AI Model Selection Framework Every Team Needs

---

## SCRIPT

---

### [0:00–0:30] HOOK — Cold Open

**[ON CAMERA — direct to camera, no intro]**

> While working with one of my customers recently, I watched them burn through $140K in AI inference costs in just 60 days.
>
> And here's the thing — they didn't pick a bad model. They picked ONE model for everything.
>
> By the end of this video, you'll have the exact framework I now use with all my customers to build model portfolios instead of model monogamy. And I'll show you a real case study where this cut costs by 66%.
>
> Let's get into it.

**[SLIDE: title card with video title]**

*(~80 words, ~30 seconds)*

---

### [0:30–2:00] THE PROBLEM — Why "Best Model" Fails

**[ON CAMERA → cut to SLIDE: decision-funnel.png]**

> So here's what happened with that customer. They were building an AI writing assistant — autocomplete, email drafts, grammar correction. They chose GPT-4 Turbo for everything. The demos looked incredible. Leadership was thrilled.
>
> Then real usage hit.

**[SLIDE: bullet points appearing one at a time]**

> First — p95 latency hit 4.2 seconds on autocomplete. Users literally typed over the AI suggestions. That's not "higher quality." That's a UX regression.
>
> Second — monthly inference cost reached $47K. Three times the projected budget. Most of it was grammar corrections that a 15-cent-per-million-token model could handle.
>
> Third — when their provider had a 40-minute degradation, the entire product went down. No fallback. Single point of failure.

**[ON CAMERA]**

> Nothing catastrophically failed. But the product became impossible to scale. And this isn't just one team — a16z's 2025 AI survey found over 60% of teams using LLMs in production have switched their primary model at least once. The "pick GPT-4 and forget about it" era is over.

*(~200 words, ~80 seconds)*

---

### [2:00–2:45] THE MINDSET SHIFT

**[ON CAMERA]**

> The teams I see succeeding at AI in production don't ask "which model is best?" They ask "which model is best FOR THIS TASK?"
>
> That's the fundamental shift — from model monogamy to a model portfolio.

**[SLIDE: model-selection-framework.png]**

> Think about it. Most products have 4 to 6 distinct AI task types. Classification, extraction, drafting, complex reasoning, code generation, maybe some multimodal stuff. Using one model for all of them is like using a chef's knife for everything in the kitchen. Technically possible. Practically expensive.
>
> So how do you actually evaluate which model goes where? I use a 7-dimension framework.

*(~120 words, ~45 seconds)*

---

### [2:45–5:30] THE 7-DIMENSION FRAMEWORK

**[SLIDE: model-selection-framework.png — keep on screen, highlight each dimension as discussed]**

> Every AI task in your product should be scored across these 7 dimensions. Let me walk through each one.

**Dimension 1: Task Fit**

> Start with the job, not the model. Classification needs speed and consistency — use a lightweight model. Drafting needs fluency — mid-tier. Complex multi-step reasoning — that's where frontier models earn their price.

**[SLIDE: task fit table from blog]**

**Dimension 2: Quality Bar**

> Define "good enough" in business terms, not vibes. Customer-facing support responses? Error tolerance near zero. Internal draft suggestions? Minor imprecision is fine if it's fast.
>
> Pro tip — create a 10-prompt evaluation set per task. Score outputs 1 to 5 across accuracy, completeness, tone, and format. Takes 2 hours. Saves weeks of debate.

**Dimension 3: Latency Budget**

**[SLIDE: latency table]**

> This one catches teams off guard. Autocomplete needs under 300 milliseconds. Chat needs under 2 seconds to first token. And a frontier model averaging 3.8 seconds on a 300ms task isn't "higher quality" — it's a UX regression. Your users feel delay long before your dashboards alert you.

**Dimension 4: Cost Envelope**

**[SLIDE: comparison-matrix.png]**

> Here's what the pricing landscape looks like right now.
>
> Lightweight models — Haiku, Gemini Flash, GPT-4o mini — 10 cents to 60 cents per million tokens.
> Mid-tier — Sonnet, GPT-4o, Gemini Pro — $2 to $15.
> Frontier — Opus, o3, Gemini Ultra — $15 to over $60.
>
> But here's the thing most teams miss — your REAL cost is typically 1.5 to 2.5x the sticker price. Why? Verbose system prompts, retry loops, guardrail passes that call a second model, and context bloat from RAG. Budget for reality, not demos.

**Dimension 5: Data Sensitivity**

> This one often eliminates options before you even benchmark. Map your data to three zones — public, internal, and regulated. Pre-approve providers for each zone. If user PII enters prompts, check data processing agreements. If you're HIPAA or GDPR, the list gets short fast.

**Dimension 6: Integration Complexity**

> A model that benchmarks well can still be expensive in engineering time. Does it reliably return structured JSON? How's the tool calling? Is streaming solid? Can you pin a specific model version? These things matter more than benchmark scores when you're shipping features.

**Dimension 7: Operational Reliability**

> You're selecting for day-2 operations, not demo day. What does provider degradation look like? Can you route to a backup transparently? Do you have circuit breakers?
>
> Here's a test most teams skip — run your eval suite at 2 AM and 2 PM on the same day. If quality variance exceeds 10%, you have a reliability problem.

**[ON CAMERA]**

> Miss any one of these seven dimensions and you'll be rewriting your pipeline in 90 days. I've seen it happen.

*(~450 words, ~3 minutes)*

---

### [5:30–6:15] TIER CHEAT SHEET

**[SLIDE: tradeoff-2x2.png]**

> Let me give you a quick visual. This 2x2 maps quality versus cost across model tiers.
>
> Top-right — frontier. Maximum capability, maximum cost. Reserve for high-stakes tasks only.
> Center — mid-tier. The workhorse zone. Best balance for most features.
> Bottom-left — lightweight. High efficiency, limited ceiling. Perfect for classification, extraction, triage.
> And bottom-right is the danger zone — low quality AND high cost. That's usually a sign of model misfit or prompt engineering debt.

**[ON CAMERA]**

> The goal isn't to use the cheapest model everywhere. It's to use the RIGHT model for each task. That's the portfolio approach.

*(~120 words, ~45 seconds)*

---

### [6:15–8:30] CASE STUDY — The Transformation

**[ON CAMERA]**

> Let me show you what this looks like in practice with a real customer engagement.

**[SLIDE: case-timeline.png]**

> One of my customers — a B2B SaaS company — launched an AI copilot for sales account teams. Three features: meeting summary generation, email drafts, and deal-risk signal analysis. They standardized on Claude 3 Opus for everything.

**[SLIDE: "What Broke" — bullet points]**

> By week 4, the cracks showed.
>
> Email drafting hit 5.1 seconds p95 latency during peak hours. Opus throughput limits under load.
> Meeting summaries were costing $28K a month — for a feature users rated "nice to have."
> Deal-risk analysis had unpredictable cost spikes on quarter-end.
>
> The model performed well. The single-model-for-everything strategy was the failure.

**[SLIDE: model-routing-flow.png]**

> We applied the 7-dimension framework and shifted to tiered routing.
>
> Haiku for meeting summary extraction — fast, cheap, perfectly adequate.
> Sonnet 3.5 as the default for email drafts, with confidence-based escalation to Opus for complex threads.
> Opus reserved ONLY for deal-risk analysis.
>
> Plus — automatic fallback, graceful degradation when a provider is slow, and a weekly cost-quality review.

**[SLIDE: results table — animated reveal]**

> The results after 8 weeks:
>
> Monthly cost: $41K down to $14K. That's 66% reduction.
> Email draft latency: 5.1 seconds down to 1.8 seconds. 65% faster.
> Meeting summary satisfaction went UP — from 3.8 to 4.1 out of 5 — because faster delivery.
> Deal-risk accuracy actually improved 2 points — because Opus was focused on what it does best instead of being stretched across everything.

**[ON CAMERA — lean in]**

> Same team. Same product. Same users. Just smarter model routing. That's the power of a portfolio approach.

*(~280 words, ~2 minutes)*

---

### [8:30–10:00] THE 30-DAY PLAYBOOK

**[ON CAMERA]**

> You can run this yourself in 30 days. Here's the playbook.

**[SLIDE: swimlane-30day.png]**

> **Week 1** — define the decision frame. List your top 3 to 5 AI tasks. Write quality rubrics — 10 test prompts, score 1 to 5. Set latency budgets per interaction type. Define cost ceilings. Map data sensitivity zones. Exit with a one-page decision brief that product, engineering, and leadership sign off on.

> **Week 2** — run controlled evaluations. Test 2 to 4 candidates — not 10 plus, that's analysis paralysis. Same prompt set, same rubric, across all candidates. Measure quality, p95 latency, and cost per 100 requests. Put it in a spreadsheet, not Slack threads.

> **Week 3** — pilot with guardrails. Route 5 to 10% of real traffic to the candidate model. Monitor USER-facing outcomes — completion rates, edit rates, satisfaction — not just API metrics. Keep fallback active. Run for at least 5 business days.

> **Week 4** — operationalize. Finalize the task-to-model routing map. Assign ownership — who monitors quality? Who approves swaps? Document the specific trigger points for when you'd re-evaluate. Set review cadence — weekly the first month, biweekly after.

*(~200 words, ~80 seconds)*

---

### [10:00–10:45] PRE-LAUNCH CHECKLIST

**[SLIDE: checklist-card.png]**

> Before you lock any model into production, run through this checklist. If you can't answer "yes" to at least 7 of these 8, your decision is premature.

**[Read through checklist — each item appears on screen as spoken]**

> One — task-specific quality thresholds with a scoring rubric?
> Two — maximum acceptable latency per interaction pattern?
> Three — cost modeled under baseline, peak, AND growth scenarios?
> Four — data handling validated per compliance zone?
> Five — fallback and escalation paths that activate automatically?
> Six — tested with representative prompts AND adversarial edge cases?
> Seven — clear ownership for monitoring, tuning, and re-evaluation?
> Eight — specific trigger points for model replacement or rerouting?

*(~120 words, ~45 seconds)*

---

### [10:45–11:30] CLOSING + CTA

**[ON CAMERA — direct, confident]**

> Model selection is no longer a one-time technical pick. It's an ongoing product capability — as important as your deployment pipeline or your monitoring stack.
>
> The teams that win at AI in production share three traits: they treat model choice as a structured, repeatable decision. They build portfolios, not monogamy. And they measure continuously — because the landscape shifts every quarter.
>
> I wrote a full field guide with all the details — the complete framework, cost benchmarks, the full case study, the 30-day playbook, and the checklist. Link is in the description.

**[Point down / gesture to description]**

> Start with the playbook. Run one focused comparison cycle. Document your first routing strategy. Your second decision will be sharper than your first.
>
> If this was useful, hit subscribe — I share practical AI engineering content from real customer work, not hype.
>
> Drop in the comments — are you running single model or portfolio? What made you switch?

**[END CARD: subscribe + link to field guide]**

*(~170 words, ~70 seconds)*

---

## TOTAL RUNTIME

| Section | Duration | Cumulative |
|---|---|---|
| Hook | 0:30 | 0:30 |
| The Problem | 1:30 | 2:00 |
| Mindset Shift | 0:45 | 2:45 |
| 7-Dimension Framework | 2:45 | 5:30 |
| Tier Cheat Sheet | 0:45 | 6:15 |
| Case Study | 2:15 | 8:30 |
| 30-Day Playbook | 1:30 | 10:00 |
| Pre-Launch Checklist | 0:45 | 10:45 |
| Closing + CTA | 0:45 | 11:30 |

**Total: ~11:30** (within 10–12 min target)

---

## SLIDE MAP — Which Visual Asset Per Section

| Timestamp | Visual | File |
|---|---|---|
| 0:30 | Title card | (create in Canva/Figma) |
| 0:45 | Decision funnel | `visuals/decision-funnel.png` |
| 2:00 | Selection framework | `visuals/model-selection-framework.png` |
| 2:45 | Selection framework (keep) | `visuals/model-selection-framework.png` |
| 3:30 | Latency table | (text overlay or `visuals/comparison-matrix.png`) |
| 4:00 | Comparison matrix | `visuals/comparison-matrix.png` |
| 5:30 | Trade-off 2×2 | `visuals/tradeoff-2x2.png` |
| 6:15 | Case timeline | `visuals/case-timeline.png` |
| 7:00 | Routing flow | `visuals/model-routing-flow.png` |
| 7:45 | Results table | (text overlay or extract from blog) |
| 8:30 | 30-day swimlane | `visuals/swimlane-30day.png` |
| 10:00 | Checklist card | `visuals/checklist-card.png` |
| 10:45 | End card | (create in Canva/Figma) |

---

## DESCRIPTION BOX (copy-paste ready)

Which AI model should you actually use — and when should you switch?

Most teams pick one AI model and use it for everything. That's how you burn $140K in 60 days. In this video, I share the 7-dimension framework I use with my customers to build model portfolios — matching the right model to each task.

Includes a real case study: one customer cut costs 66% ($41K → $14K/mo) and improved latency 65% by switching from single-model to tiered routing.

📖 Read the full field guide: https://shailesh0.substack.com/publish/post/190276894

⏱️ Timestamps:
0:00 — The $140K mistake
0:30 — Why "best model" fails
2:00 — The mindset shift
2:45 — 7-Dimension Framework
5:30 — Tier cheat sheet
6:15 — Case study (66% cost reduction)
8:30 — 30-day playbook
10:00 — Pre-launch checklist
10:45 — Next steps

#AIEngineering #LLM #ModelSelection #MachineLearning #GenAI #ProductEngineering
