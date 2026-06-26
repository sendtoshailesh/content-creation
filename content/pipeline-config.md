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
| **Current Step** | REVERSE-ENGINEERING VISUAL REVIEW (REVR, 2026-06-25) — COMPLETE. A hard visual-QA gate was built (`.github/skills/visual-reverse-review/SKILL.md`, REVR section 10 in `visual-reviewer` agent, encoding-legibility + REVR gate in `visual-standards.instructions.md`) and run across ALL 10 visuals. Each was blind-read from pixels, back-translated against the source concept, and scored (0-100; pass ≥85 AND zero legend/encoding gaps AND message matches). `p1-03` failed (46 — colored boxes + ring nodes whose labels floated in a disconnected chip row); its renderer was rewritten (self-evolving repair) and it now passes (98). The other 9 passed on first read (94-98). PASS records live under `content/visuals/revr/`. Fixed PNGs re-mirrored to `docs/blog/visuals/`; Tier 0 preflight GATE PASS. Awaiting user review before deck re-export, push, or social posting. |
| **Series** | `no (single comprehensive post)` |
| **Current Part** | n/a — single post `content/from-prompts-to-loop-engineering.md` |

> **Rebalance status-hygiene (2026-06-24):** the package is being re-worked for equal source/tool treatment (relevance-ranked, vendor-neutral), reversing the earlier first-party-leads framing. The blog, visuals, and all channel markdown are rebalanced; the **deck exports (HTML/PDF/PPTX)** and the **published blog HTML + mirrored visuals** are STALE until re-exported/re-mirrored. The pre-rebalance history is preserved in git history and in `content/publishing-log.md`. No push and no social posting until the user reviews the finished rebalance.

> **REVR visual-QA hygiene (2026-06-25):** the Reverse-Engineering Visual Review gate (`.github/skills/visual-reverse-review/SKILL.md`) has been run across ALL 10 visuals. `p1-03` was repaired at the renderer source and re-rendered; all 10 now carry a PASS REVR record under `content/visuals/revr/`. The **mirrored blog visuals** are refreshed and Tier 0 preflight is GATE PASS. The **deck exports (HTML/PDF/PPTX)** remain STALE pending re-export. No push and no social posting until the user reviews.

> **LinkedIn carousel asset — Step 6d (2026-06-25):** a self-contained, swipeable LinkedIn carousel was assembled from all 10 publish-ready visuals in blog-narrative order — cover + 10 captioned slides + CTA (12 pages, 1080×1350 / 4:5). Made a reusable pipeline step: skill `.github/skills/linkedin-carousel/SKILL.md`, generic manifest-driven renderer `scripts/visuals/build_carousel.py` (matplotlib `PdfPages`, shared design tokens, ASCII-only), curated manifest `content/visuals/loop-engineering-carousel.manifest.json`. Output: `content/visuals/loop-engineering-carousel.pdf`. Upload as a LinkedIn **document post**; put the canonical URL in the first comment. Manual-share asset; no automated social posting performed.

> **Canonical-home migration + dual index-linking — Step 10d (2026-06-25):** the post's canonical home moved from the `/content-creation/` mirror to the **personal site** `sendtoshailesh.github.io`. Rebuilt the page on the personal-site blog template (`blog-style.css`, dark theme, canonical/OG/Twitter meta, Home/Blog/Portfolio nav) at `blog/loop-engineering-ai-native-development.html`, copied all 10 visuals into `blog/visuals/`. Linked it from BOTH discovery surfaces: a new `.post-card` at the top of `blog/index.html` and a new `.blog-card` as the newest entry in the home `index.html` `<section id="insights">` `.blog-grid`. Canonical updated in `content/publishing-log.md` to `https://sendtoshailesh.github.io/blog/loop-engineering-ai-native-development.html`. The `web-publisher` agent now has an explicit **Step 3b (home #insights linking)** so future publishes update both surfaces. Personal-site repo edits require a manual `git add blog/ index.html && git commit && git push` to go live.

### Step Checklist

- [x] Step 0: Reference analysis — relevance-ranked, vendor-neutral (`content/reference-brief.md`: sources ordered by authority per claim, role-labeled primary/measurement/synthesis; verified Foundry/Copilot/Azure-git-ape/Aider/mini-swe-agent URLs live)
- [x] Step 1b: Content research (STORM) — folded into reference-brief synthesis
- [x] Steps 1-2: Strategy + outline — grounded in the most authoritative source per claim, treating all vendors and tools as equals
- [x] Step 2b: Scope assessment (single vs. series) — unchanged (single comprehensive post)
- [x] Step 2c: Multi-dimensional analysis — unchanged
- [x] Step 2d: Visual opportunity mapping — unchanged
- [x] Step 2e: Infographic art direction — unchanged
- [x] Step 3: Blog post draft — rebalanced for equal source/tool treatment (single relevance-ranked References list, no vendor-split sections); GATE PASS (0/0/0)
- [x] Step 3b: Visual assets — all 10 passed REVR; `p1-03` repaired at the renderer source (`content/visuals/render_loop_engineering.py`) and re-rendered (46 → 98), 9 others passed first read (94-98); fixed PNGs re-mirrored to `docs/blog/visuals/`
- [ ] Step 3b-img: hero/illustrative imagery (optional) — not used
- [x] Step 3c: Quality review — Tier 0 preflight GATE PASS; **REVR (Tier 2 visual gate) PASS** across all 10 visuals (PASS records under `content/visuals/revr/`)
- [x] Step 3d: SEO optimization — unchanged
- [x] Step 4a: Social distribution strategy — unchanged
- [x] Step 4a-visual: Visual-first asset pack — refreshed via re-render
- [x] Step 4: LinkedIn post — rebalanced (3 posts, plain + Unicode + first-comments): on-ramp lists Copilot/Aider/Claude Code as equals; harness defn cites VS Code on authority; projects present equal tool options; Post 3 lists git-ape as one inspectable loop alongside mini-swe-agent and Aider
- [x] Step 4c: Social platform selection — LinkedIn + Reel/Short + Slide deck + X + Medium/Substack
- [ ] Step 5: X/Twitter thread — skipped by user selection
- [x] Step 6b: Reel/Short video — rebalanced (shot list, voiceover, end-card, both caption blocks): tool-neutral on-ramp + equal tool options per project
- [x] Step 6c: Slide deck (HTML + PDF + PPTX) — markdown rebalanced (proof slide leads Stripe + lists git-ape/Aider/mini-swe-agent as equal readable loops; projects slide presents equal tool options); re-exported all three formats
- [x] Step 6d: LinkedIn carousel — consolidated all 10 finalized visuals into one swipeable document PDF (`content/visuals/loop-engineering-carousel.pdf`) via skill `linkedin-carousel` + renderer `scripts/visuals/build_carousel.py` + manifest
- [x] Step 7: Brand audit — token/voice consistency preserved across re-grounded channels
- [x] Step 7b: Grounded content review — sources verified live during reference analysis
- [ ] Step 8: YouTube script — skipped by user selection
- [x] Step 9: X/Twitter post — rebalanced primary CTA → tool-neutral ("point an agent at a failing test"); reply lists managed-runtime + gates options as equals
- [ ] Step 12: Medium/Substack distill
- [x] Step 10: Web publishing — **RE-MIRRORED (2026-06-24, rebalance)**: re-mirrored `docs/blog/loop-engineering-ai-native-development.html` from the rebalanced blog Markdown (neutralized why/harness/loop wording, proof section now "inspectable harnesses and the industry numbers" leading mini-swe-agent/Aider/git-ape as equals, projects present "Tools (pick one)", References consolidated into a single relevance-ranked list); re-copied redrawn `p1-03`/`p2-06` visuals to `docs/blog/visuals/`.
- [x] Step 10b: Citation-link remediation (2026-06-24) — inline source links in blog Markdown + References; mirrored into HTML; deterministic claim-citation guard in `scripts/pipeline/preflight_check.py`. Tier 0 preflight GATE PASS (0/0/0).
- [x] Step 10c: Web publish PUSHED LIVE (2026-06-25) — user-approved commit + push of REVR-fixed visuals (p1-03 46→98), rebalanced blog Markdown/HTML, REVR PASS records, and pipeline-doc edits to GitHub Pages. Live at the canonical URL.
- [x] Step 10d: Canonical-home migration + dual index-linking (2026-06-25) — republished onto the personal site `sendtoshailesh.github.io/blog/` (personal-site template), copied 10 visuals to `blog/visuals/`, prepended cards to BOTH `blog/index.html` (`.post-card`) and home `index.html` `#insights` (`.blog-card`), updated canonical in `content/publishing-log.md`, and added Step 3b (home #insights linking) to the `web-publisher` agent. **PUSHED LIVE (commit `1652cd5`, 13 files).** Live at `https://sendtoshailesh.github.io/blog/loop-engineering-ai-native-development.html`, linked from `/blog/` and `/#insights`.
- [ ] Step 11: Social publishing — HELD pending user review + explicit approval (no posting yet)
- [x] Step 12: Medium/Substack distill — rebalanced: proof leads Stripe + lists git-ape/Aider/mini-swe-agent as equal readable loops; harness/loop diagnostic cites VS Code on authority; 3 projects present equal tool options; single relevance-ranked References
- [ ] Step 13: Post-publish go/no-go (`post-publish-review`) — run after social publishing + measurement window; this run is `no-baseline` (published before the §4b Content hypothesis convention), seeded in `content/hypothesis-ledger.md`
- [ ] Step 14: Discover reflection (`post-run-reflection`) — harvest cut scope, open questions, unwritten parts, and the ledger verdict into `content/idea-queue.md` as ranked follow-ups
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

> Source groups below are organizational by type, not a precedence order; public sources verified 2026-06-22 (Phase 0 trend research). Full synthesis in `content/reference-brief.md` / `content/trend-research.md`. Re-verify every URL before direct citation.

**Author's own inspectable work (first-person voice):**
- Local: `agents-and-skills/automation-architecture.md`, `agents-and-skills/content-pipeline-flow.md`, `agents-and-skills/agent-definitions.md` — the agent/skill/instruction harness + review-gate loops that run this very content pipeline (a working loop-engineering example)

**Product & platform docs (Microsoft Foundry / Learn / dev blogs):**
- https://learn.microsoft.com/en-us/azure/foundry/agents/overview — What is Microsoft Foundry Agent Service? — agent runtime: loops, tools, runs
- https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent — Deploy your first hosted agent — one managed-runtime build-your-own on-ramp
- https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/runtime-components?tabs=py — Agents, conversations, responses: the Foundry agent loop components
- https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/ — Foundry IQ: unified knowledge + evaluators feeding the agent loop
- https://techcommunity.microsoft.com/blog/appsonazureblog/how-we-build-and-use-azure-sre-agent-with-agentic-workflows — How we build/use Azure SRE Agent with agentic workflows (production loop case study)

**Repos & coding surfaces (GitHub Copilot, Azure/git-ape, docs):**
- https://github.com/copilot — GitHub Copilot: the agentic coding surface (author's daily harness)
- https://github.com/Azure/git-ape — Azure/git-ape: platform-engineering framework for the agentic age (one public production repo the author works in)
- https://docs.github.com/en/copilot — GitHub Copilot docs: coding agent / CLI / Agent HQ (verify exact subpages during analysis)

**Independent measurement & expert synthesis:**

_Loop Engineering — Core (definition & the skill):_
- https://simonwillison.net/2025/Sep/30/designing-agentic-loops/ — Simon Willison "Designing agentic loops": names loop design as a discrete skill; "runs tools in a loop to achieve a goal"; the four design levers
- https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html — Kief Morris (Thoughtworks): inner/middle/outer loops, why-loop vs how-loop, humans outside/in/on the loop, "fix the artefact vs. fix the loop"
- https://www.anthropic.com/engineering/building-effective-agents — Anthropic: evaluator-optimizer loop, gates, stop conditions ("maximum number of iterations to maintain control")
- https://simonwillison.net/2025/Oct/7/vibe-engineering/ — Willison "Vibe engineering" (updated to "Agentic Engineering" Feb 2026): lists "designing agentic loops" as a core senior skill

_Inner-loop Validation / Self-correction:_
- https://www.infoq.com/news/2026/06/circleci-chunk-sidecars/ — CircleCI Chunk Sidecars: validation pulled into the agent's inner loop; "validation, not generation, is the bottleneck"
- https://www.infoq.com/news/2026/06/claude-code-harnesses/ — Anthropic Dynamic Workflows: named self-correction failure modes (agentic laziness, self-preferential bias, goal drift) + adversarial verification loops
- https://martinfowler.com/articles/build-own-coding-agent.html — Ben O'Mahony (Thoughtworks): buildable act->observe->verify loop with test-result-as-feedback

_Harness vs. Loop distinction:_
- https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html — Böckeler: harness = "everything except the model"; feed-forward vs feedback; quotes OpenAI on "environments, feedback loops, and control systems"
- https://www.infoq.com/podcasts/mcp-vibe-coding-harness-engineering/ — Böckeler podcast: one-year evolution narrative; harness = guides + sensors so the agent can self-correct
- https://martinfowler.com/articles/harness-engineering.html — Böckeler considered article: harness elements as "guides and sensors" + harness templates

_Eras / arc framing:_
- https://martinfowler.com/articles/exploring-gen-ai.html — Fowler "Exploring Generative AI" index: dated chronological map from autocomplete -> context -> harness -> loops
- https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html — Böckeler: the context-engineering middle era (lazy-loaded skills, MCP decline)
- https://openai.com/index/harness-engineering/ — OpenAI "Harness engineering": 1M-LOC / 5-month / no-typed-code case study (⚠ 403 to fetcher; corroborated indirectly, re-verify before direct citation)

_Quantified data & case studies:_
- https://www.infoq.com/news/2026/03/stripe-autonomous-coding-agents/ — Stripe "Minions": 1,300+ PRs/week, zero human-written code, "blueprints = deterministic code + flexible agent loops"; underpins $1T+ payment volume
- https://www.swebench.com/ — SWE-bench: 12.47% (Mar 2024) -> 76.8% (Claude 4.5 Opus, Feb 2026) under the same harness; mini-SWE-agent 65% in ~100 lines; per-task cost ~$0.05-$0.96

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
