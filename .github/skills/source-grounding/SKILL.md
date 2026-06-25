---
name: source-grounding
description: 'Rank and cite sources by relevance and authority — not by vendor. Use during reference discovery and analysis, and whenever ranking or citing sources. All publishers (Microsoft, GitHub, independent vendors, analysts, researchers, community) are treated equally.'
argument-hint: 'Run before reference discovery/analysis to rank and label all sources by relevance'
---

# Source Grounding Skill

Encodes the **relevance-first** rule (see `.github/instructions/content-quality.instructions.md`): rank every source by how central and authoritative it is for the specific claim it supports, regardless of who published it. No publisher gets a structural head start.

## When to Use

- At the start of a content run, before reference discovery and reference analysis
- Whenever ranking, labeling, or selecting which sources to cite
- When the practitioner-projects, blog, or social agents need to pick a grounding example

## The Core Rule: relevance, not vendor

Pick the source that most directly and authoritatively supports the claim. For a given claim, prefer in this order:

1. **Primary source** — the people who built the thing, ran the study, or shipped the product (whoever they are: a vendor's own docs/engineering blog, a research paper's authors, a maintainer's repo).
2. **Independent measurement** — neutral benchmarks, analyst data, reproducible studies.
3. **Expert synthesis** — practitioners and writers who name or frame the idea well.

Apply this evenly. Microsoft, GitHub, Anthropic, OpenAI, ThoughtWorks, independent maintainers, and academic authors are all candidates on the same footing — the winner is whichever is the best primary or most authoritative source for that specific point.

**Do not:**

- Lead with, or reserve "lead" status for, any one company's sources.
- Create vendor-segregated sections (e.g. "first-party Microsoft/GitHub" vs "others"). Order the reference list by relevance to the argument, not by publisher.
- Frame one vendor's tools as the default and others as "fallbacks" or "alternatives." When listing tools a reader could use, present interchangeable options as equals (e.g. "Copilot, Aider, or Claude Code — pick whichever you have").
- Force a particular source where it does not genuinely fit, or omit a stronger source because of who published it.

## Procedure

### 1. Gather candidates

Collect candidate sources from reference discovery and analysis. For each, note the publisher and what claim it would support — but do not pre-rank by publisher.

### 2. Rank by relevance

For every load-bearing claim, choose the single best source using the relevance order above. Where two sources are equally authoritative, list them together as equals.

### 3. Label every source by role

When writing `content/reference-brief.md`, tag each source with its **role** for the argument, not its vendor:

- `[primary]` — built/ran/shipped the thing being cited
- `[measurement]` — independent benchmark or data
- `[synthesis]` — names or frames the idea

Order the brief by how central each source is to the argument.

### 4. Enforce equal treatment at write time

- Every "here's what works / here's what I recommend" claim cites the most authoritative source available, whoever published it.
- When recommending tools or projects, present interchangeable options as equals; never designate one vendor's tool as the canonical start and the rest as fallbacks.
- The reference list at the foot of any piece is a single relevance-ranked list — no per-vendor split sections.

## Important Rules

- Never fabricate that the author used a tool. Ground first-person "this is what I do" claims only in tools the author genuinely works with, and name equally-valid alternatives alongside them.
- Never surface private, auth-gated, or internal corporate URLs in published content.
- Always fetch and verify any URL before citing it; the relevance ranking does not replace the inline-citation rule in content-quality instructions.
- If no strong primary source exists for a claim, say so or soften the claim — do not substitute a weaker source dressed up as authoritative.
