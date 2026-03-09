---
description: "List available GitHub Copilot models and help choose the best one for content creation. Use when setting up the pipeline or changing model preferences."
agent: "agent"
argument-hint: "Type 'list' to see available models, or describe your quality/speed preference"
---

Help me choose the right model for my content pipeline.

## Step 1: Detect Available Models

Check which models are currently available in my GitHub Copilot setup by reading the VS Code Copilot model picker. The models generally available include:

**Flagship / Highest Quality:**
- Claude Sonnet 4 — Strong technical writing, nuanced reasoning
- Claude Sonnet 4.5 — Enhanced creative + analytical
- GPT-4.1 — Strong general purpose, good at structured output
- GPT-4o — Multimodal, fast reasoning
- Gemini 2.5 Pro — Long context, strong analytical

**Fast / Cost-Efficient:**
- Claude Haiku 3.5 — Fast, good for simple tasks
- GPT-4o mini — Fast, lightweight
- GPT-4.1 mini — Budget-friendly
- GPT-4.1 nano — Fastest, most lightweight

**Reasoning / Deep Analysis:**
- o3 — Deep reasoning for complex analysis
- o4-mini — Reasoning at lower cost
- Claude Sonnet 4 (Extended Thinking) — Extended chain-of-thought

## Step 2: Recommend for Content Pipeline

Based on the user's preference (quality vs. speed), recommend a model and update `content/pipeline-config.md` with the selection.

**For highest content quality:** Claude Sonnet 4 or GPT-4.1
**For faster iteration:** GPT-4o or Claude Haiku 3.5
**For deep research/analysis:** o3 or Claude Sonnet 4 (Extended Thinking)

## Step 3: Apply Selection

Update the `content/pipeline-config.md` file with the chosen model. All pipeline agents read this config at startup and use the specified model via the chat picker.

Remind the user: to activate their choice, select the model in the VS Code Copilot model picker dropdown before running pipeline agents.
