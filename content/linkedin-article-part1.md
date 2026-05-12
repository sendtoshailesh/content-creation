# LinkedIn Article — Part 1: The Hidden Context Problem

> Platform: LinkedIn Article (Google-indexed, no canonical protection)
> Angle: UNIQUE — "The Hidden Cost of Open Files" (decision-making for tech leads/managers)
> NOT a republish of the blog — this is a different entry point and frame
> Word count: ~780 words
> Canonical blog: https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html

── START COPY ──

# Your AI Code Assistant Doesn't Have a Model Problem. It Has a Context Problem.

I keep hearing the same conversation in engineering teams right now.

Developer: "Copilot gave me garbage output on that refactor."
Tech Lead: "Did you use GPT-4o or the newer model?"

The conversation is about model choice. It should be about context.

I've been working with engineering teams on GitHub Copilot adoption — helping them get consistent, reliable output from AI code assistants. The single variable that predicts output quality most reliably is not which model you use. It is what you send to that model.

Here is the uncomfortable truth: 30-70% of typical AI prompt context is noise. Not neutral overhead — actively harmful tokens that push the model toward hallucination, hedging, and off-target output. The model is not confused because it is underpowered. It is confused because you gave it too much information, most of which was irrelevant.

---

## The Anthropic Lesson

Last November, Anthropic's engineering team ran into this problem at scale. Their tool-use system was loading 50+ MCP tool definitions into every prompt — up to 134,000 tokens before the conversation started.

Their fix: they stripped it out. They built a system that loads only ~500 tokens initially and fetches relevant definitions on demand. Result: 85% fewer tokens AND accuracy improved from 49% to 74% on Opus 4. On Opus 4.5, accuracy jumped from 79.5% to 88.1%.

This is not an isolated case. SWEzze, a context compression system for software engineering tasks, showed that 6x compression delivered 51-71% fewer tokens AND 5-9.2% better issue resolution rates. Multiple independent research teams have found the same pattern: less context, better output.

---

## What This Means for Your Team

When a developer complains that Copilot is giving poor results, the instinct is to suggest a better model. But the evidence points elsewhere.

The most common causes of poor AI code assistant output are:

Too many files open. Every file in the editor adds tokens to Copilot's context window. Files from other tasks introduce conflicting patterns — the model tries to reconcile your current request with code from a different feature you were working on two hours ago.

Stale thread history. Chat messages from earlier in a session accumulate in context. Old questions about authentication logic steer the model toward solved problems when you've moved on to building something different.

Generic prompts. When the model doesn't receive clear intent in the first sentence, it forms hypotheses from the surrounding context — and those hypotheses are often wrong, triggering retries.

Missing project instructions. Without a .github/copilot-instructions.md file, the model guesses at your tech stack, conventions, and constraints — and guesses differently each time.

---

## The Five Practices

I've been teaching five context engineering practices to every team I work with. Each passes a simple test: is this worth doing even if AI were free?

1. Single-task focus: close all files unrelated to your current task before prompting. Two seconds of file management, measurable improvement in output focus.

2. Thread hygiene: one thread per task. When you start a new feature, open a fresh thread. Old context does not just waste tokens — it steers the model toward problems you've already solved.

3. Targeted references: use #file:path references instead of relying on implicit open-files context. Tell the model exactly which file matters.

4. Front-loaded intent: state what you want in the first sentence. Intent first, context second, constraints third. Language models process sequentially — lead with what you need.

5. Stable instructions: maintain a .github/copilot-instructions.md with your project's tech stack, conventions, and constraints. Keep it under 200 lines. This file also enables prompt caching (detailed in Part 2 of my series), reducing the token rate by 75-90% on repeated context.

---

## The Framing That Changes Everything

Here is how I encourage tech leads to frame this with their teams: context engineering is the same skill that makes engineers good communicators. Clarity. Precision. No unnecessary noise.

The developer who writes a clear bug report, provides relevant reproduction steps, and states the expected behavior explicitly — that developer gets faster resolution than the one who says "it's broken, figure it out." Context engineering is that same discipline applied to AI interactions.

The irony: the developers who instinctively write clean code, clear commit messages, and precise documentation are already halfway there. They understand that clear input produces better output. They just haven't applied it to their AI interactions yet.

---

For the full data, scenarios, and step-by-step practices: https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html

Part 2 covers the compound savings from prompt caching and retry elimination. Part 3 covers the 120x model cost spread.

── END COPY ──
