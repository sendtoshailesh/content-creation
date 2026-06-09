# Comic and Storyboard Grammar

Programmatic comic/storyboard visuals explain complex technical concepts through simple scenes, captions, callouts, and lightweight characters. They must be generated with Python/Pillow/SVG primitives only.

## Use Cases

- Production failure stories.
- Misaligned incentives or governance gaps.
- Before/after workflows.
- "What users think happens" vs. "what actually happens."
- Human consequences of technical choices.

## Standard Structures

### 3-Panel Problem / Realization / Fix

| Panel | Purpose | Content |
|---|---|---|
| 1 | Problem | Character encounters confusing failure or expensive outcome |
| 2 | Realization | Hidden system behavior is revealed with callout labels |
| 3 | Fix | Better framework, guardrail, or process resolves the issue |

### 4-Panel Escalation

| Panel | Purpose | Content |
|---|---|---|
| 1 | Setup | Normal workflow |
| 2 | Drift | Small mistake or assumption enters |
| 3 | Failure | Visible consequence, cost, or risk |
| 4 | Lesson | Concrete rule or visual takeaway |

### 6-Panel Storyboard

Use when a workflow needs more detail:

1. Context.
2. Trigger.
3. Hidden failure mode.
4. Detection.
5. Fix.
6. Reusable rule.

## Required Elements

- Title or thesis.
- 3-6 panels.
- One idea per panel.
- Caption under each panel.
- Optional speech bubbles; max 12 words each.
- Callouts for technical terms.
- Source line if any metric appears.

## Rendering Rules

- Use `scripts/visuals/comic.py` helpers.
- Use simple geometric characters and icons; do not require external image generation.
- Keep faces/characters symbolic and inclusive.
- Body text must be measured with `textbbox()` before drawing.
- Mobile readability matters more than artistic detail.

## Anti-Patterns

- Decorative cartoons without a technical lesson.
- More than two speech bubbles per panel.
- Tiny labels.
- Data without source line.
- Jokes that obscure the insight.

