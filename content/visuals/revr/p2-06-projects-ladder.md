# REVR — p2-06-projects-ladder.png

- Source artifact: `content/from-prompts-to-loop-engineering.md` (three projects to try this week)
- Renderer: `content/visuals/render_loop_engineering.py` :: `projects_ladder()` (HTML/CSS → Chromium)
- Model (blind read): GPT (multimodal) in GitHub Copilot

## SOURCE INTENT

A laddered set of three build-it-yourself projects of increasing autonomy/time. BEGINNER (Project 1):
run a verify→correct loop in an agent (Copilot/Aider/Claude Code), success = tests exit 0 on an
agent edit while you wrote no code, ~90 min. INTERMEDIATE (Project 2): build the loop on a managed
runtime (Foundry Agent Service or Anthropic patterns), success = task resolved within iteration cap +
clean exit, half a day. ADVANCED (Project 3): platform-engineer the loop with gates (git-ape,
hve-core, mini-swe-agent), success = a tightened gate changes the outcome, a weekend.

## Iteration 1 — PASS

DERIVED READ (blind):
- One-line message: "Three ascending project cards — Beginner 'run a verify→correct loop' (~90 min),
  Intermediate 'build the loop on a managed runtime' (half a day), Advanced 'platform-engineer the loop
  with gates' (a weekend) — start here, climb toward more autonomy."
- Element inventory: each card has a level badge (BEGINNER/INTERMEDIATE/ADVANCED), project number +
  title, tool chip, SUCCESS SIGNAL, and TIME; a labelled 'start here → more autonomy' axis runs along
  the bottom. Nothing `UNDECODABLE`.
- Color/shape semantics: per-level color (teal/blue/green) tracks the badge; vertical staggering encodes
  the ladder and is reinforced by the axis label — no legend required.
- Order/structure: ascending placement + badges + axis make the progression explicit.
- Note: Unicode arrows (→) are acceptable here — HTML/CSS+Chromium renderer, not matplotlib.

SCORE: 96/100 (message 30 / encoding 24 / completeness 15 / order 15 / no-false-signal 9 / standalone 3)

VERDICT: **PASS** — score ≥ 85, zero legend/encoding gaps, blind message matches source intent.
