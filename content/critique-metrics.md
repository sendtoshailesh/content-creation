# Cascade metrics ledger (Phase D)

Append-only run log for the content review cascade. After each run closes, the orchestrator
appends one row of cascade outcomes here, then `scripts/pipeline/cascade_metrics.py` aggregates the
rows into the anti-over-trust metrics (auto-approve rate, escalation rate, escalation precision, miss
rate, judge-human agreement) and applies the self-regulating stop condition.

## How to use

- **Append** one row per run under `## Runs` with the seven counts below. Use the run date or slug as
  `run_id`.
- **Audit** a sample of that run's auto-approvals (recommend ~10-20%); record how many the audit flagged
  as misses in `audit_flagged`.
- **Run** `python3 scripts/pipeline/cascade_metrics.py` to compute the rolling metrics. Exit code 1 means
  the miss rate tripped the threshold and the gate should tighten.

## Column meanings

| Column | Meaning |
|--------|---------|
| `run_id` | Run date or slug (non-numeric). |
| `artifacts` | Total artifacts that entered the cascade. |
| `auto_approved` | Cleared by Tier 1/Tier 2/Tier 3 with no human touch. |
| `escalated` | Reached the human editor via the escalation digest. |
| `human_changed` | Of the escalated, how many the human actually revised. |
| `audited` | Auto-approvals sampled for a human audit. |
| `audit_flagged` | Of the audited, how many the audit flagged as a miss. |

## Runs

| run_id | artifacts | auto_approved | escalated | human_changed | audited | audit_flagged |
|--------|-----------|---------------|-----------|---------------|---------|---------------|
| 2026-06-22-loop-part1 | 1 | 0 | 1 | 1 | 0 | 0 |
| 2026-06-23-loop-single | 1 | 0 | 1 | 0 | 0 | 0 |
