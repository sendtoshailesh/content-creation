# REVR — p2-05-first-loop-checklist.png

- Source artifact: `content/from-prompts-to-loop-engineering.md` (your first loop — four things)
- Renderer: `content/visuals/render_loop_engineering.py` :: `first_loop_checklist()` (sketch checklist)
- Model (blind read): GPT (multimodal) in GitHub Copilot

## SOURCE INTENT

To ship your first loop, give one babysat task four things: (1) a clear goal with a success criterion,
(2) the tools to iterate — CLI, test runner, linter, (3) one machine-checkable feedback signal, (4) a
stop condition — max iterations or a definition of done.

## Iteration 1 — PASS

DERIVED READ (blind):
- One-line message: "Your first loop — four numbered items: 1 a clear goal + success criterion, 2 tools
  to iterate (CLI/test runner/linter), 3 one machine-checkable feedback signal, 4 a stop condition
  (max iterations or definition of done)."
- Element inventory: title + subtitle + four numbered cards, each fully labelled. Nothing `UNDECODABLE`.
- Color/shape semantics: green numbered badges as ordinals only — no encoded category.
- Order/structure: numbers 1–4 give explicit reading order.

SCORE: 96/100 (message 30 / encoding 25 / completeness 15 / order 15 / no-false-signal 10 / standalone 1)

VERDICT: **PASS** — score ≥ 85, zero legend/encoding gaps, blind message matches source intent.
