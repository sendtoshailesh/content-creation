# REVR — p1-03-harness-vs-loop.png

- Source artifact: `content/from-prompts-to-loop-engineering.md` (section "Harness engineering vs. loop engineering: nouns vs. verbs")
- Renderer: `content/visuals/render_loop_engineering.py` :: `harness_vs_loop()`
- Model (blind read): GPT (multimodal) in GitHub Copilot

## SOURCE INTENT

Harness ≠ loop. **Harness = nouns = the assembled parts and sensors** (the rig): skills, CLIs,
tests, linters, type checkers, guardrails — "everything except the model." **Loop = verbs = the
cycle that uses the rig**: act → observe → verify → retry, with a **stop gate** (bounded exit).
Harness asks "what tools and sensors does the agent have?"; loop asks "how does it iterate, and what
makes it stop?" Every named part and every verb must be identifiable on the picture, and the cycle
must read as a cycle with a clear stop.

## Iteration 1 — FAIL (legend/encoding gap)

DERIVED READ (blind):
- One-line message: "Two panels — left 'Nouns / Harness = the rig' shows a box of six colored
  squares; right 'Verbs / Loop = the cycle' shows a ring of four nodes with a start dot and a red
  stop sign; a ≠ says they differ." Panel-title level matches; element level does not.
- Element inventory:
  - Left: 6 rounded squares colored blue/teal/purple in a 2×3 grid — `UNDECODABLE` which square is
    which tool; the 3 colors imply three categories that do not exist. 3 grey dots between squares —
    `UNDECODABLE` (assembly pins, unreadable).
  - Left chips (skills, CLIs, tests, linters, type checkers, guardrails) float in a row **disconnected**
    from the squares — reader must mentally re-attach. Legend/encoding gap.
  - Right: 4 white ring nodes — `UNDECODABLE` which is act/observe/verify/retry; node order not
    readable. Blue dot node — `UNDECODABLE` (start?). Red octagon reads "stop" by convention but is
    unlabeled.
  - Right chips (act, observe, verify, retry, stop) float **disconnected** from the nodes. Legend gap.
- Color/shape semantics: color carries apparent (false) category meaning with **no legend**.

SCORE: 46/100

FINDINGS:

| # | Severity | Dimension | Finding | Fix applied to renderer |
|---|----------|-----------|---------|-------------------------|
| 1 | critical | Encoding legibility | 6 boxes blue/teal/purple, no legend → reads as 3 categories that don't exist | collapse to one accent family; bind a tool label inside each card |
| 2 | critical | Element completeness | tool names live only in a disconnected chip row, not identifiable on the boxes | label each of the 6 cards: skills, CLIs, tests, linters, type checkers, guardrails; drop chip row |
| 3 | critical | Encoding legibility | 4 ring nodes unlabeled; can't tell which verb is which or the order | label each node with its verb + number 1–4 clockwise (act→observe→verify→retry) |
| 4 | important | No false signal | grey "assembly pin" dots read as meaningless noise | remove pins |
| 5 | important | Order/structure | stop octagon unlabeled and detached; exit not clearly "after verify" | label the octagon "stop", connect it from the cycle with an arrow + a "start" entry marker at act |

VERDICT: **FAIL** — score 46 < 85 and multiple unresolved legend/encoding gaps.

Renderer edited (self-evolving repair): rewrote `harness_vs_loop()` SVG to bind labels to every
element, use one honest color family per panel, number the cycle, and label the stop gate. Re-render
and re-read below.

## Iteration 2 — PASS

DERIVED READ (blind):
- One-line message: "Harness = a labelled rack of parts (skills, tests, CLIs, linters, type checkers,
  guardrails) = nouns; Loop = a numbered clockwise cycle 1 act → 2 observe → 3 verify → 4 retry with a
  start marker and a red stop octagon exiting after verify = verbs; the ≠ says they are different things."
- Element inventory: every part card is labelled (one blue family — no false categories); every cycle
  node carries a number AND a verb label; the start is marked at node 1; the red octagon is labelled
  "stop" and connected by an arrow from node 3 (verify). Nothing `UNDECODABLE`.
- Order/structure: numbers + chevrons make the cycle read as a cycle; stop exits after verify.

SCORE: 98/100 (message 29 / encoding 25 / completeness 15 / order 14 / no-false-signal 10 / standalone 5)

VERDICT: **PASS** — score ≥ 85, zero legend/encoding gaps, blind message matches source intent.
Gate token recorded.
