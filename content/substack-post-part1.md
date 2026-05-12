# Substack Post — Part 1: Context Engineering

> Platform: Substack
> Post type: Substack Note (NOT newsletter/email — ambient feed only)
> Word count: ~420 words (excerpt only — avoid duplicate content penalty)
> Canonical source: https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html

── START COPY ──

Last November, Anthropic stripped 85% of the context from their tool-use system.

Accuracy improved from 49% to 74%.

They removed context, and the model got better. That is the counterintuitive finding at the center of context engineering — the most underrated skill in AI-assisted development.

---

30-70% of typical AI prompt context is noise. Not neutral overhead — actively harmful tokens that push the model toward hallucination, hedging, and irrelevant output.

In a code assistant workflow, this noise has three forms:

- Stale context: open files from a previous task, chat history from a different feature
- Redundant context: the same file referenced through multiple paths
- Irrelevant context: tool definitions, browser tabs, config files that have nothing to do with what you're building

The SWEzze paper compressed code assistant context 6x and measured the outcome: 51-71% fewer tokens AND 5-9.2% better issue resolution rates. Less input. Better output. In every study.

---

Five practices that fix this — each passes the test of "would I do this even if AI were free?":

1. Close all unrelated files before prompting. Every irrelevant file is a dilution.

2. One thread per task. Old chat messages steer the model toward solved problems you've already moved past.

3. Use explicit #file references instead of implicit open-files context.

4. Front-load your intent. First sentence: what you want. Then context. Then constraints. Models read sequentially.

5. Maintain a stable .github/copilot-instructions.md. Consistent instructions = consistent, cacheable context.

These are not hacks. They are the same habits that make good engineers good communicators: clarity, precision, no unnecessary noise.

---

The timing matters. GitHub Copilot moves to usage-based billing on June 1, 2026 — every token now has a visible price tag. Context engineering was worth doing before. Now it shows up on your bill.

But I would do all five of these practices if AI were free. Better context produces better output. The cost savings are a side effect.

Full breakdown with data tables and per-practice action steps: https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html

Part 2: how prompt caching compounds these savings silently across every session.
Part 3: the 120x model cost spread and how to route tasks to the right model.

── END COPY ──
