# Content Pipeline Configuration

> **Edit this file** to configure your content pipeline preferences. All pipeline agents read this config before starting work.

---

## Pipeline Status

> **Auto-updated by the pipeline orchestrator.** Check this to see where content creation stands.

| Field | Value |
|-------|-------|
| **Status** | `completed` |
| **Topic** | PostgreSQL EXPLAIN BUFFERS — Real-World E-Commerce Performance Case Study |
| **Started** | 2026-04-26 |
| **Current Step** | All steps complete |

### Step Checklist

- [x] Step 0: Reference analysis
- [x] Steps 1-2: Strategy + outline
- [x] Step 3: Blog post
- [x] Step 3b: Visual assets
- [x] Step 3c: Quality review
- [x] Step 4: LinkedIn post
- [x] Step 5: X/Twitter thread
- [x] Step 6: Reddit post
- [x] Step 8: YouTube script
- [x] Final review complete

**Status values:** `not-started` | `in-progress` | `completed` | `blocked`

> **What to do:**
> - If Status is `not-started` → You're clear to start a new run. Edit references/preferences below, then run `@content-pipeline` or `/new-content-pipeline`
> - If Status is `in-progress` → Content creation is underway. Run `@content-pipeline` to resume from where it left off
> - If Status is `completed` → All steps done! Review the content, then run `/archive-content` to archive and start fresh
> - If Status is `blocked` → See Current Step for what needs attention

---

## Model Selection

Choose which model to use for content generation. Select your model in the **VS Code Copilot model picker** before running agents.

### Recommended Models by Task

| Task | Recommended | Why |
|------|-------------|-----|
| Content Strategy / Planning | Claude Sonnet 4 or o3 | Deep reasoning, nuanced audience analysis |
| Blog Writing | Claude Sonnet 4 or GPT-4.1 | Strong technical writing, data accuracy |
| Visual Generation | GPT-4.1 or Claude Sonnet 4 | Reliable code generation for Python renderers |
| Quality Review | Claude Sonnet 4 | Best at critical analysis and finding gaps |
| Social Posts (LinkedIn/Twitter) | Claude Sonnet 4 or GPT-4o | Good at concise, punchy copy |
| Reddit Posts | Claude Sonnet 4 | Natural conversational tone |
| Video Scripts | Claude Sonnet 4 or GPT-4.1 | Structured output with timing |

### Current Selection

**Preferred model**: _(select in VS Code Copilot picker — agents inherit your selection)_

### Available Models (GitHub Copilot)

Run `/configure-model` to see the latest available models and get recommendations.

**Flagship**: Claude Sonnet 4, Claude Sonnet 4.5, GPT-4.1, GPT-4o, Gemini 2.5 Pro
**Fast**: Claude Haiku 3.5, GPT-4o mini, GPT-4.1 mini, GPT-4.1 nano
**Reasoning**: o3, o4-mini, Claude Sonnet 4 (Extended Thinking)

---

## Online References

List URLs below that agents should fetch, analyze, and synthesize during content creation. The pipeline will read these before writing.

### How to Use

1. Add URLs under the appropriate section below
2. Add a brief note on what to extract from each
3. Pipeline agents will fetch and analyze these during Steps 1-3

### Reference URLs

<!-- Add your reference URLs below. Format: - [description](URL) -->

**General content:**
https://boringsql.com/posts/explain-buffers/

**Industry Reports & Benchmarks:**
- 

**Competitor / Related Articles:**
- 

**Pricing Pages & Documentation:**
- 

**Case Studies & Examples:**
- 

**Research Papers:**
- 

---

## Output Preferences

### Blog
- **Target length**: ~3,000 words
- **Output path**: `content/`

### Social Posts
- **LinkedIn**: Plain + Unicode formatted versions
- **X/Twitter**: 10-12 tweet thread + standalone summary
- **Reddit**: Standard Markdown, target subreddits listed below

### Target Subreddits
- r/MachineLearning
- r/ExperiencedDevs
- r/artificial
- r/programming

### YouTube
- **Target duration**: 8-12 minutes
- **Output path**: `content/youtube-script.md`
