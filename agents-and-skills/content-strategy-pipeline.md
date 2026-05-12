# Content Strategy Pipeline — Agent & Task Record

## Objective

Build a repeatable content pipeline that takes a single technical topic and produces a full distribution package: long-form blog (single post or multi-part series), social posts (LinkedIn + user-selected platforms), optional reel/short video, and YouTube script. Each step is a discrete, automatable task suitable for an agent or skill.

---

## Pipeline Overview

| Step | Task | Agent/Skill | Status |
|------|------|-------------|--------|
| 0a | Reference Discovery | `reference-discovery` | ✅ Implemented |
| 0b | Market Intelligence | `trend-researcher` | ✅ Implemented |
| 1 | Clarifying Questions | `content-strategist` | ✅ Implemented |
| 2 | Strategy & Outline | `content-strategist` | ✅ Implemented |
| 2b | Scope Assessment (single vs. series) | `content-scope-assessment` skill | ✅ Implemented |
| 2c | Multi-Dimensional Analysis (persona, practice, WAF) | `multi-dimensional-analysis` skill | ✅ Implemented |
| 3 | Full Blog Post (or Part N) | `blog-writer` | ✅ Implemented |
| 3b | Visual Generation | `visual-renderer` | ✅ Implemented |
| 3c | Quality Overhaul | `quality-reviewer` | ✅ Implemented |
| 3d | SEO Optimization | `seo-optimizer` | ✅ Implemented |
| 4a | Social Distribution Strategy | `social-strategist` | ✅ Implemented |
| 4b | LinkedIn Post (always) | `social-linkedin` | ✅ Implemented |
| 4c | Platform Selection | (orchestrator asks user) | ✅ Implemented |
| 5 | X/Twitter Post — visual-first (if selected) | `social-twitter` | ✅ Implemented |
| 6 | Reddit Post — visual-first (if selected) | `social-reddit` | ✅ Implemented |
| 6b | Reel/Short Video (if selected) | `reel-video` | ✅ Implemented |
| 7 | Brand Audit | `brand-guardian` | ✅ Implemented |
| 8 | YouTube Script (if selected) | `video-scriptwriter` | ✅ Implemented |
| 9 | Content Repurposing (optional) | `content-repurposer` | ✅ Implemented |
| 10 | Publish to GitHub Pages | `web-publisher` | ✅ Implemented |
| 10a | Inject canonical URLs into `[link]` placeholders (pre-flight) | `social-publisher` | ✅ Implemented |
| 11 | Social Media Publishing (API) | `social-publisher` | ✅ Implemented |
| 12 | Platform distillation: Medium + Substack (visual-first), LinkedIn Article (text-only unique angle) | `platform-distiller` | ✅ Implemented |

### Skills Inventory

| Skill | Purpose |
|-------|---------|
| `content-scope-assessment` | Score topic comprehensiveness (0-16 scale), recommend single post vs. multi-part series |
| `multi-dimensional-analysis` | Analyze topic across persona, best practice, and Azure WAF pillar dimensions |
| `reference-analysis` | Fetch and synthesize online reference URLs into a reference brief |
| `unicode-formatting` | Format text with Unicode Mathematical Bold/Italic for LinkedIn and X/Twitter |
| `visual-rendering` | Generate PNG (matplotlib), SVG (Python), and Mermaid diagrams |

---

## Completed Steps — Detailed Record

### Step 0a: Reference Discovery (`reference-discovery`)

**Objective:** Search the web for high-quality references and let the user curate which sources feed into the content pipeline.

**Task:**
- Generate 2-3 targeted search queries per reference category (12-18 total queries)
- Execute batch search via Azure Bing Web Search API (falls back to Copilot web tool)
- Present results grouped by category with numbered references (title, URL, snippet, date)
- User selects/rejects references interactively — supports multiple curation rounds
- Write accepted references to `content/pipeline-config.md` under the correct category headings

**Search Backend:**
- Primary: `scripts/bing-search.py` (Azure Bing Web Search API v7)
- Fallback: Copilot built-in `web` tool

**Categories:** General content, Industry Reports & Benchmarks, Competitor / Related Articles, Pricing Pages & Documentation, Case Studies & Examples, Research Papers

**Output:** Curated reference URLs in `content/pipeline-config.md`

**Trigger:** Run `@reference-discovery [topic]` or `/discover-references` — suggested automatically by the pipeline orchestrator when reference URLs are empty.

---

### Step 1: Clarifying Questions (`content-strategist`)

**Objective:** Gather context, audience, tone, and distribution goals before writing.

**Task:**
- Ask 8–12 targeted questions covering: topic scope, audience (IC engineers vs. leaders), tone (tutorial vs. opinion), distribution channels, existing assets, and success metrics.
- Capture answers as structured input for Step 2.

**Output:** Structured brief with audience, tone, distribution plan, and topic boundaries.

---

### Step 2: Strategy & Outline (`content-strategist`)

**Objective:** Produce a content strategy document and detailed blog outline.

**Task:**
- Define content angle, key differentiator, and hook.
- Create section-by-section outline with subheadings, key points per section, and visual placement markers.
- Map distribution: which sections feed which social posts.

**Output:** Strategy doc + blog outline with visual markers.

---

### Step 3: Full Blog Post (`blog-writer`)

**Objective:** Write a publication-ready technical blog post.

**Task:**
- Write ~3,000-word blog with punchy opening ($140K cost hook), real model names (GPT-4o, Claude Opus/Sonnet/Haiku, Gemini, o1/o3, Llama 3, Mistral), actual cost benchmarks, case study ($41K→$14K), 7-dimension framework, 30-day playbook, and pre-launch checklist.
- Integrate SVG visuals via `<details>` collapsible blocks.
- Use concrete data points — no vague generalities.

**Output:** `content/choose-GenAI-model-field-guide.md`

**Quality Bar:**
- Every claim has a specific number or model name.
- Tier pricing table with real per-1M-token costs.
- Case study with before/after metrics.
- Actionable 30-day playbook with weekly milestones.

---

### Step 3b: Visual Generation (`visual-renderer`)

**Objective:** Produce all diagrams, charts, and visual aids for the blog.

**Tasks:**
1. **Mermaid diagrams** (4 `.mmd` files): model-selection-framework, model-routing-flow, case-timeline, 30-day-process.
2. **PNG renders** (9 images at 320 DPI via matplotlib): model-selection-framework, model-routing-flow, comparison-matrix, tradeoff-2x2, case-timeline, pitfalls-mitigation, swimlane-30day, checklist-card, decision-funnel.
3. **SVG graphics** (3 files): tradeoff-2x2, decision-funnel, checklist-card.

**Tools & Config:**
- Python 3.14.3, matplotlib 3.10.8, venv at `.venv`
- Design token system: 15 named colors (BG=#ffffff, ACCENT=#1f6feb, ACCENT_2=#0d9488, WARN=#dc2626, TEXT=#1e293b, etc.)
- Font: Helvetica Neue, 320 DPI output
- Renderer: `content/visuals/render_placeholders.py` (9 functions)
- SVG writer: `content/visuals/write_svgs.py` (3 SVGs)

**Output:** `content/visuals/` — 9 PNGs + 3 SVGs + 4 Mermaid files

---

### Step 3c: Quality Overhaul (`quality-reviewer`)

**Objective:** Review and upgrade content + visuals to professional standard.

**Tasks:**
- Rewrote entire blog — replaced generic advice with concrete benchmarks.
- Rebuilt renderer with full design token system.
- Fixed Unicode glyph issues (→ and ✓ replaced with ASCII alternatives).
- Fixed SVG corruption from heredoc approach — wrote Python script instead.
- Integrated SVGs into blog via `<details><summary>` collapsible blocks.

**Trigger:** User feedback "quality of content is very low."

---

### Step 4: LinkedIn Post (`social-linkedin`)

**Objective:** Create a LinkedIn post optimized for the platform's algorithm and audience.

**Tasks:**
1. Write plain-text version with story hook, numbered takeaways, case study, and CTA.
2. Create Unicode-formatted version using Mathematical Bold (𝗕𝗼𝗹𝗱) and Italic (𝘐𝘵𝘢𝘭𝘪𝘤) characters that render natively on LinkedIn.
3. Apply formatting: ━━━ separators, ▸ sub-bullets, ⚠️📊 emoji anchors.

**Formatting Strategy:**
- Unicode Mathematical Bold Sans-Serif for emphasis/key phrases.
- Unicode Mathematical Italic Sans-Serif for contrast/counterpoints.
- Copy-paste ready between ── START ── and ── END ── markers.

**Output:**
- `content/linkedin-post.md` (plain text)
- `content/linkedin-post-formatted.md` (Unicode formatted)

---

### Step 5: X/Twitter Post (`social-twitter`)

**Objective:** Create a visual-first X/Twitter post — 1–4 platform-sized visuals plus a short caption that links to the canonical blog.

**Tasks:**
1. Pick 1–4 most "screenshot-worthy" insights from the blog and write a visual brief.
2. Delegate to `visual-renderer` to render visuals at `content/visuals/social/twitter/twitter-<slug>-N.png`.
3. Delegate to `visual-reviewer` (cross-model) and block on PASS.
4. Write a caption ≤ 240 characters that ends with the canonical URL.
5. Save to `content/x-twitter-thread.md` with caption, attachments in order, alt text, and posting notes.

**Constraints:**
- Single image: 16:9 (1600×900) or 1:1 (1200×1200). Carousel (2–4): all 1:1.
- No multi-tweet textual thread — substance lives in the images.
- Optional Unicode Mathematical Bold (𝗕𝗼𝗹𝗱) on a 2–4 word phrase only.
- Each image must have a `visual-reviewer` PASS before publishing.

**Output:** `content/x-twitter-thread.md` + visuals under `content/visuals/social/twitter/`

---

## Remaining Steps

### Step 2b: Scope Assessment (`content-scope-assessment` skill)

**Objective:** Determine whether a topic needs a single blog post or a multi-part series.

**Tasks:**
- Score the strategy/outline against 8 comprehensiveness signals (0-2 each, 0-16 total):
  Pillar count, data density, audience breadth, technical depth, word count pressure, visual complexity, distribution fragmentation, dimension breadth
- If score 0-5: single post. If 6-10: suggest series. If 11+: recommend series.
- When recommending series, use dimension data (personas, WAF pillars) as split-point candidates.

**Output:** Series plan appended to strategy document + pipeline-config.md update.

---

### Step 2c: Multi-Dimensional Analysis (`multi-dimensional-analysis` skill)

**Objective:** Analyze the topic across persona, best practice, and Azure WAF pillar dimensions to inform series structure and social distribution angles.

**Tasks:**
- **Persona dimensions**: Identify distinct roles (developer, tech lead, eng manager, platform engineer), their responsibility context, application angle, depth needed, and preferred channels.
- **Best practice dimensions**: List technology practices (tools, code, config) and governance practices (process, policy, team controls); score each by complexity × impact.
- **Azure WAF pillar dimensions**: Map topic to Cost Optimization, Operational Excellence, Performance Efficiency, Reliability, Security; assess relevance (primary/secondary/tangential/none) and coverage depth (deep/moderate/mention).
- Compute dimension breadth score (0-2) as 8th signal for scope assessment.
- If series: create Dimension × Series Alignment and Dimension × Platform Matrix.

**Output:** `## Dimension Analysis` section appended to strategy document.

---

### Step 6: Reddit Post (`social-reddit`)

**Objective:** Create a visual-first Reddit Image Post — one platform-sized visual plus a 2–4 sentence context paragraph that links to the canonical blog.

**Tasks:**
- Pick the single most discussion-worthy insight from the blog and write a visual brief.
- Delegate to `visual-renderer` to render at `content/visuals/social/reddit/reddit-<slug>.png` (1:1 preferred, or 4:5).
- Delegate to `visual-reviewer` (cross-model) and block on PASS.
- Write 3–4 subreddit-specific title variants.
- Write a 2–4 sentence context paragraph (≤ 600 chars) ending with the canonical URL.
- Save to `content/reddit-post.md` with title variants, copy block, alt text, and posting notes.

**Formatting:** Standard Markdown only (no Unicode bold/italic). Submit as an Image Post wherever the subreddit allows.

**Constraints:**
- No TL;DR section — the visual is the TL;DR.
- No multi-section essay.
- Image must have a `visual-reviewer` PASS before publishing.

---

### Step 6b: Reel/Short Video (`reel-video`)

**Objective:** Create a 60-90 second short-form video script for Instagram Reels, YouTube Shorts, and LinkedIn Video.

**Tasks:**
- Select from 4 reel formats: "Did You Know?" (data shock), "Before/After" (transformation), "Quick Tutorial" (how-to), "Hot Take" (opinion/news).
- Produce shot list with timing, visuals, voiceover, and text overlays.
- Include screen recording notes (which app, settings, actions to perform).
- Write full voiceover script (word-for-word, timed to shots).
- Add platform-specific captions and hashtags.

**Constraints:**
- ONE core message only — ruthlessly cut everything else.
- Voiceover conversational, NOT corporate.
- Text overlays: max 6-8 words per screen.
- 9:16 aspect ratio (1080×1920).

**Output:** `content/reel-script.md`

---

### Step 7: Brand Audit (`brand-guardian`)

**Objective:** Audit all generated content for brand consistency.

**Tasks:**
- Verify voice/tone consistency across blog, social posts, and video scripts.
- Check design token compliance in all visual assets.
- Validate data point consistency (same numbers cited across all content pieces).
- Confirm formatting conventions per platform (Unicode for LinkedIn/X, Markdown for Reddit).

---

### Step 8: YouTube Script (`video-scriptwriter`)

**Objective:** Write a video script (8–12 min) for YouTube.

**Tasks:**
- Write script with visual cues, timing markers, and slide references.
- Map visuals from the blog to video sections.
- Include intro hook (first 30 sec), main content, and CTA.
- Provide thumbnail text/concept suggestions.
- Script should reference the existing PNGs as slide assets.

---

### Step 11: Social Media Publishing (`social-publisher`)

**Objective:** Publish generated social content to LinkedIn, X/Twitter, Reddit, and YouTube via MCP server tools with human approval.

**Architecture:** Three MCP servers orchestrated by one agent:
- `reddit-mcp-server` (npm, free) — Reddit posting with safe mode + spam protection
- `mcp-linkedin` (npm, free tier via Unipile) — LinkedIn posting with dry-run default
- `social-publisher` (custom Python) — X/Twitter thread posting + YouTube metadata updates

**Tasks:**
1. Read `pipeline-config.md` for platform selection and publish mode
2. Validate credentials via `check_credentials` tool
3. Preview all content across selected platforms (mandatory)
4. Present summary and request explicit human approval
5. Post to each approved platform in sequence
6. Log all posted URLs to `content/publishing-log.md`

**Human-in-the-loop:** All posting tools default to `dry_run: true`. The agent previews everything first and requires explicit user confirmation before any content goes live.

**Output:**
- Posted URLs reported to user
- `content/publishing-log.md` updated with timestamps and URLs
- `content/pipeline-config.md` Published URLs section updated

**Credentials:** Stored in `.env` — see `docs/social-api-setup.md` for setup guide.

---

### Step 12: Platform Distillation (`platform-distiller`)

**Objective:** Generate Step 12 platform outputs from the published blog. Medium and Substack are visual-first (one platform-sized hero image + short caption + canonical link). LinkedIn Article remains text-only with a unique angle (Google indexes the page, so a thin visual-only teaser would harm SEO).

**Architecture:** Single agent reading blog markdown + `content/publishing-log.md`, delegating to `visual-renderer` and `visual-reviewer` for the Medium/Substack heroes. No MCP servers required.

**Tasks:**
1. Read the blog file and extract: key argument, 3–5 data points, main sections
2. Look up canonical URL from `content/publishing-log.md` (matched by slug)
3. Commission Medium hero (16:9, 1500×844) and Substack hero (1:1 preferred, 1200×1200) via `visual-renderer`; require `visual-reviewer` PASS for both
4. Generate Medium post (80–150 word body): hero image + short caption + canonical link
5. Generate Substack post (40–80 word body): hero image + short hook + canonical link
6. Generate LinkedIn Article (700–900 words) — **unique angle, not a republish, no images**
7. Validate Medium/Substack: exactly one hero image, body within word limit, canonical URL at end. Validate LinkedIn Article: no image references, unique angle, canonical URL in final paragraph.

**Visual-first enforcement (Medium + Substack):** The hero image carries the substance. Inline screenshots, multiple figures, and long textual republishes are prohibited. Each hero must pass `visual-reviewer` cross-model review before the post is finalized.

**Text-only enforcement (LinkedIn Article only):** No image markdown (`![]`, `.png`, `.svg`, `<img`, `content/visuals/`, ` ```mermaid `). Numerical data is expressed inline.

**Publish sequence for outputs:**
- **Medium**: Day 0 — use Import tool (not paste); auto-sets canonical URL to GitHub Pages source
- **Substack**: Day 3–4 — post as Substack Note (ambient feed, not newsletter email)
- **LinkedIn Article**: Day 7+ — unique angle only; never a republish of the blog

**Output:**
- `content/visuals/social/medium/medium-<slug>.png` + `content/medium-post-{slug}.md` — with `── START COPY (Medium) ──` / `── END COPY (Medium) ──` markers
- `content/visuals/social/substack/substack-<slug>.png` + `content/substack-post-{slug}.md` — with `── START COPY (Substack) ──` / `── END COPY (Substack) ──` markers
- `content/linkedin-article-{slug}.md` — with `── START COPY (LinkedIn Article) ──` / `── END COPY (LinkedIn Article) ──` markers

Each file includes a publishing note at the top explaining the correct publish method for that platform.

```
content/
├── choose-GenAI-model-field-guide.md      # Main blog (Step 3)
├── choose-GenAI-model-field-guide.md.bak  # Pre-overhaul backup
├── linkedin-post.md                        # LinkedIn plain (Step 4)
├── linkedin-post-formatted.md              # LinkedIn Unicode (Step 4)
├── x-twitter-thread.md                     # Twitter thread (Step 5)
└── visuals/
    ├── render_placeholders.py              # PNG renderer (9 images)
    ├── render_placeholders.py.bak          # Pre-overhaul backup
    ├── write_svgs.py                       # SVG generator (3 files)
    ├── model-selection-framework.mmd       # Mermaid
    ├── model-routing-flow.mmd              # Mermaid
    ├── case-timeline.mmd                   # Mermaid
    ├── 30-day-process.mmd                  # Mermaid
    ├── model-selection-framework.png       # 320 DPI
    ├── model-routing-flow.png              # 320 DPI
    ├── comparison-matrix.png               # 320 DPI
    ├── tradeoff-2x2.png                    # 320 DPI
    ├── case-timeline.png                   # 320 DPI
    ├── pitfalls-mitigation.png             # 320 DPI
    ├── swimlane-30day.png                  # 320 DPI
    ├── checklist-card.png                  # 320 DPI
    ├── decision-funnel.png                 # 320 DPI
    ├── tradeoff-2x2.svg                    # Vector
    ├── decision-funnel.svg                 # Vector
    └── checklist-card.svg                  # Vector
```

## Key Decisions & Lessons

1. **Visual-first social for Twitter / Reddit / Medium / Substack** — These four platforms now lead with platform-sized visuals (commissioned via `visual-renderer`, validated cross-model by `visual-reviewer`). The accompanying text is a short context paragraph plus a link to the canonical GitHub Pages blog. Long textual threads, long Reddit essays, and long Medium/Substack republishes are no longer produced for these platforms.
2. **LinkedIn (post + Article) stays text-led** — The LinkedIn feed post (`social-linkedin`) keeps Unicode-formatted long text for algorithmic reach. The LinkedIn Article (Step 12) stays text-only with a unique angle because Google indexes the page; a thin visual-only teaser would harm SEO.
3. **Unicode formatting for social** — LinkedIn posts and the optional 2–4 word emphasis on X/Twitter captions use Unicode Mathematical Bold/Italic. Reddit always uses standard Markdown.
4. **SVGs via Python script** — Terminal heredoc corrupts SVG files. Always use a Python script to write SVGs.
5. **ASCII over Unicode in matplotlib** — Helvetica Neue lacks → and ✓ glyphs. Use `->` and `[x]` instead.
6. **Design tokens** — Centralized color/font system prevents visual inconsistency across 9+ images. Social visuals additionally rotate themes (round-robin) so the same blog does not look identical across X/Reddit/Medium/Substack.
7. **Quality requires specifics** — Generic advice ("choose the right model") fails. Concrete data ($140K, $0.10/1M tokens, 66% cost reduction) is what makes content credible — and is what the platform-sized visuals must encode.
8. **Substack URL:** `https://shailesh0.substack.com/publish/post/190276894`
