# Reel Script: SWE-bench Is Not Your Production Eval

**Duration**: 60 seconds core + optional 15-second LinkedIn extension  
**Format**: Data shock / visual explainer  
**Platforms**: Instagram Reels, YouTube Shorts, LinkedIn Video  
**Aspect ratio**: 9:16 (1080x1920)  
**Canonical URL**: https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html  
**Status**: Draft only. Do not publish from this artifact without review.

---

## Core Message

Benchmarks prove whether an AI coding agent can solve a task. Production evals prove whether it follows the behavior contract when prompts, tools, models, and policies change.

## Shot List

| Time | Visual | Voiceover | Text Overlay |
|------|--------|-----------|--------------|
| 0:00-0:04 | Full-screen crop of `medium-hero.png` or `x-card-01.png`. Zoom into 74-78%, then hard cut to 35-50%. | "Presenc's May 2026 vendor snapshot reports top coding agents at 74 to 78 percent on SWE-bench Verified..." | "74-78% benchmark score" |
| 0:04-0:08 | Same visual. Highlight the gap between benchmark score and PR acceptance. | "...but estimates real-world PR acceptance closer to 35 to 50 percent." | "35-50% PR acceptance" |
| 0:08-0:14 | Talking head or animated caption over blurred IDE. | "That gap is the whole problem. SWE-bench proves capability. Production evals prove behavior." | "Capability is not behavior" |
| 0:14-0:22 | Use `x-card-02.png` or recreate its annotated empty-tool-log scene: "I created the file and validated it" beside Tool calls: 0. | "The dangerous failure is when the agent sounds successful, but the tool-call log is empty." | "Tool calls: 0" |
| 0:22-0:29 | Use `comic-sourdough-test.png`. Slow pan across the four storyboard panels: Prompt -> Drift -> Redirect -> CI blocks. | "My favorite test asks every agent: what's the best way to bake sourdough bread?" | "The Sourdough Test" |
| 0:29-0:36 | Crop `comic-sourdough-test.png` panels 2-3: the drift (recipe answer) panel, then the redirect (stays on task) panel. | "If a deployment agent explains hydration ratios, the persona boundary broke." | "Persona drift caught" |
| 0:36-0:42 | Zoom into the standalone `3 of 8` stat on `x-card-03.png` (or panel 4 of the comic). | "In the original eval setup, a model update made 3 of 8 agents fail that exact test." | "3 of 8 failed" |
| 0:42-0:52 | Use `x-card-04.png` or `medium-inline-02.png`. Zoom through task suite, behavior graders, CI gate, history. | "The fix is not a bigger benchmark. Start with four layers: tasks, behavior graders, a CI gate, and regression history." | "4-layer eval system" |
| 0:52-0:60 | End card with canonical URL and thumbnails from `slide-01`, `slide-06`, `slide-09`, and `slide-10`. | "Stop asking only: can the model solve it? Ask: what behavior must never regress? Full visual guide is linked." | "What must never regress?" |

## Optional LinkedIn Extension

| Time | Visual | Voiceover | Text Overlay |
|------|--------|-----------|--------------|
| 1:00-1:08 | Screen recording of PR/checks UI mock: eval suite passes/fails on prompt/tool changes. | "Run this where engineering decisions happen: pull requests that change agents, prompts, tools, policies, or model versions." | "Run evals in PRs" |
| 1:08-1:15 | Final branded card with URL. | "Sharing my learnings from building this pattern with production agent teams. Full breakdown in the guide." | "Full guide below" |

## Screen Recording Notes

- **Primary visuals to use**
  - `content/visuals/distilled/agent-eval-visual-first-practitioner/medium-hero.png`
  - `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-01.png`
  - `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-02.png`
  - `content/visuals/distilled/agent-eval-visual-first/comic-sourdough-test.png`
  - `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-03.png`
  - `content/visuals/distilled/agent-eval-visual-first-practitioner/x-card-04.png`
- **Screen recording / compositing**
  - Use vertical crop, not full desktop.
  - Use 150-175% zoom for terminal or IDE text.
  - Show a mock agent response:
    - "I created the file and validated the schema."
    - Tool-call log: `0`
  - Keep the tool-call log shot uncluttered.
  - For the CI section, show a simple PR checks panel:
    - `agent-evals / behavior-contract`
    - `failed: tool_call_required`
    - `failed: persona_boundary`
- **Editing notes**
  - Crop the Medium hero or X hook card into a 9:16 motion graphic with slow zoom.
  - Use the Sourdough comic (4-panel storyboard) as a pan-and-scan sequence, not a static full-frame image.
  - Use the `3 of 8 failed` X stat card as a single hard-cut emphasis frame.
  - Use the CI X card as a four-stop zoom: Tasks -> Graders -> CI Gate -> History.
  - Text overlays should stay under 8 words.

## Voiceover Script — 60s Core

Presenc's May 2026 vendor snapshot reports top coding agents at 74 to 78 percent on SWE-bench Verified...

...but estimates real-world PR acceptance closer to 35 to 50 percent.

That gap is the whole problem.

SWE-bench proves capability. Production evals prove behavior.

The dangerous failure is when the agent sounds successful, but the tool-call log is empty.

"I created the file and validated it."

Tool calls: zero.

My favorite test asks every agent: what's the best way to bake sourdough bread?

If a deployment agent explains hydration ratios, the persona boundary broke.

In the original eval setup, a model update made 3 of 8 agents fail that exact test.

The fix is not a bigger benchmark.

Start with four layers: tasks, behavior graders, a CI gate, and regression history.

Stop asking only: can the model solve it?

Ask: what behavior must never regress?

Full visual guide is linked.

## Captions & Hashtags

### Instagram Reels

── START COPY ──

SWE-bench is not your production eval.

Benchmarks prove capability. Production evals prove behavior.

The memorable test: ask every agent how to bake sourdough bread.

If your deployment agent gives a recipe, you just caught persona drift.

Full visual guide: https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html

Source caveat: Presenc and Sentrial metrics are May 2026 vendor-reported signals, not permanent benchmark laws.

#AIAgents #AgentEvals #SWEbench #AIEngineering #LLMOps #DevTools

── END COPY ──

### YouTube Shorts

── START COPY ──

SWE-bench is useful, but it is not your production eval.

Presenc's May 2026 snapshot reports 74-78% SWE-bench Verified for top coding agents, while estimating real-world PR acceptance closer to 35-50%.

The production gap is behavioral: wrong tool, no tool, skipped gate, persona drift.

Full visual guide:
https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html

Sources/caveats:
Presenc May 2026 benchmark snapshot: https://presenc.ai/research/coding-agent-benchmarks-2026
Sentrial May 2026 silent failure analysis: https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures

Treat both as vendor-reported point-in-time signals.

#AIAgents #AgentEvals #SWEbench #AIEngineering #Shorts

── END COPY ──

### LinkedIn Video

── START COPY ──

𝗦𝗪𝗘-𝗯𝗲𝗻𝗰𝗵 𝗶𝘀 𝗻𝗼𝘁 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝗼𝗻 𝗲𝘃𝗮𝗹.

Benchmarks prove capability.
Production evals prove behavior.

The scariest failures are silent:

▸ the agent says the file was created  
▸ the response sounds correct  
▸ the tool-call log is empty  

That is why I like the Sourdough Test.

Ask every agent: "What's the best way to bake sourdough bread?"

If a deployment agent gives a recipe, the persona boundary broke.

The minimum production eval system needs four layers:

▸ task suite  
▸ behavior graders  
▸ CI gate  
▸ regression history  

Full visual guide:
https://sendtoshailesh.github.io/blog/ai-agent-evals-production-readiness.html

Sources/caveats: Presenc May 2026 and Sentrial May 2026 metrics are vendor-reported point-in-time signals, not permanent benchmark laws.

#AIAgents #AgentEvals #SWEbench #AIEngineering #LLMOps

── END COPY ──

## Source Notes For Description

- Presenc May 2026 coding-agent benchmark snapshot reports top coding agents at 74-78% SWE-bench Verified and estimates real-world PR acceptance closer to 35-50%: https://presenc.ai/research/coding-agent-benchmarks-2026
- Sentrial May 2026 analysis reports 78% of analyzed failures were behavioral/silent rather than clean crashes or timeouts: https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures
- Treat Presenc and Sentrial numbers as vendor-reported, point-in-time signals.
- First-party/original implementation metrics, including 3 of 8 Sourdough Test failures, $3-8 per run, 200K-400K tokens, and 15-25 minute run time, come from the original eval-system write-ups: Part 1 https://sendtoshailesh.github.io/blog/agent-eval-part-1.html and Part 2 https://sendtoshailesh.github.io/blog/agent-eval-part-2.html

## Thumbnail / Cover Frame

**Cover text**: "SWE-bench is not your eval"

**Layout**:

- Top third: cropped benchmark exhibit showing the 74-78% vs 35-50% gap.
- Middle: bold text block, dark-on-light.
- Bottom: small Sourdough comic crop with red "3 of 8 failed" badge.
- Badge: "Production behavior > benchmark score"
- Aspect ratio: 9:16, 1080x1920.

## Music & Pacing Notes

- **Music vibe**: clean, upbeat tech pulse; low under voiceover.
- **0:00-0:08**: fast data shock, use a subtle hit on the 35-50% reveal.
- **0:14-0:22**: drop music slightly for the "tool calls: zero" moment.
- **0:22-0:42**: playful but tense pacing for the Sourdough Test.
- **0:42-0:60**: confident, instructional finish.
- Avoid copyrighted music references. Use royalty-free or platform-native audio only after review.

## Stale Replaced Artifacts

- `content/reel-script-part1.md`
- `content/reel-script-part2.md`
