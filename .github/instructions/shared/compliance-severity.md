# Compliance Severity Schema (shared)

> Shared findings contract used by `brand-guardian` and `visual-reviewer` so brand and
> visual compliance produce **machine-readable, gated** feedback instead of prose notes.
>
> Methodology adapted from `microsoft/content-generation-solution-accelerator` (Brand
> Compliance Validation with Error / Warning / Info severities).

## Severity levels

| Severity | Meaning | Gate effect |
|----------|---------|-------------|
| **Error** | Violates a non-negotiable standard (broken visual, wrong/altered brand color, embedded text in an AI image, false/uncited claim, off-voice corporate framing). | **BLOCKS** publishing (Steps 10/11) and any downstream distribution until fixed. |
| **Warning** | Deviates from a strong preference but may be acceptable with rationale (repetitive layout, weak negative space, thin data backing). | Requires a written justification in the report, or a fix, before the gate passes. |
| **Info** | Advisory / polish opportunity (nicer phrasing, optional visual variety). | Never blocks. Recorded for optional follow-up. |

## Findings table (required output format)

Every audit emits a table; one row per finding:

```
| Severity | Category | Asset / location | Finding | Required fix |
|----------|----------|------------------|---------|--------------|
| Error    | brand-color | content/visuals/generated/hero.png | Accent rendered as #2563eb, not token ACCENT #1f6feb | Regenerate with corrected color guidance |
| Warning  | layout | content/visuals/part1-eval-stack.png | 3rd card grid in a row — pattern repetition | Vary composition or justify |
| Info     | voice | content/part1.md §3 | "leverage synergies" drifts corporate | Reword to plain practitioner voice |
```

## Categories

`voice` · `tone` · `messaging` · `claim-citation` · `design-token` · `brand-color` ·
`typography` · `layout` · `image-no-text` · `image-fidelity` · `safety` · `accessibility`

## Confidence and risk (required for LLM-tier reviewers)

LLM-based reviewers (Tier 1 rubric critic, Tier 2 jury) append two fields to every row so the
escalation controller can route by **how sure** the critic is and **how costly** a miss is.
Deterministic Tier 0 checks (`preflight_check.py`) are inherently high-confidence and may omit
these fields.

| Field | Values | Meaning |
|-------|--------|---------|
| **Confidence** | `high` / `medium` / `low` | How certain the reviewer is that the finding is real (not a critic hallucination). Anchor to a checkable signal where possible. |
| **Risk** | `high` / `medium` / `low` | Blast radius if the issue ships unfixed. `high` = pricing, attribution, factual claims, thesis, safety; `medium` = supporting data, structure; `low` = polish. |

Extended row format (superset of the base table; base columns stay identical):

```
| Severity | Category | Asset / location | Finding | Required fix | Confidence | Risk | Source signal |
|----------|----------|------------------|---------|--------------|------------|------|---------------|
| Error | claim-citation | content/part1.md §4 | "$0.002/1K tokens" not in reference brief | Cite source or remove | high | high | grounded-review: UNVERIFIED |
| Warning | layout | content/visuals/part1-stack.png | 3rd card grid in a row | Vary composition | medium | low | visual-reviewer rubric |
```

Routing rule (consumed by the escalation controller):

- **Auto-apply / auto-approve** when `Confidence: high` **and** `Risk: low|medium` and the fix is mechanical.
- **Escalate to the human** when `Risk: high`, **or** when `Confidence: low` on any `Error`.
- `ABSTAIN` is a valid reviewer output (no confident verdict) and always escalates rather than guessing.

## Gate verdict (required footer)

End every audit with an explicit verdict line:

```
GATE: PASS        # no Error rows, and every Warning has a fix or written justification
GATE: FAIL        # >=1 Error, or an unjustified Warning
```

- A `FAIL` returns the asset to the responsible producer agent (`visual-renderer`,
  `image-content-agent`, `blog-writer`, social agents) and triggers the orchestrator's
  rollback/redo protocol before any publishing step proceeds.
- `Info` findings never affect the verdict.

## Escalation digest (one consolidated exception list)

Instead of reading N separate audit artifacts, the human sees **one** digest aggregating every
reviewer's findings across all artifacts in the run. The orchestrator writes it to
`content/escalation-digest.md` after the review tiers run.

Required structure:

```
## Escalation Digest - <run id>

GATE: PASS | FAIL
Auto-approved: N artifacts   Escalated: M findings   Auto-fixed: K findings

### Needs your decision (Risk: high or Confidence: low)
| Severity | Risk | Conf. | Asset / location | Finding | Proposed fix | Decision |
|----------|------|-------|------------------|---------|--------------|----------|
| Error | high | low | content/part1.md §4 | Uncited "$0.002/1K" price | Cite or remove | [ ] approve  [ ] revise |

### Auto-fixed (high confidence, low risk) - FYI only
- content/visuals/part1-stack.png: repeated card grid -> recomposed (visual-renderer)

### Jury splits (where reviewers disagreed)
- content/part2.md §2: 2 of 3 jurors flagged tone drift; moderator note included
```

Rules:

- The digest lists **only** the escalated residue in the decision table; auto-approved and
  auto-fixed items are summarized, not enumerated for action.
- Each decision row offers a one-click `approve` / `revise` so the human stays an *editor of
  exceptions*, not a re-reviewer of everything.
- A run-level `GATE: FAIL` holds publishing until every decision row is resolved.

## AI-image-specific checks (apply when auditing `content/visuals/generated/`)

- `image-no-text` — **Error** if any legible text/letterforms appear baked into the image.
- `image-fidelity` — **Error** if brand-critical colors deviate from the token palette;
  **Warning** for minor saturation/lighting drift.
- `safety` — **Error** for sensitive/unsafe scenes; **Warning** for unintended human
  likeness that needs manual sign-off.
