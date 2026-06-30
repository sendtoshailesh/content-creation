"""Render the 4 blog companion visuals for ``content/postgresql-18-skip-scan.md``.

Design tokens only; Helvetica Neue; 320 DPI; ASCII glyphs only. Each visual uses
a different theme + a distinct composition (ladder, bar tax, EXPLAIN flip,
decision checklist) per visual-standards diversity rules.

Run from repo root:  PYTHONPATH=. python3 content/visuals/render_skip_scan.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from scripts.visuals.tokens import BASE_TOKENS, THEMES

OUT = Path(__file__).resolve().parent
DPI = 320
FONT = ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans", "sans-serif"]


def T(name):
    plt.rcParams["font.family"] = FONT
    return {**BASE_TOKENS, **THEMES[name]}


def _box(ax, x, y, w, h, fc, ec, text, tc, fs, weight="bold"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
                                fc=fc, ec=ec, lw=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=tc,
            fontsize=fs, fontweight=weight, wrap=True)


def index_ladder():
    t = T("default")
    fig, axes = plt.subplots(1, 2, figsize=(12, 6.5))
    titles = ["PostgreSQL <= 17", "PostgreSQL 18  (skip scan)"]
    for ax, title in zip(axes, titles):
        ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
        ax.text(5, 9.4, title, ha="center", fontsize=17, fontweight="bold", color=t["TEXT"])
    a = axes[0]
    _box(a, 1, 6.5, 8, 1.4, t["BLUE_BG"], t["ACCENT"], "idx (tenant_id, status)", t["TEXT"], 15)
    _box(a, 1, 4.4, 8, 1.4, t["RED_BG"], t["WARN"], "idx_status   <- redundant", t["WARN"], 15)
    a.text(5, 2.6, "2 indexes to keep + maintain", ha="center", fontsize=14, color=t["TEXT_2"])
    a.text(5, 1.6, "filter on status -> needed a 2nd index", ha="center", fontsize=12, color=t["MUTED"])
    b = axes[1]
    _box(b, 1, 6.5, 8, 1.4, t["BLUE_BG"], t["ACCENT"], "idx (tenant_id, status)", t["TEXT"], 15)
    _box(b, 1, 4.4, 8, 1.4, "#ffffff", t["MUTED"], "idx_status   [DROPPED]", t["MUTED"], 15, "normal")
    b.text(5, 2.6, "1 index covers both -> faster writes", ha="center", fontsize=14, color=t["SUCCESS"], fontweight="bold")
    b.text(5, 1.6, "status-only query uses skip scan", ha="center", fontsize=12, color=t["MUTED"])
    fig.suptitle("Skip scan reuses the multicolumn index, so the duplicate goes",
                 fontsize=18, fontweight="bold", color=t["TEXT"], y=0.99)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT / "pg-01-index-ladder.png", dpi=DPI, facecolor=t["BG"]); plt.close(fig)


def write_tax():
    t = T("sunset")
    fig, ax = plt.subplots(figsize=(12, 6.5))
    n = [1, 2, 3, 4, 5]; cost = [100, 200, 300, 400, 500]
    bars = ax.bar([str(x) for x in n], cost, color=t["ACCENT"], width=0.6)
    bars[4].set_color(t["WARN"]); bars[3].set_color(t["SUCCESS"])
    ax.set_xlabel("Indexes on the table", fontsize=14, color=t["TEXT"])
    ax.set_ylabel("Relative write maintenance cost", fontsize=14, color=t["TEXT"])
    ax.set_title("Every index is a write tax: drop one, pay less on each INSERT/UPDATE/DELETE",
                 fontsize=15, fontweight="bold", color=t["TEXT"], pad=14)
    ax.annotate("drop redundant\nindex -> 5 to 4", xy=(3, 400), xytext=(2.1, 470),
                fontsize=12, fontweight="bold", color=t["SUCCESS"],
                arrowprops=dict(arrowstyle="->", color=t["SUCCESS"], lw=2))
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.tick_params(colors=t["TEXT_2"])
    fig.tight_layout(); fig.savefig(OUT / "pg-02-write-tax.png", dpi=DPI, facecolor=t["BG"]); plt.close(fig)


def explain_flip():
    t = T("ocean")
    fig, ax = plt.subplots(figsize=(12, 6.5)); ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.text(5, 9.4, "Same query, no new index -> the plan flips", ha="center", fontsize=17, fontweight="bold", color=t["TEXT"])
    _box(ax, 0.6, 5.2, 8.8, 2.6, t["RED_BG"], t["WARN"],
         "PG 17:  Seq Scan on orders\nFilter: status = 'failed'", t["TEXT"], 14)
    _box(ax, 0.6, 1.4, 8.8, 2.6, t["TEAL_BG"], t["SUCCESS"],
         "PG 18:  Index Only Scan (skip scan)\nusing orders_tenant_status_idx", t["TEXT"], 14)
    ax.add_patch(FancyArrowPatch((5, 5.0), (5, 4.1), arrowstyle="-|>", mutation_scale=28, color=t["ACCENT"], lw=3))
    ax.text(5.4, 4.55, "DROP INDEX idx_status", ha="left", fontsize=11, color=t["ACCENT_3"], fontweight="bold")
    fig.tight_layout(); fig.savefig(OUT / "pg-03-explain-flip.png", dpi=DPI, facecolor=t["BG"]); plt.close(fig)


def checklist():
    t = T("forest")
    fig, ax = plt.subplots(figsize=(12, 6.5)); ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.text(5, 9.4, "When skip scan lets you drop an index", ha="center", fontsize=18, fontweight="bold", color=t["TEXT"])
    rows = [("[x]", "Leading column is low-cardinality (few tenants/statuses)", t["SUCCESS"]),
            ("[x]", "A single-col index duplicates a wider index's column", t["SUCCESS"]),
            ("[x]", "On 18, EXPLAIN shows skip scan + acceptable latency", t["SUCCESS"]),
            ("[ ]", "Leading column high-cardinality -> keep targeted index", t["WARN"]),
            ("[ ]", "Test DROP INDEX CONCURRENTLY on a replica first", t["TEXT_2"])]
    for i, (m, txt, c) in enumerate(rows):
        y = 7.6 - i * 1.35
        _box(ax, 0.6, y, 0.9, 1.0, t["LIGHT_BG"], c, m, c, 16)
        ax.text(1.8, y + 0.5, txt, ha="left", va="center", fontsize=14, color=t["TEXT"])
    fig.tight_layout(); fig.savefig(OUT / "pg-04-checklist.png", dpi=DPI, facecolor=t["BG"]); plt.close(fig)


if __name__ == "__main__":
    index_ladder(); write_tax(); explain_flip(); checklist()
    print("rendered: pg-01..pg-04")
