# Visual Opportunity Map — From Prompts to Loop Engineering (2-part series)

> Mandatory visual plan (Step 2d) for the 2-part series. Produced by `visual-strategist` using
> `visual-content-planning` + `infographic-design-system` + `visual-research` + `visual-style-router`.
> Sources: `content/prompts-to-loop-engineering-strategy.md`, `content/creative-brief.md` (§7),
> `content/trend-research.md` (data table D1–D12), `content/pipeline-config.md`. Companion research
> + style diversity gate: `content/visual-style-map.md`. Created 2026-06-22.
>
> **Planning only — nothing is rendered yet.** Status on every row is `planned`.

## Summary

- **Visual count:** Part 1 = **5** blog companions; Part 2 = **5** blog companions; **10 total**
  blog companions, plus reformatted LinkedIn and deck derivatives (no new information, reflow only).
- **Two HERO assets:**
  1. **P1-01 — the four-era staircase** (word -> context -> rig -> loop, leverage point rising) for
     **Part 1**.
  2. **P2-01 — the loop diagram** (plan -> act -> observe -> verify -> correct, with the verification
     gate + stop condition called out) for **Part 2**.
- **Priority split:** 4 × P0 (both heroes + SWE-bench + Stripe), 5 × P1, 1 × P1 standalone
  (honest-limits). No P2 blog companions this run.
- **Style diversity (pre-render gate):** PASS — diagram-as-code ×2, data-exhibit ×3, hand-drawn ×3,
  typographic ×1, editorial-illustration ×1; hand-drawn = 30% (< 50% cap); no two adjacent visuals
  share a style; series palette = 4 core styles + 1 moderator-move style. Full matrix and self
  peer-review live in `content/visual-style-map.md`.
- **Design tokens (enforced on every asset):** BG `#ffffff`; ACCENT `#1f6feb`; ACCENT_2 `#0d9488`;
  ACCENT_3 `#7c3aed`; WARN `#dc2626`; SUCCESS `#16a34a`; TEXT `#1e293b`; **Helvetica Neue**;
  **320 DPI**; **ASCII glyphs only in matplotlib** (`->`, `[x]`, `[ ]`). Era color ramp:
  word = ACCENT_3, context = ACCENT_2, rig = ACCENT, loop = SUCCESS (always paired with text labels
  for accessibility — never color-only).

### Opportunity index

| ID | Part / Section | Type | Style | Priority | Hero | Status |
|---|---|---|---|:--:|:--:|---|
| P1-05 | P1 §1 Hook | quote | typographic | P1 | | planned |
| P1-01 | P1 §2 The staircase | concept/process | diagram-as-code | P0 | ★ | planned |
| P1-02 | P1 §3 Eras 1-3 fast-forward | comparison | hand-drawn | P1 | | planned |
| P1-03 | P1 §5 Harness vs. loop (nouns) | comparison | editorial-illustration | P1 | | planned |
| P1-04 | P1 §8 SWE-bench proof | statistical | data-exhibit | P0 | | planned |
| P2-01 | P2 §4 What the loop is | process (cycle) | diagram-as-code | P0 | ★ | planned |
| P2-02 | P2 §6 Humans outside/in/on | comparison/concept | hand-drawn | P1 | | planned |
| P2-03 | P2 §7 Why now (bottleneck) | statistical/flow | data-exhibit | P1 | | planned |
| P2-04 | P2 §8 Stripe + SWE-bench | statistical | data-exhibit | P0 | | planned |
| P2-05 | P2 §10 Your first loop | checklist | hand-drawn | P1 | | planned |
| STD-LIMITS | P2 §9 + LinkedIn | list/statistical | hand-drawn | P1 | | planned |

---

## Blog Companion Visuals

### Part 1 — The Staircase and the Rig (5 visuals; IC practitioner)

#### P1-05 — "Your leverage point is moving" pull-quote
- **Source section / placement:** P1 §1 The hook (top-of-post + social hook).
- **Burning question:** Why is "get better at prompting" the wrong question?
- **Concept type / Infographic type:** quote.
- **Audience persona:** broad (every reader).
- **Visual family / Style:** typographic (text-as-art) — `style_id: typographic`.
- **Platform fit / placement:** Blog hero strip · LinkedIn hook card (Part 1) · deck title slide.
- **Standalone potential:** High.
- **Required source data:** none (thesis line, brief §4). One accent word ("moving") in ACCENT.
- **Rendering approach:** `scripts.visuals.styles.typographic` (SVG/HTML, 320 DPI).
- **Priority:** P1. **Confidence:** 8.

#### P1-01 — The four-era staircase  ★HERO
- **Source section / placement:** P1 §2 The staircase: four eras, one moving target.
- **Burning question:** What is the single arc that connects prompt -> context -> harness -> loop?
- **Concept type / Infographic type:** concept / process (step ladder with a rising leverage axis).
- **Audience persona:** broad.
- **Visual family / Style:** diagram-as-code (crisp schematic) — `style_id: diagram-as-code`.
- **Platform fit / placement:** Blog §2 hero figure · LinkedIn carousel seed (Part 1) · deck "the arc" slide.
- **Standalone potential:** High — this is the genuinely-missing "full arc as one diagram."
- **Required source data:** four eras + what you engineer + dates — **word** (prompt eng., 2022–2024),
  **context** (window, ~Jun 2025), **rig** (harness, Feb 2026), **loop** (cycle, Sep 2025 ->
  Mar 2026). Source: trend-research §1 table; Fowler "Exploring Gen AI" index; Böckeler; Willison.
- **Rendering approach:** matplotlib/SVG custom step diagram, 320 DPI, ASCII arrows (`->`); era color
  ramp (ACCENT_3 -> ACCENT_2 -> ACCENT -> SUCCESS) + text labels.
- **Priority:** **P0**. **Confidence:** 9.

#### P1-02 — Era ceilings small-multiple
- **Source section / placement:** P1 §3 Eras 1-3 in fast-forward.
- **Burning question:** Why did each earlier era hit a ceiling and push the human up a level?
- **Concept type / Infographic type:** comparison (three small "ceiling" panels).
- **Audience persona:** developer.
- **Visual family / Style:** hand-drawn napkin sketch — `style_id: hand-drawn`.
- **Platform fit / placement:** Blog §3 inline · deck "how we climbed" slide.
- **Standalone potential:** Medium.
- **Required source data:** three limiting factors — prompt era = *diminishing returns on wording of
  one call*; context era = *a static window can't adapt mid-task*; harness era = *a great rig still
  needs a cycle to run in*. Proof tie-in: mini-SWE-agent **65% on SWE-bench Verified in ~100 lines**
  (D6). Source: trend-research §1, D6.
- **Rendering approach:** `sketch` (Rough.js / xkcd-style), three panels with a visibly *different*
  ceiling per panel (no repeated icon), crisp digits.
- **Priority:** P1. **Confidence:** 7.

#### P1-03 — Harness vs. loop clarifier (nouns vs. verbs)
- **Source section / placement:** P1 §5 Harness vs. loop: nouns vs. verbs.
- **Burning question:** What exactly is the difference between the harness and the loop?
- **Concept type / Infographic type:** comparison (split-screen metaphor).
- **Audience persona:** broad.
- **Visual family / Style:** editorial-illustration (the one metaphor-led asset / moderator move) —
  `style_id: editorial-illustration`.
- **Platform fit / placement:** Blog §5 · LinkedIn "the one distinction" card (high-save, Part 1) ·
  deck "harness != loop" slide.
- **Standalone potential:** High.
- **Required source data:** **Harness = the rig (nouns)** — "everything except the model"; guides +
  sensors (conventions, docs, skills, CLIs, MCP, linters, tests). **Loop = the cycle (verbs)** —
  act -> observe -> verify -> retry -> stop; the evaluator-optimizer cycle. Metaphor: *gym + equipment*
  vs. *rep-scheme + coach who decides when you're done*. Source: Böckeler (D9, theme C); Anthropic
  evaluator-optimizer (theme A).
- **Rendering approach:** SVG editorial illustration; **no baked text — overlay labels only**;
  left = equipment/nouns, right = coach/verbs.
- **Priority:** P1. **Confidence:** 7.

#### P1-04 — SWE-bench trajectory + cost band
- **Source section / placement:** P1 §8 (harness-matters proof half).
- **Burning question:** What proves the rig and the cycle — not the prompt — drive results?
- **Concept type / Infographic type:** statistical (slope / trajectory line).
- **Audience persona:** tech lead / manager.
- **Visual family / Style:** data-exhibit — `style_id: data-exhibit`.
- **Platform fit / placement:** Blog §8 · LinkedIn data-proof card (Part 1) · deck data slide.
- **Standalone potential:** High.
- **Required source data:** **12.47% (Mar 2024) -> 76.8% (Claude 4.5 Opus, Feb 2026)** under the
  *same* harness; per-task cost band **~$0.05–$0.96**; SWE-bench Verified = **500 human-filtered
  instances, identical harness across models** (D4, D5, D7, D8). Caption must say "same harness,
  different model." Source line: swebench.com, Feb 2026 / v2.0.0.
- **Rendering approach:** matplotlib line/slope + shaded cost band, 320 DPI, ASCII glyphs, visible
  source line **with dataset date**.
- **Priority:** **P0**. **Confidence:** 8.

### Part 2 — Engineering the Loop (5 visuals; tech lead / manager)

#### P2-01 — The loop diagram  ★HERO
- **Source section / placement:** P2 §4 What loop engineering actually is.
- **Burning question:** What does the governed iteration cycle actually look like?
- **Concept type / Infographic type:** process (closed cycle).
- **Audience persona:** developer.
- **Visual family / Style:** diagram-as-code (cycle graph) — `style_id: diagram-as-code`.
- **Platform fit / placement:** Blog §4 hero figure · LinkedIn body card (Part 2) · deck "the loop"
  slide · Reel core-demo overlay.
- **Standalone potential:** High.
- **Required source data:** the cycle **plan -> act -> observe -> verify -> correct**, with **exactly one
  verification gate** and **one stop condition** ("maximum number of iterations to maintain control")
  labeled; the four design levers (clear goal + success criteria, tools to iterate, a feedback signal,
  scoped credentials / stop condition). Source: Willison Sep 2025 (theme A); Anthropic
  evaluator-optimizer + stop condition (D-, theme A).
- **Rendering approach:** matplotlib/SVG closed-loop diagram, ASCII arrows (`->`), gate drawn as a
  SUCCESS/WARN check node (icon + text), 320 DPI.
- **Priority:** **P0**. **Confidence:** 9.

#### P2-02 — Humans outside / in / on the loop (four-posture panel)
- **Source section / placement:** P2 §6 Who sits where.
- **Burning question:** Where should a human sit — and which posture makes you the bottleneck?
- **Concept type / Infographic type:** comparison / concept (four-posture panel).
- **Audience persona:** tech lead.
- **Visual family / Style:** hand-drawn — `style_id: hand-drawn`.
- **Platform fit / placement:** Blog §6 · LinkedIn "are you the bottleneck?" carousel (Part 2) · deck
  "where do you sit?" slide · Reel beat.
- **Standalone potential:** High.
- **Required source data:** four postures — **outside** (vibe coding — own only the why), **in**
  (gatekeep every line — *the bottleneck*, flagged WARN + text), **on** (build/tune the loop — where
  loop engineering lives), **agentic flywheel** (direct agents to improve the loop). Pivot line: *in*
  = fix the artefact; *on* = fix the loop that produced it. Source: Kief Morris, Mar 2026 (theme A).
- **Rendering approach:** `sketch`; four panels with **visibly changing** posture (no repeated icon);
  "in = bottleneck" badge in WARN with text label.
- **Priority:** P1. **Confidence:** 8.

#### P2-03 — The validation inversion (bottleneck)
- **Source section / placement:** P2 §7 Why now: validation, not generation, is the bottleneck.
- **Burning question:** Why is loop engineering emerging *now*?
- **Concept type / Infographic type:** statistical / flow (divergence + inner-loop callout).
- **Audience persona:** manager.
- **Visual family / Style:** data-exhibit — `style_id: data-exhibit`.
- **Platform fit / placement:** Blog §7 · LinkedIn "why now" card (Part 2) · deck "the inversion" slide.
- **Standalone potential:** Medium-High.
- **Required source data:** generation throughput rising while validation/production deploys stay flat;
  the fix = verification pulled **into the inner loop** (CircleCI Chunk Sidecars, Dropbox Nova, Claude
  Code). **Label as DIRECTIONAL** — CircleCI's claim is qualitative (D11); **no fabricated y-axis
  values.** If it cannot be grounded cleanly, demote to a pure flow diagram of "verification moved
  into the inner loop." Source: CircleCI via InfoQ, Jun 2026 (D11); OpenAI via Böckeler (D9).
- **Rendering approach:** matplotlib two-line divergence (clearly marked directional) + an inner-loop
  callout box; 320 DPI; ASCII glyphs.
- **Priority:** P1. **Confidence:** 7 (weakest-link — see `visual-style-map.md` self peer-review).

#### P2-04 — Stripe before/after + SWE-bench proof at scale
- **Source section / placement:** P2 §8 Proof at scale: Stripe Minions + the SWE-bench trajectory.
- **Burning question:** Does harness + loop actually work in production at scale?
- **Concept type / Infographic type:** statistical (before/after metric pair).
- **Audience persona:** manager.
- **Visual family / Style:** data-exhibit — `style_id: data-exhibit`.
- **Platform fit / placement:** Blog §8 · LinkedIn data-proof card (Part 2) · deck data slide ·
  Reel "the numbers" beat.
- **Standalone potential:** High.
- **Required source data:** Stripe Minions **~1,000 -> 1,300+ PRs/week**, **zero human-written code**
  (all human-reviewed), underpinning **$1T+** annual payment volume; architecture = "blueprints =
  deterministic code interwoven with flexible agent loops" + CI/CD/tests/static-analysis harness
  (D1, D2). Pair with the SWE-bench cost realism in the **source line: per-task cost ~$0.05–$0.96;
  pricing "still very subsidized" (Böckeler, Jun 2026, D12).** Source: InfoQ -> Stripe, Mar 2026.
- **Rendering approach:** matplotlib/Pillow **before/after two-bar pair** (kept compositionally
  distinct from P1-04's slope line — see dedup note); 320 DPI; source line with subsidy caveat.
- **Priority:** **P0**. **Confidence:** 8.

#### P2-05 — Your first loop (checklist)
- **Source section / placement:** P2 §10 Your first loop: where to start this week.
- **Burning question:** What is the one shippable first step?
- **Concept type / Infographic type:** checklist (saveable action card).
- **Audience persona:** developer.
- **Visual family / Style:** hand-drawn — `style_id: hand-drawn`.
- **Platform fit / placement:** Blog §10 · LinkedIn CTA card (Part 2) · deck final/CTA slide ·
  Reel closing line.
- **Standalone potential:** High.
- **Required source data:** four ticked levers — **[x] clear goal + success criteria · [x] tools to
  iterate · [x] one machine-checkable feedback signal (tests/types/linter) · [x] a stop condition**;
  then step *on* the loop and fix the loop, not the output. First-party proof tie-in: this pipeline's
  plan -> draft -> rubber-duck review -> fix -> re-review loop. Source: Willison's four levers (theme A);
  `agents-and-skills/content-pipeline-flow.md`.
- **Rendering approach:** `sketch`/Pillow checklist with `[x]` ASCII ticks, 4 items max (not prose).
- **Priority:** P1. **Confidence:** 8.

---

## Standalone Distribution Visuals

> LinkedIn and the slide deck are served primarily by **reformatted derivatives** of the 10 blog
> companions (reflow to platform aspect ratio; **no new information**). One asset below is authored
> standalone because §9 is short and the limits are better carried by a dedicated card.

### STD-LIMITS — The honest counterweight card (standalone)
- **Source section / placement:** P2 §9 The honest counterweight (inline strip) **and** LinkedIn
  credibility post (Part 2). Required by the creative-brief honesty guardrail (§9).
- **Burning question:** Why is loop engineering a discipline, not a victory lap?
- **Concept type / Infographic type:** list / statistical (three failure modes + a flag).
- **Audience persona:** broad (credibility / trust).
- **Visual family / Style:** hand-drawn warning card — `style_id: hand-drawn`.
- **Platform fit / placement:** Blog §9 inline strip · LinkedIn credibility card (Part 2) · deck
  "the caveats" slide.
- **Standalone potential:** High.
- **Required source data:** three named self-correction failure modes — **agentic laziness ·
  self-preferential bias · goal drift** (Anthropic via InfoQ, Jun 2026, D10) — plus the **subsidy
  flag**: agent pricing "still very subsidized" (Böckeler, Jun 2026, D12). Source lines required.
- **Rendering approach:** `sketch`/Pillow; WARN encoded by **icon + text** (not color-only); visible
  subsidy flag; standalone caption.
- **Priority:** P1. **Confidence:** 7.

### LinkedIn reformat set (derivatives — no new data)
- **Part 1:** P1-05 (hook) · P1-01 (staircase carousel seed) · P1-03 (the-one-distinction, high-save)
  · P1-04 (data proof). Square `1080x1080` or carousel `1080x1350`.
- **Part 2:** P2-01 (the loop) · P2-02 ("are you the bottleneck?" carousel) · P2-04 (data proof) ·
  P2-05 (CTA) · STD-LIMITS (credibility). Square/carousel sizes as above.

### Slide deck mapping (full-arc deck, both parts; 16:9 `1920x1080` reformats)
| Deck slide | Reuses |
|---|---|
| Title | P1-05 pull-quote |
| The arc | P1-01 staircase ★ |
| How we climbed | P1-02 era ceilings |
| Harness != loop | P1-03 clarifier |
| The proof (rig) | P1-04 SWE-bench trajectory |
| The loop | P2-01 loop diagram ★ |
| Where do you sit? | P2-02 four-posture |
| The inversion | P2-03 validation inversion |
| Proof at scale | P2-04 Stripe before/after |
| The caveats | STD-LIMITS |
| CTA | P2-05 first-loop checklist |

---

## Rendering Handoff

> For `visual-renderer`. Every asset: BG `#ffffff`, Helvetica Neue, **320 DPI**, ASCII glyphs only in
> matplotlib, era color ramp paired with text labels. Dispatch by `style_id`; route through the
> **Visual Versatility System** style adapters per `content/visual-style-map.md` (no adjacent style
> repeats; hand-drawn capped < 50%). **Route the metaphor asset (P1-03) and the sketch assets (P1-02,
> P2-02, P2-05, STD-LIMITS) through the versatility adapters explicitly** so the pack does not funnel
> into one look.

```markdown
### P1-01  ★HERO — four-era staircase
- Style: diagram-as-code | Renderer: matplotlib/SVG schematic | Size: 1600x900 (blog), 1920x1080 (deck)
- Message: the leverage point climbs word -> context -> rig -> loop.
- Data: 4 eras + "what you engineer" + dates (trend §1 table); color ramp ACCENT_3->ACCENT_2->ACCENT->SUCCESS
- Burning question: What single arc connects the four eras?
- Infographic type: concept/process (rising step ladder)
- Visual metaphor: a staircase whose tread height = leverage
- State changes: each step automates the prior craft; human moves up
- Text budget: step labels <= 3 words; one-line caption
- Icon/illustration plan: 4 steps, a rising leverage arrow, dates on a baseline rail
- Visual-reviewer acceptance: every step labeled + dated; leverage axis legible; color + text (a11y); no multi-insight bloat

### P2-01  ★HERO — the loop diagram
- Style: diagram-as-code | Renderer: matplotlib/SVG cycle | Size: 1600x900 (blog), 1920x1080 (deck)
- Message: a governed cycle with a verification gate and a stop condition.
- Data: plan -> act -> observe -> verify -> correct; 1 gate + 1 stop condition; 4 design levers (Willison; Anthropic)
- Burning question: What does the governed iteration cycle look like?
- Infographic type: process (closed cycle)
- Visual metaphor: a tightening loop
- State changes: verify branches pass -> stop / fail -> correct -> re-enter
- Text budget: node labels <= 2 words; gate + stop callouts <= 6 words
- Icon/illustration plan: 5 cycle nodes, 1 gate (check), 1 stop node, ASCII arrows
- Visual-reviewer acceptance: exactly one gate + one stop labeled; closed loop reads in 3s; ASCII glyphs; no second insight

### P1-04 — SWE-bench trajectory + cost band
- Style: data-exhibit | Renderer: matplotlib | Size: 1600x900
- Message: same harness, different model -> 12.47% -> 76.8%.
- Data: 12.47% (Mar 2024) -> 76.8% (Feb 2026); cost ~$0.05–$0.96; 500 instances, identical harness (D4,5,7,8)
- Burning question: What proves the rig/cycle, not the prompt, drives results?
- Infographic type: statistical (slope/trajectory)
- Visual metaphor: a rising line under a fixed rig
- State changes: score climbs while harness is held constant
- Text budget: title <= 9 words; "same harness, different model" caption
- Icon/illustration plan: line + shaded cost band; endpoints annotated
- Visual-reviewer acceptance: source line + dataset date visible; cost band labeled; distinct from P2-04 (slope, not bars)

### P2-04 — Stripe before/after
- Style: data-exhibit | Renderer: matplotlib/Pillow | Size: 1600x900
- Message: harness + loop in production at $1T+ scale.
- Data: ~1,000 -> 1,300+ PRs/week; zero human-written code; $1T+ volume (D1,D2); subsidy caveat in source line (D12)
- Burning question: Does harness + loop work at scale?
- Infographic type: statistical (before/after two-bar)
- Visual metaphor: a step up in throughput
- State changes: before vs. after bars
- Text budget: title <= 9 words; metric labels <= 4 words
- Icon/illustration plan: 2 bars + $1T+ context chip
- Visual-reviewer acceptance: before/after explicit; "zero human-written code" noted; subsidy caveat in source line; bars (not a slope line)

### P1-02 / P2-02 / P2-05 / STD-LIMITS — hand-drawn set
- Style: hand-drawn | Renderer: sketch (Rough.js/xkcd) | Size: 1600x900 (blog), 1080x1350 (carousel)
- Guardrails: crisp digits via path-effect; edge-to-edge arrows; visible state change per panel; no repeated icon; `[x]` ASCII ticks (P2-05)
- Per-asset data + acceptance: see each row above; WARN/SUCCESS encoded by icon + text (a11y)

### P1-03 — harness vs. loop (editorial-illustration, moderator move)
- Style: editorial-illustration | Renderer: SVG editorial | Size: 1600x900
- Guardrail: NO baked text — overlay labels only
- Metaphor: gym + equipment (nouns) vs. rep-scheme + coach (verbs)
- Visual-reviewer acceptance: nouns/verbs split obvious without reading; metaphor legible in 3s

### P1-05 — pull-quote (typographic)
- Style: typographic | Renderer: scripts.visuals.styles.typographic | Size: 1080x1080 / 1920x1080
- Text: "You're not getting better at prompting. Your leverage point is moving." (<= 12 words; "moving" in ACCENT)
```

---

## Deferred / Follow-On Visuals

- **Optional AI hero/backdrop (opt-in, programmatic mode):** abstract "rising staircase of nested
  loops, each tighter than the last," ~30% negative space, **no embedded text**, brand-color fidelity
  (creative-brief §7). Gated behind `image_generation` mode in `pipeline-config.md` (currently
  `programmatic`); runs through `image-content-agent` + `vision-grounding` + inspector. **Not a blog
  companion** — mood only.
- **Series cover / summary motif:** reduced staircase-with-nested-loops tying Part 1 + Part 2 on the
  blog index. Defer unless the index needs a unifying header.
- **Reel screen-cues (out of this map's scope):** the live agent plan->act->observe->verify->correct
  terminal loop + this repo's review-gate loop are *recordings*, not rendered assets — handled by the
  Reel script step, reusing P1-01 (screen-cue) and P2-01 (overlay).
- **`blueprint` style:** considered for the loop hero "how it's built" anatomy and **declined** (would
  fight the era color ramp) — recorded in the moderator move. Revisit only if a deep "anatomy of a
  harness" asset is added in a future part.
- **mini-SWE-agent "65% in ~100 lines" standalone stat card:** currently folded into P1-02's caption
  (D6). Promote to its own data-exhibit micro-card only if Part 1 needs an extra LinkedIn data hook.

---

## Strategy markers

The strategy outline already carries `[VISUAL: ...]` markers at §1, §2, §3, §4, §5, §6, §7, §8, §9,
§10 in `content/prompts-to-loop-engineering-strategy.md`. They map 1:1 to the assets above (the §6,
§7, §9 markers belong to Part 2 / STD-LIMITS). No re-marking needed; mapping is recorded in the
opportunity index. The two hero markers (§2 staircase, §4 loop) are the P0 anchors.
