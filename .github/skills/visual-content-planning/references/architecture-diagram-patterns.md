# Architecture and Flow Diagram Patterns

Use these patterns for system, workflow, and governance visuals.

## Patterns

| Pattern | Use when | Renderer |
|---|---|---|
| Left-to-right pipeline | Showing ordered steps, CI/CD, eval pipeline, publishing flow | Mermaid or Pillow |
| Layered stack | Showing responsibility boundaries or platform layers | Pillow |
| Hub-and-spoke | Showing a central service or policy connected to consumers | Mermaid or Pillow |
| Decision tree | Showing routing, triage, grading, or model/tool choice | Mermaid |
| Swimlane | Showing ownership across personas or teams | Pillow |
| Feedback loop | Showing measurement, review, remediation, and redeploy loops | Mermaid or Pillow |
| Before/after teardown | Showing flawed vs. improved architecture | Pillow |

## Required Elements

- Conclusion-as-title for leadership-facing diagrams.
- Clear entry and exit points.
- Named components, not vague boxes.
- Data/control flow labels where meaningful.
- Source/citation line when claims or metrics are shown.

## Selection Rules

- Use Mermaid when topology is more important than pixel-perfect design.
- Use Pillow when typography, callouts, or multi-panel composition is important.
- Use a swimlane when ownership is the core insight.
- Use a before/after teardown when the content is an opinion or recommendation.

