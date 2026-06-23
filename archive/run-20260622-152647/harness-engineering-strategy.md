---
title: Content Strategy - From Prompts to Harness Engineering
description: Strategy, outline, scope assessment, and dimension analysis for the harness engineering content run
author: Shailesh Mishra
ms.date: 2026-06-20
ms.topic: concept
keywords:
  - harness engineering
  - AI-native development
  - workflow engineering
  - custom agents
estimated_reading_time: 9
---

## Content Strategy

> Companion to `content/creative-brief.md`. Source data: `content/reference-brief.md`,
> idea-queue [11]. Created 2026-06-20.

## Working title options

1. **From Prompts to Harness Engineering: The Workflow Shift in AI-Native Development**
  *(primary, matches idea-queue [11], strong SEO on the emerging term)*
2. **So Far, the Developer Was the Harness** *(opinion hook, Böckeler's line)*
3. **Stop Writing Better Prompts. Start Engineering the Harness.** *(provocation)*
4. **The Maturity Arc of AI Coding: Autocomplete → Vibe Coding → Context → Harness**
5. **An Agent Is a Model Plus a Harness — Here's How to Build the Harness**

**Recommended:** Title 1 for the blog H1; Title 2 as the LinkedIn/Reel hook.

## One-sentence thesis

The durable skill in AI-native development has shifted from writing better prompts to
engineering the version-controlled harness around the model, feed-forward context plus
automated feedback, because the harness, not the model, is what delivers reliability, lower
cost, and reduced supervision.

## Audience persona (primary)

AI-fluent IC engineers and tech leads who already run Copilot / Claude Code / Cursor daily,
are past the novelty phase, and are frustrated by re-explaining context, inconsistent agent
behavior, and unexplained token spend. They want engineered, repeatable workflows and a
standard their team can review. Secondary: engineering managers reading for economics
(40% context-switch tax; routing savings) and governance.

## Content angle & differentiator

- A practitioner's field guide to the named maturity arc, with the harness broken
  into four inspectable building blocks, each anchored by one hard number.
- The case study is *this very pipeline*, a real, runnable harness
  (~28 custom `.agent.md` agents, lazy-loaded skills, scripts, `pipeline-config.md` as the
  contract). Most coverage is theoretical; this post shows a working harness producing the
  post you're reading.

## Tone & voice

First-person practitioner, conversational, data-driven; lead with problems/insights; honest
about limits; no corporate/hype framing.

---

## Single-post vs. series recommendation

**Recommendation: ship as a single ~3,000-word post.** A 2-part series is *defensible* but
not warranted yet.

**Reasoning:**
- The piece has a single through-line (prompts to harness) and
  one reader job-to-be-done (reframe + first step). That fits one sitting.
- Four building blocks are *facets of one concept*, not four independent topics. Consolidating
  them is the point, not a burden.
- "Encode one repeated task as a versioned agent + one feedback signal" is
  a single action; splitting would fragment it.
- The visual count fits: ~5 deterministic visuals, under the 6-visual single-post ceiling.
- The reframe is highest-impact when whole. Splitting the maturity arc from the building
  blocks would bury the payoff ("the harness, not the model, does the work").

**Natural split point if a series is later required:** Split after the "Anatomy of a harness"
section.
- **Part 1 - The Reframe:** maturity arc + what a harness is (model + feed-forward + feedback)
  + risk = probability × impact × detectability + the 40% context-switch tax. Job: change the
  mental model. CTA: audit where *you* are the harness today.
- **Part 2 - Build Your Own Harness:** the four building blocks (custom agents, skills,
  context/routing, orchestration) + first-party case study + honest limits + playbook. Job:
  build it. CTA: ship one versioned agent.

Trigger to escalate to a series: if the building-block sections each need >500 words of
how-to with code, total pushes past ~4,500 words / 7+ visuals — then split at the point above.
Cadence: 4–5 days between parts.

---

## Word-count target

~3,000 words (single post). If escalated to a series: Part 1 ~1,600, Part 2 ~2,000.

## Section-by-section outline

### H1 - From Prompts to Harness Engineering: The Workflow Shift in AI-Native Development

### H2 1. The hook: "So far, the developer was the harness" `~250 words`
- Open on the daily friction: re-explaining context, re-prompting, inconsistent results.
- Land Böckeler's reframe: **"an agent is a model plus a harness"; "so far, the developer was
  the harness"** (InfoQ *From MCP and Vibe Coding to Harness Engineering*, Jun 8 2026).
- Thesis statement.
- **Data carried:** Böckeler quote + InfoQ podcast source.
- `[VISUAL: pull-quote card, "So far, the developer was the harness."]`
- **Distribution tag:** LinkedIn hook; Reel opening line.

### H2 2. The maturity arc: how we got here `~450 words`
- Four named stages: **autocomplete to vibe coding to context engineering to harness
  engineering**. "Vibe coding" was ~2 months old at QCon London 2025; "context engineering"
  gained traction ~June 2025; "harness engineering" is emerging now.
- Why each stage hit a ceiling (ad-hoc, "fancier Stack Overflow copy-paste," Cursor-led).
- **Data carried:** the four-stage timeline + approximate dates (InfoQ podcast).
- `[VISUAL: horizontal timeline of the four stages with dates]`
- **Distribution tag:** Reel middle (screen-cue the timeline); LinkedIn carousel seed.

### H2 3. What a harness actually is `~450 words`
- Definition: harness = "everything except the model." **Agent = model + harness.**
- **Feed-forward** (conventions, architecture context, specs, design system as knowledge
  source — raise P(correct first generation)) vs. **feedback** (static analysis, test status,
  type/compiler errors, custom linters, language-server refactorings, adversarial AI review,
  self-correct without a human in the loop).
- The **"heads-up display"** companion: continuous static analysis, test status, coverage as
  an agent-readable summary; triage line "are 50% of tests failing and coverage dropped 10%?"
- **Data carried:** feed-forward/feedback framework + HUD example (InfoQ podcast).
- `[VISUAL: anatomy diagram, model in center, feed-forward in, feedback loop back]`
- **Distribution tag:** LinkedIn body (the two-halves explainer).

### H2 4. The four building blocks of a harness `~900 words`

#### H3 4.1 Custom agents: prompts become reusable workflows `~220 words`
- A custom agent = Markdown + YAML frontmatter in `.github/agents/`, `.agent.md`; encodes
  role, allowed tools, guardrails; consistent CLI → IDE → PR. Reviewable, versionable,
  shareable. Examples: `security-audit`, `iac-compliance`, `release-docs`, `incident-response`.
- **Data carried:** GitHub *From one-off prompts to workflows* (Carroll, Jun 9 2026).

#### H3 4.2 Skills: lazy-loaded, progressive disclosure (the MCP successor) `~230 words`
- Model first sees only skill *names + descriptions*; loads the full folder (markdown + docs +
  scripts) only when relevant. Smaller context footprint than
  always-loaded MCP schemas; call existing CLIs directly. **Angular shipped official Agent
  Skills** (`angular/skills`, Jun 12 2026): `angular-developer` + `angular-new-app` enforce v20
  idioms (`@if` over `*ngIf`), with an autonomous verification loop forcing `ng build`.
- **Data carried:** Angular skills case study (InfoQ, Jun 12 2026) + GitHub agent-skills docs.

#### H3 4.3 The harness doing the work: context & routing `~230 words`
- **Prompt caching** (reuse prefix state), **deferred tools / tool search** (load tool
  schemas on demand), **HyDRA auto routing**: **Peak exceeds Sonnet quality at 12.9% savings;
  Aggressive balances quality at 72.5% savings; Conservative ties OpenRouter Auto on
  resolution rate (70.8%) at 3.3× the savings.** Cache-aware routing switches models only at
  cache boundaries.
- **Data carried:** GitHub *Getting more from each token* (Binder, Jun 17 2026).

#### H3 4.4 Orchestration mechanics: delegation, parallelism, inner-loop validation `~220 words`
- Delegation isn't free: production A/B at 100% CLI traffic — **23% fewer tool failures, 27%
  fewer search failures, 18% fewer edit failures, 5% lower P95 wait, no quality regression.**
  "Start with the narrowest effective path; subagents are a parallelism tool, not a pause
  button." Git worktrees for parallel agent workspaces; CircleCI Chunk Sidecars move CI into
  the agent loop.
- **Data carried:** GitHub delegation post (Lin & Hu, Jun 12 2026) + worktrees + CircleCI.
- `[VISUAL: four-panel building-blocks board, each panel tagged with its one hard number]`
- **Distribution tag:** LinkedIn (the four numbers as a list); Reel (rapid-fire stat cuts).

### H2 5. Why ad-hoc prompting doesn't scale `~250 words`
- **Context switching between tools can cut efficiency by up to 40%** (APA multitasking
  research via TDS), worse for AI because each tool needs different prompts/formats. The "AI
  paradox": tools meant to simplify add friction. "Economical intelligence" means small models for
  simple tasks, big models only when needed.
- **Data carried:** TDS *How to Navigate the Shift…* (Manu R., Jun 4 2026) + APA 40%.
- `[VISUAL: bar/callout, "up to 40% efficiency lost to context switching"]`
- **Distribution tag:** manager-angle LinkedIn line; Reel stat.

### H2 6. First-party case study: this pipeline is a harness `~400 words`
- The post you're reading was produced by an engineered harness: **~28 custom `.agent.md`
  agents** in `.github/agents/` (content-pipeline, content-strategist, blog-writer,
  visual-renderer, quality-reviewer, social-linkedin), **lazy-loaded skills** in
  `.github/skills/` (creative-brief, content-scope-assessment, multi-dimensional-analysis,
  visual-rendering), **scripted feed-forward/feedback** in `scripts/`, and
  `pipeline-config.md` as the persistent harness contract. The run inherits whatever model the
  VS Code picker selects — quality comes from the scaffolding, not a model swap. Local proof of
  "the harness, not the model, doing the work."
- **Data carried:** repository architecture (automation-architecture.md,
  content-strategy-pipeline.md).
- `[VISUAL: architecture map, agents + skills + scripts + config contract]`
- **Distribution tag:** Reel core (live screen-record of the repo folders); LinkedIn proof.

### H2 7. The honest limits `~300 words`
- Most harness work targets maintainability/internal quality (static analysis, fitness
  functions); **behavior harnesses barely exist**. The agent writes its own tests, so "tests
  green" is weak feedback (open frontier: mutation testing, coverage-as-signal, architecture
  fitness functions). The HN critique: harness/skills approaches "pretend LLMs are strict,
  perfect rule followers… a fundamental cognitive lapse." Counter: "don't let the perfect be
  the enemy of the good." Governance model: **risk = probability × impact × detectability.**
- **Data carried:** InfoQ podcast (behavior-harness gap) + HN critique + risk formula.
- `[VISUAL: risk-formula card, risk = probability × impact × detectability]`
- **Distribution tag:** LinkedIn credibility line (showing the limits earns trust).

### H2 8. Build-your-own playbook `~300 words`
- Five steps: (1) start from a task you repeat; (2) encode the feed-forward (conventions,
  context, spec) as a versioned `.agent.md`; (3) wire one feedback signal (tests/linter/types/
  language-server); (4) version + review it like code; (5) expand, and "improve the harness
  first" every time something breaks (the OpenAI 5–6-month harness-first discipline).
- **Data carried:** OpenAI "improve the harness first before new code" (InfoQ podcast).
- `[VISUAL: 5-step playbook checklist]`
- **Distribution tag:** → the single CTA echoed on LinkedIn + Reel close.

**Outline section count:** 8 H2 sections (with 4 H3 subsections under §4) + H1.

---

## SEO keyword seeds

- Primary: *harness engineering*, *AI-native development*, *from prompts to workflows*
- Secondary: *custom agents GitHub Copilot*, *agent skills lazy loading*, *context
  engineering vs harness engineering*, *AI coding maturity model*
- Long-tail: *what is harness engineering AI*, *model plus a harness*, *build custom agent
  .agent.md*, *progressive disclosure skills MCP successor*, *reduce AI agent token cost
  routing*
- Entities to name for topical authority: Birgitta Böckeler, Thoughtworks, GitHub Copilot
  CLI, HyDRA routing, Angular Agent Skills, MCP.

## Distribution plan

- **Order:** Blog first (canonical, all data + sources) to LinkedIn to Reel.
- **LinkedIn (always-on):** Lead with **"So far, the developer was the harness."** Body =
  the two halves (feed-forward/feedback) + the four numbers (23% fewer tool failures, 72.5%
  routing savings, 40% context-switch tax, ~28 agents in this repo). Close on the single CTA.
  Unicode bold/italic formatting; link to blog. Practitioner voice.
- **Reel/Short (60–90s):** Hook line (0–5s) = "So far, *you* were the harness." Screen-record
  cues: the maturity-arc timeline to this repo's `.github/agents/` + `.github/skills/` trees to
  a `.agent.md` frontmatter to the four stat cards. Voiceover narrates the arc and the CTA.
  End card = "Engineer the harness, not the prompt."
- **Cross-link:** LinkedIn and Reel both point to the blog as the canonical deep-dive; both
  carry the *identical* single CTA so the funnel stays coherent.

## Scope Assessment

> Assessed: 2026-06-20 | Skill: `content-scope-assessment`

**Assessment score**: 5/14 (dimension analysis omitted during initial scope pass)
**Single-post feasibility**: Pass. The topic has one dominant reader job, fits in ~3,000 words, uses one narrative arc, stays at 6 or fewer visuals, and carries one CTA.
**Required series gate**: No conditions met strongly enough to require a series.
**Recommendation**: Single comprehensive post.
**Part-count rationale**: One post is better than two because the maturity arc and building blocks reinforce one reframe. A 2-part series remains the fallback only if the draft expands beyond 4,500 words or needs 7+ visuals.

### Assessment Signals

| Signal | Evidence | Score |
|--------|----------|-------|
| Pillar count | Four building blocks, each a facet of one harness model rather than independent deep dives | 1 |
| Data density | Roughly 12 to 15 unique source-backed points across InfoQ, GitHub, Angular, and TDS | 1 |
| Audience breadth | Three personas, but the IC and tech-lead path dominates | 1 |
| Technical depth | Conceptual field guide with one playbook, not code-heavy implementation | 1 |
| Word count pressure | Proper coverage fits near 3,000 words | 0 |
| Visual complexity | Five to six useful visuals | 1 |
| Distribution fragmentation | LinkedIn and Reel can use one hook and one CTA | 0 |

## Dimension Analysis

> Assessed: 2026-06-20 | Skill: `multi-dimensional-analysis`

### Persona Dimensions

| Persona | Responsibility Context | Application Angle | Depth | Preferred Channels |
|---------|------------------------|-------------------|-------|--------------------|
| AI-fluent IC engineer | Uses Copilot, Claude Code, Cursor, or similar assistants daily | Turn repeated AI tasks into versioned agents and one feedback loop | deep | Blog, LinkedIn, Reel |
| Tech lead or staff engineer | Owns team practices, code quality, reviewability, and shared standards | Standardize prompt work as reviewable workflow artifacts | moderate | Blog, LinkedIn |
| AI team decision-maker | Owns adoption governance, tool spend, and supervision risk | Evaluate harness engineering as a cost, reliability, and governance pattern | overview | LinkedIn, blog skim |

**Persona count**: 3

### Best Practice Dimensions

#### Technology Practices

| Practice | Complexity | Impact | Standalone Value |
|----------|------------|--------|------------------|
| Versioned custom agents in `.github/agents/` | medium | high | yes |
| Lazy-loaded skills and progressive disclosure | medium | high | yes |
| Feed-forward context contracts | low | high | yes |
| Feedback loops from tests, linters, types, and language servers | medium | high | yes |
| Model routing, prompt caching, and deferred tool loading | high | high | yes |

#### Governance Practices

| Practice | Complexity | Impact | Standalone Value |
|----------|------------|--------|------------------|
| Review prompts and agents like code | low | high | yes |
| Supervise AI work through risk = probability × impact × detectability | medium | high | yes |
| Improve the harness before writing more code | medium | high | yes |

**Practice count**: 5 technology + 3 governance = 8 total

### Azure WAF Pillar Dimensions

| Pillar | Relevance | Coverage Depth | Content Angle |
|--------|-----------|----------------|---------------|
| Cost Optimization | primary | moderate | HyDRA routing, prompt caching, and deferred tools reduce unnecessary spend. |
| Operational Excellence | primary | deep | Custom agents, skills, scripts, and config contracts make AI workflows repeatable and reviewable. |
| Performance Efficiency | secondary | mention | Delegation and routing reduce tool failures and wait time without lowering quality. |
| Reliability | secondary | moderate | Feedback loops and risk-aware supervision reduce unchecked agent drift. |
| Security | tangential | mention | Reviewable agents and explicit tool boundaries create a surface for governance, but security is not the core focus. |

**Primary pillars**: 2 | **Secondary pillars**: 2

### Dimension Breadth Score

| Signal | Evidence | Score (0-2) |
|--------|----------|-------------|
| Persona count | 3 personas identified | 2 |
| Practice count | 8 practices (5 technology + 3 governance) | 2 |
| WAF pillar spread | 2 primary + 2 secondary pillars | 1 |

**Dimension breadth score**: 2/2

### Dimension × Series Alignment

Series split is not recommended. If the draft exceeds the single-post ceiling, split by lifecycle stage: Part 1 for the IC reframe and Part 2 for tech-lead implementation and governance.

| Part | Primary Persona | Key Practices | WAF Pillar Focus |
|------|-----------------|---------------|------------------|
| 1 | AI-fluent IC engineer | Feed-forward contracts, feedback loops, custom agents | Operational Excellence, Reliability |
| 2 | Tech lead / AI team decision-maker | Lazy-loaded skills, routing economics, risk supervision | Cost Optimization, Operational Excellence |

### Dimension × Platform Matrix

| Platform | Primary Persona | Angle | Key Practices to Highlight |
|----------|-----------------|-------|----------------------------|
| Blog | AI-fluent IC engineer | Field guide from prompt habit to harness engineering | Custom agents, skills, feedback loops, routing |
| LinkedIn | Tech lead | "So far, the developer was the harness" plus four numbers | Reviewable agents, 23% fewer tool failures, 72.5% routing savings |
| Reel/Short | AI-fluent IC engineer | Show the repo harness live in 60 to 90 seconds | `.github/agents/`, `.github/skills/`, pipeline config, one CTA |
