"""
Visual renderer for Part 2: "Invisible Compound Savings"
Generates 5 PNGs at 320 DPI using the shared design token system.

Visuals:
1. caching-flow.png — Sequential diagram showing 3 requests with prefix caching savings
2. retry-tax-calculator.png — Line chart of retry rate vs. effective cost multiplier
3. prompt-structure-breakdown.png — Stacked bar showing what repeats (90%) vs. what changes (10%)
4. retry-loop-anatomy.png — Flow diagram showing how vague prompts compound into retry loops
5. caching-comparison.png — Side-by-side comparison of prefix caching vs semantic caching
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


def render_caching_flow():
    """Sequential diagram showing 3 requests with prefix caching savings growing."""
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(5.5, 7.6, 'Prompt Caching: Prefix Reuse Across Requests',
            fontsize=14, fontweight='bold', color=TOKENS['TEXT'], ha='center')
    ax.text(5.5, 7.2, 'Same system prompt + instructions + file context = cached at 90% discount',
            fontsize=9, color=TOKENS['TEXT_2'], ha='center')

    requests = [
        {
            'label': 'Request 1',
            'x': 1.5,
            'prefix_color': TOKENS['WARN'],
            'prefix_label': 'Prefix: 10K tokens\n(FULL PRICE)',
            'query_label': 'Query: 500 tokens',
            'cost_label': 'Cost: $0.030',
            'note': 'Cache WRITE (1.25x)',
            'note_color': TOKENS['WARN'],
        },
        {
            'label': 'Request 2',
            'x': 4.5,
            'prefix_color': TOKENS['SUCCESS'],
            'prefix_label': 'Prefix: 10K tokens\n(CACHED - 90% off)',
            'query_label': 'Query: 500 tokens',
            'cost_label': 'Cost: $0.004',
            'note': 'Cache HIT',
            'note_color': TOKENS['SUCCESS'],
        },
        {
            'label': 'Request 10',
            'x': 7.5,
            'prefix_color': TOKENS['SUCCESS'],
            'prefix_label': 'Prefix: 10K tokens\n(CACHED - 90% off)',
            'query_label': 'Query: 500 tokens',
            'cost_label': 'Cost: $0.004',
            'note': 'Cache HIT',
            'note_color': TOKENS['SUCCESS'],
        },
    ]

    for req in requests:
        x = req['x']

        # Request label
        ax.text(x + 1, 6.5, req['label'], fontsize=11, fontweight='bold',
                color=TOKENS['TEXT'], ha='center')

        # Prefix block
        prefix_box = FancyBboxPatch((x, 4.4), 2, 1.6,
                                     boxstyle="round,pad=0.12",
                                     facecolor=req['prefix_color'],
                                     edgecolor='white', linewidth=1, alpha=0.2)
        ax.add_patch(prefix_box)
        ax.text(x + 1, 5.2, req['prefix_label'], fontsize=8,
                color=TOKENS['TEXT'], ha='center', va='center', fontweight='bold')

        # Query block
        query_box = FancyBboxPatch((x, 3.2), 2, 0.9,
                                    boxstyle="round,pad=0.12",
                                    facecolor=TOKENS['BLUE_BG'],
                                    edgecolor='white', linewidth=1)
        ax.add_patch(query_box)
        ax.text(x + 1, 3.65, req['query_label'], fontsize=8,
                color=TOKENS['TEXT'], ha='center', va='center')

        # Cost label
        ax.text(x + 1, 2.6, req['cost_label'], fontsize=10, fontweight='bold',
                color=TOKENS['TEXT'], ha='center')

        # Note
        ax.text(x + 1, 2.2, req['note'], fontsize=8,
                color=req['note_color'], ha='center', fontweight='bold')

    # Arrow between request 1 and 2
    ax.annotate('', xy=(4.3, 5.2), xytext=(3.7, 5.2),
                arrowprops=dict(arrowstyle='->', color=TOKENS['MUTED'], lw=1.5))

    # Arrow between request 2 and 10
    ax.annotate('', xy=(7.3, 5.2), xytext=(6.7, 5.2),
                arrowprops=dict(arrowstyle='->', color=TOKENS['MUTED'], lw=1.5))
    ax.text(7.0, 5.6, '...', fontsize=14, color=TOKENS['MUTED'], ha='center')

    # Cumulative savings box at bottom
    savings_box = FancyBboxPatch((1.5, 0.4), 8, 1.2,
                                  boxstyle="round,pad=0.15",
                                  facecolor=TOKENS['TEAL_BG'],
                                  edgecolor=TOKENS['ACCENT_2'], linewidth=1.5)
    ax.add_patch(savings_box)
    ax.text(5.5, 1.15, 'After 100 requests: ~89% savings on prefix tokens',
            fontsize=11, fontweight='bold', color=TOKENS['TEXT'], ha='center')
    ax.text(5.5, 0.7, '1,000,000 tokens at full price -> 109,000 effective tokens with caching',
            fontsize=8.5, color=TOKENS['TEXT_2'], ha='center')

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'caching-flow.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_retry_tax_calculator():
    """Line chart showing how retry rate multiplies effective cost."""
    fig, ax = plt.subplots(figsize=(9, 5.5))

    retry_rates = np.arange(0, 65, 5)
    cost_multipliers = 1 + retry_rates / 100

    # Main line
    ax.plot(retry_rates, cost_multipliers, color=TOKENS['ACCENT'], linewidth=2.5,
            marker='o', markersize=5, markerfacecolor=TOKENS['ACCENT'], zorder=3)

    # Highlight danger zone (30-50%)
    danger_mask = (retry_rates >= 30) & (retry_rates <= 50)
    ax.fill_between(retry_rates, 1, cost_multipliers,
                    where=danger_mask, alpha=0.15, color=TOKENS['WARN'],
                    label='Most developers operate here')

    # Annotation for danger zone
    ax.annotate('Most developers\noperate here',
                xy=(40, 1.4), xytext=(52, 1.25),
                fontsize=9, fontweight='bold', color=TOKENS['WARN'],
                ha='center',
                arrowprops=dict(arrowstyle='->', color=TOKENS['WARN'], lw=1.5))

    # Annotation for context engineering effect
    ax.annotate('Context engineering\nreduces retry rate',
                xy=(15, 1.15), xytext=(8, 1.4),
                fontsize=8.5, fontweight='bold', color=TOKENS['SUCCESS'],
                ha='center',
                arrowprops=dict(arrowstyle='->', color=TOKENS['SUCCESS'], lw=1.5))

    # Monthly cost labels on right axis
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    monthly_ticks = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
    monthly_labels = [f'${30 * t:.0f}/mo' for t in monthly_ticks]
    ax2.set_yticks(monthly_ticks)
    ax2.set_yticklabels(monthly_labels, fontsize=8, color=TOKENS['TEXT_2'])
    ax2.set_ylabel('Monthly cost (100 req/day, $0.01 avg)',
                   fontsize=9, color=TOKENS['TEXT_2'])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_color(TOKENS['GRID'])
    ax2.tick_params(axis='y', colors=TOKENS['TEXT_2'])

    # Formatting
    ax.set_xlabel('Retry Rate (%)', fontsize=10, color=TOKENS['TEXT_2'])
    ax.set_ylabel('Effective Cost Multiplier', fontsize=10, color=TOKENS['TEXT_2'])
    ax.set_xlim(-2, 62)
    ax.set_ylim(0.95, 1.65)

    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}x'))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(TOKENS['GRID'])
    ax.spines['bottom'].set_color(TOKENS['GRID'])
    ax.tick_params(axis='both', colors=TOKENS['TEXT_2'])

    ax.grid(axis='y', color=TOKENS['GRID'], linewidth=0.5, alpha=0.7)

    ax.set_title('The Retry Tax: How Retry Rate Multiplies Effective Cost',
                 fontsize=13, fontweight='bold', color=TOKENS['TEXT'], pad=15)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'retry-tax-calculator.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_prompt_structure_breakdown():
    """Stacked bar showing what repeats (~90%) vs what changes (~10%) in a typical AI coding prompt.
    Uses external labels with leader lines for narrow segments to prevent text overflow."""
    fig, ax = plt.subplots(figsize=(12, 6.5))

    segments = [
        ('System prompt', 2000, TOKENS['MUTED']),
        ('copilot-instructions.md', 2500, TOKENS['ACCENT']),
        ('Active file content', 3500, TOKENS['ACCENT_2']),
        ('Thread history', 1500, TOKENS['ACCENT_3']),
        ('Your new question', 500, TOKENS['WARN']),
    ]

    bar_y = 3.5
    bar_height = 1.2
    total = sum(s[1] for s in segments)

    # Draw segments as rectangles (not barh) for precise control
    ax.set_xlim(-0.5, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(6, 6.5, 'What Repeats vs. What Changes in Your AI Coding Session',
            fontsize=14, fontweight='bold', color=TOKENS['TEXT'], ha='center')

    # Scale: map 10,000 tokens to 10 units of x-axis width
    scale = 10.0 / total
    x = 0.5

    label_positions = []  # collect for external labels

    for label, size, color in segments:
        w = size * scale
        rect = plt.Rectangle((x, bar_y), w, bar_height, facecolor=color,
                               edgecolor='white', linewidth=2, alpha=0.85)
        ax.add_patch(rect)

        # Token count inside the bar (small, always fits)
        ax.text(x + w / 2, bar_y + bar_height / 2,
                f'{size:,}', ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')

        label_positions.append((x + w / 2, label, size, color))
        x += w

    # External labels above and below the bar with leader lines
    # Top labels for first 3 segments (wide enough, place above)
    for i, (cx, label, size, color) in enumerate(label_positions[:3]):
        y_label = bar_y + bar_height + 0.4 + (i % 2) * 0.7  # stagger to avoid overlap
        ax.annotate(f'{label}\n({size:,} tokens)',
                    xy=(cx, bar_y + bar_height), xytext=(cx, y_label),
                    ha='center', va='bottom', fontsize=9, fontweight='bold',
                    color=TOKENS['TEXT'],
                    arrowprops=dict(arrowstyle='-', color=TOKENS['MUTED'], lw=0.8))

    # Bottom labels for last 2 segments (narrow, place below with offset)
    for i, (cx, label, size, color) in enumerate(label_positions[3:]):
        x_offset = -0.8 + i * 1.6  # spread them apart
        y_label = bar_y - 0.5 - (i % 2) * 0.7
        ax.annotate(f'{label}\n({size:,} tokens)',
                    xy=(cx, bar_y), xytext=(cx + x_offset, y_label),
                    ha='center', va='top', fontsize=9, fontweight='bold',
                    color=TOKENS['TEXT'],
                    arrowprops=dict(arrowstyle='-', color=TOKENS['MUTED'], lw=0.8))

    # Cacheable prefix bracket
    prefix_end = 0.5 + (total - 500) * scale
    bar_bottom = bar_y - 0.05

    # Green bracket line for cacheable prefix
    bracket_y = 1.2
    ax.plot([0.5, prefix_end], [bracket_y, bracket_y], color=TOKENS['SUCCESS'], lw=2.5)
    ax.plot([0.5, 0.5], [bracket_y - 0.1, bracket_y + 0.1], color=TOKENS['SUCCESS'], lw=2.5)
    ax.plot([prefix_end, prefix_end], [bracket_y - 0.1, bracket_y + 0.1], color=TOKENS['SUCCESS'], lw=2.5)
    ax.text((0.5 + prefix_end) / 2, 0.7,
            'CACHEABLE PREFIX (~90%) -- 90% off after first request',
            ha='center', fontsize=10, fontweight='bold', color=TOKENS['SUCCESS'])

    # Red bracket for unique portion
    unique_start = prefix_end
    unique_end = 0.5 + total * scale
    ax.plot([unique_start, unique_end], [bracket_y, bracket_y], color=TOKENS['WARN'], lw=2.5)
    ax.plot([unique_start, unique_start], [bracket_y - 0.1, bracket_y + 0.1], color=TOKENS['WARN'], lw=2.5)
    ax.plot([unique_end, unique_end], [bracket_y - 0.1, bracket_y + 0.1], color=TOKENS['WARN'], lw=2.5)
    ax.text((unique_start + unique_end) / 2, 0.7,
            'UNIQUE (~10%)', ha='center', fontsize=9, fontweight='bold', color=TOKENS['WARN'])

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'prompt-structure-breakdown.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_retry_loop_anatomy():
    """Flow diagram showing how vague prompts trigger retry loops that compound cost."""
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6)
    ax.axis('off')

    ax.text(5.5, 5.6, 'Anatomy of the Retry Loop',
            fontsize=14, fontweight='bold', color=TOKENS['TEXT'], ha='center')

    # Step boxes
    steps = [
        (1.2, 3.0, 'Vague\nprompt', TOKENS['RED_BG'], TOKENS['WARN']),
        (3.4, 3.0, 'Confused\noutput', TOKENS['RED_BG'], TOKENS['WARN']),
        (5.6, 3.0, '"Try again"\n+ more context', TOKENS['RED_BG'], TOKENS['WARN']),
        (7.8, 3.0, 'Fights old\nresponse', TOKENS['RED_BG'], TOKENS['WARN']),
        (10.0, 3.0, 'Another\nretry...', TOKENS['RED_BG'], TOKENS['WARN']),
    ]

    for x, y, text, bg, border in steps:
        box = FancyBboxPatch((x - 0.8, y - 0.5), 1.6, 1.0,
                              boxstyle="round,pad=0.12", facecolor=bg,
                              edgecolor=border, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=8,
                color=TOKENS['TEXT'], fontweight='bold')

    # Arrows
    for i in range(len(steps) - 1):
        ax.annotate('', xy=(steps[i+1][0] - 0.85, steps[i+1][1]),
                    xytext=(steps[i][0] + 0.85, steps[i][1]),
                    arrowprops=dict(arrowstyle='->', color=TOKENS['WARN'], lw=1.5))

    # Cost labels
    costs = ['$0.01', '$0.01', '$0.01', '$0.01', '$0.01']
    for i, (x, y, _, _, _) in enumerate(steps):
        ax.text(x, y - 0.75, costs[i], ha='center', fontsize=8,
                color=TOKENS['WARN'], fontweight='bold')

    ax.text(5.5, 1.6, 'Total: $0.05 for ONE successful result  (5x the cost of getting it right the first time)',
            ha='center', fontsize=10, fontweight='bold', color=TOKENS['WARN'])

    # Better path
    better_box = FancyBboxPatch((1.5, 0.2), 8, 0.8,
                                 boxstyle="round,pad=0.12", facecolor=TOKENS['TEAL_BG'],
                                 edgecolor=TOKENS['ACCENT_2'], linewidth=1.5)
    ax.add_patch(better_box)
    ax.text(5.5, 0.6, 'Better path: Specific prompt + clean context + #file reference = $0.01 (first attempt)',
            ha='center', fontsize=9, fontweight='bold', color=TOKENS['ACCENT_2'])

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'retry-loop-anatomy.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_caching_comparison():
    """Side-by-side comparison of prefix caching vs semantic caching."""
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5, 6.6, 'Prefix Caching vs. Semantic Caching',
            fontsize=14, fontweight='bold', color=TOKENS['TEXT'], ha='center')

    # Column headers
    ax.text(2.5, 5.9, 'Prefix Caching', fontsize=12, fontweight='bold',
            color=TOKENS['SUCCESS'], ha='center')
    ax.text(7.5, 5.9, 'Semantic Caching', fontsize=12, fontweight='bold',
            color=TOKENS['ACCENT_3'], ha='center')

    rows = [
        ('Setup effort', 'Nearly zero -- automatic', 'High -- embedding pipelines,\nthreshold tuning'),
        ('How it works', 'Caches identical prefixes\n(same system prompt + instructions)', 'Caches similar queries\n(embedding similarity match)'),
        ('Savings', '90% on repeated prefixes', '68.8% fewer API calls'),
        ('Risk', 'Minimal -- cache just\nexpires after TTL', 'Cache staleness, wrong\nanswers from similar-but-different'),
        ('Best for', 'Every developer.\nWorks automatically.', 'High-volume teams with\nrepetitive query patterns.'),
    ]

    for i, (label, left, right) in enumerate(rows):
        y = 5.1 - i * 1.0

        # Row background
        if i % 2 == 0:
            rect = plt.Rectangle((0.2, y - 0.35), 9.6, 0.7,
                                  facecolor=TOKENS['LIGHT_BG'], edgecolor='none')
            ax.add_patch(rect)

        ax.text(0.3, y, label, fontsize=8.5, fontweight='bold',
                color=TOKENS['TEXT'], va='center')
        ax.text(2.5, y, left, fontsize=8, color=TOKENS['TEXT_2'],
                va='center', ha='center', linespacing=1.3)
        ax.text(7.5, y, right, fontsize=8, color=TOKENS['TEXT_2'],
                va='center', ha='center', linespacing=1.3)

    # Recommendation box
    rec_box = FancyBboxPatch((0.5, 0.1), 9, 0.6,
                              boxstyle="round,pad=0.1", facecolor=TOKENS['TEAL_BG'],
                              edgecolor=TOKENS['ACCENT_2'], linewidth=1.5)
    ax.add_patch(rec_box)
    ax.text(5, 0.4, 'Recommendation: Start with prefix caching (free). Add semantic caching only when scale justifies engineering investment.',
            ha='center', fontsize=8.5, fontweight='bold', color=TOKENS['ACCENT_2'])

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'caching-comparison.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


if __name__ == '__main__':
    print('Rendering Part 2 visuals...')
    render_caching_flow()
    render_retry_tax_calculator()
    render_prompt_structure_breakdown()
    render_retry_loop_anatomy()
    render_caching_comparison()
    print('Done. 5 PNGs generated.')
