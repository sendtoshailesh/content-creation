"""
Visual renderer for Part 3 supporting visuals (originally named for Part 1).
Generates 3 PNGs at 320 DPI using the shared design token system.

Visuals:
1. model-multiplier-spectrum.png — per-request cost spectrum across Lightweight/Versatile/Powerful
2. task-routing-decision-tree.png — decision flowchart for category selection
3. routing-savings-bar.png — before/after cost comparison with 68% savings
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

# Design tokens
TOKENS = {
    'BG': '#ffffff',       'ACCENT': '#1f6feb',   'ACCENT_2': '#0d9488',
    'ACCENT_3': '#7c3aed', 'WARN': '#dc2626',     'SUCCESS': '#16a34a',
    'TEXT': '#1e293b',      'TEXT_2': '#475569',    'MUTED': '#94a3b8',
    'GRID': '#e5e7eb',      'LIGHT_BG': '#f8fafc',  'BLUE_BG': '#dbeafe',
    'TEAL_BG': '#ccfbf1',   'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2',
}
FONT = 'Helvetica Neue'
DPI = 320
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    'font.family': FONT,
    'font.size': 10,
    'axes.facecolor': TOKENS['BG'],
    'figure.facecolor': TOKENS['BG'],
    'text.color': TOKENS['TEXT'],
    'text.parse_math': False,
})


def render_multiplier_spectrum():
    """Horizontal bar chart showing per-request $ cost across categories."""
    models = [
        ('Lightweight - short chat', 0.001, '~$0.001', TOKENS['SUCCESS']),
        ('Lightweight - typical', 0.005, '~$0.005', TOKENS['SUCCESS']),
        ('Versatile - chat reply', 0.015, '~$0.015', TOKENS['ACCENT_2']),
        ('Versatile - review', 0.04, '~$0.04', TOKENS['ACCENT']),
        ('Versatile - refactor', 0.10, '~$0.10', TOKENS['ACCENT']),
        ('Powerful - moderate task', 0.20, '~$0.20', TOKENS['ACCENT_3']),
        ('Powerful - agent session', 0.30, '~$0.30', TOKENS['ACCENT_3']),
        ('Powerful - deep agent', 0.45, '~$0.45', '#991b1b'),
    ]

    fig, ax = plt.subplots(figsize=(10, 5))

    y_positions = list(range(len(models)))
    y_positions.reverse()

    for i, (name, cost, label, color) in enumerate(models):
        y = y_positions[i]
        bar_width = max(cost, 0.003)  # give cheapest a visible bar
        ax.barh(y, bar_width, height=0.6, color=color, alpha=0.85, edgecolor='white', linewidth=0.5)

        # Model name on left
        ax.text(-0.008, y, name, ha='right', va='center', fontsize=8.5,
                color=TOKENS['TEXT'], fontweight='bold')

        # $ label on bar or right of bar
        label_x = bar_width + 0.006
        ax.text(label_x, y, label, ha='left', va='center', fontsize=8,
                color=TOKENS['TEXT_2'])

    # ~450x spread annotation
    ax.annotate('~450x cost\nspread per request',
                xy=(0.45, y_positions[0]), xytext=(0.32, y_positions[3]),
                fontsize=9, fontweight='bold', color=TOKENS['WARN'],
                ha='center', va='center',
                arrowprops=dict(arrowstyle='->', color=TOKENS['WARN'], lw=1.5))

    ax.set_xlim(-0.13, 0.52)
    ax.set_ylim(-0.8, len(models) - 0.2)
    ax.set_xlabel('Per-request cost in USD (GitHub AI Credits, 1 credit = $0.01)', fontsize=10, color=TOKENS['TEXT_2'])
    ax.set_yticks([])
    ax.set_xticks([0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5])
    ax.set_xticklabels(['$0', '$0.05', '$0.10', '$0.20', '$0.30', '$0.40', '$0.50'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(TOKENS['GRID'])
    ax.tick_params(axis='x', colors=TOKENS['TEXT_2'])

    ax.set_title('Per-Request Cost Spectrum: Lightweight to Powerful',
                 fontsize=13, fontweight='bold', color=TOKENS['TEXT'], pad=15)

    fig.text(0.5, 0.02,
             'Per-token rates and category placements as of May 2026. '
             'Specific model lineups rotate; the Lightweight / Versatile / Powerful taxonomy is durable.',
             ha='center', fontsize=7.5, color=TOKENS['MUTED'], style='italic')

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    path = os.path.join(OUT_DIR, 'model-multiplier-spectrum.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_routing_decision_tree():
    """Decision flowchart for model selection based on task complexity."""
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    def draw_box(x, y, w, h, text, color, text_color=TOKENS['TEXT'], fontsize=9, bold=False):
        box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                             boxstyle="round,pad=0.15", facecolor=color,
                             edgecolor=TOKENS['MUTED'], linewidth=1)
        ax.add_patch(box)
        weight = 'bold' if bold else 'normal'
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color=text_color, fontweight=weight, wrap=True,
                linespacing=1.3)

    def draw_diamond(x, y, w, h, text, color):
        diamond = plt.Polygon([
            (x, y + h/2), (x + w/2, y), (x, y - h/2), (x - w/2, y)
        ], facecolor=color, edgecolor=TOKENS['MUTED'], linewidth=1)
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', fontsize=8.5,
                color=TOKENS['TEXT'], fontweight='bold', linespacing=1.3)

    def arrow(x1, y1, x2, y2, label='', label_side='right'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=TOKENS['MUTED'], lw=1.2))
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            offset = 0.2 if label_side == 'right' else -0.2
            ax.text(mid_x + offset, mid_y, label, fontsize=7.5,
                    color=TOKENS['ACCENT'], fontweight='bold', ha='center', va='center')

    # Title
    ax.text(5, 9.6, 'Model Routing Decision Tree', fontsize=14, fontweight='bold',
            color=TOKENS['TEXT'], ha='center', va='center')
    ax.text(5, 9.2, 'Match the model to the task, not the other way around',
            fontsize=9, color=TOKENS['TEXT_2'], ha='center', va='center')

    # Start node
    draw_box(5, 8.3, 2.5, 0.6, 'New Copilot Request', TOKENS['BLUE_BG'], bold=True)

    # Decision 1
    arrow(5, 8.0, 5, 7.4)
    draw_diamond(5, 6.8, 3, 1.1, 'Can you explain\nthe task in\n< 30 seconds?', TOKENS['LIGHT_BG'])

    # YES -> Lightweight
    arrow(3.5, 6.8, 1.8, 6.8, 'YES', 'left')
    draw_box(1.8, 5.8, 2.8, 1.2,
             'LIGHTWEIGHT\n\n~$0.001-$0.005/request\nExamples (May 2026):\nGPT-5 mini, Gemini 3.5 Flash',
             TOKENS['TEAL_BG'], bold=False, fontsize=8)
    ax.text(1.8, 4.95, '60-70% of tasks', fontsize=7.5, color=TOKENS['SUCCESS'],
            ha='center', fontweight='bold')

    # NO -> Decision 2
    arrow(6.5, 6.8, 8, 6.8, 'NO')
    draw_diamond(8, 5.8, 3, 1.1, 'Does it need\nmulti-file reasoning\nor system design?', TOKENS['LIGHT_BG'])

    # NO -> Versatile
    arrow(6.5, 5.8, 5.2, 5.8, 'NO', 'left')
    draw_box(5.2, 4.6, 2.8, 1.2,
             'VERSATILE\n\n~$0.015-$0.10/request\nClaude Sonnet 4.x, GPT-4.1,\nHaiku 4.5 (May 2026)',
             TOKENS['BLUE_BG'], fontsize=8)
    ax.text(5.2, 3.75, '20-30% of tasks', fontsize=7.5, color=TOKENS['ACCENT'],
            ha='center', fontweight='bold')

    # YES -> Powerful
    arrow(8, 5.25, 8, 4.5)
    draw_box(8, 3.7, 2.8, 1.2,
             'POWERFUL\n\n~$0.20-$0.45/request\nClaude Opus 4.x, GPT-5.5,\nGemini 2.5 Pro (May 2026)',
             TOKENS['PURPLE_BG'], fontsize=8)
    ax.text(8, 2.85, '5-10% of tasks', fontsize=7.5, color=TOKENS['ACCENT_3'],
            ha='center', fontweight='bold')

    # Bottom note
    draw_box(5, 1.5, 7, 0.9,
             'TIP: Enable auto-routing when you have no strong preference; let Copilot pick the category.\n'
             'AVOID running a Powerful agent session on a Lightweight task — that is where ~450x bills come from.',
             TOKENS['RED_BG'], fontsize=7.5, text_color=TOKENS['TEXT_2'])

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'task-routing-decision-tree.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_routing_savings():
    """Before/after cost comparison bar chart with 68% savings annotation."""
    fig, ax = plt.subplots(figsize=(8, 5))

    categories = ['Before\n(all expensive models)', 'After\n(routed by task)']
    values = [3000, 970]
    colors = [TOKENS['WARN'], TOKENS['SUCCESS']]

    bars = ax.bar(categories, values, width=0.5, color=colors, edgecolor='white', linewidth=1)

    # Value labels on bars
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 60,
                f'${val:,}/day', ha='center', va='bottom', fontsize=12,
                fontweight='bold', color=TOKENS['TEXT'])

    # Savings annotation
    mid_x = 0.5
    ax.annotate('',
                xy=(1, 2600), xytext=(0, 2600),
                arrowprops=dict(arrowstyle='<->', color=TOKENS['ACCENT'], lw=2))
    ax.text(mid_x, 2750, '68% savings', fontsize=13, fontweight='bold',
            color=TOKENS['ACCENT'], ha='center')
    ax.text(mid_x, 2500, '$740K/year', fontsize=11, fontweight='bold',
            color=TOKENS['ACCENT_2'], ha='center')

    # Context label (below chart via figure text)
    fig.text(0.5, 0.01, 'Coding assistant team: 70% simple tasks routed to cheaper models',
             fontsize=8.5, color=TOKENS['TEXT_2'], ha='center', style='italic')

    ax.set_ylim(0, 3400)
    ax.set_ylabel('Daily Cost (USD)', fontsize=10, color=TOKENS['TEXT_2'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(TOKENS['GRID'])
    ax.spines['bottom'].set_color(TOKENS['GRID'])
    ax.tick_params(axis='y', colors=TOKENS['TEXT_2'])
    ax.tick_params(axis='x', colors=TOKENS['TEXT'])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x):,}'))

    ax.set_title('Model Routing: Before vs. After',
                 fontsize=13, fontweight='bold', color=TOKENS['TEXT'], pad=15)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'routing-savings-bar.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


if __name__ == '__main__':
    print('Rendering Part 1 visuals...')
    render_multiplier_spectrum()
    render_routing_decision_tree()
    render_routing_savings()
    print('Done. 3 PNGs generated.')
