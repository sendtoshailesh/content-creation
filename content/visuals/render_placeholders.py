"""
Publication-quality visual assets for the AI Model Selection Field Guide.
Designed for Medium / blog embedding at 2x retina resolution.

Design system:
- Clean white backgrounds with subtle structure
- Blue (#1f6feb) as primary accent, teal (#0d9488) as secondary
- Slate gray typography (#1e293b / #475569)
- Rounded containers, soft shadows via layered fills
- 320 DPI output for crisp rendering on all screens
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUTPUT_DIR = Path(__file__).parent

# ── Design tokens ──────────────────────────────────────────────────────
BG        = "#ffffff"
SURFACE   = "#f8fafc"
SURFACE_2 = "#f1f5f9"
BORDER    = "#e2e8f0"
BORDER_D  = "#cbd5e1"
TEXT      = "#1e293b"
TEXT_2    = "#475569"
TEXT_3    = "#64748b"
ACCENT    = "#1f6feb"
ACCENT_L  = "#dbeafe"
ACCENT_2  = "#0d9488"
ACCENT_2L = "#ccfbf1"
WARN      = "#dc2626"
WARN_L    = "#fef2f2"
DPI       = 320
FONT      = "Helvetica Neue"


def _style_ax(ax):
    """Remove all axis chrome."""
    ax.set_axis_off()
    ax.set_facecolor(BG)


def _rounded_box(ax, x, y, w, h, label, fc=SURFACE_2, ec=BORDER, fontsize=9.5,
                 text_color=TEXT, weight="normal", alpha=1.0, zorder=2):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015",
                         fc=fc, ec=ec, linewidth=1.0, alpha=alpha, zorder=zorder)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            fontsize=fontsize, color=text_color, weight=weight,
            family=FONT, zorder=zorder + 1)
    return box


def _arrow(ax, xy_from, xy_to, color=BORDER_D, lw=1.0, style="-|>", mutation=10):
    arr = FancyArrowPatch(xy_from, xy_to, arrowstyle=style,
                          mutation_scale=mutation, color=color,
                          linewidth=lw, zorder=1)
    ax.add_patch(arr)


def _save(fig, name):
    fig.savefig(OUTPUT_DIR / name, dpi=DPI, bbox_inches="tight",
                facecolor=BG, edgecolor="none", pad_inches=0.15)
    plt.close(fig)


# ── 1. Model Selection Framework ──────────────────────────────────────
def model_selection_framework_png():
    fig, ax = plt.subplots(figsize=(10, 7))
    _style_ax(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Title
    ax.text(5, 9.5, "7-Dimension Model Selection Framework",
            ha="center", fontsize=14, weight="bold", color=TEXT, family=FONT)

    # Center node
    _rounded_box(ax, 3.8, 4.5, 2.4, 1.2, "Product\nUse Case",
                 fc=ACCENT, ec=ACCENT, fontsize=11, text_color="#ffffff", weight="bold")

    dims = [
        ("Task Fit",       1.5, 7.6),
        ("Quality Bar",    4.0, 8.0),
        ("Latency Budget", 6.5, 7.6),
        ("Cost Envelope",  7.8, 5.2),
        ("Data Sensitivity", 6.8, 2.2),
        ("Integration",    3.0, 2.0),
        ("Reliability",    1.0, 5.2),
    ]

    colors = [ACCENT_L, ACCENT_L, ACCENT_L, ACCENT_L, ACCENT_2L, ACCENT_2L, ACCENT_2L]

    for (label, x, y), fc in zip(dims, colors):
        _rounded_box(ax, x, y, 2.0, 0.9, label, fc=fc, ec=BORDER_D, fontsize=9, weight="semibold")
        # Arrow from dimension to center
        dx, dy = x + 1.0, y + 0.45
        cx, cy = 5.0, 5.1
        _arrow(ax, (dx, dy), (cx, cy), color=BORDER_D, lw=0.8)

    # Output chain: Shortlist → Pilot → Decision
    chain_y = 1.0
    _rounded_box(ax, 1.0, chain_y, 2.2, 0.8, "Shortlist Models", fc=SURFACE_2, fontsize=9, weight="semibold")
    _rounded_box(ax, 4.0, chain_y, 2.2, 0.8, "Pilot & Measure", fc=SURFACE_2, fontsize=9, weight="semibold")
    _rounded_box(ax, 7.0, chain_y, 2.2, 0.8, "Production\nDecision", fc=ACCENT, ec=ACCENT,
                 fontsize=9, text_color="#ffffff", weight="bold")

    _arrow(ax, (3.2, chain_y + 0.4), (4.0, chain_y + 0.4), color=TEXT_3, lw=1.2, mutation=12)
    _arrow(ax, (6.2, chain_y + 0.4), (7.0, chain_y + 0.4), color=TEXT_3, lw=1.2, mutation=12)

    # Arrow from center down to chain
    _arrow(ax, (5.0, 4.5), (5.1, 1.8), color=TEXT_3, lw=1.0, mutation=12)

    _save(fig, "model-selection-framework.png")


# ── 2. Model Routing Flow ─────────────────────────────────────────────
def model_routing_flow_png():
    fig, ax = plt.subplots(figsize=(11, 5))
    _style_ax(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)

    ax.text(6, 5.6, "Tiered Model Routing Architecture",
            ha="center", fontsize=13, weight="bold", color=TEXT, family=FONT)

    # Nodes
    _rounded_box(ax, 0.3, 2.5, 2.0, 1.0, "Incoming\nRequest", fc=SURFACE_2, fontsize=9.5, weight="semibold")

    _rounded_box(ax, 3.0, 2.5, 2.2, 1.0, "Task Router", fc=ACCENT_L, ec=ACCENT, fontsize=9.5, weight="bold")

    # Three model tiers
    tier_data = [
        (5.8, 4.2, "Lightweight\nHaiku / Flash", ACCENT_2L, ACCENT_2),
        (5.8, 2.5, "Mid-tier\nSonnet / GPT-4o", SURFACE_2, BORDER_D),
        (5.8, 0.8, "Frontier\nOpus / o3", ACCENT_L, ACCENT),
    ]
    for x, y, label, fc, ec in tier_data:
        _rounded_box(ax, x, y, 2.4, 0.9, label, fc=fc, ec=ec, fontsize=8.5, weight="semibold")

    _rounded_box(ax, 8.8, 2.5, 2.0, 1.0, "Quality\nValidator", fc=SURFACE_2, fontsize=9.5, weight="semibold")

    _rounded_box(ax, 11.2, 2.5, 1.6, 1.0, "User", fc=ACCENT, ec=ACCENT,
                 fontsize=10, text_color="#ffffff", weight="bold")

    # Arrows: Request → Router
    _arrow(ax, (2.3, 3.0), (3.0, 3.0), color=TEXT_3, lw=1.0, mutation=11)

    # Router → tiers
    _arrow(ax, (5.2, 3.2), (5.8, 4.65), color=ACCENT_2, lw=0.9)
    _arrow(ax, (5.2, 3.0), (5.8, 2.95), color=TEXT_3, lw=0.9)
    _arrow(ax, (5.2, 2.8), (5.8, 1.25), color=ACCENT, lw=0.9)

    # Tiers → Validator
    _arrow(ax, (8.2, 4.65), (8.8, 3.2), color=ACCENT_2, lw=0.9)
    _arrow(ax, (8.2, 2.95), (8.8, 3.0), color=TEXT_3, lw=0.9)
    _arrow(ax, (8.2, 1.25), (8.8, 2.8), color=ACCENT, lw=0.9)

    # Validator → User
    _arrow(ax, (10.8, 3.0), (11.2, 3.0), color=TEXT_3, lw=1.0, mutation=11)

    # Retry loop hint
    ax.annotate("", xy=(9.8, 2.5), xytext=(9.8, 1.5),
                arrowprops=dict(arrowstyle="-|>", color=WARN, lw=0.8))
    ax.text(10.3, 1.9, "Retry /\nEscalate", fontsize=7.5, color=WARN, ha="center", family=FONT)

    _save(fig, "model-routing-flow.png")


# ── 3. Comparison Matrix ──────────────────────────────────────────────
def comparison_matrix_png():
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.set_axis_off()

    ax.text(0.5, 0.97, "Model Strategy by Use Case",
            ha="center", va="top", fontsize=14, weight="bold",
            color=TEXT, family=FONT, transform=ax.transAxes)

    headers = ["Use Case", "Quality", "Latency", "Cost\nSensitivity", "Recommended Strategy"]
    data = [
        ["Real-time autocomplete",     "Medium",     "< 300ms",  "High",      "Lightweight (Haiku/Flash)"],
        ["Chat drafting assistant",    "Med-High",   "< 2s TTFT", "Medium",    "Mid-tier + frontier escalation"],
        ["Strategic analysis",         "Very High",  "< 15s",    "Low",       "Frontier with task gating"],
        ["Support triage",             "Medium",     "< 1s",     "Very High", "Lightweight > mid-tier"],
        ["Knowledge Q&A (RAG)",        "Medium",     "< 3s",     "Medium",    "Mid-tier + retrieval pipeline"],
        ["Code suggestions (IDE)",     "High",       "< 500ms",  "Medium",    "Fast default, frontier on-demand"],
        ["Document extraction",        "Medium",     "Batch OK", "Very High", "Lightweight + validation"],
        ["Agentic workflows",          "Very High",  "Tolerant", "Medium",    "Frontier orch. + light sub-agents"],
    ]

    col_widths = [0.20, 0.10, 0.10, 0.12, 0.30]
    n_cols = len(headers)
    n_rows = len(data) + 1

    x_start = 0.09
    y_start = 0.88
    row_h = 0.075
    cell_pad = 0.01

    # Draw header row
    x = x_start
    for j, hdr in enumerate(headers):
        w = col_widths[j]
        rect = mpatches.FancyBboxPatch((x, y_start - row_h), w - cell_pad, row_h - 0.005,
                                        boxstyle="round,pad=0.005", fc=ACCENT, ec="none",
                                        transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + (w - cell_pad) / 2, y_start - row_h / 2, hdr,
                ha="center", va="center", fontsize=8.5, color="#ffffff",
                weight="bold", family=FONT, transform=ax.transAxes)
        x += w

    # Draw data rows
    for i, row in enumerate(data):
        y = y_start - (i + 2) * row_h + 0.005
        bg = SURFACE if i % 2 == 0 else BG
        x = x_start
        for j, cell in enumerate(row):
            w = col_widths[j]
            rect = mpatches.FancyBboxPatch((x, y), w - cell_pad, row_h - 0.008,
                                            boxstyle="round,pad=0.003", fc=bg, ec=BORDER,
                                            linewidth=0.4, transform=ax.transAxes)
            ax.add_patch(rect)

            fw = "semibold" if j == 0 else "normal"
            fc = TEXT if j == 0 else TEXT_2
            ax.text(x + (w - cell_pad) / 2, y + (row_h - 0.008) / 2, cell,
                    ha="center", va="center", fontsize=7.8, color=fc,
                    weight=fw, family=FONT, transform=ax.transAxes)
            x += w

    _save(fig, "comparison-matrix.png")


# ── 4. Trade-off 2×2 ──────────────────────────────────────────────────
def tradeoff_2x2_png():
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_facecolor(BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.text(5, 9.6, "Quality vs. Cost Trade-Off Matrix",
            ha="center", fontsize=13, weight="bold", color=TEXT, family=FONT)

    # Quadrant backgrounds
    ax.fill_between([0, 5], 5, 10, color=ACCENT_2L, alpha=0.3)   # top-left: best
    ax.fill_between([5, 10], 5, 10, color=ACCENT_L, alpha=0.3)   # top-right
    ax.fill_between([0, 5], 0, 5, color=SURFACE_2, alpha=0.5)    # bottom-left
    ax.fill_between([5, 10], 0, 5, color=WARN_L, alpha=0.3)      # bottom-right: danger

    # Axis lines
    ax.axhline(5, color=BORDER_D, linewidth=1.0, linestyle="--")
    ax.axvline(5, color=BORDER_D, linewidth=1.0, linestyle="--")

    # Quadrant labels
    ax.text(2.5, 8.8, "High Quality / Low Cost", ha="center", fontsize=8,
            color=ACCENT_2, family=FONT, style="italic", alpha=0.8)
    ax.text(7.5, 8.8, "High Quality / High Cost", ha="center", fontsize=8,
            color=ACCENT, family=FONT, style="italic", alpha=0.8)
    ax.text(2.5, 1.2, "Lower Quality / Low Cost", ha="center", fontsize=8,
            color=TEXT_3, family=FONT, style="italic", alpha=0.8)
    ax.text(7.5, 1.2, "Danger Zone", ha="center", fontsize=8,
            color=WARN, family=FONT, style="italic", alpha=0.8)

    # Model dots with halos
    models = [
        (7.8, 8.5, "Frontier\n(Opus, o3, Ultra)", ACCENT, 180),
        (5.4, 6.8, "Mid-tier\n(Sonnet, GPT-4o)", ACCENT_2, 140),
        (2.8, 4.2, "Lightweight\n(Haiku, Flash)", "#475569", 120),
    ]
    for mx, my, label, color, size in models:
        ax.scatter(mx, my, s=size, color=color, zorder=5, edgecolors="white", linewidth=2)
        ax.scatter(mx, my, s=size * 3, color=color, alpha=0.1, zorder=4)
        ax.text(mx + 0.3, my - 0.4, label, fontsize=8.5, color=color,
                weight="semibold", family=FONT, va="top")

    # Axis labels
    ax.set_xlabel("Cost  >", fontsize=11, color=TEXT_2, family=FONT, labelpad=10)
    ax.set_ylabel("Quality  >", fontsize=11, color=TEXT_2, family=FONT, labelpad=10)
    ax.tick_params(axis="both", which="both", bottom=False, left=False,
                   labelbottom=False, labelleft=False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "tradeoff-2x2.png")


# ── 5. Case Timeline ──────────────────────────────────────────────────
def case_timeline_png():
    fig, ax = plt.subplots(figsize=(11, 4))
    _style_ax(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)

    ax.text(6, 3.7, "Case Study Timeline: From Single Model to Model Portfolio",
            ha="center", fontsize=12, weight="bold", color=TEXT, family=FONT)

    # Main line
    ax.plot([1, 11], [1.8, 1.8], color=BORDER_D, linewidth=2.5, zorder=1, solid_capstyle="round")

    milestones = [
        (1.5,  "Week 0",   "Launch with\nsingle model",        ACCENT),
        (3.5,  "Week 4",   "Latency spikes\n& cost overruns",  WARN),
        (5.8,  "Week 6",   "7-dimension\nframework review",    ACCENT_2),
        (8.0,  "Week 8",   "Tiered routing\npilot deployed",   ACCENT),
        (10.2, "Week 16",  "66% cost reduction\n& better UX",  ACCENT_2),
    ]

    for x, week, desc, color in milestones:
        # Dot
        ax.scatter(x, 1.8, s=100, color=color, zorder=5, edgecolors="white", linewidth=2)
        ax.scatter(x, 1.8, s=350, color=color, alpha=0.08, zorder=4)

        # Week label below
        ax.text(x, 1.3, week, ha="center", fontsize=8.5, color=color,
                weight="bold", family=FONT)

        # Description above
        ax.text(x, 2.5, desc, ha="center", fontsize=8, color=TEXT_2,
                family=FONT, linespacing=1.4, va="bottom")

        # Connector line
        ax.plot([x, x], [1.95, 2.3], color=color, linewidth=0.8, alpha=0.5)

    _save(fig, "case-timeline.png")


# ── 6. Pitfalls Table ─────────────────────────────────────────────────
def pitfalls_table_png():
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_axis_off()

    ax.text(0.5, 0.97, "Common Pitfalls & Mitigations",
            ha="center", va="top", fontsize=14, weight="bold",
            color=TEXT, family=FONT, transform=ax.transAxes)

    headers = ["Pitfall", "Symptom", "Impact", "Mitigation"]
    data = [
        ["Benchmark worship",    "Great demo, poor prod",  "Wasted cycles",     "Eval on YOUR prompts"],
        ["Latency blindness",    "Users silently leave",   "–15-30% engagement", "Set latency budgets first"],
        ["Hidden cost 2-3×",     "Bill exceeds forecast",  "Budget resets",      "Model total cost formula"],
        ["Single-model risk",    "Outage = product down",  "Reliability loss",   "Multi-model fallback"],
        ["Equal treatment",      "$60/M-tok for spam",     "10× overspend",     "Task-based tiers"],
        ["No measurement loop",  "8 months stale",         "Quality & cost drift", "Weekly review cadence"],
    ]

    col_widths = [0.18, 0.21, 0.18, 0.25]
    x_start = 0.09
    y_start = 0.87
    row_h = 0.095

    # Header
    x = x_start
    for j, hdr in enumerate(headers):
        w = col_widths[j]
        rect = mpatches.FancyBboxPatch((x, y_start - row_h), w - 0.01, row_h - 0.005,
                                        boxstyle="round,pad=0.005", fc=WARN, ec="none",
                                        transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + (w - 0.01) / 2, y_start - row_h / 2, hdr,
                ha="center", va="center", fontsize=9, color="#ffffff",
                weight="bold", family=FONT, transform=ax.transAxes)
        x += w

    # Rows
    for i, row in enumerate(data):
        y = y_start - (i + 2) * row_h + 0.005
        bg = WARN_L if i % 2 == 0 else BG
        x = x_start
        for j, cell in enumerate(row):
            w = col_widths[j]
            rect = mpatches.FancyBboxPatch((x, y), w - 0.01, row_h - 0.008,
                                            boxstyle="round,pad=0.003", fc=bg, ec=BORDER,
                                            linewidth=0.4, transform=ax.transAxes)
            ax.add_patch(rect)
            fw = "semibold" if j == 0 else "normal"
            fc = WARN if j == 0 else TEXT_2
            ax.text(x + (w - 0.01) / 2, y + (row_h - 0.008) / 2, cell,
                    ha="center", va="center", fontsize=8, color=fc,
                    weight=fw, family=FONT, transform=ax.transAxes)
            x += w

    _save(fig, "pitfalls-mitigation.png")


# ── 7. 30-Day Swimlane ────────────────────────────────────────────────
def swimlane_30day_png():
    fig, ax = plt.subplots(figsize=(12, 5.5))
    _style_ax(ax)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)

    ax.text(6.5, 6.6, "30-Day Model Selection Playbook",
            ha="center", fontsize=13, weight="bold", color=TEXT, family=FONT)

    lanes = [
        ("Product", 4.8, ACCENT_L),
        ("Engineering", 3.0, SURFACE_2),
        ("Leadership", 1.2, ACCENT_2L),
    ]

    weeks = [
        # (x_start, width, content per lane)
        (1.5, 2.5, [
            "Define top 3-5\nAI use cases",
            "Set latency\nbudgets",
            "Approve cost\nguardrails",
        ]),
        (4.3, 2.5, [
            "Write quality\nscoring rubric",
            "Benchmark 2-4\ncandidates",
            "Review eval\nresults",
        ]),
        (7.1, 2.5, [
            "Monitor user\noutcomes",
            "Run 5-10%\ntraffic pilot",
            "Review pilot\nreport",
        ]),
        (9.9, 2.5, [
            "Own model\nrouting map",
            "Document swap\ntriggers",
            "Set review\ncadence",
        ]),
    ]

    week_labels = ["Week 1: Frame", "Week 2: Evaluate", "Week 3: Pilot", "Week 4: Operationalize"]

    # Week header labels
    for i, (x, w, _) in enumerate(weeks):
        ax.text(x + w / 2, 6.15, week_labels[i], ha="center", fontsize=9,
                color=ACCENT, weight="bold", family=FONT)

    # Lane backgrounds and labels
    for lane_name, lane_y, lane_color in lanes:
        ax.add_patch(mpatches.FancyBboxPatch((0.3, lane_y - 0.1), 12.4, 1.5,
                     boxstyle="round,pad=0.02", fc=lane_color, ec=BORDER, linewidth=0.6, alpha=0.4))
        ax.text(0.8, lane_y + 0.65, lane_name, ha="center", va="center",
                fontsize=9, color=TEXT, weight="bold", family=FONT, rotation=90)

    # Task cards
    for x, w, tasks in weeks:
        for j, (lane_name, lane_y, lane_color) in enumerate(lanes):
            task_text = tasks[j]
            _rounded_box(ax, x, lane_y + 0.15, w, 1.0, task_text,
                        fc=BG, ec=BORDER_D, fontsize=7.5, text_color=TEXT_2, weight="normal")

    # Week divider lines
    for x, w, _ in weeks[1:]:
        ax.plot([x - 0.15, x - 0.15], [0.8, 6.3], color=BORDER, linewidth=0.5, linestyle=":")

    _save(fig, "swimlane-30day.png")


# ── 8. Checklist Card ─────────────────────────────────────────────────
def checklist_card_png():
    fig, ax = plt.subplots(figsize=(7, 8))
    _style_ax(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Card background with shadow
    shadow = FancyBboxPatch((0.085, 0.065), 0.84, 0.87,
                             boxstyle="round,pad=0.02", fc="#e2e8f0", ec="none", alpha=0.5)
    ax.add_patch(shadow)
    card = FancyBboxPatch((0.08, 0.07), 0.84, 0.87,
                           boxstyle="round,pad=0.02", fc=BG, ec=BORDER_D, linewidth=1.2)
    ax.add_patch(card)

    # Header bar
    header = FancyBboxPatch((0.08, 0.85), 0.84, 0.09,
                              boxstyle="round,pad=0.012", fc=ACCENT, ec=ACCENT, linewidth=0)
    ax.add_patch(header)
    ax.text(0.5, 0.895, "Production Readiness Checklist", ha="center", va="center",
            fontsize=13, weight="bold", color="#ffffff", family=FONT)

    items = [
        ("Task-specific quality thresholds with scoring rubric", True),
        ("Maximum acceptable latency per interaction pattern", True),
        ("Cost modeled for baseline, peak, and growth scenarios", True),
        ("Data handling validated per compliance zone", False),
        ("Automatic fallback and escalation paths", True),
        ("Tested with representative AND adversarial prompts", False),
        ("Clear ownership for monitoring and re-evaluation", True),
        ("Specific trigger points for model swap decisions", False),
    ]

    y = 0.79
    for item_text, checked in items:
        # Checkbox
        check_color = ACCENT if checked else BORDER_D
        check_fill = ACCENT_L if checked else BG
        checkbox = FancyBboxPatch((0.12, y - 0.012), 0.032, 0.032,
                                   boxstyle="round,pad=0.002", fc=check_fill, ec=check_color, linewidth=1.0)
        ax.add_patch(checkbox)
        if checked:
            ax.text(0.136, y + 0.005, "v", ha="center", va="center",
                    fontsize=9, color=ACCENT, weight="bold", family=FONT)

        # Item text
        ax.text(0.175, y + 0.004, item_text, fontsize=8.5, va="center",
                color=TEXT if checked else TEXT_3, family=FONT,
                weight="normal" if not checked else "normal")
        y -= 0.075

    # Footer
    ax.text(0.5, 0.14, ">=7 items -- Ready to proceed",
            ha="center", fontsize=9, color=ACCENT, weight="semibold", family=FONT)
    ax.text(0.5, 0.10, "<7 items -- Decision is likely premature",
            ha="center", fontsize=8, color=TEXT_3, family=FONT)

    _save(fig, "checklist-card.png")


# ── 9. Decision Funnel ────────────────────────────────────────────────
def decision_funnel_png():
    fig, ax = plt.subplots(figsize=(8, 7))
    _style_ax(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.text(5, 9.5, "Model Selection Funnel",
            ha="center", fontsize=13, weight="bold", color=TEXT, family=FONT)

    layers = [
        # (y_center, width_ratio, label, sublabel, fc, text_color)
        (7.5, 1.0,  "Requirements",   "7 dimensions defined",           SURFACE_2, TEXT),
        (5.8, 0.75, "Shortlist",       "2–4 candidates with evidence",  ACCENT_2L, TEXT),
        (4.1, 0.52, "Pilot",           "5–10% traffic for 5+ days",     ACCENT_L,  TEXT),
        (2.4, 0.34, "Decision",        "Task-to-model routing map",     ACCENT,    "#ffffff"),
    ]

    for y_c, w_ratio, label, sublabel, fc, tc in layers:
        half_w = w_ratio * 3.5
        h = 1.2
        # Trapezoid shape for funnel effect
        top_hw = half_w + 0.2
        bot_hw = half_w - 0.2
        trap = plt.Polygon([
            (5 - top_hw, y_c + h/2),
            (5 + top_hw, y_c + h/2),
            (5 + bot_hw, y_c - h/2),
            (5 - bot_hw, y_c - h/2),
        ], fc=fc, ec=BORDER_D if label != "Decision" else ACCENT, linewidth=1.2, zorder=2)
        ax.add_patch(trap)

        ax.text(5, y_c + 0.1, label, ha="center", va="center",
                fontsize=12, weight="bold", color=tc, family=FONT, zorder=3)
        sub_c = tc if label == "Decision" else TEXT_3
        ax.text(5, y_c - 0.3, sublabel, ha="center", va="center",
                fontsize=8.5, color=sub_c, family=FONT, zorder=3, alpha=0.85)

    # Arrows between layers
    for i in range(len(layers) - 1):
        y_from = layers[i][0] - 0.6
        y_to = layers[i + 1][0] + 0.6
        _arrow(ax, (5, y_from), (5, y_to), color=TEXT_3, lw=1.0, mutation=12)

    # Side annotations
    ax.text(9.0, 7.5, "Filter by\nconstraints", ha="center", fontsize=8,
            color=TEXT_3, family=FONT, style="italic")
    ax.text(9.0, 5.8, "Score with\nrubric", ha="center", fontsize=8,
            color=TEXT_3, family=FONT, style="italic")
    ax.text(9.0, 4.1, "Measure in\nproduction", ha="center", fontsize=8,
            color=TEXT_3, family=FONT, style="italic")

    _save(fig, "decision-funnel.png")


# ── Main ──────────────────────────────────────────────────────────────
def main():
    print("Rendering publication-quality visuals...")
    model_selection_framework_png()
    print("  ✓ model-selection-framework.png")
    model_routing_flow_png()
    print("  ✓ model-routing-flow.png")
    comparison_matrix_png()
    print("  ✓ comparison-matrix.png")
    tradeoff_2x2_png()
    print("  ✓ tradeoff-2x2.png")
    case_timeline_png()
    print("  ✓ case-timeline.png")
    pitfalls_table_png()
    print("  ✓ pitfalls-mitigation.png")
    swimlane_30day_png()
    print("  ✓ swimlane-30day.png")
    checklist_card_png()
    print("  ✓ checklist-card.png")
    decision_funnel_png()
    print("  ✓ decision-funnel.png")
    print("Done — 9 visuals rendered at 320 DPI.")


if __name__ == "__main__":
    main()
