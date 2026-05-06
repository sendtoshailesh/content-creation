---
name: content-scope-assessment
description: 'Assess whether a content topic is too comprehensive for a single blog post and recommend a multi-part series structure. Uses 8 scoring signals including dimension breadth from multi-dimensional-analysis. Use after strategy/outline creation and dimension analysis to determine if the topic should be split into a series.'
argument-hint: 'Provide the strategy file path to assess for scope'
---

# Content Scope Assessment Skill

## When to Use

- After the content-strategist produces a strategy/outline
- When a topic has 4+ distinct pillars or subtopics that each warrant deep treatment
- When estimated word count exceeds 3,500 words for proper coverage
- When the pipeline orchestrator needs to decide: single post vs. multi-part series

## Scope Assessment Criteria

Evaluate the strategy/outline against these signals:

### Indicators of Multi-Part Content (score each 0-2)

| Signal | Weight | Description |
|--------|--------|-------------|
| **Pillar count** | High | 4+ distinct pillars or frameworks that each need >500 words |
| **Data density** | Medium | >15 unique data points, benchmarks, or case studies to present |
| **Audience breadth** | Medium | 3+ distinct personas with different depth requirements |
| **Technical depth** | High | Each subtopic requires code examples, diagrams, or step-by-step walkthroughs |
| **Word count pressure** | High | Proper coverage would exceed 4,000 words in a single post |
| **Visual complexity** | Medium | 5+ visual assets needed, each requiring explanation |
| **Distribution fragmentation** | Low | Social posts would need to cherry-pick heavily due to breadth |
| **Dimension breadth** | High | 3+ personas AND 7+ practices AND 3+ WAF pillars (from `multi-dimensional-analysis` skill) |

### Dimension Breadth Signal (from multi-dimensional-analysis)

This 8th signal uses output from the `multi-dimensional-analysis` skill:

| Score | Criteria |
|-------|----------|
| **0** | 1 persona AND ≤3 total practices AND ≤1 primary WAF pillar |
| **1** | 2 personas OR 4-6 total practices OR 2-3 WAF pillars (primary + secondary) |
| **2** | 3+ personas AND 7+ total practices AND 3+ WAF pillars (primary + secondary) |

If multi-dimensional analysis has not been run yet, omit this signal and use the 0-14 scale with original thresholds.

### Scoring (8 signals, 0-16 total)

- **Score 0-5**: Single post — topic fits well in ~3,000 words
- **Score 6-10**: Consider series — topic is comprehensive but could be compressed
- **Score 11+**: Recommend series — splitting improves depth, SEO, and distribution

## Series Planning Procedure

When recommending a series:

1. **Identify the natural split points** — Where does the topic divide into self-contained subtopics?
2. **Define part boundaries** — Each part must:
   - Stand alone (reader gets value without reading other parts)
   - Have its own hook and CTA
   - Be 2,500-3,500 words
   - Have 2-3 dedicated visuals
3. **Plan the series arc**:
   - Part 1: Problem framing + highest-impact strategy (the "quick win")
   - Part 2-N: Deep dives into each subsequent pillar
   - Final part: Synthesis + complete playbook
4. **Dimension-informed split**: When multi-dimensional analysis is available, use dimension data to determine part boundaries:
   - Choose the dimension type with the most natural groupings as the primary split axis
   - Align each part to 1-2 WAF pillars and a primary persona
   - Consider a persona arc: Part 1 = IC developer, middle parts = tech lead/architect, final part = manager/executive
   - Each part must have at least 2 practices with standalone value
5. **Cross-linking strategy**: Each part links to previous/next, with a series landing page
6. **Distribution plan per part**: Each part gets its own social distribution cycle

## Output Format

Add a `## Series Plan` section to the strategy document:

```markdown
## Series Plan

**Assessment score**: X/14
**Recommendation**: Multi-part series (N parts)

### Series Structure

| Part | Title | Focus | Est. Words | Key Visual |
|------|-------|-------|------------|------------|
| 1 | [title] | [pillar] | 2,800 | [visual] |
| 2 | [title] | [pillar] | 3,000 | [visual] |
| N | [title] | [pillar] | 2,500 | [visual] |

### Publishing Cadence

- Recommended interval: [X days between parts]
- Series landing page: `content/<series-slug>-series.md`

### Cross-Promotion

- Each part references the series
- LinkedIn: one post per part + series summary post
- X/Twitter: one thread per part
- Reddit: Part 1 as main post, later parts as follow-up comments or new posts
```

## Integration with Pipeline

When a series is recommended:

1. The pipeline config gets a new `## Series Plan` section
2. Blog-writer receives instructions to write Part 1 first
3. After Part 1 completes the full pipeline (quality, social, publish), the orchestrator asks whether to proceed with Part 2
4. Each part runs through Steps 3-10 independently
5. A series index page is generated after Part 2+

## Constraints

- DO NOT automatically split every topic — many fit well in a single post
- DO NOT create artificial splits that break the reader's flow
- Each part MUST deliver standalone value (not a cliffhanger with no resolution)
- Minimum 2 parts, maximum 5 parts for a series
