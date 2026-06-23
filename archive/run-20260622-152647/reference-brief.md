# Reference Brief — From Prompts to Harness Engineering

> Synthesized from the curated reference URLs in `pipeline-config.md` (fetched 2026-06-20).
> Source for the blog/social run on idea [11]. Every data point below is citable; keep the
> inline links when claims are used downstream.

## Core Thesis: The Maturity Arc

The field moved through four named stages in roughly 18 months, per Birgitta Böckeler
(Distinguished Engineer, Thoughtworks; Global Lead for AI-assisted Software Delivery) on the
InfoQ podcast *From MCP and Vibe Coding to Harness Engineering* (June 8, 2026):

1. **Autocomplete** (Copilot-style suggestions)
2. **Vibe coding** — the term was ~2 months old at QCon London 2025; ad-hoc, "fancier Stack
   Overflow copy-paste," Cursor-led
3. **Context engineering** — tuning what the model sees; term gained traction ~June 2025
4. **Harness engineering** — the current frontier (term emerging now)

The defining reframe: **"An agent is actually a model plus a harness."** A harness is
"everything except the model." Böckeler's sharpest line: **"So far, the developer was the
harness."** Harness engineering is the work of moving that scaffolding *out of the developer's
head and into engineered, version-controlled artifacts* so agents can self-correct and humans
can reduce supervision.
Source: https://www.infoq.com/podcasts/mcp-vibe-coding-harness-engineering/

### The two halves of a harness (Böckeler's framework)

- **Feed-forward** — what you give the agent *before* it generates: coding conventions,
  architecture context, specs, design systems as a knowledge source. Goal: raise the
  probability of a correct first generation.
- **Feedback** — what the agent gets *after* it generates, without a human in the loop: static
  code analysis, test-suite status, type/compiler errors, custom linters, language-server
  refactorings (rename-symbol vs. text diff), even a second AI doing adversarial review. Goal:
  let it self-correct.

She runs a **"heads-up display"** companion next to the coding agent that continuously shows
static analysis, test status, and coverage — an "agent-optimized summary" the agent can also
read. Triage example: "is it even worth me looking at this yet, or are 50% of the tests failing
and coverage dropped 10%?"

### Supervision = a risk assessment

Böckeler governs how much she supervises with **risk = probability × impact × detectability**:
- *Probability* AI gets it right/wrong (depends on context-engineering quality + agent
  experience)
- *Impact* / criticality (a spike vs. a critical workflow you're on-call for at 2 AM)
- *Detectability* — how easily you'd catch a mistake

### The OpenAI harness-first discipline

A team at OpenAI worked a codebase for 5–6 months where the main thing they build is the
harness: **"Every time something goes wrong, they improve the harness first before new code
gets written."** (Referenced in the podcast; see also openai.com/index/harness-engineering and
Anthropic's "agent swarm building a C compiler.")

### The gap: behavior harnesses barely exist

Most harness writing targets *maintainability / internal code quality* (static analysis,
fitness functions). There's very little for **behavior** — and the agent usually writes its own
tests, so "tests are green" is weak feedback. Open frontier: mutation testing resurgence, test
coverage as a feedback signal, architecture fitness functions.

## Building Block 1 — Custom Agents (prompts → reusable workflows)

GitHub, *From one-off prompts to workflows: How to use custom agents in GitHub Copilot CLI*
(Jacklyn Carroll, June 9, 2026):
- A **custom agent** is a Markdown file with YAML frontmatter in `.github/agents/`, ending
  `.agent.md`. It encodes role/expertise, allowed tools, and guardrails so "its behavior is
  consistent wherever it runs" — CLI → IDE → pull request.
- The pitch: turn "re-running the same commands, re-explaining context, translating logs" into
  "reusable, reviewable workflows." Because the profile is a repo file, it's **reviewable,
  versionable, shareable**.
- Worked examples in the post: `security-audit`, `iac-compliance`, `release-docs`,
  `incident-response` agents — each with a fixed output contract (PR-ready checklist, CHANGELOG
  entry, incident report template).
- Decision rule: off-the-shelf/partner agents for speed + tool-specific best practice; custom
  agents for "precision, continuity, and control."
Source: https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/

## Building Block 2 — Skills (lazy-loaded, progressive disclosure; the MCP successor)

From the InfoQ podcast + Angular case study:
- **Skills** are a third "context interface" (after built-in tools and MCP). The model first
  sees only a *list of skill names + descriptions*; it loads the full skill folder (markdown +
  docs + scripts) only when it judges the task relevant — **progressive disclosure / lazy
  loading of context**.
- Why teams moved MCP use cases to skills + CLIs + scripts: (1) far smaller context-window
  footprint than always-loaded MCP schemas; (2) if you already have a CLI (e.g., AWS CLI)
  installed, why run a separate MCP process — the agent can call the CLI directly. (MCP still
  wins where you want a permission bulwark.)
- **Angular shipped official Agent Skills** (`angular/skills`, June 12, 2026) using Anthropic's
  open Skills format. Two skills (`angular-developer`, `angular-new-app`) enforce v20 idioms
  (prefer `@if` over `*ngIf`, drop redundant `standalone: true`). Praised for an "autonomous
  verification loop" that forces `ng build` after edits and an orchestrator that loads only
  relevant reference files to limit token use. Devs: skills "feel more native because they live
  in the repo," are "versionable, diffable."
- The honest counterpoint (Hacker News): harness/skills approaches "pretend as if LLMs are
  strict and perfect rule followers… that's a fundamental cognitive lapse in how LLMs operate."
  Counter: "don't let the perfect be the enemy of the good."
Sources: https://www.infoq.com/podcasts/mcp-vibe-coding-harness-engineering/ ·
https://www.infoq.com/news/2026/06/angular-agent-skills/ ·
https://docs.github.com/en/copilot/concepts/agents/about-agent-skills

## Building Block 3 — The Harness Doing the Work (context + routing)

GitHub, *Getting more from each token* (Joe Binder, June 17–18, 2026):
- **Prompt caching** reuses model state for repeated prompt prefixes instead of recomputing.
- **Tool search / deferred tools**: load tool definitions on demand instead of sending every
  full tool schema every turn — matters more as agents gain MCP tools, terminal, file ops,
  search, product actions.
- **Auto model routing (HyDRA)**: a routing model weighs reasoning depth, code complexity,
  debugging difficulty, tool-orchestration needs + real-time model health. Operating points:
  **Peak exceeds Sonnet quality at 12.9% cost savings; Aggressive balances quality for 72.5%
  savings; Conservative ties OpenRouter Auto on resolution rate (70.8%) at 3.3× the savings.**
- **Cache-aware routing**: switch models only at cache boundaries (first turn, after
  compaction) because switching mid-conversation breaks the prompt-prefix cache and can cost
  more than it saves.
- Framing line: GitHub is "improving the Copilot harness so more of each session goes toward
  the task itself" — **the harness, not the model, doing the work.**
Source: https://github.blog/ai-and-ml/github-copilot/getting-more-from-each-token-how-copilot-improves-context-handling-and-model-routing/

## Building Block 4 — Orchestration Mechanics (delegation, parallelism, inner-loop validation)

- **Delegation isn't free** — GitHub, *How we made Copilot CLI more selective about delegation*
  (Pingping Lin & Yu Hu, June 12, 2026). Smarter subagent delegation, now at 100% of CLI
  traffic (v1.0.42+), measured in a production A/B test: **23% fewer tool failures per session,
  27% fewer search-tool failures, 18% fewer edit-tool failures, 5% lower user wait at P95, 3%
  at P75, no quality regression.** Principle: "start with the narrowest effective path,"
  treat subagents "as a parallelism tool, not a pause button."
  Source: https://github.blog/ai-and-ml/how-we-made-github-copilot-cli-more-selective-about-delegation/
- **Parallel agent workspaces** — git worktrees let multiple agents work checkouts of the same
  repo simultaneously without stepping on each other.
  Source: https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/
- **Inner-loop validation** — CircleCI Chunk Sidecars move CI-style checks *into the agent's
  loop* so it self-corrects before commit (a feedback mechanism in Böckeler's sense).
  Source: https://www.infoq.com/news/2026/06/circleci-chunk-sidecars/
- **A harness for every task** — orchestrating a team of agents on one job.
  Source: https://towardsdatascience.com/a-harness-for-every-task-putting-a-team-of-claudes-on-one-job/

## Supporting Data — Why Ad-Hoc Prompting Doesn't Scale

Towards Data Science, *How to Navigate the Shift from Prompt-Based Tools to Workflow-Driven AI*
(Manu R., June 4, 2026):
- **Context switching between tools can cut efficiency by up to 40%** (APA multitasking
  research), and it's worse for AI workflows because each tool needs different prompts/formats.
- The "AI paradox": practitioners stopped debating which model is best and started asking why
  the tools meant to simplify work add friction (re-prompting, reformatting, lost context).
- Token economics: unoptimized usage overuses expensive models and reprocesses the same data —
  "economical intelligence" = smaller models for simple tasks, big models only when needed.
Source: https://towardsdatascience.com/how-to-navigate-the-shift-from-prompt-based-tools-to-workflow-driven-ai/

## First-Party Angle — This Pipeline IS a Harness

This content run is itself produced by an engineered harness, which makes a credible,
demonstrable case study rather than a hypothetical:
- **~28 custom agents** in `.github/agents/` (e.g., `content-pipeline`, `content-strategist`,
  `blog-writer`, `visual-renderer`, `quality-reviewer`, `social-linkedin`) — each a versioned
  `.agent.md` with role, tools, guardrails. Exactly the GitHub "prompts → workflows" pattern.
- **Lazy-loaded skills** in `.github/skills/` (e.g., `creative-brief`, `content-scope-assessment`,
  `multi-dimensional-analysis`, `visual-rendering`) — loaded on demand, the skills/progressive-
  disclosure pattern Böckeler describes.
- **Scripted feedback** — `scripts/` (archive, visual renderers, validators) is the
  feed-forward + feedback layer; `pipeline-config.md` is the persistent state/harness contract.
- **The harness, not the model, doing the work**: the run inherits whatever model the VS Code
  picker selects; quality comes from the agent/skill/script scaffolding, not a model swap. This
  is the local proof of GitHub's "harness improvements" thesis.
- Architecture references: `agents-and-skills/automation-architecture.md`,
  `agents-and-skills/agent-definitions.md`, `agents-and-skills/content-strategy-pipeline.md`.

## Recommended Narrative Spine for the Blog

1. **Hook** — "So far, the developer was the harness." The skill that's now valuable isn't
   prompt-whispering; it's building the scaffolding around the model.
2. **The maturity curve** — autocomplete → vibe coding → context engineering → harness
   engineering (with the named-stage timeline as a visual).
3. **What a harness actually is** — model + feed-forward + feedback; the agent = model + harness
   equation.
4. **The four building blocks** — custom agents, lazy-loaded skills, context/routing, and
   orchestration mechanics, each with one hard number (delegation A/B results; HyDRA 72.5%;
   40% context-switch tax; deferred tools).
5. **First-party case study** — this very pipeline as a worked harness (agents + skills +
   scripts + config contract).
6. **The honest limits** — behavior harnesses barely exist; the HN critique that LLMs aren't
   perfect rule-followers; risk = probability × impact × detectability as the governance model.
7. **Build-your-own playbook** — start from a task you repeat, encode feed-forward, wire one
   feedback signal, version it, expand. "Improve the harness first."
