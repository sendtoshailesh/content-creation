"""
Visual Pack Renderer — Part 2 Practitioner Mode
Blog: content/ai-code-assistant-cost-part-2.md
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
                                    facecolor=tokens['ACCENT_2'], linewidth=0)
    ax.add_patch(rect)

    ax.text(W / 2, H * 0.72, "89%",
            ha='center', va='center', fontsize=fs(96),
            fontfamily=FONT, fontweight='bold', color='#ffffff')

    ax.text(W / 2, H * 0.50, "of your prefix tokens saved\nwith prompt caching",
            ha='center', va='center', fontsize=fs(22),
            fontfamily=FONT, color=tokens['ACCENT_2'],
            multialignment='center', linespacing=1.5)

    # Three stat callouts
    stats = [
        ("1M -> 109K", "effective tokens"),
        ("75-90%", "cache discount"),
        ("1.4x", "retry tax at 40%"),
    ]
    x_positions = [W * 0.20, W * 0.50, W * 0.80]
    for (big, small), x in zip(stats, x_positions):
        ax.text(x, H * 0.28, big,
                ha='center', va='center', fontsize=fs(20),
                fontfamily=FONT, fontweight='bold', color='#ffffff')
        ax.text(x, H * 0.20, small,
                ha='center', va='center', fontsize=fs(11),
                fontfamily=FONT, color='#94a3b8')

    ax.text(W / 2, H * 0.08, "Part 2 of 3: Caching & Workflow Discipline  |  Shailesh Mishra, 2026",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, color='#64748b', style='italic')

    save(fig, "medium-hero.png")


# ─── MEDIUM INLINE 01: Caching Math (1200x800) ───────────────────────────────
def render_medium_inline_01(tokens):
    W, H = 1200, 800
    fig, ax = make_fig(W, H, tokens['BG'])

    ax.text(W / 2, H * 0.92, "Prompt Caching: 10K Token Prefix x 100 Requests/Day",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    # Two big stat boxes
    boxes = [
        ("Without Caching", "1,000,000", "tokens at full price", tokens['WARN'], tokens['RED_BG']),
        ("With Caching", "109,000", "effective tokens", tokens['SUCCESS'], tokens['TEAL_BG']),
    ]
    box_w = W * 0.38
    box_h = H * 0.32
    y_base = H * 0.42
    x_starts = [W * 0.08, W * 0.54]

    for (label, big_num, subtitle, accent, bg), x in zip(boxes, x_starts):
        rect = mpatches.FancyBboxPatch((x, y_base), box_w, box_h,
                                        boxstyle='round,pad=6',
                                        facecolor=bg,
                                        edgecolor=accent, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + box_w / 2, y_base + box_h - 40, label,
                ha='center', va='top', fontsize=fs(13),
                fontfamily=FONT, fontweight='bold', color=accent)
        ax.text(x + box_w / 2, y_base + box_h / 2 - 10, big_num,
                ha='center', va='center', fontsize=fs(32),
                fontfamily=FONT, fontweight='bold', color=accent)
        ax.text(x + box_w / 2, y_base + 30, subtitle,
                ha='center', va='center', fontsize=fs(11),
                fontfamily=FONT, color=tokens['TEXT_2'])

    # Arrow between boxes
    ax.annotate('', xy=(W * 0.52, y_base + box_h / 2),
                xytext=(W * 0.48, y_base + box_h / 2),
                arrowprops=dict(arrowstyle='->', color=tokens['ACCENT'],
                                lw=2.5, mutation_scale=20))

    # Savings callout
    rect = mpatches.FancyBboxPatch((W * 0.30, H * 0.18), W * 0.40, H * 0.14,
                                    boxstyle='round,pad=6',
                                    facecolor=tokens['BLUE_BG'],
                                    edgecolor=tokens['ACCENT'], linewidth=2)
    ax.add_patch(rect)
    ax.text(W / 2, H * 0.27, "89% savings on prefix tokens",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])
    ax.text(W / 2, H * 0.20, "By request 10, the prefix is essentially free",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, color=tokens['TEXT_2'])

    ax.text(W / 2, H * 0.06, "Source: GitHub Copilot billing documentation, 2026 | GPT-4.1: 75% off, Claude Sonnet 4.6: 90% off",
            ha='center', va='center', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    save(fig, "medium-inline-01.png")


# ─── MEDIUM INLINE 02: Retry Tax Chart (1200x800) ────────────────────────────
def render_medium_inline_02(tokens):
    W, H = 1200, 800
    fig, ax = make_fig(W, H, tokens['LIGHT_BG'])

    ax.text(W / 2, H * 0.92, "The Retry Tax: Every Follow-Up Is a Full-Price Request",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    # Bar chart: retry rates vs effective cost
    retry_rates = [0, 20, 40, 60]
    effective_costs = [1.0, 1.2, 1.4, 1.6]
    labels = ["0%\nretry", "20%\nretry", "40%\nretry", "60%\nretry"]
    colors = [tokens['SUCCESS'], tokens['ACCENT'], tokens['WARN'], '#991b1b']

    bar_w = 140
    x_positions = [W * 0.15, W * 0.37, W * 0.59, W * 0.81]
    y_base = H * 0.18
    max_bar_h = H * 0.50

    for x, cost, label, col in zip(x_positions, effective_costs, labels, colors):
        bar_h = int(cost / 1.8 * max_bar_h)
        rect = mpatches.FancyBboxPatch((x - bar_w / 2, y_base), bar_w, bar_h,
                                        boxstyle='square,pad=0',
                                        facecolor=col, linewidth=0, alpha=0.8)
        ax.add_patch(rect)
        ax.text(x, y_base + bar_h + 20, f"{cost}x",
                ha='center', va='bottom', fontsize=fs(18),
                fontfamily=FONT, fontweight='bold', color=col)
        ax.text(x, y_base - 24, label,
                ha='center', va='top', fontsize=fs(11),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.3)

    # Annotation line showing "most devs"
    ax.plot([x_positions[1] - 20, x_positions[2] + 20],
            [H * 0.78, H * 0.78], color=tokens['ACCENT'], lw=2, linestyle='--')
    ax.text((x_positions[1] + x_positions[2]) / 2, H * 0.82,
            "Most developers: 30-50% retry range",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    ax.text(W / 2, H * 0.06, "Every vague prompt, every 'try again' is a full-price request producing zero value | Source: author analysis, 2026",
            ha='center', va='center', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    save(fig, "medium-inline-02.png")


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    import datetime
    print(f"Rendering Part 2 Practitioner visual pack -- {datetime.date.today()}")
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
