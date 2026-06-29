# Content Pipeline Configuration

> **Edit this file** to configure your content pipeline preferences. All pipeline agents read this config before starting work.

---

## Pipeline Status

> **Auto-updated by the pipeline orchestrator.** Check this to see where content creation stands.

| Field | Value |
|-------|-------|
| **Status** | `in-progress` |
| **Topic** | Postgres Ate the Database Market — The "Just Use Postgres" Thesis and Where It Breaks (idea DB-1) |
| **Started** | 2026-06-26 |
| **Current Step** | Steps 1-3b complete: brief locked, anecdote provided, scope assessment = single post, blog draft written (`content/just-use-postgres.md`), four visuals rendered + visual-QA PASS (4/4). NEXT: quality review (Tier 0/REVR) then distribution (LinkedIn + Reel + Slide deck). |
| **Series** | `no` (single post — punchy ~1,800-word opinion piece per brief; formal scope assessment still pending at Step 2b) |
| **Current Part** | n/a — single post |

### Step Checklist

- [x] Step 0: Reference discovery + analysis — relevance-ranked, vendor-neutral (`content/reference-brief.md`)
- [ ] Step 1b: Content research (STORM)
- [x] Steps 1-2: Strategy + outline (creative brief locked; strategy + outline drafted — PAUSED for user review + anecdote)
- [x] Step 2b: Scope assessment (single vs. series) — single post (score ~3/16, vetting 4/4)
- [ ] Step 2c: Multi-dimensional analysis
- [x] Step 2d: Visual opportunity mapping (`content/visual-opportunity-map.md`)
- [ ] Step 2e: Infographic art direction
- [x] Step 3: Blog post draft (`content/just-use-postgres.md`, ~2,300 words incl. practitioner section)
- [x] Step 3b: Visual assets (4 rendered in `content/visuals/`, visual-reviewer PASS 4/4)
- [ ] Step 3b-img: hero/illustrative imagery (optional)
- [ ] Step 3c: Quality review (Tier 0 preflight + REVR visual gate)
- [ ] Step 3d: SEO optimization
- [ ] Step 4a: Social distribution strategy
- [ ] Step 4a-visual: Visual-first asset pack
- [ ] Step 4: LinkedIn post
- [ ] Step 4c: Social platform selection
- [ ] Step 5: X/Twitter thread
- [ ] Step 6b: Reel/Short video
- [ ] Step 6c: Slide deck (HTML + PDF + PPTX)
- [ ] Step 6d: LinkedIn carousel
- [ ] Step 7: Brand audit
- [x] Step 7b: Grounded content review (PASS 2026-06-28 — ~20 data points verified; 2 citation links repointed to live Azure successor pages)
- [ ] Step 8: YouTube script
- [ ] Step 9: X/Twitter post
- [ ] Step 10: Web publishing
- [ ] Step 10b: Citation-link remediation
- [ ] Step 11: Social publishing
- [ ] Step 12: Medium/Substack distill
- [ ] Step 13: Post-publish go/no-go (`post-publish-review`)
- [ ] Step 14: Discover reflection (`post-run-reflection`)
- [ ] Cross-cutting: Content Decision Records (`content-decision-record`) — log consequential forks + rejected alternatives to `content/content-decision-log.md` as they happen (never a gate)
- [ ] Cross-cutting: Run tracking (`run-tracking`) — for long runs / multi-part series, keep a per-run phase log + compaction handoff under `content/_tracking/<run-slug>/` so context survives compactions and series gaps (never a gate)

**Series values:** `not-applicable` | `pending-assessment` | `yes (N parts)` | `no`

**Status values:** `not-started` | `in-progress` | `completed` | `blocked`

> **What to do:**
> - If Status is `not-started` → You're clear to start a new run. Edit references/preferences below, then run `@content-pipeline` or `/new-content-pipeline`
> - If Status is `in-progress` → Content creation is underway. Run `@content-pipeline` to resume from where it left off
> - If Status is `completed` → All steps done! Review the content, then run `/archive-content` to archive and start fresh
> - If Status is `blocked` → See Current Step for what needs attention
>
> **Rollback / redo rule:** If any agent goes back to rebuild an earlier phase, update this status before editing: set Status to `in-progress`, set Current Step to the earliest step being redone with the date and reason, uncheck that step and all downstream dependent steps, and mark published/social outputs stale until republished. Do not leave this file saying a later step is complete while earlier content is being regenerated.

---

## Model Selection

Choose which model to use for content generation. Select your model in the **VS Code Copilot model picker** before running agents.

### Model Family Detection

The pipeline uses the selected model for content generation and GitHub Copilot's **rubber-duck review** feature for adversarial review gates. No model-family switch is required before reviews.

| Family | Model name prefix |
|--------|------------------|
| `anthropic` | Claude * |
| `openai` | GPT-*, o* |
| `google` | Gemini * |

### Rubber-Duck Review

| Role | Selection Rule |
|------|---------------|
| **Content Creation** | User selects any model; pipeline records the family used |
| **Critic Review** | Use GitHub Copilot **rubber-duck review**; no model switch required |
| **Visual Generation** | User selects any model |

> **How it works**: After content is created, the orchestrator runs rubber-duck review as the adversarial critique gate, then routes findings to the appropriate reviewer/fixer agents.

### Current Run

| Field | Value |
|-------|-------|
| **Creation model family** | `anthropic` |
| **Review method** | `GitHub Copilot rubber-duck` |

### Current Selection

**Preferred model**: _(select any model in the VS Code Copilot picker — agents inherit your selection automatically)_

Review gates use GitHub Copilot rubber-duck review. No specific model versions are required — use whatever is available.

---

## Online References

List URLs below that agents should fetch, analyze, and synthesize during content creation. The pipeline will read these before writing.

### Source ranking (how this list is used)

References are ranked by **relevance and authority for each claim**, not by publisher (see `.github/instructions/content-quality.instructions.md` and the `source-grounding` skill). For any claim, cite the best **primary** source (whoever built/ran/shipped the thing), backed by independent **measurement** and expert **synthesis**. All publishers are equal candidates. The groupings below are organizational by source type — not a precedence order.

### How to Use

1. Add URLs under the most fitting **group** below (by source type)
2. Add a brief note on what to extract from each
3. Pipeline agents fetch, verify, and analyze these during Steps 1-3, ranking by relevance not vendor

### Reference URLs

<!-- Add reference URLs by tier. Format: - [description](URL) -->

> **New run (DB-1, 2026-06-26):** references not yet populated. Run `@reference-discovery` to gather and curate sources for the "Just Use Postgres" thesis, then `@content-pipeline` will analyze them into `content/reference-brief.md`. Candidate source areas to discover and rank by authority per claim:
>
> - **Primary / first-party:** PostgreSQL release notes (18/19), extension project docs (pgvector, TimescaleDB, pgmq, PostGIS, Citus), specialist-DB vendor docs for the contrast cases (ClickHouse, Cassandra/ScyllaDB, DynamoDB, Redis)
> - **Measurement:** DB-Engines ranking trend, independent benchmark write-ups (throughput/latency ceilings), Postgres-extension ecosystem surveys
> - **Synthesis:** practitioner essays on the "just use Postgres" thesis, Postgres-19 feature roundups, build-vs-buy analyses
>
> Re-verify every URL before direct citation. Treat all publishers as equal candidates; cite the best primary source per claim, backed by measurement + synthesis.

---

## Output Preferences

### Blog
- **Target length**: ~1,800 words (single punchy opinion piece — overrides the prior ~3,000-word default per the DB-1 creative brief: thesis + four breakpoints, lighter on exhaustive benchmarks, real numbers only)
- **Output path**: `content/`

### Image Generation (hybrid AI imagery)

> Controls the optional image step (Step 3b-img). Scope is **hero / backdrop / scene /
> conceptual-illustration** assets only — diagrams, infographics, flows, comparison
> matrices, and executive exhibits stay deterministic/programmatic.
>
> **Two modes, default is free + offline:**
> - `programmatic` — deterministic hero/backdrop rendered by `scripts.visuals.generated.programmatic`
>   (HTML/CSS+Chromium, brand tokens, reserved negative space). **No API key, no network, no
>   cost, fully reproducible.** This is the default.
> - `ai` — calls an external image model (OpenAI/Azure) for a photoreal/illustrative look.
>   Opt-in only; needs a key + network + spend. See `agents-and-skills/image-provider-comparison.md`.
> - `off` — skip image generation entirely.

| Field | Value |
|-------|-------|
| **mode** | `programmatic` |
| **provider** (ai mode only) | `openai` |
| **model** (ai mode only) | `gpt-image-1` |
| **size** | `1024x1024` |
| **quality** (ai mode only) | `medium` |
| **max_images_per_run** | `3` |
| **reference_images** | _(paths/URLs for grounding, optional)_ |

> Every generated image (either mode) is written to `content/visuals/generated/` with a sidecar
> JSON (mode, license, safety, and for `ai` the provider/model/prompt/seed), must pass the
> deterministic `scripts.visuals.generated.inspect_image` pre-screen (no-text, brand-color
> fidelity, negative-space), and then `visual-reviewer`.

### Series Configuration

> Auto-populated by scope assessment. Edit manually to override.

| Field | Value |
|-------|-------|
| **Is Series** | `pending-assessment` |
| **Total Parts** | _(pending scope assessment)_ |
| **Current Part** | n/a |
| **Single-post focus** | _(pending)_ |
| **Publishing Cadence** | _(pending)_ |

### Dimension Analysis

> Auto-populated by multi-dimensional analysis (Step 2c). Edit manually to override.

| Field | Value |
|-------|-------|
| **Persona count** | _(pending)_ |
| **Personas** | _(pending multi-dimensional analysis)_ |
| **Technology practices** | _(pending)_ |
| **Governance practices** | _(pending)_ |
| **Total practices** | _(pending)_ |
| **Primary WAF pillars** | _(pending)_ |
| **Secondary WAF pillars** | _(pending)_ |
| **Dimension breadth score** | _(pending)_ |

### Social Platform Selection

> The pipeline always generates LinkedIn. For other platforms, select which to include:

- [x] LinkedIn (always included)
- [ ] X/Twitter thread
- [ ] Reddit post
- [x] Reel/Short video (60-90 sec)
- [ ] YouTube long-form script (8-12 min)
- [x] Slide deck (PPTX + PDF, humor + intellectual speaker notes) — optional, after blog + LinkedIn finalized

> **Note:** Pipeline will ask for confirmation at Step 4c. Pre-check platforms above to skip the prompt.

### Long-Form Platform Distribution (Step 12)

> Generates platform-optimized excerpts for Medium, Substack, and LinkedIn Article. Visual-first when a `content/visuals/distilled/{slug}-{mode}/manifest.md` exists; text-only fallback otherwise.

- [ ] Medium (700–900 words, Import tool auto-sets canonical URL — SEO safe)
- [ ] Substack (300–500 words excerpt only — post as Substack Note, not newsletter)
- [ ] LinkedIn Article (700–900 words, unique angle — NOT a republish of the blog)

### Canonical URL Configuration

| Field | Value |
|-------|-------|
| **GitHub Pages base** | `https://sendtoshailesh.github.io` |
| **Blog URL pattern** | `{base}/blog/{slug}.html` |
| **Series index URL** | `{base}/blog/series/{series-slug}.html` |
| **Publishing log** | `content/publishing-log.md` |

### Social Posts
- **LinkedIn**: Plain + Unicode formatted versions
- **X/Twitter**: 10-12 tweet thread + standalone summary (if selected)
- **Reddit**: Standard Markdown, target subreddits listed below (if selected)
- **Reel/Short video**: 60-90 sec script with screen recording cues + voiceover (if selected)

### Target Subreddits
- r/MachineLearning
- r/ExperiencedDevs
- r/artificial
- r/programming
- r/ChatGPTCoding
- r/CopilotForDevs

### YouTube
- **Target duration**: 8-12 minutes
- **Output path**: `content/youtube-script.md`

### Reel/Short Video
- **Target duration**: 60-90 seconds
- **Platforms**: Instagram Reels, YouTube Shorts, LinkedIn Video
- **Output path**: `content/reel-script.md`

---

## Distillation Settings

| Setting | Value | Description |
|---------|-------|-------------|
| `visual_strategy_mode` | `mandatory` | Visual opportunity mapping is required for every content run before blog writing. Read by: content-pipeline, visual-strategist, blog-writer, visual-renderer, social-strategist. |
| `visual_opportunity_map` | `content/visual-opportunity-map.md` | Planning artifact that maps text sections to blog companion visuals and standalone distribution assets. |
| `visual_first_platform_scope` | `blog, linkedin, medium, substack, linkedin-article` | First implementation platform scope. X/Twitter, Reddit, YouTube, and Reels remain follow-on unless selected elsewhere. |
| `visual_first_formats` | `architecture-flow, infographic-one-pager, comic-storyboard, linkedin-card-pack, executive-exhibit` | Mandatory first-milestone visual families. Comic/storyboard assets must be programmatic only. |
| `image_generation_policy` | `programmatic-only` | Use Python, Pillow, SVG via Python, Mermaid, and matplotlib only. Do not require external image generation. |
| `distillation_persona_mode` | `practitioner` | Visual pack persona mode. Options: `practitioner` (10-slide carousel, 1080×1080px, Welsh/Lenny/Bloom grammar), `executive` (3-5 exhibits, 1200×627px, HBR/McKinsey exhibit grammar), `ask` (prompt at runtime). Read by: visual-pack-generator skill, social-linkedin agent, social-twitter agent, platform-distiller agent. |
| `distillation_slug` | *(set per run)* | Part identifier used in visual pack directory naming, e.g., `part1`, `part2`. Results in `content/visuals/distilled/{slug}-{mode}/`. |

---

## Pipeline Steps Reference

> Distribution and publishing steps. Run in order. Visual opportunity mapping is mandatory before blog writing; Steps 4a-visual through 12 are post-content steps.

| Step | Agent / Skill | Trigger | Description |
|------|--------------|---------|-------------|
| Step 2d | visual-strategist / visual-content-planning | Mandatory | Creates `content/visual-opportunity-map.md` and adds P0 visual markers before blog writing. |
| Step 4a-visual | visual-pack-generator | Mandatory for visual-first distribution | Generates visual asset pack (PNGs + manifest + renderer) for selected platforms. Run BEFORE Steps 4, 5, 12. Invoked via visual-pack-generator skill with blog path + distillation_slug + distillation_persona_mode. |
| Step 4a-visual-plus | visual-strategist + visual-renderer | Mandatory when opportunity map has P0/P1 standalone visuals | Generates LinkedIn and long-form platform assets: architecture/flow diagrams, infographics/one-pagers, comic/storyboards, card packs, and executive exhibits. |
| Step 4 | social-linkedin | Manual | LinkedIn post generation. Output: `content/linkedin-post.md` |
| Step 5 | social-twitter | Manual | X/Twitter thread generation. Output: `content/x-twitter-thread.md` |
| Step 6 | social-reddit | Manual | Reddit post generation (if selected). Output: `content/reddit-post.md` |
| Step 6b | reel-video | Manual | Short video script (60-90 sec). Output: `content/reel-script.md` |
| Step 6c | deck-builder | Optional | Slide deck with humor + intellectual speaker notes; exports PPTX + PDF after user finalizes. Outputs: `content/deck/<topic>-deck.{md,pptx,pdf}` |
| Step 6d | linkedin-carousel | Optional | Consolidate the blog's finalized visuals into one LinkedIn document carousel (cover + captioned slide per visual + CTA). Runs after visuals are REVR-passed. Renderer: `scripts/visuals/build_carousel.py`. Outputs: `content/visuals/<topic>-carousel.{manifest.json,pdf}` |
| Step 7 | brand-guardian | Manual | Brand audit across all generated content pieces |
| Step 10 | web-publisher | Manual | Publish to GitHub Pages; establish canonical URL; update BOTH the blog index and the home #insights grid |
| Step 11 | social-publisher | Manual | Publish to social platforms (per publishing mode + approved platforms) |
| Step 12 | platform-distiller | Manual | Visual-first or text-only excerpts per platform-distiller |

---

## Publishing Configuration

> Controls how generated social content is published to platforms. See `docs/social-api-setup.md` for credential setup.

### Publishing Mode

| Field | Value |
|-------|-------|
| **Publish mode** | `confirm` |
| **Publish approach** | `per-platform` |

**Mode values:**
- `manual` — content generated only; user copy-pastes to platforms
- `confirm` — MCP servers preview content; user approves before posting
- `auto` — post immediately after generation (not recommended)

**Approach values:**
- `per-platform` — free MCP servers: reddit-mcp-server + mcp-linkedin + custom (X/YouTube). Cost: $0/mo
- `posteverywhere` — PostEverywhere SaaS MCP. Cost: $19-79/mo. Does NOT cover Reddit.
- `postfast` — PostFast SaaS MCP. Cost: paid. Does NOT cover Reddit.

### Published URLs

> Auto-populated after publishing. Cleared on archive.

#### GitHub Pages (Canonical)

| Part | URL | Published |
|------|-----|-----------|
| Part 1 | https://sendtoshailesh.github.io/blog/agent-eval-part-1.html | 2025-07-17 |
| Part 2 | https://sendtoshailesh.github.io/blog/agent-eval-part-2.html | 2025-07-17 |
| Series Index | https://sendtoshailesh.github.io/blog/series/agent-eval.html | 2025-07-17 |
| Visual-first Canonical | https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html | 2026-06-08 |

#### Social Media

| Platform | URL | Posted |
|----------|-----|--------|
| LinkedIn | https://www.linkedin.com/feed/update/urn:li:ugcPost:7470133668175433728/ | 2026-06-09 |
| X/Twitter | — | — |
| Reddit | — | — |

#### Long-Form Platforms

| Platform | URL | Posted |
|----------|-----|--------|
| Medium | https://medium.com/@shaileshkumarmishra/ai-agent-evals-production-readiness-guide-bd60e62f877a | 2026-06-09 |
| Substack | — | — |
| LinkedIn Article | — | — |

### Publish Sequence

| Day | Action | Notes |
|-----|--------|-------|
| Day 0 | Generate visual pack | Run visual-pack-generator (Step 4a-visual) with target slug + persona mode |
| Day 0 | GitHub Pages publish | Establishes canonical URL |
| Day 0 | Medium Import | Use Import tool — sets rel=canonical → protects SEO |
| Day 0 | LinkedIn Post | Upload carousel slides as PDF document post. Add canonical URL as FIRST COMMENT within 60 sec |
| Day 0 | X/Twitter thread | Upload image cards to tweet thread. Canonical URL in FINAL TWEET ONLY |
| Day 3-4 | Substack Note | Post as NOTE (not newsletter). Hero image + excerpt + canonical link |
| Day 7+ | LinkedIn Article | Unique angle (>30% new material). 2-3 inline exhibits. Google indexes this — must be unique. |
