---
name: visual-reverse-review
description: 'Reverse-Engineering Visual Review (REVR) — a hard quality gate that reads meaning back OUT of a rendered visual (blind, pixels only), back-translates it against the source concept it was built from, scores the semantic gap on a 0-100 rubric, and loops a self-evolving renderer fix until the derived meaning matches intent with zero legend/encoding gaps. Use in the quality phase after the deterministic inspector and the visual-reviewer checklist pass, before any visual is marked publish-ready.'
argument-hint: 'Provide the visual asset path (PNG) and the source artifact it illustrates (blog .md). The design brief / opportunity map and the renderer source are loaded automatically.'
---

# Visual Reverse-Engineering Review (REVR)

Most visual review reads **forward**: you know what the picture is supposed to say, you look at
it, and you nod. That is exactly how encoding bugs survive — the reviewer's prior fills the gap the
*reader* will fall into. REVR reads **backward**. It recovers the message **only from the pixels**,
as a stranger would, then measures how far that recovered message drifted from the source concept the
visual was built from. The size of that drift is a number; the number drives a bounded repair loop;
the loop is allowed to **rewrite the renderer program itself** so the fix is permanent, not patched.

This is the visual analogue of round-trip / back-translation testing (translate `A -> B`, then
`B -> A`, and diff against the original) combined with a G-Eval-style rubric judge. It runs as a
**hard gate**: a visual cannot be marked publish-ready until it passes or is explicitly escalated.

## Where REVR sits in the cascade

| Gate | Tool | Catches |
|------|------|---------|
| Tier 0 | `scripts/visuals/html/inspect` + `scripts/pipeline/preflight_check.py` | mechanical defects (overflow, off-scale text, missing connectors) |
| Tier 1 | `visual-reviewer` checklist (sections 1–9) | layout, readability, token compliance, comprehension heuristics |
| **Tier 2 — REVR** | **this skill** | **does the picture actually decode to its intended meaning?** legend/encoding gaps, false-category color, unreadable order, ambiguous glyphs |

REVR runs **after** Tier 0 and the Tier 1 checklist pass for the asset, because a picture that
overflows or clips is not yet worth reverse-reading. REVR is the last gate before publish-ready.

## Inputs (assembled before any reading)

1. **The rendered asset** — the PNG (e.g. `content/visuals/p1-03-harness-vs-loop.png`).
2. **The source concept** (the ground truth the visual must convey), gathered in this order:
   - the **blog passage** the visual illustrates (the section in `content/from-prompts-to-*.md`
     that carries the `![alt](path)` reference, plus its alt text);
   - the **design brief / opportunity-map entry** for the asset (`content/visual-opportunity-map.md`,
     `content/visual-style-map.md`);
   - the **renderer intent** — the function docstring / comment block in the renderer source
     (e.g. `content/visuals/render_loop_engineering.py`).
3. **The renderer source** — the exact function that produces the asset (so the repair step can edit
   it, not just regenerate output).

> The source concept is the **only** authority for answering "what was this supposed to mean?" Never
> invent intent from the picture.

## The REVR loop

```
        +-----------------------------------------------------------+
        | 0. assemble source intent (blog passage + brief + docstr) |
        +-----------------------------------------------------------+
                                  |
        +---------v---------+     (the source intent text is NOT in view during step 1)
        | 1. BLIND READ     |  view ONLY the PNG; reverse-engineer its message + every encoding
        +---------+---------+
                  |
        +---------v---------+
        | 2. BACK-TRANSLATE |  diff derived-read vs source intent; score 0-100; list gaps
        +---------+---------+
                  |
            score >= 85 AND zero legend/encoding gaps AND message matches?
                  |                                  |
                 yes                                 no
                  |                                  |
            +-----v-----+        +------------------v-------------------+
            |   PASS    |        | 3. CLARIFY: answer each ambiguity    |
            | publish-  |        |    from SOURCE CONCEPT first;        |
            |  ready    |        |    if not derivable -> redraw trigger|
            +-----------+        +------------------+-------------------+
                                                    |
                                 +------------------v-------------------+
                                 | 4. SELF-EVOLVING REPAIR: edit the    |
                                 |    renderer SOURCE (add legend/inline|
                                 |    labels/fix color encoding) & re-  |
                                 |    render. iteration += 1            |
                                 +------------------+-------------------+
                                                    |
                                    iteration < 3 ? loop to step 1
                                    iteration == 3 & still failing ?
                                       -> ESCALATE with summary (hard stop)
```

### Step 1 — Blind read (pixels only)

Use the **latest GPT multimodal model available in GitHub Copilot** via the image-viewing tool. Open
the PNG and write the read **without** the source-intent text in front of you (assemble it in step 0,
then read the picture as if you had never seen the brief). Produce a `DERIVED READ` block:

- **One-line message**: in a single sentence, what is this picture telling a stranger?
- **Element inventory**: enumerate *every* visual element — each box, node, arrow, line, shape, icon,
  color region, and label — and state **what you believe it encodes**. For anything whose meaning you
  cannot decode from the pixels, write `UNDECODABLE` (this is a finding, not a guess).
- **Reading order**: what order does the eye take, and does the layout imply a sequence/flow/hierarchy?
- **Color/shape semantics**: what does each color and each shape *appear* to mean? Is the same color
  reused for different things? Is meaning carried by color/position with **no legend to decode it**?
- **Ambiguities**: the explicit list of "I can't tell whether X means A or B from the picture alone."

A correct blind read of a broken visual will be full of `UNDECODABLE` and ambiguities — that is the
signal. Do not soften it with knowledge from the brief.

### Step 2 — Back-translate and score

Now place the `DERIVED READ` next to the `SOURCE INTENT` and diff them. Fill the rubric (do not emit
a vibe score — fill the form):

| Dimension | Weight | What full marks looks like |
|-----------|-------:|----------------------------|
| **Message fidelity** | 30 | The blind one-line message matches the source's intended takeaway. |
| **Encoding legibility** | 25 | Every meaning-bearing color/shape/position is **decodable from the picture** — there is a legend, inline label, or self-evident mapping. **Zero `UNDECODABLE` elements.** |
| **Element completeness** | 15 | Every source concept (each named part/stage/step) appears and is identifiable; nothing critical is missing or unlabeled. |
| **Order / structure** | 15 | Sequence, cycle, hierarchy, or comparison reads in the intended direction (a cycle reads as a cycle, not a timeline). |
| **No false signal** | 10 | The picture does not imply a category, ranking, or relationship the source never claims (e.g. arbitrary multi-color boxes implying types that don't exist). |
| **Standalone clarity** | 5 | A stranger gets the point in ~5 seconds without the caption/body. |
| **Total** | **100** | |

Compute the weighted total. Record every gap as a findings row using the shared compliance-severity
schema (`critical` = Error, `important` = Warning, `minor` = Info). Any `UNDECODABLE` meaning-bearing
element or any color/position that carries meaning **without a legend** is a `critical`
**legend/encoding gap** regardless of the numeric score.

### Pass criterion (hard gate)

A visual is **publish-ready** only when **all** hold:

1. weighted rubric total **>= 85**, AND
2. **zero unresolved legend/encoding gaps** (no `UNDECODABLE` meaning-bearing element; every
   color/shape/position that encodes meaning is decodable from the picture), AND
3. the blind one-line **message matches** the source intent (no inversion, no drift).

Score >= 85 with a surviving legend gap is **still a FAIL**. The legend/encoding gate is absolute.

### Step 3 — Clarifying questions (source-first, never guess)

For each ambiguity from the blind read, ask a precise question ("does the box color encode tool
category, or is it decorative?") and answer it **from the source concept first** — the blog passage,
then the design brief, then the renderer docstring. If the source concept genuinely does not settle
it, that is itself the defect: the visual is asking the reader to know something the picture never
shows. **Trigger a redraw — never guess and never invent a meaning to make the picture "work."**

### Step 4 — Self-evolving repair (edit the renderer, not just the output)

Because every visual here is produced by a deterministic program, the fix is a **program edit**, so
it is permanent and re-renders identically. Hand the findings to the renderer source and apply the
**smallest change that closes the gap**, preferring fixes in this order:

1. **Bind labels to elements** — put the name *on/under* each box/node/arrow (inline labels), or add a
   compact **legend** that maps color/shape -> meaning. A disconnected chip row that the reader must
   mentally re-attach to diagram elements is the classic gap; attach it.
2. **Make color honest** — if color does not encode a real category, collapse to one family (or a
   single accent) so it stops implying types that don't exist; if it *does* encode a category, add the
   legend that names each category.
3. **Make order readable** — number the steps, add a start marker and a labeled stop/exit, or orient
   the flow so a cycle reads as a cycle and a sequence reads left-to-right / top-to-bottom.
4. **Only if 1–3 cannot express the concept** — redraw the composition from the source concept.

The repair may **modify or enhance the renderer program itself** (add a legend helper, a label-binding
routine, a palette change) — this is the self-evolving step. Keep design-token, 320-DPI, Helvetica
Neue, ASCII-glyph (matplotlib) constraints. Re-render, then return to step 1 for a fresh blind read.

### Loop bound and escalation

Run at most **3 iterations**. If the asset still fails after the 3rd, **stop and escalate** with a
summary: the surviving gaps, the rubric trend across iterations, what was tried, and a concrete
recommendation (re-style, re-scope the concept, or human design call). Do not loop a 4th time.

## Output — the REVR record

Write one record per asset to `content/visuals/revr/<asset-stem>.md` so the gate is inspectable and
the loop is reproducible:

```
# REVR — p1-03-harness-vs-loop.png

- Source artifact: content/from-prompts-to-loop-engineering.md  (section "Harness ... nouns vs. verbs")
- Renderer: content/visuals/render_loop_engineering.py :: harness_vs_loop()
- Model (blind read): <GPT model name as shown in Copilot>

## Iteration 1
SOURCE INTENT: <2–4 lines: the takeaway + every named part/stage the picture must show>
DERIVED READ (blind): <one-line message; element inventory; order; color/shape semantics; ambiguities>
SCORE: <weighted total>/100
FINDINGS:
| # | Severity | Dimension | Finding | Fix applied to renderer |
|---|----------|-----------|---------|-------------------------|
| 1 | critical | Encoding legibility | 6 boxes colored blue/teal/purple with no legend; reads as 3 categories that don't exist | collapse to one accent + inline tool label per box |
VERDICT: FAIL (legend/encoding gap)

## Iteration 2
... (after renderer edit + re-render) ...
VERDICT: PASS (score 90, zero legend gaps, message matches)
```

A PASS record is the gate token. No PASS record (or an ESCALATE record) means the asset is **not**
publish-ready.

## Hard-gate wiring and status hygiene

- A REVR FAIL **blocks** the web-publish / deck / social steps for that asset, exactly like a
  `visual-reviewer` critical finding.
- Before applying repairs, update `content/pipeline-config.md`: set Status `in-progress`, Current Step
  to the visual-QA redo with date and reason, uncheck the visual step and downstream dependent steps,
  and mark any already-published visual/deck/social outputs **stale** until regenerated.
- After all assets reach PASS (or documented ESCALATE), re-run the Tier 0 preflight, re-mirror fixed
  PNGs to `docs/blog/visuals/`, and restore status.

## Research foundations (why REVR works)

REVR composes established, independently-validated ideas rather than a novel heuristic:

- **Round-trip / back-translation consistency.** In MT and program synthesis, translating `A -> B`
  then `B -> A` and diffing against `A` exposes meaning loss that a forward check misses. REVR applies
  the same to visuals: concept -> pixels -> recovered concept, then diff.
- **G-Eval / rubric-as-judge.** A judge that reasons against explicit rubric steps (chain-of-thought
  then form-filling) is more calibrated than an open-ended 1–10 score. REVR's weighted form is that
  rubric; the legend/encoding gate is the non-negotiable step.
- **Self-consistency / blind re-derivation.** Removing the prior (the brief) during the read prevents
  the reviewer's knowledge from silently repairing the picture — the same reason "have someone who
  never saw it describe it back" works in design crits.
- **Expressiveness & effectiveness (Mackinlay / Munzner).** A visual encoding must express all and
  only the facts in the data, using channels a human decodes accurately. Color/position carrying
  meaning **without a legend** violates expressiveness — REVR's `UNDECODABLE` and "no false signal"
  dimensions operationalize it.
- **Cleveland–McGill channel ranking.** Position and length decode more accurately than color hue;
  REVR's repair order (label/position fixes before relying on color) reflects this ranking.
- **Tufte data-ink / chartjunk + the 5-second ("squint") test.** Meaning should survive a glance and
  not depend on decorative encoding — REVR's standalone-clarity dimension and the honest-color repair.
- **Self-evolving deterministic renderers.** Because the asset is generated by code, the fix is a code
  edit (a legend helper, a label binder), making the correction permanent and reproducible rather than
  a one-off touch-up — the "modify the source program" answer to the review.

## Anti-patterns (do NOT)

- Do NOT read the source intent and *then* the picture — that defeats the blind read. Recover meaning
  from pixels first.
- Do NOT pass a visual at score >= 85 that still has a legend/encoding gap. The encoding gate is absolute.
- Do NOT guess a meaning to make an ambiguous picture "work" — answer from the source concept or redraw.
- Do NOT patch only the rendered PNG; edit the renderer program so the fix is permanent.
- Do NOT exceed 3 iterations — escalate with a summary instead.
- Do NOT leave pipeline status at a later/published step while REVR is reworking a visual.
