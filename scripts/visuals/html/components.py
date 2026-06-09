"""Reusable HTML component builders for the visual design system.

Every text node carries a ``data-role`` so the QA inspector can validate its
size. Import these from asset renderers instead of hand-writing markup, so the
whole pack stays consistent.
"""

from __future__ import annotations

from scripts.visuals.html.design import esc

DEFAULT_SRC = "Sources: SWE-bench Verified; aggregated production PR-acceptance reports (2026)."


def eyebrow(text: str) -> str:
    return f'<div class="eyebrow" data-role="caption">{esc(text)}</div>'


def title(text: str) -> str:
    return f'<div data-role="title">{esc(text)}</div>'


def subtitle(text: str) -> str:
    return f'<div data-role="subtitle">{esc(text)}</div>'


def body(text: str) -> str:
    return f'<div data-role="body">{esc(text)}</div>'


def quote(text: str) -> str:
    return f'<div class="quote" data-role="title">{esc(text)}</div>'


def source(text: str = DEFAULT_SRC) -> str:
    return f'<div class="source" data-role="caption">{esc(text)}</div>'


def stat(num: str, label: str, kind: str = "accent") -> str:
    """One focal number (display size). Use at most one per asset."""
    return (f'<div class="stat {kind}"><div class="stat-num" data-role="display">{esc(num)}</div>'
            f'<div data-role="label">{esc(label)}</div></div>')


def metric(num: str, label: str, kind: str) -> str:
    """Value-sized metric card. Safe to place several side by side."""
    return (f'<div class="metric {kind}"><div class="m-num" data-role="value">{esc(num)}</div>'
            f'<div data-role="body">{esc(label)}</div></div>')


def bar(label: str, pct: int, value: str, kind: str = "") -> str:
    color = "accent" if kind == "" else kind
    return f"""
    <div class="bar-row">
      <div class="bar-label" data-role="label">{esc(label)}</div>
      <div class="bar-track"><div class="bar-fill {kind}" style="width:{pct}%"></div></div>
      <div class="bar-value" data-role="value" style="color:var(--{color})">{esc(value)}</div>
    </div>"""


def gap_callout(num: str, text: str) -> str:
    return (f'<div class="gap-callout"><span class="gap-num" data-role="value">{esc(num)}</span>'
            f'<span data-role="label">{esc(text)}</span></div>')


def flow(steps: list[tuple[str, str, str]]) -> str:
    """Vertical numbered flow. steps = [(n, label, kind)] kind in {'', accent, ok, warn}."""
    parts = []
    for i, (n, text, kind) in enumerate(steps):
        bk = "ok" if kind == "ok" else ("warn" if kind == "warn" else "")
        parts.append(f"""
      <div class="card {kind}" style="padding:calc(16px*var(--scale)) calc(22px*var(--scale)); flex:0 0 auto;">
        <div style="display:flex; align-items:center; gap:calc(14px*var(--scale));">
          <span class="badge {bk}">{esc(n)}</span>
          <span data-role="label">{esc(text)}</span>
        </div>
      </div>""")
        if i < len(steps) - 1:
            parts.append('<div class="connector"></div>')
    return f'<div class="flow" style="flex:0 0 auto; gap:0;">{"".join(parts)}</div>'


def checklist(items: list[tuple[str, str]]) -> str:
    """items = [(state, label)] where state in {ok, warn}."""
    rows = []
    for state, label in items:
        mark = "[x]" if state == "ok" else "[ ]"
        bk = "ok" if state == "ok" else "warn"
        cls = "ok" if state == "ok" else "warn"
        rows.append(f"""
      <div class="card {cls}" style="flex-direction:row; align-items:center; gap:calc(14px*var(--scale)); padding:calc(14px*var(--scale)) calc(22px*var(--scale));">
        <span class="badge {bk}" style="font-family:monospace;">{esc(mark)}</span>
        <span data-role="label">{esc(label)}</span>
      </div>""")
    return f'<div style="display:flex; flex-direction:column; gap:calc(12px*var(--scale));">{"".join(rows)}</div>'


def grid(cards: list[str], cols: str = "two") -> str:
    return f'<div class="grid {cols}">{"".join(cards)}</div>'
