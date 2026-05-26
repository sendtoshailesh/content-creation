"""
Visual Pack Renderer — Part 3 Practitioner Mode
Blog: content/ai-code-assistant-cost-part-3.md
Persona: Practitioner (Medium hero + inline assets)

Run: python render_distilled.py
Outputs 3 PNG assets (medium-hero, medium-inline-01, medium-inline-02).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

DPI = 320
FONT = 'DejaVu Sans'
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

TOKENS = {
    'BG': '#ffffff',
    'TEXT': '#1e293b',
    'TEXT_2': '#475569',
    'MUTED': '#94a3b8',
    'GRID': '#e5e7eb',
    'LIGHT_BG': '#f8fafc',
    'ACCENT': '#1f6feb',
    'ACCENT_2': '#0d9488',
    'ACCENT_3': '#7c3aed',
    'WARN': '#dc2626',
    'SUCCESS': '#16a34a',
    'BLUE_BG': '#dbeafe',
    'TEAL_BG': '#ccfbf1',
    'PURPLE_BG': '#ede9fe',
    'RED_BG': '#fee2e2',
}


def fs(pt):
    """Scale matplotlib point fontsize to fit pixel-unit canvas at DPI=320."""
    return round(float(pt) * 0.50, 1)


def save(fig, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=DPI)
    plt.close(fig)
    print(f"  Saved: {filename}")


def make_fig(w_px, h_px, bg_color='#ffffff'):
    fig = plt.figure(figsize=(w_px / DPI, h_px / DPI))
    fig.patch.set_facecolor(bg_color)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w_px)
    ax.set_ylim(0, h_px)
    ax.set_axis_off()
    ax.set_facecolor(bg_color)
    return fig, ax


# ─── MEDIUM HERO (1400x800) ───────────────────────────────────────────────────
def render_medium_hero(tokens):
    W, H = 1400, 800
    BG = tokens['TEXT']
    fig, ax = make_fig(W, H, BG)

    # Top accent stripe
    rect = mpatches.FancyBboxPatch((0, H - 10), W, 10,
                                    boxstyle='square,pad=0',
                                    facecolor=tokens['ACCENT_3'], linewidth=0)
    ax.add_patch(rect)

    ax.text(W / 2, H * 0.72, "120x",
            ha='center', va='center', fontsize=fs(96),
            fontfamily=FONT, fontweight='bold', color='#ffffff')

    ax.text(W / 2, H * 0.50, "cost spread between cheapest\nand most expensive model",
            ha='center', va='center', fontsize=fs(22),
            fontfamily=FONT, color=tokens['ACCENT_3'],
            multialignment='center', linespacing=1.5)

    # Three stat callouts
    stats = [
        ("0.25x", "GPT-5.4 nano"),
        ("1x", "Claude Sonnet 4.6"),
        ("30x", "Claude Opus 4.6 fm"),
    ]
    x_positions = [W * 0.20, W * 0.50, W * 0.80]
    colors = [tokens['SUCCESS'], tokens['ACCENT'], tokens['WARN']]
    for (big, small), x, col in zip(stats, x_positions, colors):
        ax.text(x, H * 0.28, big,
                ha='center', va='center', fontsize=fs(22),
                fontfamily=FONT, fontweight='bold', color=col)
        ax.text(x, H * 0.20, small,
                ha='center', va='center', fontsize=fs(11),
                fontfamily=FONT, color='#94a3b8')

    ax.text(W / 2, H * 0.08, "Part 3 of 3: Model Selection & Team Governance  |  Shailesh Mishra, 2026",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, color='#64748b', style='italic')

    save(fig, "medium-hero.png")


# ─── MEDIUM INLINE 01: Task Taxonomy & Routing (1200x800) ────────────────────
def render_medium_inline_01(tokens):
    W, H = 1200, 800
    fig, ax = make_fig(W, H, tokens['BG'])

    ax.text(W / 2, H * 0.93, "3-Tier Task Taxonomy: Match Model to Complexity",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    rows = [
        ("SIMPLE", "60-70%", "0x - 0.25x",
         "Rename, docs, boilerplate,\nlinting, import fixes",
         tokens['SUCCESS'], tokens['TEAL_BG']),
        ("MODERATE", "20-30%", "1x",
         "Code review, refactor,\nunit tests, debugging",
         tokens['ACCENT'], tokens['BLUE_BG']),
        ("COMPLEX", "5-10%", "3x - 30x",
         "Multi-file refactor,\nsystem design, agent mode",
         tokens['WARN'], tokens['RED_BG']),
    ]

    col_w = W * 0.28
    x_starts = [W * 0.06, W * 0.37, W * 0.68]
    box_h = H * 0.55
    y_base = H * 0.18

    for xs, (tier, pct, mult, tasks, accent, bg) in zip(x_starts, rows):
        rect = mpatches.FancyBboxPatch((xs, y_base), col_w, box_h,
                                        boxstyle='round,pad=6',
                                        facecolor=bg,
                                        edgecolor=accent, linewidth=2)
        ax.add_patch(rect)
        ax.text(xs + col_w / 2, y_base + box_h - 30, tier,
                ha='center', va='top', fontsize=fs(14),
                fontfamily=FONT, fontweight='bold', color=accent)
        ax.text(xs + col_w / 2, y_base + box_h - 70, pct + " of tasks",
                ha='center', va='top', fontsize=fs(11),
                fontfamily=FONT, color=tokens['TEXT_2'])
        ax.text(xs + col_w / 2, y_base + box_h / 2 - 10, mult,
                ha='center', va='center', fontsize=fs(24),
                fontfamily=FONT, fontweight='bold', color=accent)
        ax.text(xs + col_w / 2, y_base + 50, tasks,
                ha='center', va='center', fontsize=fs(10),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.4)

    # Bottom note
    ax.text(W / 2, H * 0.08, "Route simple tasks to 0x models -> save 45-68% with zero quality loss",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    ax.text(W / 2, H * 0.03, "Source: Apple ML Research, 2025; GitHub Docs, 2026 | Subject to change",
            ha='center', va='center', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    save(fig, "medium-inline-01.png")


# ─── MEDIUM INLINE 02: Cost Math (1200x800) ──────────────────────────────────
def render_medium_inline_02(tokens):
    W, H = 1200, 800
    fig, ax = make_fig(W, H, tokens['LIGHT_BG'])

    ax.text(W / 2, H * 0.93, "Weighted Average: 0.55x (45% Savings vs. 1x Default)",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    # Stacked bar breakdown
    categories = [
        ("Simple\n65%", 0.65, 0.0, tokens['SUCCESS']),
        ("Moderate\n25%", 0.25, 1.0, tokens['ACCENT']),
        ("Complex\n10%", 0.10, 3.0, tokens['WARN']),
    ]

    bar_w = 160
    x_positions = [W * 0.18, W * 0.45, W * 0.72]
    y_base = H * 0.22
    max_bar_h = H * 0.44

    for (label, share, mult, col), x in zip(categories, x_positions):
        weighted = share * mult
        bar_h = max(12, int(mult / 3.5 * max_bar_h))
        rect = mpatches.FancyBboxPatch((x - bar_w / 2, y_base), bar_w, bar_h,
                                        boxstyle='square,pad=0',
                                        facecolor=col, linewidth=0, alpha=0.8)
        ax.add_patch(rect)

        # Multiplier label on bar
        ax.text(x, y_base + bar_h + 20, f"{mult}x multiplier",
                ha='center', va='bottom', fontsize=fs(13),
                fontfamily=FONT, fontweight='bold', color=col)

        # Weighted contribution — place inside bar if tall enough, else above bar
        if bar_h >= 50:
            ax.text(x, y_base + bar_h / 2, f"= {weighted:.2f}x weighted",
                    ha='center', va='center', fontsize=fs(11),
                    fontfamily=FONT, fontweight='bold', color='#ffffff')
        else:
            ax.text(x, y_base + bar_h + 55, f"= {weighted:.2f}x weighted",
                    ha='center', va='bottom', fontsize=fs(11),
                    fontfamily=FONT, fontweight='bold', color=col)

        # Category label
        ax.text(x, y_base - 24, label,
                ha='center', va='top', fontsize=fs(11),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.3)

    # Result box
    rect = mpatches.FancyBboxPatch((W * 0.25, H * 0.76), W * 0.50, H * 0.10,
                                    boxstyle='round,pad=6',
                                    facecolor=tokens['BLUE_BG'],
                                    edgecolor=tokens['ACCENT'], linewidth=2)
    ax.add_patch(rect)
    ax.text(W / 2, H * 0.81,
            "0.00 + 0.25 + 0.30 = 0.55x average  ->  45% savings",
            ha='center', va='center', fontsize=fs(14),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    ax.text(W / 2, H * 0.04,
            "RouteLLM: 95% GPT-4 quality at 75% cost reduction using only 14% GPT-4 calls | Source: LMSYS, 2024",
            ha='center', va='center', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    save(fig, "medium-inline-02.png")


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    import datetime
    print(f"Rendering Part 3 Practitioner visual pack -- {datetime.date.today()}")
    print(f"Output directory: {OUTPUT_DIR}")

    plt.rcParams['font.family'] = FONT
    plt.rcParams['figure.dpi'] = DPI

    funcs = [render_medium_hero, render_medium_inline_01, render_medium_inline_02]
    success = 0
    for func in funcs:
        try:
            func(TOKENS)
            success += 1
        except Exception as e:
            print(f"  ERROR in {func.__name__}: {e}")

    print(f"\n=== Done: {success}/{len(funcs)} assets rendered ===")
