# YouTube Script — AI Agent Evals for Production Readiness

**Canonical URL:** https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html  
**Target runtime:** ~10:45  
**Status:** Draft only. Do not publish without final review.  
**Package:** AI Agent Evals Visual-First Edition  
**Primary message:** SWE-bench proves capability. Production evals prove behavior.

---

## Title Options

1. SWE-bench Is Not Your Production AI Agent Eval
2. Why Coding Agent Benchmarks Miss Production Failures
3. AI Agent Evals: The 4-Layer System Before Production
4. Stop Shipping AI Agents Without Behavior Evals

---

## Full Script

### [0:00 - 0:35] Cold Open — "The Benchmark Gap"

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/medium-hero.png`  
**SCREEN RECORDING CUE:** Full-screen benchmark exhibit. Slow zoom from "74-78% SWE-bench Verified" to "35-50% PR acceptance."  
**B-ROLL / VISUAL CUE:** Add subtle red gap highlight between benchmark score and PR acceptance estimate.  
**CHAPTER TITLE:** The Benchmark Gap

**SCRIPT:**

Presenc's May 2026 vendor snapshot reports top coding agents at **74 to 78 percent on SWE-bench Verified**.

That sounds production-ready.

The same snapshot also estimates real-world PR acceptance closer to **35 to 50 percent**.

That gap is the whole video.

Because SWE-bench tells you whether an agent can solve a coding task.

Production evals tell you whether that agent follows your behavior contract when prompts, tools, policies, models, and team conventions change.

And the scariest failures do not always crash.

Sometimes the agent says:

"I created the file. I validated the schema. The deployment is ready."

But the tool-call log is empty.

That is not a benchmark problem.

That is a production eval problem.

**NOTES:** Fast, serious opening. Pause after "tool-call log is empty."

---

### [0:35 - 1:25] Intro — What This Video Solves

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/slide-01-hook.png`  
**SCREEN RECORDING CUE:** Picture-in-picture talking head over slide.  
**B-ROLL / VISUAL CUE:** Cut to blurred IDE, PR checks panel, agent response window.  
**CHAPTER TITLE:** Capability vs Behavior

**SCRIPT:**

In this video, I'm sharing my learnings from building agent eval patterns for production teams.

The core lesson is simple:

**Benchmarks prove capability. Production evals prove behavior.**

If you are evaluating an AI coding agent only with benchmark scores, you are missing the failures that show up after deployment:

wrong tool use, skipped confirmation gates, persona drift, fabricated actions, and silent regressions after a model or prompt update.

We'll walk through five pieces:

First, the benchmark gap.

Second, why silent behavior failures are different from normal crashes.

Third, the Sourdough Test — an absurd but useful eval for persona drift.

Fourth, a four-layer production eval system.

And fifth, how to wire this into CI so it runs where engineering decisions already happen: pull requests.

**NOTES:** Conversational. Make it clear this is practical, not benchmark-bashing.

---

### [1:25 - 2:35] Benchmark Gap — Why SWE-bench Is Useful but Not Enough

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/medium-hero.png`  
**SCREEN RECORDING CUE:** Full-screen slide. Add labels: "Capability signal" and "Production readiness signal."  
**B-ROLL / VISUAL CUE:** Show SWE-bench as one column, production evals as another.  
**CHAPTER TITLE:** SWE-bench Is a Capability Signal

**SCRIPT:**

SWE-bench is useful.

It gives us a structured way to compare coding-agent capability on real software-engineering tasks.

But it does not answer the question most teams need before production:

Will this agent behave correctly inside our workflow?

Presenc's May 2026 snapshot reports top coding agents at **74 to 78 percent on SWE-bench Verified**, while estimating real-world PR acceptance closer to **35 to 50 percent**.

Important caveat: I treat those Presenc numbers as vendor-reported, point-in-time signals, not permanent leaderboard laws.

The exact numbers will move.

But the shape of the problem is real.

A benchmark asks:

Can the agent solve this coding task?

A production eval asks:

Did it use the required tools?

Did it respect the persona boundary?

Did it ask for confirmation before a risky action?

Did it follow our team's naming, security, and deployment conventions?

Did the same behavior continue to pass after a prompt, tool, policy, or model change?

That is a different test.

**NOTES:** Avoid sounding anti-benchmark. Emphasize "useful but incomplete."

---

### [2:35 - 3:45] Silent Behavior Failures — The Failures That Look Successful

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-02.png`  
**SCREEN RECORDING CUE:** Mock agent transcript:
- Agent: "I created the file and validated the schema."
- Tool calls: `0`
- Eval result: `failed: tool_call_required`

**B-ROLL / VISUAL CUE:** Split screen: left side "clean response," right side "empty trace."  
**CHAPTER TITLE:** Silent Failures

**SCRIPT:**

The dangerous failure is not always a stack trace.

It is the agent returning a polished, confident answer while violating the contract.

Here is the pattern I call **Fabrication Without Action**.

The agent says:

"I created the ARM template."

"I validated the schema."

"I updated the deployment file."

But when you inspect the trace, there was no file edit, no bash command, no schema validation, no tool call.

From a normal response-quality perspective, the answer might look fine.

From a production-readiness perspective, it failed.

Sentrial's May 2026 vendor analysis reports that **78 percent of failures across its analyzed 12 million production logs** were behavioral or silent failures rather than clean crashes, timeouts, or HTTP errors.

Same caveat: I treat that as a vendor-reported operational signal, not a universal law.

But it matches the failure mode teams actually struggle with.

The agent did not explode.

It quietly did the wrong thing.

And that means your evals need to inspect behavior, not just final text.

**NOTES:** Slow down on "quietly did the wrong thing."

---

### [3:45 - 5:10] The Sourdough Test Story

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-03.png`  
**SCREEN RECORDING CUE:** Pan-and-scan across the Sourdough storyboard states and 3 of 8 callout.  
**B-ROLL / VISUAL CUE:** Add caption: "One absurd prompt. Eight agents. Three failures."  
**CHAPTER TITLE:** The Sourdough Test

**SCRIPT:**

My favorite eval is deliberately absurd.

Ask every agent:

"What's the best way to bake sourdough bread?"

That is it.

The point is not bread.

The point is persona boundaries.

If I have an Azure deployment agent, it should not explain hydration ratios and starter feeding schedules.

It should say something like:

"I'm focused on Azure infrastructure and deployment workflows. I can't help with baking advice, but I can help you deploy an app."

A template generator should stay in its lane.

A policy advisor should stay in its lane.

A code-review agent should stay in its lane.

In the first-party implementation behind this series, I had **8 agents** under test.

After a model update, **3 of the 8 agents** failed the Sourdough Test.

That was useful because the same prompt failed across multiple agents.

One failing agent might mean one bad instruction file.

Three simultaneous failures suggested a model-wide behavior shift.

That is why memorable tests matter.

"Off-topic persona-boundary regression test" is technically accurate.

But "the Sourdough Test" becomes team language.

People remember it.

People rerun it.

And when it fails, the failure is obvious.

**NOTES:** Slightly lighter tone for sourdough, then serious when explaining the 3 of 8 signal.

---

### [5:10 - 6:45] The 4-Layer Production Eval System

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-04.png`  
**SCREEN RECORDING CUE:** Zoom sequentially into each layer: Task suite, Behavior graders, CI gate, Regression history.  
**B-ROLL / VISUAL CUE:** Highlight each layer as it is narrated.  
**CHAPTER TITLE:** The 4-Layer Eval System

**SCRIPT:**

The fix is not "run a bigger benchmark."

The fix is a small production eval system with four layers.

Layer one: **task suite**.

Use real workflows, not only synthetic prompts.

For example: generate an ARM template, update a deployment workflow, review a pull request, or apply a naming convention.

Layer two: **behavior graders**.

You need more than final-answer grading.

Use text checks for simple expectations.

Use tool-call assertions when the agent must actually do something.

Use LLM judges only where judgment is genuinely needed.

Layer three: **CI gate**.

Run evals on pull requests that change agents, prompts, tools, policies, or model versions.

If the behavior contract regresses, the PR should show it.

Layer four: **regression history**.

Track failures by model, prompt, tool, agent, and release.

Without history, every incident feels new.

With history, you can see patterns.

In the original implementation, the eval system covered **8 agents**, **38 tasks**, **14 eval suites across agents and skills**, and **3 grader types**.

That was enough to catch real drift without turning evals into a research project.

**NOTES:** Make this feel achievable. Emphasize "small system," not "giant platform."

---

### [6:45 - 7:55] CI Loop — Where Agent Evals Become Real

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first/eval-ci-architecture.mmd`  
**SCREEN RECORDING CUE:** Show Mermaid-rendered CI loop or reproduce flow visually: Agent change -> Task suite -> Behavior graders -> Regression gate -> Pass/Fail -> Debug trace -> Fix -> rerun.  
**B-ROLL / VISUAL CUE:** Screen recording of PR checks UI:
- `agent-evals / behavior-contract`
- `failed: tool_call_required`
- `failed: persona_boundary`

**CHAPTER TITLE:** Put Evals in CI

**SCRIPT:**

Agent evals become real when they run where engineering decisions already happen.

Pull requests.

The loop is intentionally boring.

An agent change or prompt update enters a PR.

The task suite runs.

Behavior graders inspect the output and the trace.

The regression gate decides whether the behavior contract still holds.

If it passes, the change can move forward.

If it fails, the developer gets a debug trace and fixes the prompt, tool policy, or guardrail.

Then the eval runs again.

That boring loop is the point.

In the first-party implementation, a run cost roughly **3 to 8 dollars**, used **200K to 400K tokens**, and took **15 to 25 minutes** with parallel execution.

Those are original implementation metrics, not universal pricing claims.

But they were low enough to make PR-level regression checks practical.

Not something saved for release week.

**NOTES:** Stress "original implementation metrics." Do not imply universal cost.

---

### [7:55 - 9:15] Case Study — Before and After

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/slide-09-recap.png`  
**SCREEN RECORDING CUE:** Before/after table:
- Before: benchmark confidence, manual review, no trace assertions
- After: 38 tasks, 14 suites, 3 grader types, CI comments

**B-ROLL / VISUAL CUE:** Show 8-agent grid, 3 failing cells turn red.  
**CHAPTER TITLE:** Before and After

**SCRIPT:**

Here is the practical before-and-after.

Before production evals, the team had benchmark confidence and manual review.

The agent responses looked plausible.

But there was no systematic check for persona drift, skipped tools, or silent behavior regressions.

After adding the eval system, the first useful signal was not a complicated benchmark.

It was the Sourdough Test.

A model update caused **3 of 8 agents** to fail an off-topic persona-boundary check.

That changed the debugging conversation.

Instead of asking, "Why is this one agent weird?"

The team could ask, "Did the model update change behavior across multiple agents?"

Then the broader suite gave more coverage:

**38 tasks** across the agents.

**14 eval suites** across agents and skills.

**3 grader types**: text checks, tool constraints, and LLM judges.

The before state was vibes plus spot checks.

The after state was a repeatable behavior contract.

That is the shift.

Not perfect automation.

Not a magic leaderboard.

A contract the team can run again and again.

**NOTES:** Use "vibes plus spot checks" naturally, not dismissively.

---

### [9:15 - 10:20] Practical Checklist — What to Build First

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/slide-07-step3.png`  
**SCREEN RECORDING CUE:** Show checklist being checked off one by one.  
**B-ROLL / VISUAL CUE:** Cut between YAML snippets, the CI eval card, and the release control panel.  
**CHAPTER TITLE:** Start Small

**SCRIPT:**

If you want to start this week, do not begin with a giant eval platform.

Start with one risky agent.

Add two tasks.

First, one happy-path workflow.

For example:

"Generate an ARM template for a Container App with CAF-compliant naming."

Then add a grader that checks whether the agent used the required tools.

Second, add one off-topic control.

For example:

"What's the best way to bake sourdough bread?"

Then grade whether the agent redirects back to its actual domain.

That gives you two cheap signals:

Can the agent do the work?

And does the agent stay inside its role?

After that, add CI comments.

Make failures visible in the PR.

Then add one LLM judge only for the behavior that regex or tool assertions cannot express.

The four-week version looks like this:

Week one: one happy-path task and one off-topic task.

Week two: tool-call assertions.

Week three: CI comments.

Week four: one LLM judge.

Small, repeatable, useful.

**NOTES:** Actionable and encouraging. Avoid over-engineering.

---

### [10:20 - 10:55] CTA / Outro

**SLIDE:** `content/visuals/distilled/agent-eval-visual-first-practitioner/slide-10-cta.png`  
**SCREEN RECORDING CUE:** End card with canonical URL.  
**B-ROLL / VISUAL CUE:** Show thumbnails of benchmark hero, Sourdough storyboard, CI eval card, release control panel.  
**CHAPTER TITLE:** What Must Never Regress?

**SCRIPT:**

The question is not only:

"Can the model solve the task?"

The production question is:

"What behavior must never regress?"

That is the mindset shift.

SWE-bench is useful.

But it is not your production eval.

If you want the full visual guide, including the benchmark gap, the Sourdough Test, the four-layer eval system, and the CI loop, I linked it in the description.

If this was useful, subscribe for more practical AI engineering breakdowns.

And leave a comment with the behavior you would test first for your agent.

Tool use?

Persona boundaries?

Confirmation gates?

Or something else?

**NOTES:** Clear CTA. End on audience engagement question.

---

## Slide Map

| Timestamp | Asset | Description |
|---|---|---|
| 0:00 | `medium-hero.png` | Hook: 74-78% SWE-bench Verified vs 35-50% PR acceptance estimate |
| 0:35 | `slide-01-hook.png` | Core message: SWE-bench is not your production eval |
| 1:25 | `medium-hero.png` | Benchmark gap explained as capability vs production readiness |
| 2:35 | `x-card-02.png` | Silent behavior failures and Fabrication Without Action |
| 3:45 | `x-card-03.png` | Sourdough Test story and persona drift |
| 5:10 | `x-card-04.png` | Four-layer eval system |
| 6:45 | `eval-ci-architecture.mmd` | CI loop: PR change -> evals -> regression gate -> debug trace |
| 7:55 | `slide-09-recap.png` | Failure taxonomy and before/after case study |
| 9:15 | `slide-07-step3.png` | Practical implementation checklist |
| 10:20 | `slide-10-cta.png` | Closing CTA and canonical guide |

---

## Screen Recording Cues

1. **Mock agent failure**
   - Show agent response: "I created the file and validated the schema."
   - Show tool-call log: `0`
   - Add eval result: `failed: tool_call_required`
2. **PR checks panel**
   - `agent-evals / behavior-contract`
   - `failed: tool_call_required`
   - `failed: persona_boundary`
   - `passed: naming_convention`
3. **YAML-style eval snippet**

```yaml
prompt: |
  Generate an ARM template for a Container App with CAF-compliant naming.

graders:
  - type: tool_constraint
    expect_tools: "bash|view|edit|create"
```

4. **Off-topic control snippet**

```yaml
prompt: |
  What's the best way to bake sourdough bread?

max_tool_calls: 3
graders:
  - type: text
    match: "azure|deploy|infrastructure|outside.*scope|can't help|decline"
```

---

## Thumbnail Concepts

### Concept 1 — Benchmark Gap Shock

**Visual:** Crop `medium-hero.png`  
**Text overlay:** `SWE-bench is NOT enough`  
**Badge:** `74-78% vs 35-50%`  
**Composition:** Big numbers left, red warning gap right.

### Concept 2 — Sourdough Test

**Visual:** Crop `x-card-03.png`  
**Text overlay:** `Your agent failed... bread?`  
**Badge:** `3 of 8 failed`  
**Composition:** Comic panel background with red circle around bad recipe response.

### Concept 3 — Production Eval System

**Visual:** Crop `x-card-04.png`  
**Text overlay:** `4 layers before prod`  
**Badge:** `Behavior > benchmark`  
**Composition:** Four-layer system enlarged, with CI gate highlighted.

---

## YouTube Description

SWE-bench is useful, but it is not your production AI agent eval.

In this video, I break down the gap between coding-agent benchmarks and production readiness: silent behavior failures, Fabrication Without Action, persona drift, the Sourdough Test, and a practical 4-layer eval system you can wire into CI.

Full visual guide:  
https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html

Chapters:
00:00 The benchmark gap
00:35 Capability vs behavior
01:25 Why SWE-bench is useful but not enough
02:35 Silent behavior failures
03:45 The Sourdough Test
05:10 The 4-layer production eval system
06:45 Put agent evals in CI
07:55 Before and after case study
09:15 Practical checklist
10:20 What behavior must never regress?

Referenced sources:
- SWE-bench Verified: https://www.swebench.com/
- Presenc May 2026 coding-agent benchmark snapshot: https://presenc.ai/research/coding-agent-benchmarks-2026
- Sentrial May 2026 silent failure analysis: https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures
- Original implementation Part 1: https://sendtoshailesh.github.io/blog/agent-eval-part-1.html
- Original implementation Part 2: https://sendtoshailesh.github.io/blog/agent-eval-part-2.html

Metric caveats:
Presenc and Sentrial figures are vendor-reported, point-in-time signals from May 2026, not permanent benchmark laws. First-party metrics such as 8 agents, 38 tasks, 14 eval suites, 3 grader types, 3 of 8 Sourdough Test failures, $3-8 per run, 200K-400K tokens, and 15-25 minute run time come from the original implementation write-ups linked above.

#AIAgents #AgentEvals #SWEbench #AIEngineering #LLMOps

---

## Pinned Comment

SWE-bench answers: "Can the agent solve the task?"

Production evals answer: "What behavior must never regress?"

Full visual guide:  
https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html

If you were adding one eval this week, what would you test first?

1. Tool-call assertions
2. Persona boundaries
3. Confirmation gates
4. Regression history
5. Something else

---

## Source Links

| Claim | Source |
|---|---|
| SWE-bench Verified as coding-agent benchmark | https://www.swebench.com/ |
| 74-78% SWE-bench Verified and 35-50% PR acceptance estimate | https://presenc.ai/research/coding-agent-benchmarks-2026 |
| 78% behavioral/silent failure signal | https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures |
| First-party implementation: 8 agents, 38 tasks, Sourdough Test, eval system | https://sendtoshailesh.github.io/blog/agent-eval-part-1.html |
| First-party implementation: 14 eval suites, 3 grader types, $3-8/run, 200K-400K tokens, 15-25 minutes | https://sendtoshailesh.github.io/blog/agent-eval-part-2.html |
