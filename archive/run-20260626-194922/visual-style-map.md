# Visual Style Map

> STORM pre-stage for the 2-part series *From Prompts to Loop Engineering*. Written by
> `visual-strategist` using the `visual-research` + `visual-style-router` skills before any
> rendering. Source: `content/prompts-to-loop-engineering-strategy.md`,
> `content/creative-brief.md` (§7), `content/trend-research.md`, `content/pipeline-config.md`.
> Created 2026-06-22. Grounding ids reference `content/trend-research.md` §3 data table (D1–D12)
> and reference-brief themes A–E.

## Visual thesis

Draw the **leverage point physically moving up a level** — every visual should make a reader
feel the climb (word -> context -> rig -> loop) and then *see* the loop as a governed cycle, not
a vibe. Two structural heroes (the staircase, the loop) anchor the series; everything else is
proof, mechanism, or a posture decision hung off those two spines.

## Perspectives discovered (Phase 1)

| Perspective | What it needs first | Style that earns trust | Baked-in assumption that fails it | Grounding |
|---|---|---|---|---|
| **The reframe-seeker** (IC dev, primary) | The arc as one picture before any number | A crisp staircase they can locate themselves on | "Everyone already knows the eras" — they don't see them as *one* climb | Brief §4; trend §1 |
| **The chart-skeptic** (senior dev) | The *mechanism*, not a dashboard | Clean labeled flow + held-constant-harness framing | Pretty bars without the "same harness, different model" caveat | D4–D8; theme E |
| **The scanner** (3-sec skim on mobile) | One hero number / one shape | Big-type quote + single dominant chart | Dense multi-insight cards | Brief §5; infographic rule 6 |
| **The governance reader** (tech lead) | "Where should a human sit?" decision | A posture panel that flags the bottleneck | A flat 4-box grid with no state change | Morris, theme A; D-? |
| **The economics reader** (manager) | Per-task cost + the honest caveat | Before/after metric card + subsidy flag | Triumphant numbers with no cost-realism line | D1,D2,D8,D12 |
| **The accessibility / print reader** (6th, surfaced Phase 4) | Standalone captions, no color-only meaning, mono-safe | Labeled shapes + WARN/SUCCESS encoded by icon *and* text | Color-only pass/fail; tokens that vanish in grayscale | Brief §7; infographic rule 7 |

Simulated writer<->design-expert exchanges (condensed): the reframe-seeker and the chart-skeptic
**collide** — one wants a memorable napkin climb, the other distrusts anything that looks
hand-wavy. Resolution: the *hero staircase stays crisp/structural* (diagram-as-code), and the
*mechanism* of each era's ceiling goes hand-drawn (napkin) where precision is not the point.

## Contradiction map (Phase 2)

| Clash | Need A | Need B | Resolution | Hero? | Blind spot |
|---|---|---|---|---|---|
| Memorable vs. precise | Napkin warmth (reframe-seeker) | Exact rising-leverage axis (chart-skeptic) | Hero = crisp diagram-as-code; ceilings = hand-drawn | **Staircase hero** | — |
| Quick-scan vs. mechanism | Big number (scanner) | The cycle's gate + stop logic (chart-skeptic) | Loop hero shows the *whole* cycle but labels exactly one gate + one stop | **Loop hero** | — |
| Triumph vs. honesty | "76.8%! 1,300 PRs!" (economics) | "still subsidized; it still fails" (skeptic) | SWE-bench/Stripe carry the cost band; a dedicated limits card carries laziness/bias/drift | — | The **subsidy caveat** is a number no one wants to illustrate — make it a visible flag |
| Where-am-I vs. what-is-it | Posture decision (governance) | Definition of the loop (reframe-seeker) | Split: loop hero = *what it is*; four-posture panel = *where you sit* | — | "in the loop = you are the bottleneck" is the unillustrated punchline — flag it red |
| Universal agreement | Everyone needs to *see the climb* and *see the cycle* | — | The two heroes | **Both heroes** | — |

**Blind spot added (STORM unknown-unknown):** no source draws the *validation inversion* itself
— generation throughput rising while validation stays flat. That mechanism is the "why now," so
it earns its own asset (P2-03).

## Ranked visual plan (Phase 3)

One-line pack thesis: *the leverage point climbs, then the loop becomes the unit of work.*

| # | Slot | Type | Style | Renderer | Audience | Confidence | Supports / Challenges |
|---|---|---|---|---|---|---|---|
| 1 | Four-era staircase (HERO) | concept/process | diagram-as-code | matplotlib/SVG (clean schematic) | broad | 9 | Supports reframe-seeker, scanner; challenges chart-skeptic (must stay precise) |
| 2 | Loop diagram (HERO) | process (cycle) | diagram-as-code | matplotlib/SVG cycle graph | developer | 9 | Supports chart-skeptic, reframe-seeker; gate+stop label required |
| 3 | SWE-bench trajectory + cost band | statistical | data-exhibit | matplotlib | tech-lead/manager | 8 | Supports economics, skeptic; needs "same harness" caption |
| 4 | Stripe before/after | statistical | data-exhibit | matplotlib/Pillow | manager | 8 | Supports economics; challenged by honesty (pair with caveat) |
| 5 | Harness-vs-loop clarifier | comparison | editorial-illustration | SVG (gym/coach metaphor) | broad | 7 | Supports reframe-seeker; moderator-move variety pick |
| 6 | Four-posture panel | comparison/concept | hand-drawn | sketch (Rough.js/xkcd) | tech-lead | 8 | Supports governance; flag "in = bottleneck" red |
| 7 | Validation inversion (bottleneck) | statistical/flow | data-exhibit | matplotlib | manager | 7 | Supports economics; the added blind-spot asset |
| 8 | Era ceilings small-multiple | comparison | hand-drawn | sketch | developer | 7 | Supports skeptic on *why* each era capped |
| 9 | First-loop checklist | checklist | hand-drawn | sketch/Pillow | developer | 8 | Supports CTA; must show 4 ticked levers, not prose |
| 10 | Honest-limits card | list/statistical | hand-drawn | sketch/Pillow | broad | 7 | Supports honesty guardrail; subsidy flag visible |
| 11 | Pull-quote ("leverage point is moving") | quote | typographic | `styles.typographic` | broad | 8 | Supports scanner; the hook everywhere |

**Hidden connection (motif):** a single rising leverage axis / upward motion recurs — the
staircase rises, the loop tightens, the bottleneck chart diverges upward. Reuse the four-era
color ramp (ACCENT_3 word -> ACCENT_2 context -> ACCENT rig -> SUCCESS loop) as the through-line
palette so any asset signals "which era" by color alone (paired with text labels for a11y).

**One actionable style decision:** keep the two **heroes crisp (diagram-as-code)** and route the
*mental-model* assets (ceilings, posture, checklist, limits) **hand-drawn** so the pack reads as
"precise where it proves, sketchy where it teaches."

**Frontier / experimental:** the harness-vs-loop clarifier as **editorial-illustration** (gym +
equipment vs. coach + rep-scheme) — the one metaphor-led asset; highest payoff-per-pixel for the
"nouns vs. verbs" idea, and the deliberate variety injection.

## Self peer-review (Phase 4)

- **Weakest link:** the validation-inversion asset (P2-03, conf 7) — "throughput up / validation
  flat" risks looking invented. Justify with CircleCI's *directional* claim (D11) and label it
  explicitly as directional, not a measured y-axis. If it can't be grounded cleanly, demote to a
  flow diagram of "verification pulled into the inner loop" (no fake quantities).
- **Bias / dominance check:** **PASS.** Style histogram across the 10 blog companions:
  diagram-as-code ×2, data-exhibit ×3, hand-drawn ×3, typographic ×1, editorial-illustration ×1.
  No single style dominates; hand-drawn = 3/10 = 30% (< 50% cap). Audience histogram: developer
  ×4, tech-lead/manager ×4, broad ×3 — balanced across the three personas, no single audience
  owns the pack.
- **Missing perspective:** the **accessibility / print reader** (added above) changed two rules —
  every WARN/SUCCESS state must be encoded by icon **and** text, and the era color ramp must be
  paired with labels (never color-only).
- **Overall grade: A-.** Two strong structural heroes, a clean precise/sketchy split, balanced
  audiences. Top fixes before rendering: (1) ground or demote P2-03; (2) ensure both heroes carry
  exactly one labeled gate/step-axis so they don't bloat into multi-insight diagrams; (3) pair
  every triumphant data asset (SWE-bench, Stripe) with its cost/subsidy caveat in the source line.

## Package style matrix (Phase / router output)

> Adjacent visuals differ in style; series palette = {diagram-as-code, data-exhibit, hand-drawn,
> typographic} core + editorial-illustration once (moderator move). Single-style: avoided.

| Asset id | style_id | renderer | rationale | guardrails |
|---|---|---|---|---|
| P1-01 staircase (HERO) | diagram-as-code | matplotlib/SVG schematic | crisp 4-step climb + rising leverage axis | pre-render to PNG @320 DPI; label every step + date; color ramp + text labels (a11y) |
| P1-02 era ceilings | hand-drawn | sketch (Rough.js/xkcd) | "why each era capped" is a napkin idea | crisp digits via path-effect; edge-to-edge arrows; 3 panels, visible differing limit |
| P1-03 harness-vs-loop | editorial-illustration | SVG editorial | gym/equipment vs. coach/rep-scheme metaphor | NO baked text — overlay labels only; keep nouns/verbs split obvious |
| P1-04 SWE-bench trajectory | data-exhibit | matplotlib | hard benchmark numbers + cost band | "same harness, different model" caption; ASCII glyphs; visible source line + dataset date |
| P1-05 pull-quote | typographic | `styles.typographic` | one big hook idea | <= 12 words; one accent word in ACCENT |
| P2-01 loop diagram (HERO) | diagram-as-code | matplotlib/SVG cycle | the plan->act->observe->verify->correct cycle | label exactly one verification gate + one stop condition; ASCII arrows |
| P2-02 four-posture panel | hand-drawn | sketch | "where do you sit?" decision | flag "in = bottleneck" in WARN + text; 4 panels, posture visibly changes |
| P2-03 validation inversion | data-exhibit | matplotlib | the "why now" mechanism | label as DIRECTIONAL (CircleCI qualitative); no fabricated y-axis; or demote to flow |
| P2-04 Stripe before/after | data-exhibit | matplotlib/Pillow | before/after case-study metric | pair with subsidy caveat in source line; ~1,000 -> 1,300+ PRs/week + $1T+ |
| P2-05 first-loop checklist | hand-drawn | sketch/Pillow | 4 ticked levers, shippable CTA | `[x]` ASCII ticks; 4 items max; not prose |
| (std) honest-limits | hand-drawn | sketch/Pillow | laziness/bias/drift + subsidy flag | WARN encoded by icon + text; subsidy flag visible; standalone caption |

**Moderator move (Co-STORM):** the one *overlooked* style is **editorial-illustration** — used
exactly once (P1-03) as the metaphor-led variety win. **`blueprint`** is intentionally unused:
considered for the loop hero "how it's built" anatomy, but rejected because the dark schematic
look would fight the rising-leverage color ramp that ties the pack together. Recorded as the
considered-and-declined option.

## Mind map (Phase 5)

```text
From Prompts to Loop Engineering (2-part series)
├── Part 1 — The Staircase and the Rig (Eras 1-3 + harness)  [IC practitioner]
│   ├── Reframe (the hook)
│   │   └── P1-05 pull-quote {quote, typographic, broad, conf 8}
│   ├── The climb (the arc)
│   │   └── P1-01 four-era staircase {concept/process, diagram-as-code, broad, conf 9}  ★HERO
│   ├── Why each era capped
│   │   └── P1-02 era ceilings small-multiple {comparison, hand-drawn, developer, conf 7}
│   ├── Nouns vs. verbs (define the rig)
│   │   └── P1-03 harness-vs-loop clarifier {comparison, editorial-illustration, broad, conf 7}
│   └── Proof the rig matters
│       └── P1-04 SWE-bench trajectory + cost band {statistical, data-exhibit, tech-lead, conf 8}
└── Part 2 — Engineering the Loop (Era 4 payoff)  [tech lead / manager]
    ├── What the loop is
    │   └── P2-01 loop diagram {process/cycle, diagram-as-code, developer, conf 9}  ★HERO
    ├── Where the human sits
    │   └── P2-02 four-posture panel {comparison/concept, hand-drawn, tech-lead, conf 8}
    ├── Why now (the inversion)
    │   └── P2-03 validation inversion {statistical/flow, data-exhibit, manager, conf 7}
    ├── Proof at scale
    │   └── P2-04 Stripe before/after {statistical, data-exhibit, manager, conf 8}
    ├── The honest counterweight
    │   └── (std) honest-limits card {list, hand-drawn, broad, conf 7}
    └── Your first loop
        └── P2-05 first-loop checklist {checklist, hand-drawn, developer, conf 8}
```

Near-duplicate watch (post-render dedup): P1-04 and P2-04 are both data-exhibit charts — keep
P1-04 a **line/slope** (trajectory) and P2-04 a **before/after pair** (two bars) so they don't
read as the same composition. Optional series **cover** visual = a reduced staircase-with-nested-
loops motif tying both parts (defer unless the blog index needs it).

## Handoff

`content/visual-opportunity-map.md` carries the per-asset briefs, the rendering handoff, and the
deferred list. `visual-reviewer` reads this **self peer-review** (Phase 4) and the **package style
matrix** for its pre-render diversity gate before `visual-renderer` rasterizes anything.
