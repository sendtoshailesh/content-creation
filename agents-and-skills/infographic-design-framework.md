# Infographic Design Framework for Visual-First Content

This framework upgrades the visual-first content pipeline from "render text as cards" to research-backed infographic design.

## Why This Exists

The first visual-first pilot was technically valid but visually below the bar:

- The Sourdough Test storyboard repeated the same human icon without meaningful visual change.
- The four-layer eval system looked like simple text blocks rather than an infographic.
- Several assets explained through text instead of visual metaphor, hierarchy, and state change.

The new framework makes art direction mandatory before rendering.

## Reference Base

| Source | Pipeline lesson |
|---|---|
| GraphicMama, "What Is an Infographic?" | Infographics simplify heavy data, use minimal text, tell a story, and need white space plus audience fit. |
| Venngage, "What Is an Infographic?" | Infographics are imagery + data visualizations + minimal text for quick understanding. |
| Venngage, "9 Types of Infographics" | Choose type by goal: process, statistical, informational, timeline, comparison, hierarchy, list, etc. |
| Venngage, "How to Make an Infographic" | Start from goals, gather data, transform data into visuals, design layout, style, review, publish. |
| Adobe Express, "What Is an Infographic?" | Use visuals, symbols, charts, diagrams, and bite-sized information to make complex topics shareable. |
| github/awesome-copilot | Package reusable guidance as skills, references, agents, and workflows. |
| Data visualization GitHub ecosystem | Use composable tools and curated references for charts, diagrams, data stories, and rendering systems. |

## New Agent/Skill Workflow

| Stage | Owner | Output |
|---|---|---|
| Visual opportunity mapping | `visual-strategist` + `visual-content-planning` | `content/visual-opportunity-map.md` |
| Infographic art direction | `infographic-art-director` + `infographic-design-system` | Design briefs + layout diversity matrix |
| Programmatic rendering | `visual-renderer` + `visual-rendering` | PNG/SVG/Mermaid assets |
| Infographic QA | `visual-reviewer` | Pass/fail report with infographic-specific checks |
| Social/platform refresh | social/platform agents | Copy that references redesigned assets |

## Mandatory Design Brief

Every P0/P1 visual must define:

- Burning question.
- Audience.
- Platform.
- Infographic type.
- Visual metaphor.
- Narrative arc.
- State change.
- Hero visual.
- Text budget.
- Layout pattern.
- Icon/illustration plan.
- Source line.
- Anti-patterns to avoid.

## Asset Patterns for the AI Agent Evals Redesign

| Asset | Current issue | New direction |
|---|---|---|
| Benchmark gap exhibit | Needs more visual metaphor | Broken bridge or dual-gauge "capability vs acceptance" gap |
| Sourdough Test comic | Repeated static human icon | Four-panel state change: prompt, wrong recipe answer, correct redirect, CI block |
| Four-layer eval system | Text-led stack | Factory line / CI control tower: tasks enter, graders inspect, gate blocks, history learns |
| LinkedIn card pack | Risk of text-slide pattern | Mix split-screen, checklist, taxonomy map, process path, worksheet |
| CI architecture | Mermaid may be too plain | Rendered process infographic or annotated CI control loop |

## Quality Gate Additions

The visual-reviewer must fail visuals when:

- Comic/storyboard panels do not show a visual state change.
- A one-pager is mostly text boxes.
- Icons are decorative rather than encoding actor/action/state.
- The package repeats the same grid/card layout.
- The hero idea is not visible in 3 seconds on mobile.

## Implementation Notes

The renderer should extend `scripts/visuals/` with higher-level primitives:

- Character states: neutral, confused, wrong-answer, corrected, blocked.
- State badges: pass, fail, drift, blocked, warning.
- Process paths: snake path, pipeline, loop, gate.
- Data metaphors: gap bridge, gauge, radar, scorecard.
- Annotated scenes: chat window, empty tool log, PR checks panel.

This keeps all visual creation programmatic while raising the creative quality bar.
