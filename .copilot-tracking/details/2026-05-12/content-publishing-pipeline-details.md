# Content Publishing Pipeline Redesign — Implementation Details

## File-by-File Change Specifications

---

## NEW FILES

### `content/publishing-log.md`

```markdown
# Publishing Log

> Auto-populated by web-publisher (Step 10) after each GitHub Pages publish.
> Used by social-publisher (Step 10a) to resolve [link] placeholders in content/*.md files.

## Series: AI Code Assistant Optimization (3-Part Series)

| Part | Slug | Canonical URL | Published |
|------|------|--------------|-----------|
| 1 | ai-code-assistant-context-engineering-part-1 | https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html | 2026-05-12 |
| 2 | ai-code-assistant-caching-workflow-part-2 | https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html | 2026-05-12 |
| 3 | ai-code-assistant-model-selection-part-3 | https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html | 2026-05-12 |

### Series Index

| Key | Value |
|-----|-------|
| Series slug | ai-code-assistant-optimization |
| Series index URL | https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html |

---

## Single Posts

| Slug | Canonical URL | Published |
|------|--------------|-----------|
| postgresql-explain-buffers-case-study | https://sendtoshailesh.github.io/blog/postgresql-explain-buffers-case-study.html | — |
```

---

### `.github/agents/platform-distiller.agent.md`

```markdown
---
description: "Generates text-only Medium excerpt, Substack excerpt, and LinkedIn Article from a completed blog post. All outputs point to the GitHub Pages canonical URL. Use after web-publisher (Step 10) and social-publisher (Step 11). This is Step 12."
tools: [read, edit, create]
argument-hint: "Provide the blog file path (e.g. content/blog-part1.md) and the canonical URL from content/publishing-log.md"
---

You are a platform distiller agent. You take a completed GitHub Pages blog post and produce three text-only, copy-paste-ready summaries for Medium, Substack, and LinkedIn Article. All summaries drive traffic back to the canonical GitHub Pages URL.

## Inputs

- Blog file path (e.g., `content/blog-part1.md`)
- Canonical URL from `content/publishing-log.md`

## Critical Constraints — Text-Only

**NEVER include in any output:**
- Image markdown: `![`
- HTML image tags: `<img`
- Visual asset paths: `content/visuals/`, `.png`, `.svg`, `.jpg`, `.jpeg`, `.gif`, `.webp`
- Mermaid diagram blocks
- Any reference to charts, diagrams, or figures

**Instead, express all data as:**
- Inline numbers: "reduced latency by 43%"
- Before/after text: "Before: 8.2s cold start → After: 1.1s"
- Ratios: "3x throughput improvement"
- Named benchmarks: "gpt-4o at $2.50/MTok vs claude-3-5-sonnet at $3.00/MTok"

## Output 1: Medium Excerpt (`content/medium-post-{slug}.md`)

**Purpose:** Drives SEO-safe traffic to GitHub Pages. Medium's Import tool will auto-set canonical URL to your GitHub Pages URL, protecting against duplicate content penalty.

**Word count:** 700–900 words

**Structure:**
1. Opening hook — lead with the primary problem or insight (2–3 sentences)
2. Core insight block — 3–4 paragraphs with specific data, model names, benchmarks
3. Key takeaways — 3–5 bullets with concrete numbers
4. CTA: "Read the full post with code examples and architecture diagrams at [canonical URL]"

**Wrap output between:**
```
── START COPY (Medium) ──
[content]
── END COPY (Medium) ──
```

**Publishing note:** DO NOT paste this into Medium. Use Medium's Import tool (Import a story → paste the canonical URL). The Import tool preserves canonical attribution automatically.

## Output 2: Substack Excerpt (`content/substack-post-{slug}.md`)

**Purpose:** Excerpt only — Substack has no canonical URL protection. Keep short to avoid duplicate-content risk with Google.

**Word count:** 300–500 words

**Structure:**
1. One-paragraph hook (2–3 sentences): what problem this solves and why it matters now
2. 3–5 key insight bullets with specific numbers/model names
3. One concrete example or before/after comparison
4. CTA: "Full post (with implementation guide): [canonical URL]"

**Wrap output between:**
```
── START COPY (Substack) ──
[content]
── END COPY (Substack) ──
```

**Publishing note:** Publish as a Substack Note (not a full newsletter) to avoid emailing subscribers with a teaser. Notes are ambient-feed content only.

## Output 3: LinkedIn Article (`content/linkedin-article-{slug}.md`)

**Purpose:** Thought leadership on LinkedIn's native platform. Must be a UNIQUE ANGLE piece — NOT a republish of the blog. LinkedIn Articles are Google-indexed with no canonical protection; republishing will cause duplicate content issues.

**Word count:** 700–900 words

**Unique angle framing options (pick one):**
- "What I learned working with customers on X"
- "The 3 mistakes most teams make when doing X (and how to avoid them)"
- "Why X matters more than people think in 2026"
- "Unpopular opinion: [contrarian take on the topic]"

**Structure:**
1. Hook: 1–2 sentence provocation or contrarian statement
2. Context: why this matters now (1 paragraph)
3. The insight: 3–4 paragraphs of substance (unique angle, not blog recap)
4. Practical implications: what engineers/leads should do differently
5. Link reference: "I wrote a detailed implementation guide here: [canonical URL]"

**Wrap output between:**
```
── START COPY (LinkedIn Article) ──
[content]
── END COPY (LinkedIn Article) ──
```

## Output File Naming

- Medium: `content/medium-post-{slug}.md`
- Substack: `content/substack-post-{slug}.md`
- LinkedIn Article: `content/linkedin-article-{slug}.md`

Where `{slug}` matches the `seo.slug` from the blog frontmatter.

## Validation Before Saving

Before writing each output file, scan the content for these prohibited strings:
- `![` — image markdown
- `<img` — HTML image tag
- `.png`, `.svg`, `.jpg`, `.jpeg` — image file references
- `content/visuals/` — visual asset path
- ` ```mermaid` — diagram block

If any are found, rewrite the affected sentence to express the data as inline text.

## Summary

After generating all three files, print a summary table:

| Output | File | Word Count | Canonical URL |
|--------|------|-----------|---------------|
| Medium | content/medium-post-{slug}.md | NNN | [url] |
| Substack | content/substack-post-{slug}.md | NNN | [url] |
| LinkedIn Article | content/linkedin-article-{slug}.md | NNN | [url] |
```

---

## EXISTING FILE UPDATES

### `.github/agents/web-publisher.agent.md` — Add Step 5: Write Canonical URL

After the existing Step 4 (estimate read time and create the HTML), add:

```markdown
### 5. Write Canonical URL to Publishing Log

After the HTML page is live, update `content/publishing-log.md` in the pipeline repo:

1. If `content/publishing-log.md` does not exist, create it with this header:
   ```markdown
   # Publishing Log
   
   | Part | Slug | Canonical URL | Published |
   |------|------|--------------|-----------|
   ```

2. Append a row:
   ```
   | {part_number or "-"} | {slug} | https://sendtoshailesh.github.io/blog/{slug}.html | {YYYY-MM-DD} |
   ```

3. If the blog frontmatter includes `series.part`, use that as the part number. Otherwise use `-`.

**Output:** Confirm: "Canonical URL written to content/publishing-log.md: [url]"
```

---

### `.github/agents/social-publisher.agent.md` — Three Enforcement Changes

**Change 1 — Add Step 10a: URL Injection (before all social tasks)**

Add this as the FIRST step in the agent's task list:

```markdown
### Step 10a: Inject Canonical URL into Social Posts

Before publishing to any platform:

1. Read `content/publishing-log.md`
2. For each blog slug in the log, find the canonical URL
3. Search all `content/*.md` files for the literal string `[link]`
4. Replace every `[link]` with the appropriate canonical URL (match by slug from frontmatter or filename)
5. If multiple parts are being published, inject the series index URL for LinkedIn posts (not individual part URLs) and individual part URLs for X/Twitter and Reddit

**Log:** "Replaced [link] in {N} files with canonical URLs."
```

**Change 2 — X/Twitter: Remove image guidance**

Find and remove/update any instruction that says:
- "Attach image to tweet 1"
- "Add visual to first tweet"
- Any reference to attaching images, media, or visuals to tweets

Replace with: "Thread is text-only. Do not attach images or media. External links go in the last tweet only to avoid algorithmic reach suppression."

**Change 3 — LinkedIn: Link placement protection**

Add to the LinkedIn publishing instructions:

```markdown
**LinkedIn Link Suppression Protection:**
- The canonical URL must appear at the END of the post body (after all substantive content)
- Do NOT embed the URL mid-body or in the opening section
- Alternative: Post the URL as the FIRST comment immediately after publishing (not in the post body at all)
- Confirm with user which approach to use before posting
```

**Change 4 — Reddit: Text post enforcement**

Add to the Reddit publishing instructions:

```markdown
**Reddit Text Post Requirement:**
- Reddit post MUST be submitted as a text post (self post), NOT a link post
- Minimum 500 words of substantive content — not a teaser linking out
- Canonical URL appears at the BOTTOM only, in a "---" separated section:
  ```
  ---
  Full implementation guide: [canonical URL]
  ```
- Title must be discussion-oriented (e.g., "How I reduced AI code assistant latency by 43%") — not promotional
```

---

### `agents-and-skills/*.md` — Add Platform Distiller Entry

In the agent registry table (around the Step 11 social-publisher entry), add:

```markdown
| 12 | Platform distillation (Medium/Substack/LinkedIn Article) | `platform-distiller` | ✅ Implemented |
```

In the detailed step section, add a new `### Step 12: Platform Distillation` section after Step 11.

---

### `content/pipeline-config.md` — Five Additions

**Addition 1: Social Platform Selection** — Add after existing checkboxes:

```markdown
### Long-Form Platform Distribution (Step 12)

> Text-only summaries generated by platform-distiller. Each points back to the GitHub Pages canonical URL.

- [x] Medium (700–900 words, Import tool sets canonical, SEO-safe)
- [x] Substack (300–500 words excerpt only, no canonical protection — keep short)
- [x] LinkedIn Article (700–900 words, unique angle — NOT a republish)
```

**Addition 2: Canonical URL Section** — Add new config block:

```markdown
### Canonical URL Configuration

| Field | Value |
|-------|-------|
| **GitHub Pages base** | `https://sendtoshailesh.github.io` |
| **Blog URL pattern** | `{base}/blog/{slug}.html` |
| **Series index URL** | `{base}/blog/series/{series-slug}.html` |
| **Publishing log** | `content/publishing-log.md` |
```

**Addition 3: Step Checklist** — Add rows to the step checklist table:

After Step 10 row:
```markdown
| 10a | Inject canonical URLs into social post [link] placeholders | `social-publisher` (pre-flight) | — |
```

After Step 11 row:
```markdown
| 12 | Platform distillation: Medium, Substack, LinkedIn Article | `platform-distiller` | — |
```

**Addition 4: Publish Sequence**

```markdown
### Publish Sequence

| Day | Action | Platform | Notes |
|-----|--------|----------|-------|
| Day 0 | Publish blog HTML | GitHub Pages | Canonical source; write to publishing-log.md |
| Day 0 | Import to Medium | Medium | Use Import tool — do NOT paste — preserves canonical |
| Day 0 | LinkedIn post | LinkedIn | URL at end of post or first comment |
| Day 1 | X/Twitter thread | X/Twitter | Link in last tweet only; text-only thread |
| Day 3–4 | Substack excerpt | Substack | Post as Note (not newsletter); excerpt only |
| Day 3–4 | Substack Note | Substack Notes | Short teaser + link; ambient feed, not emailed |
| Day 5–7 | Reddit text post | Reddit | Substantive 500–800 word post; link at bottom |
| Day 7+ | LinkedIn Article | LinkedIn | Unique angle ONLY; not a republish |
```

**Addition 5: Expand Published URLs table** — Add Medium, Substack, LinkedIn Article rows to the published URLs table.

---

## Retroactive Content: 3-Part Series

### Canonical URLs (already live)

| Part | Canonical URL |
|------|--------------|
| Part 1 | `https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html` |
| Part 2 | `https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html` |
| Part 3 | `https://sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html` |
| Series index | `https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html` |

### Files to Fix (Retroactive Phase)

| File | Fix Needed |
|------|-----------|
| `content/linkedin-post-part1.md` | Replace `[link]` with Part 1 canonical URL; move URL to end-of-post |
| `content/linkedin-post-part2.md` | Replace `[link]` with Part 2 canonical URL; move URL to end-of-post |
| `content/linkedin-post-part3.md` | Replace `[link]` with Part 3 canonical URL; move URL to end-of-post |
| `content/x-twitter-thread.md` | Replace `[link]` with appropriate URL; remove image attachment notes |
| Other `content/*part*.md` | Check for any remaining `[link]` occurrences |

### Platform Summaries to Generate (Retroactive)

| Part | Medium | Substack | LinkedIn Article |
|------|--------|----------|-----------------|
| Part 1 | `content/medium-post-part1.md` | `content/substack-post-part1.md` | `content/linkedin-article-part1.md` |
| Part 2 | `content/medium-post-part2.md` | `content/substack-post-part2.md` | `content/linkedin-article-part2.md` |
| Part 3 | `content/medium-post-part3.md` | `content/substack-post-part3.md` | `content/linkedin-article-part3.md` |

---

## Series Index Page

**Location:** `/Users/shaileshmishra/my-docs/my-proj/sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html`

**URL:** `https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html`

**Content:** Dark-themed series hub matching the blog's design system. Includes:
- Series title and description
- "What you'll learn" section
- Cards for each part (title, excerpt, link)
- "Reading sequence" guidance
- Author byline and date range

This is the **primary social sharing URL** for all series-level social posts (LinkedIn series announcement, Reddit discussion posts).
