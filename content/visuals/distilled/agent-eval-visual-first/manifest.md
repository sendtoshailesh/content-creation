# Visual Pack Manifest: agent-eval-visual-first

Generated: 2026-06-09
Source map: `content/visual-opportunity-map.md`
Blog source: `content/agent-eval-visual-first-series.md`
Mode: mandatory visual-first pilot
Rendering policy: programmatic only

## Asset Inventory

| File | Dimensions | Platform | Visual Family | Source Opportunity |
|------|------------|----------|---------------|--------------------|
| `linkedin-card-01-hook.png` | 1080x1350 | LinkedIn | Social card pack | s01-linkedin-card-pack-gap |
| `linkedin-card-02-problem.png` | 1080x1350 | LinkedIn | Social card pack | s01-linkedin-card-pack-gap |
| `linkedin-card-03-taxonomy.png` | 1080x1350 | LinkedIn | Social card pack | s01-linkedin-card-pack-gap |
| `linkedin-card-04-framework.png` | 1080x1350 | LinkedIn | Social card pack | s01-linkedin-card-pack-gap |
| `linkedin-card-05-cta.png` | 1080x1350 | LinkedIn | Social card pack | s01-linkedin-card-pack-gap |
| `comic-sourdough-test.png` | 1080x1350 | Blog + LinkedIn | Comic/storyboard | v03-sourdough-test |
| `one-page-eval-system.png` | 1080x1350 | LinkedIn + Substack | Infographic/one-pager | s04-one-page-eval-system |
| `exhibit-01-benchmark-gap.png` | 1200x627 | Medium + LinkedIn Article | Executive exhibit | v01-benchmark-gap |
| `eval-ci-architecture.mmd` | Mermaid | Blog + Medium | Architecture/flow | s05-architecture-eval-ci |

## Redesigned Visual Concepts

| Asset | Redesigned concept |
|---|---|
| `exhibit-01-benchmark-gap.png` / `linkedin-card-01-hook.png` | Broken bridge / gauge benchmark gap: 74-78% capability signal contrasted with 35-50% production PR acceptance estimate |
| `linkedin-card-02-problem.png` | Annotated empty tool-log scene: polished agent response beside Tool calls: 0 |
| `comic-sourdough-test.png` | Stateful Sourdough storyboard: neutral prompt -> wrong recipe answer -> expected redirect -> CI block with 3/8 failed |
| `one-page-eval-system.png` / `linkedin-card-04-framework.png` | CI factory / eval gate one-pager: task suite -> behavior graders -> CI gate -> regression history |
| `eval-ci-architecture.mmd` | PR-level eval loop: change -> task suite -> graders -> regression gate -> debug trace -> rerun |

## Theme Assignment

| Asset | Theme |
|-------|-------|
| LinkedIn card pack | default |
| Comic/storyboard | ocean |
| One-pager | forest |
| Executive exhibit | midnight |
| Architecture diagram | Mermaid default with design-token-compatible colors |

## Render Command

Run from repository root:

```bash
python3 content/visuals/distilled/agent-eval-visual-first/render_visual_first.py
```

## Usage Notes

- LinkedIn: upload `linkedin-card-01` through `linkedin-card-05` as a carousel or multi-image post; canonical URL and benchmark/failure source URLs in first comment.
- Medium/Substack/LinkedIn Article: use `exhibit-01-benchmark-gap.png`, `comic-sourdough-test.png`, and `one-page-eval-system.png` as inline visuals.
- Blog: embed the benchmark exhibit, empty-tool-log scene, Sourdough storyboard, and one-page eval system; use the Mermaid flow from `eval-ci-architecture.mmd` where the CI loop appears.
- The metric claims referenced by this pack are: [SWE-bench Verified](https://www.swebench.com/) (coding-agent capability benchmark; not production-readiness proof), [Presenc May 2026 coding-agent benchmark snapshot](https://presenc.ai/research/coding-agent-benchmarks-2026) (**74-78% SWE-bench Verified**, **35-50% real-world PR acceptance**; vendor-reported, volatile point-in-time signal), [Sentrial May 2026 behavioral/silent failure analysis](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures) (**78% of analyzed failures were behavioral/silent rather than clean crashes/timeouts**; vendor-reported operational signal), and first-party/original implementation experience from [Part 1](https://sendtoshailesh.github.io/blog/agent-eval-part-1.html) and [Part 2](https://sendtoshailesh.github.io/blog/agent-eval-part-2.html) (**8 agents**, **38 tasks**, **14 eval suites/agents+skills**, **3 grader types**, **3 of 8 Sourdough Test failures**, **$3-8/run**, **200K-400K tokens**, **15-25 minutes**).
- Grounded review completed 2026-06-08; re-check Presenc/Sentrial if publishing after the May 2026 source window or after leaderboard changes.

## Render Validation

- Rendered: 2026-06-08
- PNG dimensions verified:
  - LinkedIn cards: 1080x1350
  - Comic/storyboard: 1080x1350
  - One-pager: 1080x1350
  - Executive exhibit: 1200x627
- PNG DPI metadata: approximately 320 DPI
