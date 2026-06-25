# REVR — p2-03-bottleneck.png

- Source artifact: `content/from-prompts-to-loop-engineering.md` (why now: validation, not generation)
- Renderer: `content/visuals/render_loop_engineering.py` :: `bottleneck()` (matplotlib, schematic)
- Model (blind read): GPT (multimodal) in GitHub Copilot

## SOURCE INTENT

Generation rises fast while validation stays ~flat, so the gap (the bottleneck) widens over time; the
fix is to pull verification INTO the inner loop (CircleCI Chunk Sidecars, Dropbox Nova, Claude Code).
Axes are directional/qualitative, not measured — must be disclaimed.

## Iteration 1 — PASS

DERIVED READ (blind):
- One-line message: "Generation (solid blue) climbs while validation (grey dashed, flat) barely moves;
  the red-shaded 'widening bottleneck' between them grows over time — fix: pull verification into the
  inner loop. Marked DIRECTIONAL."
- Element inventory: both lines labelled inline ('generation', 'validation (flat)'); the gap labelled
  'the widening bottleneck'; green fix callout names three tools; axes labelled 'time ->' and
  'relative volume (directional)'; a red DIRECTIONAL flag + a schematic/source footer. Nothing
  `UNDECODABLE`.
- Color/shape semantics: blue solid = generation, grey dashed = validation, red fill = the gap — all
  labelled inline, no legend required.
- No false signal: the DIRECTIONAL flag + "axes carry no measured values" footer prevent reading the
  schematic as real data.

SCORE: 95/100 (message 29 / encoding 24 / completeness 14 / order 14 / no-false-signal 10 / standalone 4)

VERDICT: **PASS** — score ≥ 85, zero legend/encoding gaps, blind message matches source intent.
