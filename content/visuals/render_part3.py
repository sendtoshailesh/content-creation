"""
Visual renderer for Part 3: "The 120x Spread"
Generates 5 PNGs at 320 DPI using the shared design token system.

Visuals:
1. task-model-alignment.png — Three-tier task/model matching diagram with cost math
2. team-governance-dashboard.png — Mock dashboard with credit consumption charts
3. three-layer-stack.png — Stacked architecture diagram (context -> caching -> model selection)
4. routing-decision-comparison.png — Auto-selection vs manual routing decision flow
5. team-optimization-strategies.png — Training vs restriction outcomes comparison
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


def render_task_model_alignment():
    """Three-tier diagram matching task complexity to model tiers with cost math."""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Title
    ax.text(6, 8.6, 'Task-Model Alignment: Match Capability to Complexity',
            fontsize=14, fontweight='bold', color=TOKENS['TEXT'], ha='center')
    ax.text(6, 8.2, '60-70% of coding tasks need zero or near-zero cost models',
            fontsize=9, color=TOKENS['TEXT_2'], ha='center')

    tiers = [
        {
            'y': 6.2, 'height': 1.5,
            'color': TOKENS['TEAL_BG'], 'border': TOKENS['ACCENT_2'],
            'title': 'Tier 1: SIMPLE (60-70%)',
            'tasks': 'Variable rename, boilerplate, test scaffold,\ndocstrings, imports, lint fixes, syntax Q&A',
            'models': 'GPT-4.1 (0x)  |  GPT-5 mini (0x)\nGPT-5.4 nano (0.25x)  |  Haiku 4.5 (0.33x)',
            'cost_label': '0x - 0.33x',
            'badge_color': TOKENS['SUCCESS'],
        },
        {
            'y': 4.0, 'height': 1.5,
            'color': TOKENS['BLUE_BG'], 'border': TOKENS['ACCENT'],
            'title': 'Tier 2: MODERATE (20-30%)',
            'tasks': 'Code review, refactoring, debugging,\narchitecture Q&A, multi-file understanding',
            'models': 'Claude Sonnet 4/4.5/4.6 (1x)\nGemini 2.5 Pro (1x)  |  GPT-5.2 (1x)',
            'cost_label': '1x',
            'badge_color': TOKENS['ACCENT'],
        },
        {
            'y': 1.8, 'height': 1.5,
            'color': TOKENS['PURPLE_BG'], 'border': TOKENS['ACCENT_3'],
            'title': 'Tier 3: COMPLEX (5-10%)',
            'tasks': 'Multi-file refactor with dependencies,\nnovel algorithms, system design, deep reasoning',
            'models': 'Claude Opus 4.5 (3x)\nReserve 7.5x+ for exceptional cases',
            'cost_label': '3x+',
            'badge_color': TOKENS['ACCENT_3'],
        },
    ]

    for tier in tiers:
        y = tier['y']
        h = tier['height']

        # Main box
        box = FancyBboxPatch((0.5, y), 8, h,
                              boxstyle="round,pad=0.15",
                              facecolor=tier['color'],
                              edgecolor=tier['border'], linewidth=1.5)
        ax.add_patch(box)

        # Title
        ax.text(0.8, y + h - 0.25, tier['title'], fontsize=10, fontweight='bold',
                color=TOKENS['TEXT'], va='top')

        # Tasks
        ax.text(0.8, y + h - 0.65, tier['tasks'], fontsize=8,
                color=TOKENS['TEXT_2'], va='top', linespacing=1.4)

        # Models (right side of box)
        ax.text(8.2, y + h/2, tier['models'], fontsize=7.5,
                color=TOKENS['TEXT'], va='center', ha='right',
                style='italic', linespacing=1.4)

    # Cost math box on the right
    math_box = FancyBboxPatch((9, 2.5), 2.8, 5.0,
                               boxstyle="round,pad=0.2",
                               facecolor=TOKENS['LIGHT_BG'],
                               edgecolor=TOKENS['GRID'], linewidth=1.5)
    ax.add_patch(math_box)

    ax.text(10.4, 7.1, 'COST MATH', fontsize=10, fontweight='bold',
            color=TOKENS['TEXT'], ha='center')
    ax.text(10.4, 6.65, '100 requests/day:', fontsize=8,
            color=TOKENS['TEXT_2'], ha='center')

    math_lines = [
        ('65 simple @ 0x', TOKENS['SUCCESS'], 6.2),
        ('= 0 credits', TOKENS['SUCCESS'], 5.85),
        ('', None, 5.6),
        ('25 moderate @ 1x', TOKENS['ACCENT'], 5.4),
        ('= 0.25x weighted', TOKENS['ACCENT'], 5.05),
        ('', None, 4.8),
        ('10 complex @ 3x', TOKENS['ACCENT_3'], 4.6),
        ('= 0.30x weighted', TOKENS['ACCENT_3'], 4.25),
        ('', None, 3.9),
        ('Effective avg:', TOKENS['TEXT'], 3.6),
        ('0.55x', TOKENS['TEXT'], 3.2),
        ('vs 1.0x baseline', TOKENS['TEXT_2'], 2.85),
    ]

    for text, color, y_pos in math_lines:
        if text:
            weight = 'bold' if 'Effective' in text or text == '0.55x' else 'normal'
            size = 12 if text == '0.55x' else 8
            ax.text(10.4, y_pos, text, fontsize=size, color=color,
                    ha='center', fontweight=weight)

    # 45% savings callout
    savings_box = FancyBboxPatch((9.2, 2.6), 2.4, 0.7,
                                  boxstyle="round,pad=0.1",
                                  facecolor=TOKENS['TEAL_BG'],
                                  edgecolor=TOKENS['ACCENT_2'], linewidth=1)
    ax.add_patch(savings_box)
    ax.text(10.4, 3.0, '45% savings', fontsize=11, fontweight='bold',
            color=TOKENS['ACCENT_2'], ha='center')
    ax.text(10.4, 2.72, 'on model costs', fontsize=7.5,
            color=TOKENS['TEXT_2'], ha='center')

    # Volatile disclaimer
    ax.text(6, 0.5, '[VOLATILE] Model multipliers and included models are subject to change. '
            'Route by task complexity, not specific multiplier values.',
            fontsize=7, color=TOKENS['MUTED'], ha='center', style='italic')

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'task-model-alignment.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_team_governance_dashboard():
    """Mock dashboard showing credit consumption, model distribution, top workflows."""
    fig = plt.figure(figsize=(12, 7))

    # Title
    fig.text(0.5, 0.96, 'Team AI Credit Governance Dashboard',
             fontsize=14, fontweight='bold', color=TOKENS['TEXT'], ha='center')
    fig.text(0.5, 0.93, 'Visibility into AI consumption patterns under usage-based billing',
             fontsize=9, color=TOKENS['TEXT_2'], ha='center')

    # --- Panel 1: Credit consumption by developer (bar chart) ---
    ax1 = fig.add_axes([0.06, 0.5, 0.42, 0.38])

    developers = ['Dev A', 'Dev B', 'Dev C', 'Dev D', 'Dev E']
    credits = [18.5, 14.2, 11.8, 8.3, 5.1]
    colors = [TOKENS['WARN'] if c > 15 else TOKENS['ACCENT'] if c > 10 else TOKENS['ACCENT_2']
              for c in credits]

    bars = ax1.barh(developers, credits, color=colors, height=0.5, edgecolor='white')
    for bar, val in zip(bars, credits):
        ax1.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'${val:.1f}', va='center', fontsize=8, color=TOKENS['TEXT'])

    ax1.set_xlim(0, 25)
    ax1.set_xlabel('Credits consumed', fontsize=8, color=TOKENS['TEXT_2'])
    ax1.set_title('Credits by Developer', fontsize=10, fontweight='bold',
                  color=TOKENS['TEXT'], pad=8)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color(TOKENS['GRID'])
    ax1.spines['bottom'].set_color(TOKENS['GRID'])
    ax1.tick_params(axis='both', labelsize=8, colors=TOKENS['TEXT_2'])

    # Budget line
    ax1.axvline(x=19, color=TOKENS['WARN'], linestyle='--', linewidth=1, alpha=0.7)
    ax1.text(19.3, 4.5, 'Budget\n($19)', fontsize=7, color=TOKENS['WARN'], va='top')

    # --- Panel 2: Model usage distribution (pie chart) ---
    ax2 = fig.add_axes([0.55, 0.5, 0.38, 0.38])

    model_labels = ['Included (0x)\n62%', 'Budget (0.25-0.33x)\n15%',
                    'Standard (1x)\n18%', 'Premium (3x+)\n5%']
    model_sizes = [62, 15, 18, 5]
    model_colors = [TOKENS['SUCCESS'], TOKENS['ACCENT_2'], TOKENS['ACCENT'], TOKENS['ACCENT_3']]

    wedges, texts = ax2.pie(model_sizes, colors=model_colors,
                            startangle=90, labels=model_labels,
                            labeldistance=1.15,
                            wedgeprops=dict(edgecolor='white', linewidth=2))
    for text in texts:
        text.set_fontsize(7.5)
        text.set_color(TOKENS['TEXT_2'])

    ax2.set_title('Model Usage Distribution', fontsize=10, fontweight='bold',
                  color=TOKENS['TEXT'], pad=8)

    # --- Panel 3: Top consuming workflows (table) ---
    ax3 = fig.add_axes([0.06, 0.06, 0.42, 0.35])
    ax3.axis('off')

    ax3.text(0.0, 0.95, 'Top 5 Token-Consuming Workflows', fontsize=10,
             fontweight='bold', color=TOKENS['TEXT'], transform=ax3.transAxes)

    table_data = [
        ['Workflow', 'Tokens/day', 'Model', 'Action'],
        ['Agent: auth refactor', '145K', 'Opus 4.5', 'Review context'],
        ['Chat: API debugging', '89K', 'Sonnet 4.6', 'OK'],
        ['Agent: test generation', '72K', 'GPT-4.1', 'OK (free)'],
        ['Chat: code review', '58K', 'Sonnet 4.6', 'OK'],
        ['Chat: boilerplate', '41K', 'Sonnet 4.6', 'Switch to 0x'],
    ]

    for i, row in enumerate(table_data):
        y = 0.85 - i * 0.15
        weight = 'bold' if i == 0 else 'normal'
        color = TOKENS['TEXT'] if i == 0 else TOKENS['TEXT_2']
        bg_color = TOKENS['LIGHT_BG'] if i == 0 else ('white' if i % 2 == 0 else TOKENS['LIGHT_BG'])

        if i > 0:
            rect = plt.Rectangle((0, y - 0.06), 1, 0.14,
                                  transform=ax3.transAxes,
                                  facecolor=bg_color, edgecolor='none')
            ax3.add_patch(rect)

        for j, cell in enumerate(row):
            x = [0.0, 0.42, 0.60, 0.80][j]
            cell_color = color
            if i > 0 and j == 3:
                cell_color = TOKENS['WARN'] if 'Review' in cell or 'Switch' in cell else TOKENS['SUCCESS']
            ax3.text(x, y, cell, fontsize=7.5, fontweight=weight,
                    color=cell_color, transform=ax3.transAxes, va='center')

    # --- Panel 4: Budget utilization gauge ---
    ax4 = fig.add_axes([0.58, 0.08, 0.35, 0.3])

    utilization = 0.61  # 61% of budget used
    theta = np.linspace(np.pi, 0, 100)

    # Background arc
    ax4.plot(np.cos(theta), np.sin(theta), color=TOKENS['GRID'], linewidth=15,
             solid_capstyle='round')

    # Filled arc
    fill_theta = np.linspace(np.pi, np.pi - (utilization * np.pi), 100)
    fill_color = TOKENS['SUCCESS'] if utilization < 0.7 else (TOKENS['WARN'] if utilization < 0.9 else TOKENS['WARN'])
    ax4.plot(np.cos(fill_theta), np.sin(fill_theta), color=fill_color, linewidth=15,
             solid_capstyle='round')

    ax4.text(0, 0.15, '61%', fontsize=22, fontweight='bold', color=TOKENS['TEXT'],
            ha='center', va='center')
    ax4.text(0, -0.15, 'Budget used', fontsize=9, color=TOKENS['TEXT_2'],
            ha='center', va='center')
    ax4.text(0, -0.35, '\$11.59 of \$19.00', fontsize=8, color=TOKENS['MUTED'],
            ha='center', va='center')

    ax4.set_xlim(-1.3, 1.3)
    ax4.set_ylim(-0.5, 1.3)
    ax4.axis('off')
    ax4.set_title('Monthly Budget', fontsize=10, fontweight='bold',
                  color=TOKENS['TEXT'], pad=5)

    plt.savefig(os.path.join(OUT_DIR, 'team-governance-dashboard.png'),
                dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {os.path.join(OUT_DIR, "team-governance-dashboard.png")}')


def render_three_layer_stack():
    """Stacked architecture diagram: context -> caching -> model selection with cumulative savings."""
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Title
    ax.text(5.5, 8.6, 'The Optimization Stack',
            fontsize=15, fontweight='bold', color=TOKENS['TEXT'], ha='center')
    ax.text(5.5, 8.2, 'Three layers that compound: start from the bottom',
            fontsize=9, color=TOKENS['TEXT_2'], ha='center')

    layers = [
        {
            'y': 1.0, 'height': 1.8,
            'color': TOKENS['TEAL_BG'], 'border': TOKENS['ACCENT_2'],
            'title': 'LAYER 1: Context Engineering',
            'subtitle': 'Quality-first. Works even if AI is free.',
            'items': '- Close irrelevant files  - One thread per task  - #file references\n'
                     '- Front-load intent  - Stable copilot-instructions.md',
            'savings': '50-85%\ntoken reduction',
            'savings_color': TOKENS['ACCENT_2'],
        },
        {
            'y': 3.2, 'height': 1.8,
            'color': TOKENS['BLUE_BG'], 'border': TOKENS['ACCENT'],
            'title': 'LAYER 2: Caching + Workflow Discipline',
            'subtitle': 'Structural. Set once, compounds forever.',
            'items': '- Prefix caching (90% off repeated context)  - Thread-per-task = cache hits\n'
                     '- Diagnose before retrying  - Stable context first, query last',
            'savings': 'Up to 90%\non repeated prefix',
            'savings_color': TOKENS['ACCENT'],
        },
        {
            'y': 5.4, 'height': 1.8,
            'color': TOKENS['PURPLE_BG'], 'border': TOKENS['ACCENT_3'],
            'title': 'LAYER 3: Informed Model Selection',
            'subtitle': 'Cost-aware. Matches capability to task.',
            'items': '- 60-70% simple tasks -> free/cheap models  - 20-30% moderate -> standard (1x)\n'
                     '- 5-10% complex -> premium (3x)  - Auto-selection for 10% discount',
            'savings': '45-75%\non model costs',
            'savings_color': TOKENS['ACCENT_3'],
        },
    ]

    for layer in layers:
        y = layer['y']
        h = layer['height']

        # Main box
        box = FancyBboxPatch((0.5, y), 7.5, h,
                              boxstyle="round,pad=0.15",
                              facecolor=layer['color'],
                              edgecolor=layer['border'], linewidth=2)
        ax.add_patch(box)

        # Title
        ax.text(0.8, y + h - 0.25, layer['title'], fontsize=11, fontweight='bold',
                color=TOKENS['TEXT'], va='top')

        # Subtitle
        ax.text(0.8, y + h - 0.55, layer['subtitle'], fontsize=8,
                color=TOKENS['TEXT_2'], va='top', style='italic')

        # Items
        ax.text(0.8, y + h - 0.95, layer['items'], fontsize=7.5,
                color=TOKENS['TEXT'], va='top', linespacing=1.5)

    # Right side: cumulative savings
    savings_x = 8.7

    ax.text(savings_x + 0.8, 7.7, 'CUMULATIVE\nSAVINGS', fontsize=9, fontweight='bold',
            color=TOKENS['TEXT'], ha='center', va='center', linespacing=1.3)

    cumulative = [
        {'y': 1.9, 'label': 'Layer 1 alone', 'value': '50-85%', 'color': TOKENS['ACCENT_2']},
        {'y': 4.1, 'label': 'Layers 1+2', 'value': '60-90%', 'color': TOKENS['ACCENT']},
        {'y': 6.3, 'label': 'Layers 1+2+3', 'value': '70-90%+', 'color': TOKENS['ACCENT_3']},
    ]

    for item in cumulative:
        # Savings box
        sbox = FancyBboxPatch((savings_x, item['y'] - 0.4), 1.6, 0.8,
                               boxstyle="round,pad=0.1",
                               facecolor=item['color'],
                               edgecolor='white', linewidth=1, alpha=0.2)
        ax.add_patch(sbox)
        ax.text(savings_x + 0.8, item['y'] + 0.1, item['value'],
                fontsize=12, fontweight='bold', color=item['color'],
                ha='center', va='center')
        ax.text(savings_x + 0.8, item['y'] - 0.2, item['label'],
                fontsize=7, color=TOKENS['TEXT_2'],
                ha='center', va='center')

    # Upward arrows between layers
    for y_start, y_end in [(2.8, 3.2), (5.0, 5.4)]:
        ax.annotate('', xy=(4.25, y_end), xytext=(4.25, y_start),
                    arrowprops=dict(arrowstyle='->', color=TOKENS['MUTED'], lw=2))

    # Bottom annotation
    ax.text(5.5, 0.4, 'Start with Layer 1 (free, quality-first). '
            'Each layer multiplies the savings of the layers below it.',
            fontsize=8.5, color=TOKENS['TEXT_2'], ha='center', style='italic')

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'three-layer-stack.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_routing_decision_comparison():
    """Side-by-side: auto-selection vs manual routing — when to use each."""
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5, 6.6, 'Auto-Selection vs. Manual Routing',
            fontsize=14, fontweight='bold', color=TOKENS['TEXT'], ha='center')

    # Left column: Auto
    auto_box = FancyBboxPatch((0.3, 1.2), 4.2, 4.8,
                               boxstyle="round,pad=0.2", facecolor=TOKENS['BLUE_BG'],
                               edgecolor=TOKENS['ACCENT'], linewidth=1.5)
    ax.add_patch(auto_box)
    ax.text(2.4, 5.6, 'Auto-Selection', fontsize=12, fontweight='bold',
            color=TOKENS['ACCENT'], ha='center')

    auto_items = [
        ('How', 'Copilot routes automatically\n+ 10% multiplier discount'),
        ('Best for', 'Individual developers,\nno strong model preference'),
        ('Pros', 'Zero effort, no fatigue,\nconsistent decisions'),
        ('Cons', 'Limited visibility into\nrouting algorithm'),
        ('Data', 'RouteLLM: 95% quality,\n75% cost reduction'),
    ]
    for i, (label, text) in enumerate(auto_items):
        y = 5.0 - i * 0.85
        ax.text(0.6, y, label + ':', fontsize=7.5, fontweight='bold', color=TOKENS['TEXT'])
        ax.text(1.7, y, text, fontsize=7.5, color=TOKENS['TEXT_2'], va='top', linespacing=1.3)

    # Right column: Manual
    manual_box = FancyBboxPatch((5.5, 1.2), 4.2, 4.8,
                                 boxstyle="round,pad=0.2", facecolor=TOKENS['PURPLE_BG'],
                                 edgecolor=TOKENS['ACCENT_3'], linewidth=1.5)
    ax.add_patch(manual_box)
    ax.text(7.6, 5.6, 'Manual Selection', fontsize=12, fontweight='bold',
            color=TOKENS['ACCENT_3'], ha='center')

    manual_items = [
        ('How', 'Developer picks model per task\nusing 3-tier taxonomy'),
        ('Best for', 'Teams wanting full control,\npredictable costs'),
        ('Pros', 'Maximum control, matches\nexact complexity needs'),
        ('Cons', 'Requires discipline,\ndecision fatigue over time'),
        ('Data', 'CascadeFlow: 69% savings,\n96% quality retention'),
    ]
    for i, (label, text) in enumerate(manual_items):
        y = 5.0 - i * 0.85
        ax.text(5.8, y, label + ':', fontsize=7.5, fontweight='bold', color=TOKENS['TEXT'])
        ax.text(6.9, y, text, fontsize=7.5, color=TOKENS['TEXT_2'], va='top', linespacing=1.3)

    # Bottom recommendation
    rec = FancyBboxPatch((0.5, 0.2), 9, 0.7,
                          boxstyle="round,pad=0.1", facecolor=TOKENS['TEAL_BG'],
                          edgecolor=TOKENS['ACCENT_2'], linewidth=1.5)
    ax.add_patch(rec)
    ax.text(5, 0.55, 'Both approaches benefit from clean context (Part 1). Clean context improves model output AND model selection.',
            ha='center', fontsize=8.5, fontweight='bold', color=TOKENS['ACCENT_2'])

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'routing-decision-comparison.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


def render_team_optimization_strategies():
    """Training vs restriction outcomes comparison for engineering managers."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    ax.text(5, 6.2, 'Team Optimization: Training vs. Restriction',
            fontsize=14, fontweight='bold', color=TOKENS['TEXT'], ha='center')

    # Restriction column (left, red)
    restrict_box = FancyBboxPatch((0.3, 0.8), 4.2, 4.8,
                                   boxstyle="round,pad=0.2", facecolor=TOKENS['RED_BG'],
                                   edgecolor=TOKENS['WARN'], linewidth=1.5)
    ax.add_patch(restrict_box)
    ax.text(2.4, 5.2, 'Restrict Model Access', fontsize=11, fontweight='bold',
            color=TOKENS['WARN'], ha='center')

    restrict_items = [
        'Force cheap models for all tasks',
        'Block premium model access',
        '-- Developer frustration',
        '-- Workarounds (personal accounts)',
        '-- Quality drops on complex tasks',
        '-- Same messy context, cheaper model',
        'Result: 20-30% cost savings,',
        'lower morale, higher turnover risk',
    ]
    for i, text in enumerate(restrict_items):
        y = 4.6 - i * 0.48
        color = TOKENS['WARN'] if text.startswith('--') else TOKENS['TEXT_2']
        ax.text(0.6, y, text, fontsize=8, color=color)

    # Training column (right, green)
    train_box = FancyBboxPatch((5.5, 0.8), 4.2, 4.8,
                                boxstyle="round,pad=0.2", facecolor=TOKENS['TEAL_BG'],
                                edgecolor=TOKENS['SUCCESS'], linewidth=1.5)
    ax.add_patch(train_box)
    ax.text(7.6, 5.2, 'Train Context Engineering', fontsize=11, fontweight='bold',
            color=TOKENS['SUCCESS'], ha='center')

    train_items = [
        'Teach 5 context practices (Part 1)',
        'Enable caching habits (Part 2)',
        '+ Better output quality',
        '+ Fewer retries (lower retry tax)',
        '+ Natural model routing (Part 3)',
        '+ Developers feel empowered',
        'Result: 50-85% token savings,',
        'better code, happier developers',
    ]
    for i, text in enumerate(train_items):
        y = 4.6 - i * 0.48
        color = TOKENS['SUCCESS'] if text.startswith('+') else TOKENS['TEXT_2']
        ax.text(5.8, y, text, fontsize=8, color=color)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'team-optimization-strategies.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=TOKENS['BG'])
    plt.close(fig)
    print(f'  [ok] {path}')


if __name__ == '__main__':
    print('Rendering Part 3 visuals...')
    render_task_model_alignment()
    render_team_governance_dashboard()
    render_three_layer_stack()
    render_routing_decision_comparison()
    render_team_optimization_strategies()
    print('Done. 5 PNGs generated.')
