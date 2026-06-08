# Visual Review Skill

## Purpose

Review rendered visual assets (PNG, SVG, Mermaid diagrams) for layout defects, text overflow, readability, design token compliance, data accuracy, and reader comprehension. Produces a structured findings report for the visual-renderer agent to act on.

## When to Use

- After `visual-renderer` generates or updates PNGs/SVGs
- As a mandatory pipeline step before publishing (Phase 2c in the content pipeline)
- When a user reports a visual defect (standalone invocation)
- After any renderer code change to verify the fix

## Rubber-Duck Review Requirement

This skill uses GitHub Copilot's rubber-duck review pattern for adversarial visual critique. Do **not** require a model-family switch before running visual review.

## Review Dimensions

### Critical (blocks publishing)

1. **Text overflow/truncation**: Text extending beyond containers, clipped at figure edges
2. **Text overlap**: Labels, annotations, or values colliding with adjacent elements
3. **Data inaccuracy**: Numbers in visual don't match the blog/reference brief
4. **Element clipping**: Chart elements cut off at figure boundaries
5. **Unreadable blog typography**: Blog/social visuals use body labels below 11pt equivalent, weak hierarchy, or non-bold primary claims
6. **Uninspected referenced image**: Any `![...](visuals/...)` reference that was not opened and visually inspected after rendering
7. **Monotone visual system**: Multiple visuals in the same post repeat the same card grid, row-table, shape language, or color theme without a concept-driven reason
8. **Excessive whitespace**: Important content is tiny or sparse while large areas of the canvas are unused

### Important (should fix before publishing)

9. **Standalone clarity**: Reader cannot understand visual without reading the blog section
10. **Design token violation**: Colors not from token palette, wrong font, wrong DPI
11. **Layout imbalance**: Misaligned columns, uneven spacing, weak grouping

### Minor (nice to fix)

12. **Visual polish**: Inconsistent padding, arrows overlapping content, legend placement

## Professional Infographic Principles

Apply these principles from information design best practices (Edward Tufte, IBCS standards):

- **Data-ink ratio**: Maximize the share of ink used to present data. Remove chartjunk (decorative gridlines, 3D effects, redundant labels).
- **Small multiples**: When comparing similar data across categories, use consistent scales and aligned axes.
- **Visual hierarchy**: The most important insight should have the largest/boldest visual treatment. Secondary information is smaller/lighter.
- **Pattern diversity**: A post should mix visual patterns (split-screen, timeline, flow, scorecard, matrix, annotated scene, radial) instead of repeating the same composition.
- **Ask before assuming**: When the user criticizes aesthetics, ask for design direction, color policy, diagram-pattern preferences, and typography density before approving or rebuilding.
- **Color semantics**: Green = positive/success, Red = warning/negative, Blue = neutral/primary. Never use color as the only differentiator (accessibility).
- **Annotation-first**: Key takeaways should be annotated directly on the visual, not left for the reader to infer.
- **Gestalt principles**: Use proximity, similarity, and enclosure to group related elements. White space separates distinct concepts.

## Narrow Segment Rule

For any chart element that is < 15% of the total width/height:
- **DO NOT** place text labels inside the segment
- **DO** use external labels with leader lines (thin connecting lines from label to segment)
- **DO** consider callout boxes or a separate legend table

This is the #1 source of text overflow in stacked bars, pie charts, and treemaps.

## Procedure

1. Enumerate all visual files from blog `![alt](visuals/...)` references. Do not infer from frontmatter `og_image`.
2. Verify every referenced file exists and is 320 DPI.
3. View each rendered image using the image viewing capability. Reading renderer code is not sufficient.
4. Apply all review dimensions from the checklist above.
5. Cross-reference data in visuals against `content/reference-brief.md` and the blog post.
6. Produce structured findings report (severity, category, finding, suggestion).
7. Return PASS only when there are **0 critical findings and 0 uninspected referenced images**. Repetitive shape/color patterns block publishing.

## Output Format

Structured table per visual with severity/category/finding/suggestion columns. Summary with counts by severity and overall PASS/FAIL verdict.

## Handoff

- **PASS**: Visuals approved for publishing
- **FAIL**: Findings report handed to `visual-renderer` agent for fixes. After fixes, visual-reviewer runs again (review loop until PASS)
