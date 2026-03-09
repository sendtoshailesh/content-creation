# Content Strategy Pipeline

An automated 8-step content creation pipeline powered by GitHub Copilot custom agents. Provide a technical topic and get a full distribution package: long-form blog, social posts (LinkedIn, X/Twitter, Reddit), and YouTube script — all with consistent visuals and data-driven quality.

## Prerequisites

- **VS Code** (or VS Code Insiders) with **GitHub Copilot Chat** extension
- **Python 3.10+** (for visual rendering)
- A GitHub Copilot subscription with [custom agents support](https://docs.github.com/en/copilot/customizing-copilot)

## Quick Start

### 1. Set Up Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install matplotlib
```

### 2. Configure Your Pipeline

Edit [`content/pipeline-config.md`](content/pipeline-config.md) to set:

- **Reference URLs** — online sources the pipeline will fetch and analyze before writing
- **Model preferences** — which Copilot model to use per task (informational; you select the actual model in the VS Code picker)
- **Output preferences** — blog length, target subreddits, YouTube duration

### 3. Choose a Model

Open the Copilot Chat panel and select your preferred model from the model picker dropdown. Run `/configure-model` in chat to see all available models with task-specific recommendations.

### 4. Run the Pipeline

**Full pipeline** — type in Copilot Chat:
```
@content-pipeline Create content about [your topic]
```

**Or use the prompt shortcut:**
```
/new-content-pipeline
```

The orchestrator will guide you through all 8 steps with quality gates between phases.

## New Content vs. Existing Content

Open [`content/pipeline-config.md`](content/pipeline-config.md) and check the **Pipeline Status** section at the top.

| Status | What It Means | What to Do |
|--------|--------------|------------|
| `not-started` | No active run | Edit config (references, preferences) → run `@content-pipeline` |
| `in-progress` | Pipeline is mid-run | Run `@content-pipeline` — it resumes from the last incomplete step |
| `completed` | All steps done | Review content → run `/archive-content` → then start a new run |
| `blocked` | A step needs attention | Check the step checklist for details, fix the issue, then resume |

### Starting a New Run

1. Check status in `content/pipeline-config.md`
2. If previous content exists (`completed` or `in-progress`), run `/archive-content` first
3. Edit references, model preferences, and output preferences
4. Run `@content-pipeline Create content about [your topic]`

### Resuming an Incomplete Run

1. Check the step checklist in `content/pipeline-config.md` — checked boxes show what's done
2. Run `@content-pipeline` — the orchestrator reads the checklist and picks up where it left off
3. No need to re-specify the topic; it's saved in the status section

## Pipeline Steps

| Step | Agent | What It Does |
|------|-------|--------------|
| 0 | `@content-pipeline` | Fetches and analyzes reference URLs from config |
| 0b | `@trend-researcher` | Market intelligence, competitive landscape, data points |
| 1-2 | `@content-strategist` | Clarifying questions → strategy doc + outline |
| 3 | `@blog-writer` | Long-form blog (~3,000 words) |
| 3b | `@visual-renderer` | PNGs, SVGs, and Mermaid diagrams |
| 3c | `@quality-reviewer` | Quality audit with fixes |
| 3d | `@seo-optimizer` | SEO metadata, keyword optimization, heading structure |
| 4a | `@social-strategist` | Cross-platform social distribution strategy |
| 4b | `@social-linkedin` | Plain + Unicode formatted LinkedIn posts |
| 5 | `@social-twitter` | Tweet thread + standalone summary |
| 6 | `@social-reddit` | Markdown Reddit post |
| 7 | `@brand-guardian` | Brand consistency audit across all content |
| 8 | `@video-scriptwriter` | YouTube script with slide map |
| 9 | `@content-repurposer` | Newsletter, slide deck, podcast, infographic |

## Using Individual Agents

You don't have to run the full pipeline. Use any agent directly:

```
@blog-writer Write a blog post from content/my-topic-strategy.md
@social-linkedin Adapt content/my-blog.md for LinkedIn
@quality-reviewer Review content/my-blog.md
@visual-renderer Create visuals for content/my-blog.md
@trend-researcher Research market landscape for [topic]
@seo-optimizer Optimize content/my-blog.md for search
@brand-guardian Audit all content for brand consistency
@social-strategist Create social distribution plan for content/my-blog.md
@content-repurposer Repurpose content/my-blog.md into newsletter, slides, podcast
```

## Adding Reference URLs

Before a content run, add your research sources to [`content/pipeline-config.md`](content/pipeline-config.md) under **Reference URLs**:

```markdown
**Industry Reports & Benchmarks:**
- [State of AI 2026](https://example.com/report) — extract market size, adoption rates

**Pricing Pages & Documentation:**
- [OpenAI pricing](https://openai.com/pricing) — per-token costs for GPT-4.1
```

The pipeline fetches these in Step 0 and produces `content/reference-brief.md` — a synthesized analysis that all downstream agents use for data-backed writing.

## Prompt Shortcuts

| Command | Description |
|---------|-------------|
| `/new-content-pipeline` | Start a full pipeline run |
| `/quality-review` | Run quality audit on existing content |
| `/configure-model` | Discover available Copilot models + recommendations |
| `/archive-content` | Archive current content and prepare for a new run |

## Project Structure

```
.github/
├── copilot-instructions.md          # Workspace-wide rules (tokens, quality, tone)
├── agents/                          # 14 specialist agents
├── skills/                          # 3 reusable skills
│   ├── visual-rendering/            #   PNG/SVG/Mermaid generation
│   ├── unicode-formatting/          #   Bold/italic for social posts
│   └── reference-analysis/          #   Fetch + synthesize online sources
├── instructions/                    # 3 auto-loading instruction files
├── prompts/                         # 4 prompt shortcuts
├── ISSUE_TEMPLATE/                  # Bug report & feature request templates
├── PULL_REQUEST_TEMPLATE.md         # PR checklist
└── CODEOWNERS                       # Review assignments

content/
├── pipeline-config.md               # ← Edit this before each run
├── reference-brief.md               # Auto-generated from reference URLs
├── *.md                             # Blog, social posts, scripts
└── visuals/                         # PNGs, SVGs, Mermaid files, renderers

archive/                             # Past content runs (max 3 kept)
├── run-YYYYMMDD-HHMMSS/
│   ├── *.md
│   └── visuals/

scripts/
└── archive-content.sh               # Archive + rotate content runs

agents-and-skills/
└── automation-architecture.md       # Detailed architecture documentation
```

## Design System

All visuals use a shared token system for consistent branding:

| Token | Color | Usage |
|-------|-------|-------|
| ACCENT | `#1f6feb` | Primary blue |
| ACCENT_2 | `#0d9488` | Secondary teal |
| ACCENT_3 | `#7c3aed` | Tertiary purple |
| WARN | `#dc2626` | Warning red |
| SUCCESS | `#16a34a` | Positive green |

Full token reference: [`.github/skills/visual-rendering/references/design-tokens.md`](.github/skills/visual-rendering/references/design-tokens.md)

## Content Quality Standards

Every piece of content must meet these bars:
- Concrete numbers, model names, or benchmarks — no vague claims
- Real pricing data, not placeholders
- At least one case study with before/after metrics
- First-person tone: "sharing my learnings working with customers"
- No corporate/fundraising framing

## Archiving Content

When you finish a content run and want to start fresh:

**Option A — Prompt shortcut:**
```
/archive-content
```

**Option B — Shell script:**
```bash
./scripts/archive-content.sh
```

This will:
1. Show you what will be archived and **ask for confirmation**
2. Copy all content (except `pipeline-config.md`) to `archive/run-YYYYMMDD-HHMMSS/`
3. Clean `content/` for a fresh pipeline run
4. Keep only the **last 3 archives** — older ones are automatically pruned

## Customization

- **Add a new pipeline step**: See the [architecture doc](agents-and-skills/automation-architecture.md#adding-a-new-step)
- **Change visual style**: Edit [design tokens](.github/skills/visual-rendering/references/design-tokens.md)
- **Adjust quality rules**: Edit [`.github/instructions/content-quality.instructions.md`](.github/instructions/content-quality.instructions.md)
- **Change social formatting**: Edit [`.github/instructions/social-formatting.instructions.md`](.github/instructions/social-formatting.instructions.md)

## Attribution

Five agents in this pipeline are adapted from the [agency-agents](https://github.com/msitarzewski/agency-agents) project (MIT License) — `trend-researcher`, `brand-guardian`, `seo-optimizer`, `social-strategist`, and `content-repurposer`. See individual agent files for source details.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, commit conventions, and code standards.

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## Security

To report a vulnerability, see [SECURITY.md](SECURITY.md). Do not open public issues for security concerns.

## License

This project is licensed under the [MIT License](LICENSE).
