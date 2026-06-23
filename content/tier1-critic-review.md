## Tier 1 Critic Review — content/from-prompts-to-loop-engineering.md

> Run 2026-06-23 (loop-engineering, merged single post). Constitution: `content-quality.instructions.md` + `writing-style.instructions.md`. Grounding corpus: `content/reference-brief.md` + `content/trend-research.md`. Tier 0 preflight cleared (0 Error / 0 Warning) before this desk ran.

### Phase 1 — Rubric critic (G-Eval, constitution as steps)

| Dimension | Verdict | Rationale |
|-----------|---------|-----------|
| Data specificity | Pass | Every load-bearing section carries a concrete number/name/date (65% in ~100 lines; 12.47%→76.8%; $0.05–$0.96; 1,300+ PRs/week; $1T+). |
| Concrete numbers | Pass | No placeholder figures; all numerics trace to trend-research data points. |
| Tone / voice | Pass | First-person practitioner throughout ("what I keep seeing when I sit with teams"); no corporate/hype framing. |
| Structure | Pass | One staircase through-line across 10 sections; hook → arc → payoff → honest limits → CTA. |
| Banned voice | Pass | No "leverage" or other banned terms (confirmed by Tier 0 preflight after the final-paragraph fix). |

No rubric deviations recorded.

### Phase 2 — Fact-check desk (reference-grounded, two-source rule)

15 load-bearing claims extracted and grounded against `trend-research.md` §3 data table:

| Claim | Grounded source | Match | Verdict |
|-------|-----------------|-------|---------|
| Validation, not generation, is the bottleneck | DP#11, CircleCI via InfoQ (Jun 2026) | yes | Pass |
| CircleCI "AI agent has already moved on, losing valuable context" (quote) | Source 5 (verified quote) | yes | Pass |
| mini-SWE-agent 65% in ~100 lines Python | DP#6 (Jul 2025) | yes | Pass |
| SWE-bench Verified = 500 human-filtered instances, fixed harness | DP#7 | yes | Pass |
| Böckeler "everything except the model" (Feb 2026) | Source 8 (17 Feb 2026) | yes | Pass |
| Context engineering, Böckeler (Feb 2026) | Source 11 (05 Feb 2026) | yes | Pass |
| Willison agent "runs tools in a loop"; "designing agentic loops" new skill; Claude Code Feb 2025 | Source 1 (Sep 2025) | yes | Pass |
| Anthropic evaluator-optimizer + stop condition quote (Dec 2024) | Source 3 | yes | Pass |
| Böckeler "guides and sensors" (paraphrased, not quoted) | Source 10 | yes | Pass |
| Morris why/how loops, outer/middle/inner, four postures (Mar 2026) | Source 2 | yes | Pass |
| Stripe 1,300+ PRs/week (up from ~1,000), zero human-written code, $1T+ | DP#1/#2/#14 (Mar 2026) | yes | Pass |
| SWE-bench 12.47% (Mar 2024) → 76.8% Claude 4.5 Opus (Feb 2026); ~6x | DP#4/#5 | yes | Pass (12.47→76.8 = 6.16x) |
| Per-task cost ~$0.05–$0.96 / instance | DP#8 (Feb 2026) | yes | Pass — see Warning W1 (freshness) |
| Failure modes: agentic laziness, self-preferential bias, goal drift | DP#10, Anthropic via InfoQ (Jun 2026) | yes | Pass |
| Pricing "still very subsidized" (Böckeler, flagged as opinion) | DP#12 (opinion, flagged) | yes | Pass |
| OpenAI "designing environments, feedback loops, and control systems" (as cited by Böckeler) | DP#9, Source 8/13 | indirect (403) | Pass — see Warning W2 (indirect) |

### Findings

| Severity | Category | Asset / location | Finding | Required fix | Confidence | Risk | Source signal |
|----------|----------|------------------|---------|--------------|------------|------|---------------|
| Warning (W1) | claim-citation | §"Proof at scale: Stripe Minions and the SWE-bench trajectory" | SWE-bench figures (12.47%→76.8%, $0.05–$0.96) are model-specific and move monthly | Re-pull at publish; dataset date (Feb 2026) already attached in-text | high | high | reference-grounded (freshness caveat) |
| Warning (W2) | claim-citation | §"Why now: validation, not generation, is the bottleneck" | OpenAI "environments, feedback loops, and control systems" rests on a primary URL that 403'd; verified indirectly via Böckeler | Re-pull `openai.com/index/harness-engineering/` at publish; already hedged as "as cited by Böckeler" | high | high | indirect (403, corroborated) |

Both Warnings are already mitigated in-text (dataset date attached; attribution hedged). They are high-risk *class* (benchmark numbers + named-org attribution), so per the routing rule they are carried to the jury rather than auto-approved. Zero Errors. No fabricated or unsupported claims found; the Part 2 additions (Stripe, Morris, CircleCI, Anthropic failure modes, pricing) all ground to Verified data points.

GATE: FAIL
ABSTAIN: no
DECISION: escalate
