---
description: "Use when writing or editing blog posts, social posts, or video scripts. Enforces content quality standards including data specificity, tone, and structure."
applyTo: "content/**/*.md"
---

# Content Quality Standards

## Data Specificity

- Every claim must include a concrete number, model name, or benchmark
- Use real pricing data (per-1M-token costs from provider pricing pages)
- Case studies require before/after metrics (cost, latency, accuracy)
- Reference model **tiers and capabilities** as the primary noun (e.g., "flagship reasoning tier", "budget tier", "standard 1x tier"); cite specific model versions only as parenthetical, time-stamped examples — see "Model Version Stability" below

## Research and Citation Links (mandatory)

- Every claim attributed to a study, paper, benchmark, vendor announcement, or company ("Apple ML Research found…", "RouteLLM…", "GitHub announced…", "Anthropic engineering says…") MUST include an inline Markdown link to the original source URL on first mention in each file
- This applies to: blog posts, LinkedIn articles, LinkedIn posts, Medium/Substack posts, X/Twitter threads, Reddit posts, reel/YouTube scripts (use spoken-link patterns like "linked in the description" + actual URL in the description block), and visual asset captions/footnotes
- The "Key Data Points Referenced" / "References" table at the end of a blog post does NOT replace this inline-link requirement
- For research with a once-meaningful model name (e.g., "RouteLLM achieved 95% of GPT-4 quality"), keep the original model name verbatim — it is part of the citation — and add a one-line clarifier explaining that the named model refers to the paper's baseline at publication time
- Source URLs must point to the canonical primary source (vendor docs, research paper, official blog) — not a secondary aggregator — whenever the primary source is reachable

## Source-of-Truth Precedence (first-party first)

Ground every claim, example, and recommendation by source precedence. The author works in AI Foundry and the GitHub platform/Copilot — content must show that the recommendations come from work and platforms the author actually uses, then corroborate with public sources. This is a **balanced** rule, not an absolutist one.

**Precedence ladder (high → low):**

1. **Author's own work + this repo's harness.** The author's shipped/recommended work and this repository's own agent/skill/instruction harness + review-gate loops (a working, inspectable example). First-person, case-study voice.
2. **Microsoft first-party.** AI Foundry (docs, blog, Agent Service, evaluators), Microsoft Learn / Microsoft Docs, Microsoft Research, and the Microsoft engineering blogs.
3. **GitHub first-party.** GitHub Copilot (docs, changelog, coding agent, CLI, Agent HQ), GitHub Engineering blog, and official GitHub-owned repos.
4. **Public / third-party.** Independent vendors, analysts, research, and community sources — used for neutral benchmarks, independent validation, contrarian angles, or when no first-party (tiers 1–3) source exists.

**Rules:**

- **Lead with first-party.** Every "here's what works / here's what I recommend" claim should present a tier 1–3 example *before* a public one. Public sources corroborate; they do not lead.
- **Balanced fallback.** Use public sources freely for neutral benchmarks (e.g., independent leaderboards), third-party validation, or any point where no Microsoft/GitHub equivalent exists. Do not force a first-party source where it doesn't genuinely fit, and do not omit a stronger public benchmark — pair it with a first-party example instead.
- **Browser history + reading list are a mandatory grounding input.** Before writing, the pipeline harvests the author's Chrome and Edge browsing history and reading lists into `content/browsing-signals.md` (via `scripts/pipeline/harvest_browsing.py`). Prefer sources the author has actually visited/saved so content reflects genuine navigation. Topic-relevant entries that are Microsoft/GitHub first-party are promoted to tiers 2–3; relevant public entries are valid tier-4 corroboration. Cite a browsing-signal URL only after fetching/verifying it like any other source (it still obeys the inline-citation rule).
- **Practitioner projects prefer Microsoft/GitHub repos.** The "Build it yourself" projects (see Practitioner Projects section) should ground in Microsoft- or GitHub-owned repos / AI Foundry samples first, and reach for other public repos only when no first-party repo fits the skill level.
- **Reference brief labels every source with its tier.** `content/reference-brief.md` must tag each source `[T1 own | T2 Microsoft | T3 GitHub | T4 public]` so downstream writers can lead first-party by construction.

## Model Version Stability (hybrid abstraction)

Model lineups change every quarter. Hardcoded model names date an article in months. Use the hybrid abstraction pattern so content stays valuable as models rotate:

- **Lead with tier and capability**, not with a specific model name. Examples of good leading phrasing:
  - "the budget tier (0.25x multiplier)"
  - "the standard 1x tier"
  - "the premium reasoning tier (3x)"
  - "the flagship fast-mode tier (30x)"
  - "included models (0x on paid plans)"
- **Cite specific models only as parenthetical, time-stamped examples**:
  - GOOD: "the budget tier at 0.25x (as of writing: GPT-5.4 nano, Claude Haiku 4.5)"
  - GOOD: "the standard 1x tier (as of writing: Claude Sonnet 4.x, Gemini 2.5 Pro, GPT-5.2)"
  - BAD:  "GPT-5.4 nano costs 0.25x. Claude Opus 4.6 fast mode costs 30x."
- **Keep multiplier numbers concrete.** GitHub's billing structure (0.25x, 1x, 3x, 30x, etc.) is the durable framework — those values do not rotate with model releases. Tier wording sits on top of the multipliers.
- **Footnote pattern for derived/short content** (X/Twitter, reels, short LinkedIn posts) where parentheticals are too noisy: use "X / X-1 / X-2" style ("X" = current flagship from a vendor, "X-1" = previous generation) and add a one-line "as of writing" footnote at the bottom mapping X to the current specific model.
- **Visual assets follow the same rule.** Labels in PNGs/SVGs should read "Budget tier (0.25x)" with specific model names only as smaller secondary labels or omitted entirely. Re-renders are cheaper than re-shoots — but tier-first labels survive re-renders unchanged.

## Role Terminology (audience naming)

When addressing leadership/governance audiences for AI tooling decisions:

- Prefer **"AI team leads"** for operational guidance (who runs day-to-day standards, budget alerts, model defaults)
- Prefer **"AI team decision-makers"** or **"decision-makers"** for strategic framing (who chooses tools, sets policy, owns budget)
- Use both contextually within a piece — operational sections lean "leads", strategic sections lean "decision-makers"
- Avoid "engineering manager" as the default label for AI-tooling governance content; reserve it for cases where engineering management specifically (not AI ownership) is the audience

## Volatile Data and Caveats

- When citing provider pricing, model availability, multipliers, or feature access, check if the source says "subject to change", "in preview", or "may change"
- If it does, include a caveat in the content: "as of [date]", "currently", or "at the time of writing — GitHub notes this is subject to change"
- Never present volatile pricing or feature data as permanent facts
- Never build the primary CTA on data tagged `[VOLATILE]` without acknowledging the risk — always provide a fallback recommendation that works even if the data changes
- When a content strategy depends on a specific pricing tier (e.g., "free models"), include a "what if this changes" paragraph with the alternative strategy

## Structure Requirements

- Blog posts: hook, framework, tier breakdown, case study, playbook, checklist
- Social posts: story hook opening, NOT "I wrote a blog"
- All content ends with a clear call-to-action

## Practitioner Projects & Art of the Possible (mandatory)

Content must do more than synthesize sources — it must hand the reader something concrete to **build**. This is what separates thought leadership from a link roundup. Every blog post MUST include a dedicated hands-on section (e.g. "Build it yourself" / "Projects to try") that turns the post's core concept into practitioner action. The full method lives in the `practitioner-projects` skill — follow it.

### Rules

- **Three projects, scaling beginner → intermediate → advanced.** Each one derives directly from a concept explained earlier in the piece — never generic filler. Together they show the art of the possible: a reader should finish thinking "I could build that this week."
- **Every project is fully structured** with: a one-line **Goal**, **Prerequisites**, numbered **Steps**, a **machine-checkable success signal** (a test passes, a metric moves, an output matches), a realistic **time estimate**, and a **Stretch goal**.
- **Ground every project in a real, verified resource.** Link a genuine GitHub repo, starter template, or tool — and verify the URL is reachable before publishing (no fabricated or guessed links). If no suitable repo exists, provide an explicit from-scratch path instead, and say so.
- **Serve practitioners, not only leads.** Audience guidance still applies for governance framing, but the projects section is the practitioner track — it must let an individual engineer get hands-on without manager sign-off.
- **The call-to-action in every channel points to a concrete project.** Blog, LinkedIn, reel/short script, slide deck, Medium/Substack distill, and X/Twitter must each close by naming at least one project the reader can start now, with the canonical URL or repo link. The CTA is "go build X", not "go read my blog".
- **Inline-link rule still applies.** Project grounding links follow the same primary-source, verified-URL standard as citations above.


## Tone

- First-person: "sharing my learnings working with customers"
- Conversational but data-driven
- Never corporate/fundraising framing
- Lead with problems and insights

## Visual Density for Dense Sections (Mandatory Pass)

Quality content requires thorough explanation. Never cut essential text to reduce word count. Instead, add visual companions to dense sections so readers can choose their preferred path: read the text OR understand the concept through the visual.

### Rules

- **Word count is flexible.** Blog posts may exceed initial targets by 25-40% when the additional text adds essential concepts, data, or context. Quality always outweighs length constraints.
- **Every section exceeding 400 words without a visual must get one.** Dense prose sections are the primary candidates for visual companions.
- **Visuals explain the same concept differently.** The visual is not decoration — it is an alternative explanation path. A reader who skips the text should still understand the concept from the visual alone.
- **Visual types by section pattern:**
  - Concept explanation (how X works) -> flow diagram or annotated illustration
  - Comparison (X vs Y) -> side-by-side comparison chart
  - Process/loop (vague prompt -> retry -> cost) -> sequential flow with cost annotations
  - Data breakdown (what repeats vs changes) -> stacked bar or pie chart
  - Decision guidance (when to use X vs Y) -> decision matrix or two-column comparison
- **Never compromise text for brevity.** If a section needs 5 paragraphs to explain a concept properly, keep all 5 paragraphs AND add a visual that captures the same idea graphically.

### Audit Method

After writing, scan each H2/H3 section. For any section over 400 words without a visual, add a `[VISUAL: description]` marker. The visual-renderer agent picks up these markers and generates the corresponding PNGs. Target: every dense concept has both a text path and a visual path.
