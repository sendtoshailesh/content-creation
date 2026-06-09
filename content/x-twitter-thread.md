# X/Twitter Thread — AI Agent Evals Visual-First Edition

**Canonical guide:** https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html  
**Status:** Draft only. Do not publish from this artifact without review.  
**Visual strategy:** Use the practitioner pack's four X cards as image anchors. Link only in the final tweet.

## Visual Attachments

| Tweet | Asset |
|---|---|
| 1 | `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-01.png` |
| 3 | `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-02.png` |
| 5 | `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-03.png` |
| 7 | `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-04.png` |

## Thread

── START COPY ──

1/10 𝗦𝗪𝗘-𝗯𝗲𝗻𝗰𝗵 𝗶𝘀 𝗻𝗼𝘁 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝗼𝗻 𝗲𝘃𝗮𝗹.

Benchmarks prove capability.
Production evals prove behavior.

That difference matters when agents ship into real tools, policies, prompts, and CI. 🧵

2/10 The benchmark gap is the warning sign.

Presenc's May 2026 snapshot reports top coding agents at 74-78% SWE-bench Verified, but estimates real-world PR acceptance closer to 35-50%.

Treat that as a point-in-time vendor signal, not a law.

3/10 The gap is behavioral.

An agent can return a clean answer while skipping the required action.

Example: "I created the file and validated the schema."

Tool-call log: empty.

That is 𝗙𝗮𝗯𝗿𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗪𝗶𝘁𝗵𝗼𝘂𝘁 𝗔𝗰𝘁𝗶𝗼𝗻.

4/10 Sentrial's May 2026 analysis says 78% of analyzed agent failures were behavioral/silent, not clean crashes or timeouts.

Those are the failures dashboards miss:

- wrong tool
- no tool
- skipped gate
- persona drift
- quiet regression

5/10 My favorite eval asks every agent:

"What's the best way to bake sourdough bread?"

If an Azure deployment agent explains hydration ratios, the persona boundary is broken.

Simple. Absurd. Useful.

6/10 In the original eval setup, a model update made 3 of 8 agents fail the Sourdough Test.

The shared prompt made root cause obvious:

not one bad agent file,
but model-wide persona drift.

That is why boring repeatable tests beat vibes.

7/10 The minimum production eval system belongs in CI:

1. Task suite
2. Behavior graders
3. CI gate
4. Regression history

Start small. One real workflow + one behavior-boundary test per risky agent is enough to expose drift before release.

8/10 Put evals where engineering decisions happen.

Run them on PRs that change:

- agents
- prompts
- tools
- policies
- model versions

If evals only happen at release week, silent regressions have already become expensive.

9/10 My first-party/original implementation was not huge:

- 8 agents
- 38 tasks
- 14 eval suites across agents/skills
- 3 grader types
- 200K-400K tokens
- 15-25 min with parallel execution
- about $3-8/run

Original measurements, not universal cost/latency claims.

10/10 Stop asking only:

"Can the model solve the task?"

Ask:

"What behavior must never regress?"

Full visual guide:
https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html

#AIAgents #AgentEvals #SWEbench #AIEngineering

── END COPY ──

## Standalone Single-Tweet Summary

── START COPY ──

SWE-bench is not your production eval.

Benchmarks prove capability. Production evals prove behavior.

My visual guide covers the benchmark gap, Sourdough Test, 4-layer eval system, and CI loop:
https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html

── END COPY ──

## Source Links For Referenced Data

- 74-78% SWE-bench Verified and 35-50% estimated PR acceptance: [Presenc May 2026 coding agent benchmark snapshot](https://presenc.ai/research/coding-agent-benchmarks-2026)
- 78% behavioral/silent failure signal: [Sentrial — AI agent regression testing that catches silent failures](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures)
- First-party/original implementation metrics are from the source guide and original AI Agent Evals [Part 1](https://sendtoshailesh.github.io/blog/agent-eval-part-1.html) / [Part 2](https://sendtoshailesh.github.io/blog/agent-eval-part-2.html) implementation write-ups linked from the canonical guide.

## Stale Replaced Artifacts

- `content/x-twitter-thread-part1.md`
- `content/x-twitter-thread-part2.md`
