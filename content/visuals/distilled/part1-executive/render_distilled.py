#!/usr/bin/env python3
"""
Part 1 Executive Visual Pack — render_distilled.py
Generates 12 PNG visual assets (executive / C-suite mode)
Source blog: ai-code-assistant-cost-part-1.md
DPI: 320  |  Font: DejaVu Sans  |  Palette: navy + accent + gray

Run: python3 render_distilled.py
"""
import os
import sys
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe

# ─── CONFIG ───────────────────────────────────────────────────────────────────
FONT = 'DejaVu Sans'
DPI  = 320
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Executive design tokens
# Navy header bar + one accent per exhibit + gray series — NO CTA on exhibit visuals

def fs(pt):
    return round(float(pt) * 0.50, 1)

TOKENS = {
    'NAVY':      '#051C2C',
    'TEXT':      '#1e293b',
    'TEXT_INV':  '#f8fafc',
    'TEXT_2':    '#475569',
    'MUTED':     '#94a3b8',
    'ACCENT':    '#1f6feb',   # system blue
    'ACCENT_2':  '#0d9488',   # system teal
    'ACCENT_3':  '#7c3aed',   # system purple
    'ACCENT_4':  '#6366f1',   # indigo — data/chart
    'LIGHT_BG':  '#f8fafc',
    'BLUE_BG':   '#dbeafe',
    'TEAL_BG':   '#ccfbf1',
    'PURPLE_BG': '#ede9fe',
    'RED_BG':    '#fee2e2',
    'WHITE':     '#ffffff',
    'SUCCESS':   '#16a34a',
    'WARN':      '#dc2626',
    'BORDER':    '#e2e8f0',
}

def get_tokens(i=0):
    return dict(TOKENS)


# ─── HELPERS ──────────────────────────────────────────────────────────────────
def make_fig(w_px, h_px, bg_color='#ffffff'):
    """Create a figure with full-bleed axis in pixel coordinates."""
    figsize = (w_px / DPI, h_px / DPI)
    fig = plt.figure(figsize=figsize, dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w_px)
    ax.set_ylim(0, h_px)
    ax.axis('off')
    ax.set_facecolor(bg_color)
    fig.patch.set_facecolor(bg_color)
    return fig, ax


def save(fig, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=DPI)
    plt.close(fig)
    print(f"  Saved: {filename}")


def add_navy_header(ax, W, H, title_text, height=72, accent=None):
    """Executive navy header bar with title + optional accent rule."""
    accent = accent or TOKENS['ACCENT']
    # Navy header bar
    rect = mpatches.FancyBboxPatch((0, H - height), W, height,
                                    boxstyle='square,pad=0',
                                    facecolor=TOKENS['NAVY'], linewidth=0)
    ax.add_patch(rect)
    # Thin accent rule below header
    ax.fill_between([0, W], [H - height], [H - height - 3], color=accent)
    # Title text in header
    ax.text(W * 0.05, H - height / 2, title_text,
            ha='left', va='center', fontsize=fs(13),
            fontfamily=FONT, fontweight='bold', color=TOKENS['TEXT_INV'])
    # Small brand tag
    ax.text(W * 0.96, H - height / 2, "github.com/copilot",
            ha='right', va='center', fontsize=fs(8),
            fontfamily=FONT, color='#64748b', style='italic')


def add_source(ax, W, H, source_text, y_offset=24):
    """Source attribution in bottom area."""
    ax.text(W * 0.04, y_offset, source_text,
            ha='left', va='bottom', fontsize=fs(8),
            fontfamily=FONT, color=TOKENS['MUTED'], style='italic')


def add_exhibit_footer(ax, W, accent=None):
    """Thin accent rule at very bottom."""
    accent = accent or TOKENS['ACCENT']
    ax.fill_between([0, W], [0], [4], color=accent)


# ─── EXHIBIT 1: Context — The 120x Cost Spread (1200×627) ────────────────────
def render_exhibit_01_context(tokens, output_dir):
    """Exec exhibit 1 — Business context: what changed and why it matters."""
    W, H = 1200, 627
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, "GitHub Copilot Billing Change — June 1, 2026", accent=tokens['ACCENT'])
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    # Key headline
    ax.text(W / 2, H * 0.80, "A 120x Cost Spread\nArrives in Your Budget",
            ha='center', va='center', fontsize=fs(22),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'],
            multialignment='center', linespacing=1.3)

    ax.text(W / 2, H * 0.66, "Premium AI code assistants will move from flat-rate seat\nlicensing to consumption-based pricing.",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, color=tokens['TEXT_2'],
            multialignment='center', linespacing=1.3)

    # Three cost tier boxes
    tiers = [
        ("Included (0x)", "GPT-4.1\nGPT-4o\nGPT-5 mini", tokens['SUCCESS']),
        ("Standard (1-5x)", "GPT-4.1 mini\nClaude Sonnet 4.5\nGemini Pro 2.5", tokens['ACCENT']),
        ("Premium (5-30x)", "GPT-5.4\nClaude Opus 4.6\nGemini Ultra 2.0", tokens['WARN']),
    ]
    box_w = W * 0.26
    box_h = H * 0.28
    y_base = H * 0.18
    x_starts = [W * 0.05, W * 0.37, W * 0.69]

    for (label, models_txt, accent), x in zip(tiers, x_starts):
        rect = mpatches.FancyBboxPatch((x, y_base), box_w, box_h,
                                        boxstyle='round,pad=4',
                                        facecolor=tokens['LIGHT_BG'],
                                        edgecolor=accent, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + box_w / 2, y_base + box_h - 18, label,
                ha='center', va='top', fontsize=fs(11),
                fontfamily=FONT, fontweight='bold', color=accent)
        ax.text(x + box_w / 2, y_base + box_h / 2 - 8, models_txt,
                ha='center', va='center', fontsize=fs(9.5),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.4)

    add_source(ax, W, H, "Source: GitHub Copilot billing documentation, 2025")
    save(fig, "exhibit-01-context.png")


# ─── EXHIBIT 2: Evidence — Real Cost Data (1200×627) ─────────────────────────
def render_exhibit_02_evidence(tokens, output_dir):
    """Exec exhibit 2 — Evidence: $3K→$970/day with routing strategy."""
    W, H = 1200, 627
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, "Routing Strategy: Documented Cost Reduction", accent=tokens['ACCENT'])
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    # Big ROI numbers
    ax.text(W * 0.26, H * 0.75, "$3,000",
            ha='center', va='center', fontsize=fs(36),
            fontfamily=FONT, fontweight='bold', color=tokens['WARN'])
    ax.text(W * 0.26, H * 0.63, "per day (before)",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, color=tokens['TEXT_2'])

    # Arrow
    ax.annotate('', xy=(W * 0.50, H * 0.69), xytext=(W * 0.38, H * 0.69),
                arrowprops=dict(arrowstyle='->', color=tokens['ACCENT'],
                                lw=2.5, mutation_scale=20))
    ax.text(W * 0.44, H * 0.76, "68%", ha='center', va='center', fontsize=fs(20),
            fontfamily=FONT, fontweight='bold', color=tokens['SUCCESS'])
    ax.text(W * 0.44, H * 0.64, "reduction", ha='center', va='center', fontsize=fs(10),
            fontfamily=FONT, color=tokens['TEXT_2'])

    ax.text(W * 0.64, H * 0.75, "$970",
            ha='center', va='center', fontsize=fs(36),
            fontfamily=FONT, fontweight='bold', color=tokens['SUCCESS'])
    ax.text(W * 0.64, H * 0.63, "per day (after)",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, color=tokens['TEXT_2'])

    # Annual savings callout
    rect = mpatches.FancyBboxPatch((W * 0.73, H * 0.54), W * 0.22, H * 0.28,
                                    boxstyle='round,pad=6',
                                    facecolor=tokens['SUCCESS'],
                                    linewidth=0, alpha=0.12)
    ax.add_patch(rect)
    ax.text(W * 0.84, H * 0.72, "$740,000",
            ha='center', va='center', fontsize=fs(22),
            fontfamily=FONT, fontweight='bold', color=tokens['SUCCESS'])
    ax.text(W * 0.84, H * 0.61, "annual savings",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, color=tokens['TEXT_2'])

    # Bottom context line
    ax.text(W / 2, H * 0.45, "Task routing: simple (0x) + moderate (1x) + complex (3x) only when required",
            ha='center', va='center', fontsize=fs(11),
            fontfamily=FONT, color=tokens['TEXT_2'])

    # Academic validation bar
    ax.fill_between([W * 0.04, W * 0.96], [H * 0.14], [H * 0.14 + 3], color=tokens['BORDER'])
    ax.text(W / 2, H * 0.22,
            "Academic validation: RouteLLM (LMSYS, 2024) — 95% quality at 75% lower cost;\nCascadeFlow — 69% savings, 96% quality retained",
            ha='center', va='center', fontsize=fs(9.5),
            fontfamily=FONT, color=tokens['MUTED'],
            multialignment='center', linespacing=1.4)

    add_source(ax, W, H, "Source: May 2026 case study; LMSYS RouteLLM paper, 2024")
    save(fig, "exhibit-02-evidence.png")


# ─── EXHIBIT 3: Framework — 3-Tier Routing Decision (1200×627) ───────────────
def render_exhibit_03_framework(tokens, output_dir):
    """Exec exhibit 3 — Decision framework: 3-tier task routing."""
    W, H = 1200, 627
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, "3-Tier Model Routing Framework", accent=tokens['ACCENT'])
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    ax.text(W / 2, H * 0.81, "Match task complexity to model capability — pay only for what the task requires",
            ha='center', va='center', fontsize=fs(12.5),
            fontfamily=FONT, color=tokens['TEXT_2'])

    # Three-column framework
    tiers_data = [
        ("Tier 1: Simple", "Autocomplete\nBoilerplate\nFormatting\nUnit tests",
         "60-70% of tasks", "0x — Included free", tokens['SUCCESS'], "0x"),
        ("Tier 2: Moderate", "Code review\nRefactoring\nDoc generation\nDebug assist",
         "20-30% of tasks", "1-5x multiplier", tokens['ACCENT'], "1-5x"),
        ("Tier 3: Complex", "Architecture\nSecurity audit\nSystem design\nNew paradigms",
         "5-10% of tasks", "5-30x multiplier", tokens['WARN'], "5-30x"),
    ]

    col_w = W * 0.27
    col_gap = W * 0.035
    x_starts = [W * 0.04, W * 0.37, W * 0.695]
    y_top = H * 0.71

    for i, (title, tasks, freq, cost, col, cost_tag), x in zip(range(3), tiers_data, x_starts):
        # Column box
        col_h = H * 0.54
        rect = mpatches.FancyBboxPatch((x, y_top - col_h), col_w, col_h,
                                        boxstyle='round,pad=4',
                                        facecolor=tokens['LIGHT_BG'],
                                        edgecolor=col, linewidth=2)
        ax.add_patch(rect)

        # Tier heading
        ax.text(x + col_w / 2, y_top - 18, title,
                ha='center', va='top', fontsize=fs(12),
                fontfamily=FONT, fontweight='bold', color=col)

        # Task list
        ax.text(x + col_w / 2, y_top - 60, tasks,
                ha='center', va='top', fontsize=fs(9.5),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.5)

        # Frequency pill
        freq_y = y_top - col_h + 52
        rpill = mpatches.FancyBboxPatch((x + 8, freq_y - 14), col_w - 16, 28,
                                         boxstyle='round,pad=3',
                                         facecolor=col, linewidth=0, alpha=0.15)
        ax.add_patch(rpill)
        ax.text(x + col_w / 2, freq_y, freq,
                ha='center', va='center', fontsize=fs(9.5),
                fontfamily=FONT, fontweight='bold', color=col)

        # Cost label
        ax.text(x + col_w / 2, y_top - col_h + 18, cost,
                ha='center', va='bottom', fontsize=fs(10),
                fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    add_source(ax, W, H, "Source: GitHub Copilot model multiplier documentation, 2025")
    save(fig, "exhibit-03-framework.png")


# ─── EXHIBIT 4: ROI — Business Case Summary (1200×627) ───────────────────────
def render_exhibit_04_roi(tokens, output_dir):
    """Exec exhibit 4 — ROI summary and implementation roadmap."""
    W, H = 1200, 627
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, "ROI Summary: Model Routing Implementation", accent=tokens['ACCENT'])
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    # Left: key metrics column
    metrics = [
        ("68%",      "Cost reduction demonstrated"),
        ("$740K",    "Annual savings (100-dev team)"),
        ("95%",      "Quality retained (RouteLLM 2024)"),
        ("~4 wks",   "Typical implementation timeline"),
    ]
    y_positions = [H * 0.73, H * 0.57, H * 0.41, H * 0.25]
    for (val, lbl), y in zip(metrics, y_positions):
        ax.text(W * 0.17, y, val,
                ha='center', va='center', fontsize=fs(28),
                fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])
        ax.text(W * 0.34, y, lbl,
                ha='left', va='center', fontsize=fs(12),
                fontfamily=FONT, color=tokens['TEXT_2'])

    # Divider
    ax.fill_between([W * 0.52, W * 0.522], [H * 0.15], [H * 0.82],
                    color=tokens['BORDER'])

    # Right: 4-step roadmap
    ax.text(W * 0.76, H * 0.82, "Implementation Roadmap",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    steps = [
        ("1", "Audit",     "Map 30-day task taxonomy"),
        ("2", "Route",     "Deploy complexity classifier"),
        ("3", "Monitor",   "Track multiplier distribution"),
        ("4", "Optimize",  "Iterate quarterly"),
    ]
    step_ys = [H * 0.68, H * 0.52, H * 0.36, H * 0.20]
    for (num, title, desc), sy in zip(steps, step_ys):
        # Step circle
        circle = plt.Circle((W * 0.60, sy), 16, color=tokens['ACCENT'])
        ax.add_patch(circle)
        ax.text(W * 0.60, sy, num,
                ha='center', va='center', fontsize=fs(11),
                fontfamily=FONT, fontweight='bold', color=tokens['WHITE'])
        ax.text(W * 0.66, sy + 2, title,
                ha='left', va='center', fontsize=fs(11.5),
                fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])
        ax.text(W * 0.66, sy - 14, desc,
                ha='left', va='center', fontsize=fs(9.5),
                fontfamily=FONT, color=tokens['TEXT_2'])

    add_source(ax, W, H, "Source: May 2026 case study May 2026; Apple ML Research 2025; LMSYS RouteLLM 2024")
    save(fig, "exhibit-04-roi.png")


# ─── X-EXHIBIT 1: The 120x Spread Data Chart (1600×900) ──────────────────────
def render_x_exhibit_01(tokens, output_dir):
    """X/Twitter exhibit 1 — Horizontal bar chart of model cost multipliers."""
    W, H = 1600, 900
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, "GitHub Copilot Model Cost Multipliers — June 2026",
                    height=80, accent=tokens['ACCENT'])
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    ax.text(W / 2, H * 0.86, "120x spread: same task costs 0.25x or 30x depending on model choice",
            ha='center', va='center', fontsize=fs(14),
            fontfamily=FONT, color=tokens['TEXT_2'])

    models = [
        ("Claude Opus 4.6 (fast)",  30,  tokens['WARN']),
        ("GPT-5.4",                 20,  tokens['WARN']),
        ("Claude Opus 4.5",         12,  tokens['ACCENT_3']),
        ("Gemini Ultra 2.0",        10,  tokens['ACCENT_3']),
        ("Claude Sonnet 4.5",        5,  tokens['ACCENT']),
        ("GPT-4.1 mini",             2,  tokens['ACCENT']),
        ("Claude Haiku 4.5",         1,  tokens['ACCENT']),
        ("GPT-4.1",                  0,  tokens['SUCCESS']),
        ("GPT-4o",                   0,  tokens['SUCCESS']),
        ("GPT-5 mini",               0,  tokens['SUCCESS']),
        ("GPT-5.4 nano",           0.25, tokens['SUCCESS']),
    ]

    bar_x    = W * 0.28
    max_mult = 30
    max_bar  = W * 0.60
    row_h    = H * 0.063
    y_top    = H * 0.78

    for i, (name, mult, col) in enumerate(models):
        y = y_top - i * row_h
        bw = max(6, int(mult / max_mult * max_bar))
        # Background track
        track = mpatches.FancyBboxPatch((bar_x, y - row_h * 0.32), max_bar, row_h * 0.64,
                                         boxstyle='square,pad=0',
                                         facecolor=tokens['LIGHT_BG'], linewidth=0)
        ax.add_patch(track)
        # Value bar
        val_bar = mpatches.FancyBboxPatch((bar_x, y - row_h * 0.32), bw, row_h * 0.64,
                                           boxstyle='square,pad=0',
                                           facecolor=col, linewidth=0, alpha=0.82)
        ax.add_patch(val_bar)

        ax.text(bar_x - 10, y, name,
                ha='right', va='center', fontsize=fs(11),
                fontfamily=FONT, color=tokens['TEXT'])
        mult_lbl = "FREE" if mult == 0 else f"{mult}x"
        ax.text(bar_x + bw + 16, y, mult_lbl,
                ha='left', va='center', fontsize=fs(11.5),
                fontfamily=FONT, fontweight='bold', color=col)

    # Legend — spread positions to avoid overlap; Standard=ACCENT, Premium=WARN
    for lbl, col, x_leg in [("FREE (0x)",  tokens['SUCCESS'], W * 0.52),
                              ("Standard",   tokens['ACCENT'],  W * 0.68),
                              ("Premium",    tokens['WARN'],    W * 0.81)]:
        dot = plt.Circle((x_leg, H * 0.08), 7, color=col)
        ax.add_patch(dot)
        ax.text(x_leg + 14, H * 0.08, lbl,
                ha='left', va='center', fontsize=fs(10),
                fontfamily=FONT, color=tokens['TEXT_2'])

    add_source(ax, W, H, "Source: GitHub Copilot model multiplier documentation, 2025", y_offset=28)
    save(fig, "x-exhibit-01.png")


# ─── X-EXHIBIT 2: ROI Comparison (1600×900) ──────────────────────────────────
def render_x_exhibit_02(tokens, output_dir):
    """X/Twitter exhibit 2 — Before/after cost comparison with routing."""
    W, H = 1600, 900
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, r"Model Routing ROI: \$3,000/day -> \$970/day (-68%)",
                    height=80, accent=tokens['ACCENT'])
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    ax.text(W / 2, H * 0.86, "100-developer team, 30-day case study | May 2026 case study",
            ha='center', va='center', fontsize=fs(12.5),
            fontfamily=FONT, color=tokens['TEXT_2'])

    # Before column
    ax.text(W * 0.25, H * 0.77, "BEFORE",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, fontweight='bold', color=tokens['WARN'])
    ax.text(W * 0.25, H * 0.68, r"\$3,000/day",
            ha='center', va='center', fontsize=fs(32),
            fontfamily=FONT, fontweight='bold', color=tokens['WARN'])
    ax.text(W * 0.25, H * 0.59, "All tasks -> premium models",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, color=tokens['TEXT_2'])

    # Bar chart comparing before/after by category
    categories = [
        ("Simple\n60-70%",   1800,   0, W * 0.18),
        ("Moderate\n20-30%", 900,  490, W * 0.42),
        ("Complex\n5-10%",   300,  480, W * 0.66),
    ]
    y_base  = H * 0.16
    bar_w   = 80
    scale   = H * 0.32 / 1800

    for lbl, before, after, x in categories:
        bh = max(6, int(before * scale))
        ah = max(6, int(after  * scale))

        # Before bar
        rect_b = mpatches.FancyBboxPatch((x - 50, y_base), bar_w, bh,
                                          boxstyle='square,pad=0',
                                          facecolor=tokens['WARN'], linewidth=0, alpha=0.75)
        ax.add_patch(rect_b)
        ax.text(x - 10, y_base + bh + 12, r"\$" + str(before) + "/d",
                ha='center', va='bottom', fontsize=fs(10),
                fontfamily=FONT, color=tokens['WARN'], fontweight='bold')

        # After bar
        rect_a = mpatches.FancyBboxPatch((x + 40, y_base), bar_w, ah,
                                          boxstyle='square,pad=0',
                                          facecolor=tokens['SUCCESS'], linewidth=0, alpha=0.8)
        ax.add_patch(rect_a)
        if after > 0:
            ax.text(x + 80, y_base + ah + 12, r"\$" + str(after) + "/d",
                    ha='center', va='bottom', fontsize=fs(10),
                    fontfamily=FONT, color=tokens['SUCCESS'], fontweight='bold')
        else:
            ax.text(x + 80, y_base + 12, r"\$0",
                    ha='center', va='bottom', fontsize=fs(10),
                    fontfamily=FONT, color=tokens['SUCCESS'], fontweight='bold')

        ax.text(x + 15, y_base - 40, lbl,
                ha='center', va='top', fontsize=fs(10.5),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.3)

    # After total callout
    ax.text(W * 0.84, H * 0.77, "AFTER",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, fontweight='bold', color=tokens['SUCCESS'])
    ax.text(W * 0.84, H * 0.68, r"\$970/day",
            ha='center', va='center', fontsize=fs(32),
            fontfamily=FONT, fontweight='bold', color=tokens['SUCCESS'])
    ax.text(W * 0.84, H * 0.59, r"\$740K/yr savings",
            ha='center', va='center', fontsize=fs(14),
            fontfamily=FONT, fontweight='bold', color=tokens['SUCCESS'])

    legend_handles = [
        mpatches.Patch(facecolor=tokens['WARN'],    alpha=0.75, label='Before routing'),
        mpatches.Patch(facecolor=tokens['SUCCESS'], alpha=0.80, label='After routing'),
    ]
    ax.legend(handles=legend_handles, loc='upper center',
              fontsize=fs(11), framealpha=0.9,
              bbox_to_anchor=(0.5, 0.52), ncol=2)

    add_source(ax, W, H, "Source: May 2026 case study", y_offset=28)
    save(fig, "x-exhibit-02.png")


# ─── MEDIUM HERO (1400×800) ───────────────────────────────────────────────────
def render_medium_hero(tokens, output_dir):
    """Medium / blog hero image — executive edition."""
    W, H = 1400, 800
    BG = tokens['NAVY']
    fig, ax = make_fig(W, H, BG)

    # Subtle gradient effect — light bottom overlay
    ax.fill_between([0, W], [0], [H * 0.38], color='#0a1a2e', alpha=0.6)

    # Accent stripe
    ax.fill_between([0, W], [H - 5], [H], color=tokens['ACCENT'])

    # Main headline
    ax.text(W / 2, H * 0.72,
            "The 120x Problem",
            ha='center', va='center', fontsize=fs(52),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT_INV'])

    ax.text(W / 2, H * 0.56,
            "Why Your AI Code Assistant Costs Are About to Change",
            ha='center', va='center', fontsize=fs(20),
            fontfamily=FONT, color=tokens['ACCENT'])

    ax.text(W / 2, H * 0.42,
            "GitHub Copilot shifts to consumption-based billing — June 1, 2026",
            ha='center', va='center', fontsize=fs(14),
            fontfamily=FONT, color='#94a3b8')

    # Data callout strip
    callout_y = H * 0.18
    for val, lbl, xp in [
        ("120x",   "cost spread",           W * 0.20),
        ("68%",    "savings documented",    W * 0.50),
        ("$740K",  "annual savings / team", W * 0.80),
    ]:
        ax.text(xp, callout_y + 22, val,
                ha='center', va='center', fontsize=fs(28),
                fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])
        ax.text(xp, callout_y - 10, lbl,
                ha='center', va='center', fontsize=fs(11),
                fontfamily=FONT, color='#94a3b8')

    ax.text(W / 2, H * 0.04, "sendtoshailesh.github.io  |  Executive Edition",
            ha='center', va='bottom', fontsize=fs(9.5),
            fontfamily=FONT, color='#475569', style='italic')

    save(fig, "medium-hero.png")


# ─── MEDIUM INLINE (1200×800) ─────────────────────────────────────────────────
def render_medium_inline_01(tokens, output_dir):
    """Medium inline image — model cost multiplier reference table."""
    W, H = 1200, 800
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, "Model Cost Multiplier Reference — June 2026")
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    ax.text(W / 2, H * 0.87, "Select models and their GitHub Copilot billing multipliers",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, color=tokens['TEXT_2'])

    # Table
    rows = [
        ("Model",            "Multiplier", "Tier",    True),
        ("GPT-5.4 nano",     "0.25x",      "Micro",   False),
        ("GPT-4.1",          "0x (FREE)",  "Incl.",   False),
        ("GPT-4o",           "0x (FREE)",  "Incl.",   False),
        ("GPT-5 mini",       "0x (FREE)",  "Incl.",   False),
        ("Claude Haiku 4.5", "1x",         "Standard",False),
        ("Claude Sonnet 4.5","5x",         "Standard",False),
        ("GPT-5.4",          "20x",        "Premium", False),
        ("Claude Opus 4.6",  "30x",        "Premium", False),
    ]
    col_xs = [W * 0.08, W * 0.50, W * 0.74]
    row_h  = H * 0.072
    y_top  = H * 0.78

    tier_colors = {
        "Incl.":    tokens['SUCCESS'],
        "Micro":    tokens['ACCENT'],
        "Standard": tokens['WARN'],
        "Premium":  tokens['WARN'],
        "Tier":     tokens['TEXT'],
    }

    for i, (name, mult, tier, is_header) in enumerate(rows):
        y = y_top - i * row_h
        # Row background
        bg = tokens['NAVY'] if is_header else (tokens['LIGHT_BG'] if i % 2 == 0 else tokens['WHITE'])
        row_rect = mpatches.FancyBboxPatch((W * 0.04, y - row_h * 0.45), W * 0.92, row_h * 0.88,
                                            boxstyle='square,pad=0',
                                            facecolor=bg, linewidth=0)
        ax.add_patch(row_rect)

        txt_col = tokens['TEXT_INV'] if is_header else tokens['TEXT']
        fw = 'bold' if is_header else 'normal'
        fsize = 12 if is_header else 11

        ax.text(col_xs[0], y, name,
                ha='left', va='center', fontsize=fs(fsize),
                fontfamily=FONT, fontweight=fw, color=txt_col)
        ax.text(col_xs[1], y, mult,
                ha='center', va='center', fontsize=fs(fsize),
                fontfamily=FONT, fontweight='bold' if not is_header else fw,
                color=tier_colors.get(tier, tokens['TEXT']) if not is_header else txt_col)
        ax.text(col_xs[2], y, tier,
                ha='center', va='center', fontsize=fs(fsize),
                fontfamily=FONT, fontweight=fw, color=txt_col)

    add_source(ax, W, H, "Source: GitHub Copilot model multiplier documentation, 2025")
    save(fig, "medium-inline-01.png")


# ─── SUBSTACK HERO (1200×630) ─────────────────────────────────────────────────
def render_substack_hero(tokens, output_dir):
    """Substack hero — executive punchy single-stat card."""
    W, H = 1200, 630
    BG = tokens['NAVY']
    fig, ax = make_fig(W, H, BG)

    ax.fill_between([0, W], [H - 5], [H], color=tokens['ACCENT'])
    ax.fill_between([0, W], [0], [5],   color=tokens['ACCENT'])

    ax.text(W / 2, H * 0.82,
            "The 120x AI Cost Spread",
            ha='center', va='center', fontsize=fs(36),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT_INV'])

    ax.text(W / 2, H * 0.66,
            "Copilot moves to consumption billing June 1, 2026",
            ha='center', va='center', fontsize=fs(16),
            fontfamily=FONT, color=tokens['ACCENT'])

    ax.text(W / 2, H * 0.50,
            "One team cut \$3,000/day to \$970/day\n— 68% reduction, \$740K/year saved",
            ha='center', va='center', fontsize=fs(14),
            fontfamily=FONT, color='#94a3b8',
            multialignment='center', linespacing=1.4)

    ax.text(W / 2, H * 0.22,
            r"120x cost spread  |  68% savings  |  \$740K/year",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, color=TOKENS['MUTED'])

    ax.text(W / 2, H * 0.12, "sendtoshailesh.github.io",
            ha='center', va='center', fontsize=fs(12),
            fontfamily=FONT, color='#475569', style='italic')

    save(fig, "substack-hero.png")


# ─── LINKEDIN ARTICLE EXHIBIT 1 (1200×627) ───────────────────────────────────
def render_linkedin_exhibit_01(tokens, output_dir):
    """LinkedIn article exhibit 1 — exec-level 120x context diagram."""
    W, H = 1200, 627
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, "Seat Licensing to Consumption Billing")
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    ax.text(W / 2, H * 0.81,
            "The strategic shift every engineering leader needs to understand",
            ha='center', va='center', fontsize=fs(13),
            fontfamily=FONT, fontweight='bold', color=tokens['TEXT'])

    # Three-zone horizontal diagram
    zones = [
        ("FLAT RATE ERA\n(Before June 2026)",
         "Predictable seat cost\nNo usage visibility\nAll models ~equal",
         tokens['TEXT_2'], tokens['LIGHT_BG']),
        ("TRANSITION\nJune 1, 2026",
         "Consumption billing\ngoes live",
         tokens['ACCENT'], tokens['BLUE_BG']),
        ("CONSUMPTION ERA\n(After June 2026)",
         "0x to 30x spread\nTask-model matching critical\n68% savings possible",
         tokens['SUCCESS'], tokens['TEAL_BG']),
    ]
    zone_w   = W * 0.27
    zone_h   = H * 0.40
    y_base   = H * 0.12
    x_starts = [W * 0.04, W * 0.365, W * 0.695]

    for (title, body, accent, bg), x in zip(zones, x_starts):
        rect = mpatches.FancyBboxPatch((x, y_base), zone_w, zone_h,
                                        boxstyle='round,pad=4',
                                        facecolor=bg, edgecolor=accent, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + zone_w / 2, y_base + zone_h - 20, title,
                ha='center', va='top', fontsize=fs(10),
                fontfamily=FONT, fontweight='bold', color=accent,
                multialignment='center', linespacing=1.3)
        ax.text(x + zone_w / 2, y_base + zone_h / 2 - 14, body,
                ha='center', va='center', fontsize=fs(9.5),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.4)

    # Arrows between zones
    for x_arr in [W * 0.36, W * 0.69]:
        ax.annotate('', xy=(x_arr + 2, y_base + zone_h / 2),
                    xytext=(x_arr - 30, y_base + zone_h / 2),
                    arrowprops=dict(arrowstyle='->', color=tokens['MUTED'],
                                    lw=2, mutation_scale=14))

    add_source(ax, W, H, "Source: GitHub Copilot billing documentation, 2025")
    save(fig, "linkedin-article-exhibit-01.png")


# ─── LINKEDIN ARTICLE EXHIBIT 2 (1200×627) ───────────────────────────────────
def render_linkedin_exhibit_02(tokens, output_dir):
    """LinkedIn article exhibit 2 — ROI waterfall: $3K to $970/day."""
    W, H = 1200, 627
    fig, ax = make_fig(W, H, tokens['WHITE'])

    add_navy_header(ax, W, H, "Cost Reduction Waterfall: Routing by Task Complexity")
    add_exhibit_footer(ax, W, tokens['ACCENT'])

    # Waterfall bars
    steps = [
        ("Baseline\n(no routing)",         3000,  3000, tokens['WARN']),
        ("Simple tasks\nto 0x models",    -1800,  1200, tokens['SUCCESS']),
        ("Moderate tasks\noptimized",       -230,   970, tokens['SUCCESS']),
        ("Final cost\n(after routing)",     970,   970, tokens['ACCENT']),
    ]
    bar_w = 160
    scale = H * 0.45 / 3000
    y_floor = H * 0.14
    x_positions = [W * 0.14, W * 0.34, W * 0.56, W * 0.78]

    prev_top = y_floor
    for i, (lbl, delta, abs_val, col) in enumerate(steps):
        x = x_positions[i]
        if i == 0:
            bar_bottom = y_floor
            bar_h = abs_val * scale
        elif delta < 0:
            bar_bottom = (abs_val) * scale + y_floor
            bar_h = abs(delta) * scale
        else:
            bar_bottom = y_floor
            bar_h = abs_val * scale

        rect = mpatches.FancyBboxPatch((x - bar_w / 2, bar_bottom), bar_w, bar_h,
                                        boxstyle='square,pad=0',
                                        facecolor=col, linewidth=0, alpha=0.82)
        ax.add_patch(rect)

        # Value label on bar
        ax.text(x, bar_bottom + bar_h + 14, f"${abs_val:,}/d",
                ha='center', va='bottom', fontsize=fs(11),
                fontfamily=FONT, fontweight='bold', color=col)
        # Step label below
        ax.text(x, y_floor - 30, lbl,
                ha='center', va='top', fontsize=fs(9.5),
                fontfamily=FONT, color=tokens['TEXT_2'],
                multialignment='center', linespacing=1.3)

        # Connector line to next bar
        if i < len(steps) - 1:
            next_x = x_positions[i + 1]
            connector_y = bar_bottom + bar_h if i == 0 else bar_bottom
            if i == 1:
                connector_y = abs_val * scale + y_floor
            ax.plot([x + bar_w / 2, next_x - bar_w / 2], [connector_y, connector_y],
                    '--', color=tokens['MUTED'], lw=1, alpha=0.6)

    # Savings annotation
    ax.annotate('', xy=(x_positions[3], y_floor + 970 * scale + 50),
                xytext=(x_positions[0], y_floor + 3000 * scale + 50),
                arrowprops=dict(arrowstyle='<->', color=tokens['ACCENT'],
                                lw=2, mutation_scale=14))
    ax.text(W / 2, y_floor + 3000 * scale + 68,
            "68% reduction = $740K/year",
            ha='center', va='bottom', fontsize=fs(11.5),
            fontfamily=FONT, fontweight='bold', color=tokens['ACCENT'])

    add_source(ax, W, H, "Source: May 2026 case study")
    save(fig, "linkedin-article-exhibit-02.png")


# ─── RUNNER ───────────────────────────────────────────────────────────────────
def main():
    print(f"Rendering Part 1 Executive visual pack — {datetime.date.today()}")
    print(f"Output directory: {OUTPUT_DIR}")

    renderers = [
        (render_exhibit_01_context,    0),
        (render_exhibit_02_evidence,   1),
        (render_exhibit_03_framework,  2),
        (render_exhibit_04_roi,        3),
        (render_x_exhibit_01,          4),
        (render_x_exhibit_02,          0),
        (render_medium_hero,           1),
        (render_medium_inline_01,      2),
        (render_substack_hero,         3),
        (render_linkedin_exhibit_01,   4),
        (render_linkedin_exhibit_02,   0),
    ]

    done   = 0
    failed = []
    for fn, theme_idx in renderers:
        tokens = get_tokens(theme_idx)
        try:
            fn(tokens, OUTPUT_DIR)
            done += 1
        except Exception as e:
            print(f"  ERROR in {fn.__name__}: {e}")
            failed.append((fn.__name__, str(e)))

    print(f"\n=== Done: {done}/{len(renderers)} assets rendered ===")
    if failed:
        print("Failed:")
        for name, err in failed:
            print(f"  - {name}: {err}")
    return 0 if not failed else 1


if __name__ == '__main__':
    sys.exit(main())
