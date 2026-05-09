"""
Visual renderer for Part 1: "Less Noise, Better Output"
Generates 3 PNGs at 320 DPI using the shared design token system.

Visuals:
1. context-quality-paradox.png — split-panel: more context (low accuracy) vs better context (high accuracy)
2. context-engineering-framework.png — five-column practice cards with quality + token benefits
3. before-after-context.png — three scenarios showing accuracy UP and tokens DOWN
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

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


def draw_rounded_box(ax, x, y, w, h, color, alpha=1.0):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                         facecolor=color, edgecolor=TOKENS['GRID'],
                         linewidth=0.8, alpha=alpha)
    ax.add_patch(box)
    return box


def render_context_quality_paradox():
    """Split-panel: cluttered context (low accuracy) vs clean context (high accuracy)."""
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Title
    ax.text(5.5, 6.6, 'The Context Quality Paradox', fontsize=15, fontweight='bold',
            color=TOKENS['TEXT'], ha='center')
    ax.text(5.5, 6.2, 'Anthropic saw accuracy jump from 49% to 74% by reducing, not adding, context',
            fontsize=9, color=TOKENS['TEXT_2'], ha='center', style='italic')

    # Divider
    ax.plot([5.5, 5.5], [0.3, 5.8], color=TOKENS['GRID'], linewidth=1.5, linestyle='--')

    # === LEFT PANEL: More Context ===
    draw_rounded_box(ax, 0.3, 0.3, 4.8, 5.5, TOKENS['RED_BG'], alpha=0.4)
    ax.text(2.7, 5.5, 'More Context', fontsize=12, fontweight='bold',
            color=TOKENS['WARN'], ha='center')

    left_items = [
        ('15 open files', '[x] [x] [x] [x] [x] ...'),
        ('Long chat history', '47 messages, mixed topics'),
        ('50+ tool definitions', '55,000-134,000 tokens'),
        ('Vague prompt', '"fix the bug"'),
    ]
    for i, (label, detail) in enumerate(left_items):
        y = 4.7 - i * 0.9
        ax.text(0.6, y, '[ ]', fontsize=8, color=TOKENS['WARN'], fontweight='bold')
        ax.text(1.1, y, label, fontsize=9, fontweight='bold', color=TOKENS['TEXT'])
        ax.text(1.1, y - 0.3, detail, fontsize=7.5, color=TOKENS['TEXT_2'])

    # Left result
    draw_rounded_box(ax, 0.8, 0.5, 3.8, 1.0, '#fecaca')
    ax.text(2.7, 1.15, 'Confused AI Output', fontsize=10, fontweight='bold',
            color=TOKENS['WARN'], ha='center')
    ax.text(2.7, 0.75, 'Accuracy: 49%', fontsize=9, color=TOKENS['WARN'], ha='center')

    # === RIGHT PANEL: Better Context ===
    draw_rounded_box(ax, 5.9, 0.3, 4.8, 5.5, TOKENS['TEAL_BG'], alpha=0.4)
    ax.text(8.3, 5.5, 'Better Context', fontsize=12, fontweight='bold',
            color=TOKENS['SUCCESS'], ha='center')

    right_items = [
        ('3 relevant files', 'Only what matters for this task'),
        ('Fresh thread', '1 task, clean slate'),
        ('On-demand tools', '~500 tokens (Tool Search)'),
        ('Targeted prompt', '#file:auth.ts fix null check L47'),
    ]
    for i, (label, detail) in enumerate(right_items):
        y = 4.7 - i * 0.9
        ax.text(6.2, y, '[x]', fontsize=8, color=TOKENS['SUCCESS'], fontweight='bold')
        ax.text(6.7, y, label, fontsize=9, fontweight='bold', color=TOKENS['TEXT'])
        ax.text(6.7, y - 0.3, detail, fontsize=7.5, color=TOKENS['TEXT_2'])

    # Right result
    draw_rounded_box(ax, 6.4, 0.5, 3.8, 1.0, '#bbf7d0')
    ax.text(8.3, 1.15, 'Accurate AI Output', fontsize=10, fontweight='bold',
            color=TOKENS['SUCCESS'], ha='center')
    ax.text(8.3, 0.75, 'Accuracy: 74%', fontsize=9, color=TOKENS['SUCCESS'], ha='center')

    # Arrow annotation
    ax.annotate('+25 points\n85% fewer tokens',
                xy=(5.5, 1.0), xytext=(5.5, 2.5),
                fontsize=9, fontweight='bold', color=TOKENS['ACCENT'],
                ha='center', va='center',
                arrowprops=dict(arrowstyle='->', color=TOKENS['ACCENT'], lw=1.5))

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'context-quality-paradox.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_context_engineering_framework():
    """Five-column practice cards with quality benefits and token reduction."""
    fig, ax = plt.subplots(figsize=(12, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(6, 6.7, 'Context Engineering: Five Practices', fontsize=14, fontweight='bold',
            color=TOKENS['TEXT'], ha='center')
    ax.text(6, 6.3, 'Each passes the test: "Would I do this even if AI were free?"',
            fontsize=9, color=TOKENS['TEXT_2'], ha='center', style='italic')

    practices = [
        {
            'title': 'Single-Task\nFocus',
            'action': 'Close unrelated\nfiles',
            'quality': 'Fewer conflicting\nsignals',
            'tokens': 'Removes noise\nfrom context',
            'color': TOKENS['BLUE_BG'],
        },
        {
            'title': 'Thread\nHygiene',
            'action': 'New thread\nper task',
            'quality': 'No stale history\nsteering output',
            'tokens': '30-70% junk\neliminated',
            'color': TOKENS['BLUE_BG'],
        },
        {
            'title': 'Targeted\nReferences',
            'action': 'Use #file for\nspecific files',
            'quality': 'Model focuses\non what matters',
            'tokens': '37% reduction\n(Anthropic)',
            'color': TOKENS['BLUE_BG'],
        },
        {
            'title': 'Front-Load\nIntent',
            'action': 'State goal in\nfirst sentence',
            'quality': 'Primes model\nattention',
            'tokens': 'Fewer retries\n= fewer tokens',
            'color': TOKENS['BLUE_BG'],
        },
        {
            'title': 'Stable\nInstructions',
            'action': 'copilot-instructions\n.md file',
            'quality': 'Consistent\nproject context',
            'tokens': 'Cacheable\nprefix (90% off)',
            'color': TOKENS['BLUE_BG'],
        },
    ]

    card_w = 2.0
    gap = 0.3
    start_x = (12 - (5 * card_w + 4 * gap)) / 2

    for i, p in enumerate(practices):
        x = start_x + i * (card_w + gap)

        # Card background
        draw_rounded_box(ax, x, 0.6, card_w, 5.2, p['color'], alpha=0.5)

        # Number badge
        badge = plt.Circle((x + card_w / 2, 5.4), 0.25,
                            facecolor=TOKENS['ACCENT'], edgecolor='white', linewidth=1.5)
        ax.add_patch(badge)
        ax.text(x + card_w / 2, 5.4, str(i + 1), fontsize=10, fontweight='bold',
                color='white', ha='center', va='center')

        # Title
        ax.text(x + card_w / 2, 4.8, p['title'], fontsize=9, fontweight='bold',
                color=TOKENS['TEXT'], ha='center', va='center', linespacing=1.3)

        # Action
        ax.plot([x + 0.2, x + card_w - 0.2], [4.1, 4.1],
                color=TOKENS['GRID'], linewidth=0.5)
        ax.text(x + card_w / 2, 3.7, p['action'], fontsize=7.5,
                color=TOKENS['TEXT_2'], ha='center', va='center', linespacing=1.3)

        # Quality benefit (green)
        draw_rounded_box(ax, x + 0.1, 2.5, card_w - 0.2, 0.9, '#dcfce7', alpha=0.8)
        ax.text(x + card_w / 2, 3.15, 'Quality', fontsize=6.5, fontweight='bold',
                color=TOKENS['SUCCESS'], ha='center')
        ax.text(x + card_w / 2, 2.75, p['quality'], fontsize=7,
                color=TOKENS['TEXT_2'], ha='center', va='center', linespacing=1.3)

        # Token reduction (teal)
        draw_rounded_box(ax, x + 0.1, 1.3, card_w - 0.2, 0.9, TOKENS['TEAL_BG'], alpha=0.8)
        ax.text(x + card_w / 2, 1.95, 'Tokens', fontsize=6.5, fontweight='bold',
                color=TOKENS['ACCENT_2'], ha='center')
        ax.text(x + card_w / 2, 1.55, p['tokens'], fontsize=7,
                color=TOKENS['TEXT_2'], ha='center', va='center', linespacing=1.3)

    # Footer
    draw_rounded_box(ax, start_x, 0.0, 5 * card_w + 4 * gap, 0.5, TOKENS['LIGHT_BG'])
    ax.text(6, 0.25, 'Combined: better first-attempt accuracy + 50-80% fewer tokens',
            fontsize=9, fontweight='bold', color=TOKENS['ACCENT'], ha='center', va='center')

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'context-engineering-framework.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_before_after_context():
    """Three scenarios showing accuracy UP and tokens DOWN."""
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    ax.text(5.5, 7.2, 'Less Context, Better Results: The Data', fontsize=14,
            fontweight='bold', color=TOKENS['TEXT'], ha='center')

    scenarios = [
        {
            'label': 'A: Tool-Heavy\nAgentic Workflow',
            'source': 'Anthropic Engineering',
            'before_tokens': '55,000 tokens',
            'before_accuracy': '49% accuracy',
            'after_tokens': '~500 tokens',
            'after_accuracy': '74% accuracy',
            'token_delta': '-85%',
            'quality_delta': '+25 pts',
        },
        {
            'label': 'B: Issue Resolution\n(SWEzze)',
            'source': 'SWEzze Paper',
            'before_tokens': 'Standard budget',
            'before_accuracy': 'Baseline',
            'after_tokens': '6x compressed',
            'after_accuracy': '+5-9.2% resolution',
            'token_delta': '-51-71%',
            'quality_delta': '+5-9.2%',
        },
        {
            'label': 'C: Complex Research\n(Programmatic Calling)',
            'source': 'Anthropic Engineering',
            'before_tokens': '43,588 tokens',
            'before_accuracy': '25.6% retrieval',
            'after_tokens': '27,297 tokens',
            'after_accuracy': '28.5% retrieval',
            'token_delta': '-37%',
            'quality_delta': '+2.9 pts',
        },
    ]

    row_h = 1.7
    start_y = 5.4

    # Column headers
    ax.text(1.5, start_y + 0.7, 'Scenario', fontsize=9, fontweight='bold',
            color=TOKENS['TEXT_2'], ha='center')
    ax.text(4.0, start_y + 0.7, 'Before', fontsize=9, fontweight='bold',
            color=TOKENS['WARN'], ha='center')
    ax.text(7.5, start_y + 0.7, 'After', fontsize=9, fontweight='bold',
            color=TOKENS['SUCCESS'], ha='center')
    ax.text(9.8, start_y + 0.7, 'Impact', fontsize=9, fontweight='bold',
            color=TOKENS['ACCENT'], ha='center')

    ax.plot([0.3, 10.7], [start_y + 0.4, start_y + 0.4],
            color=TOKENS['GRID'], linewidth=1)

    for i, s in enumerate(scenarios):
        y = start_y - i * row_h

        # Scenario label
        ax.text(1.5, y, s['label'], fontsize=8.5, fontweight='bold',
                color=TOKENS['TEXT'], ha='center', va='center', linespacing=1.3)
        ax.text(1.5, y - 0.55, s['source'], fontsize=7, color=TOKENS['MUTED'],
                ha='center', style='italic')

        # Before box (red)
        draw_rounded_box(ax, 2.8, y - 0.55, 2.4, 1.1, TOKENS['RED_BG'], alpha=0.6)
        ax.text(4.0, y + 0.1, s['before_tokens'], fontsize=8, color=TOKENS['TEXT'],
                ha='center', fontweight='bold')
        ax.text(4.0, y - 0.25, s['before_accuracy'], fontsize=8, color=TOKENS['WARN'],
                ha='center')

        # Arrow
        ax.annotate('', xy=(5.6, y), xytext=(5.25, y),
                    arrowprops=dict(arrowstyle='->', color=TOKENS['ACCENT'], lw=1.5))

        # After box (green)
        draw_rounded_box(ax, 5.9, y - 0.55, 2.8, 1.1, TOKENS['TEAL_BG'], alpha=0.6)
        ax.text(7.3, y + 0.1, s['after_tokens'], fontsize=8, color=TOKENS['TEXT'],
                ha='center', fontweight='bold')
        ax.text(7.3, y - 0.25, s['after_accuracy'], fontsize=8, color=TOKENS['SUCCESS'],
                ha='center')

        # Impact badges
        # Token delta
        draw_rounded_box(ax, 9.0, y + 0.0, 1.5, 0.4, TOKENS['ACCENT_2'], alpha=0.15)
        ax.text(9.75, y + 0.2, s['token_delta'], fontsize=8, fontweight='bold',
                color=TOKENS['ACCENT_2'], ha='center', va='center')
        # Quality delta
        draw_rounded_box(ax, 9.0, y - 0.55, 1.5, 0.4, TOKENS['SUCCESS'], alpha=0.15)
        ax.text(9.75, y - 0.35, s['quality_delta'], fontsize=8, fontweight='bold',
                color=TOKENS['SUCCESS'], ha='center', va='center')

        # Row separator
        if i < 2:
            ax.plot([0.3, 10.7], [y - 0.8, y - 0.8],
                    color=TOKENS['GRID'], linewidth=0.5, linestyle='--')

    # Bottom note
    ax.text(5.5, 0.2, 'Pattern: in every scenario, reducing context improved results. '
            'Less noise = more clarity, for humans and AI alike.',
            fontsize=8, color=TOKENS['TEXT_2'], ha='center', style='italic')

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'before-after-context.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


if __name__ == '__main__':
    print('Rendering Part 1 (new) visuals...')
    render_context_quality_paradox()
    render_context_engineering_framework()
    render_before_after_context()
    print('Done. 3 PNGs generated.')
