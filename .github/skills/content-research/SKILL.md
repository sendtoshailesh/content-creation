---
name: content-research
description: 'STORM-inspired pre-stage that builds a contradiction-aware, self-reviewed content plan before the strategy outline is written. Discovers reader-perspectives, maps where sources and personas disagree, ranks the thesis and key arguments by confidence, self-critiques the plan for bias before any drafting, and writes a hierarchical outline tree to content/content-research-map.md. Use once per content run after the creative brief, before the strategy outline.'
argument-hint: 'Provide the creative brief, reference brief, and the run audiences'
---

# Content Research Skill (STORM stage)

Adapts the **full** STORM / Co-STORM method to content planning — STORM's native home, since it
is a research-and-writing method. STORM's value is its *method*: perspective-guided question
asking + simulated conversation grounded in sources, then outline → polish; Co-STORM adds a
moderator and a dynamic mind map; the 4-prompt distillation adds the contradiction map, ranked
synthesis, and the **self peer-review** that STORM itself lacks. This skill runs those phases for
the written content and writes `content/content-research-map.md`. It is the content-track twin of
the `visual-research` skill. See `agents-and-skills/visual-versatility-system.md` §7 for the
visual analog and the STORM-component mapping.

## When to Use

- Once per content run, **after** `creative-brief` and reference/trend research, and **before**
  `content-strategist` produces the strategy outline.
- Re-run when the audience set, reference brief, or topic angle materially changes.

## Inputs

- `content/creative-brief.md` (the run's objectives, audience, key message, guardrails).
- `content/reference-brief.md` (grounding; cite entries — grounding, not decoration).
- `content/trend-research.md` if present (market data, competitive landscape).
- `content/pipeline-config.md` (run audiences, platforms, series vs. single).

## Phase 1 — Perspective discovery + simulated questioning

- **Discover, don't hardcode.** Seed from the run's audiences (developer, tech lead, exec) **and
  discover reader-perspectives** that change *what the post must argue*, e.g. *the burned
  skeptic* (tried this and it failed, wants the failure mode named), *the ROI buyer* (needs the
  cost/benefit before the mechanism), *the IC implementer* (needs the concrete mechanism and
  trade-offs), *the migrator* (compares everything to their current stack), *the time-poor
  scanner* (needs the one takeaway in the first paragraph).
- **Simulated questioning.** For each perspective run a short writer↔expert exchange (2–3
  follow-ups) grounded in the reference brief: *What must this reader be convinced of first? What
  evidence earns their trust? Which assumption, if wrong, breaks the whole argument for them?*
  Answers cite reference-brief entries.

## Phase 2 — Contradiction map (the gap-finder)

The single highest-leverage step — it produces the thesis and prevents a bland "average of the
sources" post.

1. **Source clashes** — name where the evidence disagrees (vendor benchmark vs. independent test;
   optimistic case study vs. cautionary post-mortem). Note the strongest vs. weakest evidence
   per clash.
2. **Persona clashes** — name where readers want opposite things (exec wants ROI up front vs. IC
   wants the mechanism first; tutorial depth vs. skimmable takeaways).
3. The **one decision** that resolves the biggest clash **becomes the content thesis** — the
   post's point of view, not a hedge.
4. **Universal agreement** → what every perspective and source agrees on becomes the **must-make
   claim**, stated boldly and early.
5. **Blind spot** → a claim or angle **no** source covers and **no** persona would ask for is the
   **differentiator angle**; add it (STORM's "unknown unknowns").

## Phase 3 — Synthesis into a ranked argument plan

- One-line **content thesis** (the resolved clash from Phase 2).
- **5 key arguments ranked by confidence**, each noting which sources/perspectives
  support/challenge it and the evidence behind it.
- The **hidden connection** — the narrative throughline / motif that ties the arguments together.
- The **one contrarian take** worth leading with.
- The **frontier/experimental** claim worth testing (highest reward, lowest current evidence).

## Phase 4 — Self peer-review of the plan (STORM's fixed weakness)

Before any drafting:

- **Confidence (1–10)** per argument, with reasons and the evidence it rests on.
- **Weakest claim** — least-justified argument + what evidence would justify it.
- **Bias / dominance check** — did one source or one persona dominate the plan? (The early
  warning for a one-sided post — blocking if yes; the `content-strategist` must rebalance before
  outlining.)
- **Missing perspective** — is there a 6th reader-angle that changes the plan?
- **Overall grade** + the top fixes to apply before the outline is written.

## Phase 5 — Outline tree + dedup

- Build a **hierarchical** plan, not a flat list:
  `topic → sections → claims → {evidence, persona, confidence}`. This becomes the backbone the
  `content-strategist` turns into the outline, and it keeps a **multi-part series**
  non-overlapping (dedup claims across parts — Co-STORM mind map + STORM polish).
- Flag near-duplicate sections across parts for the scope assessment to consolidate.

## Output: `content/content-research-map.md`

```markdown
# Content Research Map

## Content thesis
<one line — the resolved biggest contradiction>

## Perspectives discovered
- <perspective> — wants: <...>  (brief: <reference-brief id>)

## Contradiction map
| Clash | Source/Persona A | Source/Persona B | Resolution | Becomes thesis? | Blind spot |

## Ranked argument plan
| # | Claim | Evidence | Supports / Challenges | Persona | Confidence |

## Self peer-review
- Weakest claim:
- Bias / dominance check:  PASS | FAIL — <which source/persona dominates>
- Missing perspective:
- Overall grade:

## Outline tree
topic
  - section
    - claim {evidence, persona, confidence}
```

Every claim must trace to a perspective, a contradiction resolution, and a confidence score —
auditable the way STORM grounds statements in citations.

## Cost note

STORM's five phases are token-heavy. Mirror the visual track's balance: use a lighter reasoning
pass for Phases 1–3 (discovery, contradiction map, synthesis) and reserve depth for Phase 4 (the
self peer-review), since that is where the value concentrates.

## Handoff

Pass `content/content-research-map.md` to `content-strategist`, which uses the **outline tree** as
the outline backbone, the **thesis** as the content angle, and the **self peer-review** as a
pre-write gate (a FAIL on the bias/dominance check must be fixed before outlining). The
`content-scope-assessment` skill reads the outline tree for series boundaries;
`multi-dimensional-analysis` reads the discovered perspectives instead of hardcoding personas;
`grounded-content-reviewer` reads the self peer-review as its pre-write checklist.
