---
applyTo: '.copilot-tracking/changes/2026-05-13/visual-first-distillation-system-changes.md'
---
<!-- markdownlint-disable-file -->
# Implementation Plan: Visual-First Distillation System for Thought Leadership

## Overview

Build a reusable visual-first distillation system that converts blog posts into traffic-attracting, brand-building distilled posts across LinkedIn (Post + Article), X/Twitter, Medium, and Substack — using predominantly VISUAL outputs (carousels, exhibits, image cards) with two selectable persona modes (Practitioner and Executive), layered as a new `visual-pack-generator` skill consumed by the 3 existing distribution agents.

## Objectives

### User Requirements

* Create a `visual-pack-generator` skill that generates platform-optimized visual asset packs from blog content — Source: research document (Lines 223-267)
* Support two selectable persona modes: Practitioner (Welsh/Lenny/Bloom carousel grammar) and Executive (HBR/McKinsey exhibit grammar) — Source: user task description
* Update `social-linkedin.agent.md` to consume carousel slides and emit PDF carousel references — Source: research architecture decision (Lines 230-231)
* Update `social-twitter.agent.md` to consume image cards and emit image-anchored threads — Source: research architecture decision (Lines 232)
* Update `platform-distiller.agent.md` to REVERSE the image prohibition (lines 14-28) and consume visual assets — Source: research architecture decision (Lines 233)
* Add `distillation_persona_mode` field to `pipeline-config.md` — Source: research assumptions (Line 25)
* Demo by regenerating Part 1 of the AI Code Assistant Cost series in both persona modes (10 artifacts) — Source: research demo plan (Lines 273-290)

### Derived Objectives

* Create a `content/visuals/distilled/` output directory structure organized by part and persona mode — Derived from: platform constraints require different image dimensions per platform, and persona modes produce different visual types
* Define a slide-grammar template system mapping slide types (hook, problem, framework, data exhibit, before/after, quote, CTA) to both persona modes — Derived from: research frameworks require structured slide taxonomy for reproducibility
* Preserve canonical-URL discipline across all visual outputs (link in first comment for LinkedIn, last tweet for X, Import tool for Medium) — Derived from: SEO protection is a pipeline-wide invariant
* Add a new pipeline step (Step 3c-visual or Step 11b) for visual pack generation that runs AFTER blog visuals (Step 3b) and BEFORE social distribution (Steps 4-5, 12) — Derived from: the visual pack must exist before agents can consume it
* Update the publish sequence cadence to include visual asset uploads alongside text distribution — Derived from: carousel PDFs and image cards require separate upload steps

## Context Summary

### Project Files

* `.github/agents/social-linkedin.agent.md` - LinkedIn post generation agent, currently text-only
* `.github/agents/social-twitter.agent.md` - X/Twitter thread generation agent, currently text-only
* `.github/agents/platform-distiller.agent.md` - Platform distillation agent (Medium, Substack, LinkedIn Article) with explicit image prohibition at lines 14-28
* `.github/agents/visual-renderer.agent.md` - Visual asset generation engine (matplotlib + Pillow + Mermaid, 5 themes, 320 DPI)
* `.github/agents/visual-reviewer.agent.md` - Visual QA critic agent with 6-category checklist
* `.github/skills/visual-rendering/SKILL.md` - Visual rendering skill with design token references
* `content/pipeline-config.md` - Pipeline configuration with 12+ step sequence
* `content/visuals/` - 17 existing PNG assets + 5 Python renderer scripts

### References

* .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md - Primary research (297 lines) covering psychology frameworks, persona modes, platform specs, architecture decision, demo plan
* .copilot-tracking/research/subagents/2026-05-13/practitioner-carousel-framework.md - 695 lines, 10-slide carousel template, 7 hook archetypes
* .copilot-tracking/research/subagents/2026-05-13/executive-exhibit-framework.md - 1413 lines, 4-zone exhibit anatomy, conclusion-as-title convention
* .copilot-tracking/research/subagents/2026-05-13/platform-visual-specs.md - 509 lines, per-platform dimensions, copy budgets, CTA rules
* .copilot-tracking/research/subagents/2026-05-13/thought-leadership-psychology-frameworks.md - 460 lines, 12 frameworks, weighted scoring rubric
* .copilot-tracking/research/subagents/2026-05-13/visual-content-engagement-data.md - 350+ lines, engagement multipliers, developer audience preferences
* .copilot-tracking/research/subagents/2026-05-13/codebase-architecture-for-distillation.md - Codebase architecture analysis

### Standards References

* .github/copilot-instructions.md — Design token system (15 tokens), font (Helvetica Neue), DPI (320), no Unicode glyphs in matplotlib
* .github/instructions/social-formatting.instructions.md — LinkedIn/X use Unicode Mathematical Bold/Italic; Reddit standard Markdown
* .github/instructions/content-quality.instructions.md — Every claim needs concrete data; first-person voice; no corporate framing
* .github/instructions/visual-standards.instructions.md — Visual asset rendering standards

## Implementation Checklist

### [ ] Implementation Phase 1: Create Visual Pack Generator Skill

<!-- parallelizable: true -->

* [ ] Step 1.1: Create `.github/skills/visual-pack-generator/SKILL.md` — the core skill definition
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 15-95)
* [ ] Step 1.2: Create `.github/skills/visual-pack-generator/references/slide-grammar.md` — slide type taxonomy for both persona modes
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 97-150)
* [ ] Step 1.3: Create `.github/skills/visual-pack-generator/references/platform-specs.md` — per-platform visual dimensions and constraints
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 152-195)
* [ ] Step 1.4: Create `.github/skills/visual-pack-generator/references/psychology-stack.md` — framework-to-slide-position mapping
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 197-230)

### [ ] Implementation Phase 2: Update Existing Agents for Visual Consumption

<!-- parallelizable: true -->

* [ ] Step 2.1: Update `social-linkedin.agent.md` — add carousel/exhibit consumption and PDF carousel reference output
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 236-290)
* [ ] Step 2.2: Update `social-twitter.agent.md` — add image-card consumption and image-anchored thread output
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 292-340)
* [ ] Step 2.3: Update `platform-distiller.agent.md` — REVERSE image prohibition (lines 14-28), add visual asset consumption for Medium, Substack, LinkedIn Article
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 342-420)

### [ ] Implementation Phase 3: Update Pipeline Configuration

<!-- parallelizable: false -->

* [ ] Step 3.1: Add `distillation_persona_mode` field to `content/pipeline-config.md`
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 426-460)
* [ ] Step 3.2: Add visual-pack-generation step to the pipeline step sequence (new Step 4a-visual between social-strategist and social-linkedin)
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 462-490)
* [ ] Step 3.3: Update publish sequence cadence to include visual asset upload steps
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 492-520)

### [ ] Implementation Phase 4: Demo — Regenerate Part 1 Visual Packs

<!-- parallelizable: false -->

* [ ] Step 4.1: Generate Practitioner-mode visual pack for Part 1 (10-slide carousel + image cards + hero images)
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 526-570)
* [ ] Step 4.2: Generate Executive-mode visual pack for Part 1 (3-5 exhibits + hero images)
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 572-610)
* [ ] Step 4.3: Regenerate Part 1 distilled posts using both visual packs (10 artifacts total)
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 612-665)
* [ ] Step 4.4: Run visual-reviewer on all generated assets
  * Details: .copilot-tracking/details/2026-05-13/visual-first-distillation-system-details.md (Lines 667-690)

### [ ] Implementation Phase 5: Validation

<!-- parallelizable: false -->

* [ ] Step 5.1: Verify all new/modified agent files parse correctly (no frontmatter errors, no broken references)
  * Validate `.github/skills/visual-pack-generator/SKILL.md` exists with correct frontmatter
  * Validate all 3 updated agent files have consistent structure
  * Validate `pipeline-config.md` has new fields without breaking existing config
* [ ] Step 5.2: Verify demo artifacts are complete and platform-ready
  * Confirm 10 demo artifacts exist in `content/visuals/distilled/part1-practitioner/` and `content/visuals/distilled/part1-executive/`
  * Verify each distilled post references correct visual assets
  * Check copy-paste readiness: text wrapped in START/END COPY markers, images at correct dimensions
* [ ] Step 5.3: Report blocking issues
  * Document issues requiring additional research
  * Provide user with next steps and recommended planning
  * Avoid large-scale fixes within this phase

## Planning Log

See .copilot-tracking/plans/logs/2026-05-13/visual-first-distillation-system-log.md for discrepancy tracking, implementation paths considered, and suggested follow-on work.

## Dependencies

* Existing `visual-renderer` agent (matplotlib + Pillow + Mermaid + 5-theme palette + 320 DPI) — production engine for generating all visual assets
* Existing `visual-reviewer` agent — QA gating for generated visuals
* Existing design token system (15 tokens) in `.github/copilot-instructions.md`
* Python 3.x with matplotlib, Pillow installed (existing `requirements.txt`)
* 17 existing PNG assets in `content/visuals/` — source material for carousel slides
* Published blog posts: `content/ai-code-assistant-cost-part-1.md`, `part-2.md`, `part-3.md`

## Success Criteria

* `visual-pack-generator` skill exists at `.github/skills/visual-pack-generator/SKILL.md` with complete slide grammar, platform specs, and psychology stack references — Traces to: user requirement for reusable visual distillation system
* `social-linkedin.agent.md` generates carousel PDF references in Practitioner mode and exhibit references in Executive mode — Traces to: user requirement for visual-first LinkedIn posts
* `social-twitter.agent.md` generates image-anchored threads with 1-4 images per tweet — Traces to: user requirement for visual-first X/Twitter threads
* `platform-distiller.agent.md` image prohibition reversed; generates Medium/Substack/LinkedIn Article with embedded visuals — Traces to: user requirement to reverse text-only constraint
* `pipeline-config.md` includes `distillation_persona_mode: practitioner | executive` field — Traces to: user requirement for persona mode selection
* 10 demo artifacts generated for Part 1 (5 outputs × 2 modes) that are copy-paste/upload ready — Traces to: user demo plan requirement
* All visual assets pass `visual-reviewer` QA with no critical findings — Traces to: existing quality gate convention
