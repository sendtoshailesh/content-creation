"""
Visual renderer for Part 1: "The 120x Problem"
Generates 3 PNGs at 320 DPI using the shared design token system.

Visuals:
1. model-multiplier-spectrum.png — horizontal bar chart of model multipliers by tier
2. task-routing-decision-tree.png — decision flowchart for model selection
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
})


def render_multiplier_spectrum():
    """Horizontal bar chart showing model multipliers from 0x to 30x, color-coded by tier."""
    models = [
        ('Included tier', 0, '(0x)', TOKENS['SUCCESS']),
        ('Budget tier (entry)', 0.25, '(0.25x)', TOKENS['ACCENT_2']),
        ('Budget tier (lower-mid)', 0.33, '(0.33x)', TOKENS['ACCENT_2']),
        ('Standard tier', 1.0, '(1x)', TOKENS['ACCENT']),
        ('Premium reasoning tier', 3.0, '(3x)', TOKENS['ACCENT_3']),
        ('Premium-plus tier', 7.5, '(7.5x)', TOKENS['WARN']),
        ('Flagship tier', 15.0, '(15x)', TOKENS['WARN']),
        ('Flagship fast-mode tier', 30.0, '(30x)', '#991b1b'),
    ]

    fig, ax = plt.subplots(figsize=(10, 5))

    y_positions = list(range(len(models)))
    y_positions.reverse()

    for i, (name, mult, tier, color) in enumerate(models):
        y = y_positions[i]
        bar_width = max(mult, 0.15)  # give free models a tiny visible bar
        ax.barh(y, bar_width, height=0.6, color=color, alpha=0.85, edgecolor='white', linewidth=0.5)

        # Model name on left
        ax.text(-0.5, y, name, ha='right', va='center', fontsize=8.5,
                color=TOKENS['TEXT'], fontweight='bold')

        # Tier label on bar or right of bar
        label_x = bar_width + 0.4
        ax.text(label_x, y, tier, ha='left', va='center', fontsize=8,
                color=TOKENS['TEXT_2'])

    # 120x annotation
    ax.annotate('120x cost\ndifference',
                xy=(30, y_positions[0]), xytext=(22, y_positions[3]),
                fontsize=9, fontweight='bold', color=TOKENS['WARN'],
                ha='center', va='center',
                arrowprops=dict(arrowstyle='->', color=TOKENS['WARN'], lw=1.5))

    ax.set_xlim(-8, 35)
    ax.set_ylim(-0.8, len(models) - 0.2)
    ax.set_xlabel('Model Multiplier', fontsize=10, color=TOKENS['TEXT_2'])
    ax.set_yticks([])
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(TOKENS['GRID'])
    ax.tick_params(axis='x', colors=TOKENS['TEXT_2'])

    ax.set_title('GitHub Copilot Model Multipliers: 0x to 30x',
                 fontsize=13, fontweight='bold', color=TOKENS['TEXT'], pad=15)

    fig.text(0.5, 0.02,
             '[VOLATILE] Tier names and multipliers are accurate as of May 2026. '
             'Specific model lineups rotate; the tier structure is the durable framework.',
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

    # YES -> Free/Cheap
    arrow(3.5, 6.8, 1.8, 6.8, 'YES', 'left')
    draw_box(1.8, 5.8, 2.8, 1.2,
             'INCLUDED / BUDGET\n\nIncluded tier (0x)\nBudget tier (0.25x - 0.33x)',
             TOKENS['TEAL_BG'], bold=False, fontsize=8)
    ax.text(1.8, 4.95, '60-70% of tasks', fontsize=7.5, color=TOKENS['SUCCESS'],
            ha='center', fontweight='bold')

    # NO -> Decision 2
    arrow(6.5, 6.8, 8, 6.8, 'NO')
    draw_diamond(8, 5.8, 3, 1.1, 'Does it need\nmulti-file reasoning\nor system design?', TOKENS['LIGHT_BG'])

    # NO -> Standard
    arrow(6.5, 5.8, 5.2, 5.8, 'NO', 'left')
    draw_box(5.2, 4.6, 2.8, 1.2,
             'STANDARD (1x)\n\nMid-tier general-purpose\nmodels from your provider\nof choice',
             TOKENS['BLUE_BG'], fontsize=8)
    ax.text(5.2, 3.75, '20-30% of tasks', fontsize=7.5, color=TOKENS['ACCENT'],
            ha='center', fontweight='bold')

    # YES -> Premium
    arrow(8, 5.25, 8, 4.5)
    draw_box(8, 3.7, 2.8, 1.2,
             'PREMIUM (3x)\n\nReasoning-class models\nUse deliberately,\nnot by default',
             TOKENS['PURPLE_BG'], fontsize=8)
    ax.text(8, 2.85, '5-10% of tasks', fontsize=7.5, color=TOKENS['ACCENT_3'],
            ha='center', fontweight='bold')

    # Bottom note
    draw_box(5, 1.5, 7, 0.9,
             'TIP: Enable auto-selection for 10% multiplier discount when you have no strong preference.\n'
             'AVOID 7.5x+ models unless you have a specific, articulable reason.',
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
