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
- **Harness engineering** — everything around the model. The rig: the CLIs, the test suite, the type checker, the guardrails. A ~100-line harness (mini-SWE-agent) resolves a meaningful share of SWE-bench Verified tasks. The ceiling: a rig still needs a cycle to run in.
- **Loop engineering** — the cycle itself: plan → act → observe → verify → correct, with a stop condition that decides when it's done.

Every two years, the place where your effort actually matters climbs one step higher, because the model keeps absorbing the work beneath you.

## Why the loop, and why now

Code generation got cheap. That single fact inverts the bottleneck: it's no longer generation, it's *validation*. By the time conventional CI finds the bug, the agent has already moved on and lost the context. So the durable move is to pull verification *inside* the cycle — to make the loop check its own work and know when to stop.

The proof that this scales isn't hypothetical. Stripe's autonomous agents ship 1,300+ pull requests a week with zero human-written code, behind more than $1T in annual payment volume. And on a *fixed* harness — same infrastructure, model swapped underneath — SWE-bench Verified climbed from 12.47% (Mar 2024) to 76.8% (Feb 2026). The harness held still; the trajectory came from owning the loop and the model inside it. (The per-task cost band, ~$0.05–$0.96, is still subsidized — worth re-pulling before you budget on it.)

One distinction took me too long to see: the **harness** and the **loop** are not the same thing. The harness is nouns — the equipment. The loop is verbs — the cycle that uses it. Here's the one diagnostic I now run on every team: when you don't like what the agent produced, do you fix the *output* (that's editing), or do you change the thing that *produced* it — the rig and the cycle (that's engineering)? The whole shift is from fixing the artifact to fixing the producer.

## Build it yourself: 3 projects to try this week

Reading about loops doesn't build the instinct — closing one does. So here are three real, open-source starting points that ladder from an afternoon to a weekend. Do the first one and "plan → act → observe → verify → correct" stops being a diagram and becomes muscle memory.

1. **Beginner — run your first verify→correct loop with Aider.** Point it at a repo with a test suite and let it iterate on its own: `aider --test-cmd "pytest -q" --auto-test`. **Success signal:** `pytest` exits 0 on a change the model made while you wrote no code. **~90 minutes.** Start from [Aider-AI/aider](https://github.com/Aider-AI/aider).

2. **Intermediate — build the loop yourself.** Write a ~150-line plan → act → observe → verify → correct cycle where *you* own the stop condition, using Anthropic's agent patterns and a test runner as the verifier. **Success signal:** a seeded bug is fixed within the retry budget — and the loop exits non-zero (no infinite loop) when it can't. **Half a day.** Start from [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) (`patterns/agents`).

3. **Advanced — close the loop on real GitHub issues and measure it.** Run mini-SWE-agent on a small SWE-bench subset in a sandbox and compute your own resolve-rate and cost-per-issue. **Success signal:** a results file shows at least one issue resolved by a passing patch, plus a concrete cost figure. **A weekend.** Start from [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent).

Start with Project 1 this week. Once you've watched a test suite close a loop you didn't babysit, you stop reaching for the next prompt trick and start reaching for the next sensor.

So locate your step on the staircase — word, context, rig, or loop — and take the next one. Right now, that unit is the loop. Go ship one with a stop condition.

---

**Read the full breakdown** — with the data exhibits, the four postures around the loop, the failure modes worth budgeting for, and the practitioners who named the arc (Willison, Böckeler, Morris, Anthropic):
**[sendtoshailesh.github.io/content-creation/blog/loop-engineering-ai-native-development.html](https://sendtoshailesh.github.io/content-creation/blog/loop-engineering-ai-native-development.html)**
