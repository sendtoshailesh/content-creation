# Escalation Digest — run 2026-06-23 (loop-engineering, merged single post)

> The human edits **exceptions only**. Everything not listed here was auto-cleared by the
> cascade (Tier 0 preflight + Tier 1 critic + Tier 2 jury). One row per decision; each row is
> pre-resolved with a recommended action so sign-off is one click.
>
> Supersedes the 2026-06-22 Part 1 digest. This run validates the **merged single post**
> `content/from-prompts-to-loop-engineering.md` (the 2-part series was consolidated after Part 1
> fell below the per-part word floor). The two offline fixes from the Part 1 run are already
> carried into the merged post; only the publish-time re-pulls remain.

## Gate computation (Tier 3)

- **Confidence** = jury agreement × spread. On both items the panel split `approve / escalate / approve`
  (2–1, narrow spread) → **medium confidence** (the lone dissent is a liveness, not a correctness, concern).
- **Risk** = `probability(error) × impact × detectability` for the artifact class. Both items are
  **named public attributions / benchmark numbers** (authoritative-looking, hard for a reader to catch) → **high risk**.
- **Gate rule fired:** *high risk → escalate to human.* The risk condition holds on both rows.

## Decisions for the human editor

| # | Artifact / location | Issue | Jury split | Risk reason | Recommended action | Status |
|---|---------------------|-------|------------|-------------|--------------------|--------|
| 1 | `content/from-prompts-to-loop-engineering.md` §"Proof at scale" | SWE-bench figures (12.47% → 76.8%, $0.05–$0.96) are model-specific and move monthly | rubber-duck: approve · fact-check: escalate · brand: approve | Benchmark numbers read as authoritative; freshness is a publish-time obligation | **Defensible as written** (dataset date Feb 2026 attached; flagged "snapshot, not a forecast"). Residual: re-pull swebench.com figures at publish. | ☐ approve  ☐ revise |
| 2 | `content/from-prompts-to-loop-engineering.md` §"Why now" | OpenAI "environments, feedback loops, and control systems" rests on a primary URL that returned HTTP 403 | rubber-duck: approve · fact-check: escalate · brand: approve | Named-org attribution on an indirectly-verified (403) primary source | **Defensible as written** (hedged "as cited by Böckeler"; corroborated by two sources). Residual: re-pull `openai.com/index/harness-engineering/` at publish to restore a direct cite. | ☐ approve  ☐ revise |

## Residual human gate (publish-time)

Both items are **defensible as written** (dataset-dated + indirectly attributed). The only remaining
human action is a **publish-time source re-pull** before final sign-off:

- `https://www.swebench.com/` — SWE-bench figures (12.47% → 76.8%, $0.05–$0.96); model-specific, move monthly.
- `https://openai.com/index/harness-engineering/` — currently 403; verify live to restore a direct cite.
- (Carry-over, low priority) `https://martinfowler.com/articles/harness-engineering.html` — Böckeler "guides and sensors"; already paraphrased (no quote marks) in the merged post, so no edit needed unless restoring a verbatim quote.

GATE: ESCALATE (2 rows, both approve-with-residual; residual = publish-time re-pull, no draft-time content change required)
