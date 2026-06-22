"""HTML/CSS + Chromium pack for the PostgreSQL performance post.

Renders the two diagram-family assets:
  * loop-diagram.png    — diagnose-to-fix flow (old vs AI-assisted), V2
  * ai-help-matrix.png  — where AI helps with Postgres perf, V3

Each asset is authored with the shared design system (design.css / components),
gated by the DOM inspector, then rasterized via Chromium at device scale 2.

    python3 content/topics/postgresql/visuals/render_html_pack.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from scripts.visuals.html.components import eyebrow, source, title  # noqa: E402
from scripts.visuals.html.design import esc, page  # noqa: E402
from scripts.visuals.html.inspect import inspect_files  # noqa: E402
from scripts.visuals.html.render import render_many  # noqa: E402

OUT = Path(__file__).resolve().parent
INLINE = 1.0  # article-proportionate type


# ---------------------------------------------------------------------------
# V2 — Diagnose-to-fix loop (two stacked horizontal flow lanes)
# ---------------------------------------------------------------------------

FLOW_CSS = """
<style>
.lanes { display:flex; flex-direction:column; gap: calc(28px*var(--scale)); }
.lane { display:flex; align-items:stretch; gap: calc(22px*var(--scale)); }
.row-label {
  flex: 0 0 calc(176px*var(--scale));
  display:flex; flex-direction:column; justify-content:center;
  gap: calc(2px*var(--scale));
  padding: calc(16px*var(--scale)) calc(22px*var(--scale));
  border-radius: calc(14px*var(--scale));
  background: var(--light);
  border-left: 6px solid var(--muted);
}
.row-label.warn { border-left-color: var(--warn); background: var(--red-bg); }
.row-label.ok   { border-left-color: var(--success); background: var(--teal-bg); }

.flow.horiz { flex-direction: row; align-items: stretch; gap:0; flex:1 1 auto; }
.flow.horiz > .card {
  flex:1 1 0; justify-content:center; align-items:center; text-align:center;
  padding: calc(16px*var(--scale)) calc(12px*var(--scale)); gap: calc(3px*var(--scale));
}
.flow.horiz .card.accent { background: var(--blue-bg); border-color: var(--accent); }
.flow.horiz .card.ok     { background: var(--teal-bg); border-color: var(--success); }
.flow.horiz .card.warn   { background: var(--red-bg);  border-color: var(--warn); }

.flow.horiz .connector {
  align-self:center; flex:0 0 auto;
  width: calc(38px*var(--scale)); height:3px;
  border:none; background: var(--accent); position:relative;
}
.flow.horiz .connector::after {
  content:""; position:absolute; left:auto; bottom:auto; right:-1px; top:50%;
  width:11px; height:11px;
  border-left:none; border-top:none;
  border-right:3px solid var(--accent); border-bottom:3px solid var(--accent);
  transform: translateY(-50%) rotate(-45deg);
}
.flow.horiz.warn .connector { background: var(--warn); }
.flow.horiz.warn .connector::after { border-right-color: var(--warn); border-bottom-color: var(--warn); }
</style>
"""


def _hcard(label: str, sub: str | None = None, kind: str = "") -> str:
    sub_html = f'<div data-role="caption">{esc(sub)}</div>' if sub else ""
    return f'<div class="card {kind}"><div data-role="label">{esc(label)}</div>{sub_html}</div>'


def _hflow(cards: list[str], warn: bool = False) -> str:
    parts: list[str] = []
    for i, c in enumerate(cards):
        parts.append(c)
        if i < len(cards) - 1:
            parts.append('<div class="connector"></div>')
    cls = "flow horiz warn" if warn else "flow horiz"
    return f'<div class="{cls}">{"".join(parts)}</div>'


def _lane_label(name: str, time: str, kind: str) -> str:
    color = {"warn": "var(--warn)", "ok": "var(--success)"}.get(kind, "var(--text)")
    return (
        f'<div class="row-label {kind}">'
        f'<div data-role="label">{esc(name)}</div>'
        f'<div data-role="value" style="color:{color}">{esc(time)}</div>'
        f"</div>"
    )


def loop_diagram() -> str:
    old_lane = _hflow(
        [
            _hcard("grep logs", "scan errors"),
            _hcard("EXPLAIN", "read plan"),
            _hcard("guess", "try a change"),
            _hcard("repeat", "back to logs", kind="warn"),
        ],
        warn=True,
    )
    ai_lane = _hflow(
        [
            _hcard("ground", "EXPLAIN + stats", kind="accent"),
            _hcard("triage", "rank by cost"),
            _hcard("suggest", "index / rewrite"),
            _hcard("validate", "hypopg"),
            _hcard("measure", "confirm win", kind="ok"),
        ]
    )
    b = f"""
    {FLOW_CSS}
    {eyebrow("PostgreSQL performance")}
    {title("The diagnose-to-fix loop")}
    <div class="lanes">
      <div class="lane">
        {_lane_label("Old loop", "~1 hour", "warn")}
        {old_lane}
      </div>
      <div class="lane">
        {_lane_label("AI-assisted loop", "minutes", "ok")}
        {ai_lane}
      </div>
    </div>
    {source("Illustrative diagnose-to-fix workflow; AI-assisted path lands on a measured win.")}"""
    return page(1400, 720, b, theme="default", pad=52, scale=INLINE)


# ---------------------------------------------------------------------------
# V3 — Where AI helps with Postgres performance (comparison matrix)
# ---------------------------------------------------------------------------

MATRIX_CSS = """
<style>
.matrix {
  display:grid; grid-template-columns: 1.75fr 0.85fr 1.25fr; gap:0;
  border:1px solid var(--grid); border-radius: calc(16px*var(--scale)); overflow:hidden;
}
.matrix .cell {
  padding: calc(18px*var(--scale)) calc(22px*var(--scale));
  display:flex; align-items:center;
  border-bottom:1px solid var(--grid);
}
.matrix .head { background: var(--light); border-bottom:2px solid var(--grid); }
.matrix .row-odd .cell { background: var(--bg); }
.matrix .row-even .cell { background: var(--light); }
.matrix .last { border-bottom:none; }

.pill {
  display:inline-flex; align-items:center; justify-content:center;
  padding: calc(8px*var(--scale)) calc(20px*var(--scale)); border-radius:999px;
  color:#fff; white-space:nowrap;
}
.pill.ok  { background: var(--success); }
.pill.mid { background: var(--accent); }
.pill.low { background: var(--warn); }

.human { display:flex; align-items:center; gap: calc(12px*var(--scale)); }
.dot { width: calc(13px*var(--scale)); height: calc(13px*var(--scale));
  border-radius:999px; flex:0 0 auto; }
.dot.warn{background:var(--warn);} .dot.accent{background:var(--accent);}
.dot.muted{background:var(--muted);} .dot.ok{background:var(--success);}
</style>
"""

# (step, ai_value_text, ai_value_kind, human_text, human_dot)
MATRIX_ROWS = [
    ("Triage & summarize pg_stat_statements / Performance Insights",
     "High", "ok", "Optional", "muted"),
    ("Read EXPLAIN plans in plain English",
     "High", "ok", "Yes — verify ANALYZE", "accent"),
    ("Index & query-rewrite suggestions",
     "Medium", "mid", "Yes — validate with hypopg", "accent"),
    ("Anomaly detection (DevOps Guru for RDS, pganalyze)",
     "High", "ok", "Mostly automated", "ok"),
    ('Internals, DDL, "just run this"',
     "Low / risky", "low", "Always", "warn"),
]


def _head_cell(text: str) -> str:
    return (f'<div class="cell head"><span class="eyebrow" data-role="caption">'
            f'{esc(text)}</span></div>')


def ai_help_matrix() -> str:
    cells: list[str] = [
        _head_cell("Workflow step"),
        _head_cell("AI value"),
        _head_cell("Keep a human in front?"),
    ]
    n = len(MATRIX_ROWS)
    for i, (step, val, kind, human, dot) in enumerate(MATRIX_ROWS):
        parity = "row-odd" if i % 2 == 0 else "row-even"
        last = " last" if i == n - 1 else ""
        cells.append(
            f'<div class="cell step {parity}{last}">'
            f'<span data-role="label">{esc(step)}</span></div>'
        )
        cells.append(
            f'<div class="cell {parity}{last}">'
            f'<span class="pill {kind}" data-role="label">{esc(val)}</span></div>'
        )
        cells.append(
            f'<div class="cell {parity}{last}"><span class="human">'
            f'<span class="dot {dot}"></span>'
            f'<span data-role="body">{esc(human)}</span></span></div>'
        )

    b = f"""
    {MATRIX_CSS}
    {eyebrow("Tool fit")}
    {title("Where AI helps with Postgres performance \u2014 and where it doesn't")}
    <div class="matrix">{''.join(cells)}</div>
    {source("Pill = current AI value (High / Medium / Low). Keep a human in front wherever correctness or safety is at stake.")}"""
    return page(1340, 880, b, theme="ocean", pad=52, scale=INLINE)


ASSETS = {
    "loop-diagram": loop_diagram,
    "ai-help-matrix": ai_help_matrix,
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
    print(f"Rendered {len(docs)} HTML assets to {OUT}")


if __name__ == "__main__":
    main()
