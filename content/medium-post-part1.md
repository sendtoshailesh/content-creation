# Medium Post — Part 1: Context Engineering

> Platform: Medium
> Import URL: https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html
> Action: Use Medium's Import tool (Settings > Import a story) — do NOT paste. This preserves canonical attribution to GitHub Pages.
> Word count: ~800 words

── START COPY ──

# Spend Fewer Tokens, Get Better Code: The Context Engineering Guide for AI Code Assistants

Last November, Anthropic's engineering team ran into a problem. Their tool-use system was loading 50+ MCP tool definitions into every prompt — up to 134,000 tokens of context before the conversation even started.

Their fix was counterintuitive: they stripped it out. They built Tool Search, which loads only ~500 tokens initially and fetches relevant definitions on demand. The result: 85% fewer tokens AND accuracy improved from 49% to 74% on Opus 4.

Read that again. They removed context and the model got better.

I've been working with enterprise teams on AI code assistant adoption, and this pattern shows up everywhere. Some sessions, Copilot generates exactly what you need on the first try. Other sessions, it produces confused, irrelevant output. The difference is almost never the model. It's the context.

---

## The 30-70% Problem

Research from Towards Data Science found that 30-70% of typical AI prompt context is noise — tokens that don't help the model and actively degrade performance. In code assistant workflows, context noise falls into three categories:

Stale context: open files from a previous task, old chat messages about a different feature. The model treats all of it as relevant input and tries to reconcile it with your current request.

Redundant context: the same information loaded through multiple paths — explicit file content, a chat reference to the same file, and a tool definition that reads it again.

Irrelevant context: tool definitions for tools you'll never call, files that happen to be open from earlier browsing, configuration files that have nothing to do with the code you're writing.

The SWEzze paper put concrete numbers on this: compressing context 6x delivered 51-71% fewer tokens AND 5-9.2% better issue resolution rates. Less input. Better output.

This is not a trade-off. It's a free lunch.

---

## Five Practices That Fix the Problem

Each practice below passes a simple test: would I do this even if AI were free? The answer is yes for all five. They make you more effective. The token reduction is a bonus.

**1. Single-Task Focus**

Close files unrelated to your current task before prompting. Every open file in your editor adds tokens to Copilot's context — and more importantly, introduces conflicting patterns. If you're working on an API endpoint and have a database migration file open from earlier, the model receives mixed signals. Anthropic saw accuracy jump 25 percentage points (49% to 74%) just by loading only relevant tool definitions. The same principle applies to files.

**2. Thread Hygiene**

Start a new chat thread when you switch tasks. Chat history accumulates tokens across every message. If you asked about authentication logic 20 messages ago and now you're working on pagination, those messages are still in context — actively steering the model toward stale problems. One thread per task. It takes two seconds and gives the model a clean slate.

**3. Targeted References**

Use #file references to include specific files instead of relying on "everything that is open." When you type a prompt in Copilot Chat, the model receives context from your open files and chat history. By using #file:path/to/specific-file.ts, you tell the model exactly which file matters. High signal, low noise.

**4. Front-Load Intent**

State what you want in the first sentence, then provide details. Language models process context sequentially. If you bury your intent after three paragraphs of background, the model forms hypotheses before it knows what you want. Structure prompts as: intent, then context, then constraints.

**5. Stable Instructions**

Maintain a .github/copilot-instructions.md file with your project's tech stack, conventions, and constraints. Without it, you repeat the same context in every prompt — costing tokens and introducing variation that can confuse the model. With it, the model starts every interaction with accurate project context. And as you'll see in Part 2, a stable instructions file enables prompt caching, which reduces the token rate by 75-90% on repeated context.

---

## The Pattern Is Consistent

Three independent data points converge on the same conclusion:

Anthropic Tool Search: 85% fewer tokens, accuracy +25 percentage points (Opus 4).
SWEzze compression: 51-71% fewer tokens, issue resolution +5-9.2%.
Anthropic Programmatic Tool Calling: 37% fewer tokens, accuracy +2.9 percentage points.

In every scenario, less context produced better results. The model isn't losing information when you remove noise. It's gaining clarity.

The highest-leverage skill for AI-assisted development isn't prompt engineering. It isn't model selection. It's giving AI better input. The quality improvement is the primary goal. The cost savings — and with GitHub Copilot moving to usage-based billing on June 1, 2026, those savings are real — are a natural consequence.

---

Full article with data tables, scenario breakdowns, and visual references: https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html

Part 2 covers prompt caching (75-90% reduced rate on repeated context) and the retry tax. Part 3 covers the 120x model cost spread and how to route tasks to the right model.

── END COPY ──
