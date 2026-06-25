# REVR — p2-04-stripe-swebench.png

- Source artifact: `content/from-prompts-to-loop-engineering.md` (proof at scale: Stripe + SWE-bench)
- Renderer: `content/visuals/render_loop_engineering.py` :: `stripe_swebench()` (matplotlib, two panels)
- Model (blind read): GPT (multimodal) in GitHub Copilot

## SOURCE INTENT

Two proofs. Left: Stripe "Minions" PRs/week rose ~1,000 → 1,300+ (+30%), zero human-written code (all
human-reviewed), underpinning $1T+ annual payment volume. Right: SWE-bench Verified ~6x in two years —
12.5% (SWE-agent, Mar 2024) → 65% (mini-SWE-agent, Jul 2025) → 76.8% (Claude 4.5 Opus, Feb 2026), same
harness/different model, per-task cost band ~$0.05–$0.96/instance.

## Iteration 1 — PASS

DERIVED READ (blind):
- One-line message: "Left bar chart: Stripe PRs/week ~1,000 (before) → 1,300+ (after), +30%. Right line
  chart: SWE-bench Verified climbs 12.5% (Mar 2024) → 65% (Jul 2025) → 76.8% (Feb 2026), ~6x in two
  years, cost band ~$0.05–$0.96/instance — loops scale."
- Element inventory: bars labelled with values + a +30% delta + Before/After categories + caption; line
  points labelled with % + model name + date; y-axis 0–100%; red cost-band callout; italic 'same
  harness, different model' note; sources on both panels. Nothing `UNDECODABLE`.
- Color/shape semantics: grey 'before' vs blue 'after' bar (labelled); single blue trajectory (labelled
  points). No legend gap.
- No false signal: real measured values with named sources; cost band disclosed.

SCORE: 96/100 (message 30 / encoding 24 / completeness 15 / order 14 / no-false-signal 10 / standalone 3)

VERDICT: **PASS** — score ≥ 85, zero legend/encoding gaps, blind message matches source intent.
