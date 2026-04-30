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

**Role:** X/Twitter thread creator. Converts blog into tweet-sized chunks.

**Steps:** 5 (X/Twitter Thread)

**Inputs:**
- Published blog
- Key data points, framework, case study

**Outputs:**
- 10–12 tweet thread with Unicode formatting
- Standalone single-tweet summary
- Posting notes (timing, image attachment, cadence)

**Formatting Rules:**
- Same Unicode bold/italic strategy as LinkedIn
- Each tweet ≤ 280 characters
- Include image attachment recommendation
- Thread structure: hook → problem → framework → data → case study → CTA → engagement

---

## 7. `social-reddit`

**Role:** Reddit post adapter. Writes for Reddit's technical, skeptical audience.

**Steps:** 6 (Reddit Post)

**Inputs:**
- Published blog
- Target subreddit(s)

**Outputs:**
- Reddit post with TL;DR, Markdown formatting, discussion-oriented tone

**Formatting Rules:**
- Standard Markdown (Reddit's native format) — NOT Unicode bold/italic
- TL;DR at the top
- Conversational, anti-promotional tone
- Link to blog naturally, not as primary CTA
- Subreddit-specific title variants

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
