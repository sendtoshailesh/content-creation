# Content Strategy Pipeline

An automated content creation pipeline powered by GitHub Copilot custom agents. Provide a technical topic — or let the pipeline discover one from your blog rolls and RSS feeds — and get a full distribution package: long-form blog, social posts (LinkedIn, X/Twitter, Reddit), and YouTube script — all with consistent visuals and data-driven quality.

## Prerequisites

- **VS Code** (or VS Code Insiders) with **GitHub Copilot Chat** extension
- **Python 3.10+** (for visual rendering and feed ingestion)
- A GitHub Copilot subscription with [custom agents support](https://docs.github.com/en/copilot/customizing-copilot)

## Quick Start

### 1. Set Up Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Your Pipeline

Edit [`content/pipeline-config.md`](content/pipeline-config.md) to set:

- **Reference URLs** — online sources the pipeline will fetch and analyze before writing
- **Model preferences** — which Copilot model to use per task (informational; you select the actual model in the VS Code picker)
- **Output preferences** — blog length, target subreddits, YouTube duration

### 3. Run the Pipeline

**Discover content ideas from your blog rolls** (optional):
```
@feed-curator
```

The feed curator reads your configured RSS feeds, newsletters, and blog rolls, classifies articles by subject area, extracts key insights, and presents ranked content ideas for you to curate interactively.

**Pick an idea from the queue:**
```
/select-idea
```

**Or provide a topic directly** — type in Copilot Chat:
```
@content-pipeline Create content about [your topic]
```

**Or use the prompt shortcut:**
```
/new-content-pipeline
```

The orchestrator will guide you through all steps with quality gates between phases.

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

## Content Discovery (Feed Curation)

The feed curation feature automates the process of reading blog rolls, newsletters, and RSS feeds to discover compelling content ideas.

### How It Works

1. **Configure sources** — Edit [`content/feed-sources.md`](content/feed-sources.md) to add your RSS feeds, newsletter archives, and blog URLs
2. **Define subject areas** — Set topic filters (AI, Architecture, Databases, etc.) with priority levels in the same config
3. **Run `@feed-curator`** — The agent fetches all sources, classifies articles against your subject areas, extracts key insights, and synthesizes ranked content ideas
4. **Curate interactively** — Keep, dismiss, explore, or refine ideas (same UX as `@reference-discovery`)
5. **Pipeline handoff** — Select an idea to auto-populate `pipeline-config.md` with the topic and source URLs as references

### Source Types Supported

| Type | Example | How It's Processed |
|------|---------|-------------------|
| `rss` | GitHub Blog, InfoQ | Parsed with `feedparser`, entries filtered by age |
| `newsletter-archive` | TLDR AI, Pragmatic Engineer | Archive page fetched, article links extracted |
| `direct-url` | Specific article URL | Full text extracted via `trafilatura` |
| `opml` | Feedly/Inoreader export | Parsed for feed URLs, each processed as RSS |

### Configuration Files

| File | Purpose | Persists Across Runs |
|------|---------|---------------------|
| [`content/feed-sources.md`](content/feed-sources.md) | Source registry, subject filters, extraction preferences | Yes |
| [`content/idea-queue.md`](content/idea-queue.md) | Curated idea queue with scores and status tracking | Yes |
| [`content/pipeline-config.md`](content/pipeline-config.md) | Per-run pipeline config (auto-populated from selected idea) | Reset per run |

## Pipeline Steps

| Step | Agent / Skill | What It Does |
|------|--------------|--------------|
| -1 | `@feed-curator` | _(Optional)_ Discover content ideas from blog rolls, RSS feeds, newsletters |
| 0 | `@content-pipeline` | Fetches and analyzes reference URLs from config |
| 0b | `@trend-researcher` | Market intelligence, competitive landscape, data points |
| 1 | `@content-strategist` (`creative-brief` skill) | Structured creative brief (`content/creative-brief.md`) |
| 1-2 | `@content-strategist` | Clarifying questions → strategy doc + outline |
| 2d | `@visual-strategist` / `visual-content-planning` skill | Mandatory visual opportunity map before writing |
| 3 | `@blog-writer` | Long-form blog (~3,000 words) |
| 3b | `@visual-renderer` | PNGs, SVGs, and Mermaid diagrams (deterministic) |
| 3b-img | `@image-content-agent` | AI hero/illustrative imagery — optional, only if `image_generation: on` |
| 3c | `@quality-reviewer` | Quality audit with fixes |
| 3d | `@seo-optimizer` | SEO metadata, keyword optimization, heading structure |
| 4a | `@social-strategist` | Cross-platform social distribution strategy |
| 4a-visual | `visual-pack-generator` skill | Generate visual pack (carousel slides, exhibits, or standalone visual assets) for visual-first distribution. |
| 4a-visual-plus | `@visual-strategist` + `@visual-renderer` | Generate standalone LinkedIn and long-form platform visual assets from the opportunity map |
| 4b | `@social-linkedin` | Plain + Unicode formatted LinkedIn posts; visual-first carousel/exhibit posts when visual pack exists |
| 5 | `@social-twitter` | Single tweet (≤ 280 chars) with visual attachment; references x-card or x-exhibit from visual pack when available |
| 6 | `@social-reddit` | Markdown Reddit post |
| 7 | `@brand-guardian` | Brand consistency audit across all content |
| 7b | `@grounded-content-reviewer` | Web-search-grounded fact-checking and gap analysis |
| 8 | `@video-scriptwriter` | YouTube script with slide map |
| 9 | `@content-repurposer` | Newsletter, slide deck, podcast, infographic |
| 10 | `@web-publisher` | Publish blog to GitHub Pages site |
| 11 | `@social-publisher` | Publish to LinkedIn, X/Twitter, Reddit, and YouTube (preview + confirmation required) |
| 12 | `@platform-distiller` | Unified excerpt for Medium, Substack, and LinkedIn Article with embedded visuals (or text-only fallback) |

## Mandatory Visual-First Strategy

Every content run includes a visual opportunity map at `content/visual-opportunity-map.md`. The map turns the strategy or draft into a backlog of visual assets before the blog is finalized.

First-milestone visual families:

| Family | Use For | Primary Platforms |
|--------|---------|-------------------|
| Architecture / flow diagrams | Systems, workflows, ownership, decision paths | Blog, LinkedIn, Medium/LinkedIn Article |
| Infographics / one-pagers | Saveable summaries, metrics, checklists | Blog, LinkedIn, Substack |
| Comic explainers / storyboards | Human scenarios, failure stories, before/after lessons | Blog, LinkedIn |
| LinkedIn social card packs | Swipeable visual thought leadership | LinkedIn |
| Executive exhibits | ROI, risk, cost, and decision evidence | Blog, Medium, LinkedIn Article |
| AI-generated imagery (hero/illustrative) | Hero/backdrop/scene/conceptual shots that carry mood, never data | Blog hero, LinkedIn, Medium/Substack |

Comic/storyboard visuals are generated programmatically with Python/Pillow/SVG primitives only. The pipeline does not require external image generation for diagrams, infographics, or exhibits.

**Optional AI imagery (hybrid):** the `AI-generated imagery` family is the one place the pipeline calls an image model — **only** for hero/backdrop/illustrative slots, gated behind `image_generation: on` in `content/pipeline-config.md`. It is produced by `@image-content-agent` via the `vision-grounding` + `creative-brief` skills, must contain **no embedded text**, must honor brand colors, and passes `@visual-reviewer` like any other asset. This methodology is adapted from [`microsoft/content-generation-solution-accelerator`](https://github.com/microsoft/content-generation-solution-accelerator); see [`agents-and-skills/image-provider-comparison.md`](agents-and-skills/image-provider-comparison.md) to choose a provider.

## Visual-First Distribution

The pipeline generates a **visual asset pack** before distribution agents run. Social posts are then built around the visuals (carousel/exhibit/image cards lead; text narrates).

### Persona Modes

| Mode | Format | Dimensions | Style |
|------|--------|-----------|-------|
| `practitioner` | 10-slide LinkedIn carousel | 1080×1080 px | Hook → framework → steps → CTA (Welsh/Lenny/Bloom grammar) |
| `executive` | 3–5 exhibit charts | 1200×627 px | Context → evidence → framework → ROI (HBR/McKinsey exhibit style) |
| `ask` | _(prompt at runtime)_ | — | The pipeline asks you to choose mode before generating |

### How to Enable

1. In `content/pipeline-config.md`, set:
   ```
   distillation_persona_mode: practitioner   # or executive / ask
   distillation_slug: part1                  # used in output path
   ```
2. After Step 3d (SEO), run Step 4a-visual before LinkedIn/Twitter/Platform steps:
   ```
   @visual-pack-generator content/my-blog.md part1 practitioner
   ```
3. Visual pack is saved to `content/visuals/distilled/part1-practitioner/` (or `part1-executive/`)
4. Steps 4b, 5, and 12 automatically detect the visual pack and embed references

### Output Files

| Agent | With Visual Pack | Without Visual Pack |
|-------|-----------------|---------------------|
| `@social-linkedin` | Visual-first post referencing carousel/exhibit slides | Standard text post |
| `@social-twitter` | Single tweet teasing the key visual | Single standalone tweet |
| `@platform-distiller` | Unified excerpt with embedded hero + inline images | Text-only excerpt |

## Using Individual Agents

You don't have to run the full pipeline. Use any agent directly:

```
@feed-curator                         Discover content ideas from your blog rolls and feeds
@blog-writer Write a blog post from content/my-topic-strategy.md
@social-linkedin Adapt content/my-blog.md for LinkedIn
@social-twitter Adapt content/my-blog.md for X/Twitter
@social-reddit Adapt content/my-blog.md for Reddit
@social-publisher Publish all generated social content (with preview + confirmation)
@platform-distiller Distill content/my-blog.md into Medium, Substack, and LinkedIn Article
@quality-reviewer Review content/my-blog.md
@visual-renderer Create visuals for content/my-blog.md
@trend-researcher Research market landscape for [topic]
@seo-optimizer Optimize content/my-blog.md for search
@brand-guardian Audit all content for brand consistency
@grounded-content-reviewer Validate content against web sources
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
| `/select-idea` | Pick a content idea from the curated queue |
| `/quality-review` | Run quality audit on existing content |
| `/archive-content` | Archive current content and prepare for a new run |

## Project Structure

```
.github/
├── copilot-instructions.md          # Workspace-wide rules (tokens, quality, tone)
├── agents/                          # 22 specialist agents
├── skills/                          # 12 reusable skills
│   ├── visual-rendering/            #   PNG/SVG/Mermaid generation (deterministic)
│   ├── visual-content-planning/      #   Mandatory visual opportunity mapping
│   ├── infographic-design-system/   #   Research-backed infographic design briefs
│   ├── creative-brief/              #   Structured creative-brief front door
│   ├── vision-grounding/            #   Vision-grounded prompts for AI imagery
│   ├── unicode-formatting/          #   Bold/italic for social posts
│   ├── reference-analysis/          #   Fetch + synthesize online sources
│   ├── feed-curation/               #   Classify, extract, rank feed articles
│   ├── visual-pack-generator/       #   Platform-optimized visual packs (carousel / exhibit / cards)
│   ├── visual-review/               #   Cross-model visual QA critic
│   ├── multi-dimensional-analysis/  #   Persona × best-practice × WAF dimension analysis
│   └── content-scope-assessment/    #   Single-post vs. multi-part series scoring
├── instructions/                    # 3 auto-loading instruction files
├── prompts/                         # 5 prompt shortcuts
├── ISSUE_TEMPLATE/                  # Bug report & feature request templates
├── PULL_REQUEST_TEMPLATE.md         # PR checklist
└── CODEOWNERS                       # Review assignments

content/
├── pipeline-config.md               # ← Edit this before each run
├── creative-brief.md                # Structured creative brief (front door for every run)
├── visual-opportunity-map.md         # Mandatory visual backlog and renderer handoff
├── feed-sources.md                  # ← Feed sources + subject area config (persistent)
├── idea-queue.md                    # Curated content ideas (persistent)
├── reference-brief.md               # Auto-generated from reference URLs
├── *.md                             # Blog, social posts, scripts
└── visuals/
    ├── *.png / *.svg                 # Blog visuals from visual-renderer (deterministic)
    ├── generated/                   # AI hero/illustrative imagery + sidecar JSON (optional)
    └── distilled/                   # Visual packs from visual-pack-generator
        ├── {slug}-practitioner/     #   10-slide LinkedIn carousel (1080×1080px)
        └── {slug}-executive/        #   3-5 exhibit charts (1200×627px)

archive/                             # Past content runs (max 3 kept)
├── run-YYYYMMDD-HHMMSS/
│   ├── *.md
│   └── visuals/

scripts/
├── visuals/                          # Reusable visual rendering primitives
│   └── generated/                   # AI image generation: provider, generate, describe, cache
├── archive-content.sh               # Archive + rotate content runs
├── pipeline/
│   ├── feed_reader.py               # Multi-format blog roll / RSS ingestion
│   ├── critic_review.py             # Cross-model adversarial review
│   ├── grounded_review.py           # Fact-check against reference brief
│   ├── generate_social.py           # Generate social posts from blog
│   └── publish_social.py            # Publish to LinkedIn, Twitter, Reddit
└── Validate-DocsReadme.ps1          # Validate all docs/ subfolders have README.md

agents-and-skills/
├── automation-architecture.md       # Detailed architecture documentation
└── image-provider-comparison.md     # AI image provider comparison + decision
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
2. Copy all content (except `pipeline-config.md`, `feed-sources.md`, and `idea-queue.md`) to `archive/run-YYYYMMDD-HHMMSS/`
3. Clean `content/` for a fresh pipeline run
4. Keep only the **last 3 archives** — older ones are automatically pruned

## Customization

- **Add a new pipeline step**: See the [architecture doc](agents-and-skills/automation-architecture.md#adding-a-new-step)
- **Change visual style**: Edit [design tokens](.github/skills/visual-rendering/references/design-tokens.md)
- **Adjust quality rules**: Edit [`.github/instructions/content-quality.instructions.md`](.github/instructions/content-quality.instructions.md)
- **Change social formatting**: Edit [`.github/instructions/social-formatting.instructions.md`](.github/instructions/social-formatting.instructions.md)
- **Configure feed sources**: Edit [`content/feed-sources.md`](content/feed-sources.md) to add/remove blog rolls, set subject areas

## Attribution

Five agents in this pipeline are adapted from the [agency-agents](https://github.com/msitarzewski/agency-agents) project (MIT License) — `trend-researcher`, `brand-guardian`, `seo-optimizer`, `social-strategist`, and `content-repurposer`. See individual agent files for source details.

Three methodologies — the **structured creative brief**, **vision-grounded AI image generation**, and **severity-categorized (Error/Warning/Info) brand compliance** — are adapted from Microsoft's [content-generation-solution-accelerator](https://github.com/microsoft/content-generation-solution-accelerator) (MIT License). Only the methodology is borrowed; the reference repo's Azure infrastructure (Agent Framework, Foundry, Cosmos, AI Search) is intentionally not used.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, commit conventions, and code standards.

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## Security

To report a vulnerability, see [SECURITY.md](SECURITY.md). Do not open public issues for security concerns.

## License

This project is licensed under the [MIT License](LICENSE).
