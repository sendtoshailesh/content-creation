# YouTube Script — Part 2: Prompt Caching + Workflow Discipline

## Video Details

- **Target duration**: 8-10 minutes
- **Topic**: Invisible Compound Savings — Prompt Caching + Retry Tax
- **Source blog**: `content/ai-code-assistant-cost-part-2.md`
- **Published URL**: `https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html`

## Title Options

1. Stop Paying Twice: Prompt Caching for AI Code Assistants (Part 2)
2. The Hidden Retry Tax in GitHub Copilot Workflows (And How to Eliminate It)
3. 90% Token Savings? Prompt Caching Explained for Developers
4. AI Coding Cost Optimization Part 2: Caching + Workflow Discipline

## Description

── START COPY ──

Most developers optimize model selection first.

But Part 2 of this series covers two quieter levers that compound daily:
- prompt caching (75-90% cheaper repeated prefix tokens)
- retry-tax reduction through better workflow discipline

In this video:
- how caching works in real AI coding sessions
- the math behind a 10K-prefix workflow
- why vague prompts create a hidden 1.4x cost multiplier
- practical habits to improve first-attempt success

TIMESTAMPS:
0:00 - Why invisible savings matter
0:45 - What prompt caching actually caches
2:10 - The 10K-prefix math (1M -> 109K)
3:40 - How to maximize cache hits in day-to-day coding
5:00 - The retry tax and why “try again” is expensive
6:30 - Three workflow disciplines that reduce retries
8:00 - Action plan + link to Part 3

Part 2 of 3 in the "Engineering Better AI Code Assistant Interactions" series.

Blog post: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

#PromptCaching #GitHubCopilot #AIEngineering #DeveloperProductivity #ContextEngineering

── END COPY ──

## Thumbnail Concepts

1. **Split metric card**: Left "1,000,000 tokens", right "109,000 tokens", center badge "Part 2/3"
2. **Cost leak visual**: Funnel graphic with "Retry Tax 1.4x" label and red arrows
3. **Compounding theme**: "Set Once. Save Daily." with cache icon + VS Code panel screenshot

## Script

### [0:00 - 0:45] Cold Open

**SLIDE**: `prompt-structure-breakdown.png`  
**SCRIPT**: Most AI coding cost advice starts with model choice. That matters, but it’s not where most teams leak money first. In a typical coding session, roughly 90% of your prompt context repeats across requests — system prompt, project instructions, and active file context. If you pay full input rates every time for repeated context, you’re overspending silently. Today we’ll fix that with prompt caching and retry-tax discipline.

### [0:45 - 2:10] What Prompt Caching Does

**SLIDE**: `caching-flow.png`  
**SCRIPT**: Prompt caching stores repeated prompt prefixes so subsequent requests are billed at a reduced cached-input rate. Think of it as paying full price for processing stable context once, then paying a fraction when that same context appears again. Under modern usage-based billing, cached input is often 75 to 90 percent cheaper than regular input, depending on model and provider pricing.

### [2:10 - 3:40] The Math Developers Should Know

**SLIDE**: `caching-flow.png` (zoom on before/after request sequence)  
**SCRIPT**: Let’s run practical numbers. Suppose your stable prefix is 10,000 tokens and you make 100 requests in a workday. Without caching, that prefix costs you 1,000,000 full-price tokens. With caching, first write plus cached reads can bring the effective prefix spend down to around 109,000 token-equivalents. That’s about 89% savings on the repeated part of your prompts.

### [3:40 - 5:00] How to Maximize Cache Hits

**SLIDE**: `prompt-structure-breakdown.png`  
**SCRIPT**: You get cache savings only when the prefix stays stable. Three practical rules: one, keep your project instruction file stable during a session; don’t edit it every prompt. Two, keep related questions in one thread so the shared context remains reusable. Three, avoid unnecessary context churn — repeatedly adding and removing unrelated files can reduce cache match quality.

### [5:00 - 6:30] The Hidden Cost: Retry Tax

**SLIDE**: `retry-loop-anatomy.png`  
**SCRIPT**: Caching lowers the cost of good requests. But many teams still lose savings to retries. If 40% of prompts need clarification or correction, effective cost can rise to roughly 1.4x baseline. Every vague retry is not just another token bill — it also adds stale context to chat history, which can degrade the next answer and trigger even more retries.

### [6:30 - 8:00] Three Disciplines to Reduce Retries

**SLIDE**: `retry-tax-calculator.png`  
**SCRIPT**: First, one task per prompt. Don’t bundle unrelated asks. Second, diagnose before retrying — was the issue missing context, ambiguity, or wrong constraints? Third, write precise prompts with explicit file references and expected output. Cleaner prompts improve first-attempt success, and fewer retries means fewer wasted tokens.

### [8:00 - 9:00] Action Plan + Series Bridge

**SCRIPT**: Here’s your one-week action plan: stabilize your instruction baseline, group related questions in one thread, and track retry rate for at least three days. Aim to lower retries before changing models. Part 1 gave you context engineering fundamentals. Part 2 gave you caching and retry-tax control. Part 3 will cover model routing — exactly when premium models are worth their multiplier.

### [9:00 - 9:30] Close

**SCRIPT**: If this helped, share your current retry rate in the comments — most teams underestimate it. The full Part 2 article is linked in the description, and Part 3 is next.
