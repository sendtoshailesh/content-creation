---
name: creative-brief
description: "Turn a topic and clarifying-question answers into a structured Creative Brief that grounds every downstream agent. Use at the start of a content run (Step 1), before strategy scope assessment and visual planning."
argument-hint: "Provide the topic and the content-strategist clarifying-question answers"
---

# Creative Brief Skill

## When to Use

Use at the very start of a content run, immediately after `content-strategist` collects
clarifying-question answers and before scope assessment / visual planning. The brief is the
single source of truth for tone, key message, and visual direction that `blog-writer`,
`visual-strategist`, `infographic-art-director`, `image-content-agent`, and social agents
all read.

> Methodology adapted from `microsoft/content-generation-solution-accelerator`
> (Creative Brief Interpretation): parse free-text intent into structured fields so every
> agent works from the same contract instead of re-deriving intent ad hoc.

## Output

Write `content/creative-brief.md` using the repository template (same file path). Fill
**every** field — a blank field is a missing requirement, not a license to improvise.

## Required fields

| Field | What it captures | Who consumes it |
|-------|------------------|-----------------|
| Overview | What the content is + why now | all |
| Objectives | Primary + secondary jobs-to-be-done | strategist, blog-writer |
| Target audience | Primary/secondary personas, pain points | all |
| Key message | The one sentence to remember | all |
| **Content hypothesis** | The falsifiable bet this content makes + how success is measured | strategist, quality gates, post-publish review |
| Tone & style | Format + voice guardrails | blog-writer, social agents |
| Deliverables | Which outputs this run produces | orchestrator, social agents |
| Visual guidelines | Mood, palette, hero-image direction, reference images | visual-strategist, infographic-art-director, image-content-agent |
| Call to action | What the reader does next | social agents, blog-writer |
| Constraints & guardrails | Compliance, citation needs, safety flags, timeline | quality + compliance gates |

## Content Hypothesis (MVE format — mandatory)

Every brief states the content as a **falsifiable bet**, not just a topic. This is the design-thinking
core adapted from `microsoft/hve-core`'s Minimum Viable Experiment (MVE): a piece of content is a
hypothesis about what will change a reader's belief or behavior, and it should declare in advance how
you will know it worked. Write this as `## 4b. Content hypothesis` directly under the Key message:

```markdown
## 4b. Content hypothesis

**We believe** [target reader segment] currently believes / does [status quo],
and will shift to [new belief or action] **because** [the core insight this content delivers].

**We will know we are right when** [measurable proxy with a threshold and window], e.g.:
- Save-rate ≥ [X]% on the LinkedIn carousel within 7 days, OR
- ≥ [N] qualified comments that quote the framework (not just "great post"), OR
- Scroll-depth ≥ [X]% / read-ratio above the channel baseline, OR
- ≥ [N] practitioners report completing Project 1 from the build-it-yourself section.

**We will know we are wrong when** [the kill / pivot signal], e.g. engagement at or below the
last 3 posts' median AND no qualified comments — meaning the insight did not land and the angle
should be reworked, not just reposted.

**Riskiest assumption** [the single belief that, if false, sinks the piece — name it so the
draft can defend it hardest].
```

Qualities to enforce (from the MVE knowledge base): the hypothesis must be **testable**,
**specific**, **rationale-based**, and **falsifiable**. If you cannot state how the content could
fail, the angle is too vague — sharpen the Key message before drafting. For a multi-part series,
write one hypothesis per part; the riskiest assumption may differ per part.

## Rules

1. **Derive from answers, do not invent.** Pull each field from the clarifying-question
   answers and any `reference-brief.md` / `trend-research.md`. If an answer is missing, ask
   one targeted follow-up rather than guessing.
2. **Voice is fixed:** first-person practitioner, conversational, data-driven, no
   corporate/fundraising framing.
3. **Visual guidelines must distinguish** AI-generated hero/illustrative imagery (scene,
   composition, ~30% negative space, **no embedded text**, brand-color fidelity) from
   deterministic diagrams/infographics/exhibits, which stay programmatic.
4. **Reference images:** list any paths/URLs the `vision-grounding` step should describe so
   generated imagery is grounded in real subject/style.
5. **Set Status to `approved`** only after the user (or strategist) confirms; downstream
   agents may proceed on `draft` but must flag unresolved blanks.
6. **The Content hypothesis is not optional.** A brief with a topic but no falsifiable bet and no
   measurable success/kill signal is incomplete. The post-publish review compares actual
   engagement against this hypothesis to mark the run validated or invalidated.

## Handoff

- `content-strategist` Phase 1 → produces the brief → Phase 2 strategy + Step 2b scope
  assessment build on it.
- `image-content-agent` reads §7 Visual guidelines + §9 guardrails to build image prompts.
- Compliance gates (`brand-guardian`, `visual-reviewer`) check output against §4 key
  message, §5 tone, and §7 visual guidelines.
