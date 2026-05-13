<!-- markdownlint-disable-file -->
# Implementation Review: Visual-First Distillation System

**Date**: 2026-05-13
**Related Plan**: `.copilot-tracking/plans/2026-05-13/visual-first-distillation-system-plan.instructions.md`
**Changes Log**: `.copilot-tracking/changes/2026-05-13/visual-first-distillation-system-changes.md`
**Research Document**: `.copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md`
**Review Log**: `.copilot-tracking/reviews/2026-05-13/visual-first-distillation-system-review.md`

## Status: ❌ Visual-Reviewer FAIL — All 31 PNGs blocked; renderer requires systemic fix before re-render

**Rework Cycle 1 date**: 2026-05-13 — content, spec, and agent fixes complete ✅
**Visual-Reviewer run**: 2026-05-13 — FAILED; 3 systemic root causes identified

### Visual-Reviewer Findings Summary

| Pack | Assets | Dimensions | bbox_inches | Text rendering | Verdict |
|------|--------|-----------|------------|----------------|---------|
| Practitioner | 20 | ✅ All correct | ✅ Absent | ❌ All overflow/clip | **FAIL** |
| Executive | 11 | ✅ All correct | ✅ Absent | ❌ All overflow/clip | **FAIL** |

**Root Cause 1 (Critical — all 31 assets):** Font/DPI coordinate mismatch. `make_fig()` sets pixel-space axes (`xlim(0, W)`) but matplotlib `fontsize` is in typographic points. At DPI=320, every font renders 4.44× larger than intended. "120x" at fontsize=108 renders 1,248px wide on a 1,080px canvas.
**Fix:** `def fs(pt): return pt * 72 / DPI` helper; replace all `fontsize=N` with `fontsize=fs(N)`.

**Root Cause 2 (Critical — all 31 assets):** Design token hex values in renderer `TOKENS` dicts do not match canonical system. `ACCENT` = `#f97316` (orange) vs canonical `#1f6feb` (blue). `WARN` = amber (`#eab308`) vs canonical red (`#dc2626`) — semantic inversion on "bad" data items.
**Fix:** Remove local `TOKENS` dict; hardcode canonical values from `copilot-instructions.md`.

**Root Cause 3 (Critical — x-exhibit-02.png):** `$` signs in strings parsed as LaTeX math mode — dollar signs dropped from rendered financial figures.
**Fix:** `matplotlib.rcParams['text.usetex'] = False` + escape `$` as `\$`.

**Root Cause 4 (Major — 5 practitioner slides):** Unicode em dash `—` (U+2014) in string literals — renders as mojibake on some platforms.
**Fix:** Replace all `—` with ASCII ` - `.

### Required Action: Renderer Rework + Re-render

Both `render_distilled.py` files require fixes before re-rendering. Then visual-reviewer must be re-run.

| Priority | Fix | Renderer |
|----------|-----|----------|
| P0-A | Add `fs()` DPI-scaler; apply to ALL fontsize calls | Both |
| P0-B | Remove theme rotation; use canonical token hex values | Both |
| P0-C | `text.usetex = False`; escape `$` | Executive |
| P1 | Replace Unicode em dashes with ASCII ` - ` | Practitioner |
| P2 | Post-scale: audit residual overlaps, label positions | Both |

---

## Severity Counts (combined: RPI + Implementation Validator)

| Severity | RPI Count | IV Count | Total |
|----------|-----------|----------|-------|
| Critical | 1         | 3        | **4** |
| Major    | 7         | 9        | **16**|
| Minor    | 7         | 6        | **13**|
| **Total**| **15**    | **18**   | **33**|

> Note: Several findings overlap between RPI and IV validators (e.g., LinkedIn canonical URL, medium inline dimensions). The totals above count each finding once per validator that raised it; the rework table below deduplicates.

---

## Phase 1: Artifact Discovery

| Artifact | Path | Found |
|----------|------|-------|
| Implementation Plan | `.copilot-tracking/plans/2026-05-13/visual-first-distillation-system-plan.instructions.md` | ✅ |
| Changes Log | `.copilot-tracking/changes/2026-05-13/visual-first-distillation-system-changes.md` | ✅ |
| Research Document | `.copilot-tracking/research/2026-05-13/visual-first-distillation-system-research.md` | ✅ |
| RPI Validation — Phase 1 | `.copilot-tracking/reviews/rpi/2026-05-13/visual-first-distillation-system-001-validation.md` | ✅ |
| RPI Validation — Phase 2 | `.copilot-tracking/reviews/rpi/2026-05-13/visual-first-distillation-system-002-validation.md` | ✅ |
| RPI Validation — Phase 3 | `.copilot-tracking/reviews/rpi/2026-05-13/visual-first-distillation-system-003-validation.md` | ✅ |
| RPI Validation — Phase 4 | `.copilot-tracking/reviews/rpi/2026-05-13/visual-first-distillation-system-004-validation.md` | ✅ |
| Implementation Validator report | `.copilot-tracking/reviews/2026-05-13/visual-first-distillation-system-impl-quality.md` | ✅ |

---

## Phase 2: RPI Validation (per plan phase)

### Phase 1 — Skill Creation
**Status:** ⚠️ 2 Major, 1 Minor

| ID | Severity | Description |
|----|----------|-------------|
| F-001 | Major | Medium inline image dimensions: SKILL.md + platform-specs.md say `1200×800px`; research says `1400px minimum width`. Render scripts coded at 1200px. Changes log falsely documents as `(1400×800px)`. |
| F-002 | Major | X/Twitter file naming: SKILL.md + platform-specs.md use `twitter-card-*.png`; agents + actual files use `x-card-*.png` (Practitioner) and `x-exhibit-*.png` (Executive). Consuming agents would look for wrong filenames. |
| F-003 | Minor | SKILL.md renderer template comment shows `bbox_inches='tight'` — explicitly removed from actual renderers; future implementers may re-add it. Should be annotated as "do NOT use." |

### Phase 2 — Agent Updates
**Status:** ✅ PASSED (29/29 checks) + 1 Minor

| ID | Severity | Description |
|----|----------|-------------|
| M-001 | Minor | `platform-distiller.agent.md` line 7 opening sentence still says "text-only" (stale prose; no behavioral impact). |

### Phase 3 — Pipeline Config Update
**Status:** ⚠️ 2 Major, 5 Minor

| ID | Severity | Description |
|----|----------|-------------|
| MAJOR-01 | Major | `pipeline-config.md` line 201 — `### Long-Form Platform Distribution (Step 12)` still says "No images or media — copy-paste ready", directly contradicting Phase 2 visual-first change. |
| MAJOR-02 | Major | `pipeline-config.md` line 264 — Pipeline Steps Reference table Step 12 entry says "text-only excerpts" — stale language from pre-Phase 2. |
| MINOR-01 | Minor | `distillation_persona_mode` default is `practitioner`; Details spec said `ask`. Deviation not documented. |
| MINOR-02 | Minor | `publish_cadence` field added but the `distillation_slug` field references a separate Distillation Settings section — minor structural inconsistency. |
| MINOR-03 | Minor | `pipeline-config.md` new fields have no inline comments explaining allowed values. |
| MINOR-04 | Minor | Step 4a-visual description references "Step 4b" (social-linkedin) but the table labels it "Step 4." |
| MINOR-05 | Minor | The Distillation Settings section does not specify a fallback value for `distillation_persona_mode` if left blank. |

### Phase 4 — Demo Generation
**Status:** ❌ 1 Critical, 3 Major, 4 Minor

| ID | Severity | Description |
|----|----------|-------------|
| C-01 | Critical | Step 4.4 (visual-reviewer QA) was NOT executed. Plan success criterion requires visual-reviewer QA with no critical findings. Manual spot-checks in changes log are not a substitute. |
| M-01 | Major | `medium-post-cost-part1.md` is 624 words; target is 700–900 words (76 words short). |
| M-02 | Major | Medium inline images at 1200×800px; changes log falsely documents them as 1400×800px. |
| M-03 | Major | Both LinkedIn post files embed canonical URL inside `── START COPY ──` block (reach penalty violation). |
| m-01 | Minor | `medium-post-cost-part1.md` has no Medium Import tool instruction — without it, images break and canonical protection fails. |
| m-02 | Minor | Substack note is 319 characters; target is 150–300. |
| m-03 | Minor | Executive LinkedIn post `content/linkedin-post-part1-executive.md` is 28 lines; target is 30–40 line range for the exhibit-grammar format. |
| m-04 | Minor | `content/x-twitter-thread-part1-executive.md` tweet 5 character count not verified in changes log. |

---

## Phase 3: Quality Validation (Implementation Validator)

Full report: `.copilot-tracking/reviews/2026-05-13/visual-first-distillation-system-impl-quality.md`

### Critical Findings

| ID | Description | Affected Files |
|----|-------------|----------------|
| IV-001 | `../visuals/` relative image paths resolve outside `content/` — all inline images broken on Medium/LinkedIn Article import | `medium-post-cost-part1.md`, `medium-post-cost-part1-executive.md`, `linkedin-article-cost-part1.md`, `linkedin-article-cost-part1-executive.md` |
| IV-002 | Canonical URL embedded in LinkedIn post body — activates LinkedIn reach penalty | `linkedin-post-part1-practitioner.md`, `linkedin-post-part1-executive.md` |
| IV-003 | Final X/Twitter tweet has image (`x-card-04.png`) AND canonical URL — violates agent's own no-image-on-final-tweet rule | `x-twitter-thread-part1-practitioner.md` |

### Major Findings

| ID | Description |
|----|-------------|
| IV-004 | Both renderers use `DejaVu Sans` — all 22 PNGs violate Helvetica Neue mandate in `copilot-instructions.md` and `visual-standards.instructions.md` |
| IV-005 | SKILL.md naming convention (`slide-01.png`, `twitter-card-*.png`) mismatches actual files (`slide-01-hook.png`, `x-card-*.png`) and agents — three-way split |
| IV-006 | `social-linkedin.agent.md` Executive mode references bare `exhibit-01.png`; actual files use `exhibit-01-context.png` etc. — fresh run would fall back to text-only |
| IV-007 | `$3K→$970/day` case study attributed to "Towards Data Science" in all 10 posts; `pipeline-config.md` maps this figure to MindStudio |
| IV-008 | Volatile pricing/multiplier data (120x multiplier, consumption billing) presented as permanent facts — `content-quality.instructions.md` requires caveats |
| IV-009 | LinkedIn posts use `**Markdown bold**` not Unicode Mathematical Bold Sans-Serif — asterisks render as literal on LinkedIn |
| IV-010 | `platform-distiller.agent.md` Substack spec says "300–500 words"; `platform-specs.md` says "150–300 characters" — unresolvable unit conflict |
| IV-011 | Phase 5 (Validation) not in changes log — root cause of IV-001, IV-002, IV-003 shipping undetected |

### Minor Findings

| ID | Description |
|----|-------------|
| IV-012 | ━━━ separators missing from LinkedIn post copy blocks |
| IV-013 | First-person "sharing my learnings" voice absent from Medium and LinkedIn Article content |
| IV-014 | Executive navy `#051C2C` is an ad-hoc hex outside the 15-token system — violates SKILL.md's own Critical Rule |
| IV-015 | `copilot-instructions.md` has verbatim duplicate `## Social Formatting Conventions` section |
| IV-016 | `pipeline-config.md` Series Configuration table shows stale `pending-assessment` |
| IV-017 | Executive renderer docstring claims "12 PNG assets" but manifest and disk show 11 |
| IV-018 | `platform-distiller.agent.md` specifies `substack-post-{slug}` but correct semantic name is `substack-note-{slug}` |

---

## Phase 4: Review Completion

### Overall Status

**⚠️ NEEDS REWORK** — The implementation is structurally sound and architecturally correct, but has 4 Critical findings and 16 Major findings that must be remediated before the demo artifacts and spec documents can be used as practitioner templates.

The infrastructure layer (skill, agents, pipeline-config) is high quality and production-capable after addressing spec-drift findings (IV-005, IV-006, IV-010). The demo content layer has correctness issues that would cause real harm if copy-pasted as-is: broken image paths, LinkedIn reach-penalty trap, and a conflicting Twitter final-tweet pattern.

### Rework Prioritization

**P0 — Blocking (Critical):**

| # | Finding | Files to Fix |
|---|---------|-------------|
| 1 | IV-001: Fix `../visuals/` → `visuals/` image paths | `medium-post-cost-part1.md`, `medium-post-cost-part1-executive.md`, `linkedin-article-cost-part1.md`, `linkedin-article-cost-part1-executive.md` |
| 2 | IV-002 / M-03: Move canonical URL from START COPY block to FIRST COMMENT section | Both LinkedIn posts |
| 3 | IV-003: Move `x-card-04.png` off final tweet; final tweet = text only | `x-twitter-thread-part1-practitioner.md` |
| 4 | C-01: Run `visual-reviewer` agent on all 31 PNGs in `part1-practitioner/` and `part1-executive/` | All PNG assets |

**P1 — High (Major, spec correctness):**

| # | Finding | Files to Fix |
|---|---------|-------------|
| 5 | F-002 / IV-005: Fix X/Twitter naming: `twitter-card-*` → `x-card-*` in SKILL.md + platform-specs.md | `SKILL.md`, `platform-specs.md` |
| 6 | IV-006: Fix Executive exhibit filenames in social-linkedin Step 1 | `social-linkedin.agent.md` |
| 7 | MAJOR-01 / MAJOR-02: Remove "text-only"/"no images" from pipeline-config lines 201, 264 | `pipeline-config.md` |
| 8 | IV-009: Replace Markdown bold with Unicode 𝗕𝗼𝗹𝗱 in LinkedIn posts | Both LinkedIn posts |

**P2 — Medium (Major, content quality):**

| # | Finding | Files to Fix |
|---|---------|-------------|
| 9 | IV-007: Correct "Towards Data Science" attribution → MindStudio (verify source first) | All 10 demo posts |
| 10 | IV-008: Add "as of May 2026, subject to change" caveats for pricing data | All 10 demo posts |
| 11 | M-01 / IV-013: Expand `medium-post-cost-part1.md` by ~80 words; add first-person voice | `medium-post-cost-part1.md` |
| 12 | m-01: Add Medium Import tool instruction | `medium-post-cost-part1.md` |
| 13 | F-001 / M-02: Resolve 1200px vs 1400px medium inline dimension conflict; fix render scripts + docs | `render_distilled.py` (both), `SKILL.md`, `platform-specs.md`, `changes.md` |

**P3 — Low (Minor):**

| # | Finding | Files to Fix |
|---|---------|-------------|
| 14 | IV-004: Fix font — `DejaVu Sans` → `Helvetica Neue` (with fallback) in both renderers | Both `render_distilled.py`, both manifests |
| 15 | IV-010 / m-02: Resolve Substack word/char count conflict; trim note to ≤300 chars | `platform-distiller.agent.md`, `substack-note-cost-part1.md` |
| 16 | F-003: Annotate `bbox_inches='tight'` in SKILL.md template as "do NOT use" | `SKILL.md` |
| 17 | M-001: Fix "text-only" opening prose in platform-distiller (line 7) | `platform-distiller.agent.md` |
| 18 | MINOR-04 / IV-018: Fix "Step 4b" ref in pipeline-config; fix `substack-post-` → `substack-note-` in platform-distiller | `pipeline-config.md`, `platform-distiller.agent.md` |
| 19 | IV-014: Register `#051C2C` as 16th design token or document as Executive-mode extension | `copilot-instructions.md` or `SKILL.md` |
| 20 | IV-015: Remove duplicate `## Social Formatting Conventions` from `copilot-instructions.md` | `copilot-instructions.md` |
| 21 | IV-016: Update Series Configuration table in `pipeline-config.md` | `pipeline-config.md` |
| 22 | IV-017: Fix executive renderer docstring "12 PNG assets" → "11 PNG assets" | `render_distilled.py` (executive) |
| 23 | IV-012: Add ━━━ separators to LinkedIn post copy blocks | Both LinkedIn posts |

---

## Open Questions (require human decision before rework)

1. **Medium inline 1200px vs 1400px** — intentional render trade-off or spec error? Answer determines whether render scripts need re-run.
2. **LinkedIn first-comment** — add automated `── FIRST COMMENT ──` section to social publisher, or is this a manual step?
3. **"Towards Data Science" attribution** — was this an intentional or hallucinated source? Verify the MindStudio URL before correcting 10 files.
4. **Helvetica Neue availability** — was DejaVu Sans an intentional platform fallback? If so, update spec to document the fallback chain.
5. **Executive navy `#051C2C`** — register as 16th global token, or define as Executive-mode extension in SKILL.md only?
6. **Phase 5 validation** — execute visual-reviewer retroactively (C-01 rework), or defer until next pipeline run?
7. **`distillation_persona_mode` default** — keep `practitioner` (demo-ready) or change to `ask` per original spec?

---

## Follow-Up Items

- [ ] Answer open questions 1–7 before starting rework cycle
- [ ] Run `/task-implement` rework for P0 Critical findings first
- [ ] Run `visual-reviewer` on all 31 PNGs as a standalone task (C-01)
- [ ] Consider creating RPI-004b for executive-mode distilled posts (5 files not validated by Phase 4 RPI)
- [ ] After rework: re-run this review cycle to confirm all Critical + Major findings resolved
