---
name: feed-curation
description: 'Read configured blog rolls, newsletters, and RSS feeds, classify articles by subject area, extract key insights, synthesize content ideas, and rank them for the idea queue. Use when the feed-curator agent needs to process fetched articles into actionable content ideas.'
argument-hint: 'Run after feed_reader.py fetches articles to classify, extract, and rank content ideas'
---

# Feed Curation Skill

## When to Use

- When the `feed-curator` agent has fetched raw articles and needs to classify, extract insights, and synthesize content ideas
- When reprocessing existing articles with different subject area filters
- When merging new articles into the existing idea queue with deduplication

## Procedure

### 1. Read Configuration

Read `content/feed-sources.md` and extract:

- **Subject area filters**: The topic list with keywords and priority levels
- **Extraction preferences**: Relevance threshold, max ideas per run, cross-source threshold
- **Existing idea queue**: Read `content/idea-queue.md` to load existing ideas and archived entries for deduplication

### 2. Fetch Articles

Execute the feed reader script to get raw articles:

```bash
python scripts/pipeline/feed_reader.py --sources content/feed-sources.md --full-text
```

Parse the JSON output. If the script fails (missing dependencies, network errors), fall back to using the `web` tool to fetch each source URL directly.

### 3. Classify by Subject Area

For each article, assess relevance against every configured subject area:

**Classification prompt** (run per article or in batches of 5-10):

```
Given this article:
Title: {title}
Source: {source_name}
Text: {full_text or summary, first 2000 chars}

Rate its relevance (1-5) to each subject area:
{subject_areas_list with keywords}

Return JSON: {"subject_area": score, ...}
Only include subject areas scoring >= the minimum threshold for their priority level.
```

**Filtering rules:**
- Priority 1 (Core) subject areas: include articles scoring >= 2/5
- Priority 2 (High) subject areas: include articles scoring >= 3/5
- Priority 3 (Moderate) subject areas: include articles scoring >= 4/5
- Articles matching zero subject areas above threshold: skip entirely

### 4. Extract Wisdom

For each article that passes the subject area filter, extract structured insights. This is adapted from the Fabric `extract_wisdom` pattern:

**Extraction prompt** (run per article):

```
Analyze this article and extract:

**CORE INSIGHT** (1-2 sentences): The single most important takeaway — what does this article reveal that most people don't know or haven't considered?

**KEY DATA POINTS** (list): Specific numbers, benchmarks, statistics, pricing, performance metrics. Only include verifiable, concrete data — no vague claims.

**UNIQUE ANGLE**: What perspective or framing does this article offer that's different from common knowledge on this topic?

**PRACTICAL TAKEAWAY**: What can a reader DO differently after reading this? Be specific.

**CONTENT POTENTIAL** (1-3 sentences): How could this insight become a compelling blog post? What would the hook be? What audience would care most?

**TIMELINESS**: Is this tied to a recent event, release, or trend? Why does it matter NOW vs. 6 months ago?

**QUOTES** (if any): Notable quotable passages with attribution.

Article:
Title: {title}
Source: {source_name} ({source_url})
Published: {published}
Text: {full_text or summary}
```

### 5. Synthesize Content Ideas

Group extracted insights into content idea clusters. Look for these patterns:

**Theme clustering**: Multiple articles pointing to the same trend or topic = strong signal
- If >= {cross_source_threshold} sources cover the same theme, boost it
- Merge their data points and angles into a single idea

**Contrarian angles**: Article A says X, Article B says Y
- Tension between sources = excellent blog material ("The debate around X")
- Capture both sides with their supporting data

**Data-rich topics**: Articles with concrete numbers, benchmarks, case studies
- These translate directly to high-quality blog content (concrete > vague)
- Prioritize articles with before/after metrics, cost comparisons, performance data

**Timeliness signals**: Recent announcements, breaking changes, new releases
- Time-sensitive topics get a ranking boost
- Note the window of relevance ("publish within 2 weeks" vs. evergreen)

**Content gap detection**: What do sources discuss but not fully explain?
- Partial coverage = opportunity for a deeper, more comprehensive post
- "Everyone mentions X but nobody explains how to actually do it"

### 6. Rank and Score

Score each idea cluster on 5 dimensions (each 1-5, total /25):

| Dimension | What It Measures | Score Guide |
|-----------|-----------------|-------------|
| **Relevance** | How well it matches configured subject areas | 5 = dead center of core subject, 1 = tangential |
| **Data density** | Concrete numbers, benchmarks, case studies available | 5 = rich data from multiple sources, 1 = all qualitative |
| **Timeliness** | How current and time-sensitive | 5 = breaking/this week, 3 = this month, 1 = evergreen |
| **Content gap** | Are others NOT covering this well? | 5 = nobody else has this angle, 1 = well-covered topic |
| **Cross-source validation** | Multiple independent sources confirm the trend | 5 = 4+ sources, 3 = 2-3 sources, 1 = single source |

**Ranking**: Sort ideas by total score (descending). Cap at `max_ideas_per_run` from config.

### 7. Deduplication Check

Before presenting ideas, check against `content/idea-queue.md`:

- **Title similarity**: If an idea's title or core insight is substantially similar to an existing queued/archived idea, skip it
- **URL overlap**: If the primary source URLs are already cited in an existing idea, skip it
- **Theme overlap**: If the synthesized theme matches an archived idea from the last {dedup_window_days}, skip it

Flag near-duplicates rather than silently dropping them — the user may want a fresh angle on an old topic.

### 8. Output to Idea Queue

Format each accepted idea and append to `content/idea-queue.md` under `## Queued Ideas`:

```markdown
### [Rank] {Idea Title}
- **Score**: {total}/25 (R:{relevance} D:{data} T:{timeliness} G:{gap} V:{validation})
- **Subject areas**: {matched subject areas}
- **Source articles**:
  - [{Article 1 title}]({url}) — {key insight from this article}
  - [{Article 2 title}]({url}) — {supporting data point}
- **Content angle**: {How to frame this as a blog post — the hook}
- **Key data points**: {Specific numbers/benchmarks to use}
- **Timeliness**: {Why this matters now}
- **Status**: `queued`
```

Update the `Last curated:` date at the top of `idea-queue.md`.

## Important Rules

- **NEVER fabricate data** — only use insights actually extracted from fetched articles
- **ALWAYS attribute** — every data point links back to its source article
- **ALWAYS deduplicate** — check existing queue and archive before adding
- **Flag staleness** — if a source hasn't published in >30 days, note it in source health
- **Respect article limits** — don't fetch more than configured `max_articles` per source
- **Truncate article text** to first 3000 characters for LLM classification to manage token costs
- **Preserve existing ideas** — append to the queue, never overwrite existing entries

## Source Health Update

After processing, update the `## Feed Health` table in `content/feed-sources.md`:

```markdown
| Source | Last Fetched | Articles Found | Status |
|--------|-------------|----------------|--------|
| GitHub Blog | 2026-05-11 | 12 | ok |
| Azure Blog | 2026-05-11 | 8 | ok |
| The Morning Paper | 2026-05-11 | 0 | stale (last post: 2023-12-15) |
```

Status values: `ok`, `empty` (no articles in max_age window), `stale` (no new posts in 30+ days), `error: {reason}`
