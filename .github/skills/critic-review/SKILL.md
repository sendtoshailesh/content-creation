---
name: critic-review
description: 'Tier 1 rubric critic and reference-grounded fact-check desk for the content review cascade. Runs a G-Eval-style constitution judge (chain-of-thought + form-filling) and a faithfulness check anchored to the reference brief, emits the compliance-severity findings schema with confidence/risk fields, auto-approves the clean low-risk majority, revises the fixable in a loop, and abstains to human on high-stakes or unverifiable claims. Use after the Tier 0 preflight passes and before the Tier 2 jury.'
argument-hint: 'Provide the artifact path (blog, social post, or script). The constitution and reference brief are loaded automatically.'
---

# Critic Review Skill (Tier 1)

The deterministic [Tier 0 preflight](../../../scripts/pipeline/preflight_check.py) catches mechanical
defects at zero LLM cost. This skill is **Tier 1**: one grounded LLM critic that reads each artifact
against the project's own rules ("constitution") and the run's reference corpus, then either
auto-approves it, silently revises a fixable miss, or escalates it. The goal is to make the human an
*editor of exceptions* — most artifacts clear here without ever reaching a person.

Two critic desks run in this skill:

1. **Rubric critic** — judges prose/voice/structure against the constitution (G-Eval pattern).
2. **Fact-check desk** — verifies load-bearing claims against the reference brief (RAGAS/Self-RAG pattern).

Both emit the **same** findings contract defined in
[`.github/instructions/shared/compliance-severity.md`](../../instructions/shared/compliance-severity.md)
so the orchestrator can fold their output into one escalation digest.

## When to use

- Per artifact, **after** the Tier 0 preflight returns `GATE: PASS` for that file.
- **Before** the Tier 2 jury (rubber-duck + disjoint reviewers) — Tier 1 decides what even needs a jury.
- Re-run on any artifact the producer revised in the loop, until it clears or hits the iteration cap.

## Inputs

- The target artifact (`content/*.md` — blog, LinkedIn/X/Reddit post, reel/YouTube script).
- **The constitution** (the rubric — load explicitly, these replace human labels):
  - [`content-quality.instructions.md`](../../instructions/content-quality.instructions.md) — data
    specificity, structure, tone.
  - [`social-formatting.instructions.md`](../../instructions/social-formatting.instructions.md) — platform
    formatting. Also load `writing-style.instructions.md` for voice (resolve via the hve-core fallback in
    [`hve-core-location.instructions.md`](../../instructions/shared/hve-core-location.instructions.md) if
    it is not in this repo).
- **The grounding corpus** for fact-checks: [`content/reference-brief.md`](../../../content/reference-brief.md)
  and `content/trend-research.md` if present.
- [`content/critique-memory.md`](../../../content/critique-memory.md) if present — recurring confirmed
  misses to check for first (loaded so the critic stops re-making the same mistakes).

## Phase 1 — Rubric critic (G-Eval: chain-of-thought, then form-filling)

Score against the constitution, not preference. Do **not** emit an open-ended 1–10 score; fill the
findings form. For each constitution dimension, reason first, then record only deviations.

1. **Read the constitution dimensions** as the evaluation steps (data specificity, concrete numbers,
   tone/voice, structure, platform formatting). This is the G-Eval "chain-of-thought" — the steps come
   from the rubric, not from the model's preference.
2. **Walk the artifact** section by section. For every dimension, decide pass or deviation and write a
   one-line rationale before recording a row. Reasoning precedes the verdict.
3. **Record only deviations** as findings rows (no row for a clean dimension). Map severity to the
   constitution: a missing required element or banned-voice violation is an **Error**; a weak-but-present
   element is a **Warning**; a stylistic nicety is **Info**.

## Phase 2 — Fact-check desk (reference-grounded faithfulness)

Apply the newsroom **two-source rule**: every load-bearing claim needs at least one grounded citation
from the reference brief, or it is flagged.

1. **Extract load-bearing claims** — public pricing/benchmark numbers, named attributions, dated facts,
   and headline/thesis claims. Ignore body transitions and obvious common knowledge.
2. **Ground each claim** against `reference-brief.md` (and `trend-research.md`). For each claim record:
   the claim, the supporting reference entry (or "no source found"), and whether the artifact's wording
   matches the source.
3. **Flag the gaps** — a public claim with no grounded source, a number that disagrees with the source,
   or an attribution the brief does not support is an **Error** with `category: claim-citation` and
   `risk: high`. A claim that is plausible but stale-looking is a **Warning**.
4. **Check first-party primacy (Source-of-Truth Precedence).** For each "here's what works / here's what
   I recommend" claim, check the brief's tier labels (`[T1 own | T2 Microsoft | T3 GitHub | T4 public]`):
   does the claim lead with a Tier 1-3 (author's work / Microsoft / GitHub) example before a public one?
   A recommendation grounded **only** in public sources when a first-party source exists in the brief or
   `content/browsing-signals.md` is a **Warning** with `category: source-precedence` (lead first-party,
   cite public as corroboration). A neutral benchmark that legitimately has no first-party equivalent is
   fine — do not flag it.

## Phase 3 — Confidence, risk, and the auto-approve decision

Annotate every finding with the three extra fields from the compliance-severity schema
(`confidence`, `risk`, `source signal`) and apply the routing rule.

- **Risk** = `probability(error) x impact(if wrong) x detectability`. Public pricing/benchmark numbers and
  named attributions are **high** risk (authoritative-looking, hard for a reader to catch). Body prose,
  alt-text, and captions are **low** risk.
- **Confidence** = how sure the critic is of its own finding. If the rubric and fact-check desks agree and
  the rule is unambiguous, confidence is **high**; if the dimension is subjective or the source is
  ambiguous, confidence is **low**.
- **Decision per the schema routing rule:**
  - **Auto-approve** (no human, no jury) when the artifact has zero Errors and every Warning is
    `confidence: high` AND `risk: low|medium` with a mechanical fix — and the dimension is body prose,
    transitions, alt-text, captions, or file names.
  - **Revise-in-loop** when a finding has a clear mechanical fix: hand the findings rows back to the
    producing agent, let it fix, then re-run this skill. Cap at **3 iterations**; on the 3rd failure,
    escalate instead of looping.
  - **Escalate to Tier 2 jury / human** when any Error carries `risk: high`, any finding is
    `confidence: low`, or the critic must `ABSTAIN`.

## Phase 4 — Calibrated abstention

The critic may answer `ABSTAIN: needs human` instead of guessing. Abstain when the artifact depends on
fresh facts the brief cannot confirm, legal/public claims, source ambiguity, or visual judgment the model
cannot inspect reliably (CriticGPT notes some tasks exceed even expert-with-model evaluation). An abstain
always escalates; it never auto-approves.

## Local rubber-duck critic persona (Tier 2 fallback)

When GitHub Copilot's rubber-duck review cannot be invoked as a tool, emulate it here as one adversarial
voice. Before scoring, ask three questions and answer them against the constitution and reference brief —
not preference:

- *What claim would I challenge?*
- *What context is missing?*
- *What would embarrass us if published?*

Pair this persona with at least one other reviewer stance (fact-check desk, brand/tone desk, or
visual/layout desk) so the jury keeps diversity even in fallback mode. The rubber-duck vote is one jury
member: it can trigger revision or escalation, but it cannot auto-approve a high-risk artifact alone.

## Tier 2 — diverse jury (PoLL), only on the residue

Convene a jury **only** for the contested or high-risk residue Tier 1 escalates — never for the
auto-approved majority. A panel of disjoint stances (Panel of LLMs pattern) cancels the self-preference
bias a single critic carries.

1. **Seat three disjoint jurors.** Use stances that do not share a failure mode:
   - GitHub Copilot **rubber-duck** review when callable as a tool, else the local rubber-duck persona.
   - The **fact-check desk** (reference-grounded), distinct from the rubric desk.
   - One of **brand/tone** or **visual/layout** desk, whichever the artifact's risk class points to.
2. **Each juror votes** on the same row contract: `approve | revise | escalate`, with its findings rows and
   `confidence`/`risk` fields. No juror sees another's vote before casting its own (independent ballots).
3. **Moderator pass (Co-STORM).** A moderator reconciles the ballots: deduplicate overlapping findings,
   surface the one decision that splits the panel, and compute the **vote spread**.
4. **Aggregate:**
   - **Unanimous approve** (low spread) -> auto-approve.
   - **Unanimous fail** -> auto-return to the producer (no human) with the merged findings.
   - **Split vote / high spread** -> pass to the Tier 3 gate; the split itself is the escalation signal.

## Tier 3 — confidence x risk escalation gate (the stop condition)

The final controller decides what actually reaches the human. It consumes the jury result, not the raw
artifact.

- **Confidence** = jury agreement x self-consistency spread. Unanimous, low-spread = high confidence; a
  split panel or a juror that flipped across samples = low confidence.
- **Risk** = `probability(error) x impact x detectability` for the artifact class (pricing/benchmark and
  named attribution are high; body prose and captions are low).
- **Gate:**
  - **high confidence x low|medium risk** -> auto-approve (no human).
  - **low confidence OR high risk OR any `ABSTAIN: yes`** -> escalate to the human editor.
- **Escalation digest, not raw artifacts.** Everything escalated is written as decision-only rows into
  `content/escalation-digest.md` (format in the compliance-severity schema): the itemized critique, the
  jury split, the risk reason, and a one-click approve / revise per row. The human edits exceptions, never
  re-reviews the whole run.
- **Loop cap.** Honor the Tier 1 revise-in-loop cap of **3 iterations**; on the 3rd failure the gate
  escalates instead of looping further.

## Output contract
extended compliance-severity row format.

```markdown
## Tier 1 Critic Review — <artifact path>

| Severity | Category | Asset / location | Finding | Required fix | Confidence | Risk | Source signal |
|----------|----------|------------------|---------|--------------|------------|------|---------------|
| Error | claim-citation | content/post.md §4 | SWE-bench score has no source date attached | Add source + Feb 2026 dataset date | high | high | reference-grounded |

GATE: FAIL
ABSTAIN: no
DECISION: escalate
```

- `GATE: PASS` with `DECISION: auto-approve` when zero Errors and all Warnings clear the auto-approve bar.
- `GATE: FAIL` with `DECISION: revise` routes the rows back to the producer (loop, max 3 iterations).
- `GATE: FAIL` with `DECISION: escalate` (or any `ABSTAIN: yes`) sends the residue to the Tier 2 jury,
  then the escalation digest.

## Critique memory (Reflexion)

When a confirmed miss recurs across runs, append it to `content/critique-memory.md` so the next run loads
it first. Fix the loop, not the artifact: if the critic keeps missing the same class of error, patch the
constitution/rubric rather than re-reviewing each post by hand.
