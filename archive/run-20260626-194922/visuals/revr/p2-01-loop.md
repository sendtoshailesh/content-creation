# REVR — p2-01-loop.png

- Source artifact: `content/from-prompts-to-loop-engineering.md` (the loop, plan→act→observe→verify→correct)
- Renderer: `content/visuals/render_loop_engineering.py` :: `loop_diagram()` (diagram-as-code flowchart)
- Model (blind read): GPT (multimodal) in GitHub Copilot

## SOURCE INTENT

The loop as an explicit cycle with a stop condition: Plan (goal + success criterion) → Act (use the
tools) → Observe (read the sensors) → Verify (the gate). The gate branches: "needs work" → Correct
(adjust + retry) → iterate back to Plan; "goal met / cap hit" → STOP. Must read as a bounded cycle.

## Iteration 1 — PASS

DERIVED READ (blind):
- One-line message: "Plan → Act → Observe → Verify (decision diamond); Verify branches 'needs work'
  → Correct → iterate (inner loop) back to Plan, or 'goal met / cap hit' → STOP — a bounded loop."
- Element inventory: every node carries verb + gloss (Plan/Act/Observe/Verify/Correct/STOP); every
  edge is labelled (iterate, needs work, goal met / cap hit). Decision is a diamond; STOP is a red
  terminal. Nothing `UNDECODABLE`.
- Color/shape semantics: node colors track stages; diamond = decision; red = stop — all reinforced by
  labels, no legend required.
- Order/structure: arrowed flow + labelled branches make the cycle and its exit unambiguous.

SCORE: 97/100 (message 30 / encoding 25 / completeness 15 / order 15 / no-false-signal 9 / standalone 3)

VERDICT: **PASS** — score ≥ 85, zero legend/encoding gaps, blind message matches source intent.
