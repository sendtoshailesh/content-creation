# Visual Opportunity Map: AI Agent Evals Series

## Summary

**Source content:** AI Agent Evals: Why SWE-bench Isn't Enough Before Production  
**Pipeline mode:** mandatory visual-first strategy  
**Platform scope:** Blog/GitHub Pages, LinkedIn, Medium, Substack, LinkedIn Article  
**Rendering policy:** programmatic-only visuals using Python, Pillow, Mermaid, matplotlib, and SVG via Python  

This map turns the current AI Agent Evals series into blog companion visuals and standalone visual assets. It is the handoff contract for `visual-renderer`, `social-linkedin`, `platform-distiller`, `content-repurposer`, and `visual-reviewer`.

> **Redesign status (2026-06-09):** Infographic-first redesign rendered and passed visual QA with no critical blockers. Remaining findings are polish items, not publication blockers: avoid orphan title wraps, strengthen a few connectors/annotations, and continue improving character differentiation in future passes.

## Blog Companion Visuals

| ID | Source section | Concept type | Audience persona | Visual family | Platform fit | Standalone potential | Required source data | Rendering approach | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| v01-benchmark-gap | Part 1: SWE-bench gap | Comparison / evidence | AI team decision-maker | Executive exhibit | Blog, LinkedIn Article, Medium | High | SWE-bench score, production acceptance gap, cited benchmark URLs | Pillow or matplotlib | P0 | rendered; QA passed |
| v02-failure-taxonomy | Part 1: production failure modes | Taxonomy | Tech lead, platform engineer | Infographic / one-pager | Blog, LinkedIn | High | Failure mode labels and source URLs | Pillow | P0 | covered by `linkedin-card-03-taxonomy.png` |
| v03-sourdough-test | Part 1: Sourdough Test | Narrative / mental model | Practitioner | Comic explainer / storyboard | Blog, LinkedIn | High | Test criteria from article | Pillow comic panels | P0 | rendered; QA passed |
| v04-minimum-viable-eval | Part 1: minimum viable eval | Checklist / framework | IC engineer, tech lead | Infographic / one-pager | Blog, LinkedIn | Medium | Eval checklist, grader categories | Pillow | P0 | covered by `one-page-eval-system.png` and `linkedin-card-04-framework.png` |
| v05-eval-pipeline | Part 2: build the eval system | Architecture / flow | Platform engineer | Architecture / flow diagram | Blog, Medium | High | Pipeline stages and CI gates | Mermaid or Pillow | P0 | rendered as `eval-ci-architecture.mmd` |
| v06-grading-decision-tree | Part 2: graders | Decision guidance | IC engineer, tech lead | Architecture / flow diagram | Blog, LinkedIn | Medium | Grader types and decision rules | Mermaid | P1 | follow-on optional |
| v07-regression-timeline | Part 2: regression control | Process / timeline | Tech lead | Infographic / one-pager | Blog, LinkedIn | Medium | Regression stages, CI/release gates | Pillow | P1 | follow-on optional |

## Standalone Distribution Visuals

| ID | Source section | Concept type | Audience persona | Visual family | Platform fit | Standalone potential | Required source data | Rendering approach | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| s01-linkedin-card-pack-gap | Series thesis | Visual argument | Practitioner | LinkedIn social card pack | LinkedIn | High | Benchmark vs production claim, sources | Pillow card pack | P0 | rendered; QA passed |
| s02-comic-agent-prod-fail | Part 1 failure story | Human scenario | Broad technical audience | Comic explainer / storyboard | LinkedIn, Blog | High | Failure taxonomy and eval lesson | Pillow comic panels | P0 | rendered; QA passed |
| s03-executive-risk-exhibits | Series leadership angle | Risk / ROI | AI team decision-maker | Executive exhibit set | LinkedIn Article, Medium | High | Benchmark gap, production risk, regression cost | Pillow or matplotlib | P0 | rendered; QA passed |
| s04-one-page-eval-system | Part 2 implementation | Saveable framework | Tech lead | Infographic / one-pager | LinkedIn, Substack | High | Eval system layers, grader examples, CI gates | Pillow | P0 | rendered; QA passed |
| s05-architecture-eval-ci | Part 2 CI architecture | System design | Platform engineer | Architecture / flow diagram | Blog, Medium | Medium | CI flow, task suite, graders, dashboard | Mermaid or Pillow | P1 | rendered; QA passed |

## Rendering Handoff

## Infographic Art Direction Briefs

### Package Layout Diversity Matrix

| Asset | Infographic type | Layout pattern | Hero visual | Required state change |
|---|---|---|---|---|
| v01 / s03 benchmark gap | Statistical executive exhibit | Broken bridge or dual gauge | Vendor-reported May 2026: 74-78% capability vs 35-50% acceptance gap | Confidence drops into production-risk gap |
| v03 / s02 Sourdough Test | Comic/storyboard | Four-panel incident story | Off-topic prompt causing persona drift | Neutral prompt -> wrong recipe -> correct redirect -> CI block |
| s04 eval system | Process / hierarchy infographic | Factory line or CI control tower | Task enters eval system and passes through checks | Input task -> grader scan -> gate pass/fail -> history update |
| s01 LinkedIn pack | Visual essay / carousel | Mixed layouts, one per card | Capability-vs-behavior thesis | Each card changes pattern: split, checklist, map, process, worksheet |
| s05 CI architecture | Process infographic | Annotated CI loop | PR change flows through eval gate | PR change -> tests -> fail branch -> debug trace -> rerun |

### v01-benchmark-gap / s03-executive-risk-exhibits Art Direction Brief

- Burning question: Why does a high SWE-bench score not equal production readiness?
- Infographic type: Statistical / comparison executive exhibit.
- Visual metaphor: Broken bridge between "benchmark capability" and "production acceptance", or dual gauges with a red risk gap.
- Layout: One hero headline, two large numerical anchors, central red gap zone, source strip.
- State changes: High confidence on benchmark side drops into lower PR acceptance; red gap is the story.
- Icon/illustration plan: Left gauge labeled capability signal; right gauge labeled behavior risk; bridge/gap marker in the middle.
- Text budget: Title <= 9 words; each side <= 8 words; one caveat line.
- Source line: Presenc May 2026; official SWE-bench source; vendor-reported point-in-time caveat.
- Renderer notes: Avoid a table. Use numbers as shapes, not text blocks.
- Visual-reviewer acceptance criteria: Reader understands "capability score != release confidence" in under 3 seconds.

### v03-sourdough-test / s02-comic-agent-prod-fail Art Direction Brief

- Burning question: How can one absurd prompt reveal persona drift?
- Infographic type: Comic/storyboard.
- Visual metaphor: Incident strip: prompt enters all agents, one deployment agent drifts into recipe mode, CI blocks the release.
- Layout: Four panels with changing environment: prompt card, chat failure, expected redirect, CI dashboard.
- State changes: Character/agent changes from neutral -> confidently wrong -> corrected -> blocked by CI. Use expression, color badge, and panel background changes.
- Icon/illustration plan: Do not repeat one human icon. Use distinct states: confused engineer, recipe-spewing agent, scope-aware agent, CI gate with 3 red cells out of 8.
- Text budget: Panel caption <= 14 words; speech bubble <= 12 words.
- Source line: First-party original Sourdough Test implementation, 3 of 8 agents failed.
- Renderer notes: Add visible "3/8 failed" grid and a red "persona drift" badge. Use bread icon only as the off-topic object, not as decoration.
- Visual-reviewer acceptance criteria: Panels must show setup, wrong behavior, expected behavior, and resolution without relying on surrounding blog text.

### s04-one-page-eval-system Art Direction Brief

- Burning question: What does a minimum production agent eval system look like?
- Infographic type: Process / hierarchy infographic.
- Visual metaphor: CI factory line or control tower.
- Layout: Task enters from left/top, moves through four stations: task suite, behavior graders, CI gate, regression history.
- State changes: Work item moves through scanners; CI gate opens for pass and blocks for fail; history panel accumulates incident dots.
- Icon/illustration plan: Use station icons with state: task stack, scanner/magnifier, gate/barrier, dashboard timeline. Add pass/fail branch.
- Text budget: Four station labels <= 3 words each; station captions <= 10 words.
- Source line: First-party original implementation: 8 agents, 38 tasks, 14 suites, 3 grader types.
- Renderer notes: Do not render as four text boxes. Use a path, connectors, gates, and a history dashboard.
- Visual-reviewer acceptance criteria: Reader sees a working eval system, not a checklist.

### s01-linkedin-card-pack-gap Art Direction Brief

- Burning question: What should teams test beyond benchmark capability?
- Infographic type: Visual essay / card pack.
- Visual metaphor: Journey from capability signal to behavior contract.
- Layout: Five varied cards:
  1. Split-screen or broken bridge.
  2. Empty tool-log annotated scene.
  3. Failure taxonomy map.
  4. CI factory/control tower process.
  5. Action worksheet.
- State changes: Each card changes visual pattern and moves the reader from problem to action.
- Icon/illustration plan: Use icons only for state/category: empty log, drift, gate, history, action.
- Text budget: Card title <= 8 words; body <= 24 words.
- Source line: Manifest-level source links plus visible caveat on metric cards.
- Renderer notes: Avoid same frame with different text. Each card needs a different composition.
- Visual-reviewer acceptance criteria: Carousel should feel like a visual argument, not a slide deck.

### s05-architecture-eval-ci Art Direction Brief

- Burning question: Where should production agent evals run?
- Infographic type: Process / architecture infographic.
- Visual metaphor: PR control loop.
- Layout: PR change enters, task suite runs, graders inspect output and trace, gate decides, fail branch returns debug trace, pass branch continues.
- State changes: Gate pass/fail branch must be visible; regression history updates after each run.
- Icon/illustration plan: PR icon, task stack, grader scanner, gate, debug trace, history timeline.
- Text budget: Node labels <= 4 words each.
- Source line: First-party original implementation; canonical guide.
- Renderer notes: Mermaid may be source-only; for social/blog hero, render a polished Pillow infographic version.
- Visual-reviewer acceptance criteria: Reader understands PR-level eval loop without reading implementation text.

### v01-benchmark-gap

- Visual family: Executive exhibit
- Platform: Blog + LinkedIn Article + Medium
- Size: 1200x627
- Renderer: Pillow or matplotlib
- Message: SWE-bench proves coding capability, not production behavior.
- Layout: conclusion-as-title, two-column comparison, source line.
- Must stand alone: yes

### v03-sourdough-test

- Visual family: Comic explainer / storyboard
- Platform: Blog + LinkedIn
- Size: 1080x1350 for LinkedIn, 3200x2080 for blog variant
- Renderer: `scripts/visuals/comic.py`
- Story arc: an off-topic "How do I bake sourdough?" prompt exposes persona drift, contrasts the wrong bread answer with the expected Azure-scope redirect, and shows CI blocking the regression before release.
- Panels: 4-panel escalation.
- Must stand alone: yes

### s01-linkedin-card-pack-gap

- Visual family: LinkedIn social card pack
- Platform: LinkedIn
- Size: 1080x1350
- Renderer: Pillow helpers from `scripts/visuals/`
- Message: "Benchmarks are table stakes; behavior contracts decide production readiness."
- Structure: split benchmark-vs-production contrast, pass/fail checklist, 2x3 failure taxonomy, four-layer eval stack, action worksheet.
- Must stand alone: yes

### s03-executive-risk-exhibits

- Visual family: Executive exhibit set
- Platform: LinkedIn Article + Medium
- Size: 1200x627
- Renderer: Pillow or matplotlib
- Exhibits:
  1. Context: benchmark gap creates false confidence.
  2. Evidence: failure taxonomy shows what benchmarks miss.
  3. Framework: production eval system catches behavior drift.
- Must stand alone: yes

### s04-one-page-eval-system

- Visual family: Infographic / one-pager
- Platform: LinkedIn + Substack
- Size: 1080x1350 for LinkedIn, 1200x630 for Substack hero
- Renderer: `scripts/visuals/infographic.py`
- Message: "A production eval system needs tasks, graders, CI gates, and regression history."
- Must stand alone: yes

## Deferred / Follow-On Visuals

| ID | Visual idea | Reason deferred |
|---|---|---|
| f01-editorial-cartoon-benchmark-theater | Newspaper-style cartoon about leaderboard confidence | Editorial cartoons are follow-on scope |
| f02-interactive-eval-dashboard | Interactive GitHub Pages dashboard | Interactive visuals are follow-on scope |
| f03-x-visual-thread | 4-card X/Twitter thread | X/Twitter is outside first implementation scope unless selected later |
