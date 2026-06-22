# Social Distribution Strategy — AI Agent Evals Visual-First Edition

*Package: AI Agent Evals for Production Readiness*  
*Canonical URL: https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html*  
*Mode: mandatory visual-first*  
*Do not publish from this artifact.*

---

## Primary Narrative

SWE-bench is useful, but it is not enough for production AI agent evals.

Benchmarks prove whether an agent can solve a coding task. Production evals prove whether the agent follows the behavior contract when prompts, tools, policies, models, and team conventions change.

The core contrast:

- **SWE-bench / coding benchmarks:** capability signal
- **Production evals:** behavior, tool use, persona boundaries, CI regressions, and release readiness signal

The visual-first campaign should make one idea unavoidable:

> Benchmarks tell you whether the model can solve the task. Production evals tell you what behavior must never regress.

## Grounding Notes

- [SWE-bench Verified](https://www.swebench.com/) is used here as a coding-agent capability benchmark signal, not as a production-readiness claim.
- [Presenc's May 2026 coding-agent benchmark snapshot](https://presenc.ai/research/coding-agent-benchmarks-2026) is the source for the **74-78% SWE-bench Verified** and **35-50% real-world PR acceptance** figures. Treat both as vendor-reported, point-in-time signals.
- [Sentrial's May 2026 regression-testing article](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures) is the source for the **78% behavioral/silent failure** figure. Treat it as a vendor-reported operational signal, not a universal failure-rate law.
- First-party/original implementation metrics, including **8 agents**, **38 tasks**, **14 eval suites**, **3 grader types**, **3 of 8 Sourdough Test failures**, **$3-8/run**, **200K-400K tokens**, and **15-25 minutes**, come from the original [Part 1](https://sendtoshailesh.github.io/blog/agent-eval-part-1.html) and [Part 2](https://sendtoshailesh.github.io/blog/agent-eval-part-2.html) write-ups.

## Core Messages

1. **SWE-bench is not your production eval.** Use the benchmark gap to show why capability does not equal production readiness.
2. **The dangerous failures look successful.** Fabrication Without Action is the memorable failure mode: the agent says it created, validated, or deployed something while the tool-call log is empty.
3. **Persona drift needs simple, repeatable tests.** The Sourdough Test makes off-topic behavior visible across all agents.
4. **Production evals need a behavior contract.** Minimum viable eval system: task suite, behavior graders, CI gate, regression history.
5. **Run evals where engineering decisions happen.** The operating model is a PR-level CI loop, not a release-week benchmark ceremony.

## Shareable Assets

| Asset | Path | Visual Family | Best Persona | Primary Message |
|---|---|---|---|---|
| LinkedIn carousel cards | `content/visuals/distilled/agent-eval-visual-first-practitioner/slide-01-hook.png` through `slide-10-cta.png` | Practitioner carousel | Practitioner / tech lead | SWE-bench proves capability; production evals prove behavior |
| X/Twitter cards | `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-01.png` through `x-card-04.png` | Image-thread card pack | Practitioner | Benchmark gap -> empty trace -> Sourdough -> CI gate |
| Medium/Substack assets | `medium-hero.png`, `medium-inline-01.png`, `medium-inline-02.png`, `substack-hero.png` | Platform visual pack | Tech lead | Visual-first long-form summary with canonical link |
| LinkedIn Article exhibits | `linkedin-exhibit-01.png`, `linkedin-exhibit-02.png` | Executive exhibit | Executive / AI team decision-maker | Benchmark confidence can hide production risk |
| Platform excerpt | `content/platform-excerpt-agent-eval-visual-first.md` | Medium/Substack/LinkedIn Article excerpt | Tech lead / executive | Visual-first long-form summary with canonical link |

## Visual-First Campaign Calendar

| Day | Platform | Visual Asset | Visual Family | Text Role | CTA |
|---|---|---|---|---|---|
| Day 0, Tue-Thu 7:30 AM PT | LinkedIn | `slide-01-hook.png` through `slide-10-cta.png` | Practitioner carousel | Narrate the lesson behind the cards: benchmarks prove capability, production evals prove behavior | First comment with canonical URL |
| Day 1, 7:00 AM PT or 5:00 PM PT | X/Twitter | `x-card-01.png` through `x-card-04.png` | Image-thread visuals | Punchy thread: benchmark gap -> silent failures -> Sourdough Test -> CI eval system | Final tweet only |
| Day 3-4 | Medium/Substack | `medium-hero.png`, `medium-inline-01.png`, `medium-inline-02.png`, `substack-hero.png` | Platform visual pack | Add context not shown in visuals; keep canonical link explicit | Canonical URL |
| Day 5 | LinkedIn follow-up | `x-card-03.png` or `slide-10-cta.png` | Storyboard / CTA card | Practitioner story: why the Sourdough Test works | Comment CTA to visual guide |
| Day 7+ | LinkedIn Article | `linkedin-exhibit-01.png`, `linkedin-exhibit-02.png` | Executive exhibits | Leadership angle: production readiness and regression risk | End body canonical URL |

Canonical URL for all CTAs:  
`https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html`

## Recommended Posting Order and Timing

| Order | Day | Time | Platform | Content Type | Lead Asset | Hook |
|---|---|---:|---|---|---|---|
| 1 | Day 0, Tue-Thu | 7:30 AM PT | LinkedIn | Carousel post | 10-slide practitioner pack | "SWE-bench is not your production eval." |
| 2 | Day 0 | Within 60 sec | LinkedIn comment | Source/canonical comment | N/A | Canonical guide + source links |
| 3 | Day 1 | 7:00 AM PT or 5:00 PM PT | X/Twitter | 10-tweet thread | X card pack | "Benchmarks prove capability. Production evals prove behavior." |
| 4 | Day 3-4 | Morning PT | Medium/Substack | Platform excerpt | Medium/Substack visual pack | "The benchmark gap is behavioral." |
| 5 | Day 5 | 7:30 AM PT | LinkedIn | Follow-up post | Sourdough X card / CTA slide | "The Sourdough Test caught persona drift in 3 of 8 agents." |
| 6 | Day 7+ | Morning PT | LinkedIn Article | Leadership article | LinkedIn Article exhibits | "Why production AI agent readiness needs behavior contracts." |

## Copy Angle by Asset and Persona

### 1. LinkedIn Carousel — Practitioner Angle

**Asset:** `slide-01-hook.png` through `slide-10-cta.png`  
**Persona:** IC engineer / platform engineer  
**Angle:** "Here is what to test before your agent ships."

Use concrete practitioner language:

- Tool-call assertions
- Off-topic controls
- Behavior graders
- PR-level CI checks
- Regression history by model, prompt, tool, and release

Primary copy hook:

> SWE-bench is not your production eval.  
> Benchmarks prove capability. Production evals prove behavior.

CTA:

> Full visual guide in the first comment.

### 2. Comic/Storyboard — Practitioner Angle

**Asset:** `x-card-03.png` or `slide-10-cta.png`  
**Persona:** Practitioner  
**Angle:** "One absurd prompt can reveal persona drift."

Best copy hook:

> My favorite AI agent eval asks every agent how to bake sourdough bread.

Message:

- A deployment agent should not become a recipe assistant.
- A model update caused 3 of 8 agents to fail this in the first-party/original eval system.
- Simple repeatable tests become team language.

CTA:

> If your team has agents with different roles, add one off-topic control per agent this week.

### 3. One-Page Framework — Tech Lead Angle

**Asset:** `x-card-04.png`, `medium-inline-02.png`, or `slide-07-step3.png`  
**Persona:** Tech lead / AI team lead  
**Angle:** "You do not need a giant eval platform to start."

Use the four-layer structure:

1. Task suite
2. Behavior graders
3. CI gate
4. Regression history

Best copy hook:

> The first production agent eval system does not need to be huge. It needs four layers.

CTA:

> Start with two tasks: one happy-path workflow and one behavior-boundary test.

### 4. Executive Exhibit — Executive / Decision-Maker Angle

**Asset:** `linkedin-exhibit-01.png`  
**Persona:** AI team decision-maker / executive  
**Angle:** "Leaderboard confidence is not release confidence."

Best copy hook:

> A high benchmark score can still hide production risk.

Message:

- Presenc May 2026 snapshot: top coding agents at 74-78% SWE-bench Verified.
- Presenc May 2026 estimate: real-world PR acceptance closer to 35-50%.
- Sentrial May 2026 analysis: 78% of analyzed failures were behavioral/silent rather than clean crashes/timeouts.
- Treat all vendor numbers as vendor-reported point-in-time signals.

CTA:

> Ask your team: what behavior must never regress before an agent ships?

### 5. Platform Excerpt — Tech Lead / Executive Angle

**Asset:** `content/platform-excerpt-agent-eval-visual-first.md`  
**Persona:** Tech lead, AI team decision-maker  
**Angle:** "The visual summary for people who need the framework, not the full implementation history."

Use for:

- Medium import after canonical page exists.
- Substack Note, not newsletter.
- LinkedIn Article with unique framing.

CTA:

> Full visual guide: https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html

## Cross-Promotion Plan

- LinkedIn carousel drives to canonical guide in the first comment.
- X/Twitter thread uses the benchmark gap and Sourdough Test as thread anchors; canonical URL appears only in the final tweet.
- Reddit is not selected for this package; do not generate or publish a Reddit post from this run.
- Medium/Substack/LinkedIn Article should use the visual assets inline and point back to the canonical page.
- LinkedIn follow-up should reuse the comic/storyboard to catch people who skipped the carousel.

## Platform-Specific Notes

### For @social-linkedin

Use the already generated visual-first post as the starting point:

- `content/linkedin-post-agent-eval-visual-first.md`

Required upload order:

1. `visuals/distilled/agent-eval-visual-first-practitioner/slide-01-hook.png`
2. `visuals/distilled/agent-eval-visual-first-practitioner/slide-02-promise.png`
3. `visuals/distilled/agent-eval-visual-first-practitioner/slide-03-problem.png`
4. `visuals/distilled/agent-eval-visual-first-practitioner/slide-04-framework.png`
5. `visuals/distilled/agent-eval-visual-first-practitioner/slide-05-step1.png`
6. `visuals/distilled/agent-eval-visual-first-practitioner/slide-06-step2.png`
7. `visuals/distilled/agent-eval-visual-first-practitioner/slide-07-step3.png`
8. `visuals/distilled/agent-eval-visual-first-practitioner/slide-08-interrupt.png`
9. `visuals/distilled/agent-eval-visual-first-practitioner/slide-09-recap.png`
10. `visuals/distilled/agent-eval-visual-first-practitioner/slide-10-cta.png`

First comment must include:

`https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html`

Hashtags:

`#AIAgents #AgentEvals #SWEbench #AIEngineering`

### For @social-twitter

Use the generated visual-first X/Twitter thread at `content/x-twitter-thread.md`. Existing `x-twitter-thread-part1.md` and `x-twitter-thread-part2.md` are stale because they predate the visual-first reset and canonical slug.

Thread structure:

1. Hook: SWE-bench is not your production eval
2. Benchmark gap: 74-78% SWE-bench Verified vs 35-50% PR acceptance
3. Why the gap is behavioral
4. Fabrication Without Action
5. Sourdough Test
6. 3 of 8 agents failed after model update
7. Four-layer eval system
8. CI gate
9. What to test first
10. Canonical URL

Use visuals sparingly and match the generated thread:

- Tweet 1: `x-card-01.png`
- Tweet 3: `x-card-02.png`
- Tweet 5: `x-card-03.png`
- Tweet 7: `x-card-04.png`

Canonical URL only in final tweet.

### For @social-reddit

Reddit is not currently selected in pipeline config, but if Step 4c adds it:

Target subreddits from config:

- r/MachineLearning
- r/ExperiencedDevs
- r/artificial
- r/programming
- r/ChatGPTCoding
- r/CopilotForDevs

Best framing:

> How are you testing AI agent behavior beyond coding benchmarks?

Avoid:

- "I wrote a blog"
- Image-first promotion
- Link-first post

Suggested post structure:

- TL;DR
- Problem: benchmarks do not test production behavior
- Example: tool-call log empty while response claims work was done
- Question: what are teams using for behavior regressions?
- Optional resource link at end only

## Canonical Alignment and Legacy Artifacts

Canonical URL now must be:

`https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html`

### Current visual-first artifacts

| Artifact | Status |
|---|---|
| `content/agent-eval-visual-first-series.md` | Uses the new SEO slug, canonical URL, and redesigned visual pack |
| `content/linkedin-post-agent-eval-visual-first.md` | Uses the new canonical URL and visual-first carousel order |
| `content/platform-excerpt-agent-eval-visual-first.md` | Uses the new canonical URL and visual-first inline assets |
| `content/x-twitter-thread.md` | Uses the new canonical URL and selected redesigned assets |
| `content/reel-script.md` | Uses the new canonical URL and redesigned visual cues |
| `content/youtube-script.md` | Uses the new canonical URL and redesigned visual cues |
| `content/visuals/distilled/agent-eval-visual-first/manifest.md` | Asset manifest is slug-independent for URL purposes |

### Legacy part-specific artifacts not used in this package

| Artifact | Status |
|---|---|
| `content/x-twitter-thread-part1.md` / `content/x-twitter-thread-part2.md` | Legacy part-series artifacts; do not use for this visual-first package |
| `content/reel-script-part1.md` / `content/reel-script-part2.md` | Legacy part-series artifacts; do not use for this visual-first package |
| `content/linkedin-post-part1.md` / `content/linkedin-post-part2.md` and formatted variants | Legacy part-series artifacts; do not use for this visual-first package |

## Engagement Playbook

### LinkedIn

- Reply to every comment within the first 4 hours.
- If someone asks "why not just use SWE-bench?", respond with the capability-vs-behavior distinction.
- If someone asks for implementation detail, point to the one-page framework and canonical guide.
- Use the comic as a follow-up comment if discussion turns to persona drift.

### X/Twitter

- Pin the thread for 48 hours.
- Reply to technical objections with concrete examples: tool-call assertions, off-topic tests, CI gates.
- If the Sourdough Test gets traction, create a standalone follow-up tweet with the comic visual.

### Reddit, if selected

- Do not defend the blog. Discuss the problem.
- Ask commenters what failure modes they are seeing.
- Only share the canonical link when it directly answers a question or at the end as an optional resource.

### Recycling

- Best Reddit objection -> LinkedIn follow-up post.
- Best LinkedIn implementation question -> X/Twitter mini-thread.
- Best X/Twitter quote-tweet -> add to future LinkedIn Article angle.
