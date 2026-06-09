"""Practitioner distilled pack — rebuilt on the HTML/CSS + Chromium engine.

One consistent white design language (Inter, shared tokens), no per-slide
theme cycling, no stray slide counters, no gauges. Social cards render at a
larger type scale than in-article figures. Every asset passes the DOM
inspector before rasterizing.

Run:
    python3 content/visuals/distilled/agent-eval-visual-first-practitioner/render_html_pack.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from scripts.visuals.html.components import (  # noqa: E402
    bar, body, checklist, eyebrow, flow, gap_callout, grid, metric, quote,
    source, stat, subtitle, title,
)
from scripts.visuals.html.design import page  # noqa: E402
from scripts.visuals.html.inspect import inspect_files  # noqa: E402
from scripts.visuals.html.render import render_many  # noqa: E402

OUT = Path(__file__).resolve().parent
SOCIAL = 1.5   # 1080x1080 carousel slides (full-screen mobile)
XCARD = 1.25   # 1600x900 X feed cards
INLINE = 1.0   # article-embedded figures


# ---------------------------------------------------------------------------
# Carousel slides (1080x1080)
# ---------------------------------------------------------------------------

def slide_01() -> str:
    b = f"""
    {eyebrow("AI agent evals")}
    {stat("74-78%", "SWE-bench Verified capability score")}
    {title("A high benchmark score is not production readiness.")}
    <div class="card" style="background:var(--bg); gap:calc(18px*var(--scale));">
      {bar("Capability (benchmark)", 76, "74-78%", "")}
      {bar("Behavior (production)", 42, "35-50%", "warn")}
    </div>
    {subtitle("So what is the benchmark missing?")}
    {source()}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_02() -> str:
    b = f"""
    {eyebrow("The path")}
    {title("From benchmark to release gate")}
    {subtitle("Four checks close the behavior gap.")}
    {flow([("1","Define the behavior contract",""),
           ("2","Build a real-task eval set","accent"),
           ("3","Grade behavior, not just answers","accent"),
           ("4","Gate every release in CI","ok")])}
    {source()}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_03() -> str:
    b = f"""
    {eyebrow("The gap is behavioral")}
    {title("Can-solve is not will-follow")}
    <div class="grid two">
      {metric("74-78%", "SWE-bench Verified — can the agent solve the task", "accent")}
      {metric("35-50%", "Real PR acceptance — does it follow the contract", "warn")}
    </div>
    {body("Benchmarks ask whether an agent can solve a task. Production evals ask whether it honors the behavior contract every time.")}
    {source()}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_04() -> str:
    b = f"""
    {eyebrow("The system")}
    {title("Four layers make evals real")}
    {flow([("1","Tasks — real production workflows",""),
           ("2","Graders — text + tool-call checks","accent"),
           ("3","CI gate — pass or block the release","accent"),
           ("4","History — drift by model, prompt, tool","ok")])}
    {body("Start small: one task suite, behavior graders, a CI gate, and history tracked by model, prompt, and release.")}
    {source("Source: first-party AI agent evals implementation pattern.")}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_05() -> str:
    b = f"""
    {eyebrow("Step 1")}
    {title("Use real workflows first")}
    <div class="grid two">
      {metric("38", "production workflow tasks", "accent")}
      {metric("8", "agents under test", "purple")}
    </div>
    {body("Score the agent on the real tasks users run — not just curated benchmark prompts that flatter the model.")}
    {source("Source: first-party implementation metrics.")}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_06() -> str:
    b = f"""
    {eyebrow("Step 2")}
    {title("Grade the behavior trace")}
    {checklist([("ok","Assert the expected tool calls fired"),
                ("ok","Check refusal boundaries held"),
                ("ok","Require confirmation gates before writes")])}
    {body("Final-answer checks are not enough. A polished answer can hide a skipped step.")}
    {source("Source: OpenAI Evals guide; first-party behavior graders.")}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_07() -> str:
    b = f"""
    {eyebrow("Step 3")}
    {title("Block regressions in CI")}
    <div class="grid three">
      {metric("$3-8", "per eval run", "accent")}
      {metric("200-400K", "tokens per run", "purple")}
      {metric("15-25m", "parallel runtime", "warn")}
    </div>
    {body("A full behavior eval suite is cheap enough to run on every pull request — treat a failure like a failing test.")}
    {source("Source: first-party implementation metrics.")}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_08() -> str:
    b = f"""
    {eyebrow("Pattern interrupt")}
    {quote("The answer can look perfect while the agent quietly skipped the work.")}
    {body("That is exactly the failure benchmarks never catch — and the one your users feel first.")}
    {source("Source: AI agent evals failure taxonomy.")}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_09() -> str:
    b = f"""
    {eyebrow("Recap")}
    {title("Your release control panel")}
    {checklist([("ok","Real-task eval set"),
                ("ok","Behavior + tool-call graders"),
                ("ok","CI gate wired to block ships"),
                ("warn","Ship gate missing — scores are decoration")])}
    {source("Source: AI agent evals production-readiness guide.")}"""
    return page(1080, 1080, b, scale=SOCIAL)


def slide_10() -> str:
    b = f"""
    {eyebrow("Take this with you")}
    {title("Save this before your next agent release")}
    {body("The Sourdough Test turns silent persona drift into a visible, gated release signal.")}
    <div class="gap-callout">
      <span class="gap-num" data-role="value">Guide</span>
      <span data-role="label">Full visual walkthrough — link in comments.</span>
    </div>
    {source("Source: AI agent evals production-readiness series.")}"""
    return page(1080, 1080, b, scale=SOCIAL)


# ---------------------------------------------------------------------------
# X / Twitter cards (1600x900)
# ---------------------------------------------------------------------------

def x_card_01() -> str:
    b = f"""
    {eyebrow("AI agent evals")}
    {stat("74-78%", "SWE-bench Verified capability score")}
    {title("A high benchmark score is not production readiness.")}
    {source()}"""
    return page(1600, 900, b, scale=XCARD)


def x_card_02() -> str:
    b = f"""
    {eyebrow("Behavior gap")}
    {quote("The answer is polished. The trace is empty.")}
    <div class="card" style="background:var(--bg);">
      {bar("Final answer looks correct", 92, "passes", "ok")}
      {bar("Behavior trace honored", 38, "fails", "warn")}
    </div>
    {source("Source: AI agent evals failure taxonomy.")}"""
    return page(1600, 900, b, scale=XCARD)


def x_card_03() -> str:
    b = f"""
    {eyebrow("The Sourdough Test")}
    {title("Catch persona drift after every model update")}
    <div class="grid two" style="align-items:center;">
      {metric("3 of 8", "agents failed the behavior contract after a model update", "warn")}
      {body("Same prompts, new model — and three agents quietly stopped following their persona rules.")}
    </div>
    {source("Source: first-party implementation — 3 of 8 agents regressed.")}"""
    return page(1600, 900, b, scale=XCARD)


def x_card_04() -> str:
    b = f"""
    {eyebrow("Shift left")}
    {title("Production evals belong in CI")}
    {flow([("1","Pull request opened",""),
           ("2","Behavior eval suite runs","accent"),
           ("3","Regression blocks the merge","warn")])}
    {source("Source: AI agent evals implementation pattern.")}"""
    return page(1600, 900, b, scale=XCARD)


# ---------------------------------------------------------------------------
# Article-embedded figures (inline scale)
# ---------------------------------------------------------------------------

def medium_hero() -> str:
    b = f"""
    {eyebrow("AI agent evals for production readiness")}
    {title("Benchmarks prove capability. Production evals prove behavior.")}
    <div class="card" style="background:var(--bg); gap:22px;">
      {bar("Capability — SWE-bench Verified", 76, "74-78%", "")}
      {bar("Behavior — real PR acceptance", 42, "35-50%", "warn")}
    </div>
    {source()}"""
    return page(1400, 800, b, scale=INLINE)


def medium_inline_01() -> str:
    b = f"""
    {eyebrow("Where failures hide")}
    {title("Behavior gaps hide in the trace")}
    {checklist([("ok","Expected tool call fired"),
                ("warn","Required confirmation gate skipped"),
                ("ok","Refusal boundary held")])}
    {body("The final answer can read perfectly while a step in the trace was silently skipped.")}
    {source("Source: AI agent evals failure taxonomy.")}"""
    return page(1200, 800, b, scale=INLINE)


def medium_inline_02() -> str:
    b = f"""
    {eyebrow("The CI eval system")}
    {title("Four layers, one release gate")}
    {flow([("1","Tasks — real workflows",""),
           ("2","Graders — behavior + tool calls","accent"),
           ("3","CI gate — block regressions","accent"),
           ("4","History — drift over time","ok")])}
    {source("Source: first-party AI agent evals implementation pattern.")}"""
    return page(1200, 800, b, scale=INLINE)


def substack_hero() -> str:
    b = f"""
    {eyebrow("AI agent evals")}
    {title("Stop treating SWE-bench like a ship gate")}
    <div class="grid two">
      {metric("74-78%", "SWE-bench Verified capability", "accent")}
      {metric("35-50%", "real PR acceptance estimate", "warn")}
    </div>
    {source()}"""
    return page(1200, 630, b, scale=INLINE)


def linkedin_exhibit_01() -> str:
    b = f"""
    {eyebrow("Capability vs. behavior")}
    {title("Capability benchmarks leave a production-behavior gap")}
    <div class="card" style="background:var(--bg); gap:20px;">
      {bar("SWE-bench Verified (capability)", 76, "74-78%", "")}
      {bar("Real PR acceptance (behavior)", 42, "35-50%", "warn")}
    </div>
    {source()}"""
    return page(1200, 627, b, scale=INLINE)


def linkedin_exhibit_02() -> str:
    b = f"""
    {eyebrow("Eval economics")}
    {title("A small eval factory runs at pull-request speed")}
    <div class="grid three">
      {metric("$3-8", "per eval run", "accent")}
      {metric("200-400K", "tokens per run", "purple")}
      {metric("15-25m", "parallel runtime", "warn")}
    </div>
    {source("Source: first-party implementation — $3-8/run, 200-400K tokens, 15-25 min.")}"""
    return page(1200, 627, b, scale=INLINE)


ASSETS = {
    "slide-01-hook": slide_01, "slide-02-promise": slide_02, "slide-03-problem": slide_03,
    "slide-04-framework": slide_04, "slide-05-step1": slide_05, "slide-06-step2": slide_06,
    "slide-07-step3": slide_07, "slide-08-interrupt": slide_08, "slide-09-recap": slide_09,
    "slide-10-cta": slide_10,
    "x-card-01": x_card_01, "x-card-02": x_card_02, "x-card-03": x_card_03, "x-card-04": x_card_04,
    "medium-hero": medium_hero, "medium-inline-01": medium_inline_01,
    "medium-inline-02": medium_inline_02, "substack-hero": substack_hero,
    "linkedin-exhibit-01": linkedin_exhibit_01, "linkedin-exhibit-02": linkedin_exhibit_02,
}


def main() -> None:
    docs = {name: fn() for name, fn in ASSETS.items()}
    html_paths = []
    for name, doc in docs.items():
        hp = OUT / f"{name}.html"
        hp.write_text(doc, encoding="utf-8")
        html_paths.append(hp)
    if not inspect_files(html_paths):
        raise SystemExit("Inspector FAILED — fix before rendering.")
    render_many([(docs[name], OUT / f"{name}.png") for name in docs])
    print(f"Rendered {len(docs)} practitioner assets.")


if __name__ == "__main__":
    main()
