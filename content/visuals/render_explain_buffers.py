"""
Render 5 visual assets for the PostgreSQL EXPLAIN BUFFERS blog post.

Usage:
    cd content/visuals
    python render_explain_buffers.py
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# ── Design Tokens ──────────────────────────────────────────────────────────
TOKENS = {
    'BG': '#ffffff',
    'ACCENT': '#1f6feb',
    'ACCENT_2': '#0d9488',
    'ACCENT_3': '#7c3aed',
    'WARN': '#dc2626',
    'SUCCESS': '#16a34a',
    'TEXT': '#1e293b',
    'TEXT_2': '#475569',
    'MUTED': '#94a3b8',
    'GRID': '#e5e7eb',
    'LIGHT_BG': '#f8fafc',
    'BLUE_BG': '#dbeafe',
    'TEAL_BG': '#ccfbf1',
    'PURPLE_BG': '#ede9fe',
    'RED_BG': '#fee2e2',
}
FONT = 'Helvetica Neue'
DPI = 320

plt.rcParams.update({
    'font.family': FONT,
    'font.sans-serif': [FONT, 'Helvetica', 'Arial', 'sans-serif'],
    'text.color': TOKENS['TEXT'],
    'axes.labelcolor': TOKENS['TEXT'],
    'xtick.color': TOKENS['TEXT_2'],
    'ytick.color': TOKENS['TEXT_2'],
})

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def _save(fig, filename):
    path = os.path.join(OUT_DIR, filename)
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f"  [OK] {filename}")


# ── Visual 1: shared-buffers-flow.png ──────────────────────────────────────
def render_shared_buffers_flow():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis('off')
    fig.patch.set_facecolor(TOKENS['BG'])

    # Box helper
    def draw_box(x, y, w, h, label, sublabel=None, fc=TOKENS['LIGHT_BG'],
                 ec=TOKENS['MUTED'], lw=1.5):
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                             facecolor=fc, edgecolor=ec, linewidth=lw,
                             transform=ax.transData)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h / 2 + (0.15 if sublabel else 0), label,
                ha='center', va='center', fontsize=11, fontweight='bold',
                color=TOKENS['TEXT'])
        if sublabel:
            ax.text(x + w / 2, y + h / 2 - 0.25, sublabel,
                    ha='center', va='center', fontsize=8, color=TOKENS['TEXT_2'],
                    style='italic')

    # Boxes
    draw_box(0.3, 1.8, 2.2, 1.4, "SQL Query", fc=TOKENS['LIGHT_BG'],
             ec=TOKENS['ACCENT'])
    draw_box(4.2, 1.0, 3.6, 3.0, "Shared Buffer\nCache",
             sublabel="(shared_buffers)", fc=TOKENS['BLUE_BG'],
             ec=TOKENS['ACCENT'], lw=2)
    draw_box(9.5, 1.8, 2.2, 1.4, "Disk\n(Data Files)", fc=TOKENS['LIGHT_BG'],
             ec=TOKENS['MUTED'])

    # Arrow: Query -> Buffer Cache (shared hit / fast path)
    ax.annotate("", xy=(4.2, 2.5), xytext=(2.5, 2.5),
                arrowprops=dict(arrowstyle='->', color=TOKENS['ACCENT'],
                                lw=2.5, connectionstyle='arc3,rad=0'))
    ax.text(3.35, 2.85, "shared hit\n(fast path)", ha='center', va='bottom',
            fontsize=8, color=TOKENS['ACCENT'], fontweight='bold')

    # Arrow: Buffer Cache -> Disk (shared read)
    ax.annotate("", xy=(9.5, 2.8), xytext=(7.8, 2.8),
                arrowprops=dict(arrowstyle='->', color=TOKENS['WARN'],
                                lw=2.5, connectionstyle='arc3,rad=0'))
    ax.text(8.65, 3.15, "shared read\n(I/O latency)", ha='center', va='bottom',
            fontsize=8, color=TOKENS['WARN'], fontweight='bold')

    # Arrow: Disk -> Buffer Cache (data loaded back)
    ax.annotate("", xy=(7.8, 2.1), xytext=(9.5, 2.1),
                arrowprops=dict(arrowstyle='->', color=TOKENS['MUTED'],
                                lw=1.5, connectionstyle='arc3,rad=0',
                                linestyle='dashed'))
    ax.text(8.65, 1.7, "pages loaded", ha='center', va='top',
            fontsize=7, color=TOKENS['MUTED'])

    # Annotation: shared dirtied (inside cache area)
    ax.annotate("shared\ndirtied", xy=(5.5, 3.8), xytext=(5.5, 4.6),
                ha='center', fontsize=8, color=TOKENS['SUCCESS'],
                fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=TOKENS['SUCCESS'],
                                lw=1.5))
    ax.text(5.5, 3.55, "[modified pages]", ha='center', fontsize=7,
            color=TOKENS['SUCCESS'], style='italic')

    # Annotation: shared written (cache -> disk, sync write)
    ax.annotate("", xy=(9.5, 1.5), xytext=(7.8, 1.5),
                arrowprops=dict(arrowstyle='->', color=TOKENS['ACCENT_3'],
                                lw=2, connectionstyle='arc3,rad=-0.15',
                                linestyle='dashed'))
    ax.text(8.65, 0.95, "shared written\n(sync flush)", ha='center', va='top',
            fontsize=8, color=TOKENS['ACCENT_3'], fontweight='bold')

    # Title
    ax.text(6, 4.8, "PostgreSQL Shared Buffer Cache: Data Flow",
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=TOKENS['TEXT'])

    _save(fig, "shared-buffers-flow.png")


# ── Visual 2: buffer-hit-comparison.png ────────────────────────────────────
def render_buffer_hit_comparison():
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor(TOKENS['BG'])

    categories = ["During Incident", "Baseline (healthy)"]
    hits = [0.3, 95]
    reads = [99.7, 5]

    y_pos = np.arange(len(categories))
    bar_h = 0.45

    # Hit bars (blue)
    bars_hit = ax.barh(y_pos, hits, bar_h, label='shared hit (%)',
                       color=TOKENS['ACCENT'], zorder=3)
    # Read bars (stacked)
    bars_read = ax.barh(y_pos, reads, bar_h, left=hits, label='shared read (%)',
                        color=[TOKENS['WARN'], TOKENS['MUTED']], zorder=3)

    # Labels on bars
    for i, (h, r) in enumerate(zip(hits, reads)):
        # Hit label
        if h > 5:
            ax.text(h / 2, i, f"{h}% hit", ha='center', va='center',
                    fontsize=9, fontweight='bold', color='white')
        else:
            ax.text(h + 1.5, i, f"{h}% hit", ha='left', va='center',
                    fontsize=8, fontweight='bold', color=TOKENS['ACCENT'])
        # Read label
        read_color = TOKENS['WARN'] if i == 0 else TOKENS['MUTED']
        ax.text(h + r / 2, i, f"{r}% read", ha='center', va='center',
                fontsize=9, fontweight='bold',
                color='white' if r > 20 else TOKENS['TEXT_2'])

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=11, fontweight='bold')
    ax.set_xlim(0, 105)
    ax.set_xlabel("Percentage of Buffer Accesses", fontsize=10,
                  color=TOKENS['TEXT_2'])
    ax.set_title("Buffer Hit Ratio: Before vs During Incident",
                 fontsize=13, fontweight='bold', color=TOKENS['TEXT'], pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(TOKENS['GRID'])
    ax.spines['left'].set_color(TOKENS['GRID'])
    ax.tick_params(axis='x', colors=TOKENS['TEXT_2'])
    ax.xaxis.grid(True, color=TOKENS['GRID'], linewidth=0.5, zorder=0)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=TOKENS['ACCENT'], label='shared hit (cached)'),
        mpatches.Patch(facecolor=TOKENS['WARN'], label='shared read (disk I/O)'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
              framealpha=0.9, edgecolor=TOKENS['GRID'])

    _save(fig, "buffer-hit-comparison.png")


# ── Visual 3: query-plan-tree.png ─────────────────────────────────────────
def render_query_plan_tree():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(TOKENS['BG'])

    def draw_node(x, y, w, h, label, buffers, bg=TOKENS['LIGHT_BG'],
                  border=TOKENS['MUTED'], problem=False):
        if problem:
            bg = TOKENS['RED_BG']
            border = TOKENS['WARN']
        box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                             boxstyle="round,pad=0.12",
                             facecolor=bg, edgecolor=border, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y + 0.15, label, ha='center', va='center',
                fontsize=9, fontweight='bold', color=TOKENS['TEXT'])
        ax.text(x, y - 0.25, buffers, ha='center', va='center',
                fontsize=7, color=TOKENS['TEXT_2'], style='italic')

    def connect(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color=TOKENS['MUTED'], lw=1.5,
                zorder=0)

    # Title
    ax.text(7, 8.6, "Query Plan Tree with Buffer Annotations",
            ha='center', fontsize=14, fontweight='bold', color=TOKENS['TEXT'])

    # Nodes (positioned in a tree layout)
    # Level 0: Limit
    draw_node(7, 7.5, 4.5, 0.9, "Limit",
              "shared hit=50, read=15,000, written=847")

    # Level 1: Sort
    draw_node(7, 5.8, 4.5, 0.9, "Sort (external merge, Disk: 2,500kB)",
              "temp read=312, written=312", problem=True)
    connect(7, 7.05, 7, 6.25)

    # Level 2: Nested Loop
    draw_node(7, 4.1, 3.8, 0.9, "Nested Loop",
              "shared hit=48, read=14,950")
    connect(7, 5.35, 7, 4.55)

    # Level 3: Three leaf nodes
    # Left: orders (PROBLEM)
    draw_node(2.5, 2.0, 4.0, 1.0,
              "Index Scan on orders",
              "shared hit=12, read=14,800", problem=True)
    connect(7, 3.65, 2.5, 2.5)

    # Center: order_items
    draw_node(7, 2.0, 4.0, 1.0,
              "Index Scan on order_items",
              "shared hit=30, read=120")
    connect(7, 3.65, 7, 2.5)

    # Right: inventory
    draw_node(11.5, 2.0, 4.0, 1.0,
              "Index Scan on inventory",
              "shared hit=6, read=30")
    connect(7, 3.65, 11.5, 2.5)

    # Callout annotations
    # Arrow pointing to orders node
    ax.annotate("BOTTLENECK: 99.9% reads from disk\n(table bloat -> cache eviction)",
                xy=(2.5, 1.45), xytext=(2.5, 0.4),
                ha='center', fontsize=8, fontweight='bold',
                color=TOKENS['WARN'],
                arrowprops=dict(arrowstyle='->', color=TOKENS['WARN'], lw=1.5))

    # Arrow pointing to sort node
    ax.annotate("work_mem spill\n(256kB config too small)",
                xy=(10.5, 5.8), xytext=(12.2, 6.8),
                ha='center', fontsize=8, fontweight='bold',
                color=TOKENS['WARN'],
                arrowprops=dict(arrowstyle='->', color=TOKENS['WARN'], lw=1.5))

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=TOKENS['RED_BG'], edgecolor=TOKENS['WARN'],
                       label='Problem node'),
        mpatches.Patch(facecolor=TOKENS['LIGHT_BG'], edgecolor=TOKENS['MUTED'],
                       label='Normal node'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9,
              framealpha=0.9, edgecolor=TOKENS['GRID'])

    _save(fig, "query-plan-tree.png")


# ── Visual 4: before-after-metrics.png ─────────────────────────────────────
def render_before_after_metrics():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor(TOKENS['BG'])

    metrics = [
        "Checkout p95 (ms)",
        "Temp pages spilled",
        "Hit ratio (%)",
        "Execution time (ms)",
    ]
    before_vals = [1200, 312, 0.3, 1192]
    after_vals = [48, 0, 97.3, 42]

    y_pos = np.arange(len(metrics))
    bar_h = 0.35

    # Normalize for display: use log-ish or direct scale
    # We'll use actual values but with a smart xlim
    max_val = max(max(before_vals), max(after_vals)) * 1.15

    bars_before = ax.barh(y_pos + bar_h / 2, before_vals, bar_h,
                          label='Before (incident)', color=TOKENS['WARN'],
                          zorder=3)
    bars_after = ax.barh(y_pos - bar_h / 2, after_vals, bar_h,
                         label='After (optimized)', color=TOKENS['SUCCESS'],
                         zorder=3)

    # Value labels
    for i, (bv, av) in enumerate(zip(before_vals, after_vals)):
        # Before label
        bv_str = f"{bv:,.1f}%" if "ratio" in metrics[i].lower() else f"{bv:,}"
        ax.text(bv + max_val * 0.015, i + bar_h / 2, bv_str,
                ha='left', va='center', fontsize=9, fontweight='bold',
                color=TOKENS['WARN'])
        # After label
        av_str = f"{av:,.1f}%" if "ratio" in metrics[i].lower() else f"{av:,}"
        ax.text(max(av, max_val * 0.005) + max_val * 0.015, i - bar_h / 2,
                av_str, ha='left', va='center', fontsize=9, fontweight='bold',
                color=TOKENS['SUCCESS'])

    ax.set_yticks(y_pos)
    ax.set_yticklabels(metrics, fontsize=11, fontweight='bold')
    ax.set_xlim(0, max_val)
    ax.set_title("Before and After: Performance Impact",
                 fontsize=14, fontweight='bold', color=TOKENS['TEXT'], pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(TOKENS['GRID'])
    ax.spines['left'].set_color(TOKENS['GRID'])
    ax.xaxis.grid(True, color=TOKENS['GRID'], linewidth=0.5, zorder=0)
    ax.tick_params(axis='x', colors=TOKENS['TEXT_2'])

    ax.legend(loc='lower right', fontsize=10, framealpha=0.9,
              edgecolor=TOKENS['GRID'])

    _save(fig, "before-after-metrics.png")


# ── Visual 5: pg-version-timeline.png ──────────────────────────────────────
def render_pg_version_timeline():
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(2008, 2027.5)
    ax.set_ylim(-2.5, 3.5)
    ax.axis('off')
    fig.patch.set_facecolor(TOKENS['BG'])

    # Title
    ax.text(2017.75, 3.2,
            "PostgreSQL EXPLAIN BUFFERS: Version Timeline",
            ha='center', fontsize=14, fontweight='bold', color=TOKENS['TEXT'])

    # Main timeline line
    ax.plot([2008.5, 2027], [0, 0], color=TOKENS['MUTED'], lw=2.5, zorder=1)

    milestones = [
        (2009, "PG 8.4", "EXPLAIN (BUFFERS)\nintroduced", False),
        (2010, "PG 9.0", "Parenthesized\nsyntax", False),
        (2012, "PG 9.2", "track_io_timing", False),
        (2020, "PG 13", "Planning\nbuffers", False),
        (2023, "PG 16", "pg_stat_io\nview", False),
        (2024, "PG 17", "pg_buffercache_\nevict()", False),
        (2025, "PG 18", "BUFFERS\nby default", True),
        (2026, "PG 19", "Reduced timing\noverhead", False),
    ]

    for i, (year, version, desc, highlight) in enumerate(milestones):
        # Alternate labels above/below
        above = (i % 2 == 0)

        # Marker
        marker_size = 14 if highlight else 8
        marker_color = TOKENS['ACCENT'] if highlight else TOKENS['TEXT_2']
        marker_zorder = 5 if highlight else 3
        ax.plot(year, 0, 'o', markersize=marker_size, color=marker_color,
                zorder=marker_zorder, markeredgecolor='white',
                markeredgewidth=1.5 if highlight else 0.8)

        if highlight:
            # Highlight ring
            ax.plot(year, 0, 'o', markersize=20, color='none',
                    markeredgecolor=TOKENS['ACCENT'], markeredgewidth=2,
                    zorder=4)

        # Version label + description
        y_ver = 0.6 if above else -0.6
        y_desc = 1.2 if above else -1.3
        va_ver = 'bottom' if above else 'top'
        va_desc = 'bottom' if above else 'top'

        # Connecting line from dot to label
        line_y_end = 0.45 if above else -0.45
        ax.plot([year, year], [0.15 if above else -0.15, line_y_end],
                color=marker_color if highlight else TOKENS['GRID'],
                lw=1.2 if highlight else 0.8, zorder=2)

        fontweight = 'bold' if highlight else 'bold'
        fontsize_ver = 10 if highlight else 8.5
        fontsize_desc = 9 if highlight else 7.5

        ax.text(year, y_ver, version, ha='center', va=va_ver,
                fontsize=fontsize_ver, fontweight=fontweight,
                color=marker_color)
        ax.text(year, y_desc, desc, ha='center', va=va_desc,
                fontsize=fontsize_desc, color=TOKENS['TEXT_2'],
                linespacing=1.3)

        # Year below the line (opposite side of label)
        y_year = -0.5 if above else 0.5
        va_year = 'top' if above else 'bottom'
        ax.text(year, y_year, str(year), ha='center', va=va_year,
                fontsize=7, color=TOKENS['MUTED'])

    # Highlight box behind PG 18
    highlight_box = FancyBboxPatch((2024.3, -2.0), 1.4, 4.2,
                                   boxstyle="round,pad=0.15",
                                   facecolor=TOKENS['BLUE_BG'],
                                   edgecolor=TOKENS['ACCENT'],
                                   linewidth=1.2, alpha=0.3, zorder=0)
    ax.add_patch(highlight_box)

    _save(fig, "pg-version-timeline.png")


# ── Main ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Rendering EXPLAIN BUFFERS visuals...")
    render_shared_buffers_flow()
    render_buffer_hit_comparison()
    render_query_plan_tree()
    render_before_after_metrics()
    render_pg_version_timeline()
    print("Done. All 5 PNGs generated.")
