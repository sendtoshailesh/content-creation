---
description: "Run a quality review on existing content. Audits a content file or the full content/ directory against quality standards and produces a structured report."
agent: "quality-reviewer"
argument-hint: "Provide the file path to review, or 'all' for full audit"
---

Review the specified content file(s) against the project quality standards:

1. Read the target file (or all files in `content/` if 'all')
2. Audit each against the quality checklist:
   - Every claim has a specific number or model name
   - Real pricing data, not placeholders
   - Case study with before/after metrics
   - Correct tone ("sharing my learnings working with customers")
   - Visuals match design tokens and render at 320 DPI
   - Platform-specific formatting is correct (Unicode for LinkedIn/Twitter, Markdown for Reddit)
3. Produce a structured report with Pass/Fix Required/Recommendations sections
4. Offer to fix issues directly
