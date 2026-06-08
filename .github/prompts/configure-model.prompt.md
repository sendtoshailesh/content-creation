---
description: "Show available GitHub Copilot models and explain the rubber-duck review gate. Use when the user wants to understand model selection for the pipeline."
agent: "agent"
argument-hint: "Type 'list' to see available models"
---

Help me understand model selection for the content pipeline.

## Step 1: Explain the Model Selection Approach

This pipeline does NOT require a specific model. Select any model available in your VS Code Copilot model picker — all agents inherit your selection automatically.

There is no model-family switching requirement for reviews. Review gates use GitHub Copilot's **rubber-duck review** feature for adversarial critique, then specialized reviewers apply fixes and fact checks.

## Step 2: List Available Models

Check the VS Code Copilot model picker dropdown to see what's currently available. Models are grouped into three families:

| Family | Prefix | Use Any Model Starting With This |
|--------|--------|----------------------------------|
| Anthropic | `Claude` | Any Claude model |
| OpenAI | `GPT-*`, `o*` | Any GPT or o-series model |
| Google | `Gemini` | Any Gemini model |

## Step 3: Rubber-Duck Review

When the pipeline reaches quality review, it runs rubber-duck review without asking you to switch model families.

This keeps the review gate adversarial while avoiding model-picker interruptions.

Update the `content/pipeline-config.md` file with the chosen model. All pipeline agents read this config at startup and use the specified model via the chat picker.

Remind the user: to activate their choice, select the model in the VS Code Copilot model picker dropdown before running pipeline agents.
