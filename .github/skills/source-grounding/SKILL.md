---
name: source-grounding
description: 'Apply Source-of-Truth Precedence (first-party Microsoft/GitHub before public) and harvest the author''s Chrome/Edge browsing signals when gathering references. Use during reference discovery and analysis, and whenever ranking or citing sources.'
argument-hint: 'Run before reference discovery/analysis to harvest browsing signals and tier all sources'
---

# Source Grounding Skill

Encodes the **Source-of-Truth Precedence** rule (see `.github/instructions/content-quality.instructions.md`) and the browsing-signal harvest so every reference set leads with first-party Microsoft/GitHub material the author actually uses, with public sources as corroboration.

## When to Use

- At the start of a content run, before reference discovery and reference analysis
- Whenever ranking, labeling, or selecting which sources to cite
- When the practitioner-projects, blog, or social agents need to pick a grounding example

## The Precedence Ladder

Rank every candidate source into one of four tiers. **Lead with the highest tier that genuinely fits; use public sources for neutral benchmarks, independent validation, or when no first-party source exists.** This is balanced, not absolutist — do not force a first-party source where it does not fit, and do not omit a stronger public benchmark; pair it with a first-party example instead.

| Tier | Label | Sources | Role |
|------|-------|---------|------|
| 1 | `[T1 own]` | The author's own shipped/recommended work; this repo's agent/skill/instruction harness + review-gate loops | Lead — first-person case-study voice ("in my work with customers") |
| 2 | `[T2 Microsoft]` | AI Foundry (docs, blog, Agent Service, evaluators), Microsoft Learn / Docs, Microsoft Research, Microsoft engineering/dev blogs | Lead first-party example |
| 3 | `[T3 GitHub]` | GitHub Copilot (docs, changelog, coding agent, CLI, Agent HQ), GitHub Engineering blog, official GitHub-owned repos | Lead first-party example |
| 4 | `[T4 public]` | Independent vendors, analysts, research, community | Corroboration, neutral benchmarks, contrarian angles, gap-fillers |

**Domain cheat-sheet for tiering:**

- **T2 Microsoft:** `learn.microsoft.com`, `docs.microsoft.com`, `devblogs.microsoft.com`, `techcommunity.microsoft.com`, `azure.microsoft.com`, `research.microsoft.com`, `microsoft.github.io`
- **T3 GitHub:** `github.com` (official orgs: `github`, `githubnext`, `Azure`, `microsoft`, `dotnet`, `Azure-Samples`), `github.blog`, `docs.github.com`, `githubnext.com`
- **T4 public:** everything else (e.g. `martinfowler.com`, `thoughtworks.com`, `anthropic.com`, `openai.com`, `arxiv.org`, `infoq.com`)

## Procedure

### 1. Harvest browsing signals (mandatory)

Run the harvester with the run's topic keywords. It reads the author's Chrome + Edge history and saved bookmarks (read-only copy), filters to topic-relevant entries, drops private/auth-gated/internal corporate URLs, and writes a tiered digest.

```bash
python3 scripts/pipeline/harvest_browsing.py --days 365 --top 30 <topic keyword> <kw2> <kw3> ...
```

Output: `content/browsing-signals.md` with Tier 2 / Tier 3 / Tier 4 tables. These are sources the author has *actually visited or saved* — prefer them so content reflects genuine navigation.

> The digest is a navigation *signal*, not a fact-check. **Fetch and verify any URL before citing it**, and it still obeys the inline-citation rule in content-quality instructions.

### 2. Promote browsing signals into the reference set

- Tier 2/3 browsing entries (Microsoft/GitHub docs, blogs, repos) → promote to the lead reference list.
- Tier 4 browsing entries that are topic-relevant → keep as public corroboration.
- Skip product app-shell/portal URLs that aren't citable (the harvester already drops most).

### 3. Tier-label every source

When writing `content/reference-brief.md`, tag each source with its tier label (`[T1 own]`, `[T2 Microsoft]`, `[T3 GitHub]`, `[T4 public]`) so downstream writers can lead first-party by construction.

### 4. Enforce lead-first-party at write time

- Every "here's what works / here's what I recommend" claim shows a Tier 1–3 example *before* a public one.
- Public benchmarks are framed as independent corroboration of the first-party position.
- Practitioner projects prefer Microsoft/GitHub-owned repos and AI Foundry samples first.

## Important Rules

- Never fabricate that the author used a tool — ground the "prove my work" voice in official Microsoft/GitHub capabilities the author genuinely works with (AI Foundry, GitHub Copilot), surfaced via browsing signals.
- Never surface private, auth-gated, or internal corporate URLs in published content (the harvester denylist guards this; keep it that way).
- If the harvester finds no first-party browsing signals for a topic, fall back to first-party web discovery (Microsoft Learn / GitHub docs search) before public search.
