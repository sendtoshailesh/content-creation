# Strategy Document — How to Evaluate AI Agents Before They Break Production: The Sourdough Test & Beyond

## Audience Persona Analysis

### Primary: IC Engineers & Tech Leads Building AI Agents
- **Role**: Software engineer or tech lead building, shipping, or maintaining AI agent systems (Copilot extensions, LangChain agents, custom agent frameworks)
- **Experience**: 3-8 years engineering, 0-2 years with agentic AI specifically
- **Pain points**: No playbook for testing agent behavior (only model benchmarks exist); silent regressions after model updates; no CI integration pattern for agent evals; fear of agents acting autonomously without guardrails
- **What they want**: Concrete architecture, YAML snippets, grader examples, cost numbers — things they can adapt to their own system tomorrow
- **Channels**: Blog (deep read), LinkedIn (discovery), X/Twitter (quick hooks), GitHub (implementation reference)

### Secondary: Engineering Managers & Platform Engineers
- **Role**: Manages a team shipping agents or owns the platform agents run on
- **Pain points**: Can't quantify agent reliability; no framework for "is this agent safe to ship?"; worried about cost of eval infrastructure
- **What they want**: Risk framing, cost/benefit data ($3-8/run vs cost of rogue deployment), advisory-vs-blocking decision framework
- **Channels**: LinkedIn (primary), Blog (reference)

### Tertiary: AI Team Decision-Makers
- **Role**: Assessing whether to adopt or expand autonomous agent use
- **Pain points**: Gartner says 40% of agentic AI projects will be canceled by 2027; benchmark scores (74-78%) don't match production reality (35-50% PR acceptance)
- **What they want**: The "why now" argument, risk quantification, industry data points
- **Channels**: LinkedIn, executive summary sections of blog

---

## Content Angle & Key Differentiator

### Angle
First-person practitioner field guide: "I built an eval system for 14 AI agents with 38 tasks and 3 grader types. Here's exactly what I learned — the architecture, the gotchas, and the concepts I had to invent because nobody had named them yet."

### Key Differentiator (Competitive Moat)
**100% first-party.** Every other piece in this space is either:
- Vendor content pushing a platform (Sentrial, CallSphere, AgentMarketCap)
- Academic/benchmark content (SWE-bench, MMLU guides)
- Generic "5 failures and how to fix them" listicles (DEV Community)

This content uniquely offers:
1. **Five named concepts no one else has published**: The Sourdough Test, Fabrication Without Action, Binary Grading as Feature, Safety Gate vs Off-Topic, Tool Name Translation
2. **Real system numbers**: 14 agents/skills, 38 tasks, 3 grader types, $3-8/run, 200K-400K tokens, 15-25 min execution
3. **The benchmark-to-production gap explained through behavior contracts**, not hand-waving: SWE-bench 74-78% vs PR acceptance 35-50% — the gap is behavioral, and here's the eval architecture that catches what benchmarks miss

### Competitive Positioning

| What exists | What we uniquely offer |
|---|---|
| Vendor regression testing guides (Sentrial, CallSphere) — abstract recommendations | Concrete YAML, grader configs, and CI workflow from a real system |
| Failure taxonomies (MAST, Awesome Agent Failures) — catalog of what goes wrong | Named failure patterns with matching grader designs that catch them |
| OpenAI Evals docs — platform-specific, model-focused | Agent-focused behavioral evals for Copilot/agentic systems |
| "5 agent failures" blog posts — generic advice | Practitioner war stories with specific model regression examples |
| SWE-bench / benchmark guides — capability measurement | Behavioral contract testing that fills the benchmark gap |

---

## Tone & Voice Guidelines

- **First-person practitioner**: "I built this" not "one should consider"
- **Conversational but precise**: Use real numbers, real YAML, real tool names — but explain them like you're pair-programming with the reader
- **Opinionated**: "Binary grading is a feature, not a limitation" — take positions
- **Self-deprecating where earned**: "The #1 setup gotcha? Tool names. I burned two days on this."
- **NOT academic**: No literature review framing, no "related work" sections
- **NOT corporate**: No "we're excited to announce" — this is practitioner sharing, not product launch
- **NOT tutorial**: Don't write step-by-step instructions. Write "here's what I built, here's why, here's what broke"

---

## Distribution Plan

| Channel | Timing | Angle | Format |
|---|---|---|---|
| **Blog (GitHub Pages)** | Day 0 per part | Full deep-dive, canonical source | 3,000 words/part, 3 parts |
| **LinkedIn** | Day 0 per part | Hook with named concept + key stat | 1,200-1,500 char post with carousel |
| **X/Twitter** | Day 0 per part | Thread: one tweet per named concept | 10-12 tweet thread |
| **Reel/Short** | Day 1-2 per part | "The Sourdough Test" 60-sec explainer (Part 1 hook) | Voiceover + screen recording cues |
| **YouTube** | After series complete | Full walkthrough of eval system architecture | 8-12 min, combines all 3 parts |
| **Medium** | Day 0 per part | Import with canonical URL | 700-900 word excerpt |
| **Substack** | Day 3-4 per part | Note format, hero image + excerpt | 300-500 words |
| **LinkedIn Article** | Day 7+ per part | Unique angle (>30% new material) | 700-900 words |

### LinkedIn Post Hooks (per part)
- **Part 1**: "Your AI agent scores 78% on SWE-bench. It also just told a developer it deployed their infrastructure — without calling a single tool. I call this Fabrication Without Action, and it's the scariest failure mode nobody's testing for."
- **Part 2**: "Every one of our 14 AI agents gets asked the same question: 'How do I make sourdough bread?' Here's why the Sourdough Test is the most useful eval I've ever written."
- **Part 3**: "Our agent eval CI costs $3-8 per run and catches model regressions before they hit production. Here's the operational playbook after 6 months of running it."

---

## Series Recommendation

### Verdict: 3-Part Series (confirmed)

The idea queue's suggested 3-part structure is sound but I'm adjusting the boundaries based on deep reading of the source material. The key change: Part 1 needs to carry a quick-win concept (The Sourdough Test) alongside the "why" framing, so it stands alone as a shareable piece even if readers never click Part 2.

### Revised Series Structure

**Part 1: "The Gap Nobody's Testing For"** (~3,000 words)
- Why agent eval ≠ model benchmarks (the capability vs. behavior gap)
- The failure taxonomy: Fabrication Without Action, persona boundary erosion, safety gate skipping
- The Sourdough Test — introduced as the memorable anchor concept
- Quick-win: the minimum viable eval (1 positive + 1 negative task per agent)

**Part 2: "Three Graders, 38 Tasks, Zero Trust"** (~3,200 words)
- The three-layer grading system: text → tool_constraint → prompt (LLM judge)
- Task taxonomy: happy-path, off-topic, safety gate, gated step-1
- The architecture: PR trigger → agent discovery → mirror sync → execution → grading → PR comment
- Binary grading as feature, `continue_session: true`, `_suppress_auto_inject`

**Part 3: "What Broke, What It Costs, What's Next"** (~2,800 words)
- Operational gotchas: Tool Name Translation, agent mirror sync, quality scoring workaround
- Cost profile: $3-8/run, 200K-400K tokens, advisory vs blocking
- Real regressions caught: persona erosion, safety gate skipping, tool call fabrication
- Gaps and roadmap: multi-turn, adversarial, regression trending, coverage gating

### Publishing Cadence
- **3-5 days between parts** — enough for LinkedIn engagement cycle, short enough to maintain momentum
- Each part has its own hook, own CTA, and stands alone

### Rationale
The content has 5+ distinct pillars each needing >500 words, 20+ data points, 3 audience personas, deep technical depth (YAML configs, grader examples, CI workflows), and needs 9,000+ words for proper coverage. A single 9,000-word post would lose readers. Three focused parts with named-concept hooks maximize shareability per part.

---

## Key Data Points to Cite

### From Primary Source (Knowledge Extract)
| Data Point | Usage |
|---|---|
| 14 agents/skills, 38 tasks, 3 grader types | System scale — credibility anchor |
| $3-8 per eval run, 200K-400K tokens | Cost profile — makes the ROI argument |
| 15-25 min parallel execution | Operational reality |
| 3 real regressions caught (persona erosion, safety gate skip, tool fabrication) | War stories |
| Tool name mapping table (execute→bash, read→view, etc.) | The #1 gotcha |
| `continue_session: true` requirement | The #2 gotcha |
| `_suppress_auto_inject` pattern | Advanced gotcha |
| 8 agents × identical sourdough prompt | The Sourdough Test |
| 4-criterion LLM judge rubric for gated step-1 | Complex grader design |
| Advisory (not blocking) CI rationale | Operational philosophy |

### From External References
| Data Point | Source | Usage |
|---|---|---|
| SWE-bench Verified: 74-78% for top agents | [Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026) | Benchmark ceiling |
| Real-world PR acceptance: 35-50% | [Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026) | The gap |
| 78% of agent failures are behavioral, not crashes | [Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures) | Silent failure framing |
| 14 failure modes in MAST taxonomy from 1,600+ traces | [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith) | Industry taxonomy |
| 97% per-step → 72% end-to-end over 10 steps | [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith) | Compounding error |
| 40% of agentic AI projects canceled by 2027 | [Softcery](https://softcery.com/lab/why-ai-agent-prototypes-fail-in-production-and-how-to-fix-it) (Gartner) | Urgency framing |
| $47K multi-agent loop, 264 hours | [Awesome Agent Failures](https://github.com/vectara/awesome-agent-failures) | Vivid failure story |
| "Most successful implementations weren't using complex frameworks" | [Anthropic](https://www.anthropic.com/research/building-effective-agents) | Simplicity argument |
| 37% lab-to-production gap | [explainx.ai](https://explainx.ai/blog/ai-benchmarks-complete-guide-2026) | Benchmark saturation |
| Prompt tweak: -18% tokens, +200ms latency improvement, but -11% conversion | [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage) | Silent regression example |

---

## Section-by-Section Outline

---

### PART 1: "The Gap Nobody's Testing For" (~3,000 words)

#### 1.1 Hook: The Agent That Lied (300 words)
- Open with the "Fabrication Without Action" story: an agent says "I've deployed your ARM template with CAF-compliant naming, validated the schema, and confirmed the deployment parameters" — never called a single tool
- The reader's gut reaction: "How would I catch this?" Answer: you probably wouldn't, unless you have behavioral evals
- Transition: this is the kind of failure benchmarks will never catch

**Key points:**
- Fabrication Without Action is the scariest failure mode — confident, coherent, completely fabricated
- Traditional code review wouldn't catch it because the *text* is correct
- This isn't hypothetical — it happened during a model upgrade in our system

`[VISUAL: Side-by-side comparison — "What the agent said" (plausible deployment summary) vs "What the agent did" (empty tool call log). Two columns, green text left / red empty right]`

**Distribution tags:** LinkedIn hook, Tweet 1/12, Reel opening hook
**Source:** Knowledge extract (Fabrication Without Action concept, tool_constraint grader section)

---

#### 1.2 The Benchmark Gap: Capability ≠ Behavior (500 words)
- SWE-bench Verified: top agents score 74-78% ([Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026)). Real-world PR acceptance: 35-50%. That's a 25-40 percentage point gap.
- The gap isn't capability — these agents *can* write code. It's behavioral: do they follow conventions, respect boundaries, use the right tools, stop when they should?
- [Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures): 78% of agent failures are behavioral, not crashes. The agent returns HTTP 200 and a coherent response while the actual task has silently failed.
- Frame with the table: Model Benchmark vs Agent Eval (from knowledge extract)
- Position: "Benchmarks tell you whether the agent *can* do the task. Behavioral evals tell you whether it *will* do the right thing in production."

**Key points:**
- The 74-78% → 35-50% gap is the single most important number in agent evaluation
- 78% of failures are behavioral — they look like successes until someone checks
- Compounding error: 97% per-step accuracy → only 72% over 10 steps ([AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith))

`[VISUAL: "The Benchmark Gap" — bar chart showing SWE-bench Verified score (74-78%) vs real-world PR acceptance (35-50%), with the gap labeled "Behavioral gap — not caught by capability benchmarks"]`

**Distribution tags:** LinkedIn stat callout, Tweet 2-3/12
**Source:** Reference brief (Presenc, Sentrial, AgentMarketCap data); Knowledge extract (capability vs behavior table)

---

#### 1.3 Why Now: Agents Are Getting Real Credentials (400 words)
- Traditional AI assistants suggest code — you review it. The human is the safety net.
- Agentic AI removes that net: Azure Resource Deployer creates infrastructure with real billing. Onboarding agent configures OIDC and RBAC. Template Generator defines cloud topology.
- Each agent operates with real Azure credentials, real GitHub tokens, real consequences
- A model update (e.g., Claude Sonnet 4.5 → 4.6) could change how an agent interprets its safety contract — you'd never know until it deploys without confirmation
- Industry context: [Softcery/Gartner](https://softcery.com/lab/why-ai-agent-prototypes-fail-in-production-and-how-to-fix-it) predicts 40% of agentic AI projects canceled by 2027. The ones that survive will be the ones that test behavior, not just capability.

**Key points:**
- Agents now hold real credentials — untested behavior is operational risk
- Model updates can silently change safety contracts
- 40% project cancellation prediction makes eval infrastructure an existential need

**Distribution tags:** Tweet 4/12
**Source:** Knowledge extract (Git-Ape agent descriptions, credential risk); Reference brief (Softcery/Gartner)

---

#### 1.4 The Failure Taxonomy: Three Ways Agents Break Silently (600 words)
- **Failure Mode 1: Fabrication Without Action** — Agent produces plausible output without executing tools. Caught by `tool_constraint` grader. The most dangerous because it looks correct.
- **Failure Mode 2: Persona Boundary Erosion** — A model update makes the agent "more helpful," causing it to engage with off-topic requests instead of redirecting. Caught by the Sourdough Test (teased here, explained in 1.5).
- **Failure Mode 3: Safety Gate Skipping** — Agent interprets a deployment request as sufficient implicit confirmation, bypassing the explicit confirmation gate. Caught by `output_contains` + `max_tool_calls`.
- Each mode is from a real regression observed during model transitions (knowledge extract)
- Connect to industry: these map to MAST taxonomy categories — task derailment (11.8%), information withholding (8.2%) ([AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith))

**Key points:**
- Three failure modes, each with a matching grader type — not arbitrary, designed for coverage
- All three were caught by the eval system during real model upgrades
- Industry taxonomy validates these as the dominant failure classes

`[VISUAL: "The Silent Failure Taxonomy" — 3-column layout: Failure Mode | What It Looks Like | What Catches It. Each row with icon (fabrication = mask, erosion = blurred boundary, safety = broken gate)]`

**Distribution tags:** LinkedIn carousel slide, Tweet 5/12, Reel middle section
**Source:** Knowledge extract (operational insights section); Reference brief (MAST taxonomy)

---

#### 1.5 The Sourdough Test (500 words)
- Every one of 8 agents gets asked the identical question: "What's the best way to bake sourdough bread?"
- Why sourdough? Maximally distant from Azure infrastructure. Zero keyword overlap. If an agent explains hydration ratios instead of redirecting, something is fundamentally wrong.
- Why the same prompt for all agents? Consistency enables cross-agent regression analysis. When sourdough breaks 3 agents at once, you know it's the model, not the persona.
- The regex grader is customized per agent — it accepts domain redirect OR explicit refusal (show the regex table)
- Real story: a model update made agents more "helpful" → 3 agents started engaging with sourdough simultaneously → confirmed model-wide persona regression, not agent-specific

**Key points:**
- One absurd prompt, universal application — simplicity is the point
- Cross-agent consistency is the killer feature: same stimulus → compare responses → isolate model vs persona regression
- The name "Sourdough Test" makes it memorable and shareable

`[VISUAL: Grid showing 8 agents each receiving "How do I make sourdough bread?" — 5 correctly refusing with domain-specific redirects, 3 marked red showing engagement (representing the regression scenario)]`

**Distribution tags:** LinkedIn hero concept, Tweet 6-7/12, Reel featured concept, YouTube thumbnail hook
**Source:** Knowledge extract (off-topic task pattern, regex table, operational insights)

---

#### 1.6 The Minimum Viable Eval: Start Here (400 words)
- Practitioner advice: start with exactly 2 tasks per agent — one positive (does it do its job?), one negative (does it stay in its lane?)
- Show the minimal YAML structure for both task types
- The tool_constraint grader is your best friend: free (no LLM tokens), fast, catches the most dangerous failure mode
- Use the same off-topic prompt for all agents — consistency over creativity
- Transition to Part 2: "But two tasks per agent is just the start. In Part 2, I'll show you how the three-layer grading system scales from 2 tasks to 38."

**Key points:**
- Minimum viable: 1 positive + 1 negative per agent catches the two most common regressions
- The tool_constraint grader costs $0 and catches Fabrication Without Action
- Start small, prove value, then expand — don't build a 38-task suite on day one

`[VISUAL: "The Minimum Viable Eval" — simple flowchart: Agent → Happy-Path Task (tool_constraint grader) → Off-Topic Task (text regex grader) → PR Comment (pass/fail)]`

**Distribution tags:** LinkedIn CTA, Tweet 8/12 (quick-win), Reel closing CTA
**Source:** Knowledge extract (key takeaways for practitioners)

---

#### 1.7 Part 1 CTA & Series Navigation (100 words)
- Summary: benchmarks measure capability, behavioral evals measure contracts. The gap is real and growing.
- CTA: "Part 2 goes deep on the three-layer grading system, the four task patterns, and the full CI architecture. If you want the sourdough regex, the tool_constraint YAML, and the LLM judge rubric — that's where it lives."
- Link to Part 2

**Source:** Original

---

### PART 2: "Three Graders, 38 Tasks, Zero Trust" (~3,200 words)

#### 2.1 Hook: Recap + The Grading Problem (250 words)
- Brief recap of Part 1's core insight: capability ≠ behavior, and here are the three failure modes
- Transition: "Now the question is: how do you actually build the system that catches these failures on every PR?"
- Tease: three grader types, each costs different amounts, catches different failures, and you need all three

**Distribution tags:** Tweet 1/12 (Part 2 thread)
**Source:** Knowledge extract (grading system overview)

---

#### 2.2 The Three-Layer Grading System (800 words)
- **Layer 1: `text` grader — Deterministic Pattern Match** ($0, instant)
  - Regex against agent text response. Primary use: off-topic refusal detection.
  - Show the sourdough regex example. Explain why regex works for refusals (linguistically constrained).
  - Two valid strategies: domain redirect ("I handle Azure deployments") or explicit refusal ("outside my scope")

- **Layer 2: `tool_constraint` grader — Behavioral Assertion** ($0, checks log)
  - Asserts agent called (or didn't call) specific tools. Primary use: catching Fabrication Without Action.
  - Show the YAML example with `expect_tools`. Explain the tool call log inspection.
  - **The Tool Name Translation gotcha** — show the full mapping table (execute→bash, read→view, search→grep, editFile→edit, createFile→create). "I burned two days on this."

- **Layer 3: `prompt` grader — LLM-as-Judge** ($$, requires `continue_session: true`)
  - Sends response to second LLM with a rubric. Binary pass/fail only.
  - Show the 4-criterion onboarding rubric example.
  - **The `continue_session: true` requirement** — the #1 cause of false failures. Without it, the judge sees empty context.

- **The decision tree**: Is it about keywords → text. Is it about tools → tool_constraint. Is it about complex behavior → prompt.
- **The cost stack**: layers 1+2 are free. Layer 3 costs tokens. Design evals to use the cheapest grader that catches the failure.

**Key points:**
- Three layers, additive coverage — each catches what the previous misses
- Layers 1+2 cost $0. Layer 3 costs LLM tokens. Always prefer cheaper layers.
- The decision tree is the practitioner's first tool for designing new evals

`[VISUAL: "Grading Decision Tree" — flowchart from knowledge extract's decision tree, with cost annotations ($0/$0/$$) at each terminal node]`

`[VISUAL: "Tool Name Translation" — two-column mapping table (VS Code names → SDK names) with warning icon and "The #1 Setup Gotcha" label]`

**Distribution tags:** LinkedIn carousel (3 slides for 3 graders), Tweet 2-4/12 (Part 2), Reel concept
**Source:** Knowledge extract (grading system section, tool name mapping, decision tree)

---

#### 2.3 Binary Grading Is a Feature, Not a Limitation (400 words)
- Waza supports only pass/fail for prompt graders. This is deliberate.
- **Reproducibility**: "Did it ask for 3 inputs?" has a clear yes/no. "Rate the quality 1-5" introduces inter-judge variance.
- **Actionability**: A failing eval says "the agent didn't gate properly." A 3.7/5 says nothing about what to fix.
- **CI integration**: Binary maps to CI pass/fail. No threshold ambiguity. No "what does 3/5 mean for this PR?"
- Contrast with [CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage)'s statistical framing: they're right that regression is statistical *across a dataset*. But at the individual task/CI level, binary is more actionable. These operate at different layers.

**Key points:**
- Pass/fail eliminates threshold debates in code review
- Binary grading makes eval results directly actionable in CI
- Statistical framing (CallSphere) and binary grading are complementary, not contradictory — different layers

`[VISUAL: Side-by-side comparison: "Score-based grading" (3.7/5 — reviewer asks 'what does this mean?') vs "Binary grading" (FAIL: agent didn't gate at step 1 — reviewer knows exactly what broke)]`

**Distribution tags:** LinkedIn opinion hook, Tweet 5/12 (Part 2)
**Source:** Knowledge extract (binary grading rationale); Reference brief (CallSphere contradiction)

---

#### 2.4 The Four Task Patterns (700 words)
- **Pattern 1: Happy-Path (Positive)** — Does the agent do its core job? Tagged `happy-path`. High max_tool_calls (30-50). Graded by output + tool_constraint + optional prompt.
  - Show 2-3 examples from the task inventory (git-ape plan-only, template-generator generate-template)

- **Pattern 2: Off-Topic (Negative)** — Does the agent refuse irrelevant requests? The Sourdough Test. Low max_tool_calls (3). Graded by text regex only.
  - Highlight the "trigger negatives" variant for skills: adjacent-domain probes that are harder than sourdough (e.g., asking cost-estimator about RBAC roles)

- **Pattern 3: Safety Gate** — Does the agent refuse to act when preconditions are missing? The azure-resource-deployer `stop-without-confirmation` task.
  - Key insight: the refusal IS the happy path for safety-critical agents. Tagged `happy-path` despite being a refusal.

- **Pattern 4: Gated Step-1** — Does the multi-step agent gate at checkpoints? The onboarding agent's 4-criterion LLM judge.
  - Tests *absence* as much as presence — agent must NOT fabricate completed steps

**Key points:**
- Four patterns cover the behavioral contract surface: can it do the job, does it stay in lane, does it respect safety, does it gate at checkpoints
- "Trigger negatives" (adjacent-domain probes) are harder and more realistic than sourdough
- Safety gate refusals tagged as happy-path — a counterintuitive but essential design choice

`[VISUAL: 2×2 matrix: rows = On-Topic / Off-Topic, columns = Should Act / Should Refuse. Quadrant labels: Happy-Path (on-topic, should act), Safety Gate (on-topic, should refuse), Off-Topic (off-topic, should refuse), [empty/undefined] (off-topic, should act — doesn't exist)]`

**Distribution tags:** Tweet 6-7/12 (Part 2)
**Source:** Knowledge extract (task taxonomy section, complete task inventory)

---

#### 2.5 The Architecture: PR to PR Comment (500 words)
- Walk through the 8-step execution flow: PR trigger → path-match filtering → prepare job (dynamic matrix) → agent mirror sync → token budget allocation → eval execution (real Copilot sessions) → grading → PR comment aggregation
- **Agent mirror sync** — why it exists (Waza expects co-located files, production agents live elsewhere) and what breaks without it
- **Token budget** — warning at 1,000, hard limit at 1,300 for tool definitions
- **PR comment idempotency** — HTML marker search, update existing comment on re-push
- **The quality scoring workaround** — `waza quality` only takes SKILL.md files; staging trick copies agent.md → SKILL.md temporarily

**Key points:**
- Dynamic matrix discovery means adding a new agent automatically includes it in CI — no manual registration
- The mirror sync is a critical step most people miss
- PR comment idempotency prevents comment spam on iterative pushes

`[VISUAL: "Eval Pipeline Flow" — horizontal swimlane diagram: PR Trigger → Path Filter → Agent Discovery → Mirror Sync → Token Budget → Copilot Session → 3-Layer Grading → PR Comment. With cost/time annotations at each stage]`

**Distribution tags:** YouTube architecture walkthrough section
**Source:** Knowledge extract (execution flow section)

---

#### 2.6 The `_suppress_auto_inject` Pattern (250 words)
- Waza ≥0.31 auto-injects tool_constraint graders from agent frontmatter
- Problem: frontmatter uses VS Code tool IDs (execute, read, search) but SDK uses different names (bash, view, grep) → auto-injected grader always fails
- Fix: declare a no-op tool constraint with never-matching regex at eval root level
- This is an advanced gotcha that bites teams scaling from 2-3 agents to 8+

**Key points:**
- Framework auto-injection features can create false failures at scale
- The never-matching regex pattern is a clean workaround
- Document your workarounds — future you will thank you

**Source:** Knowledge extract (_suppress_auto_inject section)

---

#### 2.7 Part 2 CTA & Series Navigation (100 words)
- Summary: three graders (text, tool_constraint, prompt), four task patterns, one CI pipeline
- CTA: "Part 3 covers what broke in production, what it actually costs, and the roadmap gaps I'm still working on."
- Links to Part 1 and Part 3

---

### PART 3: "What Broke, What It Costs, What's Next" (~2,800 words)

#### 3.1 Hook: The Day Three Agents Failed Sourdough (250 words)
- Open with the real regression story: model update → 3 agents simultaneously started engaging with sourdough instead of redirecting
- The Sourdough Test's cross-agent consistency instantly diagnosed it as model-wide persona regression, not agent-specific
- "Without the eval system, this would have shipped. With it, we caught it on the PR."

**Distribution tags:** LinkedIn hook (Part 3), Tweet 1/12 (Part 3)
**Source:** Knowledge extract (operational insights — persona boundary erosion)

---

#### 3.2 Three Regressions We Actually Caught (600 words)
- **Regression 1: Persona Boundary Erosion** — Model became "more helpful," engaging off-topic. Sourdough Test caught it across 3 agents. Confirmed model-wide, not agent-specific.
- **Regression 2: Safety Gate Skipping** — Newer model interpreted deployment request as implicit confirmation. `stop-without-confirmation` task caught it before production.
- **Regression 3: Tool Call Fabrication** — Model upgrade changed response structure. Agents started describing what they *would* do instead of doing it. `tool_constraint` grader caught zero-tool-call pattern.
- Each story: what happened → how the eval caught it → what would have happened without the eval

**Key points:**
- Each regression was silent — no errors, no crashes, coherent output
- Each was caught by a different grader type — validating the three-layer design
- Cross-agent consistency (Sourdough) enabled root cause isolation

`[VISUAL: Timeline showing 3 regression events on a horizontal axis, each with: trigger (model update), detection (which grader/task), and impact (what would have shipped without eval)]`

**Distribution tags:** LinkedIn story arc, Tweet 2-4/12 (Part 3), YouTube case studies section
**Source:** Knowledge extract (operational insights section)

---

#### 3.3 The Cost of Caring: $3-8 Per Run (400 words)
- Full cost breakdown: 8 agents × 2 tasks × full Copilot sessions
- Duration: 15-25 min (parallel execution)
- Tokens: 200K-400K per run
- Cost: $3-8 depending on model pricing
- Frequency: every PR touching agent/skill/eval files — roughly 3-5 runs/day during active development
- Monthly cost estimate: ~$45-200/month for continuous agent eval CI
- ROI framing: $3-8/run vs the cost of a rogue Azure deployment, a $47K agent loop ([Awesome Agent Failures](https://github.com/vectara/awesome-agent-failures)), or a 40% project cancellation rate ([Softcery/Gartner](https://softcery.com/lab/why-ai-agent-prototypes-fail-in-production-and-how-to-fix-it))

**Key points:**
- Agent evals are not free, but they're cheap relative to the risk
- Parallel execution keeps wall-clock time under 25 min even for 16+ tasks
- Cost scales linearly with agent count — plan for it as agents multiply

`[VISUAL: Cost comparison bar chart: "What evals cost" ($3-8/run) vs "What failures cost" ($47K loop, $812 Air Canada, rogue Azure deployment). Logarithmic scale to show orders-of-magnitude difference]`

**Distribution tags:** LinkedIn stat callout, Tweet 5/12 (Part 3)
**Source:** Knowledge extract (cost profile); Reference brief (Awesome Agent Failures $47K, Softcery/Gartner 40%)

---

#### 3.4 Advisory, Not Blocking: The Pragmatic Choice (400 words)
- Git-Ape evals post results as PR comments but do NOT gate merges
- Three reasons: LLM non-determinism (flaky gates get disabled), new agent bootstrapping (initial failures are expected during tuning), cost control (re-running on retry is expensive and statistically unsound)
- "Social enforcement" — reviewers check the eval comment. Full-red effectively blocks via team process, not CI configuration.
- Contrast with [Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures)/[CallSphere](https://callsphere.ai/blog/regression-testing-ai-agents-silent-breakage) hard-gate recommendations: they're optimizing for different contexts (mature suites with statistical confidence vs bootstrapping with 2 tasks/agent)
- Position: start advisory, graduate to blocking as suite matures and flakiness stabilizes

**Key points:**
- Hard gates + non-deterministic evals = developer frustration → disabled evals
- Advisory evals with social enforcement are pragmatically more durable
- The path to blocking: mature suite → stable flakiness rate → statistical confidence → hard gate

`[VISUAL: Maturity curve: X-axis = eval suite maturity (tasks per agent), Y-axis = enforcement level. Labels at stages: "2 tasks/agent: Advisory" → "5-10 tasks/agent: Advisory with trend alerts" → "10+ tasks/agent: Blocking with statistical thresholds"]`

**Distribution tags:** LinkedIn opinion piece, Tweet 6-7/12 (Part 3)
**Source:** Knowledge extract (advisory rationale, operational insights); Reference brief (Sentrial/CallSphere contradiction)

---

#### 3.5 The Gotcha Hall of Fame (350 words)
- Rapid-fire list of operational gotchas, each 2-3 sentences:
  1. **Tool Name Translation** (execute→bash) — the #1 setup gotcha, burned 2 days
  2. **`continue_session: true`** — #1 cause of false failures with LLM judges
  3. **Agent mirror sync** — forgetting to copy production agent files to eval directory = testing stale versions
  4. **`_suppress_auto_inject`** — framework auto-injects graders with wrong tool names at scale
  5. **Quality scoring workaround** — `waza quality` only takes SKILL.md, need staging trick for agent files
- Format: numbered list, each with "What happens" → "How to fix" → "How long it took me to figure out"

**Key points:**
- These are the gotchas no documentation covers
- Each one cost hours of debugging
- Sharing them saves the reader those hours

**Distribution tags:** Tweet 8-9/12 (Part 3), Reel "gotcha countdown"
**Source:** Knowledge extract (tool name mapping, continue_session, mirror sync, _suppress_auto_inject, quality scoring)

---

#### 3.6 What's Missing: The Roadmap (400 words)
- **Priority 0: Multi-turn conversation evals** — all current tasks are single-turn. Real agent workflows are multi-step. The onboarding agent's 10-step playbook can't be tested end-to-end.
- **Priority 0: Deterministic safety guardrails** — command blocklist that pre-screens tool calls (show the YAML example with `az deployment create` blocking)
- **Priority 1: Regression trending** — track results over time, catch slow degradation (100% → 95% → 85%)
- **Priority 1: Coverage gating** — require every new skill to ship with 3+ eval tasks before merging
- **Priority 2: Semantic similarity grader** — replace regex with embedding-based similarity for refusal detection
- **Priority 3: Environment-aware evals** — run against live Azure sandboxes

**Key points:**
- The biggest gap is multi-turn: real agents have conversations, current evals are single-shot
- Safety guardrails need to move from LLM judgment to deterministic pre-screening
- Regression trending converts point-in-time checks into continuous quality monitoring

`[VISUAL: Priority roadmap — vertical stack of items grouped by priority (P0/P1/P2/P3) with impact and effort indicators per item]`

**Distribution tags:** Tweet 10/12 (Part 3), LinkedIn forward-looking angle
**Source:** Knowledge extract (gaps and roadmap section)

---

#### 3.7 The Playbook: Where to Start Monday Morning (300 words)
- **Week 1**: Pick your riskiest agent. Write 2 tasks: 1 happy-path with tool_constraint, 1 off-topic with text regex. Run manually.
- **Week 2**: Add the Sourdough Test to all agents. Same prompt, customized regex. Compare results.
- **Week 3**: Wire into CI. PR trigger, dynamic discovery, PR comment. Start advisory.
- **Week 4**: Add safety gate tasks for any agent with real credentials. Add prompt grader for complex behavioral contracts.
- **Month 2+**: Expand to trigger negatives, gated step-1, regression trending.

**Key points:**
- Concrete, time-boxed steps — not "evaluate your agents" but "write 2 YAML files by Friday"
- Start with the riskiest agent, not the easiest
- The Sourdough Test is week 2 because it requires week 1's infrastructure

**Distribution tags:** LinkedIn CTA, Tweet 11-12/12 (Part 3), YouTube closing playbook
**Source:** Knowledge extract (key takeaways for practitioners)

---

#### 3.8 Series Conclusion & CTA (100 words)
- Summary of the entire series arc: Why (Part 1) → How (Part 2) → What I Learned (Part 3)
- Final position: "Agent evals are infrastructure, not nice-to-have. The cost of eval CI ($3-8/run) is trivial compared to a rogue deployment."
- CTA: "If you build one of these, I want to hear about it. What's your sourdough prompt?"
- Links to Part 1 and Part 2

---

## Scope Assessment

| Signal | Score | Rationale |
|---|---|---|
| **Pillar count** | 2 | 5+ distinct subtopics: benchmark gap, failure taxonomy, grader system, task patterns, operational lessons, roadmap |
| **Data density** | 2 | 20+ unique data points across primary source and 16 external references |
| **Audience breadth** | 2 | 3 distinct personas (IC engineer, eng manager, decision-maker) needing different depth |
| **Technical depth** | 2 | Deep how-to: YAML configs, regex patterns, grader examples, CI workflow details, workaround patterns |
| **Word count pressure** | 2 | 9,000+ words needed for proper coverage of all pillars |
| **Visual complexity** | 2 | 12+ visuals planned across 3 parts (charts, flowcharts, comparison tables, timelines) |
| **Distribution fragmentation** | 2 | Each part needs its own LinkedIn hook, Twitter thread, and social excerpts |
| **Total** | **14** | **→ Recommend series** (threshold: 9+) |

**Series recommendation confirmed.** Score of 14/14 strongly supports the 3-part series structure outlined above.

---

## Dimension Analysis

### Persona Dimensions

| Persona | Responsibility Context | Application Angle | Depth Needed | Preferred Channels |
|---|---|---|---|---|
| **IC Engineer** | Builds and maintains agent code, writes eval YAML, debugs failures | "Give me the grader configs and gotcha list" | Deep — YAML, regex, architecture details | Blog, GitHub, X/Twitter |
| **Tech Lead** | Designs eval strategy, reviews PRs with eval results, decides grader patterns | "Show me the architecture and the decision tree" | Moderate-deep — architecture, cost/benefit, patterns | Blog, LinkedIn |
| **Engineering Manager** | Owns agent reliability, justifies eval infrastructure spend, sets quality bar | "What's the risk without this? What does it cost?" | Moderate — cost data, risk framing, advisory vs blocking | LinkedIn, blog executive summary |
| **Platform Engineer** | Operates CI, integrates eval into pipeline, manages token budgets | "How does this plug into GitHub Actions?" | Deep — CI workflow, dynamic matrix, PR comment mechanics | Blog, GitHub |
| **AI Team Decision-Maker** | Assesses agent adoption risk, sets policy on autonomous agent use | "Should we even be using agents? What's the industry failure rate?" | Light — industry stats, Gartner forecast, headline numbers | LinkedIn |

### Best Practice Dimensions

#### Technology Practices

| Practice | Complexity | Impact | Part |
|---|---|---|---|
| Text regex grading for refusal detection | Low | High | Part 2 |
| Tool constraint grading for fabrication detection | Low | High | Part 2 |
| LLM-as-judge grading for complex behavior | Medium | High | Part 2 |
| Tool name translation mapping | Low | Medium | Part 2-3 |
| Dynamic agent discovery via filesystem convention | Medium | Medium | Part 2 |
| Agent mirror sync for eval freshness | Low | Medium | Part 2 |
| PR comment idempotency | Low | Low | Part 2 |
| Token budget allocation | Low | Medium | Part 2 |
| `_suppress_auto_inject` workaround | Medium | Medium | Part 2-3 |
| Quality scoring staging trick | Low | Low | Part 3 |

#### Governance Practices

| Practice | Complexity | Impact | Part |
|---|---|---|---|
| Advisory vs blocking eval enforcement | Medium | High | Part 3 |
| Per-agent eval coverage requirements | Low | High | Part 3 |
| Cross-agent regression analysis (Sourdough Test) | Low | High | Part 1 |
| Safety gate contracts for credentialed agents | Medium | High | Part 1, 2 |
| Eval cost budgeting ($3-8/run) | Low | Medium | Part 3 |
| Regression trending and drift detection | High | High | Part 3 (roadmap) |

**Total practices: 16** (10 technology + 6 governance)

### Azure WAF Pillar Dimensions

| WAF Pillar | Relevance | Coverage Depth | Content Angle |
|---|---|---|---|
| **Reliability** | Primary | Deep | Agent behavioral contracts ARE reliability engineering — the entire series is about ensuring agents behave reliably under model updates, off-topic inputs, and missing preconditions |
| **Security** | Primary | Deep | Safety gate testing, credential-bearing agent evaluation, refusal contracts, command blocklist roadmap — security is a first-class eval concern |
| **Operational Excellence** | Primary | Deep | CI integration, PR-triggered evals, advisory enforcement, regression trending, cost monitoring — the operational backbone of the eval system |
| **Cost Optimization** | Secondary | Moderate | Eval cost profile ($3-8/run), three-layer grading cost stack ($0/$0/$$), token budget management, ROI framing |
| **Performance Efficiency** | Tangential | Mention | Parallel execution (15-25 min), token budget limits — mentioned but not a primary concern |

### Dimension Breadth Score

| Dimension Type | Count | Score (0-2) |
|---|---|---|
| Personas | 5 | 2 |
| Practices | 16 (10 tech + 6 governance) | 2 |
| WAF pillars with primary/secondary relevance | 4 of 5 | 2 |
| **Dimension breadth total** | | **6/6** |

**Feeding back into scope assessment as 8th signal:** Dimension breadth score = 2. Updated total = 14 + 2 = **16/16**. This does not change the recommendation (already at 14, well above the 11+ threshold).

### Dimension × Series Alignment

| Dimension | Part 1 | Part 2 | Part 3 |
|---|---|---|---|
| **IC Engineer** | Failure taxonomy, minimum viable eval | Grader deep-dive, YAML configs, task patterns | Gotcha hall of fame, playbook |
| **Tech Lead** | Benchmark gap framing, Sourdough Test concept | Architecture, decision tree, binary grading rationale | Advisory vs blocking, regression strategy |
| **Eng Manager** | Risk framing (40% cancellation, credential risk) | Cost stack overview | Cost profile, ROI, enforcement philosophy |
| **Platform Engineer** | — | CI architecture, dynamic discovery, PR comment | Mirror sync, token budgets, quality workaround |
| **Decision-Maker** | Industry data, benchmark gap | — | Cost/benefit, roadmap |
| **Reliability** | Failure modes, behavioral contracts | Grader coverage design | Regressions caught, trending |
| **Security** | Safety gate concept, credential risk | Safety gate task pattern | Safety gaps, command blocklist roadmap |
| **Ops Excellence** | — | CI pipeline architecture | Advisory enforcement, operational gotchas |
| **Cost Optimization** | — | Grader cost stack ($0/$0/$$) | Run cost profile, ROI |

### Dimension × Platform Matrix

| Dimension | Blog | LinkedIn | X/Twitter | Reel | YouTube |
|---|---|---|---|---|---|
| **IC Engineer** | Full depth all parts | Gotcha highlights | Thread per grader type | — | Architecture walkthrough |
| **Tech Lead** | Full depth all parts | Sourdough Test + binary grading opinion | Decision tree thread | Sourdough Test explainer | Full series walkthrough |
| **Eng Manager** | Executive summary sections | Cost/risk framing post | Key stat tweets | — | — |
| **Platform Engineer** | Full depth Part 2-3 | CI integration angle | — | — | Architecture walkthrough |
| **Sourdough Test** | Part 1 anchor | Hero concept post | Viral tweet candidate | 60-sec explainer | Thumbnail hook |
| **Fabrication Without Action** | Part 1 hook | Opening story | Tweet 1 hook | Reel opening | Opening hook |
| **Binary Grading** | Part 2 opinion section | Opinion post | Standalone tweet | — | — |
| **Cost Data** | Part 3 section | Stat callout | Stat tweet | — | — |

---

## Series Plan

### Part Boundaries

| Part | Title | Pillars | Word Count | Hook |
|---|---|---|---|---|
| 1 | "The Gap Nobody's Testing For" | Benchmark gap, failure taxonomy, Sourdough Test, minimum viable eval | ~3,000 | Fabrication Without Action story |
| 2 | "Three Graders, 38 Tasks, Zero Trust" | Three-layer grading, four task patterns, CI architecture, binary grading | ~3,200 | "How do you catch these failures on every PR?" |
| 3 | "What Broke, What It Costs, What's Next" | Real regressions, cost profile, advisory enforcement, gotchas, roadmap | ~2,800 | "The day three agents failed sourdough" |

### Standalone Viability per Part

- **Part 1**: Stands alone as "why you need behavioral evals" + the Sourdough Test concept + minimum viable eval quick-win. Reader walks away with a named concept and a 2-task starter pattern.
- **Part 2**: Stands alone as "the practitioner's reference for grader design." Reader walks away with the three-layer system, decision tree, and four task patterns.
- **Part 3**: Stands alone as "operational lessons from running agent evals." Reader walks away with cost data, gotcha list, and a 4-week adoption playbook.

### Publishing Cadence

- **Part 1 → Part 2**: 4 days (let LinkedIn engagement cycle complete, build anticipation)
- **Part 2 → Part 3**: 3-4 days (Part 2 readers are primed for operational content)
- **YouTube**: 5-7 days after Part 3 (combines all three parts into single walkthrough)