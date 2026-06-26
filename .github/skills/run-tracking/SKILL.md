---
name: run-tracking
description: "Give a content run a durable scratchpad that survives context loss and series gaps. Maintain a per-run phase log (append-only timeline of what each phase decided + produced) and a compaction handoff (the rehydration summary to reload when context is lost or when a later series part resumes weeks later). Writes under content/_tracking/<run-slug>/. Use for long runs and any multi-part series; optional for short single-post runs. Never a publishing gate."
argument-hint: "Provide the run slug (or topic) and the phase just completed"
---

# Run Tracking Skill

## When to Use

Long runs and **every multi-part series** lose state two ways: the agent's context window
compacts mid-run, and series Part N gets written days or weeks after Part 1. Both drop the
working memory — which decisions are locked, what each phase produced, what the next phase
must not re-open. This skill keeps a small **durable scratchpad** outside the context window so
a run can be rehydrated cheaply instead of re-derived.

> Methodology: agentic loop **state externalization** + **compaction handoff** (microsoft/hve-core
> RPI/handoff pattern). The middle/outer loop persists its own state to a file so the inner loop
> (one phase) can be resumed by a fresh context that reads the handoff instead of replaying the
> whole transcript.

Use it when: the run is a series (any number of parts), the run spans multiple sessions, or the
work is long enough that you expect a compaction. Skip it for a quick one-shot single post.

## Output

A per-run folder `content/_tracking/<run-slug>/` (topic-scoped runs may nest it under
`content/topics/<slug>/_tracking/`) holding two files:

| File | Role | Shape |
|------|------|-------|
| `phase-log.md` | Append-only **timeline** — one row per completed phase | what ran, what it decided, what it wrote |
| `handoff.md` | Overwritten **rehydration summary** — the current durable state | enough to resume cold |

`_tracking/` is process memory, not a deliverable — keep it out of published output (it may be
git-ignored). It is distinct from the durable *content* artifacts (`content-decision-log.md`,
`hypothesis-ledger.md`), which outlive the run; tracking is the run's working state.

### `phase-log.md` — append-only

```markdown
# Phase log — <run-slug>

| When | Phase | Outcome / key decision | Artifacts written | Next phase must know |
|------|-------|------------------------|-------------------|----------------------|
| 2026-06-25 14:10 | Creative brief | Thesis locked (CDR-001); audience = staff eng | creative-brief.md | §4b hypothesis is the success test |
| 2026-06-25 14:35 | Scope assessment | Split into 2 parts (CDR-002) | pipeline-config Series Plan | Part 2 = governance angle, unwritten |
```

Never edit past rows — the log is the audit trail of how the run actually went.

### `handoff.md` — overwrite each phase

The **single thing to read after a compaction or before resuming a later part.** Keep it short
and current; overwrite it as state changes.

```markdown
# Run handoff — <run-slug>     (updated: 2026-06-25 14:35)

- **Goal**: one-line run objective (from the brief).
- **Status**: Step N of M complete · current phase · `in-progress | blocked | paused`.
- **Locked decisions**: CDR-001 thesis framing, CDR-002 2-part split — do NOT re-open.
- **Series state**: Part 1 drafted + visuals done; Part 2 scoped, not started.
- **Open threads**: the 1–3 unresolved questions the next phase must pick up.
- **Next action**: the exact next step a cold start should take.
- **Key paths**: brief, strategy, decision log, draft(s) — where the real artifacts live.
```

## Procedure

1. **On run start** (series or long run): create `content/_tracking/<run-slug>/` with both files;
   seed `handoff.md` from the creative brief's goal + status.
2. **After each phase**: append one `phase-log.md` row (outcome, artifacts, what's next) and
   **overwrite** `handoff.md` to reflect new locked decisions, series state, and next action.
3. **On compaction / cold resume**: read `handoff.md` first, then the linked artifacts — do not
   replay the whole run. Reconcile against `content-decision-log.md` so locked decisions stay locked.
4. **Between series parts**: before drafting Part N, read the handoff to recover what earlier parts
   committed (thesis, split rationale, cross-references, the part's scoped angle), then continue.
5. **On run completion**: mark `handoff.md` status `completed`. The durable outcomes live in the
   content artifacts and `post-run-reflection`; `_tracking/` can be archived with the run.

## Relationship to the other run artifacts

| Artifact | Holds | Lifetime |
|----------|-------|----------|
| `_tracking/handoff.md` (this) | current resumable **state** of the run | the run only |
| `_tracking/phase-log.md` (this) | timeline of **how** the run progressed | the run only |
| `content-decision-log.md` | **why** each fork was chosen (CDRs) | durable, cross-run |
| `hypothesis-ledger.md` | predicted vs actual **engagement** | durable, cross-run |

Tracking is the *working memory*; the decision log and ledger are the *durable record*. When a
phase locks a decision, record the *why* in a CDR and the *current state* in the handoff — they
reference each other (the handoff cites CDR ids).

## Constraints

- **Handoff stays short and current** — overwrite it; a stale handoff is worse than none.
- **Phase log is append-only** — never rewrite history.
- **Never duplicate the decision log** — cite CDR ids from the handoff, don't restate rationale.
- **Process memory, not a deliverable** — keep `_tracking/` out of published output.
- **Never blocks** a run; tracking is an aid, not a gate.
