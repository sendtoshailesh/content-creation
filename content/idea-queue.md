# Content Idea Queue

> **Curated content ideas** extracted from configured feed sources. Run `@feed-curator` to discover fresh ideas. Pick an idea and run `@content-pipeline` or use `/select-idea` to auto-populate the pipeline config.

Last curated: 2026-06-08 (Apple Notes — 37 notes analyzed, 18 content-relevant, 7 ideas queued)

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

### [2] WebMCP & Browser AI Agents — The Most Architecturally Significant Shift from Google I/O
- **Score**: 21/25 (R:4 D:4 T:5 G:5 V:3)
- **Subject areas**: AI & LLM, Architecture, Developer Productivity
- **Source**: Apple Notes (last 30 days)
- **Source notes**:
  - "WebMCP enters origin trial with Chrome 149" — WebMCP is a proposed open web standard, co-authored with Microsoft, that lets any website expose structured tools directly to in-browser AI agents via client-side JavaScript or HTML form annotations without a backend MCP server. Entering origin trial now.
  - "Lightweight Microsoft computer use agents beat Google, OpenAI" — Microsoft Research released Fara1.5, a lightweight computer-use agent that outperforms Google and OpenAI on benchmarks
- **Content angle**: "WebMCP is the most architecturally significant thing from Google I/O — and almost nobody noticed. Here's what it means for how we build AI-powered web apps." Practitioner angle: how WebMCP eliminates the need for backend MCP servers, what the origin trial means for early adopters, and how Microsoft's Fara1.5 complements the browser-native agent story.
- **Key data points**: Chrome 149 origin trial, co-authored with Microsoft, client-side JavaScript + HTML form annotations, no backend MCP server required
- **Timeliness**: Origin trial active NOW in Chrome 149 — publish within 2-3 weeks for maximum relevance
- **Status**: `queued`

### [3] Agentic Design Patterns: A Decision-Tree for Choosing the Right Pattern
- **Score**: 20/25 (R:5 D:3 T:4 G:4 V:4)
- **Subject areas**: AI & LLM, Architecture, Solution Architecture
- **Source**: Apple Notes (last 30 days)
- **Source notes**:
  - "Choosing the Right Agentic Design Pattern: A Decision-Tree Approach" — Decision-tree framework for pattern selection, linked to Andrew Ng's transformers course
  - "The Infrastructure Behind Making Local LLM Agents Actually Useful" — Infrastructure requirements for different agent patterns
  - "Decision Boundary: Deterministic vs Retrieval vs Synthesis" — Classification of AI response types and when each applies
  - "How data engineers and DBA can use agentic platform engineering tools" — Applying agentic patterns to data engineering workflows
- **Content angle**: "A practitioner's decision tree for agentic design patterns — when to use ReAct vs planning vs tool-use, with concrete infrastructure requirements for each. Includes the often-missed 'Decision Boundary' framework: deterministic vs retrieval vs synthesis."
- **Key data points**: Andrew Ng course reference, 3+ design patterns compared, infrastructure requirements per pattern
- **Timeliness**: Agentic AI adoption accelerating; teams need practical guidance on pattern selection, not just framework overviews
- **Embedded references**: https://www.linkedin.com/posts/andrewyng_new-course-transformers-in-practice-youll-ugcPost-7460729989060001792
- **Status**: `queued`

### [4] Agent Eval & Failure Taxonomy — Supporting Research for Sourdough Test Series
- **Score**: 21/25 (R:5 D:4 T:4 G:3 V:5)
- **Subject areas**: AI & LLM, Architecture, DevOps & Platform Engineering
- **Source**: Apple Notes (last 30 days)
- **Note**: ⚠️ Overlaps with queued idea [1] "Sourdough Test" — these notes provide complementary research material (failure taxonomy, 12-metric framework, evaluation methods) that can enrich the existing series.
- **Source notes**:
  - "Agentic evaluation methods" (7K chars) — Evaluation process for measuring autonomous intelligence: plan → reason → act → adapt across multi-steps. Combines simulation environments, NLM assessment review, and production readiness evaluation.
  - "Mitigate failures across the failure taxonomy" (6.7K chars) — System-level view: structured failure classification across agent lifecycle — reasoning, planning, execution, and output validation failures. Failure taxonomy for reliability, control and governance.
  - "Debugging not the code but debugging the reasoning" — Testing AI agent decisions differs from testing deterministic code logic. Paradigm shift in what "debugging" means.
  - "We have spent decade to calculate, classify, generate. Now we give them autonomy to Act" (9.9K chars) — Generative AI is reactive (prompt → response). Agentic AI uses continuous loop: plan → access tools → take action. Management challenge of autonomous decision-making.
  - "Building an Evaluation Harness for Production AI Agents: A 12-Metric Framework From 100+ Deployments" — Structured evaluation framework with 12 metrics derived from 100+ production deployments
- **Content angle**: Use as research input for the existing Sourdough Test series (Parts 2 & 3). The failure taxonomy and 12-metric framework provide concrete structure for the evaluation system deep-dive.
- **Key data points**: 12-metric framework, 100+ deployments, 4 failure categories (reasoning, planning, execution, output validation), continuous evaluation loop
- **Timeliness**: Directly supports the in-progress Sourdough Test content pipeline
- **Status**: `queued`

### [5] Coherence — When Tests Pass But Your Repo Is Broken: AI Agent Drift Detection
- **Score**: 19/25 (R:4 D:4 T:4 G:5 V:2)
- **Subject areas**: DevOps & Platform Engineering, AI & LLM
- **Source**: Apple Notes (last 30 days)
- **Source notes**:
  - "Coherence — A Git-Native Drift Detector for AI-Edited Codebases" (1.3K chars) — MIT-licensed CLI tool that catches broken links AI agents leave behind — between code, docs, ADRs, tests, metrics, generated files, and endpoints — even when tests are fully green. Uses a deterministic rules engine and knowledge graph.
- **Content angle**: "Tests passing doesn't mean your repo is consistent. An AI agent can delete a route, rename a metric, or orphan an endpoint and CI will never blink. Here's how Coherence catches the gap with a deterministic rules engine and a knowledge graph." Practitioner review + integration guide.
- **Key data points**: MIT license, deterministic rules engine, knowledge graph, catches: broken links between code/docs/ADRs/tests/metrics/endpoints
- **Timeliness**: AI-assisted coding adoption growing — drift detection is an emerging need with no established tooling category yet
- **Status**: `queued`

### [6] pgvector Ecosystem: pgvector vs pgvectorscale vs pgai — When to Use What
- **Score**: 17/25 (R:4 D:3 T:4 G:4 V:2)
- **Subject areas**: Databases, AI & LLM
- **Source**: Apple Notes (last 30 days)
- **Source notes**:
  - "pgvector, pgvectorscale, pgai" — Notes on the three PostgreSQL extensions for vector/AI workloads
- **Content angle**: "The pgvector ecosystem has quietly grown from one extension to three — each solving a different problem. Here's when to use pgvector (basic vector ops), pgvectorscale (billion-scale search), and pgai (model inference in-database)." Practitioner comparison with benchmarks.
- **Key data points**: 3 PostgreSQL extensions compared, different scale/use-case targets
- **Timeliness**: pgvector ecosystem rapidly maturing; many teams using pgvector don't know about pgvectorscale and pgai
- **Status**: `queued`

### [7] From TF-IDF to Transformers: Implementing Four Generations of Semantic Search
- **Score**: 15/25 (R:4 D:3 T:3 G:3 V:2)
- **Subject areas**: AI & LLM, Machine Learning
- **Source**: Apple Notes (last 30 days)
- **Source notes**:
  - "From TF-IDF to Transformers: Implementing Four Generations of Semantic Search" — Educational walkthrough of 4 search paradigm generations
- **Content angle**: Implementation-focused walkthrough of 4 search generations (TF-IDF → BM25 → dense embeddings → transformer re-rankers). Code-heavy tutorial with side-by-side performance comparisons.
- **Key data points**: 4 generations of search, implementation comparison
- **Timeliness**: RAG pipelines making search architecture decisions daily — foundational knowledge still has gaps
- **Status**: `queued`

### [8] Microsoft Foundry PTU Cost Optimization — Saving with Reserved Capacity
- **Score**: 16/25 (R:4 D:3 T:4 G:3 V:2)
- **Subject areas**: Cloud & Infrastructure, AI & LLM
- **Source**: Apple Notes (last 30 days)
- **Source notes**:
  - "Saving with Microsoft Foundry PTU reservations" — Foundry Model Acceleration Sales Kit, PTU reservation cost patterns
- **Embedded references**: Microsoft SharePoint Foundry Model Acceleration Sales Kit
- **Content angle**: "How to right-size PTU reservations in Azure AI Foundry — the math behind reserved vs. pay-as-you-go, and when reservations actually save money." Cost optimization practitioner guide.
- **Key data points**: PTU reservation pricing, Foundry Model Acceleration patterns
- **Timeliness**: Azure AI Foundry adoption growing; cost optimization is top concern for enterprise AI teams
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
