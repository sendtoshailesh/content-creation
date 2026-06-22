---
name: visual-research
description: 'STORM-inspired four-phase pre-stage that decides a contradiction-aware, self-reviewed visual plan before any pixels are rendered. Discovers reader-perspectives, maps where they conflict, ranks visual decisions by confidence, self-critiques the plan, and writes a hierarchical mind map to content/visual-style-map.md. Use once per content run before styling/rendering.'
argument-hint: 'Provide the strategy/blog source, reference brief, and the run audiences'
---

# Visual Research Skill (STORM stage)

Adapts the **full** STORM / Co-STORM method — not just "list some perspectives" — to a visual
pack. STORM's value is its *method*: perspective-guided question asking + simulated conversation
grounded in sources, then outline → polish; Co-STORM adds a moderator and a dynamic mind map; the
4-prompt distillation adds the contradiction map, ranked synthesis, and the **self peer-review**
that STORM itself lacks. This skill runs those phases for visuals and writes
`content/visual-style-map.md`. See `agents-and-skills/visual-versatility-system.md` §7.

## When to Use

- Once per content run, **before** `visual-style-router`, `infographic-art-director`, and
  `visual-renderer`.
- Re-run when the audience set, reference brief, or blog thesis materially changes.

## Inputs

- The strategy or blog source.
- `content/reference-brief.md` (grounding; cite entries — grounding, not decoration).
- `content/pipeline-config.md` (run audiences, platforms, series vs. single).
- Existing `content/visual-opportunity-map.md` if present.

## Phase 1 — Perspective discovery + simulated questioning

- **Discover, don't hardcode.** Seed from the run's audiences (dev, tech lead, exec) **and
  discover reader-perspectives** that change what a visual must do, e.g. *the scanner* (3-second
  skim), *the chart-skeptic* (distrusts dashboards, wants the mechanism), *the visual learner*
  (needs a metaphor), *the accessibility-first reader* (contrast, standalone captions, no
  color-only meaning), *the printout reader* (mono, no color reliance).
- **Simulated questioning.** For each perspective run a short writer↔design-expert exchange (2–3
  follow-ups) grounded in the reference brief: *What must this reader see first? Which style earns
  their trust? What baked-in assumption fails them?* Answers cite reference-brief entries.

## Phase 2 — Contradiction map (the gap-finder)

The single highest-leverage anti-sameness step.

1. **Direct clashes** — name the two needs that collide (exec quick-scan exhibit vs. developer
   detailed mechanism; hand-drawn warmth vs. data precision; density vs. skimmability).
2. **Strongest vs. weakest** style evidence per clash.
3. The **one decision** that resolves the biggest clash — often *split into two assets in two
   styles*, one per audience (this is the versatility the pack needs).
4. **Universal agreement** → what every perspective needs becomes a **hero** visual.
5. **Blind spot** → a key claim **no** perspective would illustrate is the **missing visual**;
   add it (STORM's "unknown unknowns").

## Phase 3 — Synthesis into a ranked visual plan

- One-line **visual thesis** for the pack.
- **5 key visual decisions ranked by confidence**, each noting which perspectives
  support/challenge it.
- The **hidden connection** — a motif/palette/style rhythm that ties the pack together.
- The **one actionable style decision**.
- The **frontier/experimental** visual worth trying.

## Phase 4 — Self peer-review of the plan (STORM's fixed weakness)

Before any pixels:

- **Confidence (1–10)** per visual decision, with reasons.
- **Weakest link** — least-justified style choice + what would justify it.
- **Bias / dominance check** — did one style or one audience dominate the matrix? (The early
  warning for the "one-type" failure — blocking if yes; see §10 pre-render gate.)
- **Missing perspective** — is there a 6th reader-angle that changes the plan?
- **Overall grade** + the top fixes to apply before rendering.

## Phase 5 — Mind map + polish/dedup

- Build a **hierarchical** map, not a flat list:
  `topic → sub-themes → visual slots → {type, style, renderer, audience, confidence}`. This keeps
  a multi-part series coherent (Co-STORM mind map).
- Flag near-duplicate compositions for the post-render dedup pass and, if useful, a cohesive
  **cover/summary** visual (STORM `polish` + Co-STORM `reorganize()`).

## Output: `content/visual-style-map.md`

```markdown
# Visual Style Map

## Visual thesis
<one line>

## Perspectives discovered
- <perspective> — needs: <...>  (brief: <reference-brief id>)

## Contradiction map
| Clash | Need A | Need B | Resolution | Hero? | Blind spot |

## Ranked visual plan
| # | Slot | Type | Style | Renderer | Audience | Confidence | Supports / Challenges |

## Self peer-review
- Weakest link:
- Bias / dominance check:  PASS | FAIL — <which style/audience dominates>
- Missing perspective:
- Overall grade:

## Mind map
topic
  - sub-theme
    - slot {type, style, renderer, audience, confidence}
```

Every style choice must trace to a perspective, a contradiction resolution, and a confidence
score — auditable the way STORM grounds statements in citations.

## Handoff

Pass `content/visual-style-map.md` to `visual-style-router` (which fills/validates `style_id` +
renderer and runs the moderator move), then to `infographic-art-director` and `style-rendering`.
The `visual-reviewer` reads the **self peer-review** for its pre-render gate.
