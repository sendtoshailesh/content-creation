# Content Idea Queue

> **Curated content ideas** extracted from configured feed sources. Run `@feed-curator` to discover fresh ideas. Pick an idea and run `@content-pipeline` or use `/select-idea` to auto-populate the pipeline config.

Last curated: 2026-06-09 (All sources — Feeds: 98 articles from 6 live sources + Apple Notes: 170 notes + Chrome Reading List: 0 items. 10 new ideas queued, total now 18)

> **Source health (2026-06-09 run):** GitHub Blog ✅ 5 · DeepLearning.AI Batch ✅ 20 · Towards Data Science ✅ 20 · Simon Willison ✅ 30 · TLDR AI ✅ 2 · InfoQ ✅ 15 · PostgreSQL Weekly ⚠️ no parseable articles (nav-only page) · The Pragmatic Engineer ⚠️ empty (paywall/login) · Chrome Reading List ⚠️ 0 items (Chrome was running — data may be stale).

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
