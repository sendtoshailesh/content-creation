"""Base distilled pack — built on the HTML/CSS + Chromium engine.

Covers the in-article figures (exhibit, one-pager) and the five LinkedIn
carousel cards. The comic (illustration) stays in the Pillow renderer.
All assets author HTML via the shared design system, pass the DOM inspector,
then rasterize. Run:

    python3 content/visuals/distilled/agent-eval-visual-first/render_html_pack.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from scripts.visuals.html.components import (  # noqa: E402
    bar, body, checklist, eyebrow, flow, gap_callout, grid, metric,
    source, subtitle, title,
)
from scripts.visuals.html.design import page  # noqa: E402
from scripts.visuals.html.inspect import inspect_files  # noqa: E402
from scripts.visuals.html.render import render_many  # noqa: E402

OUT = Path(__file__).resolve().parent
CARD = 1.45    # 1080x1350 LinkedIn carousel cards
INLINE = 1.0   # article-embedded figures


# --- In-article figures -----------------------------------------------------

def exhibit_benchmark_gap() -> str:
    b = f"""
    {eyebrow("Capability vs. behavior")}
    {title("A high benchmark score is not production reliability")}
    <div class="card" style="gap:22px; background:var(--bg);">
      {bar("SWE-bench Verified (capability)", 76, "74-78%", "")}
      {bar("Real PR acceptance (behavior)", 42, "35-50%", "warn")}
    </div>
    {gap_callout("~30 pts", "Behavior gap: what a model can do is not what it reliably does in production.")}
    {source()}"""
    return page(1200, 627, b, pad=48, scale=INLINE)


def one_page_eval_system() -> str:
    b = f"""
    {eyebrow("Production eval system")}
    {title("From benchmark scores to a release gate")}
    {flow([("1", "Define the behavior contract", ""),
           ("2", "Build a real-task eval set", "accent"),
           ("3", "Grade behavior, not just answers", "accent"),
           ("4", "Gate every release in CI", "ok")])}
    {body("Four steps to catch silent failures before your users do.")}
    {source()}"""
    return page(1080, 1350, b, scale=INLINE)


# --- LinkedIn carousel cards (1080x1350) ------------------------------------

def card_01_hook() -> str:
    b = f"""
    {eyebrow("AI agent evals")}
    {title("SWE-bench is not your production eval")}
    {subtitle("A high capability signal can still leave a behavior gap.")}
    <div class="card" style="background:var(--bg); gap:calc(18px*var(--scale));">
      {bar("Capability — SWE-bench Verified", 76, "74-78%", "")}
      {bar("Behavior — real PR acceptance", 42, "35-50%", "warn")}
    </div>
    {gap_callout("~30 pts", "The behavior gap is what benchmarks never measure.")}
    {source()}"""
    return page(1080, 1350, b, scale=CARD)


def card_02_problem() -> str:
    b = f"""
    {eyebrow("Fabrication without action")}
    {title("The failure looks successful")}
    {subtitle("The answer is polished. The trace tells the truth.")}
    <div class="card" style="background:var(--bg);">
      {body('Agent says: "I created the file and validated the schema."')}
    </div>
    {checklist([("warn", "No file-write tool call in the trace"),
                ("warn", "No schema-validation step ran"),
                ("ok", "Final answer reads as a clean success")])}
    {body("Production evals inspect behavior, not just the final text.")}
    {source("Source: AI agent evals failure taxonomy.")}"""
    return page(1080, 1350, b, scale=CARD)


def card_03_taxonomy() -> str:
    cards = [
        metric("No tool", "called when one was required", "warn"),
        metric("Wrong tool", "used for the task", "warn"),
        metric("Skipped gate", "confirmation bypassed", "warn"),
        metric("Persona drift", "stepped outside its role", "purple"),
        metric("Lost handoff", "context dropped between agents", "accent"),
        metric("Silent regress", "passed before, fails now", "warn"),
    ]
    b = f"""
    {eyebrow("What benchmarks miss")}
    {title("Behavior failures cluster around contracts")}
    {grid(cards, "two")}
    {source("Source: AI agent evals behavior taxonomy.")}"""
    return page(1080, 1350, b, scale=CARD)


def card_04_framework() -> str:
    b = f"""
    {eyebrow("A production eval is a gate")}
    {title("Tasks move through graders before release")}
    {flow([("1", "Task suite — real workflows", ""),
           ("2", "Graders — text + tools + judge", "accent"),
           ("3", "CI gate — pass or block", "warn"),
           ("4", "History — drift over time", "ok")])}
    {body("Run it on every PR that changes agents, prompts, tools, policies, or models.")}
    {source("Source: AI agent evals implementation pattern.")}"""
    return page(1080, 1350, b, scale=CARD)


def card_05_cta() -> str:
    rows = [
        metric("1. Risky agent", "Which agent can cause real damage?", "accent"),
        metric("2. Must do", "What tool or action must happen?", "accent"),
        metric("3. Must refuse", "What behavior is outside its scope?", "warn"),
    ]
    b = f"""
    {eyebrow("Write the first eval")}
    {title("Start with one risky agent and one boundary")}
    <div style="display:flex; flex-direction:column; gap:calc(16px*var(--scale));">{''.join(rows)}</div>
    {body("Ship-with question: what behavior must never regress?")}
    {source("Source: AI agent evals visual-first guide.")}"""
    return page(1080, 1350, b, scale=CARD)


ASSETS = {
    "exhibit-01-benchmark-gap": exhibit_benchmark_gap,
    "one-page-eval-system": one_page_eval_system,
    "linkedin-card-01-hook": card_01_hook,
    "linkedin-card-02-problem": card_02_problem,
    "linkedin-card-03-taxonomy": card_03_taxonomy,
    "linkedin-card-04-framework": card_04_framework,
    "linkedin-card-05-cta": card_05_cta,
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
    print(f"Rendered {len(docs)} base assets.")


if __name__ == "__main__":
    main()
