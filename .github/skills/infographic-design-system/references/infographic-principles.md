# Infographic Design Principles Reference

This reference summarizes reusable principles for the content pipeline's visual-first redesign.

## Source Lessons

### GraphicMama

- Infographics are information graphics: they simplify heavy data into a high-level view.
- Great infographics use minimal text in favor of visuals.
- A strong title sets the topic and core message.
- White space prevents overwhelming the reader.
- Good infographics tell a story with flow, hierarchy, contrast, and charts.
- Audience determines tone, colors, and visual style.

### Venngage

- Choose the infographic type based on the communication goal.
- Process infographics need numbered steps and directional cues.
- Statistical infographics need the story behind the data, hero numbers, icons, and varied chart types.
- Informational infographics should use descriptive section headers and varied color/direction.
- Timeline, comparison, hierarchy, and list formats each solve different problems.
- Effective design starts from a burning problem and 3-5 supporting questions.

### Adobe Express

- Infographics combine visuals with bite-sized information.
- Symbols, charts, diagrams, and imagery help complex topics become easier to understand.
- Topics should be shareable, audience-relevant, and brand-aligned.
- Visual aids should be prioritized over text.
- Memorable infographics use images, short copy, brand colors, and recognizable structure.

## Design Checklist

Use this before rendering.

| Check | Question |
|---|---|
| Burning question | What question does the visual answer? |
| Type fit | Is this process, statistical, informational, timeline, comparison, hierarchy, list, or comic/storyboard? |
| Hero visual | What is the first thing the eye sees? |
| State change | What visually changes from problem to solution? |
| Text budget | Can the visual survive with 60% less text? |
| Mobile scan | Does it work in 3 seconds on a phone? |
| Source | Is each number visibly sourced or in the manifest? |
| Layout diversity | Is this package avoiding repeated card grids? |

## Redesign Guidance for AI Agent Evals

### Sourdough Test

Do not repeat the same human icon in each panel. Show a real sequence:

1. Prompt card: "How do I bake sourdough?"
2. Wrong behavior: deployment agent becomes a recipe assistant.
3. Expected behavior: agent redirects to Azure/deployment scope.
4. CI catches drift: 3 of 8 agents fail; model-wide warning appears.

Visual changes:

- Character expression changes from neutral to confused to corrected.
- Agent bubble changes from green pass to red drift.
- Tool panel changes from empty/no-op to CI fail badge.
- Background shifts from chat to CI dashboard.

### Four-Layer Eval System

Do not render four text boxes. Use a system metaphor:

- Factory line: tasks enter, graders inspect, CI gate blocks, history dashboard learns.
- Airport security: task baggage, scanners, gate, incident log.
- Circuit board: input signal, test nodes, release gate, telemetry memory.
- Control tower: agents as flights, eval radar, runway gate, incident timeline.

Visual changes:

- Data moves through the system.
- Gate opens/closes.
- Failures branch to debug trace.
- Regression history accumulates markers over time.

### Benchmark Gap

Use a visual gap metaphor:

- Broken bridge between benchmark score and PR acceptance.
- Two gauges: capability high, production acceptance lower.
- Slope drop from benchmark to real-world acceptance.
- Risk zone between "can solve task" and "safe to merge".

## Package-Level Layout Mix

For a strong visual-first package, use at least four distinct patterns:

1. Hero statistical exhibit.
2. Narrative comic/storyboard.
3. Process/system infographic.
4. Comparison or taxonomy visual.
5. Action worksheet or checklist.

Avoid a package where most visuals are rectangular text cards.
