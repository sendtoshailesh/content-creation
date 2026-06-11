# Pipeline Config — Python

> Topic-scoped pipeline. The orchestrator reads this when run with topic `python`
> (e.g. `/topic-pipeline python`). Outputs land in this workspace
> (`content/topics/python/`). Persistent files: `feed-sources.md`, `idea-queue.md`.

## Pipeline Status

| Field | Value |
|-------|-------|
| **Status** | `not-started` |
| **Topic** | Python |
| **Topic slug** | `python` |
| **Output path** | `content/topics/python/` |
| **Started** | _(set on first run)_ |
| **Current Step** | _(set on first run)_ |
| **Series** | `pending-assessment` |

### Step Checklist

- [ ] Step 0: Reference analysis
- [ ] Steps 1-2: Creative brief + strategy + outline
- [ ] Step 2b-2e: Scope, dimensions, visual map, art direction
- [ ] Step 3: Blog post
- [ ] Step 3b: Visual assets
- [ ] Step 3b-img: Hero/illustrative imagery (optional)
- [ ] Step 3c-3d: Quality review + SEO
- [ ] Step 4: Social distribution
- [ ] Step 7: Brand audit (severity-gated)
- [ ] Step 10: Web publishing
- [ ] Step 11: Social publishing

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

## Output Preferences

- **Blog target length**: ~3,000 words per part
- **Output path**: `content/topics/python/`

### Social Platform Selection

- [x] LinkedIn (always)
- [ ] X/Twitter
- [ ] Reddit
- [ ] Reel/Short video
- [ ] YouTube

## Online References

> Topic source material is seeded in `idea-queue.md`. Add specific reference URLs here
> before a run, or let `@reference-discovery` populate them.

<!-- - [description](URL) — what to extract -->
