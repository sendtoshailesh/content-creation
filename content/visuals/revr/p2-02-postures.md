# REVR — p2-02-postures.png

- Source artifact: `content/from-prompts-to-loop-engineering.md` (humans outside / in / on the loop + flywheel)
- Renderer: `content/visuals/render_loop_engineering.py` :: `postures()` (hand-drawn / xkcd style)
- Model (blind read): GPT (multimodal) in GitHub Copilot

## SOURCE INTENT

Four human postures relative to the loop: OUTSIDE (vibe coding — own only the why), IN (gatekeep every
line — you are the bottleneck/limit), ON (build + tune the loop — where loop engineering lives),
FLYWHEEL (direct agents to improve the loop). Pivot: IN = fix the output; ON = fix the loop.

## Iteration 1 — PASS

DERIVED READ (blind):
- One-line message: "Four panels of a stick figure positioned relative to a loop — OUTSIDE (points at
  it), IN (inside it, marked BOTTLENECK / 'you are the limit'), ON (on top, 'loop engineering lives
  here'), FLYWHEEL (directing two loops) — IN fixes output, ON fixes the loop."
- Element inventory: each panel has a position name (OUTSIDE/IN/ON/FLYWHEEL) + a caption; the IN panel
  is flagged "[!] BOTTLENECK / you are the limit"; the ON panel is flagged "loop engineering lives
  here". Figure position encodes the posture and is explicitly named. Nothing `UNDECODABLE`.
- Color/shape semantics: per-panel color (blue/red/green/purple) tracks the posture label; red marks
  the bottleneck. Labels disambiguate.
- Order/structure: outside → in → on → flywheel reads as increasing leverage; pivot caption ties it.

SCORE: 94/100 (message 29 / encoding 23 / completeness 14 / order 14 / no-false-signal 9 / standalone 5)

VERDICT: **PASS** — score ≥ 85, zero legend/encoding gaps, blind message matches source intent.
