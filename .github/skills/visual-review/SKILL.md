# Visual Review Skill

## Purpose

Review rendered visual assets (PNG, SVG, Mermaid diagrams) for layout defects, text overflow, readability, design token compliance, data accuracy, and reader comprehension. Produces a structured findings report for the visual-renderer agent to act on.

## When to Use

- After `visual-renderer` generates or updates PNGs/SVGs
- As a mandatory pipeline step before publishing (Phase 2c in the content pipeline)
- When a user reports a visual defect (standalone invocation)
- After any renderer code change to verify the fix

## Cross-Model Requirement

This skill MUST be executed on a different LLM model family than the one that created the visuals. This follows the same principle as the content quality review (cross-model critic) and GitHub's rubber duck review pattern — adversarial diversity catches systematic blind spots.

| Creation model | Reviewer model options |
|---------------|----------------------|
| Anthropic (Claude) | OpenAI (GPT) or Google (Gemini) |
| OpenAI (GPT) | Anthropic (Claude) or Google (Gemini) |
| Google (Gemini) | Anthropic (Claude) or OpenAI (GPT) |

## Review Dimensions

### Critical (blocks publishing)

1. **Text overflow/truncation**: Text extending beyond containers, clipped at figure edges
2. **Text overlap**: Labels, annotations, or values colliding with adjacent elements
3. **Data inaccuracy**: Numbers in visual don't match the blog/reference brief
4. **Element clipping**: Chart elements cut off at figure boundaries

### Important (should fix before publishing)

5. **Readability**: Font size < 7pt at 320 DPI, insufficient color contrast
6. **Standalone clarity**: Reader cannot understand visual without reading the blog section
7. **Design token violation**: Colors not from token palette, wrong font, wrong DPI
8. **Layout imbalance**: Large empty areas, misaligned columns, uneven spacing

### Minor (nice to fix)

9. **Visual polish**: Inconsistent padding, arrows overlapping content, legend placement
10. **Theme compliance**: Multiple visuals in same post using the same theme (should rotate)

## Professional Infographic Principles

Apply these principles from information design best practices (Edward Tufte, IBCS standards):

- **Data-ink ratio**: Maximize the share of ink used to present data. Remove chartjunk (decorative gridlines, 3D effects, redundant labels).
- **Small multiples**: When comparing similar data across categories, use consistent scales and aligned axes.
- **Visual hierarchy**: The most important insight should have the largest/boldest visual treatment. Secondary information is smaller/lighter.
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

1. Enumerate all visual files to review (from blog `![](path)` references or `content/visuals/` scan)
2. View each rendered image using the image viewing capability
3. Apply all review dimensions from the checklist above
4. Cross-reference data in visuals against `content/reference-brief.md` and the blog post
5. Produce structured findings report (severity, category, finding, suggestion)
6. Return PASS (0 critical findings) or FAIL (1+ critical findings)

## Output Format

Structured table per visual with severity/category/finding/suggestion columns. Summary with counts by severity and overall PASS/FAIL verdict.

## Handoff

- **PASS**: Visuals approved for publishing
- **FAIL**: Findings report handed to `visual-renderer` agent for fixes. After fixes, visual-reviewer runs again (review loop until PASS)
