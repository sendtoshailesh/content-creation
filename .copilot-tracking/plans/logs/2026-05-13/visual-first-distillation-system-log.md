<!-- markdownlint-disable-file -->
# Planning Log: Visual-First Distillation System for Thought Leadership

## Discrepancy Log

Gaps and differences identified between research findings and the implementation plan.

### Unaddressed Research Items

* DR-01: Weighted scoring rubric (12 dimensions, 1-5 scale) for evaluating distilled post quality
  * Source: .copilot-tracking/research/subagents/2026-05-13/thought-leadership-psychology-frameworks.md
  * Reason: The scoring rubric is a quality-measurement tool, not an implementation artifact. It can be integrated into the visual-reviewer or a future quality-scoring step but is not required for the initial visual-pack-generator build.
  * Impact: low

* DR-02: Full demo matrix coverage (5 outputs × 3 parts × 2 modes = 30 artifacts)
  * Source: .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 273-276)
  * Reason: Plan constrains demo to Part 1 only (10 artifacts) per research recommendation. Parts 2 and 3 are follow-on work after the system is validated.
  * Impact: low

* DR-03: Cross-platform sequencing automation (Day 0 → Day 1 → Day 3 → Day 7+ cadence)
  * Source: .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 186-195)
  * Reason: Sequencing is already documented in pipeline-config.md publish sequence. The visual-first system generates assets; scheduling is handled by existing social-publisher agent.
  * Impact: low

* DR-04: Reference accounts study (Justin Welsh, Lenny Rachitsky, Sahil Bloom, HBR, McKinsey formatting)
  * Source: .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 47-48)
  * Reason: Already incorporated into subagent research (practitioner-carousel-framework.md, executive-exhibit-framework.md). No additional implementation action needed.
  * Impact: none

* DR-05: Developer audience preference for functional visuals over decorative imagery
  * Source: .copilot-tracking/research/subagents/2026-05-13/visual-content-engagement-data.md (Line 118)
  * Reason: The slide grammar and exhibit framework inherently produce functional data-driven visuals (charts, diagrams, frameworks) rather than decorative stock imagery. Not explicitly encoded as a skill constraint but mitigated by design.
  * Impact: low

* DR-05: Developer audience functional-visual preference not encoded as explicit skill constraint
  * Source: .copilot-tracking/research/subagents/2026-05-13/visual-content-engagement-data.md; .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Line 118)
  * Reason: Research identifies that developer audiences prefer functional visuals (diagrams, architecture) over decorative imagery. The visual-pack-generator Critical Rules (details lines 79-88) specify design tokens, DPI, fonts, and color palettes but do not explicitly encode a "functional over decorative" constraint. The skill's focus on data-driven carousel slides and exhibits implicitly favors functional visuals, but without an explicit rule, future content could drift toward decorative elements that underperform with the target audience.
  * Impact: low — mitigated by the inherently data-driven nature of the slide grammar and exhibit conventions

### Plan Deviations from Research

* DD-01: Pipeline step placement — skill invocation instead of new numbered step
  * Research recommends: A distinct new pipeline step for visual pack generation
  * Plan implements: The `visual-pack-generator` skill is invoked within the existing Steps 4b, 5, and 12 by each agent, rather than adding a standalone step. Pipeline-config gets a documentation-only step reference (Step 4a-visual) for visibility.
  * Rationale: Skills are invoked by agents implicitly in the existing pipeline pattern. Adding a standalone step would require orchestrator changes. Having each agent invoke the skill on-demand preserves the current architecture.

* DD-02: Carousel PDF generation — delegated to manual Canva/export step rather than automated PDF assembly
  * Research recommends: Automated PDF carousel generation from slide PNGs
  * Plan implements: The visual-pack-generator produces individual slide PNGs. PDF assembly from PNGs is noted as a follow-on automation (WI-02). For demo, slides are uploaded individually or assembled manually.
  * Rationale: matplotlib/Pillow can generate individual PNGs reliably. Automated PDF assembly (with proper page sizing, compression, LinkedIn compatibility) requires additional tooling (reportlab/fpdf2) not currently in requirements.txt. Adding it increases scope without blocking the core visual-first capability.

* DD-03: Serif typography in Executive mode — existing renderer uses Helvetica Neue exclusively
  * Research recommends: Serif headlines for gravitas in Executive exhibit mode
  * Plan implements: Helvetica Neue Bold for all typography (consistent with design token system)
  * Rationale: Single-font convention simplifies rendering. Executive gravitas achieved through data-ink ratio, minimal color, and exhibit labeling.

* DD-04: Skill file naming — directory-based SKILL.md vs flat .skill.md
  * Research recommends: Flat `.skill.md` file referenced in research architecture scenario
  * Plan implements: Directory-based `.github/skills/visual-pack-generator/SKILL.md` with `references/` subdirectory
  * Rationale: Matches existing project convention — all 7 existing skills use directory + SKILL.md pattern
  * Research recommends: Serif headlines for gravitas in Executive exhibit mode (research Lines 159)
  * Plan implements: Executive mode uses Helvetica Neue Bold for headlines (consistent with existing design token system) instead of serif fonts
  * Rationale: The visual-renderer agent and design token system standardize on Helvetica Neue. Introducing serif fonts requires font file management, cross-platform testing, and breaks the single-font convention. Executive gravitas is achieved through data-ink ratio, minimal color palette, and exhibit labeling conventions instead.

* DD-04: Skill file structure — directory-based SKILL.md vs flat .skill.md file
  * Research recommends: `.github/skills/visual-pack-generator.skill.md` (flat file, research Lines 228, 240)
  * Plan implements: `.github/skills/visual-pack-generator/SKILL.md` with `references/` subdirectory containing slide-grammar.md, platform-specs.md, and psychology-stack.md
  * Rationale: All 7 existing skills in the repository use the directory-based convention (`{skill-name}/SKILL.md`). The plan correctly follows established project conventions. The directory structure also enables the `references/` subdirectory pattern needed for the 3 reference files, which would otherwise require a separate organizational approach.

## Implementation Paths Considered

### Selected: Layered `visual-pack-generator` Skill + Existing Agents Consume It

* Approach: Create a new skill that generates visual asset packs (carousel slides, exhibit images, hero images) organized by platform and persona mode. Update the 3 existing distribution agents to consume these visual packs and embed them into their respective outputs.
* Rationale: Preserves separation of concerns. Each agent retains its platform-specific expertise. Visual generation is centralized in a reusable skill. Incremental migration — update one agent at a time. Visual pack can be regenerated independently.
* Evidence: .copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md (Lines 223-267)

### IP-01: Single `visual-distiller` Agent (Replaces 3 Existing Agents)

* Approach: A monolithic agent that reads the base blog, selects persona mode, generates all visuals, and emits all 5 distilled outputs in one invocation.
* Trade-offs: Simpler orchestration (single entry point) vs. enormous prompt surface (5 platform specs × 2 persona modes = 10 behavioral variants), regression risk (changes to one platform break others), breaks existing pipeline Steps 4-5 and 12.
* Rejection rationale: Violates separation of concerns. The existing pipeline architecture is well-tested. A monolithic replacement introduces regression risk and makes per-platform iteration impossible. The prompt would exceed practical limits for reliable output.

## Suggested Follow-On Work

Items identified during planning that fall outside current scope.

* WI-01: Extend demo to Parts 2 and 3 — Generate visual packs and regenerate distilled posts for remaining 2 parts of the AI Code Assistant Cost series (20 additional artifacts) (medium priority)
  * Source: DR-02 (constrained demo scope)
  * Dependency: Phase 4 completion (Part 1 demo validated)

* WI-02: Automated PDF carousel assembly — Add reportlab/fpdf2 dependency and automate PDF generation from carousel slide PNGs for LinkedIn upload (medium priority)
  * Source: DD-02 (manual PDF assembly)
  * Dependency: Phase 1 completion (visual-pack-generator skill exists)

* WI-03: Integrate psychology scoring rubric into visual-reviewer — Extend the visual-reviewer's checklist with the 12-dimension weighted scoring rubric from thought-leadership-psychology-frameworks.md (low priority)
  * Source: DR-01 (unaddressed scoring rubric)
  * Dependency: Phase 5 completion (system validated end-to-end)

* WI-04: Add `content-pipeline.agent.md` orchestration for visual distillation — Update the content-pipeline orchestrator to automatically invoke visual-pack-generator before distribution steps when `distillation_persona_mode` is set (medium priority)
  * Source: Planning analysis of pipeline integration
  * Dependency: Phase 3 completion (pipeline-config updated)

* WI-05: Platform-specific A/B testing framework — Track engagement metrics (carousel vs text-only) across LinkedIn and X/Twitter to validate the 1.5-6x engagement uplift hypothesis (low priority)
  * Source: .copilot-tracking/research/subagents/2026-05-13/visual-content-engagement-data.md
  * Dependency: WI-01 completion (sufficient artifacts for comparison)
