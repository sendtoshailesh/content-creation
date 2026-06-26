---
name: post-run-reflection
description: "Close the discovery loop. After a content run finishes, reflect on what the run itself surfaced — cut scope, open questions, unwritten series parts, reader-perspective gaps, and validated angles from the hypothesis ledger — and harvest them into the idea queue as ranked, ready-to-pick follow-ups. Use once at the end of a run (and again after post-publish-review renders a verdict). Optional, never a publishing gate."
argument-hint: "Provide the run slug (defaults to the most recent completed run)"
---

# Post-Run Reflection Skill (the Discover phase)

## When to Use

Run this **at the end of a content run** — after the piece is `completed` — and again **after
`post-publish-review` renders a verdict**. It is the internal-reflection twin of
`post-publish-review`:

- `post-publish-review` (#7) looks **outward**: did the audience validate the §4b hypothesis?
- `post-run-reflection` (#6) looks **inward**: what did making this piece teach us about *what to
  make next?*

Every real content run generates more ideas than it spends — scope you deliberately cut, open
questions you flagged, a series Part 3 you scoped but did not write, a reader perspective the
draft under-served, a contradiction the research map could not fully resolve. Without a harvest
step those leads evaporate. This skill captures them while the context is still warm and writes
them where the next run will look: `content/idea-queue.md`.

> Methodology: a Reflexion-style "what did this episode teach me" pass, pointed at the *next*
> topic rather than at the current artifact. It is generative (produces ideas), not corrective
> (it does not rewrite the published piece).

This skill is **optional and never blocks** anything. A run can be `completed` without it; the
reflection simply keeps the idea queue fed from the pipeline's own exhaust.

## Inputs

| Input | Source | What to mine |
|-------|--------|--------------|
| Out-of-scope / cut decisions | `content/creative-brief.md` (scope + key-message), strategy/outline | Topics named then deferred — "out of scope for this part", "a separate post" |
| **Rejected alternatives** | `content/content-decision-log.md` (CDR entries) | The framing/scope/format options a decision record set aside — often the next piece's strongest angle |
| Unwritten series parts | scope-assessment Series Plan, `content/pipeline-config.md` | Parts scoped but not yet drafted |
| Open questions & low-confidence claims | `content/content-research-map.md` | Flagged unknowns, contradictions left unresolved, low-ranked arguments |
| Reader-perspective gaps | content-research-map perspectives, visual-style-map | Personas the final piece under-served |
| Validated / invalidated angles | `content/hypothesis-ledger.md` | VALIDATED → "more like this, next dimension"; INVALIDATED → a *different* angle on the same need |
| Recurring process lessons | `content/critique-memory.md`, Tier 1/2 reviews | Only for the process note (step 4), not for queued ideas |

**Never invent reader demand.** A harvested idea must trace to something real in the run —
a cut line, a flagged question, a ledger verdict. If nothing real surfaced, queue nothing and
say so. A short honest harvest beats a padded one.

## Procedure

### 1. Re-read the run's own trail

Read the creative brief, the content-research map, the scope/series plan, and (if it exists) the
hypothesis-ledger verdict for this run. List every place the run **pointed past itself**:
deferred scope, "we'll cover X separately", open questions, unresolved contradictions,
under-served personas, and any VALIDATED/INVALIDATED angle.

### 2. Turn each lead into a candidate idea

For each lead, write a one-line content angle and tag its origin:

- `cut-scope` — deliberately deferred from this run (a scope cut, or a rejected scope option from a CDR)
- `series-next` — a scoped-but-unwritten part
- `open-question` — a flagged unknown worth its own investigation
- `perspective-gap` — a persona the piece under-served
- `validated-angle` — harvested from a VALIDATED ledger verdict ("do more of this")
- `pivot-angle` — a fresh take prompted by an INVALIDATED verdict (never a repost)

Merge near-duplicates and drop anything already sitting in `idea-queue.md`.

### 3. Score and queue

Score each surviving candidate on the queue's shared 25-point scale
(relevance + data density + timeliness + gap + validation), then append it to
`content/idea-queue.md` using that file's existing entry format. Required additions per entry:

- **Source**: `Post-run reflection: <run-slug>` plus the origin tag from step 2.
- **Status**: `queued`.
- A one-line **provenance** note ("deferred from loop-engineering Part 1 scope") so a future
  reader trusts where it came from.

`validated-angle` ideas inherit a validation boost — they are grounded in a real go/no-go result,
not a guess. Update the queue header's "Last curated" line to note the reflection harvest and count.

### 4. Record at most one process lesson

If the run exposed a **recurring** process lesson (a gate that keeps missing the same class of
problem, a phase that repeatedly needed rework), append one entry to `content/critique-memory.md`
so the *rubric* improves, not just this run. One-off friction does not belong there — only
patterns confirmed across runs. Skip this step if nothing recurring surfaced.

### 5. Report

Summarize: N ideas queued (by origin tag), any process lesson recorded, and the single
highest-scoring follow-up as the suggested next pick. Keep it to a few lines.

## Relationship to the other discovery channels

This is one of several feeds into `content/idea-queue.md`, and the only one sourced from the
pipeline's own output:

| Channel | Source of ideas |
|---------|-----------------|
| `feed-curator` | external blogs / newsletters / RSS |
| `reading-list-curator`, `apple-notes-curator`, `social-saves-curator` | the author's saved reading |
| **`post-run-reflection`** | **the pipeline's own completed runs (this skill)** |

All write the same 25-point entry format, so any pick flows into `content-pipeline` identically.

## Constraints

- **Generative, not corrective** — never edits the published piece, visuals, or social posts.
- **Every queued idea traces to a real lead** in the run; never fabricate reader demand to pad the harvest.
- **Never blocks** a run; it runs after `completed` and only feeds the *next* run.
- **De-duplicate** against the existing queue before appending.
- An **INVALIDATED** angle becomes a *pivot* idea (a different take on the same reader need), never a repost of what failed.
- Promote a lesson to `critique-memory.md` only when it is **confirmed and recurring**, not one-off.
