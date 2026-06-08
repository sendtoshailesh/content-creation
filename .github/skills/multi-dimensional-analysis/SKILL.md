---
name: multi-dimensional-analysis
description: 'Analyze a content topic across three dimension types — persona, best practice, and Azure Well-Architected Framework pillars — to inform series planning, content depth, and social distribution angles. Use after scope assessment to shape how parts are split and which angles each part covers.'
argument-hint: 'Provide the strategy file path to analyze for dimensions'
---

# Multi-Dimensional Topic Analysis Skill

## When to Use

- After the content-strategist produces a strategy/outline and scope assessment
- When planning a multi-part series and need to determine part boundaries
- When the topic spans multiple audiences, practice areas, or architectural concerns
- When social distribution needs persona-specific or pillar-specific angles

## Purpose

Analyze the topic across three orthogonal dimension types to produce a dimension matrix that:

1. Informs series part boundaries (which dimensions group into which part)
2. Guides content depth per section (deep/moderate/mention based on WAF relevance)
3. Shapes social distribution angles (which persona × platform to emphasize)
4. Feeds a "dimension breadth" score back into the scope assessment (0-2 scale)

## Dimension Types

### 1. Persona Dimensions

Identify distinct roles that would consume this content differently.

For each persona, capture:

| Field | Description |
|-------|-------------|
| **Role** | Job title or function (e.g., Senior Developer, Engineering Manager) |
| **Responsibility context** | What they own that makes this topic relevant |
| **Application angle** | How they would apply the topic (hands-on implementation vs. policy vs. budgeting) |
| **Depth needed** | `deep` (implementation details, code examples) / `moderate` (concepts, decision frameworks) / `overview` (impact summary, ROI) |
| **Preferred channels** | Where this persona consumes content (LinkedIn, Reddit, YouTube, etc.) |

**Scoring guide:**

- 1 persona: Narrow audience, single-angle content
- 2 personas: Moderate breadth, consider dual framing
- 3+ personas: Broad audience, strong series candidate with persona-aligned parts

### 2. Best Practice Dimensions

Identify distinct best practices the topic covers, split into two categories.

#### Technology Practices

Practices involving tools, configurations, code, or technical implementation.

For each practice, capture:

| Field | Description |
|-------|-------------|
| **Practice name** | Descriptive label (e.g., "Model routing/selection") |
| **Category** | `technology` |
| **Complexity** | `low` / `medium` / `high` — how hard to implement |
| **Impact** | `low` / `medium` / `high` — magnitude of outcome when applied |
| **Standalone value** | Can a reader get value from this practice alone? (yes/no) |

#### Governance Practices

Practices involving process, policy, team coordination, or organizational controls.

For each practice, capture the same fields with `Category` = `governance`.

**Scoring guide:**

- 1-3 practices total: Focused topic, single post likely sufficient
- 4-6 practices: Moderate breadth, consider grouping related practices
- 7+ practices: Broad scope, strong series candidate with practice-grouped parts

### 3. Azure Well-Architected Framework Pillar Dimensions

Map the topic to the five Azure WAF pillars. Every technical topic touches at least one pillar; most touch 2-3.

| Pillar | Assessment |
|--------|------------|
| **Cost Optimization** | Is the topic about reducing spend, improving ROI, or rightsizing resources? |
| **Operational Excellence** | Does the topic involve monitoring, governance, team processes, or automation? |
| **Performance Efficiency** | Does the topic affect latency, throughput, resource utilization, or scalability? |
| **Reliability** | Does the topic involve fault tolerance, fallback patterns, or availability? |
| **Security** | Does the topic involve data protection, access control, threat mitigation, or compliance? |

For each pillar, assign:

| Field | Description |
|-------|-------------|
| **Relevance** | `primary` (core focus) / `secondary` (significant but not central) / `tangential` (minor connection) / `none` |
| **Coverage depth** | `deep` (800+ words, dedicated section) / `moderate` (200-500 words, subsection or callout) / `mention` (1-2 sentences acknowledging the connection) |
| **Content angle** | How the pillar applies to this specific topic (one sentence) |

**Scoring guide:**

- 1 primary pillar only: Focused topic
- 1 primary + 1-2 secondary: Moderate breadth
- 2+ primary or 3+ secondary: Broad architectural impact, series candidate

## Output Format

Append a `## Dimension Analysis` section to the strategy document with these subsections:

```markdown
## Dimension Analysis

> Assessed: [date] | Skill: `multi-dimensional-analysis`

### Persona Dimensions

| Persona | Responsibility Context | Application Angle | Depth | Preferred Channels |
|---------|----------------------|-------------------|-------|-------------------|
| [role] | [context] | [angle] | deep/moderate/overview | [channels] |

**Persona count**: N

### Best Practice Dimensions

#### Technology Practices

| Practice | Complexity | Impact | Standalone Value |
|----------|-----------|--------|------------------|
| [name] | low/med/high | low/med/high | yes/no |

#### Governance Practices

| Practice | Complexity | Impact | Standalone Value |
|----------|-----------|--------|------------------|
| [name] | low/med/high | low/med/high | yes/no |

**Practice count**: N technology + N governance = N total

### Azure WAF Pillar Dimensions

| Pillar | Relevance | Coverage Depth | Content Angle |
|--------|-----------|---------------|---------------|
| Cost Optimization | primary/secondary/tangential/none | deep/moderate/mention | [angle] |
| Operational Excellence | ... | ... | ... |
| Performance Efficiency | ... | ... | ... |
| Reliability | ... | ... | ... |
| Security | ... | ... | ... |

**Primary pillars**: N | **Secondary pillars**: N

### Dimension Breadth Score

| Signal | Evidence | Score (0-2) |
|--------|----------|-------------|
| Persona count | N personas identified | 0/1/2 |
| Practice count | N practices (N tech + N governance) | 0/1/2 |
| WAF pillar spread | N primary + N secondary pillars | 0/1/2 |

**Dimension breadth score**: N/2

### Dimension × Series Alignment

[When a series is recommended, map dimensions to proposed parts]

| Part | Primary Persona | Key Practices | WAF Pillar Focus |
|------|----------------|---------------|-----------------|
| 1 | [persona] | [practices] | [pillar] |
| 2 | [persona] | [practices] | [pillar] |
| N | [persona] | [practices] | [pillar] |

### Dimension × Platform Matrix

[Map personas and practices to social platform emphasis]

| Platform | Primary Persona | Angle | Key Practices to Highlight |
|----------|----------------|-------|---------------------------|
| LinkedIn | [persona] | [angle] | [practices] |
| X/Twitter | [persona] | [angle] | [practices] |
| Reddit | [persona] | [angle] | [practices] |
| YouTube | [persona] | [angle] | [practices] |
| Reel/Short | [persona] | [angle] | [practices] |
```

## Integration with Scope Assessment

The dimension breadth score (0-2) feeds into the `content-scope-assessment` skill as the 8th scoring signal:

| Score | Criteria |
|-------|----------|
| **0** | 1 persona AND ≤3 total practices AND ≤1 primary WAF pillar |
| **1** | 2 personas OR 4-6 total practices OR 2-3 WAF pillars (primary + secondary) |
| **2** | 3+ personas AND 7+ total practices AND 3+ WAF pillars (primary + secondary) |

## Dimension-Informed Series Split Rules

When the scope assessment recommends a multi-part series, use dimension data to determine part boundaries:

1. **Primary split axis**: Choose the dimension type with the most natural groupings (usually best practices for technical topics, personas for cross-functional topics)
2. **Part 1 rule**: Always pair the highest-impact practice with the most common persona (usually the developer/IC). Part 1 must deliver a quick win.
3. **Pillar alignment**: Each part should map to 1-2 WAF pillars. Avoid mixing all 5 pillars into one part.
4. **Part-count neutrality**: Do not infer that a series must have 3 parts. Use the number of natural groups from the primary split axis, constrained to 2-5 parts.
5. **Persona progression**: If series has 3+ parts, consider a persona arc: Part 1 = IC developer, middle parts = tech lead/architect, final part = manager/executive.
6. **Standalone check**: Each part must have at least 2 practices with standalone value = yes.

## Constraints

- DO NOT generate separate content per persona or per pillar — dimensions inform structure only
- DO NOT force WAF pillar relevance where none exists — use `none` for irrelevant pillars
- DO NOT exceed 6 personas — consolidate similar roles (e.g., "Staff Engineer" and "Principal Engineer" are one persona)
- ALWAYS include both technology and governance practices — even if one category has only 1-2 items
- ALWAYS assess all 5 WAF pillars — mark irrelevant ones as `none`
