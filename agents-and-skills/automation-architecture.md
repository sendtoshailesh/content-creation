# Content Strategy Pipeline — Automation Architecture

> For the phase-by-phase **run flow** (every agent, skill, input, output, and gate, with a full
> diagram and worked example), see [content-pipeline-flow.md](content-pipeline-flow.md).

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
│   ├── visual-renderer.agent.md               # Step 3b: PNGs, SVGs, Mermaid (deterministic)
│   ├── image-content-agent.agent.md           # Step 3b-img: AI hero/illustrative imagery (optional)
│   ├── quality-reviewer.agent.md              # Step 3c: audit + fixes
│   ├── social-linkedin.agent.md               # Step 4: LinkedIn posts
│   ├── social-twitter.agent.md                # Step 5: Twitter thread
│   ├── social-reddit.agent.md                 # Step 6: Reddit post
│   ├── social-publisher.agent.md              # Step 11: Publish to social platforms via MCP
│   └── video-scriptwriter.agent.md            # Step 8: YouTube script
├── skills/
│   ├── visual-rendering/
│   │   ├── SKILL.md                           # Multi-step visual generation workflow (deterministic)
│   │   └── references/
│   │       └── design-tokens.md               # Color palette, typography, DPI standards
│   ├── creative-brief/
│   │   └── SKILL.md                           # Structured creative-brief front door (Step 1)
│   ├── vision-grounding/
│   │   └── SKILL.md                           # Vision-grounded prompt grammar for AI imagery
│   ├── unicode-formatting/
│   │   └── SKILL.md                           # Unicode bold/italic procedure for social posts
│   └── reference-analysis/
│       └── SKILL.md                           # Fetch + synthesize online references
├── instructions/
│   ├── content-quality.instructions.md        # Auto-loads for content/**/*.md files
│   ├── visual-standards.instructions.md       # Auto-loads for content/visuals/** files
│   ├── social-formatting.instructions.md      # On-demand for social media tasks
│   └── shared/
│       └── compliance-severity.md             # Error/Warning/Info findings schema + gate
└── prompts/
    ├── new-content-pipeline.prompt.md         # Quick-start: /new-content-pipeline
    ├── quality-review.prompt.md               # Quick-start: /quality-review
    └── configure-model.prompt.md              # Discover + choose Copilot models

content/
├── pipeline-config.md                         # User-editable: references, model prefs, output prefs, image-gen settings
├── creative-brief.md                          # Structured creative brief (front door for every run)
├── reference-brief.md                         # Auto-generated: synthesized reference analysis
├── *.md                                       # Blog, social posts, scripts
└── visuals/                                   # PNGs, SVGs, Mermaid files, Python renderers
    └── generated/                             # AI hero/illustrative imagery + sidecar JSON (optional)

scripts/visuals/generated/                     # Hero imagery: programmatic.py (default, deterministic),
                                               #   generate.py/provider.py/describe.py/cache.py (ai opt-in),
                                               #   inspect_image.py (deterministic QA), selftest.py (offline)
scripts/visuals/charts_js/                     # Opt-in JS chart bridge: echarts_render.py (ECharts -> Chromium PNG)
                                               #   for advanced charts only (sankey/treemap/network/heatmap)

agents-and-skills/
└── image-provider-comparison.md               # AI image provider comparison + decision
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
@content-researcher ───► content/content-research-map.md (STORM: perspectives, contradiction map, ranked arguments, self peer-review, outline tree)
        │
        ▼
@content-strategist ──► Strategy doc + outline (uses reference brief + content-research map)
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

## Social Media Publishing (Step 11)

### MCP Server Topology

```
@social-publisher agent
        │
        ├──► reddit-mcp-server (npm, stdio)
        │      Tools: create_post, get_top_posts, search_reddit, ...
        │      Auth: REDDIT_CLIENT_ID + SECRET
        │      Features: Safe mode, spam protection, bot disclosure
        │
        ├──► mcp-linkedin (npm, stdio)
        │      Tools: linkedin_publish, linkedin_comment, linkedin_react
        │      Auth: UNIPILE_API_KEY + DSN
        │      Features: Dry-run default, media, @mentions, auto-like
        │
        └──► social-publisher (Python, stdio)
               Tools: post_to_twitter, update_youtube_metadata,
                      preview_content, check_credentials
               Auth: TWITTER_* keys, YOUTUBE_* OAuth
               Features: Thread support, metadata-only YouTube
```

### Human-in-the-Loop Flow

```
Generated content (content/*.md)
        │
        ▼
@social-publisher reads pipeline-config.md
        │
        ▼
check_credentials ──► Report missing credentials
        │
        ▼
Preview ALL platforms (dry_run=true)
        │
        ▼
Present summary to user
        │
        ▼
User approves? ──► NO ──► Stop / Edit / Retry
        │
       YES
        │
        ▼
Post to each platform (dry_run=false)
        │
        ▼
Log URLs to content/publishing-log.md
```

### Configuration

MCP servers are registered in `.vscode/mcp.json`. Credentials in `.env` (see `docs/social-api-setup.md`).

Publishing preferences in `content/pipeline-config.md` → Publishing Configuration section:
- **Publish mode**: `manual` | `confirm` | `auto`
- **Publish approach**: `per-platform` (free) | `posteverywhere` ($19/mo) | `postfast` (paid)

### CI/CD Script

`scripts/pipeline/publish_social.py` provides terminal/GitHub Actions publishing:
```bash
python scripts/pipeline/publish_social.py --dry-run --platform linkedin,reddit
python scripts/pipeline/publish_social.py --platform twitter --subreddit ExperiencedDevs
```

---

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
| image-content-agent | read, edit, search, execute | Runs the AI image-generation/vision scripts; hero/illustrative imagery only |
| quality-reviewer | read, edit, search, execute | Needs to verify rendered output |
| social-linkedin | read, edit, search | Content adaptation only |
| social-twitter | read, edit, search | Content adaptation only |
| social-reddit | read, edit, search | Content adaptation only |
| video-scriptwriter | read, edit, search | Script writing only |
| social-publisher | read, edit, search, mcp | Orchestrates 3 MCP servers for social posting |
| content-pipeline | read, edit, search, execute, agent, todo, web | Full orchestration + reference analysis |

## Skills

### visual-rendering
Multi-step workflow for generating all visual asset types. Includes the design token reference and rendering procedures. Loaded automatically when agents need to create charts, diagrams, or graphics.

### unicode-formatting
Procedure for converting plain text to Unicode Mathematical Bold/Italic for LinkedIn and X/Twitter native rendering. Includes character maps and platform rules.

### reference-analysis
Fetches and synthesizes online reference URLs listed in `content/pipeline-config.md`. Produces `content/reference-brief.md` with per-source summaries, cross-source analysis, consensus/contradictions, and extractable data points. Used by the orchestrator in Phase 0 before content creation begins.

### content-research
STORM-inspired four-phase content pre-stage (run by `@content-researcher`, the content-track twin of `visual-strategist`/`visual-research`). Discovers reader-perspectives, builds a contradiction map that resolves into the post's thesis, ranks arguments by confidence, self-reviews the plan for source/persona bias **before** drafting, and writes a hierarchical outline tree to `content/content-research-map.md`. `content-strategist` consumes the map as its outline backbone and pre-write gate.

### creative-brief
Turns the topic and clarifying-question answers into a structured `content/creative-brief.md` (overview, objectives, audience, key message, tone, deliverables, visual guidelines, CTA, guardrails). It is the single source of visual/voice direction for all downstream agents. Adapted from the reference accelerator's Creative Brief Interpretation.

### vision-grounding
Describes reference images with a vision model and assembles the consolidated image-prompt grammar (subject + brief + brand + constraints: no-text, color fidelity, ~30% negative space). Backs the `image-content-agent`.

## AI Imagery & Adopted Methodologies

Three methodologies are adapted from Microsoft's
[content-generation-solution-accelerator](https://github.com/microsoft/content-generation-solution-accelerator)
(MIT). The reference repo's Azure infrastructure is intentionally **not** used — only the
methodology.

1. **Structured Creative Brief** (`creative-brief` skill → `content/creative-brief.md`) — a
   rigorous front door at Step 1 that all agents read.
2. **Hero/illustrative imagery (hybrid), free-and-offline by default** — `image-content-agent`
   (Step 3b-img) generates **hero/illustrative** images only, in one of two modes set in
   `content/pipeline-config.md`:
   - `programmatic` (**default**): deterministic backdrops via
     `scripts/visuals/generated/programmatic.py` (HTML/CSS + Chromium, brand tokens, reserved
     negative space). **No key, no network, no cost, reproducible** — the model parameterizes a
     render exactly as it does for diagrams.
     - `ai` (opt-in): external image model via `scripts/visuals/generated/` (provider-agnostic
       adapter over OpenAI / Azure OpenAI) for a true photoreal look; trades determinism, cost,
       and licensing simplicity for realism.
   Both modes: **no embedded text** (overlays added programmatically), sidecar JSON
   (mode/license/safety + provider/model/prompt/seed for `ai`), a prompt-hash cache, and a
   **deterministic QA pre-screen** (`scripts/visuals/generated/inspect_image.py`: OCR no-text +
   brand-color fidelity + negative-space) before the `visual-reviewer` gate. Reference-image
   grounding and output verification prefer the agent's **own Copilot vision** (`viewImage`);
   `describe.py` is a non-interactive/CI fallback. A key-free self-test
   (`python -m scripts.visuals.generated.selftest`) exercises the default path offline. Diagrams,
   infographics, and exhibits stay deterministic in `visual-renderer`.
3. **Severity-categorized compliance** (`.github/instructions/shared/compliance-severity.md`) —
   `brand-guardian` and `visual-reviewer` emit Error/Warning/Info findings with a PASS/FAIL gate;
   any Error blocks Steps 10/11 and triggers the rollback/redo protocol. As the **final** visual
   sub-gate, `visual-reviewer` runs **REVR** (`.github/skills/visual-reverse-review/SKILL.md`): it
   blind-reads each rendered visual (pixels only), back-translates it against source intent, scores
   the semantic gap on a 0-100 rubric, and loops a renderer fix until the derived meaning matches
   intent with zero legend/encoding gaps. Every Markdown-referenced asset must carry a PASS record
   at `content/visuals/revr/<asset-stem>.md`; a FAIL or missing record blocks publish-ready.

Provider selection guidance lives in `agents-and-skills/image-provider-comparison.md`; keys are
configured in `.env` (see `.env.example`).

## Visual Tech Stack Decision (Python vs JS)

Decided via web research **and** an empirical head-to-head render test (matplotlib vs ECharts of
the same branded chart). Output is **static-only** (every visual pre-rendered to PNG/SVG;
published GitHub Pages load no client JS), so JS frameworks enter only as a server-side
pre-render step.

| Visual type | Stack | Module |
|---|---|---|
| Standard charts (bar/line/scatter/pie) | matplotlib | (renderers) |
| Advanced charts (sankey/treemap/network/heatmap) | ECharts → Chromium PNG (opt-in) | `scripts/visuals/charts_js/echarts_render.py` |
| Infographics / exhibits / tables / layouts | HTML/CSS + Chromium | `scripts/visuals/html/` |
| Diagrams | Mermaid → PNG; Graphviz/DOT for dense | `scripts/visuals/html/render_mermaid.py` |
| Hero / illustrative + text overlay | programmatic backdrop + CSS overlay | `scripts/visuals/generated/programmatic.py` |
| Comics / storyboards | HTML/CSS + Chromium (text); SVG/CSS shapes | `scripts/visuals/html/`, `scripts/visuals/svg/` |

**Key empirical finding:** both matplotlib and a JS lib produce excellent branded static charts,
but the JS path required `npm install` + an inlined bundle + a Playwright harness, and the first
render was **silently wrong** — the screenshot caught the bars mid entrance-animation. The bridge
therefore **forces `animation:false`** as a deterministic guard. matplotlib remains the default
for standard charts; the JS bridge is reserved for chart types matplotlib handles poorly.

**Hard rules:** static-only (no client JS on Pages); JS charts disable animation; text-heavy uses
browser text (HTML/CSS+Chromium), never Pillow/hand-SVG; hero text is composited as a CSS layer.
Full matrix in `.github/instructions/visual-standards.instructions.md` → Stack Selection.

## Prompts

| Prompt | Purpose |
|---|---|
| `/new-content-pipeline` | Start a full pipeline run with `@content-pipeline` |
| `/quality-review` | Run quality audit with `@quality-reviewer` |
| `/configure-model` | Discover available Copilot models and get task recommendations |

## Multi-Topic Pipelines

Beyond the single root pipeline, the system supports **isolated per-topic workspaces** under
`content/topics/<slug>/`, each with its own `pipeline-config.md`, `feed-sources.md`,
`idea-queue.md`, and outputs (`visuals/` subfolder). Topics run independently and in parallel.

- **Scaffolding:** `scripts/pipeline/scaffold_topics.py` defines the topic set, reads Apple Notes
  (`apple_notes_reader.py`) + Chrome bookmarks + Chrome reading list (`reading_list_reader.py`,
  which falls back to the signed-in **Sync Data LevelDB** since modern Chrome no longer keeps the
  reading list in the Bookmarks file), filters out employer-internal/personal links, clusters
  candidates by keyword, and generates each workspace + a `content/topics/README.md` registry.
  Idempotent: it refreshes idea queues but never overwrites an in-flight `pipeline-config.md`
  (status ≠ `not-started`).
- **Running:** `/topic-pipeline <slug>` (or naming a topic to `@content-pipeline`). The
  orchestrator's **Topic-Scoped Runs** rule substitutes the topic workspace for the repo-root
  `content/` paths for the entire run; all gates/phases apply unchanged.
- **Seeding flow:** seeded `idea-queue.md` candidates → `@feed-curator` (scoped to the topic) to
  synthesize ranked ideas → pipeline writes outputs into the topic workspace.

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
