---
name: post-publish-review
description: "Close the content-as-experiment loop. After a piece is published, compare its actual engagement against the falsifiable Content hypothesis from the creative brief, render a go/no-go verdict (validated / partially validated / invalidated / inconclusive), and write the outcome to the hypothesis ledger. Use after social-publisher posts and after a measurement window has elapsed. Optional, time-delayed, never a publishing gate."
argument-hint: "Provide the run slug (and engagement numbers if you have them); defaults to the most recent published run"
---

# Post-Publish Go/No-Go Review Skill

## When to Use

Run this **after** the content is live and **after** a measurement window has elapsed — not at
publish time. This is the back half of the Minimum Viable Experiment loop adapted from
`microsoft/hve-core`: the `creative-brief` skill declared a falsifiable bet (§4b Content
hypothesis); this skill checks whether reality validated or invalidated it.

> Methodology: MVE go/no-go. An MVE succeeds whether the hypothesis is validated OR invalidated —
> both outcomes are valuable because both teach the next run. The failure mode is *not measuring*.

- **Quick-look** (optional): ~48 hours after publish — early signal, never a verdict.
- **Decision review** (the real one): ~7 days after publish — render the go/no-go verdict.
- Re-run on demand for a long-tail check (e.g. 30 days) when a piece keeps accruing saves.

This skill is **optional and never blocks** any other phase. A run can be marked `completed`
without it; the verdict simply makes the *next* run smarter.

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Content hypothesis (predicted thresholds + riskiest assumption) | `content/creative-brief.md` §4b | Yes |
| Canonical URL(s) of the published piece | `content/publishing-log.md` | Yes |
| Actual engagement numbers per channel | user-provided, or platform read-only tools when available | Yes (else verdict = INCONCLUSIVE) |
| Prior verdicts for the same angle | `content/hypothesis-ledger.md` | No |

**Never fabricate metrics.** If you cannot obtain a real number for a proxy, mark that proxy
`no-data` and let it push the verdict toward INCONCLUSIVE. Ask the user for the numbers rather
than guessing. For runs published before the §4b hypothesis field existed, there is no recorded
prediction — record the actuals as a baseline row and mark the verdict `no-baseline`.

## Procedure

### 1. Load the hypothesis

Read `content/creative-brief.md` §4b. Extract, per part for a series:

- The **predicted success proxies** with their thresholds and windows (save-rate ≥ X%, ≥ N
  qualified comments, scroll-depth ≥ X%, ≥ N project completions, etc.).
- The **kill signal** (the "we will know we are wrong when …" clause).
- The **riskiest assumption** — the one belief that, if false, sinks the piece.

If §4b is absent, this run predates the hypothesis convention → baseline-only (see Inputs).

### 2. Gather actuals (read-only)

For each predicted proxy, collect the real number for its window. Sources, in order of preference:

1. Read-only platform tools if configured (e.g. the `social-publisher` MCP read paths, LinkedIn/X
   analytics the user pastes in). Never post, like, or follow while measuring.
2. User-provided numbers (preferred when no API) — ask explicitly for each proxy.
3. `no-data` when neither is available.

Record the window each number covers (e.g. "saves at day 7"). Comparing a 48h number to a 7-day
threshold is invalid — note the mismatch rather than forcing a verdict.

### 3. Score each proxy

| Proxy state | Meaning |
|-------------|---------|
| **hit** | actual ≥ threshold within the window |
| **miss** | actual < threshold within the window |
| **no-data** | no real number available |

Then evaluate the **riskiest assumption** separately as held / broken / untested, using the
proxy evidence plus the qualitative signal (do the comments quote the framework, or just say
"great post"? qualified engagement is the strongest validation).

### 4. Render the verdict

| Verdict | Condition |
|---------|-----------|
| **VALIDATED** | Majority of proxies hit, the primary proxy hit, and the riskiest assumption held |
| **PARTIALLY VALIDATED** | The primary proxy hit but a secondary missed, OR the riskiest assumption held while a proxy missed |
| **INVALIDATED** | The kill signal fired (primary proxy missed AND no qualified engagement), or the riskiest assumption broke |
| **INCONCLUSIVE** | Too many `no-data` proxies, or window mismatch — cannot decide; schedule a re-measure |

State the verdict in one sentence with the deciding evidence (which proxy, which number, which
window). Be candid: an INVALIDATED result is a successful experiment, not a failure to hide.

### 5. Decide the next action (the "go/no-go")

| Verdict | Next action |
|---------|-------------|
| VALIDATED | **Go — do more of this.** Harvest the winning angle/hook/format into `content/idea-queue.md` as a ranked follow-up ("more like this, next dimension"). Note what specifically worked. |
| PARTIALLY VALIDATED | **Go, with a fix.** Keep the angle; fix the weak proxy (e.g. the carousel saved but no comments → sharpen the discussion prompt / CTA next time). Queue a refined variant. |
| INVALIDATED | **No-go on repost.** Do NOT just repost or boost. The insight did not land — rework the angle or retire it. Capture why the riskiest assumption broke. |
| INCONCLUSIVE | **Hold.** Schedule a re-measure with a defined window; gather the missing numbers. |

### 6. Write the outcome

Append to `content/hypothesis-ledger.md` (create from the template below if missing):

1. A **ledger row** in the summary table.
2. A dated **verdict block** with per-proxy evidence, the riskiest-assumption call, the verdict,
   and the next action.

If the review surfaces a **recurring** miss in the cascade itself (e.g. the critic keeps
approving hooks that consistently underperform, confirmed across runs), append an entry to
`content/critique-memory.md` so the rubric — not each artifact — gets fixed. One-off misses do
not belong there.

When the next action queues an idea, write it to `content/idea-queue.md` using that file's
existing scoring format so the discovery phase can pick it up.

## Output: hypothesis ledger

The ledger at `content/hypothesis-ledger.md` is the durable experiment record across all runs.
Seed it with this structure when it does not exist:

```markdown
# Hypothesis Ledger (content go/no-go log)

> Each published piece is an experiment. This ledger records the falsifiable bet from the
> creative brief (§4b), the actual engagement against it, the verdict, and the next action.
> Written by the `post-publish-review` skill. VALIDATED and INVALIDATED are both useful outcomes.

| Date | Run / slug | Primary proxy (threshold → actual) | Riskiest assumption | Verdict | Next action |
|------|-----------|-----------------------------------|---------------------|---------|-------------|

## Verdicts
```

## Constraints

- This skill is **read-only on the live platforms** — never like, follow, comment, or repost while measuring.
- **Never fabricate or estimate** an engagement number; `no-data` is an honest, valid state.
- Never let this skill **block** a run; it runs after `completed` and informs the *next* run.
- A verdict needs the **window** stated; do not compare a number to a threshold from a different window.
- INVALIDATED is a **legitimate, valuable** outcome — record it plainly, never bury or spin it.
- Only promote a miss to `critique-memory.md` when it is **confirmed and recurring**, not one-off.

## Hand-off to Discover

After the verdict is written, run the `post-run-reflection` skill (the Discover step). It reads
this ledger verdict plus the run's own trail (cut scope, open questions, unwritten parts) and
harvests ranked follow-up ideas into `content/idea-queue.md` — a VALIDATED angle becomes a
"more like this, next dimension" idea; an INVALIDATED one becomes a pivot, never a repost.
