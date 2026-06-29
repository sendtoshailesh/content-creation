# REVR — p1-01-staircase.png

- Source artifact: `content/from-prompts-to-loop-engineering.md` (opening "four eras" arc)
- Renderer: `content/visuals/render_loop_engineering.py` :: `staircase()`
- Model (blind read): GPT (multimodal) in GitHub Copilot

## SOURCE INTENT

Four eras as ascending levels, each automating the craft below and pushing effort up a level:
1 WORD / prompt engineering (2022–2024) → 2 CONTEXT / context engineering (~Jun 2025) →
3 RIG / harness engineering (Feb 2026) → 4 LOOP / loop engineering (Sep 2025→Mar 2026). The reader
must be able to name each era, its engineering type, its definition, and its rough date, and see the
"automates the craft below" relationship.

## Iteration 1 — PASS

DERIVED READ (blind):
- One-line message: "Four stacked, numbered levels (WORD → CONTEXT → RIG → LOOP), each a labelled era
  with engineering type + definition + date, joined by 'automates the craft below' arrows — your
  level of work keeps moving up."
- Element inventory: every step carries number + era name + engineering type + one-line definition +
  date; connector arrows are labelled. Nothing `UNDECODABLE`.
- Color/shape semantics: per-step color (purple/teal/blue/green) is decorative differentiation, not a
  false category — each box is self-labelled, so no legend is required.
- Order/structure: numbers 1–4 + vertical stack + arrows make the progression unambiguous.

SCORE: 97/100 (message 30 / encoding 24 / completeness 15 / order 15 / no-false-signal 8 / standalone 5)

VERDICT: **PASS** — score ≥ 85, zero legend/encoding gaps, blind message matches source intent.
