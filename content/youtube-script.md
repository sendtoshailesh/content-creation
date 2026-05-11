# YouTube Script — Part 1: Context Engineering for AI Code Assistants

## Video Details

- **Target duration**: 8-10 minutes
- **Topic**: Spend Fewer Tokens, Get Better Code — Context Engineering Guide
- **Source blog**: `content/context-engineering-part-1.md`

## Title Options

1. Anthropic Cut AI Context by 85% — Accuracy IMPROVED (Here's How)
2. 5 Context Engineering Practices That Make AI Code Assistants Actually Work
3. Why Less Context = Better AI Code Output (Data-Backed Guide)
4. Stop Wasting Tokens: Context Engineering for GitHub Copilot

## Description

── START COPY ──

Anthropic's engineering team cut tool context by 85% and accuracy jumped from 49% to 74%. Less context, better output.

In this video, I cover five context engineering practices that make your AI code assistant (GitHub Copilot, Cursor, etc.) produce better results while spending fewer tokens. Every practice passes one test: would I do this even if AI were free?

TIMESTAMPS:
0:00 - The Counterintuitive Truth
0:30 - The 30-70% Problem
2:00 - Practice 1: Single-Task Focus
3:00 - Practice 2: Thread Hygiene
4:00 - Practice 3: Targeted References
5:00 - Practice 4: Front-Load Intent
6:00 - Practice 5: Stable Instructions
7:00 - The Data: Three Scenarios
8:30 - June 2026 Billing Change
9:30 - Your First Week Action Plan

KEY DATA POINTS:
- 85% token reduction, 49% to 74% accuracy (Anthropic Tool Search)
- 6x compression, 5-9% better issue resolution (SWEzze)
- 37% token reduction, improved knowledge retrieval (Programmatic Tool Calling)
- 30-70% of typical AI context is noise (TDS research)

Part 1 of 3 in the "Engineering Better AI Code Assistant Interactions" series.

Blog post: [link]

#AICodeAssistant #ContextEngineering #GitHubCopilot #DeveloperProductivity

── END COPY ──

## Thumbnail Concepts

1. **Split screen**: Left side cluttered code editor (red tint), right side clean editor (green tint). Text: "85% LESS → 50% BETTER"
2. **Data callout**: Large "49% → 74%" with subtext "Less context. Better output." Anthropic logo subtle in corner
3. **Contrarian hook**: "REMOVE context to IMPROVE AI" crossed-out brain icon with upward arrow

## Script

### [0:00 - 0:30] Cold Open

**SLIDE**: context-quality-paradox.png
**SCRIPT**: Last November, Anthropic's engineering team had a problem. They were loading 50 plus MCP tool definitions into every prompt — that's 134,000 tokens before the conversation even started. Their fix? They stripped it out. Loaded only 500 tokens initially. The result: 85 percent fewer tokens AND accuracy jumped from 49 to 74 percent. They removed context and the model got better. Let me show you why.
**NOTES**: Fast pace, emphasize the paradox. Pause briefly after "the model got better."

### [0:30 - 2:00] The 30-70% Problem

**SLIDE**: context-noise-breakdown.png
**SCRIPT**: Research found that 30 to 70 percent of typical AI prompt context is noise. Not neutral overhead — active noise that degrades performance. In code assistant workflows, this noise falls into three buckets. First, stale context: open files from a previous task, old chat messages about a different feature. The model tries to reconcile all of it with your current request. Second, redundant context: the same file loaded through multiple paths. You opened it, it's referenced in chat, and a tool reads it again. Third, irrelevant context: tool definitions for tools you'll never call, project config files that have nothing to do with your code. Every irrelevant file dilutes the model's attention on what you actually need.
**NOTES**: Use hand gestures for "three buckets." Point to visual for each category.

### [2:00 - 3:00] Practice 1: Single-Task Focus

**SLIDE**: context-engineering-framework.png
**SCRIPT**: Practice one: single-task focus. Close files unrelated to your current task before prompting. If you have 12 files open in VS Code and ask Copilot about one of them, the other 11 are noise. Anthropic saw accuracy jump 25 percentage points just by loading only relevant tool definitions. Same principle applies to your files. Fewer, more relevant files produce better suggestions. Before your next Copilot interaction, close everything except what you're working on right now.
**NOTES**: Show VS Code tab bar with many tabs, then close most.

### [3:00 - 4:00] Practice 2: Thread Hygiene

**SCRIPT**: Practice two: thread hygiene. Start a new chat thread when you switch tasks. Chat history accumulates tokens across every message. If you asked about authentication logic 20 messages ago and now you're working on pagination, those old messages are still in context. The model tries to reconcile them. One thread per task. Takes two seconds. Gives the model a clean slate.
**NOTES**: Demonstrate opening new chat in VS Code.

### [4:00 - 5:00] Practice 3: Targeted References

**SCRIPT**: Practice three: targeted references. Use hash-file references to include specific files instead of relying on implicit context. When you type a prompt in Copilot Chat, the model receives context from your open files, your chat history, and any explicit references. By pointing to a specific file, you tell the model exactly what matters. Anthropic's Programmatic Tool Calling reduced tokens by 37 percent while improving accuracy. Targeted input beats broad input every time.
**NOTES**: Show #file autocomplete in VS Code.

### [5:00 - 6:00] Practice 4: Front-Load Intent

**SCRIPT**: Practice four: front-load intent. State what you want in the first sentence, then provide details. Language models process context sequentially. The first tokens prime the model's attention. If you bury your intent after three paragraphs of background, the model is already forming hypotheses. Lead with the goal. "Add cursor-based pagination to this endpoint with default page size 50." Intent first. Context second. Constraints third.
**NOTES**: Show good vs bad prompt structure side by side.

### [6:00 - 7:00] Practice 5: Stable Instructions

**SCRIPT**: Practice five: stable instructions. Create a copilot-instructions.md file in your repo with your tech stack, conventions, and constraints. Without it, you repeat the same context in every prompt: "we use TypeScript," "follow the existing pattern." Each repetition costs tokens and introduces variation. A stable instructions file provides consistent project context automatically. It also enables prompt caching, which I'll cover in Part 2 — up to 90 percent discount on repeated context.
**NOTES**: Show example copilot-instructions.md file.

### [7:00 - 8:30] The Data: Three Scenarios

**SLIDE**: before-after-context.png
**SCRIPT**: Let me give you the data across three independent studies. Scenario A: Anthropic's Tool Search — 85 percent token reduction, accuracy jumped from 49 to 74 percent on Opus 4, and from 79.5 to 88.1 on Opus 4.5. Scenario B: SWEzze context compression — 6x compression, 51 to 71 percent fewer tokens, AND 5 to 9 percent better issue resolution. Scenario C: Programmatic Tool Calling — 37 percent fewer tokens, improved knowledge retrieval. The pattern is unambiguous. In every scenario, less context produced better results. The model is not losing information when you remove noise. It is gaining clarity.
**NOTES**: Point to each row in the comparison table. Emphasize "every scenario."

### [8:30 - 9:30] June 2026 Billing Change

**SLIDE**: model-multiplier-spectrum.png
**SCRIPT**: One more reason this matters now. Starting June 1, 2026, GitHub Copilot moves to usage-based billing. Every token of junk context will have a visible cost on your bill. But I want to be clear: every practice in this video is worth doing even if AI were completely free. They make your output better. The cost savings follow naturally. Build your workflow around context quality, which is durable. Not around specific pricing, which changes.
**NOTES**: Don't dwell on pricing specifics. Emphasize quality-first.

### [9:30 - 10:00] Your First Week + CTA

**SCRIPT**: Here's your action plan for this week. Monday: close irrelevant files before every prompt. Tuesday: start new threads when switching tasks. Wednesday: use hash-file references instead of broad context. Thursday: create a copilot-instructions.md for your main project. Friday: front-load intent in every prompt. Five days, five minutes each. You'll notice better first-attempt output within the week. This is Part 1 of 3. Part 2 covers prompt caching and workflow discipline. Part 3 covers the 120x model cost spread. Subscribe so you don't miss them. Drop a comment with your best context engineering tip. I'll see you in Part 2.
**NOTES**: Count on fingers for each day. End with genuine enthusiasm.

## Slide Map

| Timestamp | Visual | Description |
|-----------|--------|-------------|
| 0:00 | context-quality-paradox.png | Anthropic 49% to 74% accuracy with 85% less context |
| 0:30 | context-noise-breakdown.png | Three categories of context noise |
| 2:00 | context-engineering-framework.png | Five practices overview |
| 7:00 | before-after-context.png | Three scenarios comparison table |
| 8:30 | model-multiplier-spectrum.png | Model multiplier range and billing context |

## Tags

AI code assistant, context engineering, GitHub Copilot, developer productivity, AI tokens, prompt engineering, Anthropic, MCP tools, usage-based billing, coding tips
