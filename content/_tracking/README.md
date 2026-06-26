# `_tracking/` — per-run process memory

Durable scratchpad for content runs, written by the `run-tracking` skill. Each run gets a folder
`content/_tracking/<run-slug>/` (topic-scoped runs may nest it under
`content/topics/<slug>/_tracking/`) holding two files:

| File | Role |
|------|------|
| `phase-log.md` | Append-only timeline — one row per completed phase (outcome, artifacts, what's next) |
| `handoff.md` | Overwritten rehydration summary — the single thing to read after a compaction or before resuming a later series part |

## Why this exists

Long runs lose state two ways: the agent's context window compacts mid-run, and series Part N is
written days or weeks after Part 1. The handoff lets a fresh context **rehydrate cheaply** instead
of replaying the whole run, and keeps locked decisions locked across series parts.

## What this is NOT

`_tracking/` is **process memory, not a deliverable** — keep it out of published output (it may be
git-ignored). The durable *content* record lives elsewhere:

- `content/content-decision-log.md` — *why* each fork was chosen (ADR-style CDRs), cross-run.
- `content/hypothesis-ledger.md` — predicted vs actual engagement, cross-run.

Tracking holds the run's working state; those hold the durable record. The handoff **cites** CDR
ids rather than restating their rationale.

## When to use

Series (any number of parts), multi-session runs, or any run long enough to expect a compaction.
Skip it for a quick one-shot single post.
