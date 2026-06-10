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

## AI-image-specific checks (apply when auditing `content/visuals/generated/`)

- `image-no-text` — **Error** if any legible text/letterforms appear baked into the image.
- `image-fidelity` — **Error** if brand-critical colors deviate from the token palette;
  **Warning** for minor saturation/lighting drift.
- `safety` — **Error** for sensitive/unsafe scenes; **Warning** for unintended human
  likeness that needs manual sign-off.
