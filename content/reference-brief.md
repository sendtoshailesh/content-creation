---
title: Reference Brief — From Prompts to Loop Engineering (re-grounded, relevance-ranked)
description: Relevance-ranked source brief for the loop-engineering run. Sources are ordered by how authoritative they are for each claim, regardless of publisher; all vendors and independent writers are treated equally.
author: Shailesh Mishra
ms.date: 2026-06-24
ms.topic: reference
---

# Reference Brief — re-grounded under relevance-first source ranking

> **Why this brief was rebuilt (2026-06-24).** Sources are ranked by how directly and
> authoritatively each one supports the specific claim it grounds — **not** by who published it.
> For any load-bearing "here's what a harness/loop is" or "here's what I recommend" claim, the
> first citation is the best **primary** source available (whoever built/ran/shipped the thing),
> backed by independent **measurement** and expert **synthesis**. Microsoft, GitHub, Anthropic,
> OpenAI, ThoughtWorks, independent maintainers, and researchers are all candidates on the same
> footing. Every URL is verified by fetch before citing.
>
> The groupings below are organizational only (own work / docs / repos / writers) — they are not
> a precedence order, and no publisher gets a structural head start.

## Author's own inspectable work (first-person "this is what I do")

| Source | What it proves | Tag |
|---|---|---|
| This content pipeline's review-gate loop (`agents-and-skills/`, this repo) — plan → draft → rubber-duck review → fix → re-review, with a deterministic preflight + tiered critic as sensors and an iteration cap as the stop condition | A working, inspectable loop the author runs daily; the post is itself a loop-engineering artifact | T1 own |
| `github.com/sendtoshailesh` repos + contributions to `Azure/git-ape` (PRs, issues) | First-hand harness/loop building, not theory | T1 own |

## Product & platform primary sources (docs/engineering blogs) — VERIFIED

| Source | URL | What it grounds (verified) | Tag |
|---|---|---|---|
| **The Coding Harness Behind GitHub Copilot in VS Code** — Julia Kasper, Megan Rogge, Aaron Munger, May 15 2026 | https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode | **The spine.** Defines the **coding harness** = the bridge that turns model text into action (3 jobs: context assembly, tool exposure, tool execution). Defines the **agent loop** = "think → act → observe → think again." Vocabulary: **turn / round / run**. **Loop-control**: tool-call limit, cancellation checks, **stop hooks**. "**The harness is the product**" / "**the model is the engine, the harness is the car**." Per-model harness tuning (Claude → `replace_string_in_file`; GPT → `apply_patch`; Gemini needs tool-call reminders). **Evaluation**: VSC-Bench (40 runs, 8 model-effort configs; resolution rate vs token usage; xhigh past the effort sweet spot). Notes OpenAI **stopped reporting SWE-bench Verified**. | T2 Microsoft |
| **Build with agents, conversations, and responses in Foundry Agent Service** (runtime components) — ms.date 2026-04-10 | https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/runtime-components | The managed-service agent loop in production: **agent + conversation + response**; the model processes input + instructions, **calls tools**, appends items, you check status and retrieve. **Background mode** = poll `status` (queued/in_progress) until done = an explicit, bounded run loop. **Memory stores** carry state across turns. Tool-call item types (web_search_call, function_call, file_search_call). First-party proof that "the loop" is a real product primitive, not a metaphor. | T2 Microsoft |
| **What is Microsoft Foundry Agent Service?** (overview) | https://learn.microsoft.com/en-us/azure/foundry/agents/overview | Defines agents as model + instructions + tools as a governed, versioned asset; the platform framing for "engineer the loop, not the prompt." | T2 Microsoft |
| **Quickstart: Deploy your first hosted agent** | https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent | The "Start from" for Project 2 (build a loop on Foundry). | T2 Microsoft |
| **Foundry IQ: Build smarter agents faster with unified knowledge** — devblogs/foundry | https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/ | First-party signal that the platform is investing in the harness layer (knowledge/grounding around the model). | T2 Microsoft |

> The two load-bearing T2 URLs (VS Code harness blog, Foundry runtime-components) were
> fetched and verified on 2026-06-24 — quotes above are confirmed against the live pages.

## Repos you can build from — VERIFIED

| Source | URL | What it grounds (verified) | Tag |
|---|---|---|---|
| **Azure/git-ape** — "platform engineering framework for the agentic age," built on GitHub Copilot | https://github.com/Azure/git-ape | A real, public harness+loop: multi-agent **plan → generate → confirm/PR-review → deploy → post-deploy validation**, with **security + cost gates as sensors** and **CI/CD (git-ape-plan/deploy/destroy) via OIDC** as the bounded run. Headless mode = Copilot Coding Agent picks up an issue → branch → PR → validated deploy. 252 stars, MIT, v0.3.0. **Project 3 "Start from."** Author is a listed contributor. | T3 GitHub |
| **microsoft/hve-core** — "Hypervelocity Engineering prompt library for GitHub Copilot" | https://github.com/microsoft/hve-core | RPI (Research → Plan → Implement) workflow with **validated artifacts + quality gates + a CI validation pipeline** = harness/loop discipline as a shipped library. 1.2k stars, MIT. This workspace runs on it. Advanced "Start from" alternative. | T3 GitHub |
| **GitHub Copilot** (agent mode) | https://github.com/copilot | The everyday first-party loop the author uses (38 visits): the harness blog's loop, live in the editor. **Project 1 "Start from."** | T3 GitHub |
| **github/awesome-copilot** | https://github.com/github/awesome-copilot | Community-curated Copilot instructions/agents/skills — corroborates the harness-as-library pattern. | T3 GitHub |

## Independent measurement & expert synthesis

| Source | URL | Role (supporting evidence) | Tag |
|---|---|---|---|
| Simon Willison — "Designing agentic loops" (Sep 2025) | https://simonwillison.net/2025/Sep/30/designing-agentic-loops/ | Corroborates the loop-design framing + "distinct new skill"; four levers. Echoes the VS Code harness blog's loop. | T4 public |
| Simon Willison — "vibe engineering" (Oct 2025) | https://simonwillison.net/2025/Oct/7/vibe-engineering/ | Names the climb (vibe coding → engineering). | T4 public |
| Birgitta Böckeler — "Harness Engineering — first thoughts" (Feb 2026) | https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html | Corroborates "harness = everything except the model" / "guides and sensors." The VS Code blog is the first-party version of the same idea. | T4 public |
| Böckeler — "Context Engineering for Coding Agents" (Feb 2026) | https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html | Corroborates the context era. | T4 public |
| Kief Morris — "Humans and Agents in Software Engineering Loops" (Mar 2026) | https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html | Corroborates outside/in/on the loop + "fix the artefact vs. fix the loop." | T4 public |
| Anthropic — "Building Effective Agents" (Dec 2024) | https://www.anthropic.com/engineering/building-effective-agents | Corroborates evaluator-optimizer + stop condition. The Foundry runtime-components doc is the first-party managed equivalent. | T4 public |
| Stripe autonomous coding agents (via InfoQ, Mar 2026) | https://www.infoq.com/news/2026/03/stripe-autonomous-coding-agents/ | Corroborating production-scale data point (1,300+ PRs/week, $1T+). Third-party — cite with date, re-pull before budget use. | T4 public |
| SWE-bench Verified leaderboard | https://www.swebench.com/ | Corroborating benchmark trajectory (12.47% → 76.8%; $0.05–$0.96/task). **Note:** the VS Code harness blog itself flags benchmark limits and that OpenAI stopped reporting SWE-bench Verified — cite SWE-bench as a starting point, not proof. | T4 public |
| CircleCI Chunk Sidecars (via InfoQ, Jun 2026) | https://www.infoq.com/news/2026/06/circleci-chunk-sidecars/ | Corroborates "validation is the bottleneck" + inner-loop validation. | T4 public |
| InfoQ/Thoughtworks podcast — "From MCP and Vibe Coding to Harness Engineering" (Jun 2026) | https://www.infoq.com/podcasts/mcp-vibe-coding-harness-engineering/ | Corroborates the one-year arc; subsidy caveat. | T4 public |

## Source Map (best source per load-bearing claim)

| Claim in the post | Best source | Backed by |
|---|---|---|
| What a **harness** is (everything around the model; context + tools + execution) | T2 VS Code harness blog ("the coding harness… 3 responsibilities") | Böckeler "everything except the model" (T4) |
| What the **loop** is (think→act→observe→think again; turn/round/run) | T2 VS Code harness blog ("the agent loop") | Willison "runs tools in a loop" (T4) |
| **Stop conditions / loop-control** (you must bound the run) | T2 VS Code harness blog (tool-call limit, cancellation, stop hooks) + T2 Foundry runtime-components (background-mode polling, capped iterations) | Anthropic "maximum number of iterations" (T4) |
| **The harness — not the model — is the product** | T2 VS Code harness blog ("the harness is the product" / "engine vs. car"; per-model tuning) | — (this is the first-party thesis) |
| **Validation/evaluation is the constraint** | T2 VS Code harness blog (VSC-Bench; "evaluation keeps the harness honest"; OpenAI dropped SWE-bench) | CircleCI inner-loop validation (T4); SWE-bench trajectory (T4) |
| **The loop is a real product primitive** (not a metaphor) | T2 Foundry runtime-components (agent+conversation+response, tool calls, background runs, memory) | Anthropic evaluator-optimizer (T4) |
| **Art of the possible at scale** (a production harness+loop you can read) | T3 Azure/git-ape (plan→validate→deploy with gates + CI/OIDC) | Stripe Minions (T4) |
| **Build it yourself** (3 projects, equal tool options) | run a verify→correct loop in an agent (Copilot / Aider / Claude Code) → build the loop on a managed runtime (Foundry / Anthropic patterns) → platform-engineer with gates (git-ape / hve-core / mini-swe-agent) | — |

## Gaps / flags

- The VS Code harness blog is **April–May 2026** and is the best primary source for the harness +
  loop definitions because its authors built that harness — cite it first for those points on
  authority, not vendor. The independent writers (Willison, Böckeler, Morris) stay as synthesis.
- SWE-bench numbers: the harness blog itself cautions against over-trusting SWE-bench
  (contamination; OpenAI dropped it). Keep the trajectory as *illustration*, and ground the
  "evaluation matters" point with VSC-Bench (and CircleCI's inner-loop validation) instead.
- All "Tools (pick one)" repos for the practitioner projects are **verified live** (Azure/git-ape
  252★, microsoft/hve-core 1.2k★, github.com/copilot, Aider, mini-swe-agent, Claude Cookbooks).
