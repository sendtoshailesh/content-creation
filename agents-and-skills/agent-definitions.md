# Agent Definitions — Content Strategy Pipeline

Each agent below maps to one or more steps in the pipeline. These definitions capture the role, inputs, outputs, and constraints for each agent.

---

## 0. `reference-discovery`

**Role:** Web reference scout. Searches the web for high-quality sources across 6 categories, presents results for interactive curation (select/reject), and writes accepted references into the pipeline config.

**Steps:** 0a (Reference Discovery) — runs before reference analysis

**Inputs:**
- Topic or search terms from user
- Existing pipeline topic from `content/pipeline-config.md`

**Outputs:**
- Curated reference URLs appended to `content/pipeline-config.md` under the correct category headings

**Search Backend:**
- Primary: Azure Bing Web Search API v7 via `scripts/bing-search.py`
- Fallback: Copilot built-in `web` tool (when API key not configured or quota exceeded)

**Workflow:**
1. Generate 2-3 targeted queries per category (12-18 total)
2. Execute batch search via Bing API (or web tool fallback)
3. Present results grouped by category with numbered references
4. User selects/rejects by number — supports multiple curation rounds
5. Write accepted references to pipeline config

**Categories:**
- General content
- Industry Reports & Benchmarks
- Competitor / Related Articles
- Pricing Pages & Documentation
- Case Studies & Examples
- Research Papers

**Constraints:**
- Never auto-select — always present for user approval
- Never modify files other than `pipeline-config.md`
- Append to existing references, never overwrite
- Deduplicate against URLs already in config

---

## 1. `content-strategist`

**Role:** Interviewer + planner. Gathers context and produces a distribution-aware content outline.

**Steps:** 1 (Clarifying Questions), 2 (Strategy & Outline)

**Inputs:**
- Topic or rough idea from user
- Target audience (IC engineers, tech leads, executives)

**Outputs:**
- Structured brief (audience, tone, channels, success metrics)
- Section-by-section outline with visual placement markers

**Constraints:**
- Ask 8–12 targeted questions before writing anything.
- Outline must tag which sections feed which social posts.

---

## 2. `blog-writer`

**Role:** Technical writer. Produces the long-form anchor content.

**Steps:** 3 (Full Blog Post)

**Inputs:**
- Strategy doc + outline from `content-strategist`
- Visual assets (file paths) from `visual-renderer`

**Outputs:**
- Publication-ready Markdown blog (~3,000 words)
- SVG integrations via `<details>` collapsible blocks

**Constraints:**
- Every claim needs a concrete number, model name, or benchmark.
- Use real pricing data, not placeholders.
- Include: hook, framework, tier breakdown, case study, playbook, checklist.

---

## 3. `visual-renderer`

**Role:** Diagram/chart generator. Produces all visual assets.

**Steps:** 3b (Visual Generation)

**Inputs:**
- Blog outline with visual markers
- Design tokens (colors, fonts, DPI)

**Outputs:**
- Mermaid `.mmd` files (flowcharts, timelines)
- PNG renders at 320 DPI via matplotlib
- SVG graphics for web embedding

**Tools:**
- Python + matplotlib
- Design token config: 15 named colors, Helvetica Neue, 320 DPI
- `render_placeholders.py` for PNGs
- `write_svgs.py` for SVGs

**Constraints:**
- No Unicode glyphs (→, ✓) in matplotlib — use ASCII equivalents.
- Write SVGs via Python script, never terminal heredoc.
- All images must share consistent color palette and typography.

---

## 4. `quality-reviewer`

**Role:** Editor/critic. Reviews content + visuals and enforces quality bar.

**Steps:** 3c (Quality Overhaul)

**Inputs:**
- Draft blog, visual assets, user feedback

**Outputs:**
- Revised content with concrete data replacing vague claims
- Fixed/rebuilt visuals meeting design standards

**Trigger:** User feedback or quality gate failure.

**Quality Checklist:**
- [ ] Every section has at least one specific number or model name
- [ ] Pricing table uses real per-1M-token costs
- [ ] Case study has before/after metrics
- [ ] All visuals render cleanly at target DPI
- [ ] No broken Unicode glyphs

---

## 5. `social-linkedin`

**Role:** LinkedIn content adapter. Converts blog into LinkedIn-native format.

**Steps:** 4 (LinkedIn Post)

**Inputs:**
- Published blog
- Key data points, case study, framework summary

**Outputs:**
- Plain-text version (`linkedin-post.md`)
- Unicode-formatted version (`linkedin-post-formatted.md`)

**Formatting Rules:**
- Unicode Mathematical Bold Sans-Serif (𝗕𝗼𝗹𝗱) for emphasis
- Unicode Mathematical Italic Sans-Serif (𝘐𝘵𝘢𝘭𝘪𝘤) for contrast
- ━━━ separators, ▸ sub-bullets, ⚠️📊 emoji anchors
- Copy-paste ready between ── START ── / ── END ── markers
- Story hook opening (not "I wrote a blog" — lead with problem/insight)

---

## 6. `social-twitter`

**Role:** X/Twitter visual-first distributor. Commissions platform-sized visuals (via `visual-renderer`, validated by `visual-reviewer`) and writes a short caption that links to the canonical blog.

**Steps:** 5 (X/Twitter Post)

**Inputs:**
- Published blog
- Canonical URL from `content/publishing-log.md`
- Existing `content/visuals/` (re-use where possible)

**Outputs:**
- 1–4 platform-sized visuals saved to `content/visuals/social/twitter/twitter-<slug>-N.png`
- `content/x-twitter-thread.md` containing: short caption (≤ 240 chars), canonical URL, image references in attach order, alt text per image, posting notes

**Formatting Rules:**
- Caption ≤ 240 characters (URL counts ~23 chars)
- Optional Unicode Mathematical Bold (𝗕𝗼𝗹𝗱) on a 2–4 word phrase only
- Single image: 16:9 or 1:1; carousel (2–4): all 1:1
- No multi-tweet textual thread — substance lives in the images
- Every image must have a `visual-reviewer` PASS before publishing

---

## 7. `social-reddit`

**Role:** Reddit visual-first distributor. Commissions a single platform-sized visual (via `visual-renderer`, validated by `visual-reviewer`) and writes a short context paragraph that links to the canonical blog.

**Steps:** 6 (Reddit Post)

**Inputs:**
- Published blog
- Target subreddit(s)
- Canonical URL from `content/publishing-log.md`

**Outputs:**
- 1 platform-sized visual at `content/visuals/social/reddit/reddit-<slug>.png` (1:1 preferred, or 4:5)
- `content/reddit-post.md` with: subreddit-specific title variants, 2–4 sentence context paragraph (≤ 600 chars), canonical URL, image alt text, posting notes

**Formatting Rules:**
- Submitted as an Image Post wherever the subreddit allows
- Standard Markdown only (no Unicode bold/italic)
- No TL;DR section — the visual is the TL;DR
- No multi-section essay
- Image must have a `visual-reviewer` PASS before publishing

---

## 8. `demo-builder`

**Role:** Creates interactive VS Code walkthrough or code demo.

**Steps:** 7 (VS Code Demo) — Optional

**Inputs:**
- Framework/concepts from blog
- Model tier definitions

**Outputs:**
- Demo project with tiered routing config
- README with setup instructions

---

## 9. `video-scriptwriter`

**Role:** Converts blog into a timed video script with visual cues.

**Steps:** 8 (YouTube Script)

**Inputs:**
- Published blog
- Visual assets (PNGs for slides)

**Outputs:**
- 8–12 min script with timing markers
- Visual cue annotations (which PNG/slide per section)
- Intro hook (first 30 sec), main content, CTA
- Thumbnail concept suggestions

---

## 10. `platform-distiller`

**Role:** Generates the Step 12 platform outputs from a published blog. Visual-first for Medium and Substack; text-only unique-angle for LinkedIn Article.

**Steps:** 12 (Platform Distillation) — runs after web-publisher (Step 10) and social-publisher (Step 11)

**Inputs:**
- Blog file path (e.g., `content/blog-part1.md`)
- Canonical URL from `content/publishing-log.md` (matched by `seo.slug`)
- Existing visuals in `content/visuals/`

**Outputs:**
- Medium hero visual at `content/visuals/social/medium/medium-<slug>.png` (16:9, 1500×844) + `content/medium-post-{slug}.md` (80–150 word body + canonical link)
- Substack hero visual at `content/visuals/social/substack/substack-<slug>.png` (1:1 preferred, 1200×1200) + `content/substack-post-{slug}.md` (40–80 word body + canonical link)
- `content/linkedin-article-{slug}.md` (700–900 words, text-only, **unique angle**, NOT a republish)

**Formatting Rules:**
- Medium and Substack outputs include exactly one hero image (no inline screenshots) and end with the canonical URL
- Both hero images must receive a `visual-reviewer` PASS before the post is finalized
- LinkedIn Article remains text-only with no image markdown — Google indexes the page and a thin visual-only teaser would harm SEO
