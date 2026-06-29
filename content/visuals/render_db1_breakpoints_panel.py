#!/usr/bin/env python3
"""Render db1-four-breakpoints-panel.png (v03, P0 — data-exhibit).

Four WARN-red walled cards in a 2x2 grid. Each card: the wall name, the ONE
ceiling number (hero figure), the specialist (primary), and a small Azure
secondary line. Specialists are first-class equals; Azure is one cloud's option,
rendered smaller and muted (never the default).

Grounding: content/reference-brief.md §C (vendor/self-reported figures).
ASCII glyphs only (matplotlib): '->' not arrows; no middle dots. 320 DPI.
Reproducible:

    python3 content/visuals/render_db1_breakpoints_panel.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# --- Shared design tokens (exact) -------------------------------------------
BG = "#ffffff"
ACCENT = "#1f6feb"
ACCENT_2 = "#0d9488"
ACCENT_3 = "#7c3aed"
WARN = "#dc2626"
SUCCESS = "#16a34a"
TEXT = "#1e293b"
TEXT_2 = "#475569"
MUTED = "#94a3b8"
GRID = "#e5e7eb"
LIGHT_BG = "#f8fafc"
RED_BG = "#fee2e2"
DPI = 320

plt.rcParams["font.family"] = "Helvetica Neue"
plt.rcParams["svg.fonttype"] = "none"

# Card content (from reference-brief.md §C). Each tuple:
# (wall_name, ceiling_hero, ceiling_sub, specialist, why_pg, azure_secondary)
CARDS = [
    (
        "1. Extreme write throughput",
        "7.5M inserts/sec",
        "@ 4 ms P99  (ScyllaDB, vendor; 2-5x Apache Cassandra)",
        "Cassandra / ScyllaDB",
        "Why not PG: a single primary funnels all writes through one node.",
        "Azure: Managed Cassandra / Cosmos DB",
    ),
    (
        "2. Planet-scale sharding",
        "ALL of YouTube, 5+ yrs",
        "Vitess ran YouTube's entire DB traffic (also Slack, Square, JD.com)",
        "Spanner / CockroachDB / Vitess",
        "Why not PG: no transparent native sharding -- you bolt it on.",
        "Azure: Cosmos DB / PostgreSQL Elastic Clusters",
    ),
    (
        "3. Sub-millisecond key-value",
        "single-digit ms",
        "500k+ req/s, 200 TB+, 99.999%  (DynamoDB, vendor)",
        "Redis / DynamoDB",
        "Why not PG: connection/transaction overhead can't hold that floor.",
        "Azure: Managed Redis / Cosmos DB",
    ),
    (
        "4. True OLAP at petabyte scale",
        "~1 billion rows/sec",
        "100M rows in 92 ms, ~7 GB/s per query  (ClickHouse)",
        "ClickHouse / Snowflake",
        "Why not PG: row-oriented OLTP can't match a column store's scan rate.",
        "Azure: Data Explorer (Kusto) / Fabric",
    ),
]


def wall_motif(ax, x, y, color):
    """Small ASCII-free brick wall motif drawn as little rectangles."""
    bw, bh, gap = 0.022, 0.012, 0.003
    for row in range(2):
        offset = (bw + gap) / 2 if row % 2 else 0
        for col in range(3):
            bx = x + offset + col * (bw + gap)
            by = y + row * (bh + gap)
            ax.add_patch(Rectangle((bx, by), bw, bh, facecolor=color,
                                   edgecolor="none", alpha=0.9,
                                   transform=ax.transAxes, zorder=6))


def draw_card(ax, card):
    name, hero, sub, specialist, why, azure = card
    # card background
    ax.add_patch(FancyBboxPatch(
        (0.04, 0.06), 0.92, 0.88,
        boxstyle="round,pad=0.012,rounding_size=0.03",
        facecolor=BG, edgecolor=GRID, linewidth=1.5,
        mutation_aspect=ax.bbox.height / ax.bbox.width,
        transform=ax.transAxes, zorder=2))
    # thick WARN-red top border bar
    ax.add_patch(Rectangle((0.04, 0.885), 0.92, 0.055, facecolor=WARN,
                           edgecolor="none", transform=ax.transAxes, zorder=4))
    # red wash strip behind the hero number
    ax.add_patch(Rectangle((0.04, 0.50), 0.92, 0.20, facecolor=RED_BG,
                           edgecolor="none", alpha=0.55,
                           transform=ax.transAxes, zorder=3))

    # wall motif + wall name (text label, not color-only)
    wall_motif(ax, 0.075, 0.905, "#ffffff")
    ax.text(0.20, 0.918, name, transform=ax.transAxes, fontsize=15.5,
            fontweight="bold", color="#ffffff", va="center", ha="left", zorder=7)

    # hero ceiling number
    ax.text(0.5, 0.625, hero, transform=ax.transAxes, fontsize=33,
            fontweight="bold", color=TEXT, va="center", ha="center", zorder=7)
    ax.text(0.5, 0.535, sub, transform=ax.transAxes, fontsize=11.5,
            color=TEXT_2, va="center", ha="center", zorder=7)

    # specialist (primary)
    ax.text(0.5, 0.40, specialist, transform=ax.transAxes, fontsize=19,
            fontweight="bold", color=ACCENT, va="center", ha="center", zorder=7)
    ax.text(0.5, 0.345, "the legitimate specialist exit", transform=ax.transAxes,
            fontsize=10.5, color=MUTED, va="center", ha="center", zorder=7)

    # why-not-postgres line
    ax.text(0.5, 0.235, why, transform=ax.transAxes, fontsize=11,
            color=TEXT_2, va="center", ha="center", zorder=7, wrap=True)

    # Azure secondary line (smaller, muted, clearly secondary)
    ax.text(0.5, 0.125, azure, transform=ax.transAxes, fontsize=10,
            color=MUTED, va="center", ha="center", zorder=7, style="italic")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")


def main() -> None:
    fig = plt.figure(figsize=(12.4, 9.4), dpi=DPI)
    fig.patch.set_facecolor(BG)

    # Header band
    fig.text(0.5, 0.955, "Where the belief stops -- the four walls",
             fontsize=27, fontweight="bold", color=TEXT, ha="center")
    fig.text(0.5, 0.918,
             "Four workloads where I leave Postgres on purpose -- each justified by one ceiling number.",
             fontsize=13.5, color=TEXT_2, ha="center")

    # 2x2 grid of cards
    gs = fig.add_gridspec(2, 2, left=0.035, right=0.965, top=0.875,
                          bottom=0.085, wspace=0.06, hspace=0.10)
    for i, card in enumerate(CARDS):
        ax = fig.add_subplot(gs[i // 2, i % 2])
        draw_card(ax, card)

    # Footer
    fig.text(0.035, 0.038,
             "Specialists are legitimate equals; Azure is one cloud's option among equals (AWS / GCP / "
             "self-hosted equally valid).",
             fontsize=10.5, color=TEXT_2, ha="left")
    fig.text(0.035, 0.015,
             "Vendor / self-reported figures. Source: reference-brief.md C; verified 2026-06-26.",
             fontsize=10, color=MUTED, ha="left")

    out_path = Path(__file__).resolve().parent / "db1-four-breakpoints-panel.png"
    fig.savefig(out_path, dpi=DPI, facecolor=BG, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    w, h = fig.get_size_inches() * DPI
    print(f"wrote {out_path} ({int(w)}x{int(h)} px @ {DPI} DPI)")


if __name__ == "__main__":
    main()
