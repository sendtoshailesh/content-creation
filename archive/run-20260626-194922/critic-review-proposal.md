---
title: Proposal - Automated Critic-Review Layer for the Content Pipeline
description: A tiered, confidence-gated critic-review design that reviews artifacts on the human's behalf and escalates only the uncertain or high-risk residue, applying harness + loop engineering to the pipeline's own review bottleneck
author: Shailesh Mishra
ms.date: 2026-06-22
ms.topic: concept
keywords:
  - critic review
  - LLM-as-a-judge
  - evaluator-optimizer
  - selective escalation
  - loop engineering
estimated_reading_time: 14
---

## Proposal: An Automated Critic-Review Layer

> **Problem statement.** The pipeline produces many artifacts (brief, research maps, strategy, 2 blog
> parts, ~10 visuals, LinkedIn, Reel, deck) and every one currently funnels to a human reviewer. That
> human is the bottleneck — review latency, not generation, is what delays production. We want a layer
> of agents/skills/workflows that reviews **on the human's behalf**, catches issues, and escalates only
> the genuinely uncertain or high-stakes residue.
>
> **Grounding.** Evidence base: [content/critic-review-research.md](critic-review-research.md) (18+
> verified sources, STORM-style synthesis) and [content/trend-research.md](trend-research.md)
> (evaluator-optimizer loop, adversarial verification, self-correction failure modes). This document is
> the **design proposal** built from those findings plus reasoning. It changes no other pipeline files.

---

## 1. The core insight (and the irony)

The bottleneck the user hit — too many "Artifacts to review" — is exactly the inversion we documented in
the loop-engineering research: **validation, not generation, is the constraint.** The fix is the same one
the industry is converging on for coding agents: pull verification *into the inner loop* and engineer the
loop so the system self-corrects, escalating to a human only when it genuinely can't.

So this is **harness engineering + loop engineering applied to our own pipeline's review step**:

- **The critic harness** = the *nouns* — the deterministic checks, rubrics ("constitution"), reference
  grounding, and a diverse judge panel. The equipment a reviewer uses.
- **The review loop** = the *verbs* — critique -> score confidence -> decide (auto-approve / revise / escalate)
  -> on revise, regenerate and re-critique -> stop on a condition. The control cycle that decides when a
  human is needed.

The single hardest constraint from the literature governs the whole design: **intrinsic self-correction
without an external signal can *degrade* output** ("LLMs Cannot Self-Correct Reasoning Yet," ICLR 2024).
So every gate must anchor to a *checkable signal* (a link that resolves, a token that matches, a citation
that grounds), never to "model, are you sure?" alone.

---

## 2. Design principles (each traces to evidence)

| # | Principle | Why (evidence) |
|---|-----------|----------------|
| P1 | **Separate generator from critic; critic emits itemized, span-located findings — not a vibe score** | CriticGPT, Self-Refine, evaluator-optimizer all separate roles; CriticGPT's gains came from *written* critiques (critiques preferred 63% on natural bugs) |
| P2 | **Rubric + reference grounding, not open-ended 1-10 scoring** | G-Eval (CoT + form-filling) hit 0.514 Spearman vs humans, beating BLEU/ROUGE "by a large margin" |
| P3 | **Prefer a small, diverse jury over one big judge** | PoLL: a disjoint-family panel is *more* accurate, *less* biased, and **>7x cheaper** than a single large judge |
| P4 | **Anchor every gate to an external, checkable signal** | ICLR 2024: intrinsic self-correction without external feedback can degrade output |
| P5 | **Escalation = confidence x risk, not score alone** | Self-consistency spread + jury disagreement = confidence; risk = probability x impact x detectability (Böckeler) |
| P6 | **Critic augments the human and remembers** | CriticGPT: human+critic preferred >60% vs unassisted; Reflexion: episodic memory lifted pass@1 to 91% vs 80% |
| P7 | **Review process artifacts early, not just the final post** | Agent-as-a-Judge reviews intermediate steps; "as reliable as human evaluation," catching issues cheaper upstream |
| P8 | **Tier the gates cheapest-first, like a newsroom** | triage -> copy-edit -> fact-check -> editor sign-off maps to deterministic -> rubric -> jury -> human; NeMo's 5 rails are this in code |

---

## 3. The architecture: a four-tier critic cascade with a confidence x risk gate

```
                          ARTIFACT (brief / outline / blog / visual / social / script)
                                              │
        ┌─────────────────────────────────────┼─────────────────────────────────────┐
        ▼                                                                             │
  TIER 0 — DETERMINISTIC PREFLIGHT  (near-zero cost, runs on every artifact)          │
  link/citation present & resolves · design-token & DPI check · markdown lint ·       │
  unicode/format rules · word-count band · alt-text present · banned-phrase regex     │
        │  fail -> auto-return to producer agent (no human, no LLM call)              │
        ▼  pass                                                                        │
  TIER 1 — RUBRIC CRITIC  (one grounded LLM critic; G-Eval style, CoT + form-filling) │
  judges against the "content constitution" (content-quality + brand + writing-style) │
  + grounds factual claims against reference-brief.md · emits compliance-severity rows │
        │  clean & low-risk -> AUTO-APPROVE                                            │
        │  findings or medium-risk -> revise-in-loop (regenerate -> re-critique, max N)│
        ▼  contested OR high-risk                                                      │
  TIER 2 — DIVERSE JURY  (PoLL: 3 disjoint-family small judges, only on the residue)  │
  Copilot rubber-duck critic + fallback critic persona + moderator (Co-STORM)         │
        │  unanimous/low-spread -> AUTO-APPROVE (or auto-return if unanimous fail)     │
        ▼  split vote / high-spread                                                    │
  TIER 3 — CONFIDENCE x RISK GATE  (the escalation controller / stop condition)       │
  confidence = jury agreement x self-consistency spread                               │
  risk      = probability x impact x detectability  (per artifact type)               │
        │  high-confidence x low-risk -> AUTO-APPROVE                                  │
        ▼  low-confidence OR high-risk                                                 │
  HUMAN EDITOR  ◄── sees ONLY the residue + a digest: the itemized critique,          │
                    the jury split, the risk reason, and a one-click approve/▢/revise   │
```

**What reaches the human shrinks at every tier.** Tier 0 removes mechanical defects for ~zero cost
(no LLM call). Tier 1 auto-approves the clean, low-risk majority and silently revises fixable ones in a
loop. Tier 2 runs only on what's contested or high-risk. Tier 3 escalates only the still-uncertain or
high-stakes residue. The human becomes an *editor of exceptions*, not a reviewer of everything.

### 3.1 The "content constitution" (Tier 1 rubric)

Reuse what already exists as the judge's rubric (Constitutional AI: principles replace human labels):

- `content/.github/instructions/content-quality.instructions.md` — data specificity, structure, tone
- `writing-style.instructions.md` + `social-formatting.instructions.md` — voice, platform formatting
- `visual-standards.instructions.md` + design tokens — color/typography/DPI for visuals
- `content/reference-brief.md` + `trend-research.md` — the grounding corpus for fact-checks (the
  newsroom "two-source rule" -> require >=1 grounded citation per load-bearing claim)

The critic outputs the **existing machine-readable schema** in
`.github/instructions/shared/compliance-severity.md` (Error / Warning / Info rows + a `GATE: PASS/FAIL`
footer). That schema is already wired to the rollback protocol — we extend it, we don't replace it.

### 3.2 The risk model (Tier 3) — why a pricing claim escalates but alt-text doesn't

`risk = probability(error) x impact(if wrong) x detectability(how hard a reader would catch it)`, scored
0–3 each, per artifact class. High score -> low auto-approve threshold (more readily escalated).

| Artifact / claim type | Impact | Detectability | Risk posture |
|-----------------------|:------:|:-------------:|--------------|
| Public pricing / benchmark number (e.g. "$0.05–$0.96", "76.8%") | High | Hard (looks authoritative) | **Escalate readily** — always fact-check vs source |
| Named attribution ("Willison", "Böckeler") | High | Hard | Escalate readily |
| Headline / hook / thesis claim | High | Medium | Jury, then gate |
| Body prose, transitions | Low | Easy | Auto-approve if Tier 1 clean |
| Alt-text, captions, file names | Low | Easy | Auto-approve on Tier 0 pass |
| Design-token / layout compliance | Medium | Deterministic | Tier 0 catches it; no LLM needed |

### 3.3 Confidence signal (Tier 3) — how we know when to trust the critic

- **Self-consistency spread** — sample the Tier 1 critique N times; high agreement = high confidence,
  divergence = escalate (self-consistency added +3.9 to +17.9 pts on reasoning by marginalizing samples;
  here we use the *spread* as the uncertainty proxy).
- **Jury disagreement** (Tier 2) — a split panel is the cleanest escalation trigger.
- **Calibrated abstention** — the critic may answer "out of my depth"; that auto-escalates (CriticGPT
  notes some tasks exceed even expert-with-model evaluation).

### 3.4 GitHub Copilot rubber-duck review (Tier 2 panelist)

GitHub Copilot's **rubber-duck review** should be treated as a named Tier 2 panelist, not as the whole
review gate. Its value is adversarial reasoning: it reads the artifact from a fresh stance, explains what
looks weak, and forces the producer loop to justify or fix. That maps directly to CriticGPT's strongest
lesson: the useful artifact is an **itemized written critique**, not a score.

**Preferred path when available in VS Code:**

1. The critic orchestrator sends the artifact + constitution + reference brief + risk class to the
   Copilot rubber-duck review surface.
2. Rubber-duck returns a structured critique using the compliance-severity schema.
3. The critic orchestrator normalizes it into the same fields as other jurors:
   `severity`, `category`, `asset/location`, `finding`, `required_fix`, `confidence`, `risk`, `source_signal`.
4. Rubber-duck's vote is one member of the jury. It can trigger revision or escalation, but it cannot
   auto-approve high-risk artifacts alone.

**Fallback when rubber-duck is not programmatically callable:** create a local **rubber-duck critic
persona** inside `.github/skills/critic-review/SKILL.md`. The persona uses the same behavior pattern:

- Ask three adversarial questions before scoring: *What claim would I challenge? What context is missing?
  What would embarrass us if published?*
- Review against the constitution and reference sources, not preference.
- Emit only the findings table + gate verdict + confidence/risk fields.
- Use an explicit abstention: `ABSTAIN: needs human` when the artifact depends on fresh facts, legal/public
  claims, source ambiguity, or visual judgment the model cannot inspect reliably.

This gives us the Copilot rubber-duck behavior even if the product feature cannot be invoked as a tool. In
that fallback mode, the panel still keeps diversity by pairing the local rubber-duck persona with at least
one other reviewer stance: fact-check desk, brand/tone desk, or visual/layout desk.

**Rubber-duck output contract:**

```markdown
## Rubber-Duck Critique

| Severity | Category | Asset / location | Finding | Required fix | Confidence | Risk | Source signal |
|----------|----------|------------------|---------|--------------|------------|------|---------------|
| Error | claim-citation | content/post.md §4 | SWE-bench score has no source date attached | Add source + Feb 2026 dataset date | high | high | reference-grounded |

GATE: FAIL
ABSTAIN: no
JURY_VOTE: revise
```

### 3.5 Critique memory (Reflexion) — the loop that compounds

Persist recurring, confirmed misses to `content/critique-memory.md` (an episodic buffer). On each run the
critic loads it so it stops re-making the same mistakes and producers stop re-triggering them. This is the
"fix the loop, not the artefact" move from loop engineering — when the critic keeps missing X, we patch
the *rubric/harness*, not the individual post.

---

## 4. Mapping onto what we already have (minimal new surface area)

We do **not** start from zero. Today's reviewers become tiers of one cascade:

| Existing piece | Becomes | Change needed |
|----------------|---------|---------------|
| `quality-reviewer` agent | **Tier 1 rubric critic** (prose) | Emit compliance-severity rows + a confidence line; load the constitution explicitly |
| `visual-reviewer` agent | **Tier 1 critic** (visuals) — already emits the schema | Add Tier 0 deterministic token/DPI pre-check before it runs |
| `brand-guardian` agent | **Tier 1 critic** (voice/brand) — already emits the schema | Fold into the same cascade; dedupe overlap with quality-reviewer |
| `grounded-content-reviewer` agent | **Tier 1 fact-check desk** | Anchor strictly to `reference-brief.md`; require grounded citation per claim |
| `compliance-severity.md` | **The findings contract** for all tiers | Add two fields: `confidence` and `risk` per finding |
| GitHub Copilot rubber-duck review | **Tier 2 jury member** (one adversarial voice) | Use directly when callable; otherwise emulate with a local rubber-duck critic persona |
| Orchestrator rollback/redo protocol | **The revise-in-loop + stop condition** | Add a max-iteration cap and the escalation digest |

**New pieces to build (small):**

1. `scripts/pipeline/preflight_check.py` — Tier 0 deterministic checks (links, tokens, lint, citations,
   format, word-count, alt-text). Pattern borrowed from **promptfoo** assertion gates + **DeepEval** DAG.
2. `.github/skills/critic-review/SKILL.md` — the cascade controller: orchestrates Tiers 0-3, computes
  confidence x risk, invokes Copilot rubber-duck review when available, falls back to the local
  rubber-duck critic persona when not, writes the escalation digest, updates `critique-memory.md`.
3. `.github/agents/critic-orchestrator.agent.md` — thin conductor that runs the skill and is the single
   review entry point (replaces ad-hoc calls to four separate reviewers).
4. `content/critique-memory.md` — the Reflexion episodic buffer (created on first run).

---

## 5. Open-source we adopt or borrow from (don't reinvent)

| Framework | License · traction | What we reuse | How |
|-----------|--------------------|---------------|-----|
| **promptfoo** | MIT · 22.5k★ | Assertion-based gates + pairwise judge + CI | Model Tier 0/Tier 1 as declarative assertions runnable in CI on every artifact change |
| **DeepEval** | Apache-2.0 · 16.4k★ | **G-Eval** metric + **DAG** deterministic judge + pytest gates | Tier 1 rubric scoring with deterministic decision graphs (less judge variance) |
| **RAGAS** | Apache-2.0 · 14.5k★ | **Faithfulness** + **Aspect-Critique** | The fact-check tier: grounded-ness vs reference-brief; custom aspects for brand/tone |
| **Guardrails AI / NeMo Guardrails** | Apache-2.0 · 7k / 6.5k★ | Deterministic validator rails (regex, topic, competitor, self-check-facts) | The cheap Tier 0 rail cascade |
| **stanford-oval/storm (Co-STORM)** | MIT · 29.1k★ | **Moderator** agent + **mind-map** shared state | Tier 2 moderator that surfaces issues no juror raised; mind-map as long-review shared state |
| **CriticGPT pattern** | (method) | Tunable catch-rate vs hallucination dial + human-augmentation framing | Tier 3 digest assists the human; tune the dial per risk class |

We can start by *borrowing the patterns* (assertions, G-Eval prompt, faithfulness check) implemented in our
own Python/skills, and only take a hard dependency on a framework (likely **DeepEval** or **promptfoo**) if
we want CI-grade regression tracking.

---

## 6. Phased adoption (each phase ships value and is reversible)

- **Phase A — Deterministic triage + unified findings (the quick win).** Build `preflight_check.py`
  (Tier 0); make all four reviewers emit the compliance-severity table + a confidence/risk line; add the
  escalation digest so the human sees one consolidated exception list instead of N artifacts. *Most of the
  mechanical review load disappears here at ~zero LLM cost.*
- **Phase B — Rubric critic + fact-check desk.** Stand up the `critic-review` skill with a G-Eval-style
  constitution judge (Tier 1) and a reference-grounded faithfulness check (RAGAS/Self-RAG pattern). Auto-
  approve the clean, low-risk majority; revise-in-loop the fixable.
- **Phase C — Jury + confidence x risk gate + memory.** Add the PoLL jury (Tier 2) on the high-risk residue,
  the escalation controller (Tier 3), and `critique-memory.md` (Reflexion). Now only the uncertain/high-
  stakes residue reaches the human.
- **Phase D — Observability + anti-over-trust.** Track auto-approve rate, escalation rate, and judge-human
  agreement over time (Phoenix/MLflow pattern); add **sampled human audits** of auto-approvals so drift
  surfaces. This phase is what keeps the system honest.

---

## 7. Honest risks and the guardrails against them

The research is blunt that an automated critic can be *worse* than no critic if over-trusted. The guardrails
are part of the design, not an afterthought:

| Risk | Guardrail in this design |
|------|--------------------------|
| **Self-preference bias** (critic favors our own model's text — documented in MT-Bench & G-Eval) | Disjoint-family jury (P3); reference-anchored judging (P2); sampled human audits (Phase D) |
| **Position / verbosity bias** in pairwise judging | Randomize order, length-normalize, prefer pointwise rubric where order matters |
| **Intrinsic self-correction degrades output** (ICLR 2024) | P4: never gate on model confidence alone — always an external checkable signal |
| **Automation complacency** (high auto-approve hides drift) | Sampled audits + escalation-rate monitoring; treat the >80% judge-human number as a *ceiling*, not a guarantee |
| **Cost/latency creep** (juries x debate rounds) | Tier ordering — deterministic first; jury runs only on contested/high-risk residue (PoLL keeps even that cheap) |
| **Dispersed, subtle, high-stakes errors** | Goal is *less* human review, not zero — high-risk classes (pricing, attribution, thesis) keep a human in the loop by design |

---

## 8. What "success" looks like (and how we'll measure it)

We avoid promising a fabricated percentage. Instead we instrument the loop and target a measured outcome:

- **Primary metric:** fraction of artifacts auto-approved without human touch (target: the mechanical/low-
  risk majority), tracked alongside **escalation precision** (of escalated items, how many the human
  actually changed) and **miss rate** (auto-approved items a sampled audit later flags).
- **Evidence the ceiling is real:** strong LLM judges already match *human–human* agreement (>80%, MT-Bench);
  CriticGPT-assisted reviewers are preferred >60% of the time vs unassisted; PoLL shows the jury is both
  better and cheaper. The literature supports a large reduction in human touches **for low/medium-risk
  artifacts**, while keeping humans on the high-risk residue.
- **Stop condition:** if sampled-audit miss rate rises above an agreed threshold, the gate tightens
  automatically (lower auto-approve thresholds) — the loop self-regulates.

---

## 9. Recommendation

Adopt the four-tier cascade, starting with **Phase A** (deterministic preflight + unified findings + an
escalation digest) because it removes the largest chunk of mechanical review for the least effort and is
fully reversible. Then layer Phases B–D. Reuse the existing reviewers and the compliance-severity schema as
the backbone; borrow patterns from promptfoo/DeepEval/RAGAS/Co-STORM rather than building judges from
scratch. Keep the human as an **editor of the high-risk exception residue**, never remove them entirely —
the goal is to reduce review time, not to eliminate human judgment where it matters most.

> **Next decision for you:** approve Phase A so I can scaffold `preflight_check.py`, the `critic-review`
> skill, and the unified escalation digest — or adjust the tier boundaries / risk model first. The content
> run remains on hold (see `pipeline-config.md`) until you're ready to resume it through the new gate.
