#!/usr/bin/env python3
"""Renderer for Agent Eval Part 2 blog visuals — 5 PNGs at 320 DPI."""

import os
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Design Tokens
# ---------------------------------------------------------------------------
BASE_TOKENS = {
    'BG': '#ffffff', 'TEXT': '#1e293b', 'TEXT_2': '#475569',
    'MUTED': '#94a3b8', 'GRID': '#e5e7eb', 'LIGHT_BG': '#f8fafc',
}
THEMES = {
    'default': {'ACCENT': '#1f6feb', 'ACCENT_2': '#0d9488', 'ACCENT_3': '#7c3aed',
                'WARN': '#dc2626', 'SUCCESS': '#16a34a',
                'BLUE_BG': '#dbeafe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2'},
    'ocean':   {'ACCENT': '#0ea5e9', 'ACCENT_2': '#06b6d4', 'ACCENT_3': '#155e75',
                'WARN': '#f97316', 'SUCCESS': '#14b8a6',
                'BLUE_BG': '#e0f2fe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#cffafe', 'RED_BG': '#ffedd5'},
    'sunset':  {'ACCENT': '#f97316', 'ACCENT_2': '#ef4444', 'ACCENT_3': '#b91c1c',
                'WARN': '#dc2626', 'SUCCESS': '#eab308',
                'BLUE_BG': '#fff7ed', 'TEAL_BG': '#fef3c7', 'PURPLE_BG': '#fee2e2', 'RED_BG': '#fef2f2'},
    'forest':  {'ACCENT': '#16a34a', 'ACCENT_2': '#65a30d', 'ACCENT_3': '#a16207',
                'WARN': '#ca8a04', 'SUCCESS': '#15803d',
                'BLUE_BG': '#f0fdf4', 'TEAL_BG': '#ecfccb', 'PURPLE_BG': '#fefce8', 'RED_BG': '#fef9c3'},
    'midnight':{'ACCENT': '#7c3aed', 'ACCENT_2': '#6366f1', 'ACCENT_3': '#8b5cf6',
                'WARN': '#ec4899', 'SUCCESS': '#a78bfa',
                'BLUE_BG': '#ede9fe', 'TEAL_BG': '#e0e7ff', 'PURPLE_BG': '#fae8ff', 'RED_BG': '#fce7f3'},
}
DPI = 320
FONT_PATH = '/System/Library/Fonts/HelveticaNeue.ttc'
FONT_PATH_BOLD = '/System/Library/Fonts/HelveticaNeue.ttc'

def get_tokens(theme_name):
    return {**BASE_TOKENS, **THEMES[theme_name]}

def font(size, bold=False):
    idx = 1 if bold else 0  # index 0=Regular, 1=Bold in .ttc
    try:
        return ImageFont.truetype(FONT_PATH, size, index=idx)
    except Exception:
        return ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', size)

def font_mono(size):
    try:
        return ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', size)
    except Exception:
        return font(size)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)


# ---------------------------------------------------------------------------
# Visual 1: Tool Name Translation (theme: default)
# ---------------------------------------------------------------------------
def render_tool_name_translation(tokens):
    W, H = 3200, 1550
    img = Image.new('RGB', (W, H), tokens['BG'])
    draw = ImageDraw.Draw(img)

    # Warning banner at top
    banner_h = 200
    draw.rectangle([0, 0, W, banner_h], fill=tokens['RED_BG'])
    # Warning icon as text
    warn_font = font(72, bold=True)
    warn_text = "!!  THE #1 SETUP GOTCHA  !!"
    bb = draw.textbbox((0, 0), warn_text, font=warn_font)
    tx = (W - (bb[2] - bb[0])) // 2
    ty = (banner_h - (bb[3] - bb[1])) // 2 - 10
    draw.text((tx, ty), warn_text, fill=tokens['WARN'], font=warn_font)

    # Subtitle
    sub_font = font(36)
    sub_text = 'Your grader checks for "execute" but the eval env uses "bash". Every test fails.'
    bb = draw.textbbox((0, 0), sub_text, font=sub_font)
    sx = (W - (bb[2] - bb[0])) // 2
    draw.text((sx, banner_h + 30), sub_text, fill=tokens['TEXT_2'], font=sub_font)

    # Table
    table_top = banner_h + 120
    row_h = 110
    col1_x = 400
    col2_x = 1700
    arrow_x = 1480
    margin = 300

    # Header row
    hdr_font = font(42, bold=True)
    draw.rectangle([margin, table_top, W - margin, table_top + row_h], fill=tokens['BLUE_BG'])
    draw.text((col1_x, table_top + 30), "VS Code Tool Name", fill=tokens['ACCENT'], font=hdr_font)
    draw.text((col2_x, table_top + 30), "SDK / Eval Name", fill=tokens['ACCENT'], font=hdr_font)

    # Data rows
    mappings = [
        ("execute", "bash"),
        ("read", "view"),
        ("search", "grep"),
        ("editFile", "edit"),
        ("createFile", "create"),
        ("runQuery", "sql"),
        ("spawnAgent", "task"),
    ]
    mono = font_mono(40)
    mono_bold = font_mono(42)
    arrow_font = font(44, bold=True)
    row_font = font(40)

    for i, (left, right) in enumerate(mappings):
        y = table_top + row_h * (i + 1)
        bg = tokens['LIGHT_BG'] if i % 2 == 0 else tokens['BG']
        draw.rectangle([margin, y, W - margin, y + row_h], fill=bg)
        draw.line([margin, y, W - margin, y], fill=tokens['GRID'], width=2)
        draw.text((col1_x, y + 30), left, fill=tokens['WARN'], font=mono)
        draw.text((arrow_x, y + 28), "->", fill=tokens['MUTED'], font=arrow_font)
        draw.text((col2_x, y + 30), right, fill=tokens['SUCCESS'], font=mono_bold)

    # Bottom border
    last_y = table_top + row_h * 8
    draw.line([margin, last_y, W - margin, last_y], fill=tokens['GRID'], width=2)

    # Outer table border
    draw.rectangle([margin, table_top, W - margin, last_y], outline=tokens['GRID'], width=3)

    # Left column labels
    label_font = font(30, bold=True)
    # "WRONG" label for left column
    draw.text((col1_x, table_top + row_h + 30 + row_h * 7 + 40), "", fill=tokens['WARN'], font=label_font)

    # Bottom callout
    callout_y = last_y + 60
    callout_font = font(34, bold=True)
    callout_text = "Every tool_constraint grader must use the right-hand column (SDK names)."
    bb = draw.textbbox((0, 0), callout_text, font=callout_font)
    cx = (W - (bb[2] - bb[0])) // 2
    draw.text((cx, callout_y), callout_text, fill=tokens['ACCENT'], font=callout_font)

    # Strike-through decoration on left column header area
    # Red X / Green check labels
    label_y = last_y + 130
    draw.text((col1_x - 80, label_y), "[X] Don't use these in graders", fill=tokens['WARN'], font=font(32, bold=True))
    draw.text((col2_x - 80, label_y), "[OK] Use these in graders", fill=tokens['SUCCESS'], font=font(32, bold=True))

    img.save(os.path.join(OUT_DIR, 'tool_name_translation.png'), dpi=(DPI, DPI))
    print("  [OK] tool_name_translation.png")


# ---------------------------------------------------------------------------
# Visual 2: Grading Decision Tree (theme: ocean) — matplotlib
# ---------------------------------------------------------------------------
def render_grading_decision_tree(tokens):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor(tokens['BG'])
    ax.set_facecolor(tokens['BG'])
    ax.set_xlim(-0.5, 11)
    ax.set_ylim(0.5, 8)
    ax.axis('off')

    # Title
    ax.text(5, 7.5, 'Grading Decision Tree', fontsize=18, fontweight='bold',
            ha='center', va='center', color=tokens['TEXT'], fontfamily='Helvetica Neue')

    def draw_diamond(cx, cy, w, h, text, color):
        from matplotlib.patches import Polygon
        pts = [(cx, cy + h/2), (cx + w/2, cy), (cx, cy - h/2), (cx - w/2, cy)]
        poly = Polygon(pts, closed=True, facecolor=color, edgecolor=tokens['TEXT'], linewidth=1.5, zorder=3)
        ax.add_patch(poly)
        lines = text.split('\n')
        for i, line in enumerate(lines):
            offset = ((len(lines)-1)/2 - i) * 0.22
            ax.text(cx, cy + offset, line, ha='center', va='center', fontsize=9,
                    fontweight='bold', color=tokens['TEXT'], zorder=4, fontfamily='Helvetica Neue')

    def draw_box(cx, cy, w, h, text, color, text_color=None, fontsize=10):
        box = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                             boxstyle="round,pad=0.1", facecolor=color,
                             edgecolor=tokens['TEXT'], linewidth=1.5, zorder=3)
        ax.add_patch(box)
        tc = text_color or tokens['TEXT']
        lines = text.split('\n')
        for i, line in enumerate(lines):
            offset = ((len(lines)-1)/2 - i) * 0.28
            fw = 'bold' if i == 0 else 'normal'
            fs = fontsize if i == 0 else fontsize - 1
            ax.text(cx, cy + offset, line, ha='center', va='center', fontsize=fs,
                    fontweight=fw, color=tc, zorder=4, fontfamily='Helvetica Neue')

    def arrow(x1, y1, x2, y2, label='', label_side='right'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=tokens['TEXT_2'], lw=1.8),
                    zorder=2)
        if label:
            mx = (x1 + x2) / 2
            my = (y1 + y2) / 2
            offset = 0.18 if label_side == 'right' else -0.18
            ax.text(mx + offset, my + 0.08, label, fontsize=9, fontweight='bold',
                    color=tokens['ACCENT'], ha='center', va='center', fontfamily='Helvetica Neue')

    # Start node
    draw_box(5, 6.6, 2.8, 0.5, 'What are you checking?', tokens['BLUE_BG'])

    # Diamond 1 — keywords
    draw_diamond(5, 5.5, 3.2, 0.8, 'Keywords / patterns\nin agent text?', tokens['TEAL_BG'])
    arrow(5, 6.35, 5, 5.9)

    # Terminal 1
    draw_box(8.2, 5.5, 2.6, 0.8, 'text grader\nFree, instant', tokens['BLUE_BG'])
    arrow(6.6, 5.5, 6.9, 5.5, 'YES')

    # Diamond 2 — tool calls
    draw_diamond(5, 4.0, 3.2, 0.8, 'Tool calls\nmade / not made?', tokens['TEAL_BG'])
    arrow(5, 5.1, 5, 4.4, 'NO')

    # Terminal 2
    draw_box(8.2, 4.0, 2.6, 0.8, 'tool_constraint\nFree, instant', tokens['BLUE_BG'])
    arrow(6.6, 4.0, 6.9, 4.0, 'YES')

    # Diamond 3 — complex
    draw_diamond(5, 2.5, 3.2, 0.8, 'Complex behavioral\njudgment?', tokens['TEAL_BG'])
    arrow(5, 3.6, 5, 2.9, 'NO')

    # Terminal 3
    draw_box(8.2, 2.5, 2.6, 0.8, 'prompt grader\nLLM judge (costly)', tokens['RED_BG'])
    arrow(6.6, 2.5, 6.9, 2.5, 'YES')

    # Footer
    ax.text(5, 1.3, 'Always prefer the cheapest grader that catches the failure.',
            fontsize=11, fontstyle='italic', ha='center', va='center',
            color=tokens['ACCENT_3'], fontfamily='Helvetica Neue')

    plt.tight_layout(pad=0.5)
    fig.savefig(os.path.join(OUT_DIR, 'grading_decision_tree.png'), dpi=DPI,
                facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close(fig)
    print("  [OK] grading_decision_tree.png")


# ---------------------------------------------------------------------------
# Visual 3: Binary vs Score Grading (theme: sunset)
# ---------------------------------------------------------------------------
def render_binary_vs_score(tokens):
    W, H = 3200, 1500
    img = Image.new('RGB', (W, H), tokens['BG'])
    draw = ImageDraw.Draw(img)

    # Title
    title_font = font(56, bold=True)
    title = "Binary Grading Is a Feature, Not a Limitation"
    bb = draw.textbbox((0, 0), title, font=title_font)
    draw.text(((W - (bb[2]-bb[0]))//2, 50), title, fill=tokens['TEXT'], font=title_font)

    panel_top = 160
    panel_h = 1000
    panel_w = 1400
    gap = 120
    left_x = (W - 2 * panel_w - gap) // 2
    right_x = left_x + panel_w + gap
    radius = 30

    # --- Left panel: Score-based (bad) ---
    rounded_rect(draw, [left_x, panel_top, left_x + panel_w, panel_top + panel_h],
                 radius, fill=tokens['PURPLE_BG'], outline=tokens['ACCENT_2'], width=3)

    lbl_font = font(42, bold=True)
    draw.text((left_x + 80, panel_top + 50), "Score-Based Grading", fill=tokens['ACCENT_2'], font=lbl_font)

    # Score display
    score_font = font(96, bold=True)
    score_text = "3.7 / 5.0"
    bb = draw.textbbox((0, 0), score_text, font=score_font)
    sx = left_x + (panel_w - (bb[2]-bb[0])) // 2
    draw.text((sx, panel_top + 200), score_text, fill=tokens['ACCENT_2'], font=score_font)

    # Score bar background
    bar_y = panel_top + 380
    bar_x = left_x + 120
    bar_w = panel_w - 240
    bar_h = 40
    draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h],
                           radius=10, fill=tokens['GRID'])
    fill_w = int(bar_w * 3.7 / 5.0)
    draw.rounded_rectangle([bar_x, bar_y, bar_x + fill_w, bar_y + bar_h],
                           radius=10, fill=tokens['ACCENT_2'])

    # Confused reviewer
    q_font = font(38)
    q_font_b = font(38, bold=True)
    questions = [
        '"What does 3.7 actually mean?"',
        '"Is this good enough to ship?"',
        '"Last run was 3.4 -- is that a regression?"',
        '"Should we change the threshold?"',
    ]
    qy = bar_y + 80
    for q in questions:
        draw.text((left_x + 100, qy), q, fill=tokens['TEXT_2'], font=q_font)
        qy += 60

    # Verdict
    verdict_font = font(36, bold=True)
    draw.text((left_x + 100, panel_top + panel_h - 180), "Outcome: AMBIGUITY",
              fill=tokens['WARN'], font=verdict_font)
    draw.text((left_x + 100, panel_top + panel_h - 120), "Nobody knows if this should merge.",
              fill=tokens['MUTED'], font=font(30))

    # --- Right panel: Binary (good) ---
    rounded_rect(draw, [right_x, panel_top, right_x + panel_w, panel_top + panel_h],
                 radius, fill=tokens['BLUE_BG'], outline=tokens['ACCENT'], width=3)

    draw.text((right_x + 80, panel_top + 50), "Binary Grading", fill=tokens['ACCENT'], font=lbl_font)

    # FAIL badge
    fail_font = font(72, bold=True)
    draw.text((right_x + 120, panel_top + 200), "FAIL", fill=tokens['WARN'], font=fail_font)

    # Reason
    reason_font = font(36)
    reason_font_b = font(36, bold=True)
    draw.text((right_x + 100, panel_top + 340), "Agent didn't gate at step 1.",
              fill=tokens['TEXT'], font=reason_font_b)
    draw.text((right_x + 100, panel_top + 400), "Fabricated OIDC configuration claims.",
              fill=tokens['TEXT_2'], font=reason_font)

    # Clear reviewer response
    ry = panel_top + 520
    responses = [
        '"I know exactly what broke."',
        '"The fix is clear: add gating logic."',
        '"CI is red -> block merge."',
    ]
    for r in responses:
        draw.text((right_x + 100, ry), r, fill=tokens['TEXT_2'], font=q_font)
        ry += 60

    # Verdict
    draw.text((right_x + 100, panel_top + panel_h - 180), "Outcome: CLARITY",
              fill=tokens['SUCCESS'], font=verdict_font)
    draw.text((right_x + 100, panel_top + panel_h - 120), "Reviewer knows the fix. CI blocks the merge.",
              fill=tokens['MUTED'], font=font(30))

    # VS divider circle
    vs_x = left_x + panel_w + gap // 2
    vs_y = panel_top + panel_h // 2
    r = 50
    draw.ellipse([vs_x - r, vs_y - r, vs_x + r, vs_y + r], fill=tokens['TEXT'], outline=tokens['TEXT'])
    vs_font = font(36, bold=True)
    bb = draw.textbbox((0, 0), "vs", font=vs_font)
    draw.text((vs_x - (bb[2]-bb[0])//2, vs_y - (bb[3]-bb[1])//2 - 2), "vs",
              fill=tokens['BG'], font=vs_font)

    # Bottom tagline
    tag_font = font(34, bold=True)
    tag = "Binary = reproducible + actionable + CI-native"
    bb = draw.textbbox((0, 0), tag, font=tag_font)
    draw.text(((W - (bb[2]-bb[0]))//2, H - 120), tag, fill=tokens['ACCENT'], font=tag_font)

    img.save(os.path.join(OUT_DIR, 'binary_vs_score_grading.png'), dpi=(DPI, DPI))
    print("  [OK] binary_vs_score_grading.png")


# ---------------------------------------------------------------------------
# Visual 4: Task Pattern Matrix (theme: forest)
# ---------------------------------------------------------------------------
def render_task_pattern_matrix(tokens):
    W, H = 3200, 1900
    img = Image.new('RGB', (W, H), tokens['BG'])
    draw = ImageDraw.Draw(img)

    # Title
    title_font = font(56, bold=True)
    title = "The Four Task Patterns"
    bb = draw.textbbox((0, 0), title, font=title_font)
    draw.text(((W - (bb[2]-bb[0]))//2, 60), title, fill=tokens['TEXT'], font=title_font)

    sub_font = font(34)
    sub = "Every eval task falls into one of these quadrants"
    bb = draw.textbbox((0, 0), sub, font=sub_font)
    draw.text(((W - (bb[2]-bb[0]))//2, 140), sub, fill=tokens['TEXT_2'], font=sub_font)

    # Matrix layout
    margin_left = 550
    margin_top = 260
    cell_w = 1200
    cell_h = 620
    header_h = 80

    # Column headers
    col_hdr_font = font(38, bold=True)
    for i, label in enumerate(["Agent Should Act", "Agent Should Refuse"]):
        cx = margin_left + i * cell_w + cell_w // 2
        draw.text((cx - 140, margin_top - 60), label, fill=tokens['ACCENT'], font=col_hdr_font)

    # Row headers (rotated via multiple text)
    row_hdr_font = font(36, bold=True)
    for i, label in enumerate(["On-Topic", "Off-Topic"]):
        cy = margin_top + i * cell_h + cell_h // 2
        # Write vertically-ish
        draw.text((margin_left - 350, cy - 30), label, fill=tokens['ACCENT'], font=row_hdr_font)
        sub_label = "Request"
        draw.text((margin_left - 300, cy + 20), sub_label, fill=tokens['ACCENT'], font=font(30))

    # Quadrant data
    quads = [
        # (row, col, title, example, color, tag_color)
        (0, 0, "Happy-Path", "Generate ARM template\nwith CAF naming", tokens['BLUE_BG'], tokens['SUCCESS']),
        (0, 1, "Safety Gate", "Deploy without\nconfirmation step", tokens['TEAL_BG'], tokens['WARN']),
        (1, 0, "N/A", "This quadrant\ndoesn't exist", tokens['LIGHT_BG'], tokens['MUTED']),
        (1, 1, "Off-Topic Refusal", "Bake sourdough bread\n(The Sourdough Test)", tokens['PURPLE_BG'], tokens['ACCENT']),
    ]

    for row, col, title, example, bg, tag_color in quads:
        x = margin_left + col * cell_w
        y = margin_top + row * cell_h
        rounded_rect(draw, [x + 10, y + 10, x + cell_w - 10, y + cell_h - 10],
                     20, fill=bg, outline=tokens['GRID'], width=2)

        # Title
        tf = font(44, bold=True)
        bb = draw.textbbox((0, 0), title, font=tf)
        tx = x + (cell_w - (bb[2]-bb[0])) // 2
        draw.text((tx, y + 80), title, fill=tag_color, font=tf)

        # Tag line under title
        tag_line_y = y + 150
        draw.line([x + 200, tag_line_y, x + cell_w - 200, tag_line_y], fill=tokens['GRID'], width=2)

        # Example
        ef = font(34)
        lines = example.split('\n')
        ey = y + 200
        for line in lines:
            bb = draw.textbbox((0, 0), line, font=ef)
            lx = x + (cell_w - (bb[2]-bb[0])) // 2
            draw.text((lx, ey), line, fill=tokens['TEXT_2'], font=ef)
            ey += 50

        # Grader tags
        if title == "Happy-Path":
            tags = ["text", "tool_constraint", "prompt"]
        elif title == "Safety Gate":
            tags = ["tool_constraint", "prompt"]
        elif title == "Off-Topic Refusal":
            tags = ["text"]
        else:
            tags = []

        if tags:
            tag_font_sm = font(26, bold=True)
            total_w = sum(draw.textbbox((0, 0), t, font=tag_font_sm)[2] - draw.textbbox((0, 0), t, font=tag_font_sm)[0] + 40 for t in tags) + 15 * (len(tags) - 1)
            start_x = x + (cell_w - total_w) // 2
            ty = y + cell_h - 160
            for t in tags:
                bb = draw.textbbox((0, 0), t, font=tag_font_sm)
                tw = bb[2] - bb[0] + 40
                th = bb[3] - bb[1] + 20
                rounded_rect(draw, [start_x, ty, start_x + tw, ty + th + 10],
                             10, fill=tokens['BG'], outline=tag_color, width=2)
                draw.text((start_x + 20, ty + 8), t, fill=tag_color, font=tag_font_sm)
                start_x += tw + 15

    img.save(os.path.join(OUT_DIR, 'task_pattern_matrix.png'), dpi=(DPI, DPI))
    print("  [OK] task_pattern_matrix.png")


# ---------------------------------------------------------------------------
# Visual 5: Eval Pipeline Flow (theme: midnight)
# ---------------------------------------------------------------------------
def render_eval_pipeline_flow(tokens):
    W, H = 3840, 1200
    img = Image.new('RGB', (W, H), tokens['BG'])
    draw = ImageDraw.Draw(img)

    # Title
    title_font = font(52, bold=True)
    title = "From PR to PR Comment: The Eval Pipeline"
    bb = draw.textbbox((0, 0), title, font=title_font)
    draw.text(((W - (bb[2]-bb[0]))//2, 50), title, fill=tokens['TEXT'], font=title_font)

    stages = [
        ("PR Trigger", "Push or PR\nevent fires"),
        ("Path Filter", "Changed files\nmatch agent paths"),
        ("Agent\nDiscovery", "Find affected\nagents & skills"),
        ("Mirror Sync", "Copy agent code\nto eval workspace"),
        ("Token Budget", "Calculate max\ntokens per task"),
        ("Copilot\nSession", "Run agent in\nsandbox env"),
        ("3-Layer\nGrading", "text -> tool ->\nprompt graders"),
        ("PR Comment", "Post results\nback to PR"),
    ]

    n = len(stages)
    margin = 160
    stage_w = 340
    gap = (W - 2 * margin - n * stage_w) / (n - 1)
    cy = 480
    box_h = 240
    desc_offset = 180

    colors = [tokens['BLUE_BG'], tokens['TEAL_BG'], tokens['BLUE_BG'], tokens['TEAL_BG'],
              tokens['PURPLE_BG'], tokens['BLUE_BG'], tokens['PURPLE_BG'], tokens['BLUE_BG']]
    border_colors = [tokens['ACCENT'], tokens['ACCENT_2'], tokens['ACCENT'], tokens['ACCENT_2'],
                     tokens['ACCENT_3'], tokens['ACCENT'], tokens['ACCENT_3'], tokens['ACCENT']]

    for i, (label, desc) in enumerate(stages):
        x = margin + i * (stage_w + gap)
        # Box
        rounded_rect(draw, [x, cy - box_h//2, x + stage_w, cy + box_h//2],
                     20, fill=colors[i], outline=border_colors[i], width=3)

        # Stage number
        num_font = font(28, bold=True)
        draw.text((x + 15, cy - box_h//2 + 12), str(i + 1), fill=border_colors[i], font=num_font)

        # Label
        lbl_font = font(34, bold=True)
        lines = label.split('\n')
        total_h = len(lines) * 42
        start_y = cy - total_h // 2 + 10
        for j, line in enumerate(lines):
            bb = draw.textbbox((0, 0), line, font=lbl_font)
            lx = x + (stage_w - (bb[2]-bb[0])) // 2
            draw.text((lx, start_y + j * 42), line, fill=tokens['TEXT'], font=lbl_font)

        # Description below box
        desc_font = font(26)
        dlines = desc.split('\n')
        dy = cy + box_h//2 + 30
        for dl in dlines:
            bb = draw.textbbox((0, 0), dl, font=desc_font)
            dx = x + (stage_w - (bb[2]-bb[0])) // 2
            draw.text((dx, dy), dl, fill=tokens['TEXT_2'], font=desc_font)
            dy += 36

        # Arrow to next stage
        if i < n - 1:
            ax1 = x + stage_w + 8
            ax2 = x + stage_w + gap - 8
            ay = cy
            # Arrow line
            draw.line([ax1, ay, ax2 - 15, ay], fill=tokens['MUTED'], width=3)
            # Arrowhead
            draw.polygon([(ax2, ay), (ax2 - 18, ay - 10), (ax2 - 18, ay + 10)],
                         fill=tokens['MUTED'])

    # Time/cost annotation
    ann_font = font(36, bold=True)
    ann_y = cy + box_h // 2 + 180

    # Bracket-style annotation
    bracket_x1 = margin
    bracket_x2 = margin + (n - 1) * (stage_w + gap) + stage_w
    bracket_y = ann_y - 30
    draw.line([bracket_x1, bracket_y, bracket_x2, bracket_y], fill=tokens['ACCENT'], width=2)
    draw.line([bracket_x1, bracket_y - 15, bracket_x1, bracket_y], fill=tokens['ACCENT'], width=2)
    draw.line([bracket_x2, bracket_y - 15, bracket_x2, bracket_y], fill=tokens['ACCENT'], width=2)

    # Cost labels
    cost_text = "15-25 min total  |  ~3-8 USD per run"
    bb = draw.textbbox((0, 0), cost_text, font=ann_font)
    draw.text(((W - (bb[2]-bb[0]))//2, ann_y), cost_text, fill=tokens['ACCENT'], font=ann_font)

    # Subtitle
    sub_font = font(30)
    sub = "Fully automated: no human in the loop until the PR comment appears"
    bb = draw.textbbox((0, 0), sub, font=sub_font)
    draw.text(((W - (bb[2]-bb[0]))//2, ann_y + 60), sub, fill=tokens['MUTED'], font=sub_font)

    img.save(os.path.join(OUT_DIR, 'eval_pipeline_flow.png'), dpi=(DPI, DPI))
    print("  [OK] eval_pipeline_flow.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    theme_order = ['default', 'ocean', 'sunset', 'forest', 'midnight']
    renderers = [
        (render_tool_name_translation, 'default'),
        (render_grading_decision_tree, 'ocean'),
        (render_binary_vs_score, 'sunset'),
        (render_task_pattern_matrix, 'forest'),
        (render_eval_pipeline_flow, 'midnight'),
    ]
    print(f"Rendering {len(renderers)} visuals for Agent Eval Part 2...")
    for render_fn, theme in renderers:
        tokens = get_tokens(theme)
        render_fn(tokens)
    print("Done!")

if __name__ == '__main__':
    main()
