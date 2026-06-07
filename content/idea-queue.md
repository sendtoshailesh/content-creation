# Content Idea Queue

> **Curated content ideas** extracted from configured feed sources. Run `@feed-curator` to discover fresh ideas. Pick an idea and run `@content-pipeline` or use `/select-idea` to auto-populate the pipeline config.

Last curated: _(not yet run)_

---

## Queued Ideas

<!-- Ideas are appended here by the feed-curator agent, ranked by score. -->
<!-- Format for each idea:

### [Rank] Idea Title
- **Score**: X/25 (relevance + data density + timeliness + gap + validation)
- **Subject areas**: AI, Architecture
- **Source articles**:
  - [Article title](URL) — key insight extracted
  - [Article title](URL) — supporting data point
- **Content angle**: How to frame this as a blog post
- **Key data points**: Specific numbers/benchmarks to use
- **Timeliness**: Why this matters now
- **Status**: `queued`

-->

### [1] How to Evaluate AI Agents Before They Break Production — The Sourdough Test & Beyond
- **Score**: 23/25 (relevance: 5 + data density: 5 + timeliness: 5 + gap: 4 + validation: 4)
- **Subject areas**: AI & LLM, DevOps & Platform Engineering, Architecture
- **Source articles**:
  - [First-party] Azure/git-ape-private repo — built and operated the eval system (Waza) with 14 agents/skills, 38 tasks, 3 grader types
  - [First-party] Live-tested all CLI commands, built workshop Labs 07+08, analyzed CI workflow (1,029 lines)
- **Content angle**: Practitioner deep-dive — "I built an agent evaluation system for GitHub Copilot agents that deploy real Azure infrastructure. Here's the taxonomy of what can go wrong and how to test for it." Unique concepts: The Sourdough Test, Fabrication Without Action, Binary Grading as Feature, Safety Gate vs Off-Topic distinction, Tool Name Translation gotcha
- **Key data points**: 14 agents/skills evaluated, 38 task definitions, 3 grader types (text/tool_constraint/prompt), 4 task patterns (positive/negative/safety/gated), $3-8 per eval run, ~200K-400K tokens per full run, 5 model regressions caught, `continue_session: true` as #1 gotcha
- **Timeliness**: Agentic AI moving from autocomplete to autonomous operations; model updates (Claude 4.5→4.6, GPT-5.x) create silent behavioral regressions; no established industry practice for agent evaluation yet — thought leadership opportunity
- **Knowledge extract**: `content/agent-eval-knowledge-extract.md` (34K chars, 100% first-party, zero external dependencies)
- **Suggested series**: Yes (Part 1: Why agent eval ≠ model benchmarks + taxonomy, Part 2: Building the eval system + grader deep-dive, Part 3: Operational lessons + roadmap)
- **Status**: `queued`

_(Run `@feed-curator` to populate this queue with content ideas from your configured sources.)_

---

## Archive (Previously Processed)

> Ideas that were selected for the pipeline, published, or dismissed. Kept for deduplication — the feed curator checks this section to avoid re-suggesting old ideas.

<!-- Archived ideas are moved here with their final status:
- `selected` — Picked for pipeline, may be in-progress
- `in-pipeline` — Currently being processed by the content pipeline
- `published` — Content was created and published
- `dismissed` — Rejected, not interesting enough
-->
