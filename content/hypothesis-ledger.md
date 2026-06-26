# Hypothesis Ledger (content go/no-go log)

> Each published piece is an experiment. This ledger records the falsifiable bet from the
> creative brief (§4b Content hypothesis), the actual engagement against it, the verdict, and the
> next action. Written by the `post-publish-review` skill after a measurement window elapses.
> VALIDATED and INVALIDATED are both useful outcomes — the only failure mode is not measuring.

## How to use

- A **pending** row is seeded by `social-publisher` at publish time, capturing the predicted
  thresholds and riskiest assumption from `content/creative-brief.md` §4b.
- The `post-publish-review` skill fills in the **actuals** and **verdict** after the window
  (~48h quick-look, ~7-day decision review).
- Verdicts: **VALIDATED** · **PARTIALLY VALIDATED** · **INVALIDATED** · **INCONCLUSIVE** ·
  `no-baseline` (run published before the §4b hypothesis convention).

## Ledger

| Date | Run / slug | Primary proxy (threshold → actual @ window) | Riskiest assumption | Verdict | Next action |
|------|-----------|---------------------------------------------|---------------------|---------|-------------|
| 2026-06-23 | loop-engineering-ai-native-development | n/a (published before §4b) | not recorded | `no-baseline` | Baseline only — no predicted thresholds; future runs carry a hypothesis. |

## Verdicts

### 2026-06-23 — loop-engineering-ai-native-development — `no-baseline`

Published before the Content hypothesis (§4b) convention existed, so there is no recorded
falsifiable prediction to score against. No verdict is rendered. If engagement numbers are
gathered later they can be recorded here as a baseline reference for similar future angles.
