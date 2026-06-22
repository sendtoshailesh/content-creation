"""Practitioner carousel pack — "How AI Actually Helps You Fix PostgreSQL
Performance Problems (and Where It Lies)".

9 square (1080x1080) LinkedIn carousel slides, authored as HTML/CSS via the
shared design system, gated by the DOM inspector, then rasterized with
Chromium at device scale 2 (retina-crisp 2160x2160 px PNGs of a 1080x1080
layout).

One cohesive theme across the whole deck (ocean) + brand design tokens.
No gauges/arcs — magnitude is shown with horizontal bars. At most one focal
"display" number per slide. No baked-in slide counters.

Run:
    .venv/bin/python content/visuals/distilled/postgresql-practitioner/render_distilled.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from scripts.visuals.html.components import (  # noqa: E402
    bar, body, checklist, eyebrow, flow, gap_callout, grid, metric,
    source, stat, subtitle, title,
)
from scripts.visuals.html.design import esc, page  # noqa: E402
from scripts.visuals.html.inspect import inspect_files  # noqa: E402
from scripts.visuals.html.render import render_many  # noqa: E402

OUT = Path(__file__).resolve().parent

# One cohesive theme across the deck (Postgres-blue family).
THEME = "ocean"
# Full-screen social square. Tuned for legibility without overflow in 1080x1080.
SCALE = 1.55
SQUARE = 1080


# --- small inline helpers ----------------------------------------------------

def ground_card(n: str, artifact: str, note: str) -> str:
    """A numbered grounding-input row: accent badge + artifact + what it carries."""
    return f"""
    <div class="card accent" style="flex-direction:row; align-items:center;
         gap:calc(18px*var(--scale)); padding:calc(18px*var(--scale)) calc(24px*var(--scale));">
      <span class="badge">{esc(n)}</span>
      <div style="display:flex; flex-direction:column; gap:calc(4px*var(--scale));">
        <span data-role="label" style="font-family:'SFMono-Regular',Menlo,Consolas,monospace;">{esc(artifact)}</span>
        <span data-role="body">{esc(note)}</span>
      </div>
    </div>"""


def score_row(capability: str, rating: str, kind: str) -> str:
    """A scorecard row: capability label + a colored rating tag.

    kind in {ok, warn, low}. 'low' uses an outlined caution treatment so it
    reads as distinct from 'warn' (medium) while staying inside the palette.
    """
    if kind == "low":
        tag_style = ("background:var(--red-bg); color:var(--warn); "
                     "border:2px solid var(--warn);")
    elif kind == "warn":
        tag_style = "background:var(--warn); color:#fff;"
    else:  # ok
        tag_style = "background:var(--success); color:#fff;"
    return f"""
    <div class="card" style="flex-direction:row; align-items:center; justify-content:space-between;
         gap:calc(18px*var(--scale)); padding:calc(13px*var(--scale)) calc(26px*var(--scale));">
      <span data-role="label">{esc(capability)}</span>
      <span data-role="label" style="{tag_style} padding:calc(6px*var(--scale)) calc(20px*var(--scale));
            border-radius:999px; white-space:nowrap; letter-spacing:0.04em;">{esc(rating)}</span>
    </div>"""


# --- slides ------------------------------------------------------------------

def slide_01_hook() -> str:
    b = f"""
    {eyebrow("AI + PostgreSQL performance")}
    {title("AI won't fix your Postgres performance.")}
    {stat("10x", "It just makes you faster at finding the fix.")}
    {source("A DBA's field guide — what helps, and where AI lies.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


def slide_02_trap() -> str:
    b = f"""
    {eyebrow("The trap")}
    {title("An LLM can't see your database")}
    {subtitle("Text-to-SQL accuracy on 95 real, messy databases (BIRD benchmark).")}
    <div class="card" style="background:var(--bg); gap:calc(18px*var(--scale));
         --bar-label-w:300px; --bar-value-w:200px;">
      {bar("GPT-4 (best case)", 55, "54.89%", "warn")}
      {bar("Expert humans", 93, "92.96%", "ok")}
    </div>
    {gap_callout("~38 pts", "Grounding is everything — feed it your real stats.")}
    {source("Source: BIRD text-to-SQL benchmark (bird-bench.github.io), 2024.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


def slide_03_rule() -> str:
    b = f"""
    {eyebrow("The rule")}
    {title("Ground every prompt that matters")}
    <div style="display:flex; flex-direction:column; gap:calc(14px*var(--scale));">
      {ground_card("1", "EXPLAIN (ANALYZE, BUFFERS)", "Actual rows, timings, buffer hits — not estimates.")}
      {ground_card("2", "pg_stat_statements", "calls, mean_exec_time, rows for the real workload.")}
      {ground_card("3", "version() + non-default settings", "So advice matches your Postgres, not the internet's.")}
    </div>
    {source("Withhold these and you're just autocompleting Stack Overflow.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


def slide_04_matrix() -> str:
    b = f"""
    {eyebrow("Where AI helps")}
    {title("The value is wildly uneven")}
    <div style="display:flex; flex-direction:column; gap:calc(12px*var(--scale));">
      {score_row("Triage & summarize", "HIGH", "ok")}
      {score_row("Read query plans", "HIGH", "ok")}
      {score_row("Index / rewrite advice", "MEDIUM", "warn")}
      {score_row("Anomaly detection (ML)", "HIGH", "ok")}
      {score_row("Internals & DDL", "LOW", "low")}
    </div>
    {body("Medium = validate every suggestion. Low = keep a human on every lock.")}
    {source("Map of where AI helps across the Postgres performance workflow.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


def slide_05_example() -> str:
    b = f"""
    {eyebrow("Real example · composite index")}
    {title("A missing composite index, found fast")}
    <div class="card" style="background:var(--bg); gap:calc(18px*var(--scale));
         --bar-label-w:300px; --bar-value-w:230px;">
      {bar("Before — seq scan + sort", 100, "4,200 ms", "warn")}
      {bar("After — composite index", 8, "38 ms", "ok")}
    </div>
    {gap_callout("~110x", "faster — validated with hypopg before CREATE INDEX CONCURRENTLY.")}
    {source("Illustrative of a composite-index win; mechanism, SQL & tools are real.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


def slide_06_autovacuum() -> str:
    cards = [
        metric("0.2", "Default scale_factor — too high on large, hot tables.", "warn"),
        metric("0.02", "Your tuned per-table value — then watch n_dead_tup.", "accent"),
    ]
    b = f"""
    {eyebrow("Autovacuum starvation")}
    {title("AI names the knob. You own the value.")}
    {subtitle("Dead tuples climbing? AI nails the mechanism: vacuum triggers at threshold + scale_factor x live rows.")}
    {grid(cards, "two")}
    {body("The mechanism is textbook. The value is workload-dependent — set it, watch, and tune from there.")}
    {source("Source: PostgreSQL docs — routine vacuuming.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


def slide_07_safe() -> str:
    b = f"""
    {eyebrow("Safe wiring")}
    {title("Connect AI to live stats, not the keys")}
    {checklist([
        ("ok", "Read-only role - SELECT on stats views, pg_monitor"),
        ("ok", "Postgres MCP for live stats (safe-SQL mode)"),
        ("warn", "Never auto-apply DDL - a human runs every change"),
        ("ok", "Validate with hypopg + a staging replica"),
    ])}
    {source("Postgres MCP Pro defaults to read-only; humans own anything that locks.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


def slide_08_playbook() -> str:
    b = f"""
    {eyebrow("The playbook")}
    {title("Six steps, every slow query")}
    <style>#stage .flow .connector{{height:calc(8px*var(--scale));}}
    #stage .flow > .card{{padding:calc(9px*var(--scale)) calc(22px*var(--scale));}}
    #stage .flow .badge{{min-width:calc(var(--fs-label)*1.7); height:calc(var(--fs-label)*1.7);}}</style>
    {flow([("1", "Ground", ""),
           ("2", "Triage", "accent"),
           ("3", "Hypothesize", "accent"),
           ("4", "Validate", "accent"),
           ("5", "Apply", "accent"),
           ("6", "Measure", "ok")])}
    {source("AI took the slow parts. It did not take the judgment.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


def slide_09_cta() -> str:
    b = f"""
    {eyebrow("Read the full field guide")}
    {title("Grounded prompts. Validated changes.")}
    {subtitle("That single habit is the whole difference between AI that helps and AI that pages you at 2 a.m.")}
    <div class="card accent" style="align-items:center; text-align:center; gap:calc(8px*var(--scale));">
      <span data-role="body" style="color:var(--accent); font-weight:700;">sendtoshailesh.github.io/blog/ai-postgresql-performance.html</span>
    </div>
    {body("Follow for the next one: grounding LLMs on live Postgres stats with MCP.")}
    {source("sendtoshailesh.github.io - a DBA's field guide.")}"""
    return page(SQUARE, SQUARE, b, theme=THEME, scale=SCALE)


ASSETS = {
    "slide-01-hook": slide_01_hook,
    "slide-02-trap": slide_02_trap,
    "slide-03-rule": slide_03_rule,
    "slide-04-matrix": slide_04_matrix,
    "slide-05-example": slide_05_example,
    "slide-06-autovacuum": slide_06_autovacuum,
    "slide-07-safe-wiring": slide_07_safe,
    "slide-08-playbook": slide_08_playbook,
    "slide-09-cta": slide_09_cta,
}


def main() -> None:
    docs = {name: fn() for name, fn in ASSETS.items()}
    html_paths = []
    for name, doc in docs.items():
        hp = OUT / f"{name}.html"
        hp.write_text(doc, encoding="utf-8")
        html_paths.append(hp)
    if not inspect_files(html_paths):
        raise SystemExit("Inspector FAILED - fix before rendering.")
    render_many([(docs[name], OUT / f"{name}.png") for name in docs])
    print(f"Rendered {len(docs)} carousel slides at {SQUARE}x{SQUARE} (scale {SCALE}, @2x).")


if __name__ == "__main__":
    main()
