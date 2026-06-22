# Reference Brief — AI Agent Evals: Why SWE-bench Isn't Enough Before Production

Generated: 2025-07-17
Topic: AI Agent Evals: Why SWE-bench Isn't Enough Before Production
Primary source: `content/agent-eval-knowledge-extract.md` (34K chars, first-party practitioner knowledge)

## Primary Source Summary

The primary source is first-party practitioner material from building and running Waza-based evals for GitHub Copilot's [Git-Ape](https://github.com/Azure/git-ape) project. It covers 14 skills, 8 agents, and 38 task patterns; three grader types (`text`, `tool_constraint`, `prompt`); the full PR-triggered eval flow; real costs (~15-25 minutes, ~200K-400K tokens, ~$3-8 per run); and several operational lessons that do not appear in the external references.

Most importantly, it introduces four original framing ideas that should anchor the blog:
- **The Sourdough Test**: one identical off-topic prompt across agents to catch persona-boundary regressions.
- **Fabrication Without Action**: the agent says it did the work but never called tools.
- **Safety Gate vs. Off-Topic**: refusing a valid deployment without confirmation is a different contract from refusing sourdough.
- **Binary grading as a feature**: pass/fail is more actionable in CI than subjective 1-5 scales.

It also contributes a concrete execution gotcha that external sources barely discuss: **tool name translation** between production and eval environments (`execute` -> `bash`, `read` -> `view`, `search` -> `grep`, etc.).

## External Source Summaries

### [Working with evals | OpenAI API](https://platform.openai.com/docs/guides/evals)
- **Key data points**: Official OpenAI flow is **3 steps**: describe the task, run the eval on test inputs, analyze results and iterate. Evals require a `data_source_config` plus `testing_criteria`, with examples using `string_check` graders.
- **Unique angle**: Strongest official product framing for evals as a repeatable API object rather than an ad hoc notebook habit.
- **Relevant quotes**: "Writing evals to understand how your LLM applications are performing against your expectations, especially when upgrading or trying new models, is an essential component to building reliable applications." `[VOLATILE]` "Evals will become read-only for existing users on October 31, 2026, and the platform is scheduled to shut down on November 30, 2026."
- **Credibility**: Official OpenAI documentation; high authority for API shape and platform roadmap.
- **Date**: No page date surfaced in the curl excerpt; deprecation notice references a 2026 transition timeline.

### [OpenAI Evals GitHub repository](https://github.com/openai/evals)
- **Key data points**: Repo positions Evals as both a **framework** and an **open-source registry**. It requires **Python 3.9+** and uses **Git LFS** for registry data. README points users to YAML/JSON-first eval authoring and notes that OpenAI was "currently not accepting evals with custom code."
- **Unique angle**: Useful contrast with the API guide: the repo emphasizes community contribution, templates, local runs, and private evals using your own data.
- **Relevant quotes**: "Evals provide a framework for evaluating large language models (LLMs) or systems built using LLMs." / "Without evals, it can be very difficult and time intensive to understand how different model versions might affect your use case."
- **Credibility**: Official OpenAI open-source repo; high authority, though the README reflects an older/open-source workflow while the product docs now emphasize the API/dashboard path.
- **Date**: No publication date surfaced in the curl excerpt.

### [Building Effective AI Agents — Anthropic](https://www.anthropic.com/research/building-effective-agents)
- **Key data points**: Published **Dec 19, 2024**. Distinguishes **workflows** from **agents**. Recommends five reusable patterns: **prompt chaining**, **routing**, **parallelization**, **orchestrator-workers**, and **evaluator-optimizer**.
- **Unique angle**: Best source for the "start simpler than you think" argument. Anthropic explicitly says many successful teams use composable patterns rather than heavy frameworks.
- **Relevant quotes**: "The most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns." / "Agentic systems often trade latency and cost for better task performance."
- **Credibility**: High. First-party engineering guidance from a model provider with practical implementation examples.
- **Date**: 2024-12-19.

### [SWE-bench Leaderboards](https://www.swebench.com/)
- **Key data points**: The site describes **SWE-bench Verified** as a **human-filtered subset of 500 instances** created with OpenAI. It also documents a **bash-only** comparison mode using **mini-SWE-agent** in a minimal bash environment with a simple ReAct loop.
- **Unique angle**: Important benchmark-context source because it clarifies what SWE-bench Verified actually is: a capability benchmark with a constrained execution setup, not a production-behavior test.
- **Relevant quotes**: "A human-validated subset of 500 SWE-bench instances for reliable evaluation of coding agents and language models." / "No tools, no special scaffold structure; just a simple ReAct agent loop."
- **Credibility**: High for benchmark definition and leaderboard framing. Exact ranking values appear to be dynamically rendered and were not fully extractable from the first 50K curl snapshot.
- **Date**: No publication date surfaced in the curl excerpt.

### [Coding Agent Benchmarks 2026 — Presenc AI](https://presenc.ai/research/coding-agent-benchmarks-2026)
- **Key data points**: Claims SWE-Bench Verified rose from **13% (early 2024)** to **78% (May 2026)**. Reports top-agent ranges of **74-78%** on SWE-Bench Verified, **52-58%** on TerminalBench, and real-world PR acceptance rates of only **35-50%**. Also reports median time-to-PR of **8-25 minutes** and test-pass-before-review rates of **63-71%**. `[VOLATILE]` Cost/task estimates: Claude Code **$1.50-3.00**, Cursor Agent **$0.40-0.90**, Devin **$3.00-6.00**, Aider **$0.30-0.70**.
- **Unique angle**: Strongest explicit benchmark-to-production gap framing for coding agents.
- **Relevant quotes**: "Real-world pull-request pass rates ... are estimated at 35-50 percent for top agents, materially below SWE-Bench because real codebases have implicit conventions and reviewer expectations benchmarks miss."
- **Credibility**: Mixed. Detailed and numerically rich, but it is a vendor research page aggregating public reports plus Presenc's own instrumentation across **25+ enterprise coding-agent rollouts**.
- **Date**: 2026-05-07.

### [AI Benchmarks in 2026: The Complete Guide — explainx.ai](https://explainx.ai/blog/ai-benchmarks-complete-guide-2026)
- **Key data points**: Says frontier models cluster at **Arena Elo 1,424-1,503**. Claims MMLU/HellaSwag are functionally saturated above **88%** and **95%**. Gives a claimed **37% gap** between lab benchmark scores and real-world deployment performance, with **50x cost variation** for similar accuracy.
- **Unique angle**: Best source for the "benchmark saturation" argument and for explaining why older academic leaderboards are becoming less decision-useful.
- **Relevant quotes**: "The most significant development is benchmark saturation." / "These differences tell us little about which model performs better in production."
- **Credibility**: Secondary synthesis rather than primary benchmark research. Good for framing, weaker than primary benchmark papers for hard claims.
- **Date**: 2026-05-02.

### [Awesome Agent Failures](https://github.com/vectara/awesome-agent-failures)
- **Key data points**: Maintains a concrete failure taxonomy including **tool hallucination**, **response hallucination**, **goal misinterpretation**, **plan generation failures**, **incorrect tool use**, **verification & termination failures**, and **prompt injection**. The curated incident list includes concrete numbers such as **$812** Air Canada damages, **10,000 customer inquiries** deleted in one email-tool example, **~40 hallucinations** in one Sullivan & Cromwell filing, **~72% of 27 citations** fabricated/broken in the EY report example, and a **$47,000** multi-agent loop lasting **264 hours (11 days)**.
- **Unique angle**: Best compendium of vivid production failure stories across legal, customer-service, autonomous-agent, and security incidents.
- **Relevant quotes**: "AI agents fail in predictable ways." / "$47,000 LangChain A2A Multi-Agent Loop ... observability without enforcement."
- **Credibility**: Useful curated survey, but community-maintained rather than peer-reviewed. Individual examples should be traced to primary case links before publication.
- **Date**: No single publication date; living repository.

### [Why AI Agent Prototypes Fail in Production — Softcery](https://softcery.com/lab/why-ai-agent-prototypes-fail-in-production-and-how-to-fix-it)
- **Key data points**: Cites Gartner's **June 2025** forecast that **over 40%** of agentic AI projects will be canceled by end of **2027**; claims only **~130** of thousands of vendors are "real" agentic vendors. Also cites hallucination ranges of **~3%** for Claude Sonnet 4.6 versus **15-25%** for many production models on harder real-world benchmarks.
- **Unique angle**: Strong architecture anti-pattern framing: wrong problem selection, PoC architecture promoted to prod, brittle integrations, missing tests, poor observability, and all-in rollouts.
- **Relevant quotes**: "Most production failures trace back to six common patterns." / "A PoC tests business need, not technical feasibility for production."
- **Credibility**: Vendor/lab content with useful practitioner heuristics and citations, but still a consultancy-marketing source.
- **Date**: Page metadata shows 2025-10-08; article body says "Last updated on April 24, 2026." Treat as 2026-updated content.

### [5 AI Agent Failures in Production — DEV Community](https://dev.to/thedailyagent/5-ai-agent-failures-in-production-and-how-to-fix-them-2nm0)
- **Key data points**: Opens with a concrete failure vignette: **47 tool calls instead of 3** and a **$200** API-bill spike. Organizes production failure into five patterns: **infinite helpfulness loop**, **tool schema mismatch**, **retrieval pollution**, **overconfident wrong answer**, and **prompt regression**. Recommends eval sets of **30-50** golden cases.
- **Unique angle**: Best "minimal observability stack" piece. Very practical on what to log, where to set step budgets, and how to catch loops before they become billing surprises.
- **Relevant quotes**: "Agents fail quietly, producing plausible-looking wrong behavior five steps downstream from the actual cause." / "A healthy agent run should have zero tool errors."
- **Credibility**: Practitioner blog post; useful operational heuristics, but anecdotal and not independently audited.
- **Date**: Visible in page content as "Posted on Mar 7"; year was not surfaced in the first 50K curl excerpt.

### [Agent Regression Testing Actually Catches Silent Failures This Way — Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures)
- **Key data points**: Claims **78%** of agent failures are not crashes or timeouts; cites observations across **12 million production logs**. Recommends an initial suite of **20-50 scenarios**, about **one day** to build the first suite, and roughly **one sprint** to wire it into CI/CD.
- **Unique angle**: Strongest closed-loop framing: offline versioned regression suite plus production monitoring that continuously feeds new incidents back into the suite.
- **Relevant quotes**: "Passing all tests and not regressing are different things for agents." / "Offline regression testing and production monitoring aren't the same thing, and they're not alternatives."
- **Credibility**: Vendor blog. Valuable for operational framing, but several headline numbers are themselves attributed to other linked sources and should be re-verified if used.
- **Date**: 2026-05-28 (page metadata) / article body says May 27, 2026.

### [Regression Testing for AI Agents: Catching Silent Breakage Before Users Do — CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage)
- **Key data points**: Provides one of the strongest concrete silent-regression examples: a prompt edit reduced token usage by **18%**, improved latency by **200ms**, but dropped booking conversion by **11%** over **5 days** because the confirmation step disappeared. Recommends gate thresholds such as **no eval drop >2%**, **no tag drop >5%**, and latency p95 staying within **+20%** of baseline.
- **Unique angle**: Best source for the idea that regression in agent systems is a **statistical claim**, not a deterministic snapshot. Also useful for pairwise A-vs-B judging and baseline/candidate experiment comparisons.
- **Relevant quotes**: "A regression in agent-land is a statistical claim, not a binary one." / "The metric you forgot to test moves silently while the metrics you did test all look fine."
- **Credibility**: Vendor blog with strong implementation detail and concrete examples, but still not neutral benchmark research.
- **Date**: 2026-05-06.

### [About agent skills — configured URL in pipeline](https://docs.github.com/en/copilot/concepts/agents/agent-skills)
- **Key data points**: The configured URL returned **404** during curl fetch, which is itself useful: the pipeline reference appears stale. A current canonical GitHub Docs page exists at `/en/copilot/concepts/agents/about-agent-skills`, and it states that project skills live in **`.github/skills`, `.claude/skills`, or `.agents/skills`**, while personal skills live in **`~/.copilot/skills` or `~/.agents/skills`**.
- **Unique angle**: Useful context for how Copilot packages reusable behavior as skill folders of instructions, scripts, and resources.
- **Relevant quotes**: From the current canonical docs page: "Skills allow Copilot to perform specialized tasks." / "Agent skills are folders of instructions, scripts, and resources that Copilot can load when relevant."
- **Credibility**: Official GitHub documentation, but the exact URL in the pipeline is stale and should be updated before publishing.
- **Date**: Listed URL unavailable; current canonical page has no visible publication date in the fetched excerpt.

### [Custom agents configuration — GitHub Docs](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- **Key data points**: Documents frontmatter properties including `name`, `description`, `target`, `tools`, `model`, `disable-model-invocation`, `user-invocable`, `mcp-servers`, and `metadata`. It also documents tool aliases and mappings such as `execute` -> shell (`bash`/`powershell`) and `read` -> `view`.
- **Unique angle**: Very relevant for this topic because it validates that tool naming and agent frontmatter are part of the behavioral contract surface.
- **Relevant quotes**: `[VOLATILE][CAVEAT: "public preview"]` "Custom agents are in public preview for JetBrains IDEs, Eclipse, and Xcode, and subject to change." / "The prompt can be a maximum of 30,000 characters."
- **Credibility**: Official GitHub docs; high authority for configuration behavior.
- **Date**: No publication date surfaced in the fetched excerpt.

### [How to maximize GitHub Copilot's agentic capabilities — GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)
- **Key data points**: Frames agent mode around multi-file, architecture-aware work: decomposition, migrations, refactors, and test modernization. The example workflow covers decomposition, tagging subsystem design, backward-compatible schema migration, validation-layer refactor, and contract/integration/domain tests.
- **Unique angle**: Shows how GitHub positions agentic capability as a collaborator for system design and multi-step coordination, not just code generation.
- **Relevant quotes**: "Copilot's agentic capabilities don't replace your judgment in these situations—they amplify it." / "This transforms Copilot from an autocomplete tool into a design reviewer."
- **Credibility**: Official GitHub Blog; strong for GitHub's product framing and practitioner workflow examples.
- **Date**: 2026-02-02.

### [AI Agent Monitoring Best Practices, Tools and Metrics — UptimeRobot](https://uptimerobot.com/knowledge-hub/monitoring/ai-agent-monitoring-best-practices-tools-and-metrics/)
- **Key data points**: Could not be fetched successfully with `curl -sL --max-time 15 ... | head -c 50000`; follow-up fetch attempts also timed out.
- **Unique angle**: Intended as monitoring/metrics context, but no verified claims were extracted.
- **Relevant quotes**: None — fetch failed.
- **Credibility**: Not assessed because content could not be retrieved.
- **Date**: Unavailable.

### [Agent Failure Diagnosis in Production — AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith)
- **Key data points**: Claims **40%** of multi-agent pilots fail within **6 months** of production deployment. Cites a **76.3% -> 50.5%** drop from short to long-horizon pass@1, a **14-failure-mode** MAST taxonomy built from **1,600+ annotated traces**, and breakdowns such as **11.8%** task derailment and **8.2%** information withholding. Gives a compounding-error example: a **10-step** pipeline at **97%** per-step accuracy yields only **72%** end-to-end accuracy; at **99%** per-step it reaches **90%**. Also claims teams spend roughly **40%** of sprint time investigating failures, and that **89%** of orgs have observability but only **62%** can inspect step-level behavior.
- **Unique angle**: Best market/observability framing in this set. It is especially useful for the case that standard APM misses semantic drift and silent step-level failures.
- **Relevant quotes**: "Welcome to the silent failure problem — the defining operational challenge of production AI agents in 2026." / "Traditional observability tools check HTTP status codes and return 200 OK while the agent has already sent the wrong context to the wrong tool three steps ago."
- **Credibility**: Vendor/market-analysis blog, numerically rich and well framed, but many figures are synthesized from external studies rather than first-party audited market data.
- **Date**: URL path indicates 2026-04-06; no explicit published date surfaced in the first 50K curl excerpt.

## Cross-Source Analysis

### Consensus Points
- **Benchmarks are necessary but insufficient**. [OpenAI's evals guide](https://platform.openai.com/docs/guides/evals), [Anthropic's agent guide](https://www.anthropic.com/research/building-effective-agents), [Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026), [explainx.ai](https://explainx.ai/blog/ai-benchmarks-complete-guide-2026), [Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures), and [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage) all converge on the idea that you need explicit evaluation because capability and production quality drift apart.
- **Silent failures dominate agent operations**. [DEV Community](https://dev.to/thedailyagent/5-ai-agent-failures-in-production-and-how-to-fix-them-2nm0), [Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures), [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage), and [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith) all emphasize that the agent often returns *something* coherent while the actual task has failed.
- **Simple, observable systems beat clever opaque ones**. [Anthropic](https://www.anthropic.com/research/building-effective-agents), [Softcery](https://softcery.com/lab/why-ai-agent-prototypes-fail-in-production-and-how-to-fix-it), [DEV Community](https://dev.to/thedailyagent/5-ai-agent-failures-in-production-and-how-to-fix-them-2nm0), and the [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/) all push decomposition, explicit contracts, and stepwise review.
- **Tool use is a first-class eval surface**. [Anthropic](https://www.anthropic.com/research/building-effective-agents) discusses tools and ground truth, [GitHub custom agents docs](https://docs.github.com/en/copilot/reference/custom-agents-configuration) document tool alias mappings, and failure catalogs like [Awesome Agent Failures](https://github.com/vectara/awesome-agent-failures) and [DEV Community](https://dev.to/thedailyagent/5-ai-agent-failures-in-production-and-how-to-fix-them-2nm0) repeatedly show incorrect tool use as a core failure mode.

### Contradictions
- **Capability leaderboards vs. production acceptance**: [SWE-bench](https://www.swebench.com/) and [Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026) celebrate high coding-agent scores, while [Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026), [Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures), [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage), and [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith) argue those numbers overstate real-world reliability.
- **Blocking gates vs. advisory evals**: vendor regression-testing sources like [Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures) and [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage) push hard release gates, whereas the primary first-party knowledge argues for **advisory** agent evals because of non-determinism, cost, and bootstrapping friction.
- **Binary vs. statistical framing**: [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage) frames regressions statistically across datasets, while the primary source argues that **binary pass/fail** is more actionable at the single-task CI level. These are not mutually exclusive, but they operate at different layers and should be reconciled explicitly in the blog.
- **Platform stability**: [OpenAI's evals guide](https://platform.openai.com/docs/guides/evals) says the Evals platform is being deprecated, while the [OpenAI/evals repo](https://github.com/openai/evals) still presents Evals as an active framework/registry. That split is useful context for "framework vs. product" drift.

### Data Points for Content
- [SWE-bench Verified](https://www.swebench.com/) is a **500-instance human-validated subset** — useful to define the benchmark before critiquing it.
- [Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026): **74-78%** SWE-Bench Verified vs **35-50%** real-world PR acceptance; **52-58%** TerminalBench.
- [explainx.ai](https://explainx.ai/blog/ai-benchmarks-complete-guide-2026): **37% lab-to-production gap** and **50x cost variation** for similar accuracy.
- [Softcery](https://softcery.com/lab/why-ai-agent-prototypes-fail-in-production-and-how-to-fix-it): Gartner forecast of **40%** project cancellations by **2027**.
- [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage): a prompt tweak cut tokens **18%**, improved latency **200ms**, but hurt conversion **11%** over **5 days**.
- [Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures): **78%** of failures are behavioral rather than clean crashes/timeouts.
- [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith): **14** failure modes in the MAST taxonomy; **11.8%** derailment; **8.2%** information withholding; **97%** per-step accuracy still yields only **72%** end-to-end over **10 steps**.
- [Awesome Agent Failures](https://github.com/vectara/awesome-agent-failures): concrete incident numbers such as **$47K** loop cost, **264 hours** loop duration, **6.3M lost orders** in one Amazon Q incident, and **CVSS 9.4 / 9.9** style security severity examples.
- `[VOLATILE]` [OpenAI docs](https://platform.openai.com/docs/guides/evals): read-only on **2026-10-31** and shutdown on **2026-11-30**.
- `[VOLATILE][CAVEAT: "public preview"]` [GitHub custom agents docs](https://docs.github.com/en/copilot/reference/custom-agents-configuration): custom agents remain in preview for some IDEs.
- `[VOLATILE]` [Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026): cost/task estimates and model-specific benchmark snapshots are time-sensitive.

### Gaps
- None of the external references describe **The Sourdough Test** as a reusable off-topic boundary probe.
- None of them name **Fabrication Without Action** as a distinct failure class caught by tool-call assertions.
- None of them make the **Safety Gate vs. Off-Topic** distinction as crisply as the primary source.
- None of them argue for **Binary Grading as a Feature** from the perspective of reviewer actionability in CI.
- None of them capture the **Tool Name Translation** problem between production tool IDs and eval-environment tool IDs as concretely as the primary source.
- Several sources discuss regression testing or observability, but almost none describe a real, PR-triggered Copilot-agent eval system with dynamic agent discovery, mirrored agent files, and three grader types running inside full sessions.

### Industry Context for Framing
- The external set makes the timing argument strong: coding-agent benchmark scores are rising quickly ([Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026)), old academic benchmarks are saturating ([explainx.ai](https://explainx.ai/blog/ai-benchmarks-complete-guide-2026)), and production failures are shifting from loud crashes to silent behavioral drift ([Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures), [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage), [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith)).
- The best framing for the blog is therefore **not** "benchmarks are useless." It is: **benchmarks tell you whether the agent can do the task; behavioral evals tell you whether it will do the right thing in production.**
- The primary source gives the missing practitioner bridge between those two worlds: how to turn abstract worries about silent regressions into concrete pass/fail tasks that run on every PR.
