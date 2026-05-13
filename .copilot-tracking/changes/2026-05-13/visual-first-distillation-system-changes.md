<!-- markdownlint-disable-file -->
# Release Changes: Visual-First Distillation System for Thought Leadership

**Related Plan**: visual-first-distillation-system-plan.instructions.md
**Implementation Date**: 2026-05-13

## Summary

Builds a reusable visual-first distillation system: new `visual-pack-generator` skill with slide grammar, platform specs, and psychology stack references; updated `social-linkedin`, `social-twitter`, and `platform-distiller` agents to consume visual packs; updated `pipeline-config.md` with persona mode field; demo visual packs and distilled posts for Part 1 in both Practitioner and Executive modes.

## Changes

### Added

**Phase 1 — Visual Pack Generator Skill**
- `.github/skills/visual-pack-generator/SKILL.md` — 7-step skill procedure, Practitioner + Executive mode specs, output directory contract, critical rules (design tokens, DPI, fonts)
- `.github/skills/visual-pack-generator/references/slide-grammar.md` — 10-slide Practitioner carousel grammar + 5-exhibit Executive grammar, hook archetypes, exhibit anatomy, shared content rules
- `.github/skills/visual-pack-generator/references/platform-specs.md` — per-platform dimensions, copy budgets, CTA rules, asset inventory tables, publish cadence, engagement benchmarks
- `.github/skills/visual-pack-generator/references/psychology-stack.md` — 12-framework quick reference, per-position psychology stacks for both modes, anti-patterns, operational checklists

**Phase 4 — Demo: Practitioner Visual Pack (Part 1)**
- `content/visuals/distilled/part1-practitioner/render_distilled.py` — standalone Python renderer for all 20 practitioner assets
- `content/visuals/distilled/part1-practitioner/manifest.md` — 20-asset manifest with usage notes
- `content/visuals/distilled/part1-practitioner/slide-01-hook.png` through `slide-10-cta.png` (10 carousel slides, 1080×1080px, 320 DPI)
- `content/visuals/distilled/part1-practitioner/x-card-01.png` through `x-card-04.png` (4 X/Twitter cards, 1600×900px, 320 DPI)
- `content/visuals/distilled/part1-practitioner/medium-hero.png` (1400×800px), `medium-inline-01.png`, `medium-inline-02.png` (1200×800px)
- `content/visuals/distilled/part1-practitioner/substack-hero.png` (1200×630px)
- `content/visuals/distilled/part1-practitioner/linkedin-article-exhibit-01.png`, `linkedin-article-exhibit-02.png` (1200×627px)

**Phase 4 — Demo: Executive Visual Pack (Part 1)**
- `content/visuals/distilled/part1-executive/render_distilled.py` — standalone Python renderer for all 11 executive assets
- `content/visuals/distilled/part1-executive/manifest.md` — 11-asset manifest with 5-zone anatomy
- `content/visuals/distilled/part1-executive/exhibit-01-context.png` through `exhibit-04-roi.png` (4 exhibits, 1200×627px)
- `content/visuals/distilled/part1-executive/x-exhibit-01.png`, `x-exhibit-02.png` (1600×900px)
- `content/visuals/distilled/part1-executive/medium-hero.png` (1400×800px), `medium-inline-01.png` (1200×800px)
- `content/visuals/distilled/part1-executive/substack-hero.png` (1200×630px)
- `content/visuals/distilled/part1-executive/linkedin-article-exhibit-01.png`, `linkedin-article-exhibit-02.png` (1200×627px)

**Phase 4 — Demo: Distilled Posts (Part 1, Both Modes)**
- `content/linkedin-post-part1-practitioner.md` — LinkedIn carousel post, visual-first, copy-paste ready
- `content/linkedin-post-part1-executive.md` — LinkedIn exhibit post, executive mode
- `content/x-twitter-thread-part1-practitioner.md` — X image-anchored thread, Practitioner
- `content/x-twitter-thread-part1-executive.md` — X exhibit-anchored thread, Executive
- `content/medium-post-cost-part1.md` — Medium article with embedded visual references (practitioner)
- `content/medium-post-cost-part1-executive.md` — Medium article (executive mode)
- `content/substack-note-cost-part1.md` — Substack Note with hero image reference
- `content/substack-note-cost-part1-executive.md` — Substack Note (executive mode)
- `content/linkedin-article-cost-part1.md` — LinkedIn Article unique angle (practitioner)
- `content/linkedin-article-cost-part1-executive.md` — LinkedIn Article unique angle (executive)

### Modified

**Phase 2 — Agent Updates**
- `.github/agents/social-linkedin.agent.md` — Added Step 1b visual pack detection + Visual-First Procedure (Practitioner + Executive modes) with first-comment canonical URL rules; existing text-only path preserved as backward-compatible fallback
- `.github/agents/social-twitter.agent.md` — Added Step 1b visual pack detection + Visual-First Procedure (Practitioner + Executive modes) with final-tweet-only canonical URL rule; existing text-only path preserved
- `.github/agents/platform-distiller.agent.md` — Replaced `Critical Constraint: Text-Only Output` section (image prohibition) with `Visual-First Output Policy` (conditional image embedding per platform); Medium/Substack/LinkedIn Article output specs updated with visual-first/text-only branches; prohibited-string scan replaced with positive manifest verification

**Phase 3 — Pipeline Configuration**
- `content/pipeline-config.md` — Added `## Distillation Settings` section with `distillation_persona_mode` (value: `practitioner`) and `distillation_slug` fields; added `## Pipeline Steps Reference` table with `Step 4a-visual` (visual-pack-generator); updated `### Publish Sequence` to Day 0 cadence with visual pack generation as first step

### Removed

*(none)*

## Additional or Deviating Changes

- **`medium-post-cost-part1.md` naming** (DD-05): `medium-post-part1.md` already existed (context-engineering article); new cost-article distillation uses `medium-post-cost-part1.md` to avoid collision. Same pattern applied to substack and linkedin-article files.
- **FancyBboxPatch API fix**: 12 call sites in `render_distilled.py` required `(x, y)` tuple wrapping; `bbox_inches='tight'` removed from both renderers to preserve target pixel dimensions at 320 DPI.
- **Pipeline Steps Reference table**: Phase 3 added a new `## Pipeline Steps Reference` table rather than inserting into the existing checkbox checklist, as the checklist is used for per-run tracking and the reference table is persistent documentation.

## Release Summary

Implemented the complete Visual-First Distillation System. The system adds a `visual-pack-generator` skill (4 files) that generates platform-optimized visual asset packs from blog content in two persona modes (Practitioner carousel grammar, Executive exhibit grammar). Three distribution agents (social-linkedin, social-twitter, platform-distiller) now detect visual packs and follow visual-first paths when manifests exist, while preserving text-only fallback for backward compatibility. The foundational change is the reversal of the image prohibition in `platform-distiller.agent.md`. Demo artifacts generated for Part 1: 31 visual assets across 2 modes, 10 distilled posts. All 15 dimension spot-checks passed at 1080×1080, 1600×900, 1400×800, 1200×800, 1200×630, and 1200×627px at 320 DPI.
