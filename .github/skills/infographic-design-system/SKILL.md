---
name: infographic-design-system
description: "Create research-backed infographic design briefs before rendering visual assets. Use for infographics, one-pagers, comic/storyboards, social card packs, executive exhibits, and visual-first blog/social content."
argument-hint: "Provide content artifact path, visual opportunity map, or visual asset request"
---

# Infographic Design System Skill

## When to Use

Use this skill before any visual renderer writes code for infographic-style assets. It is mandatory when creating or redesigning:

- Infographics / one-pagers.
- Comic explainers / storyboards.
- LinkedIn carousel or card packs.
- Executive exhibits.
- Process diagrams, timelines, comparison graphics, and visual frameworks.

Use this skill especially when visuals were rejected as too text-led, repetitive, static, or insufficiently infographic-like.

## Core Principle

An infographic is not a decorated text slide. It is a visual explanation system.

Every asset must answer:

1. What is the one burning question this visual solves?
2. Which infographic type best fits that question?
3. What is the visual metaphor or diagram structure?
4. What changes visually from start to finish?
5. What can be understood in 3 seconds on mobile?

## Research Base

This skill applies principles synthesized from:

- GraphicMama: infographics simplify heavy data, use minimal text, tell a clear story, and need audience-specific visuals.
- Venngage: choose infographic type by goal; use process, statistical, informational, timeline, comparison, hierarchy, and list formats intentionally.
- Adobe Express: use visuals, symbols, charts, diagrams, and bite-sized information to make complex topics easier to understand and share.
- Data visualization practice: use visual hierarchy, white space, clear annotation, accurate chart selection, and source attribution.
- GitHub ecosystem patterns: package reusable guidance as skills, references, and agent workflows similar to `github/awesome-copilot`.

## Infographic Type Router

Choose the type before choosing the layout.

| Communication goal | Preferred visual family | Layout patterns |
|---|---|---|
| Explain a workflow | Process infographic | Snake path, step ladder, pipeline, loop |
| Prove a gap or risk | Statistical / executive exhibit | Hero numbers, slope gap, scorecard, before/after |
| Explain a concept | Informational infographic | Annotated scene, hub-and-spoke, layered stack |
| Show change over time | Timeline infographic | Milestone rail, release history, regression timeline |
| Compare two ideas | Comparison infographic | Split-screen, scale, opposing columns, decision matrix |
| Show priority or levels | Hierarchical infographic | Pyramid, stack, maturity ladder, nested rings |
| Summarize actions | List / checklist infographic | Saveable checklist, action cards, worksheet |
| Humanize a failure | Comic / storyboard | Setup, tension, wrong behavior, corrected behavior, resolution |

## Required Design Brief

Before rendering, create a design brief in the visual opportunity map or renderer notes:

```markdown
### [visual-id]
- Burning question:
- Audience:
- Platform:
- Infographic type:
- Visual metaphor:
- Narrative arc:
- Data/source inputs:
- Primary visual element:
- State change or motion cue:
- Text budget:
- Layout pattern:
- Icon/illustration plan:
- Source line:
- Failure modes to avoid:
```

## Mandatory Quality Rules

1. **One insight per asset**: do not combine multiple arguments into one crowded design.
2. **Visual first, text second**: the main idea must be visible through shape, contrast, chart, icon, or scene before reading paragraphs.
3. **State change is required**: comics and process visuals must show before/after, pass/fail, drift/fix, or risk/control.
4. **No repeated static icons**: if a character or icon appears across panels, change expression, posture, color, status badge, tool state, or environment.
5. **Minimum text budget**: hero title <= 9 words; panel caption <= 14 words; supporting callout <= 20 words.
6. **Mobile 3-second test**: title, hero visual, and takeaway must be understandable at phone size.
7. **Source hygiene**: every metric-bearing asset needs a visible source line or linked manifest entry.
8. **Layout diversity**: a package cannot be mostly card grids. Mix split-screen, process, timeline, storyboard, scorecard, and annotated scene patterns.
9. **White space is a design element**: leave breathing room around hero numbers and illustrations.
10. **Review against anti-patterns**: text slide, table-as-infographic, repeated icon, decorative cartoon, unlabeled chart, unsupported metric.

## Output Handoff

The skill should output:

- A visual design brief for each P0/P1 asset.
- A package-level layout diversity matrix.
- Renderer instructions for Python/Pillow, Mermaid, matplotlib, or SVG.
- Visual-reviewer acceptance criteria.

## Anti-Patterns

- Do not render until the infographic type and visual metaphor are chosen.
- Do not treat icons as decoration. Icons must encode state, actor, action, or category.
- Do not repeat the same human/agent icon across comic panels without visible change.
- Do not create a "four cards with text" one-pager and call it an infographic.
- Do not use dense text blocks where a chart, path, scene, or comparison would explain faster.
