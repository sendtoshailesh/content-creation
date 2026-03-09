# Content Strategy Pipeline — Automation Architecture

## Overview

The 8-step content strategy pipeline is automated as GitHub Copilot custom agents, skills, instructions, and prompts following VS Code Copilot customization standards.

## File Structure

```
.github/
├── copilot-instructions.md                    # Workspace-wide: design tokens, quality bar, tone, config
├── agents/
│   ├── content-pipeline.agent.md              # Orchestrator — coordinates all agents
│   ├── content-strategist.agent.md            # Steps 1-2: interview + outline
│   ├── blog-writer.agent.md                   # Step 3: long-form blog
│   ├── visual-renderer.agent.md               # Step 3b: PNGs, SVGs, Mermaid
│   ├── quality-reviewer.agent.md              # Step 3c: audit + fixes
│   ├── social-linkedin.agent.md               # Step 4: LinkedIn posts
│   ├── social-twitter.agent.md                # Step 5: Twitter thread
│   ├── social-reddit.agent.md                 # Step 6: Reddit post
│   └── video-scriptwriter.agent.md            # Step 8: YouTube script
├── skills/
│   ├── visual-rendering/
│   │   ├── SKILL.md                           # Multi-step visual generation workflow
│   │   └── references/
│   │       └── design-tokens.md               # Color palette, typography, DPI standards
│   ├── unicode-formatting/
│   │   └── SKILL.md                           # Unicode bold/italic procedure for social posts
│   └── reference-analysis/
│       └── SKILL.md                           # Fetch + synthesize online references
├── instructions/
│   ├── content-quality.instructions.md        # Auto-loads for content/**/*.md files
│   ├── visual-standards.instructions.md       # Auto-loads for content/visuals/** files
│   └── social-formatting.instructions.md      # On-demand for social media tasks
└── prompts/
    ├── new-content-pipeline.prompt.md         # Quick-start: /new-content-pipeline
    ├── quality-review.prompt.md               # Quick-start: /quality-review
    └── configure-model.prompt.md              # Discover + choose Copilot models

content/
├── pipeline-config.md                         # User-editable: reference URLs, model prefs, output prefs
├── reference-brief.md                         # Auto-generated: synthesized reference analysis
├── *.md                                       # Blog, social posts, scripts
└── visuals/                                   # PNGs, SVGs, Mermaid files, Python renderers
```

## How It Works

### Starting a Pipeline Run

**Option A — Orchestrator Agent**: Select `@content-pipeline` in the agent picker and provide a topic. The orchestrator delegates to each specialist agent in order with quality gates between phases.

**Option B — Prompt Shortcut**: Type `/new-content-pipeline` in chat and provide a topic. This routes through the orchestrator.

**Option C — Individual Agents**: Use any agent directly (e.g., `@social-linkedin`) for one-off tasks.

### Pipeline Flow

```
User provides topic
        │
        ▼
Read pipeline-config.md (reference URLs?)
        │ yes
        ▼
reference-analysis skill ──► content/reference-brief.md
        │
        ▼
@content-strategist ──► Strategy doc + outline (uses reference brief)
        │
        ▼
@blog-writer ──────────► Long-form blog (uses reference brief)
@visual-renderer ──────► PNGs, SVGs, Mermaid diagrams
        │
        ▼
@quality-reviewer ─────► Quality audit (gate)
        │
        ▼
@social-linkedin ──────► Plain + Unicode LinkedIn posts
@social-twitter ───────► 12-tweet thread + summary
@social-reddit ────────► Markdown Reddit post
@video-scriptwriter ───► YouTube script + slide map
```

### Quality Gates

The orchestrator enforces quality gates between phases:
1. **Post-Planning**: Strategy and outline saved, user confirms direction
2. **Post-Content**: Blog and visuals exist, quality reviewer passes audit
3. **Post-Distribution**: All social posts correctly formatted, video script complete

### Automatic Instruction Loading

| File Pattern | Loaded Instructions |
|---|---|
| `content/**/*.md` | content-quality.instructions.md |
| `content/visuals/**` | visual-standards.instructions.md |
| Social media tasks | social-formatting.instructions.md (on-demand) |

## Model Configuration

Agents do **not** hardcode a model. The user selects the model via the VS Code model picker in the chat panel. This keeps agents flexible as new models become available.

- Use the `/configure-model` prompt to discover all currently available Copilot models
- `content/pipeline-config.md` documents recommended models per task category:
  - **Flagship** (Claude Sonnet 4, GPT-4.1, Gemini 2.5 Pro) — long-form writing, strategy
  - **Fast** (Claude Haiku 3.5, GPT-4o mini) — social post adaptation, formatting
  - **Reasoning** (o3, o4-mini) — data analysis, fact-checking

## Agent Tool Restrictions

| Agent | Tools | Rationale |
|---|---|---|
| content-strategist | read, search, web | Research + reference fetching, no file editing |
| blog-writer | read, edit, search, web | Writes content, fetches references |
| visual-renderer | read, edit, search, execute | Needs terminal to run Python scripts |
| quality-reviewer | read, edit, search, execute | Needs to verify rendered output |
| social-linkedin | read, edit, search | Content adaptation only |
| social-twitter | read, edit, search | Content adaptation only |
| social-reddit | read, edit, search | Content adaptation only |
| video-scriptwriter | read, edit, search | Script writing only |
| content-pipeline | read, edit, search, execute, agent, todo, web | Full orchestration + reference analysis |

## Skills

### visual-rendering
Multi-step workflow for generating all visual asset types. Includes the design token reference and rendering procedures. Loaded automatically when agents need to create charts, diagrams, or graphics.

### unicode-formatting
Procedure for converting plain text to Unicode Mathematical Bold/Italic for LinkedIn and X/Twitter native rendering. Includes character maps and platform rules.

### reference-analysis
Fetches and synthesizes online reference URLs listed in `content/pipeline-config.md`. Produces `content/reference-brief.md` with per-source summaries, cross-source analysis, consensus/contradictions, and extractable data points. Used by the orchestrator in Phase 0 before content creation begins.

## Prompts

| Prompt | Purpose |
|---|---|
| `/new-content-pipeline` | Start a full pipeline run with `@content-pipeline` |
| `/quality-review` | Run quality audit with `@quality-reviewer` |
| `/configure-model` | Discover available Copilot models and get task recommendations |

## Pipeline Configuration

The user-editable config lives at `content/pipeline-config.md` and controls:
- **Reference URLs** — online sources grouped by category (industry reports, competitor articles, pricing pages, case studies, research papers). Agents fetch and analyze these before writing.
- **Model preferences** — recommended models per task (informational; actual model set via picker)
- **Output preferences** — blog length, social targets, subreddits, YouTube duration

## Adding a New Step

1. Create a new agent at `.github/agents/<name>.agent.md`
2. Add the step to `content-pipeline.agent.md`'s pipeline table and orchestration protocol
3. Add any file-specific instructions to `.github/instructions/` if needed
4. Update this doc
