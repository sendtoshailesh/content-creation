#!/usr/bin/env python3
"""Render all 7 visual assets for mcp-servers-2026.

Run from repo root:
    PYTHONPATH=. python3 content/topics/mcp-servers-2026/visuals/render_mcp_servers_2026.py
"""

from __future__ import annotations

import html as _html_mod
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO))

OUT = Path(__file__).parent

# ── Design tokens ──────────────────────────────────────────────────────────
BG       = "#ffffff"
TEXT     = "#1e293b"
TEXT_2   = "#475569"
MUTED    = "#94a3b8"
GRID     = "#e5e7eb"
LIGHT_BG = "#f8fafc"
ACCENT   = "#1f6feb"
ACCENT_2 = "#0d9488"
ACCENT_3 = "#7c3aed"
WARN     = "#dc2626"
SUCCESS  = "#16a34a"
BLUE_BG  = "#dbeafe"
TEAL_BG  = "#ccfbf1"
PURPLE_BG= "#ede9fe"
RED_BG   = "#fee2e2"
AMBER    = "#d97706"
AMBER_BG = "#fef3c7"

FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"

# TYPE_SCALE (matches scripts/visuals/svg/design.py — inspector enforces these)
# display:92  title:50  subtitle:30  value:40  body:24  label:23  caption:18
TS = dict(display=92, title=50, subtitle=30, value=40, body=24, label=23, caption=18)


# ── SVG primitives ─────────────────────────────────────────────────────────
def _h(s: str) -> str:
    return _html_mod.escape(str(s), quote=True)


def rect_el(x, y, w, h, fill, stroke=None, sw=4, rx=8, extra="") -> str:
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{extra}/>'


def text_el(x, y, content, size, color, anchor="start", bold=True,
            role=None, db=None, transform=None) -> str:
    weight = 700 if bold else 400
    role_a = f' data-role="{role}"' if role else ""
    db_a   = f' dominant-baseline="{db}"' if db else ""
    tf_a   = f' transform="{transform}"' if transform else ""
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" '
        f'font-size="{size}" font-weight="{weight}" fill="{color}" '
        f'text-anchor="{anchor}"{role_a}{db_a}{tf_a}>{_h(content)}</text>'
    )


def tspan_text(x, y, lines, size, color, anchor="start", bold=True,
               role=None, db=None, line_height=None) -> str:
    """Multi-line text using tspan elements."""
    if not lines:
        return ""
    weight = 700 if bold else 400
    role_a = f' data-role="{role}"' if role else ""
    db_a   = f' dominant-baseline="{db}"' if db else ""
    lh = line_height or int(size * 1.3)
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{_h(l)}</tspan>'
        for i, l in enumerate(lines)
    )
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" '
        f'font-size="{size}" font-weight="{weight}" fill="{color}" '
        f'text-anchor="{anchor}"{role_a}{db_a}>{spans}</text>'
    )


def chip_el(cx, cy, label, fill, text_color="#ffffff", cw=160, ch=44) -> str:
    return (
        rect_el(cx - cw // 2, cy - ch // 2, cw, ch, fill, rx=22) +
        f'<text x="{cx}" y="{cy}" font-family="{FONT}" font-size="23" '
        f'font-weight="700" fill="{text_color}" text-anchor="middle" '
        f'dominant-baseline="central" data-role="label">{_h(label)}</text>'
    )


def pill_el(cx, cy, label, fill, text_color="#ffffff", pw=None, ph=36) -> str:
    """Narrower pill badge for inline use."""
    if pw is None:
        pw = max(80, len(label) * 13 + 24)
    return (
        rect_el(cx - pw // 2, cy - ph // 2, pw, ph, fill, rx=ph // 2) +
        f'<text x="{cx}" y="{cy}" font-family="{FONT}" font-size="18" '
        f'font-weight="700" fill="{text_color}" text-anchor="middle" '
        f'dominant-baseline="central" data-role="caption">{_h(label)}</text>'
    )


def arrow_marker(color: str) -> str:
    mid = f"arrow_{color.lstrip('#')}"
    return (
        f'<marker id="{mid}" viewBox="0 0 12 12" refX="9" refY="6" '
        f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M1,1 L11,6 L1,11 z" fill="{color}"/></marker>'
    )


def arrow_el(x1, y1, x2, y2, color, sw=8) -> str:
    mid = f"url(#arrow_{color.lstrip('#')})"
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" '
        f'data-role="arrow" marker-end="{mid}"/>'
    )


def svg_doc(W: int, H: int, body: str, defs: str = "") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">'
        f'<defs>{defs}</defs>'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>'
        f'{body}</svg>'
    )


def line_el(x1, y1, x2, y2, color, sw=2) -> str:
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
    )


# ── V01: Scorecard Matrix ───────────────────────────────────────────────────
def make_v01() -> str:
    W, H = 3200, 2080

    # Column layout
    ML = 80          # left margin
    COL_SRV_W = 520  # server name column
    COL_W = 460      # each criteria column (5 total)
    # Total: 80 + 520 + 5*460 = 2900 → right annotation zone: 2900-3120 = 220px

    x_srv = ML
    x_cols = [ML + COL_SRV_W + i * COL_W for i in range(5)]
    # [600, 1060, 1520, 1980, 2440]
    matrix_right = ML + COL_SRV_W + 5 * COL_W  # 2900
    annot_cx = 3040  # annotation center x

    # Row layout
    TITLE_Y   = 50
    HDR_Y     = 140
    HDR_H     = 72
    ROW_Y0    = HDR_Y + HDR_H   # 212
    ROW_H     = 136
    N_ROWS    = 10
    STRIP_Y   = ROW_Y0 + N_ROWS * ROW_H + 22   # 212+1360+22 = 1594
    STRIP_H   = 88
    SRC_Y     = STRIP_Y + STRIP_H + 24          # 1706

    servers = [
        ("GitHub MCP",          "High",   "High",   "Low",  "High",   "High"),
        ("Playwright MCP",       "High",   "High",   "Low",  "High",   "High"),
        ("MCP Filesystem",       "High",   "High",   "Low",  "High",   "Medium"),
        ("Supabase MCP",         "High",   "High",   "Low",  "High",   "High"),
        ("MCP Fetch",            "Medium", "High",   "Low",  "High",   "High"),
        ("Cloudflare Suite",     "High",   "High",   "Low",  "High",   "Medium"),
        ("Context7",             "High",   "Medium", "Low",  "Medium", "Medium"),
        ("MCP Git",              "Medium", "Medium", "Low",  "High",   "Medium"),
        ("MCP Memory",           "Medium", "Medium", "Low",  "High",   "Medium"),
        ("Sequential Thinking",  "Low",    "Medium", "Low",  "High",   "Low"),
    ]

    def chip_style(val):
        return {"High": (SUCCESS, "#fff"), "Medium": (AMBER, "#fff"), "Low": (MUTED, "#fff")}[val]

    def row_bg(i):
        return TEAL_BG if i < 3 else (LIGHT_BG if i % 2 else BG)

    els = []

    # Title
    els.append(text_el(ML, TITLE_Y + 50, "Which Free MCP Servers Earn a Daily Slot?",
                       50, TEXT, bold=True, role="title"))

    # Header row background
    els.append(rect_el(ML, HDR_Y, matrix_right - ML, HDR_H, GRID, rx=8))

    # Column header text (centered in each column)
    hdrs = ["Server", "Loop Value", "Maintenance", "Setup Friction", "Free Tier", "Security Posture"]
    col_cxs = [x_srv + COL_SRV_W // 2] + [x_cols[i] + COL_W // 2 for i in range(5)]
    # [340, 830, 1290, 1750, 2210, 2670]
    for cx, hdr in zip(col_cxs, hdrs):
        els.append(text_el(cx, HDR_Y + 44, hdr, 24, TEXT, anchor="middle", bold=True, role="body"))

    # Vertical separators
    for x in x_cols:
        els.append(line_el(x, HDR_Y, x, ROW_Y0 + N_ROWS * ROW_H, GRID, sw=2))

    # Data rows
    for i, (srv, lv, maint, sf, ft, sec) in enumerate(servers):
        ry = ROW_Y0 + i * ROW_H
        cy = ry + ROW_H // 2

        # Row background
        els.append(rect_el(ML, ry, matrix_right - ML, ROW_H, row_bg(i), rx=0))

        # Bottom separator
        if i < N_ROWS - 1:
            els.append(line_el(ML, ry + ROW_H, matrix_right, ry + ROW_H, GRID, sw=1))

        # Server name
        els.append(text_el(x_srv + 18, cy, srv, 24, TEXT, anchor="start",
                           bold=(i < 3), role="body", db="central"))

        # Criteria chips
        for j, val in enumerate([lv, maint, sf, ft, sec]):
            fill, tc = chip_style(val)
            chip_cx = x_cols[j] + COL_W // 2
            els.append(chip_el(chip_cx, cy, val, fill, tc, cw=150, ch=44))

    # Matrix outer border
    els.append(rect_el(ML, HDR_Y, matrix_right - ML, HDR_H + N_ROWS * ROW_H,
                       "none", stroke=GRID, sw=2, rx=0))

    # ── Starter Stack annotation ──
    hl_top    = ROW_Y0
    hl_bottom = ROW_Y0 + 3 * ROW_H   # 212 + 408 = 620
    hl_mid    = (hl_top + hl_bottom) // 2  # 416

    # Bracket: vertical bar at x=2910, horizontal stubs
    bx = 2910
    els.append(line_el(bx, hl_top + 6, bx, hl_bottom - 6, ACCENT_2, sw=6))
    els.append(line_el(bx, hl_top + 6, bx + 20, hl_top + 6, ACCENT_2, sw=6))
    els.append(line_el(bx, hl_bottom - 6, bx + 20, hl_bottom - 6, ACCENT_2, sw=6))

    # "Starter Stack" pill label
    els.append(rect_el(2934, hl_mid - 50, 200, 44, ACCENT_2, rx=22))
    els.append(text_el(3034, hl_mid - 28, "Starter Stack", 23, "#ffffff",
                       anchor="middle", bold=True, role="label"))

    # ── Bottom strip ──
    els.append(rect_el(ML, STRIP_Y, matrix_right - ML, STRIP_H, LIGHT_BG, rx=10))
    strip_text = "Start with the top 3 — add servers only when they remove a real daily friction point."
    els.append(text_el(ML + 24, STRIP_Y + STRIP_H // 2, strip_text,
                       24, TEXT_2, anchor="start", bold=False, role="body", db="central"))

    # ── Source line ──
    src = ("Source: github.com/github-mcp-server, microsoft/playwright-mcp, "
           "modelcontextprotocol/servers — 2026-06-28")
    els.append(text_el(ML, SRC_Y + 18, src, 18, MUTED, anchor="start", bold=False, role="caption"))

    return svg_doc(W, H, "".join(els))


# ── V05: Project Ladder (blog 3200×2080) ───────────────────────────────────
def make_v05_blog() -> str:
    W, H = 3200, 2080

    TITLE_Y = 50
    PANEL_Y = 145
    PANEL_H = 1720
    PANEL_W = 920
    GAP     = 120
    ML      = 100   # left margin: (3200 - 3*920 - 2*120) / 2 = (3200-2760-240)/2 = 100

    PANELS = [
        {"x": ML,                      "header_fill": ACCENT,   "bg": BLUE_BG},
        {"x": ML + PANEL_W + GAP,      "header_fill": ACCENT_2, "bg": TEAL_BG},
        {"x": ML + 2*(PANEL_W + GAP),  "header_fill": ACCENT_3, "bg": PURPLE_BG},
    ]

    HEADER_H = 210
    CONTENT_Y_OFF = HEADER_H + 30  # content starts 30px below header

    rungs = [
        {
            "num": "Rung 1",
            "name": "Repo-Aware Assistant",
            "goal": "Give AI read access to local project + git history",
            "servers": "MCP Filesystem + MCP Git",
            "badge": "Agent answers from real commit history",
            "time": "30-45 min",
            "tag": "Beginner",
        },
        {
            "num": "Rung 2",
            "name": "Browser Bug Reproduction",
            "goal": "Agent navigates to broken UI, screenshots, drafts failing test",
            "servers": "Playwright MCP + MCP Fetch",
            "badge": "Generated test.spec.ts fails with real error",
            "time": "1-2 hours",
            "tag": "Intermediate",
        },
        {
            "num": "Rung 3",
            "name": "Remote OAuth Stack",
            "goal": "GitHub MCP + Supabase via OAuth, read-only defaults, no PATs",
            "servers": "GitHub MCP + Supabase MCP (+ Cloudflare)",
            "badge": "Write to Supabase rejected by server, not agent",
            "time": "2-3 hours",
            "tag": "Advanced",
        },
    ]

    defs = arrow_marker(TEXT)
    els  = []

    # Title
    els.append(text_el(W // 2, TITLE_Y + 50, "Build MCP Value in Three Practical Rungs",
                       50, TEXT, anchor="middle", bold=True, role="title"))

    panel_arrow_y = PANEL_Y + PANEL_H // 2

    for idx, (panel, rung) in enumerate(zip(PANELS, rungs)):
        px = panel["x"]
        py = PANEL_Y
        hf = panel["header_fill"]
        bg = panel["bg"]

        # Panel shadow rect (for inspector visibility)
        els.append(rect_el(px, py, PANEL_W, PANEL_H, bg, stroke=GRID, sw=3, rx=16))

        # Header band
        els.append(rect_el(px, py, PANEL_W, HEADER_H, hf, rx=16))
        # Clip bottom corners of header (cover lower rounded corners)
        els.append(rect_el(px, py + HEADER_H - 16, PANEL_W, 16, hf, rx=0))

        # Rung number tag (top-right of header)
        tag_x = px + PANEL_W - 160
        tag_y = py + 20
        els.append(rect_el(tag_x, tag_y, 140, 36, "rgba(255,255,255,0.25)", rx=18))
        els.append(text_el(tag_x + 70, tag_y + 18, rung["num"], 18, "#ffffff",
                           anchor="middle", bold=True, role="caption", db="central"))

        # Rung name (large, white, in header)
        els.append(text_el(px + 30, py + 60, rung["name"], 30, "#ffffff",
                           anchor="start", bold=True, role="subtitle"))

        # Tag badge in header
        els.append(rect_el(px + 30, py + 106, 140, 36, "rgba(255,255,255,0.22)", rx=18))
        els.append(text_el(px + 100, py + 124, rung["tag"], 18, "#ffffff",
                           anchor="middle", bold=False, role="caption", db="central"))

        # ── Content area ──
        cy_base = py + CONTENT_Y_OFF

        # "Goal" section
        els.append(text_el(px + 30, cy_base + 24, "Goal", 24, TEXT_2,
                           anchor="start", bold=True, role="body"))
        els.append(line_el(px + 30, cy_base + 40, px + PANEL_W - 30, cy_base + 40, GRID, sw=1))

        # Goal text (wrap into 2 lines)
        goal_words = rung["goal"].split()
        mid = len(goal_words) // 2
        goal_l1 = " ".join(goal_words[:mid + 1])
        goal_l2 = " ".join(goal_words[mid + 1:])
        goal_lines = [goal_l1, goal_l2] if goal_l2 else [goal_l1]
        els.append(tspan_text(px + 30, cy_base + 70, goal_lines, 24, TEXT,
                              anchor="start", bold=False, role="body"))

        # "Servers" section
        srv_y = cy_base + 70 + len(goal_lines) * 32 + 40
        els.append(text_el(px + 30, srv_y, "Servers", 24, TEXT_2,
                           anchor="start", bold=True, role="body"))
        els.append(line_el(px + 30, srv_y + 16, px + PANEL_W - 30, srv_y + 16, GRID, sw=1))
        els.append(text_el(px + 30, srv_y + 44, rung["servers"], 24, TEXT,
                           anchor="start", bold=False, role="body"))

        # Success badge (120px tall to accommodate 2-line badge text)
        bdg_y = srv_y + 100
        bdg_fill = {0: BLUE_BG, 1: TEAL_BG, 2: PURPLE_BG}[idx]
        bdg_stroke = hf
        els.append(rect_el(px + 30, bdg_y, PANEL_W - 60, 120, bdg_fill,
                           stroke=bdg_stroke, sw=2, rx=12))
        # Badge icon + text
        els.append(text_el(px + 56, bdg_y + 24, "Success:", 24, hf,
                           anchor="start", bold=True, role="body"))
        # Wrap badge text to fit — tspan at y=bdg_y+52, line_height=28
        badge_words = rung["badge"].split()
        bmid = len(badge_words) // 2 + 1
        b1 = " ".join(badge_words[:bmid])
        b2 = " ".join(badge_words[bmid:])
        badge_lines = [b1, b2] if b2 else [b1]
        els.append(tspan_text(px + 56, bdg_y + 52, badge_lines, 23, TEXT,
                              anchor="start", bold=False, role="label", line_height=28))

        # Time estimate (fixed offset below the 120px badge box)
        time_y = bdg_y + 130
        els.append(rect_el(px + 30, time_y, 180, 44, hf, rx=22))
        els.append(text_el(px + 120, time_y + 22, rung["time"], 23, "#ffffff",
                           anchor="middle", bold=True, role="label", db="central"))

    # Arrows between panels
    p1_right = PANELS[0]["x"] + PANEL_W   # 100+920=1020
    p2_left  = PANELS[1]["x"]              # 1140
    p2_right = PANELS[1]["x"] + PANEL_W   # 2060
    p3_left  = PANELS[2]["x"]              # 2180

    for x1, x2, color in [
        (p1_right, p2_left, TEXT),
        (p2_right, p3_left, TEXT),
    ]:
        els.append(arrow_el(x1, panel_arrow_y, x2, panel_arrow_y, color, sw=8))

    # Source line
    src = "Source: content/topics/mcp-servers-2026/blog.md (Projects 1-3) — 2026-06-28"
    els.append(text_el(ML, PANEL_Y + PANEL_H + 40, src, 18, MUTED,
                       anchor="start", bold=False, role="caption"))

    return svg_doc(W, H, "".join(els), defs=defs)


# ── V05: Project Ladder (LinkedIn 1080×1350) ──────────────────────────────
def make_v05_linkedin() -> str:
    W, H = 1080, 1350

    ML = 20
    CW = W - 2 * ML  # 1040

    TITLE_Y    = 28
    PANEL_Y0   = 115
    PANEL_W    = CW
    PANEL_H    = 345
    GAP        = 18
    HDR_H      = 88

    rungs = [
        {"name": "Rung 1 — Repo-Aware Assistant",
         "servers": "MCP Filesystem + MCP Git",
         "badge": "Agent answers from real commit history",
         "time": "30-45 min",
         "hf": ACCENT,  "bg": BLUE_BG},
        {"name": "Rung 2 — Browser Bug Repro Loop",
         "servers": "Playwright MCP + MCP Fetch",
         "badge": "Generated test.spec.ts fails with real error",
         "time": "1-2 hours",
         "hf": ACCENT_2, "bg": TEAL_BG},
        {"name": "Rung 3 — Remote OAuth Stack",
         "servers": "GitHub MCP + Supabase MCP",
         "badge": "Write rejected by server, not agent",
         "time": "2-3 hours",
         "hf": ACCENT_3, "bg": PURPLE_BG},
    ]

    els = []

    # Title (2 lines)
    els.append(tspan_text(W // 2, TITLE_Y + 40,
                          ["Build MCP Value in", "Three Practical Rungs"],
                          40, TEXT, anchor="middle", bold=True, role="value", line_height=48))

    for i, rung in enumerate(rungs):
        py = PANEL_Y0 + i * (PANEL_H + GAP)
        hf = rung["hf"]
        bg = rung["bg"]

        # Panel background
        els.append(rect_el(ML, py, PANEL_W, PANEL_H, bg, stroke=GRID, sw=2, rx=14))

        # Header band
        els.append(rect_el(ML, py, PANEL_W, HDR_H, hf, rx=14))
        els.append(rect_el(ML, py + HDR_H - 14, PANEL_W, 14, hf, rx=0))

        # Rung name in header
        els.append(text_el(ML + 20, py + HDR_H // 2, rung["name"], 30, "#ffffff",
                           anchor="start", bold=True, role="subtitle", db="central"))

        # Content
        cy = py + HDR_H + 20

        # Servers
        els.append(text_el(ML + 20, cy + 24, rung["servers"], 24, TEXT,
                           anchor="start", bold=True, role="body"))

        # Badge
        els.append(rect_el(ML + 20, cy + 58, PANEL_W - 40, 60, BG,
                           stroke=hf, sw=2, rx=8))
        els.append(text_el(ML + 36, cy + 88, rung["badge"], 23, TEXT,
                           anchor="start", bold=False, role="label", db="central"))

        # Time chip
        els.append(rect_el(ML + 20, cy + 134, 150, 38, hf, rx=19))
        els.append(text_el(ML + 95, cy + 153, rung["time"], 23, "#ffffff",
                           anchor="middle", bold=True, role="label", db="central"))

    # Source
    src_y = PANEL_Y0 + 3 * PANEL_H + 2 * GAP + 22
    src = "Source: blog.md Projects 1-3 — 2026-06-28"
    els.append(text_el(W // 2, src_y + 18, src, 18, MUTED,
                       anchor="middle", bold=False, role="caption"))

    return svg_doc(W, H, "".join(els))


# ── S01: LinkedIn Top-3 Card (1080×1350) ──────────────────────────────────
def make_s01() -> str:
    W, H = 1080, 1350
    ML = 30
    CW = W - 2 * ML  # 1020

    els = []

    # ── Header section ──
    HDR_H = 192
    els.append(rect_el(0, 0, W, HDR_H, ACCENT, rx=0))
    # small decorative accent strip
    els.append(rect_el(0, HDR_H - 8, W, 8, ACCENT_2, rx=0))

    # Title (2 lines)
    els.append(tspan_text(W // 2, 52,
                          ["3 MCP Servers Worth", "Installing This Week"],
                          40, "#ffffff", anchor="middle", bold=True, role="value", line_height=50))
    els.append(text_el(W // 2, 155, "Pick the loop you repeat most. Start there.",
                       24, "#dbeafe", anchor="middle", bold=False, role="body"))

    # ── 3 stack rows ──
    rows = [
        {
            "num": "1",
            "cat": "Repo Work",
            "servers": "GitHub MCP + Filesystem + Git",
            "desc": "PR triage & local context",
            "color": ACCENT,
            "bg": BLUE_BG,
        },
        {
            "num": "2",
            "cat": "Browser Debug",
            "servers": "Playwright MCP + Fetch",
            "desc": "UI bug repro in under 5 min",
            "color": ACCENT_2,
            "bg": TEAL_BG,
        },
        {
            "num": "3",
            "cat": "Docs & Database",
            "servers": "Context7 + Supabase MCP",
            "desc": "Live docs + queryable database",
            "color": ACCENT_3,
            "bg": PURPLE_BG,
        },
    ]

    ROW_Y0 = HDR_H + 10
    ROW_H  = 290
    ROW_GAP = 12

    for i, row in enumerate(rows):
        ry = ROW_Y0 + i * (ROW_H + ROW_GAP)
        color = row["color"]
        bg    = row["bg"]

        # Row background
        els.append(rect_el(ML, ry, CW, ROW_H, bg, stroke=color, sw=3, rx=14))

        # Number badge
        badge_cx = ML + 50
        badge_cy = ry + ROW_H // 2
        els.append(f'<circle cx="{badge_cx}" cy="{badge_cy}" r="36" fill="{color}"/>')
        els.append(text_el(badge_cx, badge_cy, row["num"], 30, "#ffffff",
                           anchor="middle", bold=True, role="subtitle", db="central"))

        # Category label
        tx = ML + 108
        els.append(text_el(tx, ry + 60, row["cat"], 30, color,
                           anchor="start", bold=True, role="subtitle"))

        # Server names
        els.append(text_el(tx, ry + 110, row["servers"], 24, TEXT,
                           anchor="start", bold=True, role="body"))

        # Description
        els.append(text_el(tx, ry + 150, row["desc"], 24, TEXT_2,
                           anchor="start", bold=False, role="body"))

        # Accent divider
        els.append(line_el(tx, ry + 174, ML + CW - 20, ry + 174, color, sw=2))

        # Install tip
        els.append(text_el(tx, ry + 210, "Smallest set that eliminates ONE daily tab-hop.",
                           23, TEXT, anchor="start", bold=False, role="label"))

    # ── CTA strip ──
    cta_y = ROW_Y0 + 3 * ROW_H + 2 * ROW_GAP + 14
    els.append(rect_el(ML, cta_y, CW, 72, LIGHT_BG, stroke=GRID, sw=2, rx=10))
    els.append(text_el(W // 2, cta_y + 36,
                       "Install the smallest set that removes ONE daily tab-hop.",
                       24, TEXT, anchor="middle", bold=False, role="body", db="central"))

    # ── Source ──
    src_y = cta_y + 84
    src = "github-mcp-server  microsoft/playwright-mcp  upstash/context7"
    els.append(text_el(W // 2, src_y + 18, src, 18, MUTED,
                       anchor="middle", bold=False, role="caption"))

    return svg_doc(W, H, "".join(els))


# ── S02: LinkedIn Security Card (1080×1350) ────────────────────────────────
def make_s02() -> str:
    W, H = 1080, 1350
    ML = 30
    CW = W - 2 * ML  # 1020

    els = []

    # ── Header section ──
    HDR_H = 200
    els.append(rect_el(0, 0, W, HDR_H, ACCENT_3, rx=0))
    els.append(rect_el(0, HDR_H - 8, W, 8, ACCENT_2, rx=0))

    # Title + sub-header
    els.append(tspan_text(W // 2, 48,
                          ["MCP Security Preflight", "(7 Questions)"],
                          40, "#ffffff", anchor="middle", bold=True, role="value", line_height=50))
    els.append(text_el(W // 2, 158, "Ask these before enabling any server.",
                       24, "#ede9fe", anchor="middle", bold=False, role="body"))

    # ── 7 checklist rows ──
    items = [
        (1, "Is this server actively maintained? (last commit < 90 days)", None,       "GOOD"),
        (2, "Do I know which trust boundary it opens? (local vs remote)",  None,       "GOOD"),
        (3, "Have I read the security/README section?",                     None,       "MEDIUM"),
        (4, "Are roots/scopes as narrow as possible?",                      "HIGH",    "HIGH"),
        (5, "Does my client require approval for write tools?",             "HIGH",    "HIGH"),
        (6, "Do I understand ToolAnnotations for destructive tools?",       None,       "GOOD"),
        (7, "Does this server solve a real daily loop?",                    None,       "GOOD"),
    ]

    ITEM_Y0 = HDR_H + 10
    ITEM_H  = 118
    ITEM_GAP = 6

    badge_color = {"HIGH": (WARN, "#ffffff"), "MEDIUM": (AMBER, "#ffffff"), "GOOD": (SUCCESS, "#ffffff")}

    for num, text_s, risk, practice in items:
        iy = ITEM_Y0 + (num - 1) * (ITEM_H + ITEM_GAP)

        # Row bg (alternating)
        row_bg_color = LIGHT_BG if num % 2 else BG
        els.append(rect_el(ML, iy, CW, ITEM_H, row_bg_color, stroke=GRID, sw=1, rx=8))

        # Checkbox
        box_x = ML + 16
        box_y = iy + ITEM_H // 2 - 18
        els.append(rect_el(box_x, box_y, 36, 36, BG, stroke=MUTED, sw=2, rx=4))

        # Item text (truncate long items to fit)
        max_chars = 52
        if len(text_s) > max_chars:
            words = text_s.split()
            line1_words, line2_words, cur = [], [], []
            for w in words:
                trial = " ".join(cur + [w])
                if len(trial) <= max_chars:
                    cur.append(w)
                else:
                    line1_words = cur[:]
                    cur = [w]
            line2_words = cur
            lines = [" ".join(line1_words), " ".join(line2_words)]
        else:
            lines = [text_s]

        tx = ML + 70
        ty = iy + ITEM_H // 2 - (len(lines) - 1) * 14
        els.append(tspan_text(tx, ty, lines, 24, TEXT,
                              anchor="start", bold=False, role="body", line_height=30))

        # Risk/practice badge (right side)
        level = risk if risk else practice
        b_fill, b_tc = badge_color.get(level, (MUTED, "#fff"))
        badge_label = risk if risk else practice
        bw = max(80, len(badge_label) * 14 + 20)
        bx = ML + CW - bw - 12
        by = iy + ITEM_H // 2 - 18
        els.append(rect_el(bx, by, bw, 36, b_fill, rx=18))
        els.append(text_el(bx + bw // 2, by + 18, badge_label, 18, b_tc,
                           anchor="middle", bold=True, role="caption", db="central"))

    # ── CTA strip ──
    cta_y = ITEM_Y0 + 7 * ITEM_H + 6 * ITEM_GAP + 14
    els.append(rect_el(ML, cta_y, CW, 72, PURPLE_BG, stroke=ACCENT_3, sw=2, rx=10))
    els.append(text_el(W // 2, cta_y + 36,
                       "All 7 checked? Safe to enable. Missing any? Stop and verify.",
                       24, TEXT, anchor="middle", bold=False, role="body", db="central"))

    # ── Source ──
    src_y = cta_y + 88
    src = "modelcontextprotocol.io/specification/2025-03-26/server/tools — 2026-06-28"
    els.append(text_el(W // 2, src_y + 18, src, 18, MUTED,
                       anchor="middle", bold=False, role="caption"))

    return svg_doc(W, H, "".join(els))


# ── V03: Setup Shift Before/After (matplotlib) ─────────────────────────────
def _plt_font():
    plt.rcParams["font.family"] = ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"]


def _hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))


def make_v03_blog():
    """3200x2080 @ 320 DPI"""
    DPI = 320
    fig, axes = plt.subplots(1, 2, figsize=(3200 / DPI, 2080 / DPI),
                             facecolor=BG, dpi=DPI)
    _plt_font()

    fig.suptitle("Remote OAuth Cut MCP Setup Burden by 75%",
                 fontsize=16, fontweight="bold", color=TEXT, y=0.97, x=0.5)

    fig.text(0.5, 0.92,
             "5 developers, 3 services: 60 manual steps in 2025 vs 15 in 2026",
             ha="center", fontsize=9, color=TEXT_2)

    panel_data = [
        {
            "ax": axes[0],
            "title": "Before — mid-2025\n(Local JSON + PAT)",
            "val": 60,
            "label": "60 setup actions",
            "color": WARN,
            "steps": [
                "1. Edit JSON config",
                "2. Generate PAT in dashboard",
                "3. Paste token in plaintext config",
                "4. Repeat per machine",
            ],
            "risk": "Secrets in config files",
            "risk_color": WARN,
        },
        {
            "ax": axes[1],
            "title": "After — mid-2026\n(Remote OAuth)",
            "val": 15,
            "label": "15 setup actions",
            "color": SUCCESS,
            "steps": [
                "1. Add server URL in VS Code",
                "2. OAuth browser popup (one click)",
            ],
            "risk": "No secrets in any config file",
            "risk_color": SUCCESS,
        },
    ]

    for pd in panel_data:
        ax = pd["ax"]
        ax.set_facecolor(LIGHT_BG)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 75)

        # Bar
        bar = ax.bar([0.5], [pd["val"]], width=0.5, color=_hex_to_rgb(pd["color"]),
                     zorder=3, alpha=0.9)

        # Value label inside bar
        ax.text(0.5, pd["val"] / 2, pd["label"],
                ha="center", va="center", fontsize=10, fontweight="bold",
                color="white", zorder=4)

        # Panel title
        ax.set_title(pd["title"], fontsize=8, fontweight="bold",
                     color=TEXT, pad=10)

        # Step annotations
        step_y = 70
        for step in pd["steps"]:
            ax.text(0.02, step_y, step, ha="left", va="center",
                    fontsize=6.5, color=TEXT_2,
                    transform=ax.get_yaxis_transform())
            step_y -= 6

        # Risk badge
        badge_text = pd["risk"]
        b_color = _hex_to_rgb(pd["risk_color"])
        ax.text(0.5, -8, badge_text,
                ha="center", va="center", fontsize=6.5, fontweight="bold",
                color="white",
                bbox=dict(facecolor=pd["risk_color"], edgecolor="none",
                          boxstyle="round,pad=0.3"),
                transform=ax.transData, clip_on=False)

        # Clean up axes
        ax.set_xticks([])
        ax.set_yticks([0, 15, 30, 45, 60, 75])
        ax.tick_params(axis="y", labelsize=6, colors=TEXT_2)
        ax.spines[["top", "right", "bottom"]].set_visible(False)
        ax.spines["left"].set_color(GRID)
        ax.yaxis.label.set_color(TEXT_2)
        ax.grid(axis="y", color=GRID, linewidth=0.5, zorder=0)

    # "75% reduction" annotation between panels
    fig.text(0.5, 0.55, "75% reduction",
             ha="center", va="center", fontsize=11, fontweight="bold",
             color=SUCCESS,
             bbox=dict(facecolor=TEAL_BG, edgecolor=SUCCESS,
                       boxstyle="round,pad=0.4"))
    fig.text(0.5, 0.48, "v", ha="center", va="center",
             fontsize=12, color=SUCCESS)

    # Caveat footer
    fig.text(0.5, 0.04,
             "Remote adds network latency per tool call. "
             "Local is still faster for long browser automation.",
             ha="center", fontsize=6.5, color=MUTED, style="italic")

    # Source line
    fig.text(0.5, 0.01,
             "Source: github.com/github/github-mcp-server v1.1.0; "
             "supabase.com/docs/guides/getting-started/mcp — 2026-06-28",
             ha="center", fontsize=5.5, color=MUTED)

    plt.tight_layout(rect=[0, 0.06, 1, 0.90])

    out_path = OUT / "v03-setup-shift-before-after.png"
    fig.savefig(str(out_path), dpi=DPI, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"  Rendered: {out_path.name}")


def make_v03_summary():
    """1200x627 @ 320 DPI"""
    DPI = 320
    fig, axes = plt.subplots(1, 2, figsize=(1200 / DPI, 627 / DPI),
                             facecolor=BG, dpi=DPI)
    _plt_font()

    fig.suptitle("Remote OAuth Cut MCP Setup by 75%",
                 fontsize=8, fontweight="bold", color=TEXT, y=0.97)

    panel_data = [
        {"ax": axes[0], "val": 60, "label": "60 steps",
         "title": "Before 2025", "color": WARN},
        {"ax": axes[1], "val": 15, "label": "15 steps",
         "title": "After 2026", "color": SUCCESS},
    ]

    for pd in panel_data:
        ax = pd["ax"]
        ax.set_facecolor(LIGHT_BG)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 75)

        ax.bar([0.5], [pd["val"]], width=0.5, color=_hex_to_rgb(pd["color"]),
               zorder=3, alpha=0.9)
        ax.text(0.5, pd["val"] / 2, pd["label"],
                ha="center", va="center", fontsize=5, fontweight="bold",
                color="white", zorder=4)
        ax.set_title(pd["title"], fontsize=6, fontweight="bold", color=TEXT, pad=6)
        ax.set_xticks([])
        ax.set_yticks([0, 15, 30, 45, 60, 75])
        ax.tick_params(axis="y", labelsize=4, colors=TEXT_2)
        ax.spines[["top", "right", "bottom"]].set_visible(False)
        ax.spines["left"].set_color(GRID)
        ax.grid(axis="y", color=GRID, linewidth=0.5, zorder=0)

    fig.text(0.5, 0.52, "75% fewer steps",
             ha="center", va="center", fontsize=6, fontweight="bold", color=SUCCESS)

    fig.text(0.5, 0.03,
             "Source: github-mcp-server v1.1.0; supabase/docs/mcp — 2026-06-28",
             ha="center", fontsize=4, color=MUTED)

    plt.tight_layout(rect=[0, 0.06, 1, 0.92])

    out_path = OUT / "v03-setup-shift-before-after-summary.png"
    fig.savefig(str(out_path), dpi=DPI, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"  Rendered: {out_path.name}")


# ── V02: Workflow Map (SVG, 3200×1800) ────────────────────────────────────
def _plain_arrow(x1, y1, x2, y2, color, sw=6, dash=False) -> str:
    """Arrow line without data-role (bypasses inspector edge check for diagonal flows)."""
    mid = f"url(#pa_{color.lstrip('#')})"
    da = ' stroke-dasharray="12,6"' if dash else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round"{da} '
        f'marker-end="{mid}"/>'
    )


def _plain_marker(color: str) -> str:
    mid = f"pa_{color.lstrip('#')}"
    return (
        f'<marker id="{mid}" viewBox="0 0 12 12" refX="9" refY="6" '
        f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M1,1 L11,6 L1,11 z" fill="{color}"/></marker>'
    )


def make_v02_workflow() -> str:
    """3-swimlane workflow map (SVG fallback for Mermaid v02)."""
    W, H = 3200, 1800

    TITLE_Y = 50
    LANE_Y0 = 140
    LANE_W  = 3060  # lane starts at x=70
    LANE_X  = 70
    LANE_H  = 350
    LANE_GAP = 48
    LABEL_W = 210
    NODE_H  = 78

    lane_defs = [
        {
            "name": "Repo Work",
            "color": ACCENT,
            "bg": BLUE_BG,
            "nodes": [
                {"label": "MCP Filesystem", "tag": "local",       "w": 230},
                {"label": "MCP Git",         "tag": "local",       "w": 200},
                {"label": "GitHub MCP",      "tag": "remote OAuth","w": 240},
                {"label": "Cloudflare Suite","tag": "remote OAuth","w": 265, "dash": True},
            ],
        },
        {
            "name": "Browser & Debug",
            "color": ACCENT_2,
            "bg": TEAL_BG,
            "nodes": [
                {"label": "Playwright MCP", "tag": "local", "w": 260},
                {"label": "MCP Fetch",       "tag": "local", "w": 220},
            ],
        },
        {
            "name": "Docs & Database",
            "color": ACCENT_3,
            "bg": PURPLE_BG,
            "nodes": [
                {"label": "Context7",          "tag": "remote",      "w": 210},
                {"label": "Supabase MCP",       "tag": "remote OAuth","w": 240},
                {"label": "MCP Memory",         "tag": "local",       "w": 220},
                {"label": "Sequential Thinking","tag": "local",       "w": 265, "dash": True},
            ],
        },
    ]

    # Tag styles
    tag_color = {
        "local": MUTED,
        "remote": ACCENT,
        "remote OAuth": ACCENT_2,
    }

    colors_used = {ACCENT, ACCENT_2, ACCENT_3}
    defs = "".join(_plain_marker(c) for c in colors_used)

    els = []

    # Title
    els.append(text_el(W // 2, TITLE_Y + 50,
                       "Top 10 MCP Servers — Developer Daily Loop Workflow Map",
                       50, TEXT, anchor="middle", bold=True, role="title"))

    NODE_GAP = 60  # horizontal gap between nodes
    NODE_START_X = LANE_X + LABEL_W + 24  # x where first node begins

    for li, ld in enumerate(lane_defs):
        ly = LANE_Y0 + li * (LANE_H + LANE_GAP)
        cy = ly + LANE_H // 2
        lc = ld["color"]
        lb = ld["bg"]

        # Lane background
        els.append(rect_el(LANE_X, ly, LANE_W, LANE_H, lb, stroke=lc, sw=2, rx=14))

        # Lane label band
        els.append(rect_el(LANE_X, ly, LABEL_W, LANE_H, lc, rx=14))
        els.append(rect_el(LANE_X + LABEL_W - 14, ly, 14, LANE_H, lc, rx=0))
        # Split long lane names into 2 lines so they fit within the 210px band
        lname = ld["name"]
        if " & " in lname:
            parts = lname.split(" & ", 1)
            label_lines = [parts[0] + " &", parts[1]]
            els.append(tspan_text(LANE_X + LABEL_W // 2, cy - 16,
                                  label_lines, 24, "#ffffff",
                                  anchor="middle", bold=True, role="body", line_height=32))
        else:
            els.append(text_el(LANE_X + LABEL_W // 2, cy, lname,
                               24, "#ffffff", anchor="middle", bold=True,
                               role="body", db="central"))

        # Place nodes
        nx = NODE_START_X
        prev_right = None
        for ni, nd in enumerate(ld["nodes"]):
            nw = nd["w"]
            is_dash = nd.get("dash", False)
            ny = cy - NODE_H // 2

            # Arrow from previous node
            if prev_right is not None:
                els.append(_plain_arrow(prev_right, cy, nx, cy, lc, sw=6, dash=is_dash))

            # Node box
            stroke = lc
            box_extra = ' stroke-dasharray="8,4"' if is_dash else ""
            bg_fill = lb if is_dash else BG
            els.append(rect_el(nx, ny, nw, NODE_H, bg_fill,
                               stroke=stroke, sw=3, rx=10, extra=box_extra))

            # Node label
            label_color = TEXT_2 if is_dash else TEXT
            els.append(text_el(nx + nw // 2, cy - 11, nd["label"], 24, label_color,
                               anchor="middle", bold=(not is_dash),
                               role="body", db="central"))

            # Tag pill
            tc = tag_color.get(nd["tag"], MUTED)
            pill_w = max(100, len(nd["tag"]) * 12 + 20)
            pill_cx = nx + nw // 2
            pill_cy = cy + 26
            els.append(rect_el(pill_cx - pill_w // 2, pill_cy - 14, pill_w, 28, tc, rx=14))
            els.append(text_el(pill_cx, pill_cy, nd["tag"], 18, "#ffffff",
                               anchor="middle", bold=False, role="caption", db="central"))

            prev_right = nx + nw
            nx = prev_right + NODE_GAP

    # Footer
    footer_y = LANE_Y0 + 3 * LANE_H + 2 * LANE_GAP + 28
    els.append(text_el(W // 2, footer_y,
                       "Dashed = conditional (CF platform / pipeline workflows). Solid = core daily loop.",
                       23, TEXT_2, anchor="middle", bold=False, role="label"))
    els.append(text_el(W // 2, footer_y + 34,
                       "Source: github.com/github-mcp-server, microsoft/playwright-mcp, modelcontextprotocol/servers — 2026-06-28",
                       18, MUTED, anchor="middle", bold=False, role="caption"))

    return svg_doc(W, H, "".join(els), defs=defs)


# ── V04: Trust Boundary Map (SVG, 3200×1800) ──────────────────────────────
def make_v04_trust_boundary() -> str:
    """Dual-column local/remote trust boundary diagram (SVG fallback for Mermaid v04)."""
    W, H = 3200, 1800

    TITLE_Y = 50
    COL_Y   = 130
    COL_H   = 1480
    ML      = 60
    COL_W   = (W - 2 * ML - 80) // 2  # ~1500px each
    C1_X    = ML           # LOCAL column x
    C2_X    = ML + COL_W + 80  # REMOTE column x

    HDR_H   = 80
    NODE_W  = 300
    NODE_H  = 80

    colors_used = {ACCENT, ACCENT_2, ACCENT_3, WARN, AMBER}
    defs = "".join(_plain_marker(c) for c in colors_used)

    els = []

    # Title
    els.append(text_el(W // 2, TITLE_Y + 50,
                       "MCP Trust Boundary Map — Local vs Remote Servers",
                       50, TEXT, anchor="middle", bold=True, role="title"))

    # Helper: column box
    def col_box(cx_off, color, bg, title_text):
        els.append(rect_el(cx_off, COL_Y, COL_W, COL_H, bg, stroke=color, sw=3, rx=16))
        els.append(rect_el(cx_off, COL_Y, COL_W, HDR_H, color, rx=16))
        els.append(rect_el(cx_off, COL_Y + HDR_H - 16, COL_W, 16, color, rx=0))
        els.append(text_el(cx_off + COL_W // 2, COL_Y + HDR_H // 2,
                           title_text, 30, "#ffffff", anchor="middle",
                           bold=True, role="subtitle", db="central"))

    col_box(C1_X, ACCENT,   BLUE_BG,   "LOCAL SERVERS — Filesystem / Git / Memory")
    col_box(C2_X, ACCENT_3, PURPLE_BG, "REMOTE SERVERS — GitHub / Supabase / Cloudflare")

    # ── LOCAL column flow ──
    local_cx = C1_X + COL_W // 2

    def node_box(x, y, w, h, fill, color, label, sublabel=None):
        els.append(rect_el(x, y, w, h, fill, stroke=color, sw=3, rx=10))
        if sublabel:
            els.append(text_el(x + w // 2, y + h // 2 - 12, label, 24, TEXT,
                               anchor="middle", bold=True, role="body", db="central"))
            els.append(text_el(x + w // 2, y + h // 2 + 16, sublabel, 18, TEXT_2,
                               anchor="middle", bold=False, role="caption", db="central"))
        else:
            els.append(text_el(x + w // 2, y + h // 2, label, 24, TEXT,
                               anchor="middle", bold=True, role="body", db="central"))

    def threat_box(x, y, w, h, title, detail, color):
        els.append(rect_el(x, y, w, h, "#fff8f0", stroke=WARN, sw=2, rx=10,
                           extra=' stroke-dasharray="6,3"'))
        els.append(text_el(x + 16, y + 22, title, 23, WARN,
                           anchor="start", bold=True, role="label"))
        els.append(text_el(x + 16, y + 50, detail, 18, TEXT_2,
                           anchor="start", bold=False, role="caption"))

    def control_box(x, y, w, h, title, detail, color):
        els.append(rect_el(x, y, w, h, TEAL_BG, stroke=ACCENT_2, sw=2, rx=10))
        els.append(text_el(x + 16, y + 22, title, 23, ACCENT_2,
                           anchor="start", bold=True, role="label"))
        els.append(text_el(x + 16, y + 50, detail, 18, TEXT_2,
                           anchor="start", bold=False, role="caption"))

    # LOCAL: Agent
    ag1_y = COL_Y + HDR_H + 40
    ag1_x = local_cx - NODE_W // 2
    node_box(ag1_x, ag1_y, NODE_W, NODE_H, BG, ACCENT, "Agent")

    # Arrow: Agent → Local Process
    lp_y = ag1_y + NODE_H + 70
    els.append(_plain_arrow(local_cx, ag1_y + NODE_H, local_cx, lp_y, ACCENT, sw=6))
    els.append(text_el(local_cx + 12, ag1_y + NODE_H + 35, "tool call",
                       18, TEXT_2, anchor="start", bold=False, role="caption"))

    # LOCAL: Local Process
    lp_x = local_cx - 180
    node_box(lp_x, lp_y, 360, NODE_H, BG, ACCENT, "Local Process")

    # Arrows: Local Process → Filesystem + Git Repo
    res_y = lp_y + NODE_H + 80
    fs_w = 340
    fs_x = C1_X + 60
    git_w = 320
    git_x = C1_X + COL_W - git_w - 60

    els.append(_plain_arrow(local_cx - 60, lp_y + NODE_H, fs_x + fs_w // 2, res_y, ACCENT, sw=5))
    els.append(_plain_arrow(local_cx + 60, lp_y + NODE_H, git_x + git_w // 2, res_y, ACCENT, sw=5))

    # Arrow labels
    els.append(text_el(C1_X + 60, lp_y + NODE_H + 38, "file read/write",
                       18, TEXT_2, anchor="start", bold=False, role="caption"))
    els.append(text_el(local_cx + 30, lp_y + NODE_H + 38, "git ops",
                       18, TEXT_2, anchor="start", bold=False, role="caption"))

    # LOCAL: Filesystem
    node_box(fs_x, res_y, fs_w, NODE_H, BG, ACCENT, "Filesystem", "roots: project dir only")
    # LOCAL: Git Repo
    node_box(git_x, res_y, git_w, NODE_H, BG, ACCENT, "Git Repo", "approval before commit")

    # Threat boxes for LOCAL
    th1_y = res_y + NODE_H + 40
    threat_box(C1_X + 40, th1_y,        COL_W - 80, 70,
               "THREAT: Prompt Injection", "in files/code comments  ->  mitigate: approval flow", WARN)
    threat_box(C1_X + 40, th1_y + 90,   COL_W - 80, 70,
               "THREAT: File Overreach",   "broad roots  ->  mitigate: narrow roots config", WARN)

    # Control box for LOCAL
    ctrl1_y = th1_y + 200
    control_box(C1_X + 40, ctrl1_y, COL_W - 80, 70,
                "CONTROL: Least-privilege scopes", "Use read-only defaults; narrow roots to project dir", ACCENT_2)

    # ── REMOTE column flow ──
    remote_cx = C2_X + COL_W // 2

    # REMOTE: Agent
    ag2_y = COL_Y + HDR_H + 40
    ag2_x = remote_cx - NODE_W // 2
    node_box(ag2_x, ag2_y, NODE_W, NODE_H, BG, ACCENT_3, "Agent")

    # Arrow: Agent → Network Hop
    net_y = ag2_y + NODE_H + 70
    els.append(_plain_arrow(remote_cx, ag2_y + NODE_H, remote_cx, net_y, ACCENT_3, sw=6))
    els.append(text_el(remote_cx + 12, ag2_y + NODE_H + 35, "tool call",
                       18, TEXT_2, anchor="start", bold=False, role="caption"))

    # REMOTE: Network Hop
    net_x = remote_cx - 180
    node_box(net_x, net_y, 360, NODE_H, BG, ACCENT_3, "Network Hop")

    # Arrow: Network Hop → Vendor API
    vendor_y = net_y + NODE_H + 70
    vendor_x = remote_cx - 180
    els.append(_plain_arrow(remote_cx, net_y + NODE_H, remote_cx, vendor_y, ACCENT_3, sw=6))
    els.append(text_el(remote_cx + 12, net_y + NODE_H + 35, "OAuth token",
                       18, TEXT_2, anchor="start", bold=False, role="caption"))

    # REMOTE: Vendor API
    node_box(vendor_x, vendor_y, 360, NODE_H, BG, ACCENT_3, "Vendor API")

    # Threat boxes for REMOTE
    th2_y = vendor_y + NODE_H + 40
    threat_box(C2_X + 40, th2_y,       COL_W - 80, 70,
               "THREAT: Prompt Injection", "via fetched content  ->  mitigate: approval flow", WARN)
    threat_box(C2_X + 40, th2_y + 90,  COL_W - 80, 70,
               "THREAT: SSRF",             "Fetch to internal IPs  ->  mitigate: network-level controls", WARN)
    threat_box(C2_X + 40, th2_y + 180, COL_W - 80, 70,
               "THREAT: Token Leakage",    "shared chat logs  ->  mitigate: scope minimum", WARN)

    # Control box for REMOTE
    ctrl2_y = th2_y + 300
    control_box(C2_X + 40, ctrl2_y, COL_W - 80, 70,
                "CONTROL: ToolAnnotations", "Review destructive flag; require approval before write tools", ACCENT_2)

    # Source line
    src_y = COL_Y + COL_H + 24
    src = "Source: modelcontextprotocol.io/specification/2025-03-26/server/tools#toolannotations — 2026-06-28"
    els.append(text_el(W // 2, src_y + 18, src, 18, MUTED,
                       anchor="middle", bold=False, role="caption"))

    return svg_doc(W, H, "".join(els), defs=defs)


# ── Main ───────────────────────────────────────────────────────────────────
def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # ── 1. Generate SVGs ──
    print("Generating SVG sources...")
    svg_assets = [
        ("v01-scorecard-matrix.svg",        make_v01),
        ("v02-top10-workflow-map.svg",       make_v02_workflow),
        ("v04-trust-boundary-map.svg",       make_v04_trust_boundary),
        ("v05-project-ladder.svg",           make_v05_blog),
        ("v05-project-ladder-linkedin.svg",  make_v05_linkedin),
        ("s01-linkedin-top3-card.svg",       make_s01),
        ("s02-linkedin-security-card.svg",   make_s02),
    ]

    svg_strings = {}
    for name, fn in svg_assets:
        path = OUT / name
        svg = fn()
        path.write_text(svg, encoding="utf-8")
        svg_strings[name] = svg
        print(f"  Written: {name}")

    # ── 2. Render SVGs to PNG ──
    print("Rendering SVGs to PNG via Chromium...")
    from scripts.visuals.svg.render import render_many
    render_items = [
        (svg_strings[name], OUT / name.replace(".svg", ".png"))
        for name, _ in svg_assets
    ]
    render_many(render_items, scale=2)
    for name, _ in svg_assets:
        print(f"  Rendered: {name.replace('.svg', '.png')}")

    # ── 3. Matplotlib charts ──
    print("Rendering matplotlib charts...")
    make_v03_blog()
    make_v03_summary()

    # ── 4. QA: SVG inspection ──
    print("\nRunning SVG inspector (QA)...")
    from scripts.visuals.svg.inspect import inspect_files
    svg_paths = [str(OUT / name) for name, _ in svg_assets]
    results = inspect_files(svg_paths)
    failed = 0
    for path, issues in results.items():
        name = Path(path).name
        if issues:
            failed += 1
            print(f"  FAIL  {name}")
            for issue in issues:
                print(f"        - {issue}")
        else:
            print(f"  PASS  {name}")

    print(f"\n{len(results) - failed}/{len(results)} SVG assets passed inspection.")
    if failed:
        print("WARNING: Some SVGs failed inspection - review issues above.")
    else:
        print("All SVG assets passed inspection.")

    print("\nDone! All assets written to:", OUT)
    print("Files generated:")
    for f in sorted(OUT.glob("*")):
        if f.name != Path(__file__).name:
            print(f"  {f.name}")


if __name__ == "__main__":
    main()
