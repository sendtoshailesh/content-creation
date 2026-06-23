---
title: "Visual Opportunity Map - From Prompts to Harness Engineering"
description: "Visual planning contract for blog, LinkedIn, and Reel assets in the harness engineering content run"
author: Shailesh Mishra
ms.date: 2026-06-20
ms.topic: concept
keywords:
  - visual planning
  - harness engineering
  - infographic
  - LinkedIn visuals
estimated_reading_time: 8
---

<!-- markdownlint-disable MD013 -->

## Visual Opportunity Map

> Source artifacts: `content/harness-engineering-strategy.md`, `content/reference-brief.md`, `content/pipeline-config.md`  
> Visual mode: `programmatic`  
> Platforms in scope: Blog, LinkedIn, Reel/Short video  
> Platforms out of scope: X/Twitter, Reddit, YouTube

## Visual Strategy

The visual package should make one idea instantly clear: the model is not the whole agent. The harness around it carries the context, feedback, routing, and governance that make AI-native development repeatable.

The package avoids generic AI imagery. It uses deterministic diagrams, exhibits, and saveable cards that can be inspected, cited, and reused across the blog and LinkedIn.

## Blog Companion Visuals

| ID | Source section | Concept type | Audience persona | Visual family | Platform fit | Standalone potential | Required source data | Rendering approach | Priority | Status |
|----|----------------|--------------|------------------|---------------|--------------|----------------------|----------------------|--------------------|----------|--------|
| v01-harness-quote | H2 1. The hook | narrative | Practitioner | Infographic / one-pager | Blog, LinkedIn | high | Böckeler quote, InfoQ podcast URL | HTML/CSS + Chromium | P1 | rendered |
| v02-maturity-arc | H2 2. The maturity arc | timeline | Practitioner | Infographic / one-pager | Blog, LinkedIn | high | Autocomplete, vibe coding, context engineering, harness engineering dates | HTML/CSS + Chromium | P0 | rendered |
| v03-harness-anatomy | H2 3. What a harness is | architecture | Practitioner | Architecture / flow diagram | Blog, LinkedIn | high | Feed-forward and feedback definitions, InfoQ URL | HTML/CSS + Chromium | P0 | rendered |
| v04-building-blocks | H2 4. Four building blocks | framework | Practitioner, tech lead | Infographic / one-pager | Blog, LinkedIn | high | 23%, 27%, 18%, 72.5%, 70.8%, 3.3x | HTML/CSS + Chromium | P0 | rendered |
| v05-context-switch-cost | H2 5. Why ad-hoc prompting does not scale | data | AI team decision-maker | Executive exhibit | Blog, LinkedIn Article | medium | Up to 40% efficiency loss, TDS/APA source | HTML/CSS + Chromium | P1 | rendered |
| v06-pipeline-case-study | H2 6. First-party case study | architecture | Tech lead | Architecture / flow diagram | Blog, Reel | high | `.github/agents/`, `.github/skills/`, `scripts/`, `pipeline-config.md` | HTML/CSS + Chromium | P0 | rendered |
| v07-risk-limits | H2 7. The honest limits | governance | Tech lead, decision-maker | Executive exhibit | Blog, LinkedIn | medium | Risk = probability × impact × detectability; behavior-harness gap | HTML/CSS + Chromium | P1 | rendered |
| v08-playbook-checklist | H2 8. Build-your-own playbook | checklist | Practitioner | Infographic / one-pager | Blog, LinkedIn | high | Five-step playbook, OpenAI harness-first discipline | HTML/CSS + Chromium | P0 | rendered |

## Standalone Distribution Visuals

| ID | Source section | Concept type | Audience persona | Visual family | Platform fit | Standalone potential | Required source data | Rendering approach | Priority | Status |
|----|----------------|--------------|------------------|---------------|--------------|----------------------|----------------------|--------------------|----------|--------|
| s01-linkedin-card-pack | Whole post | narrative sequence | Practitioner, tech lead | LinkedIn social card pack | LinkedIn | high | Böckeler quote, 23%, 72.5%, 40%, repo harness proof | HTML/CSS + Chromium | P0 | planned |
| s02-reel-storyboard | Whole post | narrative | Practitioner | Comic explainer / storyboard | Reel planning | high | Maturity arc, repo folders, one CTA | SVG via Python | P1 | planned |

## Art Direction Briefs

### v02-maturity-arc

* Burning question: How did AI coding mature from autocomplete into harness engineering?
* Audience: AI-fluent IC engineers and tech leads
* Platform: Blog + LinkedIn
* Infographic type: Timeline infographic
* Visual metaphor: A four-stage rail that moves from single suggestion to engineered control loop
* Narrative arc: Assistance expands from completion to context to repeatable workflow
* Data/source inputs: InfoQ podcast, Jun 8 2026; QCon London 2025 timing; context engineering around Jun 2025
* Primary visual element: Horizontal milestone rail with four labeled stations
* State change or motion cue: Each station adds one new layer around the model
* Text budget: Hero title <= 8 words; each milestone <= 12 words
* Layout pattern: Milestone rail with compact date labels
* Icon/illustration plan: Cursor, prompt bubble, context folder, harness loop
* Source line: Source: InfoQ, "From MCP and Vibe Coding to Harness Engineering", Jun 8 2026
* Failure modes to avoid: Dense chronology, decorative icons without progression, unsupported exact dates
* Visual-reviewer acceptance criteria: Reader can name the four stages in order in 3 seconds on mobile

### v03-harness-anatomy

* Burning question: What parts make an AI agent more than a model?
* Audience: Practitioners
* Platform: Blog + LinkedIn
* Infographic type: Informational architecture diagram
* Visual metaphor: Model core wrapped by two active rails: feed-forward into the model and feedback back into the harness
* Narrative arc: Context improves first generation; feedback improves correction without waiting for a human
* Data/source inputs: Böckeler definition; feed-forward and feedback descriptions from InfoQ podcast
* Primary visual element: Center model node with two colored loops
* State change or motion cue: Input enters as conventions/specs, output returns through tests/types/static analysis
* Text budget: Title <= 7 words; node labels <= 4 words; callouts <= 14 words
* Layout pattern: Hub-and-loop system diagram
* Icon/illustration plan: Model core, knowledge stack, compiler/test gauges, review loop
* Source line: Source: InfoQ, Jun 8 2026
* Failure modes to avoid: Confusing feed-forward with feedback, too many tool logos, unreadable arrows
* Visual-reviewer acceptance criteria: Feed-forward and feedback are visually distinct and readable without the blog text

### v04-building-blocks

* Burning question: What should a team actually build around the model?
* Audience: Practitioners and tech leads
* Platform: Blog + LinkedIn
* Infographic type: Framework one-pager
* Visual metaphor: Four structural beams around a central model: agents, skills, routing, orchestration
* Narrative arc: Prompt habit becomes engineered system through reusable workflows, lazy context, routing, and validation
* Data/source inputs: GitHub custom agents post; Angular skills post; HyDRA routing post; delegation A/B post
* Primary visual element: Four-beam frame around the model
* State change or motion cue: Each beam adds one measurable capability
* Text budget: Title <= 9 words; each beam <= 16 words; one metric badge per beam
* Layout pattern: Framed system, not a plain four-card grid
* Icon/illustration plan: File, skill drawer, router, subagent loop
* Source line: Sources: GitHub Blog Jun 9, Jun 12, Jun 17 2026; InfoQ Angular skills Jun 12 2026
* Failure modes to avoid: Text-heavy cards, metric crowding, missing source line
* Visual-reviewer acceptance criteria: Each building block has one metric or named source and the whole frame reads as one harness

### v06-pipeline-case-study

* Burning question: What does a real harness look like in this repository?
* Audience: Tech leads and practitioners
* Platform: Blog + Reel planning
* Infographic type: Architecture / flow diagram
* Visual metaphor: Content pipeline control room: config contract routes work to agents, skills, scripts, and review gates
* Narrative arc: The model is interchangeable; the harness determines the run sequence and quality gates
* Data/source inputs: `agents-and-skills/automation-architecture.md`, `agents-and-skills/content-strategy-pipeline.md`, local repo structure
* Primary visual element: Config node feeding agents, skills, scripts, and publishing/review outputs
* State change or motion cue: Topic enters; reference brief, strategy, blog, visuals, LinkedIn, and Reel exit through gates
* Text budget: Title <= 8 words; node labels <= 5 words; gate labels <= 3 words
* Layout pattern: Directed flow with control node and review gates
* Icon/illustration plan: Config document, agent group, skill shelf, script gear, gate checkmarks
* Source line: Source: this repository, current run, 2026-06-20
* Failure modes to avoid: Overstating automation, hiding pause gates, unreadable repo filenames
* Visual-reviewer acceptance criteria: A reader can identify `pipeline-config.md` as the contract and understand why this is a harness

### v08-playbook-checklist

* Burning question: What can I ship this week to start harness engineering?
* Audience: Practitioners
* Platform: Blog + LinkedIn
* Infographic type: Checklist infographic
* Visual metaphor: Five-step workbench from repeated task to reviewed harness
* Narrative arc: A vague repeated task becomes a versioned agent with one feedback signal
* Data/source inputs: OpenAI harness-first discipline from InfoQ podcast; playbook from strategy
* Primary visual element: Step ladder with a feedback loop returning from breakage to harness improvement
* State change or motion cue: Step 5 loops back to Step 2 when something breaks
* Text budget: Title <= 8 words; each step <= 10 words
* Layout pattern: Step ladder + loopback arrow
* Icon/illustration plan: Repeat task, agent file, test signal, code review, improve harness
* Source line: Source: InfoQ, Jun 8 2026; practitioner playbook from this run
* Failure modes to avoid: Generic productivity checklist, no loopback, vague verbs
* Visual-reviewer acceptance criteria: The CTA is unmistakable: encode one repeated task and wire one feedback signal

### s01-linkedin-card-pack

* Burning question: Why should a busy engineer save and share this idea?
* Audience: Practitioners and tech leads
* Platform: LinkedIn
* Infographic type: LinkedIn social card pack
* Visual metaphor: Seven-card mini-argument from quote to playbook
* Narrative arc: You were the harness; now make the harness explicit
* Data/source inputs: Böckeler quote, 23% fewer tool failures, 72.5% savings, 40% context-switch tax, repo harness proof
* Primary visual element: Card sequence with one idea per card
* State change or motion cue: Cards progress from pain to framework to proof to CTA
* Text budget: Card title <= 8 words; body <= 22 words; source footnote <= 10 words
* Layout pattern: Mixed sequence: quote, timeline, frame, stat exhibit, repo map, risk card, checklist
* Icon/illustration plan: Same visual language as blog assets, cropped for 1080x1350
* Source line: Per-card source footer where metrics appear
* Failure modes to avoid: Repeating the blog verbatim, dense paragraphs, identical card layouts
* Visual-reviewer acceptance criteria: Each card stands alone and the whole pack drives to one CTA

## Rendering Handoff

### Required P0 assets before blog draft review

* `v02-maturity-arc`: 1600x900 SVG/PNG, timeline infographic, blog companion
* `v03-harness-anatomy`: 1600x900 SVG/PNG, architecture diagram, blog companion
* `v04-building-blocks`: 1600x900 SVG/PNG, framework one-pager, blog companion + LinkedIn crop candidate
* `v06-pipeline-case-study`: 1600x900 SVG/PNG, architecture map, blog companion + Reel screen cue
* `v08-playbook-checklist`: 1600x900 SVG/PNG, checklist infographic, blog close + LinkedIn

### P1 assets after blog text stabilizes

* `v01-harness-quote`: quote card for blog opener and LinkedIn crop
* `v05-context-switch-cost`: executive exhibit with 40% efficiency-loss callout
* `v07-risk-limits`: risk formula exhibit for honest-limits section
* `s01-linkedin-card-pack`: 7-card LinkedIn carousel after blog approval
* `s02-reel-storyboard`: storyboard after blog approval

## Layout Diversity Matrix

| Asset | Layout pattern | Avoids repeating |
|-------|----------------|------------------|
| v02-maturity-arc | Timeline rail | Card grid |
| v03-harness-anatomy | Hub-and-loop | Timeline |
| v04-building-blocks | Structural frame | Plain four-card board |
| v05-context-switch-cost | Hero-number exhibit | Framework diagram |
| v06-pipeline-case-study | Directed flow map | Hub-and-loop |
| v07-risk-limits | Formula + gauge | Timeline |
| v08-playbook-checklist | Step ladder + loopback | Plain checklist |
| s01-linkedin-card-pack | Mixed narrative sequence | Identical slide templates |

## Strategy Markers To Preserve

The strategy already includes `\[VISUAL: ...]` markers for all blog companion P0/P1 assets. Blog writing should preserve or refine these markers but should not replace them with final image links until rendered assets exist.
