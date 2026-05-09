"""
Visual for 'The 30-70% Problem' section.
Renders: context-noise-breakdown.png — stacked bar showing noise categories
as proportion of a typical AI code assistant context window.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
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


def draw_rounded_box(ax, x, y, w, h, color, alpha=1.0, ec=None):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                         facecolor=color, edgecolor=ec or TOKENS['GRID'],
                         linewidth=0.8, alpha=alpha)
    ax.add_patch(box)
    return box


def render_context_noise_breakdown():
    """Stacked bar showing noise categories in a typical context window."""
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Title
    ax.text(5.5, 8.2, 'The 30-70% Problem', fontsize=15, fontweight='bold',
            color=TOKENS['TEXT'], ha='center')
    ax.text(5.5, 7.8, '30-70% of typical AI prompt context is noise that actively degrades output',
            fontsize=9, color=TOKENS['TEXT_2'], ha='center', style='italic')

    # ========== LEFT: Typical unoptimized context bar ==========
    bar_x = 1.0
    bar_w = 3.5
    total_h = 6.0
    bar_y = 0.8

    # Label
    ax.text(bar_x + bar_w / 2, bar_y + total_h + 0.3, 'Typical Context Window',
            fontsize=10, fontweight='bold', color=TOKENS['TEXT'], ha='center')
    ax.text(bar_x + bar_w / 2, bar_y + total_h + 0.0, '(unoptimized)',
            fontsize=8, color=TOKENS['MUTED'], ha='center')

    # Segments (bottom to top): useful signal, then three noise types
    segments = [
        {'label': 'Useful Signal', 'pct': 35, 'color': TOKENS['SUCCESS'],
         'bg': '#dcfce7', 'detail': 'Relevant files, current prompt,\nproject instructions'},
        {'label': 'Stale Context', 'pct': 22, 'color': '#ea580c',
         'bg': '#fff7ed', 'detail': 'Old chat messages, files from\nprevious tasks, outdated instructions'},
        {'label': 'Redundant Context', 'pct': 18, 'color': TOKENS['WARN'],
         'bg': TOKENS['RED_BG'], 'detail': 'Same info loaded via file +\nchat reference + tool definition'},
        {'label': 'Irrelevant Context', 'pct': 25, 'color': TOKENS['ACCENT_3'],
         'bg': TOKENS['PURPLE_BG'], 'detail': 'Unused tool definitions,\nunrelated open files, config noise'},
    ]

    y_cursor = bar_y
    for seg in segments:
        seg_h = total_h * seg['pct'] / 100
        draw_rounded_box(ax, bar_x, y_cursor, bar_w, seg_h - 0.05,
                         seg['bg'], alpha=0.85, ec=seg['color'])

        # Percentage badge
        mid_y = y_cursor + seg_h / 2
        ax.text(bar_x + 0.3, mid_y, f"{seg['pct']}%", fontsize=11,
                fontweight='bold', color=seg['color'], va='center')
        ax.text(bar_x + 1.1, mid_y + 0.1, seg['label'], fontsize=9,
                fontweight='bold', color=TOKENS['TEXT'], va='center')
        ax.text(bar_x + 1.1, mid_y - 0.25, seg['detail'], fontsize=7,
                color=TOKENS['TEXT_2'], va='center', linespacing=1.3)

        y_cursor += seg_h

    # Noise bracket on the right side of bar
    noise_bottom = bar_y + total_h * 0.35
    noise_top = bar_y + total_h
    bracket_x = bar_x + bar_w + 0.2

    ax.plot([bracket_x, bracket_x + 0.15, bracket_x + 0.15, bracket_x],
            [noise_bottom, noise_bottom, noise_top, noise_top],
            color=TOKENS['WARN'], linewidth=1.5)
    ax.text(bracket_x + 0.35, (noise_bottom + noise_top) / 2,
            '65%\nnoise', fontsize=11, fontweight='bold',
            color=TOKENS['WARN'], va='center')

    # ========== RIGHT: Three proof points ==========
    proof_x = 6.2
    proof_w = 4.3

    ax.text(proof_x + proof_w / 2, 7.4, 'What the Data Shows',
            fontsize=11, fontweight='bold', color=TOKENS['TEXT'], ha='center')

    proofs = [
        {
            'icon': 'Anthropic',
            'stat': '55K-134K tokens',
            'detail': 'of tool definitions per request.\nMost tools unused. After Tool Search:\n~500 tokens. Accuracy: 49% -> 74%.',
            'color': TOKENS['ACCENT'],
            'bg': TOKENS['BLUE_BG'],
        },
        {
            'icon': 'SWEzze',
            'stat': '6x compression',
            'detail': '51-71% fewer tokens AND\n5-9.2% better issue resolution.\nNoise removal improved results.',
            'color': TOKENS['ACCENT_2'],
            'bg': TOKENS['TEAL_BG'],
        },
        {
            'icon': 'TDS Analysis',
            'stat': '$6,000/month',
            'detail': 'wasted on junk context at 40K\ncontext window with 100K daily runs.\nPure waste, zero value.',
            'color': TOKENS['WARN'],
            'bg': TOKENS['RED_BG'],
        },
    ]

    card_h = 1.7
    card_gap = 0.3
    proof_start_y = 6.8 - card_h

    for i, p in enumerate(proofs):
        cy = proof_start_y - i * (card_h + card_gap)
        draw_rounded_box(ax, proof_x, cy, proof_w, card_h, p['bg'], alpha=0.5)

        # Source badge
        draw_rounded_box(ax, proof_x + 0.15, cy + card_h - 0.5, 1.5, 0.35,
                         p['color'], alpha=0.15)
        ax.text(proof_x + 0.9, cy + card_h - 0.32, p['icon'], fontsize=7.5,
                fontweight='bold', color=p['color'], ha='center', va='center')

        # Stat
        ax.text(proof_x + 0.3, cy + card_h - 0.8, p['stat'], fontsize=11,
                fontweight='bold', color=p['color'])

        # Detail
        ax.text(proof_x + 0.3, cy + 0.3, p['detail'], fontsize=7.5,
                color=TOKENS['TEXT_2'], va='center', linespacing=1.4)

    # ========== Bottom takeaway ==========
    draw_rounded_box(ax, 0.5, 0.0, 10, 0.55, TOKENS['LIGHT_BG'])
    ax.text(5.5, 0.27, 'Removing noise does not sacrifice information. '
            'It gives the model clarity. Less noise = better output + fewer tokens.',
            fontsize=8.5, fontweight='bold', color=TOKENS['ACCENT'], ha='center', va='center')

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'context-noise-breakdown.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


if __name__ == '__main__':
    print('Rendering noise breakdown visual...')
    render_context_noise_breakdown()
    print('Done.')
