# Trend Research: From Prompts to Harness Engineering to Loop Engineering

> Phase 0 — trend research + reference discovery. Topic: "From Prompts to Harness Engineering to Loop Engineering — The Workflow Shift in AI-Native Development." Audience: working developers and AI-native practitioners. Treats the four eras as one unified arc.
>
> Research date: 2026-06-22. All URLs below were fetched and verified during this run unless flagged otherwise.

---

## 1. Synthesis — What "Loop Engineering" Is and Where It Sits in the Arc

### The four-era arc (one continuous thread)

The progression is not four separate trends — it is one moving target: **as the model handles more, the human's leverage point moves up a level.** Each era names where the developer's effort concentrates once the previous concern gets automated.

| Era | What you engineer | What the human is doing | Representative moment |
|-----|-------------------|-------------------------|------------------------|
| **Prompt engineering** | The wording of a single request | Crafting the input to one LLM call | ChatGPT / Copilot autocomplete (2022–2024) |
| **Context engineering** | What the model sees — conventions, architecture, skills, lazy-loaded files | Curating the information window | Term gained traction ~June 2025 (per Böckeler) |
| **Harness engineering** | Everything around the model — skills, CLIs, scripts, MCP, linters, tests, guardrails | Building the rig the agent runs inside | OpenAI "Harness engineering" + Böckeler memo (Feb 2026) |
| **Loop engineering** | The control loop itself — plan → act → observe → verify → correct, with stop conditions | Designing and governing the iteration cycle | Simon Willison "Designing agentic loops" (Sep 2025); Kief Morris "Humans and Agents in Software Engineering Loops" (Mar 2026) |

The arc is explicitly framed by practitioners themselves. The InfoQ/Thoughtworks podcast is literally titled *"From MCP and Vibe Coding to Harness Engineering: How AI Native Engineering Evolved in One Year"* (Jun 2026). Simon Willison tracks the same move from "vibe coding" → "vibe engineering" → (his Feb 2026 update) "agentic engineering."

### What loop engineering actually means

**Definition (synthesized from sources):** Loop engineering is the discipline of designing and governing the agent's *iteration cycle* — the repeating plan → act → observe → verify → correct loop — so the agent can brute-force its way to a correct solution and **self-correct without a human in the inner loop.** The core unit of work is no longer the prompt or even the toolset; it's the loop: its goal, its tools, its feedback signal, its stop conditions, and who (human or agent) sits at which level.

Simon Willison's working definition of an agent is "[something that] runs tools in a loop to achieve a goal," and his key claim is that **"designing agentic loops" is a distinct, new skill** (he notes Claude Code only shipped Feb 2025, so this is genuinely fresh). The art is reducing a problem "to a clear goal and a set of tools that can iterate towards that goal" — then the agent can "brute force its way to an effective solution."

**Inner loop vs. outer loop (Kief Morris's model, the clearest articulation):**
- The **"why loop"** iterates over *idea → working software* — humans own this because we're the ones who want the outcome.
- The **"how loop"** iterates over *interim artefacts (specs, code, tests)* — and it contains *multiple nested loops*: an **outer** loop on a feature, a **middle** loop on stories, an **inner** loop that generates and tests code.
- Four human postures emerge: **outside the loop** (vibe coding — human owns only the why), **in the loop** (human gatekeeps every line — becomes the bottleneck), **on the loop** (human builds/tunes the how-loop rather than inspecting output — this is where harness engineering lives), and the **agentic flywheel** (human directs agents to improve the loop itself).

The pivotal distinction: when you're *in* the loop and dislike the output, you **fix the artefact**; when you're *on* the loop, you **change the harness/loop that produced it.** That shift from "fix the output" to "fix the loop that produces the output" *is* loop engineering.

### How loop engineering differs from harness engineering

These are adjacent and overlapping, but the sources draw a real line:

- **Harness engineering = the rig (nouns).** Böckeler defines a harness as "everything except the model" — the feed-forward context (coding conventions, architecture docs, skills, CLIs, MCP, language servers) plus the feedback sensors (static analysis, test results, type errors, custom linters). Her later framing: harnesses are **"guides and sensors,"** which may be computational or inferential. It's the equipment the agent operates inside.
- **Loop engineering = the cycle (verbs).** It's what *uses* the harness: the control flow that decides act → observe → verify → retry → stop. It governs the *evaluator-optimizer* cycle (Anthropic's term for "one LLM generates while another evaluates and gives feedback in a loop"), the stop conditions ("maximum number of iterations to maintain control" — Anthropic), the verification gates, and the reward/feedback signal that tells the agent whether it's done.

A clean mental model: **the harness is the gym and the equipment; the loop is the rep-scheme and the coach deciding when you're done.** Harness engineering asks *"what tools and sensors does the agent have?"* Loop engineering asks *"how does the agent iterate against those sensors, and what makes it stop?"* In practice, mature setups (Stripe's "blueprints," Anthropic's "Dynamic Workflows") are *both* — a harness plus an explicit, code-defined loop with verification and stop logic.

### Why this matters *now* (timing)

The shift is being forced by an economics inversion that multiple 2026 sources independently report: **code generation is no longer the bottleneck — validation is.** CircleCI's internal data shows feature-branch activity surging while production deployments lag. When an agent generates code faster than CI can validate it, "by the time conventional CI discovers an issue, the AI agent has already moved on, losing valuable context." So the industry is pulling verification *into the inner loop* (CircleCI Chunk Sidecars, Dropbox Nova, Claude Code's iterative validation). That is loop engineering becoming a product category, not just a blog-post idea.

---

## 2. Ranked Source List (verified, grouped by theme)

### Theme A — Loop engineering core (definition & the skill)

1. **Simon Willison — "Designing agentic loops"** (30 Sep 2025) — https://simonwillison.net/2025/Sep/30/designing-agentic-loops/ — *The* origin point for naming loop design as a discrete skill: "runs tools in a loop to achieve a goal," YOLO mode, picking tools for the loop, scoped credentials, when to design a loop (problems with clear success criteria + tedious trial-and-error). **Extract:** the definition and the four design levers.
2. **Kief Morris (Thoughtworks) — "Humans and Agents in Software Engineering Loops"** (04 Mar 2026) — https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html — Inner/middle/outer loops; why-loop vs how-loop; humans outside / in / on the loop; the agentic flywheel. **Extract:** the canonical loop taxonomy and the "fix the artefact vs. fix the loop" distinction.
3. **Anthropic — "Building Effective Agents"** (19 Dec 2024) — https://www.anthropic.com/engineering/building-effective-agents — Foundational vocabulary: workflows vs. agents, the **evaluator-optimizer loop**, "LLMs using tools based on environmental feedback in a loop," gates, and stop conditions ("maximum number of iterations to maintain control"). **Extract:** the loop primitives and the verification-gate language.
4. **Simon Willison — "Vibe engineering"** (07 Oct 2025, updated 23 Feb 2026 to "Agentic Engineering") — https://simonwillison.net/2025/Oct/7/vibe-engineering/ — Names the senior-practitioner end of the spectrum; explicitly lists "designing agentic loops" as a core skill alongside tests, planning, QA. **Extract:** the eras naming + the practitioner skill list.

### Theme B — Inner-loop validation / self-correction

5. **CircleCI — "Chunk Sidecars" (via InfoQ)** (19 Jun 2026) — https://www.infoq.com/news/2026/06/circleci-chunk-sidecars/ — CI-quality validation moved *into the agent's inner development loop* so agents "self-correct before code reaches the pipeline"; explicitly calls it "inner-loop validation." **Extract:** the validation-is-the-bottleneck thesis + the inner-loop product framing. (Primary source: https://circleci.com/blog/chunk-sidecars/)
6. **Anthropic — "How Claude Builds Its Own Execution Harnesses" / Dynamic Workflows (via InfoQ)** (15 Jun 2026) — https://www.infoq.com/news/2026/06/claude-code-harnesses/ — Self-correction failure modes named: "agentic laziness," "self-preferential bias," "goal drift." Loop patterns: fan-out-and-synthesize, **adversarial verification**, tournament-style, classifier routing, per-stage model routing for cost. **Extract:** named failure modes + verification loop patterns. (Primary: https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)
7. **Ben O'Mahony (Thoughtworks) — "Building your own CLI Coding Agent with Pydantic-AI"** (27 Aug 2025) — https://martinfowler.com/articles/build-own-coding-agent.html — Concrete walk-through of an agent that runs tests, reads failures, edits, re-runs, and verifies in one loop; shows the test-result-as-feedback signal in code. **Extract:** a buildable example of the act→observe→verify cycle.

### Theme C — Harness vs. loop distinction

8. **Birgitta Böckeler (Thoughtworks) — "Harness Engineering – first thoughts"** (17 Feb 2026) — https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html — Defines harness as "everything except the model"; feed-forward vs. feedback; quotes OpenAI: *"Our most difficult challenges now center on designing environments, feedback loops, and control systems."* **Extract:** the harness definition + the explicit bridge to loops/control systems.
9. **InfoQ Podcast — "From MCP and Vibe Coding to Harness Engineering" (Böckeler)** (08 Jun 2026) — https://www.infoq.com/podcasts/mcp-vibe-coding-harness-engineering/ — Full transcript: context engineering → skills/CLIs replacing MCP → harness = feed-forward + feedback so the agent can "self-correct"; risk = probability + impact + detectability. **Extract:** the one-year evolution narrative and the feed-forward/feedback split.
10. **Birgitta Böckeler — "Harness Engineering" (the considered article)** — https://martinfowler.com/articles/harness-engineering.html — Frames harness elements as **"guides and sensors"** (computational or inferential) and "harness templates." *(Referenced repeatedly by the two sources above; treat as confident-real, skim before citing specifics.)*

### Theme D — Eras / arc framing

11. **Birgitta Böckeler — "Context Engineering for Coding Agents"** (05 Feb 2026) — https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html — The middle era; lazy-loaded skills, progressive disclosure, MCP's decline. *(Listed and dated on the verified Exploring Gen AI index; not individually fetched — confident-real.)*
12. **Martin Fowler — "Exploring Generative AI" (series index)** (ongoing) — https://martinfowler.com/articles/exploring-gen-ai.html — The single best chronological map of the arc, from "autocomplete to agents" (2023) through context → harness → loops (2026). **Extract:** dated timeline to anchor the era boundaries.
13. **OpenAI — "Harness engineering: leveraging Codex in an agent-first world"** — https://openai.com/index/harness-engineering/ — The 1M-LOC / 5-month / no-typed-code case study. **Extract:** the flagship harness case study. ⚠️ *Returned HTTP 403 to the fetcher; verified indirectly via Böckeler's memo and the InfoQ podcast, which both cite and quote it. Re-verify the live URL before direct citation.*

### Theme E — Quantified data & case studies

14. **Stripe "Minions" (via InfoQ)** (20 Mar 2026) — https://www.infoq.com/news/2026/03/stripe-autonomous-coding-agents/ — 1,300+ PRs/week, no human-written code, all human-reviewed; "blueprints = deterministic code + flexible agent loops"; CI/CD + tests + static analysis as the harness. **Extract:** the headline before/after metric + the blueprint loop architecture. (Primary: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents and part 2)
15. **SWE-bench (official leaderboards + site)** — https://www.swebench.com/ — Verified = 500 human-filtered instances, same harness (mini-SWE-agent) across models; progression from SWE-agent 12.47% (Mar 2024) to 76.8% (Claude 4.5 Opus, Feb 2026); mini-SWE-agent hits 65% in 100 lines of Python. **Extract:** the benchmark trajectory + the "same harness, different model" methodology that proves harness/loop matters.

---

## 3. Strongest Quantified Data Points (with source)

| # | Data point | Value | Source | Confidence |
|---|-----------|-------|--------|-----------|
| 1 | Stripe Minions PR output (autonomous, human-reviewed, zero human-written code) | **1,300+ PRs/week** (up from ~1,000) | InfoQ → Stripe blog (Mar 2026) | Verified |
| 2 | Code volume the Minions-managed code underpins | **$1 trillion+** annual payment volume | InfoQ / Stripe (Mar 2026) | Verified |
| 3 | OpenAI harness-engineering case study | **1M+ lines of code in 5 months, "no manually typed code at all"** | Böckeler memo quoting OpenAI (Feb 2026) | Likely accurate (indirect; OpenAI page 403) |
| 4 | SWE-bench Verified top score, frontier model under one harness | **76.8% resolved** (Claude 4.5 Opus, high reasoning) | swebench.com leaderboard (Feb 2026) | Verified |
| 5 | SWE-bench progression (same benchmark, ~2 yrs) | **12.47% (Mar 2024) → 76.8% (Feb 2026)** | swebench.com news + leaderboard | Verified |
| 6 | Minimal harness can be most of the win | **mini-SWE-agent: 65% on SWE-bench Verified in ~100 lines of Python** | swebench.com (Jul 2025) | Verified |
| 7 | SWE-bench Verified harness is held constant | **500 human-filtered instances, identical harness across all models** | swebench.com/verified.html | Verified |
| 8 | Per-task cost on SWE-bench Verified (loop efficiency proxy) | **~$0.05–$0.96 per instance** depending on model | swebench.com leaderboard (Feb 2026) | Verified |
| 9 | OpenAI's stated hardest problem in agent-first dev | **"designing environments, feedback loops, and control systems"** | Böckeler memo quoting OpenAI | Likely accurate (indirect) |
| 10 | Self-correction failure modes loop engineering must defend against | **agentic laziness, self-preferential bias, goal drift** | Anthropic via InfoQ (Jun 2026) | Verified |
| 11 | Validation, not generation, is the new bottleneck | feature-branch activity up sharply while **production deployments have not kept pace** | CircleCI via InfoQ (Jun 2026) | Verified (qualitative/directional) |
| 12 | Cost realism flag | flat-rate and per-token agent pricing is "still very subsidized" (no public IPO numbers yet) | Böckeler, InfoQ podcast (Jun 2026) | Opinion of named expert — flag as such |

**Case study with before/after (requested):** Stripe Minions is the strongest — explicit before/after (~1,000 → 1,300+ PRs/week), a named architecture ("blueprints" = deterministic code interwoven with agent loops), a concrete verification harness (CI/CD + automated tests + static analysis before human review), and scale context ($1T+ payment volume). OpenAI's 1M-LOC/5-month Codex case is the strongest *harness-engineering* before/after but lacks an explicit "before" number and the source page 403'd, so cite it as the secondary, indirectly-verified case.

---

## 4. Content Opportunities & Recommended Angle

**Gaps the existing sources leave open (our white space):**
1. **Nobody has drawn the full four-era arc as one continuous diagram.** Each source covers one or two eras; Fowler's index is chronological but not synthesized. A single "leverage keeps moving up a level" visual is genuinely missing.
2. **The harness-vs-loop boundary is fuzzy in every source** — practitioners use "harness" to mean both the rig and the cycle. A crisp "nouns vs. verbs / equipment vs. rep-scheme" distinction is a clarifying contribution.
3. **Most writing is theory-forward; quantified loop economics are scattered.** Pulling Stripe + SWE-bench cost-per-task + CircleCI's bottleneck data into one place gives the piece hard numbers others lack.

**Recommended narrative angle:** *"You're not getting better at prompting — your leverage point is moving."* Frame the four eras as one staircase where each step automates the previous craft and pushes the human up to govern the next-larger unit: word → context → rig → loop. Land the thesis that **loop engineering is where validation (not generation) becomes the job**, backed by the CircleCI bottleneck data and the Stripe before/after. Keep it first-person/practitioner ("what I'm seeing working with teams"), data-anchored, and end on the open question every honest source raises: cost is still subsidized and self-correction still fails in named ways (laziness, bias, drift) — so loop engineering is a discipline, not a victory lap.

---

## 5. Confidence & Freshness Notes

- **Verified (fetched this run):** Sources 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15 and all their datapoints.
- **Confident-real but not individually fetched:** Sources 10, 11 (listed/dated on verified Thoughtworks/Fowler index pages). Skim before quoting verbatim.
- **Indirectly verified — re-check before direct citation:** Source 13 (OpenAI harness-engineering page returned HTTP 403; content corroborated by two independent sources that quote it).
- **Freshness:** Strong. The center of gravity is Sep 2025 → Jun 2026. Loop engineering as a named discipline is <12 months old (Willison, Sep 2025; Morris, Mar 2026), so this is genuinely current rather than retrospective.
- **One caution to carry into drafting:** model-specific SWE-bench numbers and pricing move monthly — cite with the dataset date (Feb 2026, mini-SWE-agent harness, v2.0.0) attached, and re-pull at publish time.
