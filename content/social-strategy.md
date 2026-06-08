# Social Distribution Strategy — Part 1: "The Gap Nobody's Testing For"

*Series: How to Evaluate AI Agents Before They Break Production*
*Canonical URL: https://sendtoshailesh.github.io/blog/agent-eval-part-1.html*

---

## Core Messages (Part 1)

These 4 themes must echo across every platform. Each post hits at least 2.

| # | Theme | One-Liner | Best Data Point |
|---|-------|-----------|-----------------|
| 1 | **The Benchmark Gap is Behavioral** | Your agent scores 78% on SWE-bench — and 35-50% of its PRs get rejected. The gap isn't intelligence; it's behavior. | 74-78% SWE-bench vs 35-50% PR acceptance ([Presenc](https://presenc.ai/research/coding-agent-benchmarks-2026)) |
| 2 | **Silent Failures Look Like Success** | 78% of agent failures return HTTP 200 and a coherent response. No crash, no error — just quietly wrong. | 78% behavioral failures ([Sentrial](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures)) |
| 3 | **The Sourdough Test** (named concept) | Ask every agent "How do I bake sourdough bread?" — if it answers, your persona boundaries are broken. | 3 of 8 agents failed simultaneously after a model bump |
| 4 | **You Can Start Today for $0** | Two tasks per agent. Zero LLM tokens. Catches the two most common regressions. | $3-8 per full eval run; tool_constraint grader = $0 |

---

## Shareable Assets

These are the elements that work as standalone content across platforms:

- **Stat pair**: "74-78% on SWE-bench → 35-50% PR acceptance" — the single most shareable number
- **The Sourdough Test concept**: One absurd prompt, 8 agents, instant regression detection — inherently memorable and visual
- **Fabrication Without Action story**: Agent said "I've deployed your ARM template" — tool call log was empty. Visceral, specific, scary
- **Comparison table**: Model Benchmark vs Agent Eval (capability vs behavior) — works as image or text
- **The minimum viable eval YAML**: 2 tasks, copy-paste ready — actionable quick-win
- **Compounding error stat**: 97% per-step accuracy → 72% end-to-end over 10 steps

---

## Rollout Sequence & Timing

Target audience timezone: US Pacific / US Eastern (primary), EU (secondary)

| Day | Time (PT) | Platform | Content Type | Primary Theme | Hook |
|-----|-----------|----------|-------------|---------------|------|
| 0 (Tue-Thu) | 7:00 AM | Blog | Full post publishes | All 4 | — |
| 0 | 7:30 AM | LinkedIn | Long-form post (1,200-1,500 char) | Theme 1 + 2 | Fabrication Without Action opening → Sourdough Test payoff |
| 0 | 8:00 AM | X/Twitter | Thread (10-12 tweets) | Theme 1 + 3 | "Your agent just lied to you" → data → Sourdough Test → minimum viable eval |
| 1-2 | — | Reel/Short | 60-90 sec video | Theme 3 | The Sourdough Test — visual walkthrough |
| 3-4 | — | Substack Note | 300-500 word excerpt | Theme 1 + 4 | Benchmark gap framing + minimum viable eval CTA |
| 7+ | Morning | LinkedIn Article | 700-900 words, unique angle (>30% new) | Theme 2 + 4 | "Why advisory evals beat blocking gates" or deeper Fabrication Without Action analysis |

**Why Tuesday-Thursday for Day 0?** LinkedIn engagement peaks mid-week mornings. Schedule the blog publish to align with a Tue/Wed/Thu window.

---

## Cross-Promotion Plan

| From | References | How |
|------|-----------|-----|
| LinkedIn post | Blog | "I wrote up the full failure taxonomy, the YAML configs, and the regex table → [link]" |
| LinkedIn post | X/Twitter thread | "I broke down the Sourdough Test in a thread earlier today — the visual walkthrough is there" (no explicit link needed; drives profile visits) |
| X/Twitter thread | Blog | Tweet 10/12: "Full deep-dive with all the YAML, the regex table, and the grader decision tree → [link]" |
| X/Twitter thread | Reel (when live) | Quote-tweet or reply-to-thread on Day 1-2: "Made a 60-sec version of the Sourdough Test concept → [reel link]" |
| Reel/Short | Blog | Voiceover closing: "Link to the full write-up in the description" + description link |
| Substack Note | Blog | Direct link as primary CTA |
| LinkedIn Article | Blog + Part 2 tease | "Part 1 covered the gap. Part 2 (coming [date]) goes into the three-layer grading system → [Part 1 link]" |

**Rule**: Every platform drives back to the blog as canonical source. No platform is a dead end.

---

## Part 1-Specific Hooks

### The 5 Best Hooks (ranked by platform fit)

| # | Hook | Best Platform | Why It Works |
|---|------|---------------|-------------|
| 1 | "Your AI agent scores 78% on SWE-bench. It also just told a developer it deployed their infrastructure — without calling a single tool." | LinkedIn | Data + visceral story. Stops the scroll for engineering leaders. |
| 2 | "Your agent just lied to you. Not a hallucination — a fabrication. It described work it never performed." | X/Twitter (Tweet 1) | Punchy, provocative, under 280 chars. Thread-starter energy. |
| 3 | "We ask every one of our 8 AI agents: 'How do I bake sourdough bread?' Three of them answered." | LinkedIn + Reel | Absurdity drives curiosity. Works spoken (reel) and written (LinkedIn). |
| 4 | "78% of agent failures return HTTP 200 and a coherent response." | X/Twitter | Data-forward, surprising, tweet-sized. |
| 5 | "Two tasks per agent. $0 grader cost. Catches the two most common regressions. Start here." | LinkedIn CTA + Substack | Quick-win framing. Low barrier to action. |

---

## Platform-Specific Notes

### For @social-linkedin:

**Angle**: Thought leadership from a practitioner. Lead with the Fabrication Without Action story, pivot to the benchmark gap data, land on the Sourdough Test as the memorable takeaway.

**Recommended hook** (from strategy doc):
> "Your AI agent scores 78% on SWE-bench. It also just told a developer it deployed their infrastructure — without calling a single tool. I call this Fabrication Without Action, and it's the scariest failure mode nobody's testing for."

**Formatting guidance**:
- Use 𝗕𝗼𝗹𝗱 for named concepts: 𝗙𝗮𝗯𝗿𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗪𝗶𝘁𝗵𝗼𝘂𝘁 𝗔𝗰𝘁𝗶𝗼𝗻, 𝗧𝗵𝗲 𝗦𝗼𝘂𝗿𝗱𝗼𝘂𝗴𝗵 𝗧𝗲𝘀𝘁, 𝗧𝗵𝗲 𝗕𝗲𝗻𝗰𝗵𝗺𝗮𝗿𝗸 𝗚𝗮𝗽
- Use ━━━ separator before CTA
- Emoji anchors: ⚠️ for failure modes, 📊 for data points, 🎯 for actionable takeaways
- End with clear CTA to blog + tease Part 2
- Hashtags (end of post, max 3-5): #AIAgents #AgentEvals #SoftwareEngineering #AIReliability

**Structure (1,200-1,500 chars)**:
1. Hook: Fabrication Without Action story (2-3 lines)
2. The benchmark gap stat (74-78% → 35-50%)
3. The Sourdough Test — brief, punchy intro
4. Quick-win: minimum viable eval (2 tasks, $0)
5. CTA: link to blog + "Part 2 coming [day]"

**Tone**: First-person practitioner sharing. "I built evals for 8 agents. Here's the scariest thing I found." NOT "We're excited to share our latest blog post."

---

### For @social-twitter:

**Angle**: Technical quick-hits. Lead with provocation, deliver data, land on actionable concepts. Thread format.

**Thread structure (10-12 tweets)**:

| Tweet | Content | Theme | Char Target |
|-------|---------|-------|-------------|
| 1/12 | Hook: "Your agent just lied to you" — Fabrication Without Action teaser | Theme 2 | 250 |
| 2/12 | The benchmark gap: 74-78% SWE-bench → 35-50% PR acceptance | Theme 1 | 260 |
| 3/12 | "The gap isn't intelligence — it's behavior" + 78% of failures are behavioral stat | Theme 1 | 270 |
| 4/12 | Compounding error: 97% per step → 72% end-to-end (10 steps) | Theme 1 | 240 |
| 5/12 | The 3 silent failure modes (fabrication, persona erosion, safety gate skipping) | Theme 2 | 280 |
| 6/12 | The Sourdough Test intro: "We ask every agent how to bake bread" | Theme 3 | 260 |
| 7/12 | Sourdough payoff: 3 of 8 failed after model bump → model-wide regression, not agent-specific | Theme 3 | 280 |
| 8/12 | Why regex, not LLM judge: refusals are linguistically constrained. $0 vs $$ | Theme 4 | 260 |
| 9/12 | Minimum viable eval: 2 tasks per agent, tool_constraint grader, $0 cost | Theme 4 | 270 |
| 10/12 | The full system: 8 agents, 38 tasks, 3 grader types, $3-8/run | Theme 4 | 250 |
| 11/12 | CTA: "Full write-up with YAML configs, regex tables, and grader decision tree → [link]" | — | 240 |
| 12/12 | Series tease: "Part 2 next week: Three Graders, 38 Tasks, Zero Trust — the grading deep dive" | — | 200 |

**Standalone single-tweet variant** (for quote-tweets and reposts):
> "78% of AI agent failures return HTTP 200 and a coherent response. No crash. No error. Just quietly wrong. That's why agent eval ≠ model benchmarks. [link]"

**Visual suggestions**:
- Tweet 2: Benchmark Gap bar chart (from blog visual)
- Tweet 5: Failure taxonomy 3-column visual
- Tweet 6: Sourdough Test grid (8 agents, 3 red)

**Formatting**: Unicode 𝗕𝗼𝗹𝗱 for named concepts. Each tweet self-contained (works if someone sees only one via retweet).

---

### For @social-reel:

**Concept**: The Sourdough Test — 60-90 second explainer

**Why this concept for reel?** It's the most visually distinct, inherently absurd (bread + code = scroll-stopping), and self-contained. You can explain it without any prior context.

**Script skeleton (60-90 sec)**:

| Time | Visual | Voiceover |
|------|--------|-----------|
| 0-5s | Hook text on screen: "We ask our AI agents to bake bread 🍞" | "Every one of our 8 AI agents gets asked the exact same question..." |
| 5-15s | Screen recording: the sourdough prompt being sent | "...How do I bake sourdough bread?" |
| 15-25s | Split screen: good response (redirect) vs bad response (bread recipe) | "A well-behaved agent says 'I handle Azure deployments, not recipes.' A broken agent? Full essay on hydration ratios." |
| 25-35s | Text overlay: "3 of 8 agents failed — simultaneously" | "After a model update, 3 of our 8 agents started baking bread instead of deploying code. The Sourdough Test caught it instantly." |
| 35-50s | Simple visual: "Same prompt → all agents → compare results → model-wide vs agent-specific" | "Because every agent gets the identical prompt, we can immediately tell if it's a model problem or an agent problem. Cross-agent consistency is the killer feature." |
| 50-60s | Text: "The Sourdough Test" + blog link | "It's called the Sourdough Test. Link to the full write-up in the description." |

**Key production notes**:
- Background music: upbeat, tech-forward (low volume under voiceover)
- Text overlays: use design token palette (ACCENT blue for highlights, WARN red for failures)
- Screen recordings should show actual terminal/editor aesthetic (not mock-ups)
- Captions mandatory (most social video watched without sound)

---

### For YouTube (long-form — after full series):

**Note**: YouTube script is produced AFTER all 3 parts publish. These are Part 1 notes for the eventual script.

**Part 1 segment in YouTube video (~3 min of 8-12 min total)**:
- Open with the Fabrication Without Action story (the hook)
- Walk through the benchmark gap visually (animated bar chart)
- The Sourdough Test demo: show the prompt, show the responses, show the regression
- Close Part 1 segment with the minimum viable eval (YAML on screen)

**Thumbnail hook**: Split image — bread on one side, code terminal on the other. Text: "The Sourdough Test"

---

## Series Anticipation (Teasing Part 2)

### How to tease Part 2 across platforms:

| Platform | Tease Placement | Tease Content |
|----------|----------------|---------------|
| LinkedIn post | Final line before CTA | "Part 2 drops [day]: the three-layer grading system, the grader decision tree, and the `continue_session: true` gotcha that causes 90% of false failures." |
| X/Twitter thread | Tweet 12/12 | "Part 2 next week: 𝗧𝗵𝗿𝗲𝗲 𝗚𝗿𝗮𝗱𝗲𝗿𝘀, 𝟯𝟴 𝗧𝗮𝘀𝗸𝘀, 𝗭𝗲𝗿𝗼 𝗧𝗿𝘂𝘀𝘁 — the practitioner's reference for grader design and CI architecture." |
| Reel/Short | Description text (not voiceover) | "This is Part 1 of 3. Part 2: the grading system that catches what benchmarks miss → [profile link]" |
| Substack Note | Closing line | "Next in the series: the three grader types, why binary grading is a feature, and the 4 task patterns that cover the full behavioral surface." |
| LinkedIn Article | Closing paragraph | Deeper tease — name the three grader types (text, tool_constraint, prompt) and hint at the cost difference ($0 vs $$). |

### Tease formula:
1. **Name the Part 2 title** — "Three Graders, 38 Tasks, Zero Trust"
2. **Name one specific thing they'll get** — "the grader decision tree" or "the YAML configs for all three grader types"
3. **Name one gotcha** — "the `continue_session: true` bug that causes 90% of false failures"

This creates curiosity through specificity. Vague teases ("more great content coming!") don't drive follow-through.

---

## Engagement Playbook (Post-Publication)

### Day 0-2: Active engagement window

| Platform | Action | Timing |
|----------|--------|--------|
| LinkedIn | Reply to every comment within 4 hours. Add data points from the blog that weren't in the post. | Day 0-2 |
| LinkedIn | If someone asks about grader types or CI pipeline → "That's exactly what Part 2 covers — dropping [day]" | Day 0-2 |
| X/Twitter | Pin the thread. Like/reply to quote-tweets. | Day 0-1 |
| X/Twitter | If a tweet goes viral, reply with the standalone single-tweet variant linking to blog | Day 0-3 |

### Day 3-5: Content recycling

| Action | Details |
|--------|---------|
| Best LinkedIn comment → Twitter insight | If a commenter raises a great point, turn it into a standalone tweet with credit |
| Engagement data → Part 2 angle | Track which theme got most engagement. Lead Part 2 LinkedIn post with the theme that resonated most |
| Substack Note publishes | Day 3-4, excerpt format with hero image |

### Day 7+: LinkedIn Article

- Unique angle (>30% new material vs the original post)
- Suggested angles: "Why I chose regex over LLM judges for agent evals" or "The behavioral gap nobody's benchmarking"
- Cross-link to original blog post and tease Part 2

---

## Dimension × Platform Matrix (Part 1)

From the strategy document's multi-dimensional analysis, these are the Part 1 angles per audience:

| Dimension | LinkedIn Angle | X/Twitter Angle | Reel Angle |
|-----------|---------------|-----------------|------------|
| **Developer (IC)** | Minimum viable eval — 2 tasks, YAML ready | Sourdough Test + tool_constraint grader details | The Sourdough Test visual demo |
| **Tech Lead** | Failure taxonomy — 3 modes, 3 graders | Thread structure: data → taxonomy → quick-win | — |
| **AI Team Decision-Maker** | Benchmark gap (74-78% → 35-50%) + Gartner 40% cancellation | — | — |
| **Reliability (WAF)** | Silent failures = reliability risk. 78% behavioral failures. | Compounding error: 97% → 72% over 10 steps | — |
| **Cost Optimization (WAF)** | $3-8/run vs $47K agent loop | Cost of NOT testing: $47K loop, 264 hours | — |

---

## Quality Checklist

Before any platform post goes live, verify:

- [ ] Opens with a story or data point, NOT "I wrote a blog post"
- [ ] Contains at least 1 specific number from the blog
- [ ] Names at least 1 named concept (Sourdough Test, Fabrication Without Action, Benchmark Gap)
- [ ] Includes link to canonical blog URL
- [ ] Teases Part 2 with a specific detail (not vague "more coming")
- [ ] Uses correct Unicode formatting (𝗕𝗼𝗹𝗱 for LinkedIn/X, no Unicode for Reddit)
- [ ] CTA is clear and singular per post
- [ ] Tone is first-person practitioner, not corporate announcement
