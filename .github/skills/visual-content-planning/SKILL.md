---
name: visual-content-planning
description: 'Create a mandatory visual opportunity map from a strategy document or blog draft. Use before writing or rendering visuals to plan diagrams, infographics, comic/storyboard explainers, LinkedIn card packs, executive exhibits, and long-form platform visuals.'
argument-hint: 'Provide the strategy or blog file path to map into visual opportunities'
---

# Visual Content Planning Skill

## When to Use

Use this skill for every content pipeline run after strategy, scope assessment, and dimension analysis. It is mandatory because visuals are treated as first-class content, not decoration.

Use it when:

- A strategy or outline needs visual markers before blog writing.
- A blog draft needs a visual-density and visual-opportunity audit.
- Social strategy needs standalone visual assets for LinkedIn, Medium, Substack, or LinkedIn Article.
- A text-heavy section should become a diagram, infographic, comic/storyboard, card pack, or executive exhibit.

## Inputs

- Strategy document or blog post path.
- Optional `content/reference-brief.md` for source data.
- Optional `content/trend-research.md` for market data.
- Optional `content/social-strategy.md` for distribution angles.
- `content/pipeline-config.md` for persona, platform, and visual settings.

## Required Output

Create or update:

```text
content/visual-opportunity-map.md
```

The map is the contract between strategy, writing, rendering, review, and distribution agents.

## Visual Opportunity Map Schema

Every opportunity row must include:

| Field | Description |
|---|---|
| `ID` | Stable identifier, e.g. `v01-benchmark-gap` |
| `Source section` | Heading or section that creates the visual opportunity |
| `Concept type` | Architecture, flow, comparison, data, narrative, case study, checklist, governance |
| `Audience persona` | Practitioner, executive, decision-maker, platform engineer, IC engineer |
| `Visual family` | One of the approved families from `references/visual-taxonomy.md` |
| `Platform fit` | Blog, LinkedIn, Medium/Substack/LinkedIn Article |
| `Standalone potential` | High, medium, low |
| `Required source data` | Numbers, model names, URLs, citations, or "none" |
| `Rendering approach` | Pillow, Mermaid, matplotlib, SVG via Python |
| `Priority` | P0, P1, P2 |
| `Status` | planned, marker-added, rendered, reviewed, published |

Each P0/P1 row must also have an art-direction brief from the `infographic-design-system` skill before rendering starts.

## Procedure

1. **Read source artifacts**
   - Read the provided strategy or blog.
   - Read `content/pipeline-config.md`.
   - Read reference/trend/social artifacts if present.

2. **Extract visual candidates**
   - Identify every H2/H3 section over 400 words without a visual.
   - Identify every named framework, decision tree, before/after story, case study, cost/risk number, workflow, failure mode, and checklist.
   - Identify visual opportunities that can stand alone on LinkedIn or long-form platform distribution.

3. **Classify each candidate**
   - Use `references/visual-taxonomy.md`.
   - Use `infographic-design-system` to choose the infographic type, visual metaphor, and state-change plan for each P0/P1 asset.
   - Prefer first-milestone families:
     - Architecture / flow diagrams.
     - Infographics / one-pagers.
     - Comic explainers / storyboards.
     - LinkedIn social card packs.
     - Executive exhibits.

4. **Prioritize**
   - `P0`: Required for comprehension or standalone thought-leadership value.
   - `P1`: Strong social/distribution upside.
   - `P2`: Nice-to-have or derivative.

5. **Write the map**
   - Save `content/visual-opportunity-map.md`.
   - Include a `## Blog Companion Visuals` section and a `## Standalone Distribution Visuals` section.
   - Include a `## Rendering Handoff` section with exact visual prompts for `visual-renderer`.
   - Include a package-level layout diversity matrix so adjacent visuals do not repeat the same card/grid pattern.

6. **Insert strategy markers**
   - If editing a strategy/outline, add `[VISUAL: ...]` markers for P0 blog companion visuals.
   - Do not insert generated image links until assets exist.

## Selection Rules

- Use **architecture / flow diagrams** for system structure, agent workflows, API/data flow, governance loops, and CI/CD paths.
- Use **infographics / one-pagers** for saveable summaries, statistics, checklists, and "how to explain this to a team" artifacts.
- Use **comic/storyboard explainers** for human scenarios, production failures, misuse cases, before/after moments, and "why this matters" stories.
- Use **LinkedIn social card packs** for swipeable thought leadership, practitioner frameworks, and high-save content.
- Use **executive exhibits** for ROI, risk, cost, operational decision-making, and leadership-facing evidence.

## Quality Rules

- Do not invent numbers. Every data-bearing visual must cite the source document or URL.
- Every P0 visual must be understandable without the surrounding blog text.
- Every standalone visual must have one insight, one audience, and one platform target.
- Comic/storyboard visuals must be programmatic only: Pillow/SVG primitives, panels, captions, callouts, and simple characters. Do not require external image generation.
- Prefer reusable renderer utilities from `scripts/visuals/` for panel, card, text, and source-line layout.
- Infographics must not be text slides. The main idea must be carried by visual metaphor, hierarchy, chart, scene, or process structure.
- Comic/storyboard assets must show visible state changes between panels. Do not repeat the same icon/character with only the text changed.
- One-pagers must use an infographic structure such as a pipeline, factory, control tower, bridge, gauge, timeline, or annotated scene; do not use four plain text boxes.

## Handoff to Renderer

For each P0/P1 visual, provide a compact prompt:

```markdown
### v01-benchmark-gap
- Visual family: Executive exhibit
- Platform: Blog + LinkedIn Article
- Size: 1200x627
- Renderer: Pillow or matplotlib
- Message: SWE-bench scores prove coding capability, not production behavior.
- Data: SWE-bench Verified score, production acceptance gap, source URLs
- Layout: conclusion-as-title, evidence chart, source line
- Must stand alone: yes
```

Add art-direction fields:

```markdown
- Burning question:
- Infographic type:
- Visual metaphor:
- State changes:
- Text budget:
- Icon/illustration plan:
- Visual-reviewer acceptance criteria:
```
