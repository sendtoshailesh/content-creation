# Content Publishing Pipeline Redesign — Implementation Plan

## Problem Statement

The current pipeline publishes to social platforms with `[link]` placeholders never resolved, no Medium/Substack/LinkedIn Article generation, image references that prevent copy-paste, and no X/Twitter link placement protection. The redesigned pipeline makes GitHub Pages the canonical primary destination and produces text-only, copy-paste-ready summaries for all downstream platforms pointing back to it.

## Approach: Scenario B — Refactor Publishing Stage

Extend the existing pipeline with two new steps (10a and 12) while updating existing agents (web-publisher, social-publisher) to enforce canonical URL injection and text-only constraints.

**New publishing sequence:**
```
Step 10:  web-publisher      → Publish HTML to GitHub Pages; write canonical URL to content/publishing-log.md
Step 10a: [within social-publisher] → Inject canonical URL from publishing-log.md into all [link] placeholders in content/*.md
Step 11:  social-publisher   → LinkedIn/X-Twitter/Reddit with real URL + platform-safe placement
Step 12:  platform-distiller → Medium excerpt, Substack excerpt, LinkedIn Article (text-only, no images)
```

## Phase 1: Infrastructure (create new files)

### 1.1 — Create `content/publishing-log.md`
Template file that web-publisher writes to after each publish. Tracks canonical URLs per series part. Used by social-publisher (Step 10a) to replace `[link]` placeholders.

**Format:**
```markdown
| Part | Slug | Canonical URL | Published |
|------|------|--------------|-----------|
| 1 | ai-code-assistant-context-engineering-part-1 | https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html | 2026-05-12 |
```

### 1.2 — Create `.github/agents/platform-distiller.agent.md`
New agent (Step 12). Reads the full blog markdown from `content/*.md` and `content/publishing-log.md`, then generates three text-only, copy-paste-ready derivative pieces:
- **Medium excerpt** (700–900 words): Excerpt + canonical URL at bottom for Import tool. Opens with the primary insight, includes key data points inline (no charts). Ends: `Read the full post at [canonical URL]`.
- **Substack excerpt** (300–500 words): Short hook + 3–5 key bullets + canonical URL. No republish of full content — protects against duplicate-content risk.
- **LinkedIn Article** (700–900 words): Unique angle piece (e.g., "what I learned building X" framing, NOT a republish). Links to canonical URL in opening paragraph and conclusion.

**Text-only enforcement:** Agent prompt explicitly forbids `![]`, `<img`, `.png`, `.svg`, `.jpg`, `content/visuals/` in output. All chart data expressed as inline numbers, ratios, or before/after text.

**Output paths:**
- `content/medium-post-{slug}.md` (with START/END COPY markers)
- `content/substack-post-{slug}.md` (with START/END COPY markers)
- `content/linkedin-article-{slug}.md` (with START/END COPY markers)

### 1.3 — Create `docs/series/ai-code-assistant-optimization.html`
Series index hub page in the GitHub Pages site (mirrored in the `sendtoshailesh.github.io` repo at `blog/series/ai-code-assistant-optimization.html`). Establishes topical authority. Links all three parts. All social posts for series content link to this page as the primary URL.

**URL:** `https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html`

---

## Phase 2: Agent Updates (update existing agents)

### 2.1 — Update `web-publisher.agent.md`
After publishing each HTML page, add Step 5: write canonical URL to `content/publishing-log.md`:
- Append a row to the markdown table with: part number (from frontmatter), slug, full canonical URL, publish date.
- If publishing-log.md doesn't exist, create it with the header row first.

### 2.2 — Update `social-publisher.agent.md`
Three enforcement changes:
1. **Step 10a (URL injection):** Before running social tasks, read `content/publishing-log.md` and replace every `[link]` occurrence in all `content/*.md` social post files with the actual canonical URL.
2. **X/Twitter text-only:** Remove all references to "Attach image to tweet 1" or image attachments. The thread is text-only.
3. **LinkedIn link suppression protection:** Add instruction: "Post body must be substantive. Place the canonical URL at the very end of the LinkedIn post (after all body copy), OR post it as the first comment after publishing — never mid-body."
4. **Reddit text post:** Add instruction: "Reddit must be a substantive text post (500–800 words), NOT a link post. Link to the canonical URL at the bottom of the post only."

### 2.3 — Update `agents-and-skills/*.md`
Add `platform-distiller` entry to the agent registry:
- Step 12 in the pipeline
- Description: Generates Medium excerpt, Substack excerpt, and LinkedIn Article text-only summaries pointing to the GitHub Pages canonical URL

---

## Phase 3: Config Updates

### 3.1 — Update `content/pipeline-config.md`
Five additions:
1. **Social Platform Selection:** Add Medium, Substack, LinkedIn Article checkboxes (with explanatory note about each platform's canonical risk level)
2. **Canonical URL section:** Add `### Canonical URL` block with GitHub Pages base URL and the series index URL
3. **Step checklist:** Add `Step 10a: URL injection` and `Step 12: Platform distillation` rows to the step checklist table
4. **Publish sequence block:** Add `### Publish Sequence` with Day 0–7+ schedule (Day 0: GitHub Pages + Medium Import + LinkedIn Post; Day 1: X/Twitter; Day 3–4: Substack; Day 5–7: Reddit; Day 7+: LinkedIn Article)
5. **Published URLs table:** Expand to include Medium, Substack, LinkedIn Article rows

---

## Phase 4: Retroactive Content Fixes (3-part series)

### 4.1 — Populate `content/publishing-log.md` with existing Part 1–3 URLs
The three HTML pages are already live. Back-fill their canonical URLs:
- Part 1: `https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html`
- Part 2: `https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html`
- Part 3: `https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html`

### 4.2 — Fix existing social posts (parts 1–3)
Files: `content/linkedin-post-part1.md`, `content/linkedin-post-part2.md`, `content/linkedin-post-part3.md`, `content/x-twitter-thread.md` (and parts 2/3 if they exist).
- Replace `[link]` with the appropriate canonical URL from publishing-log.md
- Remove any "Attach image" / image posting instructions from X/Twitter files
- Move LinkedIn URL to end-of-post (not mid-body)

### 4.3 — Generate platform summaries for 3-part series
Run platform-distiller against each blog post to produce:
- `content/medium-post-part{1,2,3}.md`
- `content/substack-post-part{1,2,3}.md`
- `content/linkedin-article-part{1,2,3}.md`
All must pass text-only validation before commit.

---

## Phase 5: Validation

- [ ] All `content/medium-*.md`, `content/substack-*.md`, `content/linkedin-article-*.md` contain no image references (`![]`, `.png`, `.svg`, `.jpg`, `content/visuals/`, `<img`)
- [ ] All social post files have canonical URLs (no remaining `[link]` placeholders)
- [ ] `content/publishing-log.md` has correct entries for all 3 parts
- [ ] `docs/series/ai-code-assistant-optimization.html` renders correctly
- [ ] `pipeline-config.md` step checklist has Step 10a and Step 12
- [ ] All platform distiller outputs have `── START COPY ──` / `── END COPY ──` markers

---

## Parallelism Notes

- Phase 1.1, 1.2, 1.3 can run in parallel (independent files)
- Phase 2.1, 2.2, 2.3 can run in parallel (independent agent files)
- Phase 3.1 is sequential (single config file)
- Phase 4.1 must complete before 4.2 and 4.3
- Phase 4.2 and 4.3 can run in parallel (different content files)
- Phase 5 runs last

## Key Constraints

- **Two repos in play**: Content pipeline lives in `how2genmodel/` (repo: `sendtoshailesh/content-creation`). GitHub Pages source is `/Users/shaileshmishra/my-docs/my-proj/sendtoshailesh.github.io` (repo: `sendtoshailesh/sendtoshailesh.github.io`). Series index page must be created in the Pages repo, not in docs/ here.
- **No images in platform summaries**: Enforced by agent prompt + validation step
- **X/Twitter link suppression**: Link goes in last tweet only (already correct in existing files); remove image posting notes
- **LinkedIn reach suppression**: Canonical URL at end of post body or first comment — never inline
- **Medium canonical**: Use Import tool (not paste) to auto-set canonical to GitHub Pages URL
- **Substack**: Excerpt only (300–500 words) — no canonical protection available
