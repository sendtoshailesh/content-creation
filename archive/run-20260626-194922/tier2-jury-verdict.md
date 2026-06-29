# Tier 2 Jury Verdict — content/from-prompts-to-loop-engineering.md

> Run 2026-06-23 (loop-engineering, merged single post). The Tier 1 desk returned `GATE: FAIL → escalate` on two high-risk-class claim-citation Warnings (W1 SWE-bench freshness, W2 OpenAI 403 indirect). Panel-of-LLM-judges (PoLL): three **disjoint** jurors vote independently on the escalated residue only; a moderator reconciles. No juror sees another's ballot before voting.

## Panel composition (disjoint roles)

| Juror | Lens | Scope | Cannot rule on |
|-------|------|-------|----------------|
| J1 — Rubber-duck / local reader | "Would a working developer be misled reading this as written?" | In-text hedging, comprehension | External source liveness |
| J2 — Fact-check desk | "Does each cited number/attribution survive the two-source rule?" | Source liveness, attribution accuracy | Tone / persona |
| J3 — Brand / tone | "Does the hedging read as honest practitioner voice, not legalese?" | Voice, framing of caveats | Numeric accuracy |

## Ballots

### W1 — SWE-bench figures (12.47%→76.8%, $0.05–$0.96), §"Proof at scale"

| Juror | Vote | Reason |
|-------|------|--------|
| J1 | approve | Reader is explicitly told the numbers are a "snapshot, not a forecast" and to "cite with dataset date and re-pull." Not misleading as written. |
| J2 | escalate | Numbers are model-specific and move monthly; trend-research flags re-pull at publish. Verified now, but liveness is a publish-time obligation, not a draft-time one. |
| J3 | approve | "the first sign that the loop has an economics problem worth taking seriously" reads as honest practitioner candor, not hype. |

**Spread: approve / escalate / approve → majority approve, one escalate.** Residual: publish-time re-pull.

### W2 — OpenAI "environments, feedback loops, and control systems", §"Why now"

| Juror | Vote | Reason |
|-------|------|--------|
| J1 | approve | Attribution is hedged in-text as "as cited by Böckeler" — reader is not told OpenAI said it directly to us. Defensible. |
| J2 | escalate | Primary URL (`openai.com/index/harness-engineering/`) returned HTTP 403; corroborated by two independent sources but not re-fetched this run. |
| J3 | approve | The indirect framing is the honest move; restoring a direct quote would over-claim. |

**Spread: approve / escalate / approve → majority approve, one escalate.** Residual: publish-time re-pull of the 403 URL.

## Moderator reconciliation

- Both items carry the **same shape**: content is *defensible as written today* (hedged + dataset-dated), with a **single deferred obligation** — a publish-time source re-pull. No juror found a draft-time error requiring a content change.
- Vote spread is narrow (2 approve / 1 escalate on each item), but the lone escalate is a *liveness* concern, not a *correctness* one. Per the gate rule, any escalate vote on a high-risk class item forwards the residue to Tier 3 rather than auto-clearing.
- No new findings surfaced beyond the two Tier 1 Warnings. Rubric dimensions (voice, structure, data density) were unanimously clean and not re-litigated.

## Verdict

- W1: **approve-with-residual** (publish-time SWE-bench/pricing re-pull)
- W2: **approve-with-residual** (publish-time OpenAI 403 re-pull)

GATE: FAIL
DECISION: escalate (2 rows, both approve-with-residual → Tier 3 digest)
