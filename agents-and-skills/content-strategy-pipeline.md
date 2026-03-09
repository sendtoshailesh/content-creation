# Content Strategy Pipeline — Agent & Task Record

## Objective

Build a repeatable 8-step content pipeline that takes a single technical topic and produces a full distribution package: long-form blog, social posts (LinkedIn, X/Twitter, Reddit), optional VS Code demo, and YouTube script. Each step is a discrete, automatable task suitable for an agent or skill.

---

## Pipeline Overview

| Step | Task | Agent/Skill | Status |
|------|------|-------------|--------|
| 1 | Clarifying Questions | `content-strategist` | ✅ Done |
| 2 | Strategy & Outline | `content-strategist` | ✅ Done |
| 3 | Full Blog Post | `blog-writer` | ✅ Done |
| 3b | Visual Generation | `visual-renderer` | ✅ Done |
| 3c | Quality Overhaul | `quality-reviewer` | ✅ Done |
| 4 | LinkedIn Post | `social-linkedin` | ✅ Done |
| 5 | X/Twitter Thread | `social-twitter` | ✅ Done |
| 6 | Reddit Post | `social-reddit` | ⬜ Next |
| 7 | VS Code Demo | `demo-builder` | ⬜ Optional |
| 8 | YouTube Script | `video-scriptwriter` | ⬜ Pending |

---

## Completed Steps — Detailed Record

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

### Step 5: X/Twitter Thread (`social-twitter`)

**Objective:** Create a 12-tweet thread + standalone summary tweet.

**Tasks:**
1. Write 12-tweet thread covering: hook → problem → framework → tiers → hidden costs → case study → latency → routing → playbook → CTA → engagement close.
2. Apply same Unicode formatting strategy as LinkedIn.
3. Add standalone single-tweet summary at top of file.
4. Include posting notes (image attachment, timing, cadence).

**Constraints:**
- Each tweet under 280 characters.
- Unicode chars count as 1 char on X/Twitter.

**Output:** `content/x-twitter-thread.md` (Unicode formatted, 12 tweets + summary)

---

## Remaining Steps

### Step 6: Reddit Post (`social-reddit`)

**Objective:** Write a Reddit post for r/MachineLearning, r/artificial, or r/ExperiencedDevs.

**Tasks:**
- Reddit supports native Markdown — use **bold**, *italic*, headers, bullet lists (NOT Unicode formatting).
- Write a longer, more technical version — Reddit rewards depth and contrarian takes.
- Include a TL;DR at the top.
- Be conversational and anti-promotional (no obvious self-promotion).
- Link to blog naturally at the end.
- Suggest subreddit-specific title variants.

**Formatting:** Markdown (Reddit's native format). NO Unicode bold/italic.

---

### Step 7: VS Code Demo (`demo-builder`) — Optional

**Objective:** Create a VS Code walkthrough or demo showcasing the model selection framework.

**Tasks:**
- Build a demo project that shows tiered model routing in action.
- Include configuration files, sample API calls to different model tiers.
- Create a README with setup instructions.

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

## File Inventory

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

1. **Unicode formatting for social** — LinkedIn and X/Twitter don't support Markdown. Unicode Mathematical Bold/Italic characters render natively. Reddit supports Markdown natively, so use standard formatting there.
2. **SVGs via Python script** — Terminal heredoc corrupts SVG files. Always use a Python script to write SVGs.
3. **ASCII over Unicode in matplotlib** — Helvetica Neue lacks → and ✓ glyphs. Use `->` and `[x]` instead.
4. **Design tokens** — Centralized color/font system prevents visual inconsistency across 9+ images.
5. **Quality requires specifics** — Generic advice ("choose the right model") fails. Concrete data ($140K, $0.10/1M tokens, 66% cost reduction) is what makes content credible.
6. **Substack URL:** `https://shailesh0.substack.com/publish/post/190276894`
