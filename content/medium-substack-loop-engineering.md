---
title: "You're Not Getting Better at Prompting — The Skill Moved"
subtitle: "Prompt → context → harness → loop: why the unit of work you own keeps climbing, and three projects to feel it for yourself this week."
canonical_url: https://sendtoshailesh.github.io/content-creation/blog/loop-engineering-ai-native-development.html
source_blog: content/from-prompts-to-loop-engineering.md
platforms: [Medium, Substack, LinkedIn Article]
status: draft
---

<!-- One unified distilled excerpt for Medium, Substack, and LinkedIn Article. -->
<!-- Copy the same content to all three. Every platform's canonical link points to the GitHub Pages URL above. -->
<!-- Voice: first-person practitioner. Avoid corporate filler verbs. -->

> **Originally published at [sendtoshailesh.github.io](https://sendtoshailesh.github.io/content-creation/blog/loop-engineering-ai-native-development.html).** This is the distilled version — the full post has the data exhibits, the source links, and the worked example.

You're not getting better at prompting. I mean that as a relief, not an insult.

For a while I treated prompting like a craft to perfect — the right persona, the right few-shot examples, the right chain-of-thought nudge. Then I noticed the people shipping the most real software with agents had quietly stopped optimizing the sentence. They were optimizing everything around it. The skill didn't get better. It moved.

It moves up a staircase with four steps, and each one automates the floor below it:

- **Prompt engineering** — the wording of one request. The ceiling: you can phrase it perfectly and still get a confident answer to the wrong problem.
- **Context engineering** — what the model sees: your conventions, your architecture, lazy-loaded skills. The ceiling: a well-fed model still can't *act*.
- **Harness engineering** — everything around the model. The VS Code team's own framing: context assembly + tool exposure + tool execution — the CLIs, the test suite, the type checker, the guardrails. "The model is the engine; the harness is the car." The ceiling: a rig still needs a cycle to run in.
- **Loop engineering** — the cycle itself: plan → act → observe → verify → correct, with a stop condition that decides when it's done.

Every two years, the place where your effort actually matters climbs one step higher, because the model keeps absorbing the work beneath you.

## Why the loop, and why now

Code generation got cheap. That single fact inverts the bottleneck: it's no longer generation, it's *validation*. By the time conventional CI finds the bug, the agent has already moved on and lost the context. So the durable move is to pull verification *inside* the cycle — to make the loop check its own work and know when to stop.

The proof that this scales isn't hypothetical. At industry scale, Stripe's autonomous agents ship 1,300+ pull requests a week with zero human-written code, behind more than $1T in annual payment volume. And you don't have to take it on faith — several production loops are open enough to read end to end: **mini-swe-agent**, **Aider**, and **Azure/git-ape** (an MIT-licensed agentic deploy loop: plan → PR → deploy, with security and cost gates as the sensors and CI/OIDC as the bounded run). SWE-bench Verified climbed from 12.47% (Mar 2024) to 76.8% (Feb 2026) — but treat that as illustration, not a scoreboard: the scores increasingly reflect the *harness*, which is why OpenAI stopped reporting it.

One distinction took me too long to see: the **harness** and the **loop** are not the same thing. The VS Code team put it plainly — "the harness is the product" — and even tune theirs per model. The harness is nouns: the assembled parts and the sensors. The loop is verbs: the act → observe → verify → retry cycle that uses them. Here's the one diagnostic I now run on every team: when you don't like what the agent produced, do you fix the *output* (that's editing), or do you change the thing that *produced* it — the rig and the cycle (that's engineering)? The whole shift is from fixing the artifact to fixing the producer.

## Build it yourself: 3 projects to try this week

Reading about loops doesn't build the instinct — closing one does. So here are three starting points that ladder from an afternoon to a weekend. Each one names a few interchangeable tools — pick whichever you already have access to; none is required. Do the first one and "plan → act → observe → verify → correct" stops being a diagram and becomes muscle memory.

1. **Beginner — run a verify→correct loop in an agent.** Give it a task with a failing test and watch it edit → run tests → read failures → retry on its own (in Copilot, the **Chat Debug View** shows the prompts and tool calls behind the run). **Success signal:** your test command exits 0 on an edit you didn't write. **~90 minutes.** **Tools (pick one):** [VS Code / Copilot agent mode](https://code.visualstudio.com/docs/agents/overview), [Aider](https://github.com/Aider-AI/aider), or Claude Code.

2. **Intermediate — build the loop on a managed runtime.** Stand up an agent + conversation + one tool, run it in background mode, and make a capped iteration count your stop condition. **Success signal:** a seeded task is resolved within the iteration cap — and the run exits cleanly at the cap when it can't. **Half a day.** **Tools (pick one):** [Foundry hosted-agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent) or [Anthropic's `patterns/agents`](https://github.com/anthropics/claude-cookbooks) — the loop is identical either way.

3. **Advanced — platform-engineer the loop with gates.** Run a headless deploy loop (issue → PR → plan → security/cost gate → deploy), then tighten a gate and re-run to change the outcome. **Success signal:** a tuned gate visibly changes what the loop does. **A weekend.** **Tools (pick one):** [Azure/git-ape](https://github.com/Azure/git-ape), [microsoft/hve-core](https://github.com/microsoft/hve-core), or [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent).

Start with Project 1 this week. Once you've watched a test suite close a loop you didn't babysit, you stop reaching for the next prompt trick and start reaching for the next sensor.

So locate your step on the staircase — word, context, rig, or loop — and take the next one. Right now, that unit is the loop. Go ship one with a stop condition.

---

**Read the full breakdown** — with the data exhibits, the four postures around the loop, the failure modes worth budgeting for, the full source list (from VS Code's agent-loop and harness posts, Stripe and Anthropic's production patterns, and open frameworks like Azure/git-ape, to the practitioners who named the arc — Willison, Böckeler, Morris):
**[sendtoshailesh.github.io/content-creation/blog/loop-engineering-ai-native-development.html](https://sendtoshailesh.github.io/content-creation/blog/loop-engineering-ai-native-development.html)**
