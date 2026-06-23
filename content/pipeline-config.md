# Content Pipeline Configuration

> **Edit this file** to configure your content pipeline preferences. All pipeline agents read this config before starting work.

---

## Pipeline Status

> **Auto-updated by the pipeline orchestrator.** Check this to see where content creation stands.

| Field | Value |
|-------|-------|
| **Status** | `in-progress` |
| **Topic** | From Prompts to Harness Engineering to Loop Engineering — The Workflow Shift in AI-Native Development |
| **Started** | 2026-06-22 |
| **Current Step** | STEP 10 COMPLETE (2026-06-23) — Web publishing done. Converted `content/from-prompts-to-loop-engineering.md` to `docs/blog/loop-engineering-ai-native-development.html` (SEO title as `<title>`, 151-char meta description, slug `loop-engineering-ai-native-development`), matching existing `docs/` site structure/styling/design tokens — no new frameworks. All 9 visuals embedded as `visuals/pX-XX-*.png` relative paths (PNGs copied into `docs/blog/visuals/`; filenames unchanged). Linked the post at the top of `docs/index.html` blog list. Canonical URL recorded in `content/publishing-log.md`: https://sendtoshailesh.github.io/content-creation/blog/loop-engineering-ai-native-development.html. Next: Step 4a social distribution strategy. |
| **Series** | `no (single comprehensive post)` |
| **Current Part** | n/a — single post `content/from-prompts-to-loop-engineering.md` |

### Step Checklist

- [x] Step 0: Reference analysis
- [ ] Step 1b: Content research (STORM) — `content-researcher`
- [x] Steps 1-2: Strategy + outline
- [x] Step 2b: Scope assessment (single vs. series) — 13/16 → ran series test → **per-part word floor FAILED** (drafted Part 1 ~1,600w < 2,400w) → **single comprehensive post**. Skill fixed to enforce the 2,400-word floor.
- [x] Step 2c: Multi-dimensional analysis — 3 personas, 8 practices, WAF: OpsExcellence+Cost primary
- [x] Step 2d: Visual opportunity mapping — 10 blog companions (5/part); heroes = staircase + loop diagram; `content/visual-opportunity-map.md` + `content/visual-style-map.md`
- [ ] Step 2e: Infographic art direction
- [x] Step 3: Blog post draft — merged single post written and cascade-validated (`content/from-prompts-to-loop-engineering.md`, ~2,800 words, all 10 sections). Supersedes the deleted ~1,600-word Part 1 draft. Full four-tier cascade re-run against the merged post (2026-06-23):
  - Tier 0 preflight → `content/preflight-report.md` — GATE: PASS (0 Error / 0 Warning, exit 0)
  - Tier 1 critic + fact-check → `content/tier1-critic-review.md` — GATE: FAIL → escalate (2 high-risk-class claim-citation Warnings; 15/15 load-bearing claims grounded, 0 Errors)
  - Tier 2 diverse jury → `content/tier2-jury-verdict.md` — 3 disjoint jurors, 2–1 approve-with-residual on each item → Tier 3
  - Tier 3 escalation gate → `content/escalation-digest.md` — 2 rows, both defensible as written; residual = publish-time source re-pull only (no draft-time change)
  - Phase D metrics → `content/critique-metrics.md` + `content/cascade-metrics-report.md` — 2 runs; escalation rate 100%, escalation precision 50%, GATE: PASS (exit 0)
  - Residual human action before publish: re-pull the SWE-bench figures (12.47%→76.8%, $0.05–$0.96) and the OpenAI harness-engineering page (currently 403). Böckeler "guides and sensors" already paraphrased — no edit needed.
- [x] Step 3b: Visual assets — 9 companions rendered at 320 DPI by `content/visuals/render_loop_engineering.py` and embedded into the post (markers replaced; Tier 0 preflight GATE PASS, all paths resolve). Re-rendered 2026-06-23 after migrating the p1-01 staircase HERO from hand-placed matplotlib to D2 (auto-layout, `direction: up`) to end the hand-geometry defect class; deep QA via image view confirms clean cards/arrows/title/sources, no overlap / overflow / occlusion. Style diversity across the set:
  - `p1-05-pull-quote.png` (typographic) — the reframe pull-quote [line 9]
  - `p1-01-staircase.png` (diagram-as-code ★HERO, d2 vertical climb) — four-era staircase [line 17]
  - `p1-02-ceilings.png` (hand-drawn) — three ceiling cards [line 36]
  - `p2-01-loop.png` (diagram-as-code ★HERO, d2 vertical) — plan→act→observe→verify→correct [line 50]
  - `p1-03-harness-vs-loop.png` (editorial-illustration) — nouns vs. verbs [line 60]
  - `p2-02-postures.png` (hand-drawn) — outside/in/on the loop + flywheel [line 77]
  - `p2-03-bottleneck.png` (data-exhibit, directional) — generation vs. validation [line 87]
  - `p2-04-stripe-swebench.png` (data-exhibit) — Stripe before/after + SWE-bench trajectory + cost band [line 95]
  - `p2-05-first-loop-checklist.png` (hand-drawn) — your first loop checklist [line 116]
- [ ] Step 3b-img: hero/illustrative imagery (optional)
- [x] Step 3c: Quality review — `quality-reviewer` verdict PASS; 1 surgical fix (p1-02-ceilings.png repositioned to end of Eras 1–3 with setup sentence); no "leverage"; data preserved; Tier 0 preflight GATE PASS. Re-validated 2026-06-23 after migrating the p1-01 staircase HERO to D2 (re-rendered + deep-QA via image view, preflight GATE PASS).
- [x] Step 3d: SEO optimization — in-place on `content/from-prompts-to-loop-engineering.md` (2026-06-23). Primary keyword "loop engineering" + 5 secondary; added `seo:` frontmatter (title 50 chars / meta 151 chars / slug `loop-engineering-ai-native-development`); front-loaded primary keyword in subtitle; optimized 5 H2s with secondary keywords (reader-first); verified descriptive alt text on all 9 images (paths unchanged). Tier 0 preflight deterministically validated GATE: PASS (0/0/0).
- [ ] Step 4a: Social distribution strategy
- [ ] Step 4a-visual: Visual-first asset pack
- [ ] Step 4: LinkedIn post
- [x] Step 4c: Social platform selection — LinkedIn + Reel/Short video + Slide deck (PPTX + PDF)
- [ ] Step 5: X/Twitter thread — skipped by user selection
- [ ] Step 6b: Reel/Short video
- [ ] Step 6c: Slide deck (PPTX + PDF, humor + intellectual speaker notes) — `deck-builder`
- [ ] Step 7: Brand audit
- [ ] Step 7b: Grounded content review
- [ ] Step 8: YouTube script — skipped by user selection
- [x] Step 10: Web publishing — `content/from-prompts-to-loop-engineering.md` → `docs/blog/loop-engineering-ai-native-development.html` (2026-06-23). 9 visuals copied to `docs/blog/visuals/` and referenced via relative `visuals/` paths; linked from `docs/index.html`; canonical URL logged to `content/publishing-log.md`.
- [ ] Step 11: Social publishing
- [ ] Step 12: Platform distillation draft

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

### How to Use

1. Add URLs under the appropriate section below
2. Add a brief note on what to extract from each
3. Pipeline agents will fetch and analyze these during Steps 1-3

### Reference URLs

<!-- Add your reference URLs below. Format: - [description](URL) -->

> Verified 2026-06-22 (Phase 0 trend research). Full synthesis + quantified data table in `content/trend-research.md`.

**Loop Engineering — Core (definition & the skill):**
- https://simonwillison.net/2025/Sep/30/designing-agentic-loops/ — Simon Willison "Designing agentic loops": names loop design as a discrete skill; "runs tools in a loop to achieve a goal"; the four design levers
- https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html — Kief Morris (Thoughtworks): inner/middle/outer loops, why-loop vs how-loop, humans outside/in/on the loop, "fix the artefact vs. fix the loop"
- https://www.anthropic.com/engineering/building-effective-agents — Anthropic: evaluator-optimizer loop, gates, stop conditions ("maximum number of iterations to maintain control")
- https://simonwillison.net/2025/Oct/7/vibe-engineering/ — Willison "Vibe engineering" (updated to "Agentic Engineering" Feb 2026): lists "designing agentic loops" as a core senior skill

**Inner-loop Validation / Self-correction:**
- https://www.infoq.com/news/2026/06/circleci-chunk-sidecars/ — CircleCI Chunk Sidecars: validation pulled into the agent's inner loop; "validation, not generation, is the bottleneck"
- https://www.infoq.com/news/2026/06/claude-code-harnesses/ — Anthropic Dynamic Workflows: named self-correction failure modes (agentic laziness, self-preferential bias, goal drift) + adversarial verification loops
- https://martinfowler.com/articles/build-own-coding-agent.html — Ben O'Mahony (Thoughtworks): buildable act->observe->verify loop with test-result-as-feedback

**Harness vs. Loop distinction:**
- https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html — Böckeler: harness = "everything except the model"; feed-forward vs feedback; quotes OpenAI on "environments, feedback loops, and control systems"
- https://www.infoq.com/podcasts/mcp-vibe-coding-harness-engineering/ — Böckeler podcast: one-year evolution narrative; harness = guides + sensors so the agent can self-correct
- https://martinfowler.com/articles/harness-engineering.html — Böckeler considered article: harness elements as "guides and sensors" + harness templates

**Eras / arc framing:**
- https://martinfowler.com/articles/exploring-gen-ai.html — Fowler "Exploring Generative AI" index: dated chronological map from autocomplete -> context -> harness -> loops
- https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html — Böckeler: the context-engineering middle era (lazy-loaded skills, MCP decline)
- https://openai.com/index/harness-engineering/ — OpenAI "Harness engineering": 1M-LOC / 5-month / no-typed-code case study (⚠ 403 to fetcher; corroborated indirectly, re-verify before direct citation)

**Quantified data & case studies:**
- https://www.infoq.com/news/2026/03/stripe-autonomous-coding-agents/ — Stripe "Minions": 1,300+ PRs/week, zero human-written code, "blueprints = deterministic code + flexible agent loops"; underpins $1T+ payment volume
- https://www.swebench.com/ — SWE-bench: 12.47% (Mar 2024) -> 76.8% (Claude 4.5 Opus, Feb 2026) under the same harness; mini-SWE-agent 65% in ~100 lines; per-task cost ~$0.05-$0.96

**First-Party Reference (this repo's own harness/loop):**
- Local: `agents-and-skills/automation-architecture.md`, `agents-and-skills/content-pipeline-flow.md`, `agents-and-skills/agent-definitions.md` — the agent/skill/instruction harness + review-gate loops that run this very content pipeline (a working loop-engineering example)

---

## Output Preferences

### Blog
- **Target length**: ~3,000 words per part (if series)
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
| **Is Series** | `no` — consolidated to a single post on 2026-06-22 (drafted Part 1 fell below the 2,400-word per-part floor) |
| **Total Parts** | 1 |
| **Current Part** | n/a — single post `content/from-prompts-to-loop-engineering.md` |
| **Single-post focus** | The full four-era staircase (word → context → rig → loop) + the loop-engineering payoff in one ~2,800-word post; IC practitioner through tech lead |
| **Publishing Cadence** | n/a — single post |

### Dimension Analysis

> Auto-populated by multi-dimensional analysis (Step 2c). Edit manually to override.

| Field | Value |
|-------|-------|
| **Persona count** | 3 |
| **Personas** | AI-native practitioner (IC/senior dev), tech lead/staff engineer, engineering manager |
| **Technology practices** | 5 (agentic loop design, inner-loop validation, evaluator-optimizer, stop conditions, harness construction) |
| **Governance practices** | 3 (human posture outside/in/on, cost+subsidy awareness, failure-mode defense) |
| **Total practices** | 8 |
| **Primary WAF pillars** | Operational Excellence, Cost Optimization |
| **Secondary WAF pillars** | Reliability |
| **Dimension breadth score** | 2/2 |

### Social Platform Selection

> The pipeline always generates LinkedIn. For other platforms, select which to include:

- [x] LinkedIn (always included)
- [ ] X/Twitter thread
- [ ] Reddit post
- [x] Reel/Short video (60-90 sec)
- [ ] YouTube long-form script (8-12 min)
- [ ] Slide deck (PPTX + PDF, humor + intellectual speaker notes) — optional, after blog + LinkedIn finalized

> **Note:** Pipeline will ask for confirmation at Step 4c. Pre-check platforms above to skip the prompt.

### Long-Form Platform Distribution (Step 12)

> Generates platform-optimized excerpts for Medium, Substack, and LinkedIn Article. Visual-first when a `content/visuals/distilled/{slug}-{mode}/manifest.md` exists; text-only fallback otherwise.

- [x] Medium (700–900 words, Import tool auto-sets canonical URL — SEO safe)
- [x] Substack (300–500 words excerpt only — post as Substack Note, not newsletter)
- [x] LinkedIn Article (700–900 words, unique angle — NOT a republish of the blog)

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
| Step 7 | brand-guardian | Manual | Brand audit across all generated content pieces |
| Step 10 | web-publisher | Manual | Publish to GitHub Pages; establish canonical URL; update index |
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
