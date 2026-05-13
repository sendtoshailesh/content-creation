"""
Visual Pack Renderer — Part 1 Practitioner Mode
Blog: content/ai-code-assistant-cost-part-1.md
Persona: Practitioner (10-slide carousel + platform assets)

Run: python render_distilled.py
Outputs 20 PNG assets to the same directory.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np

DPI = 320
FONT = 'DejaVu Sans'
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_TOKENS = {
    'BG': '#ffffff',
    'TEXT': '#1e293b',
    'TEXT_2': '#475569',
    'MUTED': '#94a3b8',
    'GRID': '#e5e7eb',
    'LIGHT_BG': '#f8fafc',
}

THEMES = {
    'default':  {'ACCENT': '#1f6feb', 'ACCENT_2': '#0d9488', 'ACCENT_3': '#7c3aed',
                 'WARN': '#dc2626', 'SUCCESS': '#16a34a',
                 'BLUE_BG': '#dbeafe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2'},
    'ocean':    {'ACCENT': '#0ea5e9', 'ACCENT_2': '#06b6d4', 'ACCENT_3': '#155e75',
                 'WARN': '#f97316', 'SUCCESS': '#14b8a6',
                 'BLUE_BG': '#e0f2fe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#cffafe', 'RED_BG': '#ffedd5'},
    'sunset':   {'ACCENT': '#f97316', 'ACCENT_2': '#ef4444', 'ACCENT_3': '#b91c1c',
                 'WARN': '#dc2626', 'SUCCESS': '#eab308',
                 'BLUE_BG': '#fff7ed', 'TEAL_BG': '#fef3c7', 'PURPLE_BG': '#fee2e2', 'RED_BG': '#fef2f2'},
    'forest':   {'ACCENT': '#16a34a', 'ACCENT_2': '#65a30d', 'ACCENT_3': '#a16207',
                 'WARN': '#ca8a04', 'SUCCESS': '#15803d',
                 'BLUE_BG': '#f0fdf4', 'TEAL_BG': '#ecfccb', 'PURPLE_BG': '#fefce8', 'RED_BG': '#fef9c3'},
    'midnight': {'ACCENT': '#7c3aed', 'ACCENT_2': '#6366f1', 'ACCENT_3': '#8b5cf6',
                 'WARN': '#ec4899', 'SUCCESS': '#a78bfa',
                 'BLUE_BG': '#ede9fe', 'TEAL_BG': '#e0e7ff', 'PURPLE_BG': '#fae8ff', 'RED_BG': '#fce7f3'},
}

def get_tokens(theme_name):
    return {**BASE_TOKENS, **THEMES[theme_name]}


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

def add_slide_counter(ax, n, total, w, h, color='#94a3b8', fontsize=fs(9)):
    ax.text(w - 64, 64, f"{n:02d} / {total:02d}",
            ha='right', va='top', fontsize=fontsize,
            fontfamily=FONT, color=color)

def add_source(ax, text, w, h, color='#94a3b8', fontsize=fs(7.5)):
    ax.text(40, 22, text, ha='left', va='bottom',
            fontsize=fontsize, fontfamily=FONT, color=color, style='italic')

def add_brand_bar(ax, w, h, tokens, height=6):
    rect = mpatches.FancyBboxPatch((0, h - height), w, height,
                                    boxstyle='square,pad=0',
                                    facecolor=tokens['ACCENT'], linewidth=0)
    ax.add_patch(rect)

# ─── SLIDE 01: Hook (1080×1080, dark BG) ──────────────────────────────────────
def render_slide_01_hook(tokens, output_dir):
    W, H = 1080, 1080
    BG = tokens['TEXT']  # #1e293b dark
    fig, ax = make_fig(W, H, BG)
    add_brand_bar(ax, W, H, tokens, height=8)

    # Giant number
    ax.text(W/2, H*0.58, "120x",
            ha='center', va='center', fontsize=fs(108),
            fontfamily=FONT, fontweight='bold', color='#ffffff')

    # Subtitle
    ax.text(W/2, H*0.38, "cost spread between the cheapest\nand most expensive GitHub Copilot model",
            ha='center', va='center', fontsize=fs(19),
            fontfamily=FONT, color=tokens['ACCENT'],
            multialignment='center', linespacing=1.5)

    # Tagline
    ax.text(W/2, H*0.20, "Starting June 1, 2026 — your bill\nis about to get personal.",
            ha='center', va='center', fontsize=fs(14),
            fontfamily=FONT, color='#94a3b8',
            multialignment='center', linespacing=1.5)

    add_source(ax, "Source: GitHub Docs, 2026", W, H, color='#64748b')
    add_slide_counter(ax, 1, 10, W, H, color='#64748b')
    save(fig, "slide-01-hook.png")

# ─── SLIDE 02: Promise (1080×1080, white BG) ──────────────────────────────────
def render_slide_02_promise(tokens, output_dir):
    W, H = 1080, 1080
    fig, ax = make_fig(W, H, tokens['BG'])
    add_brand_bar(ax, W, H, tokens)

    ax.text(W/2, H*0.88, "In this carousel you'll learn:",
            ha='center', va='center', fontsize=fs(22),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    promises = [
        "1.  How GitHub Copilot's new usage-based billing works",
        "2.  Why the 120x cost spread is your biggest risk",
        "3.  The 3-tier task taxonomy that drives routing",
        "4.  The 3 steps to cut spend by 68-75% today",
        "5.  What to do RIGHT NOW before June 1, 2026",
    ]
    y_start = H * 0.70
    for i, p in enumerate(promises):
        ax.text(W*0.08, y_start - i * 110, p,
                ha='left', va='center', fontsize=fs(15.5),
                fontfamily=FONT, color=tokens['TEXT_2'], linespacing=1.4)

    add_source(ax, "Source: ai-code-assistant-cost-part-1.md", W, H)
    add_slide_counter(ax, 2, 10, W, H)
    save(fig, "slide-02-promise.png")

# ─── SLIDE 03: Problem (1080×1080, chart) ──────────────────────────────────────
def render_slide_03_problem(tokens, output_dir):
    W, H = 1080, 1080
    fig, ax = make_fig(W, H, tokens['BG'])
    add_brand_bar(ax, W, H, tokens)

    ax.text(W/2, H*0.92, "Most teams pay 3x more than they need to",
            ha='center', va='center', fontsize=fs(19),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    # Bar chart: before/after
    labels = ['Before routing', 'After routing']
    values = [3000, 970]
    colors = [tokens['WARN'], tokens['SUCCESS']]
    bar_w = 200
    x_positions = [W/2 - 180, W/2 + 180]
    y_base = 240

    for x, v, c, lbl in zip(x_positions, values, colors, labels):
        bar_h = int(v / 3500 * 520)
        rect = mpatches.FancyBboxPatch((x - bar_w/2, y_base), bar_w, bar_h,
                                        boxstyle='square,pad=0', facecolor=c, linewidth=0)
        ax.add_patch(rect)
        ax.text(x, y_base + bar_h + 24, f"${v:,}/day",
                ha='center', va='bottom', fontsize=fs(18),
                fontfamily=FONT, fontweight='bold', color=c)
        ax.text(x, y_base - 30, lbl, ha='center', va='top', fontsize=fs(13),
                fontfamily=FONT, color=tokens['TEXT_2'])

    # Delta annotation
    ax.annotate('', xy=(x_positions[1] - 120, y_base + 400),
                xytext=(x_positions[0] + 120, y_base + 400),
                arrowprops=dict(arrowstyle='->', color=tokens['ACCENT'], lw=2))
    ax.text(W/2, y_base + 460, "-68%  (-$740K/yr)",
            ha='center', va='center', fontsize=fs(17),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    ax.text(W/2, H*0.16, "Real team. Zero quality loss. Just smarter model routing.",
            ha='center', va='center', fontsize=fs(13.5),
            fontfamily=FONT, color=tokens['TEXT_2'], style='italic')

    add_source(ax, "Source: May 2026", W, H)
    add_slide_counter(ax, 3, 10, W, H)
    save(fig, "slide-03-problem.png")

# ─── SLIDE 04: Framework (1080×1080) ──────────────────────────────────────────
def render_slide_04_framework(tokens, output_dir):
    W, H = 1080, 1080
    fig, ax = make_fig(W, H, tokens['BG'])
    add_brand_bar(ax, W, H, tokens)

    ax.text(W/2, H*0.92, "The Task Taxonomy: 3 tiers, 3 cost levels",
            ha='center', va='center', fontsize=fs(18),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    rows = [
        ("SIMPLE",   "60-70%", "0x - 0.25x", "Rename, docs, boilerplate,\nlinting, import fixes",        tokens['SUCCESS'],  tokens['LIGHT_BG']),
        ("MODERATE", "20-30%", "1x",          "Code review, single-file\nrefactor, unit tests",           tokens['ACCENT'],   tokens['BLUE_BG']),
        ("COMPLEX",  "5-10%",  "3x - 30x",    "Multi-file refactor,\nsystem design, agent mode",          tokens['WARN'],     tokens['RED_BG']),
    ]

    y_positions = [H*0.70, H*0.50, H*0.30]
    col_x = [90, 300, 480, 650, 980]
    headers = ["Tier", "% of tasks", "Multiplier", "Task types"]

    for i, hdr in enumerate(headers):
        ax.text(col_x[i] + (col_x[i+1]-col_x[i])/2, H*0.82, hdr,
                ha='center', va='center', fontsize=fs(11),
                fontfamily=FONT, fontweight='bold', color=tokens['MUTED'])

    row_h = 140
    for row_i, (tier, pct, mult, tasks, fc, bg_c) in enumerate(rows):
        y = y_positions[row_i]
        # Row background
        rect = mpatches.FancyBboxPatch((50, y - row_h/2), W - 100, row_h,
                                        boxstyle='round,pad=4', facecolor=bg_c,
                                        edgecolor=fc, linewidth=1.5, alpha=0.7)
        ax.add_patch(rect)
        ax.text(col_x[0]+60, y, tier, ha='center', va='center', fontsize=fs(11.5),
                fontfamily=FONT, fontweight='bold', color=fc)
        ax.text((col_x[1]+col_x[2])/2, y, pct, ha='center', va='center', fontsize=fs(17),
                fontfamily=FONT, fontweight='bold', color=fc)
        ax.text((col_x[2]+col_x[3])/2, y, mult, ha='center', va='center', fontsize=fs(14),
                fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])
        ax.text((col_x[3]+col_x[4])/2, y, tasks, ha='center', va='center', fontsize=fs(10.5),
                fontfamily=FONT, color=tokens['TEXT_2'], multialignment='center', linespacing=1.4)

    ax.text(W/2, H*0.12, "Route simple tasks to 0x/0.25x models -> save 68-75% with zero quality loss",
            ha='center', va='center', fontsize=fs(12.5),
            fontfamily=FONT, color=tokens['TEXT_2'], style='italic')

    add_source(ax, "Source: Apple ML Research + 2026", W, H)
    add_slide_counter(ax, 4, 10, W, H)
    save(fig, "slide-04-framework.png")

# ─── SLIDE 05: Step 1 (1080×1080) ─────────────────────────────────────────────
def render_slide_05_step1(tokens, output_dir):
    W, H = 1080, 1080
    fig, ax = make_fig(W, H, tokens['BLUE_BG'])
    add_brand_bar(ax, W, H, tokens)

    # Big step number
    ax.text(W/2, H*0.82, "01",
            ha='center', va='center', fontsize=fs(88),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'], alpha=0.15)
    ax.text(W/2, H*0.82, "01",
            ha='center', va='center', fontsize=fs(88),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    ax.text(W/2, H*0.62, "Switch your default to GPT-4.1",
            ha='center', va='center', fontsize=fs(24),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    ax.text(W/2, H*0.49, "Currently included at 0x on paid plans.\nHandles 60-70% of daily tasks with identical quality.",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, color=tokens['TEXT_2'],
            multialignment='center', linespacing=1.5)

    # Stat box — clamped to safe margins
    rect = mpatches.FancyBboxPatch((W*0.04, H*0.26), W*0.92, 120,
                                    boxstyle='round,pad=6', facecolor='#ffffff',
                                    edgecolor=tokens['ACCENT'], linewidth=2)
    ax.add_patch(rect)
    ax.text(W/2, H*0.29 + 60, "5 minutes to change.\nImmediate savings on 60-70% of interactions.",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'],
            multialignment='center', linespacing=1.4)

    ax.text(W/2, H*0.18, "Even if 0x moves to 0.25x — still 4x cheaper than Claude Sonnet (1x)",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, color=tokens['TEXT_2'], style='italic')

    add_source(ax, "Source: GitHub Docs, 2026", W, H)
    add_slide_counter(ax, 5, 10, W, H)
    save(fig, "slide-05-step1.png")

# ─── SLIDE 06: Step 2 (1080×1080) ─────────────────────────────────────────────
def render_slide_06_step2(tokens, output_dir):
    W, H = 1080, 1080
    fig, ax = make_fig(W, H, tokens['TEAL_BG'])
    add_brand_bar(ax, W, H, tokens)

    ax.text(W/2, H*0.82, "02",
            ha='center', va='center', fontsize=fs(88),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT_2'], alpha=0.15)
    ax.text(W/2, H*0.82, "02",
            ha='center', va='center', fontsize=fs(88),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT_2'])

    ax.text(W/2, H*0.62, "Enable auto-selection mode",
            ha='center', va='center', fontsize=fs(24),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    ax.text(W/2, H*0.49, "Copilot picks the right model for each task.\nYou pay 10% less on the multiplier — automatically.",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, color=tokens['TEXT_2'],
            multialignment='center', linespacing=1.5)

    # Stat box — expanded to safe margins
    rect = mpatches.FancyBboxPatch((W*0.04, H*0.26), W*0.92, 120,
                                    boxstyle='round,pad=6', facecolor='#ffffff',
                                    edgecolor=tokens['ACCENT_2'], linewidth=2)
    ax.add_patch(rect)
    ax.text(W/2, H*0.29 + 60, "1 minute to enable.\n10% off every model multiplier forever.",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT_2'],
            multialignment='center', linespacing=1.4)

    ax.text(W/2, H*0.18, "Combine with GPT-4.1 default for compounding savings",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, color=tokens['TEXT_2'], style='italic')

    add_source(ax, "Source: GitHub Copilot Docs, 2026", W, H)
    add_slide_counter(ax, 6, 10, W, H)
    save(fig, "slide-06-step2.png")

# ─── SLIDE 07: Step 3 (1080×1080) ─────────────────────────────────────────────
def render_slide_07_step3(tokens, output_dir):
    W, H = 1080, 1080
    fig, ax = make_fig(W, H, tokens['PURPLE_BG'])
    add_brand_bar(ax, W, H, tokens)

    ax.text(W/2, H*0.82, "03",
            ha='center', va='center', fontsize=fs(88),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT_3'], alpha=0.15)
    ax.text(W/2, H*0.82, "03",
            ha='center', va='center', fontsize=fs(88),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT_3'])

    ax.text(W/2, H*0.62, "Upgrade deliberately,\nnot by default",
            ha='center', va='center', fontsize=fs(21),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    rules = [
        "Prompt < 30 sec to write?  ->  Stay on cheap model",
        "Code review / refactor?    ->  Switch to Sonnet (1x)",
        "Multi-file / architecture?  ->  Use Opus (3x)",
        "Never default to 7.5x+ without a specific reason",
    ]
    y = H * 0.50
    for r in rules:
        ax.text(W/2, y, r, ha='center', va='center', fontsize=fs(13.5),
                fontfamily=FONT, color=tokens['TEXT_2'])
        y -= 80

    ax.text(W/2, H*0.18, "This single habit cut my monthly spend by ~70% with zero quality loss",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, color=tokens['TEXT_2'], style='italic')

    add_source(ax, "Source: author experience + Apple ML Research, 2026", W, H)
    add_slide_counter(ax, 7, 10, W, H)
    save(fig, "slide-07-step3.png")

# ─── SLIDE 08: Pattern Interrupt (1080×1080, dark BG) ─────────────────────────
def render_slide_08_pattern_interrupt(tokens, output_dir):
    W, H = 1080, 1080
    BG = tokens['TEXT']  # #1e293b
    fig, ax = make_fig(W, H, BG)
    add_brand_bar(ax, W, H, tokens)

    # Decorative quote mark
    ax.text(W/2, H*0.80, '"',
            ha='center', va='center', fontsize=fs(160),
            fontfamily=FONT, color=tokens['ACCENT'], alpha=0.25)

    ax.text(W/2, H*0.62, "Three days.\nOne month of credits.\nGone.",
            ha='center', va='center', fontsize=fs(38),
            fontfamily=FONT, fontweight='bold', color='#ffffff',
            multialignment='center', linespacing=1.6)

    ax.text(W/2, H*0.34, "A senior engineer using Claude Opus agent mode for\nmulti-file refactoring — 30x per request.",
            ha='center', va='center', fontsize=fs(15),
            fontfamily=FONT, color='#94a3b8',
            multialignment='center', linespacing=1.5)

    ax.text(W/2, H*0.20, "Under usage-based billing, this is every team's problem after June 1.",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, color=tokens['ACCENT'],
            multialignment='center')

    add_source(ax, "Source: ai-code-assistant-cost-part-1.md, 2026", W, H, color='#475569')
    add_slide_counter(ax, 8, 10, W, H, color='#475569')
    save(fig, "slide-08-pattern-interrupt.png")

# ─── SLIDE 09: Recap (1080×1080) ──────────────────────────────────────────────
def render_slide_09_recap(tokens, output_dir):
    W, H = 1080, 1080
    fig, ax = make_fig(W, H, tokens['BG'])
    add_brand_bar(ax, W, H, tokens)

    ax.text(W/2, H*0.91, "Your model routing checklist",
            ha='center', va='center', fontsize=fs(22),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    checks = [
        ("[x] Switch default to GPT-4.1 or cheapest included model",   tokens['SUCCESS']),
        ("[x] Enable auto-selection -> 10% multiplier discount",         tokens['ACCENT']),
        ("[x] Use Sonnet (1x) for review and refactoring only",         tokens['ACCENT_2']),
        ("[x] Reserve Opus (3x+) for multi-file + architecture ONLY",   tokens['WARN']),
        ("[x] Never default to 7.5x+ models (GPT-5.5, Opus fast)",     tokens['WARN']),
    ]

    y = H * 0.76
    for i, (text, color) in enumerate(checks):
        # Check mark in accent
        ax.text(90, y, "[x]", ha='left', va='center', fontsize=fs(15),
                fontfamily=FONT, fontweight='bold', color=color)
        ax.text(170, y, text[4:], ha='left', va='center', fontsize=fs(14.5),
                fontfamily=FONT, color=tokens['TEXT'])

        # Divider line
        if i < len(checks) - 1:
            ax.plot([80, W - 80], [y - 50, y - 50], color=tokens['GRID'], lw=1)
        y -= 120

    ax.text(W/2, H*0.10, "Potential annualized savings: $740,000 per team | RouteLLM: 75% lower cost at 95% quality",
            ha='center', va='center', fontsize=fs(10.5),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    add_source(ax, "Source: LMSYS, 2026", W, H)
    add_slide_counter(ax, 9, 10, W, H)
    save(fig, "slide-09-recap.png")

# ─── SLIDE 10: CTA (1080×1080) ────────────────────────────────────────────────
def render_slide_10_cta(tokens, output_dir):
    W, H = 1080, 1080
    fig, ax = make_fig(W, H, tokens['BG'])
    add_brand_bar(ax, W, H, tokens)

    # Accent block
    rect = mpatches.FancyBboxPatch((W*0.08, H*0.62), W*0.84, 180,
                                    boxstyle='round,pad=8', facecolor=tokens['BLUE_BG'],
                                    edgecolor=tokens['ACCENT'], linewidth=2.5)
    ax.add_patch(rect)

    ax.text(W/2, H*0.70, "Save this post ->",
            ha='center', va='center', fontsize=fs(34),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    ax.text(W/2, H*0.56, "Full cost calculator\n+ Part 2 (caching) + Part 3 (team playbook)",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, color=tokens['TEXT_2'],
            multialignment='center', linespacing=1.4)

    ax.text(W/2, H*0.44, "Link in first comment",
            ha='center', va='center', fontsize=fs(19),
            fontfamily=FONT, color=tokens['TEXT'])

    ax.text(W/2, H*0.26, "sendtoshailesh.github.io/blog/\nai-code-assistant-context-engineering-part-1.html",
            ha='center', va='center', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'],
            multialignment='center', linespacing=1.4)

    ax.text(W/2, H*0.16, "Part 1 of 3: Optimizing AI Code Assistant Costs",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, color=tokens['TEXT_2'])

    add_slide_counter(ax, 10, 10, W, H)
    save(fig, "slide-10-cta.png")

# ─── X/TWITTER CARDS (1600×900px) ─────────────────────────────────────────────
def render_x_card_01_hook(tokens, output_dir):
    W, H = 1600, 900
    BG = tokens['TEXT']
    fig, ax = make_fig(W, H, BG)

    ax.text(W/2, H*0.62, "120x",
            ha='center', va='center', fontsize=fs(108),
            fontfamily=FONT, fontweight='bold', color='#ffffff')

    ax.text(W/2, H*0.34, "cost spread between cheapest and most expensive\nGitHub Copilot model — starting June 1, 2026",
            ha='center', va='center', fontsize=fs(20),
            fontfamily=FONT, color=tokens['ACCENT'],
            multialignment='center', linespacing=1.5)

    ax.text(W/2, H*0.14, "Full routing guide + savings calculator -> link in last tweet",
            ha='center', va='center', fontsize=fs(14),
            fontfamily=FONT, color='#64748b', style='italic')

    add_source(ax, "Source: GitHub Docs, 2026", W, H, color='#475569')
    save(fig, "x-card-01.png")

def render_x_card_02_data(tokens, output_dir):
    W, H = 1600, 900
    fig, ax = make_fig(W, H, tokens['BG'])

    ax.text(W/2, H*0.88, "Model routing: real savings data",
            ha='center', va='center', fontsize=fs(24),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    # Two stat boxes
    boxes = [
        (W*0.22, r"\$3,000 -> \$970/day", "68% reduction\n\$740K/year savings", tokens['SUCCESS'],   "May 2026"),
        (W*0.56, "95% GPT-4 quality", "at 75% lower cost\nRouting 14% to GPT-4", tokens['ACCENT'], "RouteLLM, LMSYS 2024"),
        (W*0.78, "69% savings\n96% quality", "CascadeFlow\nresult",             tokens['ACCENT_2'], "2026"),
    ]
    for bx, val, sub, col, src in boxes:
        rect = mpatches.FancyBboxPatch((bx - 160, H*0.25), 310, H*0.48,
                                        boxstyle='round,pad=6', facecolor=col,
                                        alpha=0.1, edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(bx, H*0.62, val, ha='center', va='center', fontsize=fs(17),
                fontfamily=FONT, fontweight='bold', color=col,
                multialignment='center', linespacing=1.3)
        ax.text(bx, H*0.42, sub, ha='center', va='center', fontsize=fs(13),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.3)
        ax.text(bx, H*0.28, src, ha='center', va='center', fontsize=fs(10),
                fontfamily=FONT, color=tokens['MUTED'],
                multialignment='center', linespacing=1.3, style='italic')

    add_source(ax, "Sources: LMSYS 2024, 2026", W, H)

    # FIX 11: Summary row filling lower canvas area
    ax.fill_between([W*0.08, W*0.92], [H*0.16], [H*0.16 + 2], color=tokens['GRID'])
    ax.text(W/2, H*0.12,
            r"Combined result: \$3,000/day -> \$970/day  |  68% cost reduction  |  \$740K saved per year",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])
    ax.text(W/2, H*0.07, "Zero quality degradation documented across all three studies",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, color=tokens['TEXT_2'], style='italic')

    save(fig, "x-card-02.png")

def render_x_card_03_framework(tokens, output_dir):
    W, H = 1600, 900
    fig, ax = make_fig(W, H, tokens['LIGHT_BG'])

    ax.text(W/2, H*0.88, "Task Taxonomy -> Model Routing Policy",
            ha='center', va='center', fontsize=fs(24),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    tiers = [
        ("SIMPLE 60-70%",   "GPT-4.1 / 0x",        "Rename, docs,\nboilerplate",            tokens['SUCCESS'],  tokens['BG']),
        ("MODERATE 20-30%", "Claude Sonnet / 1x",   "Code review,\nrefactoring, tests",     tokens['ACCENT'],   tokens['BLUE_BG']),
        ("COMPLEX 5-10%",   "Claude Opus / 3x",     "Multi-file, design,\nagent sessions",  tokens['WARN'],     tokens['RED_BG']),
    ]

    col_w = W * 0.28
    x_starts = [W*0.08, W*0.38, W*0.68]

    for xs, (tier, model, tasks, col, bgc) in zip(x_starts, tiers):
        rect = mpatches.FancyBboxPatch((xs, H*0.14), col_w, H*0.60,
                                        boxstyle='round,pad=5', facecolor=bgc,
                                        edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(xs + col_w/2, H*0.65, tier, ha='center', va='center', fontsize=fs(14),
                fontfamily=FONT, fontweight='bold', color=col)
        ax.text(xs + col_w/2, H*0.50, model, ha='center', va='center', fontsize=fs(16),
                fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])
        ax.text(xs + col_w/2, H*0.34, tasks, ha='center', va='center', fontsize=fs(12.5),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.4)

    add_source(ax, "Source: Apple ML Research + GitHub Docs, 2026", W, H)
    save(fig, "x-card-03.png")

def render_x_card_04_cta(tokens, output_dir):
    W, H = 1600, 900
    fig, ax = make_fig(W, H, tokens['BG'])

    rect = mpatches.FancyBboxPatch((W*0.08, H*0.35), W*0.84, H*0.42,
                                    boxstyle='round,pad=10', facecolor=tokens['BLUE_BG'],
                                    edgecolor=tokens['ACCENT'], linewidth=2.5)
    ax.add_patch(rect)

    ax.text(W/2, H*0.68, "Full 3-part cost optimization guide",
            ha='center', va='center', fontsize=fs(26),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    ax.text(W/2, H*0.54, "Part 1: Model Routing  |  Part 2: Caching  |  Part 3: Team Playbook",
            ha='center', va='center', fontsize=fs(17),
            fontfamily=FONT, color=tokens['TEXT_2'])

    ax.text(W/2, H*0.40, "70-90% total savings possible | Link in last tweet ->",
            ha='center', va='center', fontsize=fs(17),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    ax.text(W/2, H*0.22, "https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html",
            ha='center', va='center', fontsize=fs(10.5),
            fontfamily=FONT, color=tokens['MUTED'])

    # FIX 12: Supporting tagline filling lower canvas area
    ax.text(W/2, H*0.12, "Save 68-75% with smarter model routing  |  Part 1 of 3",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, color=tokens['TEXT_2'], style='italic')

    save(fig, "x-card-04.png")

# ─── MEDIUM HERO (1400×800) ────────────────────────────────────────────────────
def render_medium_hero(tokens, output_dir):
    W, H = 1400, 800
    BG = tokens['TEXT']
    fig, ax = make_fig(W, H, BG)

    # Top accent stripe
    rect = mpatches.FancyBboxPatch((0, H - 10), W, 10,
                                    boxstyle='square,pad=0', facecolor=tokens['ACCENT'], linewidth=0)
    ax.add_patch(rect)

    ax.text(W/2, H*0.70, "The 120x Problem",
            ha='center', va='center', fontsize=fs(52),
            fontfamily=FONT, fontweight='bold', color='#ffffff')

    ax.text(W/2, H*0.50, "Why Your AI Code Assistant Costs Are About to Change",
            ha='center', va='center', fontsize=fs(22),
            fontfamily=FONT, color=tokens['ACCENT'],
            multialignment='center')

    ax.text(W/2, H*0.33, "Starting June 1, 2026 — a 120x cost spread, usage-based billing,\nand a routing strategy that saves 68-75%",
            ha='center', va='center', fontsize=fs(15),
            fontfamily=FONT, color='#94a3b8',
            multialignment='center', linespacing=1.5)

    ax.text(W/2, H*0.14, "Part 1 of 3: Optimizing AI Code Assistant Costs  |  Shailesh Mishra, 2026",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, color='#64748b', style='italic')

    save(fig, "medium-hero.png")

# ─── MEDIUM INLINE 01 (1200×800) ──────────────────────────────────────────────
def render_medium_inline_01(tokens, output_dir):
    W, H = 1200, 800
    fig, ax = make_fig(W, H, tokens['BG'])

    ax.text(W/2, H*0.92, "GitHub Copilot Model Multipliers\n0x to 30x (June 2026)",
            ha='center', va='center', fontsize=fs(15),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'],
            multialignment='center', linespacing=1.4)

    models = [
        ("GPT-5.4 nano",        0.25,  tokens['SUCCESS']),
        ("Claude Haiku 4.5",    0.33,  tokens['SUCCESS']),
        ("Claude Sonnet 4.6",   1.0,   tokens['ACCENT']),
        ("GPT-5.2",             1.0,   tokens['ACCENT']),
        ("Claude Opus 4.5",     3.0,   tokens['WARN']),
        ("GPT-5.5",             7.5,   tokens['WARN']),
        ("Claude Opus 4.7",    15.0,   '#991b1b'),
        ("Claude Opus 4.6 fm", 30.0,   '#7f1d1d'),
    ]

    y_positions = np.linspace(H*0.78, H*0.10, len(models))
    max_mult = 30.0
    bar_x = 340
    max_bar_w = W - bar_x - 120

    for (name, mult, col), y in zip(models, y_positions):
        bar_w = max(8, int(mult / max_mult * max_bar_w))
        rect = mpatches.FancyBboxPatch((bar_x, y - 20), bar_w, 38,
                                        boxstyle='square,pad=0', facecolor=col,
                                        linewidth=0, alpha=0.85)
        ax.add_patch(rect)
        ax.text(bar_x - 8, y, name, ha='right', va='center', fontsize=fs(11),
                fontfamily=FONT, color=tokens['TEXT'])
        ax.text(bar_x + bar_w + 10, y, f"{mult}x", ha='left', va='center', fontsize=fs(11.5),
                fontfamily=FONT, fontweight='bold', color=col)

    ax.text(W/2, H*0.02, "Included (0x) models: GPT-4.1, GPT-4o, GPT-5 mini — subject to change | Source: GitHub Docs, 2026",
            ha='center', va='bottom', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    save(fig, "medium-inline-01.png")

# ─── MEDIUM INLINE 02 (1200×800) ──────────────────────────────────────────────
def render_medium_inline_02(tokens, output_dir):
    W, H = 1200, 800
    fig, ax = make_fig(W, H, tokens['LIGHT_BG'])

    ax.text(W/2, H*0.92, "Model Routing: Before vs. After Cost Breakdown",
            ha='center', va='center', fontsize=fs(18),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    categories = [
        ("Simple tasks\n(60-70%)", 1800, 0,    "60% -> 0x model saves $1,800/day"),
        ("Moderate\n(20-30%)",      900, 490,  "30% -> stay at 1x = $490/day"),
        ("Complex\n(5-10%)",        300, 480,  "10% -> 3x only when needed"),
    ]

    x_positions = [W*0.20, W*0.50, W*0.80]
    for (lbl, before, after, note), x in zip(categories, x_positions):
        bar_w = 100
        y_base = H * 0.18

        scale = H * 0.60 / 1800
        bh = max(8, int(before * scale))
        ah = max(8, int(after * scale))

        rect_b = mpatches.FancyBboxPatch((x - 70, y_base), bar_w, bh,
                                          boxstyle='square,pad=0', facecolor=tokens['WARN'],
                                          linewidth=0, alpha=0.7)
        ax.add_patch(rect_b)
        rect_a = mpatches.FancyBboxPatch((x + 10, y_base), bar_w, ah,
                                          boxstyle='square,pad=0', facecolor=tokens['SUCCESS'],
                                          linewidth=0, alpha=0.8)
        ax.add_patch(rect_a)

        if before > 0:
            ax.text(x - 20, y_base + bh + 16, f"${before}/d", ha='center', va='bottom',
                    fontsize=fs(10.5), fontfamily=FONT, color=tokens['WARN'], fontweight='bold')
        if after > 0:
            ax.text(x + 60, y_base + ah + 16, f"${after}/d", ha='center', va='bottom',
                    fontsize=fs(10.5), fontfamily=FONT, color=tokens['SUCCESS'], fontweight='bold')
        else:
            ax.text(x + 60, y_base + 16, "$0", ha='center', va='bottom',
                    fontsize=fs(10.5), fontfamily=FONT, color=tokens['SUCCESS'], fontweight='bold')

        ax.text(x, y_base - 30, lbl, ha='center', va='top', fontsize=fs(11),
                fontfamily=FONT, color=tokens['TEXT_2'], multialignment='center', linespacing=1.3)

    # Legend (proxy handles only — not added as patches)
    legend_handles = [
        mpatches.Patch(facecolor=tokens['WARN'], alpha=0.7, label='Before routing'),
        mpatches.Patch(facecolor=tokens['SUCCESS'], alpha=0.8, label='After routing'),
    ]
    ax.legend(handles=legend_handles, loc='upper right', fontsize=fs(11), framealpha=0.9, bbox_to_anchor=(0.97, 0.92))

    ax.text(W/2, H*0.01, "Illustrative breakdown of \$3,000/day -> \$970/day savings | Source: May 2026",
            ha='center', va='bottom', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    save(fig, "medium-inline-02.png")

# ─── SUBSTACK HERO (1200×630) ─────────────────────────────────────────────────
def render_substack_hero(tokens, output_dir):
    W, H = 1200, 630
    BG = tokens['TEXT']
    fig, ax = make_fig(W, H, BG)

    rect = mpatches.FancyBboxPatch((0, H - 8), W, 8,
                                    boxstyle='square,pad=0', facecolor=tokens['ACCENT'], linewidth=0)
    ax.add_patch(rect)

    ax.text(W/2, H*0.68, "The 120x Problem",
            ha='center', va='center', fontsize=fs(46),
            fontfamily=FONT, fontweight='bold', color='#ffffff')

    ax.text(W/2, H*0.46, "GitHub Copilot is moving to usage-based billing.\nOne decision cuts costs 68-75%.",
            ha='center', va='center', fontsize=fs(17),
            fontfamily=FONT, color=tokens['ACCENT'],
            multialignment='center', linespacing=1.5)

    ax.text(W/2, H*0.22, "Part 1 of 3: Model Routing  |  sendtoshailesh.github.io",
            ha='center', va='center', fontsize=fs(11.5),
            fontfamily=FONT, color='#64748b', style='italic')

    save(fig, "substack-hero.png")

# ─── LINKEDIN ARTICLE EXHIBIT 01 (1200×627) ───────────────────────────────────
def render_linkedin_exhibit_01(tokens, output_dir):
    W, H = 1200, 627
    NAVY = '#051C2C'
    fig, ax = make_fig(W, H, '#ffffff')

    # Header bar
    rect = mpatches.FancyBboxPatch((0, H - 72), W, 72,
                                    boxstyle='square,pad=0', facecolor=NAVY, linewidth=0)
    ax.add_patch(rect)
    ax.text(W/2, H - 36, "AI coding costs vary 120x across model tiers — most teams default to expensive",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, fontweight='bold', color='#ffffff')

    ax.text(W/2, H*0.74, "Exhibit 1  |  Context",
            ha='center', va='center', fontsize=fs(10),
            fontfamily=FONT, color=tokens['MUTED'])

    # Horizontal bar chart for model tiers
    tiers_data = [
        ("GPT-5.4 nano",        0.25),
        ("Claude Haiku 4.5",    0.33),
        ("Claude Sonnet 4.6",   1.0),
        ("Claude Opus 4.5",     3.0),
        ("GPT-5.5",             7.5),
        ("Claude Opus 4.7",    15.0),
        ("Claude Opus 4.6 fm", 30.0),
    ]
    y_base = H * 0.64
    row_h = 52
    bar_x = 280
    max_bar_w = W - bar_x - 120
    max_val = 30.0

    for i, (name, mult) in enumerate(tiers_data):
        y = y_base - i * row_h
        bw = max(8, int(mult / max_val * max_bar_w))
        intensity = mult / max_val
        col = f"#{int(31 + intensity*200):02x}{int(111 - intensity*100):02x}{int(235 - intensity*200):02x}"
        rect = mpatches.FancyBboxPatch((bar_x, y - 15), bw, 28,
                                        boxstyle='square,pad=0', facecolor=tokens['ACCENT'],
                                        linewidth=0, alpha=0.2 + intensity * 0.8)
        ax.add_patch(rect)
        ax.text(bar_x - 6, y, name, ha='right', va='center', fontsize=fs(10),
                fontfamily=FONT, color=tokens['TEXT'])
        ax.text(bar_x + bw + 8, y, f"{mult}x", ha='left', va='center', fontsize=fs(10.5),
                fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    ax.text(W/2, H*0.06, "Source: GitHub Docs, 2026  |  0x models (GPT-4.1, GPT-5 mini) included on paid plans — subject to change",
            ha='center', va='center', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    save(fig, "linkedin-article-exhibit-01.png")

# ─── LINKEDIN ARTICLE EXHIBIT 02 (1200×627) ───────────────────────────────────
def render_linkedin_exhibit_02(tokens, output_dir):
    W, H = 1200, 627
    NAVY = '#051C2C'
    fig, ax = make_fig(W, H, '#ffffff')

    # Header bar
    rect = mpatches.FancyBboxPatch((0, H - 72), W, 72,
                                    boxstyle='square,pad=0', facecolor=NAVY, linewidth=0)
    ax.add_patch(rect)
    ax.text(W/2, H - 36, "Routing simple tasks to 0x/0.25x models cuts spend 68-75% with no quality loss",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, fontweight='bold', color='#ffffff')

    ax.text(W/2, H*0.74, "Exhibit 2  |  Evidence",
            ha='center', va='center', fontsize=fs(10),
            fontfamily=FONT, color=tokens['MUTED'])

    # Three evidence blocks
    evidence = [
        ("RouteLLM\n(LMSYS, 2024)",       "75%\ncost\nreduction",   "95% GPT-4\nquality retained",   tokens['ACCENT']),
        ("Case Study\n(May 2026)",          "\$3K -> \$970\n/day",  "68% reduction\n\$740K/yr saved", tokens['SUCCESS']),
        ("CascadeFlow\n(2026)",             "69%\nsavings",           "96% quality\nretention",        tokens['ACCENT_2']),
    ]

    col_w = W * 0.28
    x_starts = [W*0.06, W*0.37, W*0.68]

    for xs, (src, big, detail, col) in zip(x_starts, evidence):
        rect = mpatches.FancyBboxPatch((xs, H*0.10), col_w, H*0.56,
                                        boxstyle='round,pad=6', facecolor='#f8fafc',
                                        edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(xs + col_w/2, H*0.56, src, ha='center', va='center', fontsize=fs(10),
                fontfamily=FONT, color=tokens['MUTED'],
                multialignment='center', linespacing=1.3, style='italic')
        ax.text(xs + col_w/2, H*0.40, big, ha='center', va='center', fontsize=fs(22),
                fontfamily=FONT, fontweight='bold', color=col,
                multialignment='center', linespacing=1.2)
        ax.text(xs + col_w/2, H*0.22, detail, ha='center', va='center', fontsize=fs(11),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.4)

    ax.text(W/2, H*0.04, "Source: LMSYS 2024, May 2026",
            ha='center', va='center', fontsize=fs(9),
            fontfamily=FONT, color=tokens['MUTED'], style='italic')

    save(fig, "linkedin-article-exhibit-02.png")


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    import datetime
    print(f"Rendering Part 1 Practitioner visual pack — {datetime.date.today()}")
    print(f"Output directory: {OUTPUT_DIR}")

    # All slides use 'default' theme for canonical token compliance
    visual_functions = [
        render_slide_01_hook,
        render_slide_02_promise,
        render_slide_03_problem,
        render_slide_04_framework,
        render_slide_05_step1,
        render_slide_06_step2,
        render_slide_07_step3,
        render_slide_08_pattern_interrupt,
        render_slide_09_recap,
        render_slide_10_cta,
        render_x_card_01_hook,
        render_x_card_02_data,
        render_x_card_03_framework,
        render_x_card_04_cta,
        render_medium_hero,
        render_medium_inline_01,
        render_medium_inline_02,
        render_substack_hero,
        render_linkedin_exhibit_01,
        render_linkedin_exhibit_02,
    ]

    plt.rcParams['font.family'] = FONT
    plt.rcParams['figure.dpi'] = DPI

    success_count = 0
    failed = []
    for i, func in enumerate(visual_functions):
        t = get_tokens('default')
        try:
            func(t, OUTPUT_DIR)
            success_count += 1
        except Exception as e:
            print(f"  ERROR in {func.__name__}: {e}")
            failed.append((func.__name__, str(e)))

    print(f"\n=== Done: {success_count}/{len(visual_functions)} assets rendered ===")
    if failed:
        print("Failed:")
        for name, err in failed:
            print(f"  - {name}: {err}")
