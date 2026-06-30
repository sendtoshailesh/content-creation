# Pipeline Config — GitHub CLI for Copilot Cost Optimization

> Topic-scoped pipeline. The orchestrator reads this when run with topic `github-cli-copilot-cost`
> (e.g. `/topic-pipeline github-cli-copilot-cost`). Outputs land in this workspace
> (`content/topics/github-cli-copilot-cost/`). Persistent files: `feed-sources.md`, `idea-queue.md`.

## Pipeline Status

| Field | Value |
|-------|-------|
| **Status** | `in-progress` |
| **Autonomous** | `auto` (off = never; on = always unattended; auto = unattended only on an `auto/*`, `autorun/*`, or `unattended/*` branch or when the prompt asks for it) |
| **Topic** | Different scenarios to showcase how GitHub CLI commands can save cost and optimise AI (Copilot) usage |
| **Topic slug** | `github-cli-copilot-cost` |
| **Output path** | `content/topics/github-cli-copilot-cost/` |
| **Started** | 2026-06-30 |
| **Current Step** | Step 0 — starting autonomous pipeline run |
| **Series** | `pending-assessment` |

### Step Checklist

- [ ] Step 0: Reference analysis
- [ ] Steps 1-2: Creative brief + strategy + outline
- [ ] Step 2b-2e: Scope, dimensions, visual map, art direction
- [ ] Step 3: Blog post
- [ ] Step 3b: Visual assets
- [ ] Step 3b-img: Hero/illustrative imagery (optional)
- [ ] Step 3c: Quality review
- [ ] Step 3e: Grounded content review (web-verified)
- [ ] Step 3d: SEO optimization
- [ ] Step 4a: Social distribution strategy
- [ ] Step 4a-visual: Visual-first pack (carousel/exhibit via visual-pack-generator)
- [ ] Step 4: Social posts (LinkedIn always; visual-first + canonical link)
- [ ] Step 6b: Reel/Short video (60-90 sec)
- [ ] Step 7: Brand audit (severity-gated)
- [ ] Step 10: Web publishing
- [ ] Step 11: Social publishing
- [ ] Step 12: Platform distillation (Medium / Substack / LinkedIn Article + canonical URL)

**Status values:** `not-started` | `in-progress` | `completed` | `blocked`

---

## Image Generation (hybrid AI imagery)

| Field | Value |
|-------|-------|
| **mode** | `programmatic` |
| **provider** (ai mode) | `openai` |
| **model** (ai mode) | `gpt-image-1` |
| **size** | `1024x1024` |
| **max_images_per_run** | `3` |

## Visual-First Distribution

> Step 4a-visual generates a visual asset pack before social/long-form distribution.
> Read by: `visual-pack-generator` skill, `social-linkedin`, `social-twitter`, `platform-distiller`.

| Field | Value |
|-------|-------|
| **distillation_persona_mode** | `practitioner` |
| **distillation_slug** | `github-cli-copilot-cost` |

> `practitioner` = 10-slide LinkedIn carousel (1080×1080). `executive` = 3–5 exhibits (1200×627).
> Output: `content/visuals/distilled/github-cli-copilot-cost-practitioner/`.

## Output Preferences

- **Blog target length**: ~2,500 words (scenario-driven, concrete CLI commands, real cost numbers)
- **Output path**: `content/topics/github-cli-copilot-cost/`

### Social Platform Selection

- [x] LinkedIn (always — visual-first when a pack exists, links to canonical blog)
- [ ] X/Twitter
- [ ] Reddit
- [x] Reel/Short video (60-90 sec)
- [ ] YouTube

### Long-Form Platform Distribution (Step 12)

> `platform-distiller` produces ONE unified excerpt for all three, pointing to the GitHub Pages
> canonical URL. Visual-first when a distilled pack exists; text-only otherwise.

- [x] Medium (700–900 words; Import tool sets canonical — SEO safe)
- [x] Substack (300–500-word excerpt / Note)
- [x] LinkedIn Article (700–900 words, distinct angle — not a republish of the LinkedIn post)

## Online References

> Topic source material seeded from web research. Add specific reference URLs here before a run.

- [GitHub Copilot seat assignment automation](https://docs.github.com/en/copilot/reference/copilot-billing/seat-assignment) — official docs on seat management
- [Administering Copilot CLI for enterprises](https://docs.github.com/en/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise) — enterprise CLI controls
- [GitHub Copilot metrics API](https://docs.github.com/en/rest/copilot/copilot-metrics) — usage data extraction via API
- [AutoKitteh: Copilot seat management case study](https://autokitteh.com/technical-blog/practical-automation-managing-your-teams-github-copilot-seats/) — automation workflow saving 15-25% costs
- [Visualize ROI of GitHub Copilot usage](https://devblogs.microsoft.com/all-things-azure/visualize-roi-of-your-github-copilot-usage-how-it-works/) — ROI measurement patterns
- [How CLI achieved 50% cost savings](https://completeaitraining.com/news/how-cli-achieved-50-cost-savings-and-faster-product/) — real cost savings case study
