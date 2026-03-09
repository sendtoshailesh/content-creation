---
name: reference-analysis
description: 'Fetch and synthesize online reference URLs for content creation. Use when the pipeline config has reference URLs that need to be analyzed before writing blog posts or social content.'
argument-hint: 'Run to fetch and analyze all URLs listed in content/pipeline-config.md'
---

# Reference Analysis Skill

## When to Use

- Before writing a blog post, when `content/pipeline-config.md` has reference URLs listed
- When the user adds new URLs and wants them analyzed
- During Steps 1-3 of the content pipeline (strategy, outline, blog writing)

## Procedure

### 1. Read the Config

Read `content/pipeline-config.md` and extract all URLs from the **Online References** section. URLs are organized under:
- Industry Reports & Benchmarks
- Competitor / Related Articles
- Pricing Pages & Documentation
- Case Studies & Examples
- Research Papers

### 2. Fetch Each URL

For each URL listed, use the `web` tool to fetch the page content. Extract:
- **Key claims** with specific numbers, benchmarks, or data points
- **Pricing data** (model costs, API rates, token pricing)
- **Case studies** with before/after metrics
- **Frameworks or methodologies** described
- **Contrarian or unique perspectives** that differentiate this source

### 3. Synthesize into Reference Brief

Create a structured reference brief at `content/reference-brief.md` with:

```markdown
# Reference Brief — [Topic]
Generated: [date]

## Source Summary

### [Source Title](URL)
- **Key data points**: [specific numbers, benchmarks]
- **Pricing info**: [if applicable]
- **Unique angle**: [what this source adds that others don't]
- **Relevant quotes**: [key passages, attributed]
- **Credibility**: [author expertise, publication quality]

## Cross-Source Analysis

### Consensus Points
- [claims that multiple sources agree on]

### Contradictions
- [where sources disagree — flag for investigation]

### Data Points for Content
- [specific numbers, benchmarks to cite in blog]
- [pricing data to use in comparisons]
- [case study metrics to reference]

### Gaps
- [topics the references don't cover that we should address]
```

### 4. Signal Readiness

After creating the brief, notify that references are analyzed and the blog-writer or content-strategist can proceed.

## Important Rules

- Always attribute data to its source
- Flag any data that seems outdated (check publication dates)
- Note when pricing data has a specific date — it may change
- If a URL fails to load, note it and proceed with remaining sources
- Do NOT fabricate data — only use what's actually in the references
