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

## Source-of-Truth Precedence

This skill enforces the **Source-of-Truth Precedence** rule (see `.github/instructions/content-quality.instructions.md` and the `source-grounding` skill). Lead with first-party Microsoft/GitHub sources; use public sources for neutral benchmarks, independent validation, or when no first-party source exists. Every source in the brief is tagged with its tier so writers can lead first-party by construction.

## Procedure

### 0. Harvest browsing signals (mandatory)

Before reading the config, run the browsing harvester with the run's topic keywords so the author's real navigation feeds the brief:

```bash
python3 scripts/pipeline/harvest_browsing.py --days 365 --top 30 <topic keywords>
```

Read `content/browsing-signals.md`. Promote its Tier 2 (Microsoft) and Tier 3 (GitHub) entries into the reference set as lead first-party sources, and keep relevant Tier 4 entries as public corroboration. Fetch/verify any URL before citing it.

### 1. Read the Config

Read `content/pipeline-config.md` and extract all URLs from the **Online References** section. URLs are organized into source tiers (first-party Microsoft/GitHub first, public fallback below) and the legacy categories:
- Tier 2 — Microsoft first-party
- Tier 3 — GitHub first-party
- Tier 4 — Public (Industry Reports, Competitor Articles, Pricing/Docs, Case Studies, Research Papers)

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

### [Source Title](URL) `[T1 own | T2 Microsoft | T3 GitHub | T4 public]`
- **Tier**: [T1/T2/T3/T4 + why — e.g. "T2 Microsoft: AI Foundry docs"]
- **Key data points**: [specific numbers, benchmarks]
- **Pricing info**: [if applicable]
- **Unique angle**: [what this source adds that others don't]
- **Relevant quotes**: [key passages, attributed]
- **Credibility**: [author expertise, publication quality]
- **From browsing signals**: [yes/no — was this surfaced from the author's history/bookmarks?]

## Cross-Source Analysis

### Consensus Points
- [claims that multiple sources agree on]

### Contradictions
- [where sources disagree — flag for investigation]

### Data Points for Content
- [specific numbers, benchmarks to cite in blog]
- [pricing data to use in comparisons]
- [case study metrics to reference]

### Lead-First-Party Map
- [for each major claim: the Tier 1-3 example that leads, and the Tier 4 source that corroborates]

### Gaps
- [topics the references don't cover that we should address]
- [claims with NO first-party source — flag so a Microsoft/GitHub source can be sought]
```

### 4. Signal Readiness

After creating the brief, notify that references are analyzed and the blog-writer or content-strategist can proceed.

## Important Rules

- Always attribute data to its source
- Flag any data that seems outdated (check publication dates)
- Note when pricing data has a specific date — it may change
- If a URL fails to load, note it and proceed with remaining sources
- Do NOT fabricate data — only use what's actually in the references

## Volatility Tagging

Tag data points that are likely to change before the content is published. Add a `[VOLATILE]` marker next to any data point that meets these criteria:

- **Pricing data**: Model costs, API rates, token pricing, plan pricing, credit allocations
- **Feature availability**: Free tier models, included models, feature access by plan
- **Policy/billing changes**: Billing model transitions, deadline dates, promotional periods
- **Multiplier tables**: Model multipliers, discount rates, tier classifications
- **Quota/limit data**: Request limits, rate limits, usage caps

Format in the reference brief:
```
- `[VOLATILE]` Model X included at 0x on paid plans — [source](URL) — verified [date]
```

The `grounded-content-reviewer` agent uses these tags during Step 3e to prioritize which claims to re-verify against live sources before publishing. Data points without `[VOLATILE]` tags (research findings, benchmarks, case studies) are less likely to change and receive lower re-verification priority.

### "Subject to Change" Detection

When a source explicitly states that data is "subject to change", "may change", or "in preview", capture the caveat:
```
- `[VOLATILE][CAVEAT: "subject to change"]` Model multipliers — [source](URL)
```

Content writers MUST include appropriate caveats when citing `[VOLATILE][CAVEAT]` data points.
