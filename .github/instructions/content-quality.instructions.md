---
description: "Use when writing or editing blog posts, social posts, or video scripts. Enforces content quality standards including data specificity, tone, and structure."
applyTo: "content/**/*.md"
---

# Content Quality Standards

## Data Specificity

- Every claim must include a concrete number, model name, or benchmark
- Use real pricing data (per-1M-token costs from provider pricing pages)
- Case studies require before/after metrics (cost, latency, accuracy)
- Reference specific model names: GPT-4o, Claude Opus/Sonnet/Haiku, Gemini, Llama 3, Mistral

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
