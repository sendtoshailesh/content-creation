---
description: "Show available GitHub Copilot models and explain the cross-model review constraint. Use when the user wants to understand model selection for the pipeline."
agent: "agent"
argument-hint: "Type 'list' to see available models"
---

Help me understand model selection for the content pipeline.

## Step 1: Explain the Model Selection Approach

This pipeline does NOT require a specific model. Select any model available in your VS Code Copilot model picker — all agents inherit your selection automatically.

The only constraint: **cross-model critic review** requires switching to a model from a different *family* (not a different version) before quality review. The pipeline auto-detects which family you used and prompts you to switch.

## Step 2: List Available Models

Check the VS Code Copilot model picker dropdown to see what's currently available. Models are grouped into three families:

| Family | Prefix | Use Any Model Starting With This |
|--------|--------|----------------------------------|
| Anthropic | `Claude` | Any Claude model |
| OpenAI | `GPT-*`, `o*` | Any GPT or o-series model |
| Google | `Gemini` | Any Gemini model |

## Step 3: Cross-Model Review

When the pipeline reaches quality review, it will ask you to switch families. For example:
- Created content with any Claude model → switch to any GPT/o-series or Gemini model for review
- Created content with any GPT model → switch to any Claude or Gemini model for review

This ensures adversarial diversity — different model families catch different blind spots.

Update the `content/pipeline-config.md` file with the chosen model. All pipeline agents read this config at startup and use the specified model via the chat picker.

Remind the user: to activate their choice, select the model in the VS Code Copilot model picker dropdown before running pipeline agents.
