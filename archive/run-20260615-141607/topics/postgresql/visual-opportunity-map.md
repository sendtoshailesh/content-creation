# Visual Opportunity Map — PostgreSQL × AI performance

Static-only output (PNG). Diagrams/matrix via HTML/CSS+Chromium; chart via matplotlib; hero via
programmatic backdrop + CSS overlay. All pass the deterministic gates / visual-reviewer.

## Blog Companion Visuals (P0)

| ID | Family | What it shows | Renderer | Marker |
|----|--------|---------------|----------|--------|
| V1 | Hero | Title hero (programmatic backdrop + CSS overlay) | `scripts.visuals.generated.programmatic` | top of post |
| V2 | Flow diagram | Diagnose→fix loop: old (grep→EXPLAIN→guess) vs AI-assisted (ground→triage→suggest→validate→measure) | HTML/CSS + Chromium | §1 |
| V3 | Matrix | Where AI helps vs hurts across the workflow (triage, rewrite, index, anomaly, internals) | HTML/CSS + Chromium | §3 |
| V4 | Bar chart | Before/after query latency for Example 1 (4,200 ms → 38 ms, log scale) | matplotlib | §4 |

## Standalone Distribution Visuals
- V3 (matrix) doubles as the LinkedIn lead image.
- V4 (before/after) anchors the Reel.

## Rendering handoff notes
- Brand tokens; one theme per visual (round-robin). Hero: no embedded text in backdrop; title via CSS overlay.
- V4: log-scale y so 38 ms vs 4,200 ms both readable; bold value labels; source line "illustrative".
- All output to `content/topics/postgresql/visuals/`.
