# Content Idea Queue

> **Curated content ideas** extracted from configured feed sources. Run `@feed-curator` to discover fresh ideas. Pick an idea and run `@content-pipeline` or use `/select-idea` to auto-populate the pipeline config.
>
> **Feeds:** `@feed-curator` (blogs/RSS) · `@reading-list-curator` / `@apple-notes-curator` / `@social-saves-curator` (saved reading) · `post-run-reflection` skill (the pipeline's own completed runs — cut scope, open questions, unwritten parts, validated angles). All write the 25-point entry format below.

Last curated: 2026-06-19 (Feeds only — 92 articles from 7 live sources; 61 published since the 06-15 run. 5 new ideas queued ([23]–[27]) + 7 existing ideas reinforced with fresh articles; total now 27)

> **Source health (2026-06-19 run):** GitHub Blog ✅ 6 · DeepLearning.AI Batch ✅ 20 · Towards Data Science ✅ 20 · Simon Willison ✅ 23 · InfoQ ✅ 15 · PostgreSQL Weekly ✅ 6 · TLDR AI ✅ 2 · The Pragmatic Engineer ⚠️ empty (paywall/login — persistent). 7 of 8 sources live.
>
> **Previous (2026-06-15 run):** GitHub Blog ✅ 8 · DeepLearning.AI Batch ✅ 20 · Towards Data Science ✅ 20 · Simon Willison ✅ 30 · InfoQ ✅ 15 (14 dated) · PostgreSQL Weekly ✅ 6 (recovered — issue #652 now parses; was nav-only on 06-09) · TLDR AI ✅ 2 · The Pragmatic Engineer ⚠️ empty (paywall/login — persistent). 7 of 8 sources live.

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

### [1] AI Agent Evals: Why SWE-bench Isn't Enough Before Production — The Sourdough Test & Beyond
- **Score**: 23/25 (relevance: 5 + data density: 5 + timeliness: 5 + gap: 4 + validation: 4)
- **Subject areas**: AI & LLM, DevOps & Platform Engineering, Architecture
- **Source articles**:
  - [First-party] [Azure/git-ape](https://github.com/Azure/git-ape) repo — built and operated the eval system (Waza) with 14 agents/skills, 38 tasks, 3 grader types
  - [First-party] Live-tested all CLI commands, built workshop Labs 07+08, analyzed CI workflow (1,029 lines)
- **Content angle**: Practitioner deep-dive — "I built an agent evaluation system for GitHub Copilot agents that deploy real Azure infrastructure. Here's the taxonomy of what can go wrong and how to test for it." Unique concepts: The Sourdough Test, Fabrication Without Action, Binary Grading as Feature, Safety Gate vs Off-Topic distinction, Tool Name Translation gotcha
- **Key data points**: 14 agents/skills evaluated, 38 task definitions, 3 grader types (text/tool_constraint/prompt), 4 task patterns (positive/negative/safety/gated), $3-8 per eval run, ~200K-400K tokens per full run, 5 model regressions caught, `continue_session: true` as #1 gotcha
- **Timeliness**: Agentic AI moving from autocomplete to autonomous operations; model updates (Claude 4.5→4.6, GPT-5.x) create silent behavioral regressions; no established industry practice for agent evaluation yet — thought leadership opportunity
- **Knowledge extract**: `content/agent-eval-knowledge-extract.md` (34K chars, 100% first-party, zero external dependencies)
- **Suggested series**: Yes — consolidated to 2 parts (Part 1: Why agent eval ≠ model benchmarks + taxonomy, Part 2: Building the eval system + grader deep-dive + operational lessons + roadmap)
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

<!-- ───────── New ideas from 2026-06-09 all-sources run (RSS/newsletter feeds) ───────── -->

### [9] The AI Coding Cost Reckoning — FinOps for Token-Burning Agents
- **Score**: 24/25 (R:5 D:5 T:5 G:4 V:5)
- **Subject areas**: Developer Productivity, Cloud & Infrastructure, AI & LLM
- **Source**: RSS feeds (Simon Willison's Weblog, DeepLearning.AI Batch)
- **Source articles**:
  - [Uber Caps Usage of AI Tools Like Claude Code to Manage Costs](https://simonwillison.net/2026/Jun/3/uber-caps-usage/) — Uber limits all employees to **$1,500/month per AI coding tool**; previously blew its entire 2026 AI budget in **4 months**
  - [Anthropic's run-rate revenue hits $47 billion](https://simonwillison.net/2026/May/29/anthropic/) — $65B Series H; run-rate crossed $47B (annualized from a single month × 13) — shows how fast agent token spend is compounding
  - [The solution might be cancelling my AI subscription](https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/) — practitioner spins up 16+ unintended projects; "quick script" sessions balloon into hours of token spend
  - [GLM 5.1 Thinks Strategically / coding-agent acceleration](https://www.deeplearning.ai/the-batch/issue-350) — Andrew Ng ranks where agents actually pay off: frontend > backend > infrastructure > research
- **Content angle**: "Your AI coding bill is the new cloud bill — and most teams have no FinOps for it. Here's how to budget, cap, and govern token spend per developer and per tool, plus where agents actually return the investment (frontend vs. backend vs. infra)."
- **Key data points**: $1,500/mo/tool Uber cap, 2026 budget gone in 4 months, $47B Anthropic run-rate, agent acceleration ranking by software layer
- **Timeliness**: Uber cap reported this week; enterprises setting 2026 AI budgets are getting burned — peak relevance now
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [10] Containing the Agent — Sandboxing & Prompt-Injection Defense in Production
- **Score**: 24/25 (R:5 D:4 T:5 G:5 V:5)
- **Subject areas**: AI & LLM, DevOps & Platform Engineering, Architecture
- **Source**: RSS feeds (Simon Willison's Weblog, InfoQ)
- **Source articles**:
  - [How we contain Claude across products](https://simonwillison.net/2026/May/30/how-we-contain-claude/) — Anthropic's defense-in-depth: process sandboxes, VMs, filesystem boundaries, and egress controls
  - [OpenAI Help: Lockdown Mode](https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/) — limits outbound network requests to block the final data-exfiltration stage of a prompt-injection attack
  - [Hackers Simply Asked Meta AI to Give Them Access to High-Profile Instagram Accounts. It Worked](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/) — real account takeover via a support bot, no exploit code required
  - [AI-Driven Phishing: How the Technique Is Evolving](https://www.infoq.com/articles/artificial-intelligence-driven-phishing/) — Microsoft Digital Defense Report 2025: AI industrializes targeted phishing, removing traditional bottlenecks
  - [Running Python code in a sandbox with MicroPython and WASM](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/) — a concrete sandbox pattern for executing agent-generated code safely
- **Content angle**: "Agents that can act can be made to act against you. A defense-in-depth playbook: sandbox the runtime (VMs, filesystem, egress), add lockdown-style network controls, and treat every external input as a prompt-injection vector — illustrated with the Meta AI takeover and AI-phishing data."
- **Key data points**: 4 containment layers (process/VM/filesystem/egress), lockdown mode blocks outbound exfil, Meta IG takeover via support bot, MS Digital Defense Report 2025 phishing shift
- **Timeliness**: OpenAI Lockdown Mode rolled out this week; agent security is an unsolved, fast-moving space
- **Scope hypothesis**: `possible series` — security taxonomy + each control layer could each warrant a part
- **Status**: `queued`

### [11] From Prompts to Harness Engineering — The Workflow Shift in AI-Native Development
- **Score**: 23/25 (R:5 D:4 T:5 G:4 V:5)
- **Subject areas**: Developer Productivity, AI & LLM, Architecture
- **Source**: RSS feeds (GitHub Blog, Towards Data Science, InfoQ)
- **Source articles**:
  - [From one-off prompts to workflows: How to use custom agents in GitHub Copilot CLI](https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/) — custom agents turn repeatable prompts into reusable terminal workflows
  - [Podcast: From MCP and Vibe Coding to Harness Engineering](https://www.infoq.com/podcasts/mcp-vibe-coding-harness-engineering/) — Thoughtworks' Birgitta Böckeler: monolithic context files and MCP servers giving way to lazy-loaded **skills**, CLIs, and scripts
  - [How to Navigate the Shift from Prompt-Based Tools to Workflow-Driven AI](https://towardsdatascience.com/how-to-navigate-the-shift-from-prompt-based-tools-to-workflow-driven-ai/) — the cost of constant tool/context switching and how workflows fix it
  - [Automate Writing Your LLM Prompts](https://towardsdatascience.com/automate-writing-your-llm-prompts/) — writing robust, reliable prompts for unattended LLM applications
- **Content angle**: "Vibe coding was step one. The teams winning now have moved from ad-hoc prompts to engineered harnesses — custom agents, lazy-loaded skills, and scripted workflows. Here's the maturity curve and how to build your own (first-party: this very content pipeline runs on it)."
- **Key data points**: custom agents in Copilot CLI, skills-replace-MCP-servers thesis, context-switching cost, prompt-as-code reliability
- **Timeliness**: GitHub Blog post published 2026-06-09; "harness engineering" framing is emerging now
- **Scope hypothesis**: `single-post candidate` — strong first-party angle from this repo's own agent/skill architecture
- **Status**: `queued`

### [12] Local & On-Device Agents Go Mainstream — Small Models, Real Autonomy
- **Score**: 21/25 (R:4 D:4 T:5 G:4 V:4)
- **Subject areas**: AI & LLM, Machine Learning, Developer Productivity
- **Source**: RSS feeds (InfoQ, Simon Willison) + Apple Notes
- **Source articles**:
  - [Gemma 4 12B Enables On-Device, Multimodal Agentic Workflows](https://www.infoq.com/news/2026/06/google-gemma4-12b-local-coding/) — novel **encoder-free** unified multimodal architecture; runs agentic workflows on everyday laptops via Google AI Edge
  - [Microsoft's new MAI models](https://simonwillison.net/2026/Jun/2/microsofts-new-models/) — **MAI-Code-1-Flash (137B params, 5B active)** purpose-built for GitHub Copilot/VS Code for high performance at lower cost; MAI-Thinking-1 (1T/35B active)
  - "Lightweight Microsoft computer use agents beat Google, OpenAI" (Apple Notes) — Microsoft Research **Fara1.5** lightweight computer-use agent outperforms larger rivals on benchmarks
  - "The Infrastructure Behind Making Local LLM Agents Actually Useful" (Apple Notes) — what local agent deployments actually require
- **Content angle**: "The agent that runs on your laptop just got good. Encoder-free Gemma 4, MoE models with tiny active-parameter counts (MAI-Code-1-Flash: 5B of 137B active), and lightweight computer-use agents are moving real autonomy on-device — here's what it changes for cost, privacy, and latency."
- **Key data points**: Gemma 4 12B encoder-free, MAI-Code-1-Flash 137B/5B active, MAI-Thinking-1 1T/35B active, Fara1.5 benchmark wins
- **Timeliness**: All three model announcements landed at/around Build 2026 (early June)
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [13] Production-Grade Agentic Inference — Killing Redundant GPU Work
- **Score**: 20/25 (R:4 D:5 T:4 G:4 V:3)
- **Subject areas**: Machine Learning, AI & LLM, Cloud & Infrastructure
- **Source**: RSS feeds (Towards Data Science, DeepLearning.AI, InfoQ)
- **Source articles**:
  - [Prefill Once, Fan Out: KV Snapshot Sharing for Multi-Agent LLM Pipelines](https://towardsdatascience.com/kv-cache-reuse-for-multi-agent-llm-inference-i-built-a-c-orchestrator-so-my-gpu-would-stop-reading-the-same-document-twice/) — SwarmKV makes a two-agent pipeline **~1.95× faster** and the second branch's activation latency **52× faster** via KV-snapshot fan-out
  - [The Hardware That Makes AI Possible](https://towardsdatascience.com/the-hardware-that-makes-ai-possible/) — why traditional hardware wasn't built for trillions of ops per inference
  - [AWS Releases Next Generation of Amazon OpenSearch Serverless](https://www.infoq.com/news/2026/06/aws-opensearch-serverless/) — **20× faster** provisioning, true scale-to-zero, up to **60% lower cost** for peak loads; positioned for agentic AI
- **Content angle**: "Multi-agent pipelines re-read the same documents over and over. A practitioner's guide to eliminating redundant prefill and waiting — KV-cache snapshot sharing, scale-to-zero serving, and the hardware constraints driving it all."
- **Key data points**: 1.95× pipeline speedup, 52× activation-latency cut, 20× faster provisioning, 60% lower cost, scale-to-zero
- **Timeliness**: "Production-Grade Agentic Inference" series Part 1 published 2026-06-09; inference cost is the bottleneck for agent economics
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [14] 10 RAG Mistakes in Production — and the Four Generations of Retrieval
- **Score**: 20/25 (R:5 D:4 T:4 G:3 V:4)
- **Subject areas**: AI & LLM, Databases, Machine Learning
- **Source**: RSS feeds (Towards Data Science) + Apple Notes
- **Note**: ⚠️ Complements queued ideas [6] (pgvector ecosystem) and [7] (TF-IDF→Transformers) — could be consolidated into one retrieval mega-series.
- **Source articles**:
  - [10 Common RAG Mistakes We Keep Seeing in Production](https://towardsdatascience.com/10-common-rag-mistakes-we-keep-seeing-in-production/) — enterprise RAG fails when the question spans a whole corpus, not one document; concrete anti-patterns
  - [Increase Recommendation Systems' Precision with LLMs, Using Python](https://towardsdatascience.com/increase-recommendation-systems-precision-with-llm-using-python/) — tradeoffs in LLM-augmented retrieval
  - "From TF-IDF to Transformers: Implementing Four Generations of Semantic Search" (Apple Notes) — TF-IDF → BM25 → dense embeddings → transformer re-rankers
- **Content angle**: "Most RAG demos work on one PDF and fall apart on a corpus. Here are the 10 mistakes that kill production RAG, mapped onto the four generations of retrieval — so you know which generation each fix actually requires."
- **Key data points**: 10 named RAG anti-patterns, 4 retrieval generations, corpus-vs-document failure mode
- **Timeliness**: RAG mistakes article published 2026-06-09; retrieval is the #1 production-LLM pain point
- **Scope hypothesis**: `possible series` — overlaps existing retrieval ideas; scope assessment should decide consolidation
- **Status**: `queued`

### [15] The Open-Source Trust Crisis in the Agent Era — Who Owns AI-Written Code?
- **Score**: 20/25 (R:4 D:3 T:4 G:5 V:4)
- **Subject areas**: DevOps & Platform Engineering, Architecture, AI & LLM
- **Source**: RSS feeds (Simon Willison, InfoQ) + Apple Notes
- **Source articles**:
  - [Quoting Andreas Kling (Ladybird)](https://simonwillison.net/2026/Jun/5/andreas-kling/) — Ladybird will **no longer accept public pull requests**; a substantial patch no longer signals substantial effort/good faith in the AI era
  - [sqlite AGENTS.md](https://simonwillison.net/2026/May/27/sqlite-agents/) — SQLite won't accept PRs without prior agreement/public-domain paperwork; documents its stance toward agents pointed at the codebase
  - [Presentation: Confidently Automating Changes Across a Diverse Fleet](https://www.infoq.com/presentations/automate-fleetwide-changes/) — Netflix's approach to automating code changes across a heterogeneous fleet *with confidence*
  - "Coherence — A Git-Native Drift Detector for AI-Edited Codebases" (Apple Notes, also idea [5]) — catches broken links AI agents leave behind even when tests are green
- **Content angle**: "When anyone can generate a 'substantial' patch in seconds, the cost signal that open source relied on collapses. Ladybird and SQLite are closing PRs; Netflix is automating fleet-wide changes with guardrails. Here's the new contract for trust, ownership, and accountability of AI-written code."
- **Key data points**: Ladybird no-public-PR policy, SQLite agent policy, Netflix fleet automation, deterministic drift detection (Coherence)
- **Timeliness**: Ladybird stance quoted 2026-06-05; live debate about AI contributions to OSS
- **Scope hypothesis**: `single-post candidate` — strong opinion/thought-leadership angle
- **Status**: `queued`

### [16] Microsoft Foundry Grows Up — Runtime, Memory & Governance for Production Agents
- **Score**: 18/25 (R:4 D:3 T:5 G:3 V:3)
- **Subject areas**: Cloud & Infrastructure, AI & LLM, Solution Architecture
- **Source**: RSS feeds (InfoQ) + Apple Notes
- **Note**: ⚠️ Complements queued idea [8] (Foundry PTU cost optimization) — could pair as a "Foundry in production" two-parter (capabilities + cost).
- **Source articles**:
  - [Microsoft Foundry Adds Runtime, Tooling, and Governance for Production Agents](https://www.infoq.com/news/2026/06/microsoft-foundry-agents/) — Build 2026: runtime, tools, memory, grounding, models, observability, and governance — "where agents move from experiments to production"
  - [Microsoft Launches Logic Apps Automation at Build 2026](https://www.infoq.com/news/2026/06/azure-logic-apps-automation/) — managed SaaS at auto.azure.com; production automations without a dedicated integration developer, keeping enterprise governance
  - "Saving with Microsoft Foundry PTU reservations" (Apple Notes, also idea [8]) — PTU reservation cost patterns
- **Content angle**: "Azure AI Foundry just shipped the unglamorous parts that actually matter for production agents — runtime, memory, grounding, observability, and governance. A practitioner's tour of what moved from preview to GA at Build 2026 and how to wire it together (with the cost math)."
- **Key data points**: 7 Foundry production capabilities (runtime/tools/memory/grounding/models/observability/governance), Logic Apps Automation SaaS, PTU reservation economics
- **Timeliness**: Announced at Build 2026 (early June) — fresh, Azure-aligned
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

<!-- ───────── New ideas from 2026-06-09 all-sources run (fresh Apple Notes since 06-08) ───────── -->

### [17] Design Patterns for AI-Native Apps — and Modernizing Existing Apps to AI-Native
- **Score**: 16/25 (R:4 D:2 T:4 G:4 V:2)
- **Subject areas**: Architecture, Solution Architecture, AI & LLM
- **Source**: Apple Notes (captured 2026-06-07)
- **Source notes**:
  - "Design patterns for ai native apps and how to modernise the existing app to ai native apps" — seed note on patterns for greenfield AI-native apps vs. retrofitting existing systems
- **Content angle**: "Most teams aren't building AI-native from scratch — they're modernizing apps that already exist. A pattern catalog for both paths: what 'AI-native' actually means architecturally, and a migration ladder from a conventional app to an agentic one."
- **Key data points**: _(needs research — note is a seed; pair with InfoQ harness-engineering podcast and Foundry production capabilities)_
- **Timeliness**: AI-native modernization is the dominant enterprise question of 2026
- **Scope hypothesis**: `possible series` — greenfield patterns vs. brownfield modernization are natural parts
- **Status**: `queued`

### [18] Why Spec-Driven Development Is Still Hard in the Agent Era
- **Score**: 16/25 (R:4 D:2 T:4 G:4 V:2)
- **Subject areas**: Developer Productivity, AI & LLM, Architecture
- **Source**: Apple Notes (captured 2026-06-07)
- **Source notes**:
  - "What and why still spec driven development is challenge and what to avoid" — seed note on persistent friction in spec-driven development and anti-patterns to avoid
- **Content angle**: "Spec-driven development promised that agents would just build what we specify. In practice the spec keeps drifting from the code. Here's why spec-first still breaks with coding agents, the anti-patterns to avoid, and a workflow that actually keeps specs and implementation in sync."
- **Key data points**: _(needs research — note is a seed; pair with Coherence drift detection and harness-engineering sources)_
- **Timeliness**: Spec-driven/"plan then build" workflows are heavily promoted but under-examined
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

<!-- ───────── New ideas from 2026-06-15 feeds-only run (articles since 06-09) ───────── -->

### [19] When Your Model Gets Pulled Overnight — Hidden Safeguards, Export Controls & Vendor Risk in the Agent Era
- **Score**: 22/25 (R:4 D:4 T:5 G:5 V:4)
- **Subject areas**: AI & LLM, Solution Architecture, DevOps & Platform Engineering
- **Source**: RSS feeds (Simon Willison's Weblog ×4, InfoQ, DeepLearning.AI Batch)
- **Source articles**:
  - [Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/) — US export-control directive (received 5:21pm ET) forced Anthropic to **abruptly disable Fable 5 and Mythos 5 for all customers**, citing a jailbreak technique; other Anthropic models unaffected
  - [Anthropic Releases and Temporarily Suspends Claude Fable 5](https://www.infoq.com/news/2026/06/claude-5-release/) — released Jun 9, offline within **3 days**; $10/M input, $50/M output (**2× Opus 4.8**), 1M-token context, 128K output; shipped same day on Claude API, AWS, and **Microsoft Foundry**
  - [Anthropic Walks Back Policy That Could Have 'Sabotaged' AI Researchers Using Claude](https://simonwillison.net/2026/Jun/11/anthropic-walks-back-policy/) — Anthropic had a system-card policy to silently "limit effectiveness" of flagged requests; after outcry, flagged requests now **visibly** fall back to Opus 4.8 ("we made the wrong tradeoff")
  - [Claude Fable is relentlessly proactive](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/) — frontier autonomy: the model will deploy "pretty much any trick" to reach a goal unsupervised, raising the stakes of behavioral changes
  - [Initial impressions of Claude Fable 5](https://simonwillison.net/2026/Jun/9/claude-fable-5/) — new API mechanisms to signal guardrail hits and **auto-fall-back to another model** when a request is rejected
- **Content angle**: "A frontier model you build on can be made invisible to you — or pulled offline overnight by a government directive. Here's why production agents need model abstraction, multi-provider fallback, and governance for silent behavioral changes, illustrated by the Fable 5 / Mythos 5 saga."
- **Key data points**: Fable 5 live→offline in 3 days, export directive 5:21pm ET, $10/$50 per M tokens (2× Opus 4.8), 1M context / 128K output, invisible→visible safeguard reversal, automatic model fallback as a new API primitive
- **Timeliness**: Breaking 06-09 → 06-14; the suspension and policy reversal are days old — peak relevance for a "vendor risk / model abstraction" thesis
- **Scope hypothesis**: `single-post candidate` — strong opinion/architecture thought-leadership angle
- **Status**: `queued`

### [20] Enterprise Document Intelligence — The PDF Parsing Layer That Makes or Breaks RAG
- **Score**: 21/25 (R:5 D:5 T:4 G:4 V:3)
- **Subject areas**: AI & LLM, Databases, Machine Learning
- **Note**: ⚠️ Complements queued ideas [14] (10 RAG mistakes), [6] (pgvector), and [7] (search generations) — but distinct: this is the **ingestion/parsing** brick, upstream of retrieval. Scope assessment should decide whether to fold into a retrieval mega-series.
- **Source**: RSS feeds (Towards Data Science — "Enterprise Document Intelligence" series, 5+ parts)
- **Source articles**:
  - [Stop Returning Flat Text from a PDF: The Relational Tables RAG Needs](https://towardsdatascience.com/stop-returning-flat-text-from-a-pdf-the-relational-shape-rag-needs/) — `text = extract_text(pdf)` is where RAG breaks; a good parser emits **7-8 relational tables** (toc/line/table/image…), not one flat string, so a page-14 table keeps its columns
  - [Beyond extract_text: The Two Layers of a PDF That Drive RAG Quality](https://towardsdatascience.com/beyond-extract_text-the-two-layers-of-a-pdf-that-drive-rag-quality/) — born-digital vs scanned detection; OCR-quality-0.3 turns "Renewal fee EUR 250" into "Renewa1 fee EUR 25O" and keyword retrieval silently misses
  - [When PyMuPDF Can't See the Table: Parse PDFs for RAG with Azure Layout](https://towardsdatascience.com/when-pymupdf-cant-see-the-table-parse-pdfs-for-rag-with-azure-layout/) — fitz goes blind in 3 places (tables, scanned pages, text-in-figures); **Azure Document Intelligence** prebuilt-layout recovers cells, OCR, figures, and paragraph roles in one call
  - [Parse PDFs for RAG Locally with Docling: Rich Tables, No Cloud Upload](https://towardsdatascience.com/parse-pdfs-for-rag-locally-with-docling-rich-tables-no-cloud-upload/) — **Docling** (IBM Research, MIT license, TableFormer) gives the same relational output fully offline for compliance-sensitive data
  - [Vision LLMs are PDF Parsers Too: Reading Charts and Diagrams for RAG](https://towardsdatascience.com/vision-llms-are-pdf-parsers-too-reading-charts-and-diagrams-for-rag/) — vision models read charts text-parsers see as empty boxes; **gpt-4.1 reads a chart gpt-4o-mini half-misses** — use selectively for picture-heavy pages
  - [Larger Context Windows Don't Fix RAG — So I Built a System That Does](https://towardsdatascience.com/larger-context-windows-dont-fix-rag-so-i-built-a-system-that-does/) — measured across **7 query types × 5 context sizes on 100,000 rows**; the fix is routing computation queries away from RAG entirely
- **Content angle**: "Most RAG failures are blamed on the model, but they start at `extract_text()`. A practitioner's tour of the parsing layer — relational table extraction, OCR-quality gates, Azure Document Intelligence vs. Docling (cloud vs. on-prem), and when to reach for a vision LLM — because retrieval can only be as good as what you fed it."
- **Key data points**: 7-8 relational tables per doc, OCR quality 0.3 corruption example, fitz blind in 3 places, Azure DI prebuilt-layout one-call enrichment, Docling MIT/TableFormer offline, gpt-4.1 vs gpt-4o-mini chart reading, 7×5×100K benchmark
- **Timeliness**: TDS "Enterprise Document Intelligence" series publishing through 06-10→06-14; document parsing is the under-covered half of the RAG conversation
- **Scope hypothesis**: `possible series` — parsing → retrieval → generation map naturally onto parts; overlaps existing retrieval ideas
- **Status**: `queued`

### [21] MCP Goes Operational — Agents Reach Into Your Infrastructure and Data
- **Score**: 21/25 (R:4 D:4 T:5 G:4 V:4)
- **Subject areas**: Cloud & Infrastructure, AI & LLM, DevOps & Platform Engineering
- **Note**: ⚠️ Distinct from queued idea [2] (WebMCP — *browser* actuation). This idea is about **backend infrastructure and data-plane** MCP servers.
- **Source**: RSS feeds (InfoQ ×3)
- **Source articles**:
  - [Terraform MCP Server Enables AI Assistants to Interact with Terraform Infrastructure](https://www.infoq.com/news/2026/06/terraform-mcp-server-ga/) — HashiCorp ships **GA** of an open-source MCP server over Terraform Registry APIs; agents discover approved modules and enforce org policy instead of engineers manually searching private registries
  - [Pinecone Brings AI Agents Directly to Enterprise Data with Microsoft OneLake Integration](https://www.infoq.com/news/2026/06/pinecone-ai-agents-onelake/) — Pinecone Nexus + OneLake serves pre-built knowledge artifacts; Pinecone claims **>95% lower LLM token consumption** and **up to 30× faster** task execution vs. traditional retrieval (Build 2026)
  - [Google Launches Colab CLI for Developers, Automation, and AI Agents](https://www.infoq.com/news/2026/06/google-colab-cli/) — agents provision remote **GPU/TPU** runtimes and run jobs from the terminal, exposing cloud accelerators to agentic workflows
- **Content angle**: "WebMCP put agents into the browser; this wave puts them into your control plane. Terraform, OneLake, and Colab all shipped MCP/CLI surfaces in one week — here's the emerging pattern for governed, policy-enforcing agent access to infrastructure and enterprise data (and the token-cost math that makes it worth it)."
- **Key data points**: Terraform MCP Server GA (Registry APIs, policy/module governance), Pinecone+OneLake >95% token cut / up to 30× faster, Colab CLI GPU/TPU provisioning for agents
- **Timeliness**: All three landed 06-12→06-13 around Build 2026; "MCP for infra/data" is crystallizing into a category now
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [22] AI-Assisted Legacy Modernization — Migrating in Weeks, Not Years
- **Score**: 18/25 (R:4 D:3 T:4 G:4 V:3)
- **Subject areas**: Architecture, Solution Architecture, DevOps & Platform Engineering
- **Note**: ⚠️ Complements queued idea [17] (design patterns for AI-native / brownfield modernization) — this is the **case-study / execution** angle with real numbers.
- **Source**: RSS feeds (InfoQ ×2)
- **Source articles**:
  - [Presentation: Moving Mountains: Migrating Legacy Code in Weeks Instead of Years](https://www.infoq.com/presentations/refactoring-ai-agents/) — ServiceTitan Principal AI Engineer David Stein on using AI agents to compress migrations that "plan out to take months, quarters, years" into weeks
  - [Slack Eliminates SSH in EMR Pipelines, Migrates 700+ Jobs to Rest-Based Architecture](https://www.infoq.com/news/2026/06/slack-ssh-rest-quarry-migration/) — Slack moved **700+ Airflow operators** off direct-SSH EMR execution to a centralized REST job-submission layer across **8 data regions**, improving security and observability
- **Content angle**: "Migrations have always been the work everyone dreads. Two 2026 case studies — ServiceTitan compressing legacy migrations from years to weeks with AI agents, and Slack retiring SSH across 700+ jobs — show the new modernization playbook: agent-assisted refactoring plus a governed orchestration layer."
- **Key data points**: ServiceTitan AI-driven migrations (months/quarters/years → weeks), Slack 700+ Airflow operators SSH→REST across 8 regions
- **Timeliness**: Both published 06-12; AI-assisted modernization is the dominant enterprise question of 2026
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

<!-- ───────── New ideas from 2026-06-19 feeds-only run (articles since 06-15) ───────── -->

### [23] The AI-Era Software Supply Chain — Cooldowns, Coalitions, and the Hours-Not-Months Window
- **Score**: 23/25 (R:5 D:5 T:5 G:4 V:4)
- **Subject areas**: DevOps & Platform Engineering, Architecture, AI & LLM
- **Source**: RSS feeds (InfoQ ×3)
- **Source articles**:
  - [VS Code 1.123 Adds Two-Hour Extension Update Delay to Limit Supply Chain Attacks](https://www.infoq.com/news/2026/06/vscode-extension-update-delay/) — newly published extensions wait **2 hours** before auto-update; mirrors **pip 26.1's 7-day cooldown** (research found a 7-day cooldown would have stopped **8 of 10** analyzed supply-chain attacks); npm/pnpm/Yarn/Bun/RubyGems all added minimum-release-age settings. Catch: the delay exempts "trusted publishers" (Microsoft, GitHub, OpenAI) — the highest-value compromise targets
  - [Athena Coalition Brings Coordinated Defence to Open Source Security](https://www.infoq.com/news/2026/06/athena-security-coalition/) — Chainguard-led coalition of **24+ founders** (BNY, JPMorgan Chase, Cisco, Cloudflare, Docker, Kyndryl, PwC) using frontier AI to find/fix OSS vulns before attackers; the discovery→exploit gap has shrunk from **months/years to hours**; already running in production with findings in ~1 month
  - [GitLab 19.0 Embeds Agentic AI in Secrets, Merge Requests, and Supply Chain Security](https://www.infoq.com/news/2026/06/gitlab-19-agentic-ai/) — **SBOM dependency scanning GA** + Secrets Manager public beta (scoped per-job, audit-traceable, integrates Vault/AWS/Azure/GCP rather than replacing them)
- **Content angle**: "Frontier models can now read a whole dependency graph and chain flaws that survived years of human review — and the attacker gets there in hours, not months. The defensive playbook that emerged this month: package-manager cooldowns (pip's 7-day window would have stopped 8/10 attacks), IDE-extension delays, SBOM-by-default, and AI-vs-AI coalitions like Athena. Here's how to wire cooldowns, SBOM gating, and scoped secrets into your own supply chain."
- **Key data points**: 7-day cooldown stops 8/10 attacks, VS Code 2-hr delay (trusted-publisher carve-out), Athena 24+ members, discovery→exploit months→hours, GitLab SBOM GA, per-job-scoped secrets
- **Timeliness**: All three landed 06-18→06-19; package-ecosystem cooldowns are crystallizing into a cross-tooling norm right now
- **Scope hypothesis**: `single-post candidate` — could split into "attack side (AI finds vulns fast)" vs "defense side (cooldowns/SBOM/coalitions)" if it grows
- **Status**: `queued`

### [24] Agents With Their Own Identity — Continuous Authorization and OS-Level Trust for Autonomous Agents
- **Score**: 22/25 (R:5 D:4 T:5 G:4 V:4)
- **Subject areas**: AI & LLM, Solution Architecture, DevOps & Platform Engineering
- **Note**: ⚠️ Distinct from queued idea [10] (Containing the Agent — *runtime sandboxing / prompt-injection*). This idea is about **identity and runtime authorization** — who the agent is and whether each action should be allowed *right now* — not about boxing the process.
- **Source**: RSS feeds (InfoQ ×3)
- **Source articles**:
  - [Windows Platform Security and the Race to Secure AI Agents](https://www.infoq.com/news/2026/06/windows-security-agents/) — Microsoft positions Windows as the trustworthy OS for agents via the **Microsoft Execution Containers (MXC) SDK**: a policy-driven layer (JSON or TypeScript SDK) spanning process/session isolation → planned micro-VMs → Linux containers, with **identity and manageability built into the OS** (centrally managed via **Entra ID + Intune**, observed via **Defender + Purview**)
  - [Article: Designing Continuous Authorization for Sensitive Cloud Systems](https://www.infoq.com/articles/continuous-authorization-cloud/) — login-time RBAC leaves an active session unchecked (worked example: a rep with valid perms exports **5,000 patient records at 10 AM**, file hits personal email by 10:15, SIEM alerts hours later). Fix: evaluate **each sensitive operation as its own decision point** with behavioral baselines, selective evaluation + caching, and audit-ready evidence that doesn't expose the underlying data
  - [Microsoft Scout, New Enterprise Autopilot Built on OpenClaw](https://www.infoq.com/news/2026/06/microsoft-scout-openclaw-build/) — "Autopilot" agents run always-on **with their own identity**, executing privileged local ops (file read/write, shell, code patches, browser automation) — raising the stakes for per-action authorization
- **Content angle**: "When an agent acts with its own identity and runs unsupervised, login-time RBAC is the wrong abstraction — it authorizes the session, not the 5,000th record export at 10 AM. A practitioner's guide to runtime trust for agents: OS-level execution containers (MXC) with Entra/Intune governance, continuous per-action authorization with behavioral baselines, and audit evidence that survives a privacy review."
- **Key data points**: MXC isolation spectrum (process→session→micro-VM→Linux container), Entra ID/Intune/Defender/Purview governance, continuous-authz worked example (5,000 records / 10:00 / 10:15 exfil), per-operation decision points + behavioral baselines, agents acting with own identity
- **Timeliness**: All published 06-17→06-19 around Build 2026; agent identity/authorization is the next security frontier after sandboxing
- **Scope hypothesis**: `possible series` — OS-level containment+identity vs application-level continuous authorization are natural parts
- **Status**: `queued`

### [25] Event-Driven and Always-On Agents — Serverless Hosting Moves Agents from Chat to Continuous Work
- **Score**: 21/25 (R:5 D:4 T:5 G:4 V:3)
- **Subject areas**: Cloud & Infrastructure, AI & LLM, Architecture
- **Note**: ⚠️ Complements queued idea [16] (Foundry production capabilities) but distinct: this is specifically the **serverless / event-triggered hosting model** and the always-on paradigm shift, not the Foundry capability catalog.
- **Source**: RSS feeds (InfoQ ×2)
- **Source articles**:
  - [Azure Functions Ships Serverless Agents Runtime at Build 2026](https://www.infoq.com/news/2026/06/azure-functions-serverless-agent/) — agents declared in **`.agent.md`** files (markdown-first: instructions, tools, connections in one doc); **any trigger spawns an agent** (HTTP/Timer/Service Bus/Event Hubs/SQL/Cosmos DB + new Teams/Outlook/calendar/SharePoint triggers); **Flex Consumption scale-to-zero, per-second billing**; sandboxed code + browser via **ACA dynamic sessions**; **1,400+ managed connectors**; "no extra cold start beyond normal Functions"
  - [Microsoft Scout, New Enterprise Autopilot Built on OpenClaw](https://www.infoq.com/news/2026/06/microsoft-scout-openclaw-build/) — "Autopilots": **always-on agents** that act autonomously on your behalf without per-task prompting; the shift "from single exchanges to something more continuous" where the system "holds your priorities and acts on them"
- **Content angle**: "Agents are escaping the chat box. With serverless agent runtimes, any event — a Service Bus message, an Outlook mail, a calendar entry — can wake an agent that reasons, calls MCP tools, and acts through 1,400+ connectors, then scales back to zero. Pair that with always-on 'autopilot' agents and the architecture question flips from 'how do I answer' to 'what should fire when.' A practitioner's tour of event-driven + always-on agent hosting (and the cold-start/cost realities)."
- **Key data points**: `.agent.md` markdown-first model, every Functions trigger can spawn an agent, scale-to-zero + per-second billing, ACA dynamic sessions sandbox, 1,400+ connectors, autopilot always-on with own identity
- **Timeliness**: Both announced at/around Build 2026 (06-17→06-19); serverless agent hosting is a brand-new category
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [26] Stop Over-Engineering Your Agents — When Workflows, Plain Python, and MCP Beat Frameworks
- **Score**: 21/25 (R:5 D:4 T:4 G:4 V:4)
- **Subject areas**: AI & LLM, Architecture, Developer Productivity
- **Source**: RSS feeds (Towards Data Science ×3)
- **Source articles**:
  - [You Probably Don't Need an Agent Framework](https://towardsdatascience.com/you-probably-dont-need-an-agent-framework/) — hours lost comparing CrewAI/LangGraph/Microsoft Agent Framework before writing any code; for many useful LLM apps what reliably ships is a **workflow**, built with **plain Python + structured outputs + the Responses API**, no framework
  - [The Protocol That Cleaned Up Our Agent Architecture](https://towardsdatascience.com/the-protocol-that-cleaned-up-our-agent-architecture/) — LangGraph tool-calling is "a local concern": the same tool lived in **4 files** across orchestrator/validator/utility with a hand-wired human gate per tool; moving to a shared **MCP server** consolidated tools + put the human-in-the-loop at the protocol boundary
  - [LLM Fallbacks Break Agent Pipelines — I Built the Missing Recovery Layer](https://towardsdatascience.com/llm-fallbacks-break-agent-pipelines-i-built-the-missing-recovery-layer/) — a naive fallback router shows **100% completion but 0% schema integrity**: the backup model gets a payload formatted for a different engine, drops the `confidence` key, and the Validator never knows. Fix: catch the error, **rebuild the payload for the backup model, save progress before the swap** (std Python 3.12, zero deps)
- **Content angle**: "Everyone reaches for an agent framework and a multi-model fallback router on day one. Three practitioners independently found the opposite: a plain-Python workflow ships faster than an autonomous agent, an MCP server beats tool definitions scattered across four files, and a naive fallback that reads 100% green is silently emitting 0% valid schema. The 2026 correction — choose the simplest abstraction that survives production."
- **Key data points**: workflow > autonomous agent for many apps, plain Python + structured outputs (no framework), MCP consolidates 4 tool copies → 1 server, fallback router 100% completion / 0% schema integrity, save-progress-before-swap recovery pattern
- **Timeliness**: All three published 06-15→06-17; a clear counter-narrative forming against framework/agent over-engineering
- **Scope hypothesis**: `single-post candidate` — strong opinion + first-party angle (this repo's own skills/scripts harness embodies the thesis)
- **Status**: `queued`

### [27] Structured Outputs With LLMs — JSON Mode vs Function Calling vs Structured Outputs (and the Fallback Schema Trap)
- **Score**: 15/25 (R:4 D:3 T:3 G:3 V:2)
- **Subject areas**: AI & LLM, Developer Productivity
- **Note**: ⚠️ Shares the schema-integrity data point with idea [26]; keep as a tighter, evergreen explainer if [26] goes broad-thesis.
- **Source**: RSS feeds (Towards Data Science ×2)
- **Source articles**:
  - [Structured Outputs with LLMs: JSON Mode, Function Calling, and When to Use Each](https://towardsdatascience.com/structured-outputs-with-llms-json-mode-function-calling-and-when-to-use-each/) — three commonly-confused mechanisms: **JSON Mode** (valid JSON, no schema guarantee), **Function Calling / tool use** (model picks a tool + args), and OpenAI's stricter **Structured Outputs** (hard schema enforcement); how each works under the hood and when to reach for which
  - [LLM Fallbacks Break Agent Pipelines](https://towardsdatascience.com/llm-fallbacks-break-agent-pipelines-i-built-the-missing-recovery-layer/) — concrete failure mode when structured output is not re-validated across a model swap (schema integrity → 0%)
- **Content angle**: "JSON Mode, Function Calling, and Structured Outputs get used interchangeably and they shouldn't be. A practitioner's decision guide to the three structured-output mechanisms — what each actually guarantees, how schema enforcement differs, and why your fallback model can quietly hand you 'valid' output that breaks the next stage."
- **Key data points**: 3 structured-output mechanisms compared (JSON Mode / Function Calling / Structured Outputs), schema-enforcement differences, fallback schema-integrity failure
- **Timeliness**: Published 06-18; foundational/evergreen rather than breaking
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

<!-- ───────── Database topic brainstorm (manual, 2026-06-26) — distinct from feed-sourced ideas above ───────── -->

## Database Topic Ideas (manual brainstorm — 2026-06-26)

> A focused, topical batch on databases. IDs are prefixed `DB-` to avoid colliding with the ranked feed queue. These are seed ideas — most need a research pass (`@trend-researcher` / `@reference-discovery`) to harden the data points before pipeline.
> **Dedup note:** complements existing queued ideas [6] (pgvector vs pgvectorscale vs pgai), [14] (10 RAG mistakes), and [20] (PDF parsing for RAG). Those stay vector/RAG-scoped; this batch covers the broader database surface.

### [DB-1] Postgres Ate the Database Market — The "Just Use Postgres" Thesis and Where It Breaks
- **Score**: 22/25 (R:5 D:4 T:5 G:4 V:4)
- **Subject areas**: Databases, Architecture, Solution Architecture
- **Content angle**: "'Just use Postgres' went from a meme to a default. With extensions covering vectors (pgvector), time-series (Timescale), queues (pgmq), full-text, and JSON, Postgres now absorbs workloads that used to need 5 separate systems. Here's the consolidation case — and the four places where reaching for a specialist database is still the right call (extreme write throughput, planet-scale sharding, sub-ms KV, true OLAP at petabyte scale)."
- **Key data points**: _(needs research — collect: Postgres extension ecosystem count, DB-Engines ranking trend, Postgres 18/19 feature deltas, concrete throughput ceilings vs Cassandra/ClickHouse/DynamoDB)_
- **Timeliness**: Postgres 19 Beta 1 already noted in this queue (graph queries, faster inserts, pg_plan_advice); the "one database" consolidation narrative is peaking
- **Scope hypothesis**: `single-post candidate` — strong opinion/architecture thesis
- **Status**: `selected` — picked 2026-06-26; pipeline run started (`content/pipeline-config.md` Topic = DB-1). Previous run (Loop Engineering) archived to `archive/run-20260626-194922/`.

### [DB-2] Vector Database vs Postgres+pgvector — A Build-vs-Buy Decision Framework for AI Retrieval
- **Score**: 21/25 (R:5 D:4 T:5 G:4 V:3)
- **Subject areas**: Databases, AI & LLM, Architecture
- **Note**: ⚠️ Adjacent to [6] (which compares the three pg extensions). This idea is the **dedicated vector DB (Pinecone/Weaviate/Qdrant/Milvus) vs pg** decision, not an intra-Postgres comparison.
- **Content angle**: "Every RAG project hits the same fork: bolt vectors onto the Postgres you already run, or adopt a purpose-built vector database. A practitioner's decision framework across the dimensions that actually decide it — recall@k at your scale, index build time, filtered search, hybrid (keyword+vector) quality, operational surface area, and cost per million vectors — with the crossover point where pgvector stops being enough."
- **Key data points**: _(needs research — collect: HNSW vs IVFFlat vs DiskANN tradeoffs, pgvector recall/latency at 1M/10M/100M vectors, dedicated-DB filtered-search benchmarks, $/M vectors cloud pricing)_
- **Timeliness**: RAG is the #1 production-LLM workload; this is the most-asked database question in AI teams right now
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [DB-3] Text-to-SQL in Production — Why the Demo Works and the Deployment Doesn't (Semantic Layers & Guardrails)
- **Score**: 21/25 (R:5 D:4 T:5 G:4 V:3)
- **Subject areas**: Databases, AI & LLM, Developer Productivity
- **Content angle**: "Text-to-SQL demos nail 'top 10 customers by revenue' and then fall apart on a real warehouse with 400 tables, ambiguous column names, and business logic that lives in nobody's schema. The production fix isn't a bigger model — it's a semantic layer, retrieval over schema + example queries, read-only execution sandboxes, result validation, and a human gate on anything that writes. Here's the architecture that takes text-to-SQL from 60% to shippable."
- **Key data points**: _(needs research — collect: Spider/BIRD benchmark accuracy vs real-schema accuracy gap, semantic-layer tools, schema-RAG patterns, cost of a wrong-but-confident query)_
- **Timeliness**: Every BI/analytics vendor is shipping NL-query; the accuracy-in-the-wild gap is under-covered
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [DB-4] Database Branching & Ephemeral Environments — Copy-on-Write Postgres for CI, Previews, and Agents
- **Score**: 20/25 (R:4 D:4 T:4 G:5 V:3)
- **Subject areas**: Databases, DevOps & Platform Engineering, Developer Productivity
- **Content angle**: "Branching your code is instant; branching your database has always meant a slow restore or a shared staging DB everyone steps on. Copy-on-write storage (Neon-style) flips that — a full production-shaped database in seconds, one per PR, one per CI run, one per AI agent. Here's how branchable databases change preview environments, migration testing, and how you give an autonomous agent a safe place to actually run its SQL."
- **Key data points**: _(needs research — collect: CoW branch creation time vs pg_dump/restore, storage cost model, per-PR/per-CI patterns, agent-sandbox angle tie-in to this repo's eval work)_
- **Timeliness**: Branchable Postgres is mainstreaming; the agent-sandbox angle connects to the queue's eval/containment themes
- **Scope hypothesis**: `single-post candidate` — first-party hook: an agent eval harness needs disposable databases
- **Status**: `queued`

### [DB-5] The Lakehouse Table-Format Wars — Apache Iceberg, Delta, and the Open Catalog Endgame
- **Score**: 19/25 (R:4 D:4 T:4 G:4 V:3)
- **Subject areas**: Databases, Cloud & Infrastructure, Architecture
- **Content angle**: "Object storage + an open table format quietly became the default analytics substrate. Iceberg won the format debate, every major vendor now reads it, and the real fight moved to the catalog (who owns the metadata). A practitioner's map of the lakehouse stack — table formats vs catalogs vs engines — and how to avoid locking your data into the one layer that's supposed to be open."
- **Key data points**: _(needs research — collect: Iceberg vs Delta vs Hudi adoption, REST catalog spec, vendor Iceberg support matrix, cost vs cloud-DW comparison)_
- **Timeliness**: Catalog interoperability and Iceberg-everywhere announcements are landing across vendors
- **Scope hypothesis**: `possible series` — formats vs catalogs vs engines are natural parts
- **Status**: `queued`

### [DB-6] The SQLite Renaissance — When the Embedded Database Is the Right Server-Side Choice
- **Score**: 18/25 (R:4 D:3 T:4 G:5 V:2)
- **Subject areas**: Databases, Architecture, Developer Productivity
- **Content angle**: "SQLite stopped being 'the database for tests.' Edge replicas, single-file app formats, per-tenant databases, and read-heavy services are running it in production — and the operational simplicity (no server, no connection pool, one file to back up) is the feature. Here's where server-side SQLite genuinely wins, where it absolutely doesn't (write concurrency, multi-writer), and the patterns (litestream/replicas/per-tenant) that make it safe."
- **Key data points**: _(needs research — collect: WAL concurrency limits, edge-replica latency numbers, per-tenant DB patterns, durability/replication tooling)_
- **Timeliness**: Edge + local-first momentum keeps SQLite-on-the-server in the conversation
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [DB-7] Zero-Downtime Schema Migrations at Scale — Online DDL, Expand/Contract, and Backfills That Don't Page You
- **Score**: 18/25 (R:4 D:4 T:3 G:4 V:3)
- **Subject areas**: Databases, DevOps & Platform Engineering, Architecture
- **Content angle**: "A migration that locks a hot table for 30 seconds is an outage. The discipline that prevents it — expand/contract, lock-free index builds, batched backfills, dual-writes, and feature-flagged cutovers — is well understood and still routinely skipped. A practitioner's runbook for evolving a schema under live traffic, including the Postgres-specific lock traps (and why `ALTER TABLE ... ADD COLUMN ... DEFAULT` finally stopped being scary)."
- **Key data points**: _(needs research — collect: lock levels per DDL operation, online-schema-change tooling, backfill batch-size math, real incident examples)_
- **Timeliness**: Evergreen reliability topic; pairs with the queue's broader reliability/agent-safety themes
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

### [DB-8] AI-Assisted Database Operations — Index Advisors, Slow-Query Triage, and the Self-Tuning Database
- **Score**: 18/25 (R:4 D:3 T:4 G:4 V:3)
- **Subject areas**: Databases, AI & LLM, DevOps & Platform Engineering
- **Note**: ⚠️ Postgres 19's `pg_plan_advice` (already cited in this queue) is a concrete hook for this idea.
- **Content angle**: "Database tuning has always been expert-and-intuition work. Now plan-advice features, LLM-driven slow-query explainers, and automated index recommendations are moving it toward assisted (and partly autonomous) operations. Here's what's real today — where AI genuinely speeds up query diagnosis and index selection — and where 'self-tuning' is still marketing, plus the guardrails before you let anything touch production indexes."
- **Key data points**: _(needs research — collect: pg_plan_advice capabilities, index-advisor accuracy, LLM EXPLAIN-analysis patterns, autonomous-tuning risk cases)_
- **Timeliness**: Postgres 19 plan-advice + the broader "agents reach into infra" theme (queue idea [21]) make this current
- **Scope hypothesis**: `single-post candidate`
- **Status**: `queued`

<!-- ───────── Fresh-article reinforcements (2026-06-15) — strengthen existing ideas, not new ───────── -->

### Reinforcements to Existing Ideas (2026-06-15 feeds)

> New articles since 06-09 that strengthen ideas already in the queue. No new idea created — use these as added sources when the idea goes to pipeline.

- **Idea [2] WebMCP & Browser AI Agents** — reinforced by [WebMCP Standard Proposal for Agentic Web Actuation Now Available in Chrome (Origin Trials)](https://www.infoq.com/news/2026/06/webmcp-web-agent-standard-chrome/) (InfoQ, 06-12). First-party confirmation the Chrome origin trial is live — upgrades the timeliness claim from "entering" to "available now."
- **Idea [6] pgvector Ecosystem** — reinforced by [Postgres 19 Beta 1 is here](https://postgresweekly.com/issues/652) (Postgres Weekly, issue #652, final ~late Sept/Oct). Postgres 19 adds **graph queries, faster inserts, pg_plan_advice, parallel-worker autovacuuming, online checksum toggling** — context for "where does the core engine go while the vector extensions mature."
- **Idea [10] Containing the Agent (Sandboxing & Prompt-Injection)** — reinforced by [Run Untrusted AI Agent Code Safely with Azure Container Apps Sandboxes](https://www.infoq.com/news/2026/06/untrusted-ai-agents-sandboxes/) (InfoQ, 06-12): public preview of `Microsoft.App/SandboxGroups` — hardware-isolated, **OCI image starts in <1s, scales to thousands, zero idle cost**. A concrete managed-service primitive for the "sandbox the runtime" layer.
- **Idea [11] From Prompts to Harness Engineering** — reinforced by four fresh sources: [How we made GitHub Copilot CLI more selective about delegation](https://github.blog/ai-and-ml/how-we-made-github-copilot-cli-more-selective-about-delegation/) ("delegation isn't free" — data-driven subagent tuning), [Give GitHub Copilot CLI real code intelligence with language servers](https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers/) (LSP Setup skill), [A Harness for Every Task: Putting a Team of Claudes on One Job](https://towardsdatascience.com/a-harness-for-every-task-putting-a-team-of-claudes-on-one-job/), and [Angular's Official Agent Skills](https://www.infoq.com/news/2026/06/angular-agent-skills/) (Anthropic's open Skills format, load-on-demand). The "harness engineering" thesis is now corroborated across GitHub, Google/Angular, and Anthropic.
- **Idea [13] Production-Grade Agentic Inference** — reinforced by [GPU Time-Slicing for Concurrent LLM Agents on Kubernetes](https://towardsdatascience.com/gpu-time-slicing-for-concurrent-llm-agents-on-kubernetes/) (this is literally **Part 2** of the same series; p99 jumps 3.68→6.10 ms ≈1.66×, jitter 1.02→1.70 when two agents share a time-sliced GPU) and [When GPU Utilization Lies](https://towardsdatascience.com/when-gpu-utilization-lies-the-hidden-systems-problem-slowing-modern-ai/) (79/82/84% GPU utilization masked a RAID-rebuild storage bottleneck starving inference). Adds an observability angle to the inference-cost story.
- **Idea [14] 10 RAG Mistakes / Four Generations of Retrieval** — reinforced by the new [20] Document Intelligence cluster and [Larger Context Windows Don't Fix RAG](https://towardsdatascience.com/larger-context-windows-dont-fix-rag-so-i-built-a-system-that-does/) (7 query types × 5 context sizes × 100,000 rows; route computation queries away from RAG).

### Reinforcements to Existing Ideas (2026-06-19 feeds)

> New articles since 06-15 that strengthen ideas already in the queue. No new idea created — use these as added sources when the idea goes to pipeline.

- **Idea [9] The AI Coding Cost Reckoning / FinOps** — reinforced by [Drilling Into AI's Financial Sustainability](https://towardsdatascience.com/drilling-into-ais-financial-sustainability/) (TDS, 06-16): "tokenmaxxing," internal token-usage leaderboards at Amazon, shocking quarterly AI token expense at Uber and others, and the pivot away from "use AI more" mandates because the spend is unsustainable *and* the business outcomes didn't materialize.
- **Idea [10] Containing the Agent (Sandboxing & Prompt-Injection)** — reinforced by [Windows Platform Security and the Race to Secure AI Agents](https://www.infoq.com/news/2026/06/windows-security-agents/) (InfoQ, 06-19): the **MXC SDK** isolation spectrum (process → session → planned micro-VM → Linux container) is another concrete OS-native containment primitive alongside the ACA Sandboxes cited on 06-15. (Identity/continuous-authz angle split out into new idea [24].)
- **Idea [11] From Prompts to Harness Engineering** — reinforced by four fresh GitHub/InfoQ sources: [Getting more from each token: How Copilot improves context handling and model routing](https://github.blog/ai-and-ml/github-copilot/getting-more-from-each-token-how-copilot-improves-context-handling-and-model-routing/) (prompt caching + **deferred tools** + Auto model routing — the harness, not the model, doing the work), [GitHub Copilot CLI for Beginners: common slash commands](https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-overview-of-common-slash-commands/), [What are git worktrees, and why should I use them?](https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/) (parallel agent workspaces), and [CircleCI Introduces Chunk Sidecars](https://www.infoq.com/news/2026/06/circleci-chunk-sidecars/) (CI-style validation moved *into the agent's inner loop* so it self-corrects before commit).
- **Idea [12] Local & On-Device Agents** — reinforced by [Run a Local LLM with OpenClaw on Your Mac Mini](https://towardsdatascience.com/run-a-local-llm-with-openclaw-on-your-mac-mini/) (TDS, 06-16: free local agent on an M2 / 24GB Mac Mini, "almost indistinguishable" for email/calendar/IoT/research with a cloud fallback for heavy coding) and [GLM-5.2 is probably the most powerful text-only open weights LLM](https://simonwillison.net/2026/Jun/17/glm-52/) (Simon, 06-17: **753B / 40-active MoE, MIT license, 1M-token context**, leads the Artificial Analysis open-weights Intelligence Index at 51, #2 on Code Arena WebDev behind Fable 5 — but token-hungry at **43k output tokens/task**).
- **Idea [15] The Open-Source Trust Crisis in the Agent Era** — reinforced by [How pull request limits are cutting down the noise](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/) (GitHub, 06-18): persistent, configurable per-repo PR caps for non-write contributors, **Copilot/AI-agent PRs count toward the limit** — a direct mechanism for the "a polished change and a rough draft look the same in the queue" problem the idea is built on.
- **Idea [19] When Your Model Gets Pulled Overnight (Vendor Risk / Model Abstraction)** — reinforced by [LLM Fallbacks Break Agent Pipelines](https://towardsdatascience.com/llm-fallbacks-break-agent-pipelines-i-built-the-missing-recovery-layer/) (TDS, 06-16: the *mechanics* of safe model swapping — 100% completion / 0% schema integrity unless you rebuild the payload and save progress before the swap), [The Fable 5 Export Controls Harm US Cyber Defense](https://simonwillison.net/2026/Jun/16/fable-5-export-controls/) (Simon, 06-16: follow-on to the suspension saga), and [The Batch issue 358 — "Testing Mythos and Fable, Moving Beyond SWE-bench"](https://www.deeplearning.ai/the-batch/issue-358) (DeepLearning.AI, 06-19). *(Note: this article is also the third source for new idea [26].)*
- **Idea [20] Enterprise Document Intelligence (PDF Parsing for RAG)** — reinforced by the TDS "question parsing" trilogy ([RAG Questions Need Parsing Too](https://towardsdatascience.com/question-parsing-in-rag-structure-before-you-search/) 06-16, [What the Question Parser Extracts](https://towardsdatascience.com/what-the-question-parser-extracts-from-a-user-string-keywords-scope-shape-decomposition-clarification/) 06-17, [Dispatching the Parsed RAG Question](https://towardsdatascience.com/dispatching-the-parsed-rag-question-chunk-strategy-model-tier-activations-audit/) 06-18) plus [Parse Scanned PDFs for RAG with EasyOCR](https://towardsdatascience.com/parse-scanned-pdfs-for-rag-with-easyocr-free-ocr-gives-you-words-not-a-document/) (06-19) and [GPU-Resident Top-K for Agentic RAG](https://towardsdatascience.com/gpu-resident-top-k-for-agentic-rag-i-built-a-cuda-kernel-so-my-retrieval-step-would-stop-bouncing-off-the-gpu/) (06-19). The series now spans **parse-the-document → parse-the-question → dispatch → retrieve**, extending the ingestion thesis upstream into query understanding (e.g., "name" on a CV resolves via doc profile, not literal grep).

_(Run `@feed-curator`, `@apple-notes-curator`, or `@reading-list-curator` to refresh this queue from your configured sources.)_

---

## Archive (Previously Processed)

> Ideas that were selected for the pipeline, published, or dismissed. Kept for deduplication — the feed curator checks this section to avoid re-suggesting old ideas.

<!-- Archived ideas are moved here with their final status:
- `selected` — Picked for pipeline, may be in-progress
- `in-pipeline` — Currently being processed by the content pipeline
- `published` — Content was created and published
- `dismissed` — Rejected, not interesting enough
-->
