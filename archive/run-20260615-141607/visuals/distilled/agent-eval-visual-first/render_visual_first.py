"""Render infographic-first assets for the AI Agent Evals series."""

from __future__ import annotations

import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.visuals.export import save_png
from scripts.visuals.panels import Box, rounded_panel
from scripts.visuals.text_layout import draw_wrapped_text, load_font
from scripts.visuals.tokens import PLATFORM_SIZES, get_tokens

OUT_DIR = Path(__file__).resolve().parent


def footer(draw: ImageDraw.ImageDraw, text: str, tokens: dict[str, str], width: int, height: int, x: int = 60) -> None:
    draw.text((x, height - 54), text, font=load_font(22), fill=tokens["TEXT_2"])


def title(draw: ImageDraw.ImageDraw, text: str, subtitle: str, tokens: dict[str, str], width: int, y: int = 70) -> int:
    y = draw_wrapped_text(draw, (70, y), text, load_font(58, bold=True), width - 140, tokens["TEXT"], line_gap=10)
    return draw_wrapped_text(draw, (70, y + 8), subtitle, load_font(28), width - 140, tokens["TEXT_2"], line_gap=8) + 12


def badge(draw: ImageDraw.ImageDraw, box: Box, text: str, fill: str, outline: str, text_color: str) -> None:
    rounded_panel(draw, box, fill=fill, outline=outline, radius=18, width=3)
    draw_wrapped_text(draw, (box.x + 18, box.y + 13), text, load_font(22, bold=True), box.width - 36, text_color, line_gap=4)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str, width: int = 6) -> None:
    draw.line((start, end), fill=color, width=width)
    sx, sy = start
    ex, ey = end
    angle = math.atan2(ey - sy, ex - sx)
    size = 18
    points = [
        (ex, ey),
        (ex - size * math.cos(angle - 0.45), ey - size * math.sin(angle - 0.45)),
        (ex - size * math.cos(angle + 0.45), ey - size * math.sin(angle + 0.45)),
    ]
    draw.polygon(points, fill=color)


def draw_gauge(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    radius: int,
    value: float,
    label: str,
    tokens: dict[str, str],
    color: str,
) -> None:
    cx, cy = center
    bbox = (cx - radius, cy - radius, cx + radius, cy + radius)
    draw.arc(bbox, 180, 360, fill=tokens["GRID"], width=24)
    draw.arc(bbox, 180, 180 + int(180 * value), fill=color, width=24)
    needle_angle = math.radians(180 + 180 * value)
    nx = cx + int((radius - 25) * math.cos(needle_angle))
    ny = cy + int((radius - 25) * math.sin(needle_angle))
    draw.line((cx, cy, nx, ny), fill=tokens["TEXT"], width=6)
    draw.ellipse((cx - 12, cy - 12, cx + 12, cy + 12), fill=tokens["TEXT"])
    draw.text((cx - radius + 15, cy + 18), label, font=load_font(25, bold=True), fill=tokens["TEXT"])


def draw_agent(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    tokens: dict[str, str],
    state: str,
    scale: int = 90,
) -> None:
    cx, cy = center
    color = {
        "neutral": tokens["ACCENT"],
        "wrong": tokens["WARN"],
        "correct": tokens["SUCCESS"],
        "blocked": tokens["ACCENT_3"],
    }[state]
    head_r = scale // 4
    head_top = cy - scale
    # body
    draw.rounded_rectangle((cx - scale // 2, cy - scale // 2, cx + scale // 2, cy + scale // 2), radius=18, fill=tokens["LIGHT_BG"], outline=color, width=5)
    # chest emblem changes per state so silhouette differs even at a glance
    if state == "correct":
        ex, ey = cx, cy - scale // 2 + 34
        draw.polygon([(ex, ey - 22), (ex + 22, ey - 12), (ex + 22, ey + 14), (ex, ey + 28), (ex - 22, ey + 14), (ex - 22, ey - 12)], fill=tokens["TEAL_BG"], outline=tokens["SUCCESS"])
        draw.line((ex - 11, ey, ex - 2, ey + 11), fill=tokens["SUCCESS"], width=5)
        draw.line((ex - 2, ey + 11, ex + 13, ey - 12), fill=tokens["SUCCESS"], width=5)
    elif state == "wrong":
        # chest left intentionally clean; the bread prop is drawn beside the agent
        pass
    # head
    draw.ellipse((cx - head_r, head_top, cx + head_r, head_top + 2 * head_r), fill=tokens["BG"], outline=color, width=5)
    # eyes
    eye_y = head_top + 25
    if state == "wrong":
        draw.line((cx - 12, eye_y - 4, cx - 4, eye_y + 4), fill=tokens["TEXT"], width=3)
        draw.line((cx - 4, eye_y - 4, cx - 12, eye_y + 4), fill=tokens["TEXT"], width=3)
        draw.line((cx + 4, eye_y - 4, cx + 12, eye_y + 4), fill=tokens["TEXT"], width=3)
        draw.line((cx + 12, eye_y - 4, cx + 4, eye_y + 4), fill=tokens["TEXT"], width=3)
    else:
        draw.ellipse((cx - 13, eye_y - 4, cx - 5, eye_y + 4), fill=tokens["TEXT"])
        draw.ellipse((cx + 5, eye_y - 4, cx + 13, eye_y + 4), fill=tokens["TEXT"])
    # mouth + accessories per state
    if state == "wrong":
        draw.arc((cx - 12, head_top + 44, cx + 12, head_top + 62), 0, 180, fill=tokens["WARN"], width=3)
        # chef hat
        band_y = head_top - 14
        draw.rectangle((cx - 22, band_y, cx + 22, band_y + 14), fill=tokens["BG"], outline=tokens["MUTED"], width=3)
        for dx in (-16, 0, 16):
            draw.ellipse((cx + dx - 16, band_y - 30, cx + dx + 16, band_y + 4), fill=tokens["BG"], outline=tokens["MUTED"], width=3)
        # sweat drop (filled teardrop)
        sx, sy = cx + head_r + 4, head_top + 18
        draw.ellipse((sx - 7, sy + 2, sx + 7, sy + 18), fill=tokens["ACCENT"])
        draw.polygon([(sx, sy - 10), (sx - 7, sy + 6), (sx + 7, sy + 6)], fill=tokens["ACCENT"])
    elif state == "correct":
        draw.arc((cx - 16, head_top + 38, cx + 16, head_top + 64), 0, 180, fill=tokens["SUCCESS"], width=5)
    elif state == "blocked":
        draw.line((cx - 14, head_top + 50, cx + 14, head_top + 50), fill=tokens["WARN"], width=4)
    else:
        draw.line((cx - 12, head_top + 50, cx + 12, head_top + 50), fill=tokens["TEXT"], width=3)


def draw_bread(draw: ImageDraw.ImageDraw, cx: int, cy: int, tokens: dict[str, str]) -> None:
    """Illustrative bread-loaf prop on a small plate (non-data colors are intentional for the comic)."""
    draw.ellipse((cx - 56, cy + 18, cx + 56, cy + 34), fill=tokens["GRID"], outline=tokens["MUTED"], width=2)
    draw.ellipse((cx - 46, cy - 22, cx + 46, cy + 22), fill="#e8b87a", outline="#a9743b", width=4)
    for dx in (-22, 0, 22):
        draw.line((cx + dx - 8, cy - 10, cx + dx + 8, cy + 10), fill="#a9743b", width=3)


def draw_stop_sign(draw: ImageDraw.ImageDraw, cx: int, cy: int, tokens: dict[str, str], r: int = 32) -> None:
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(22, 382, 45)]
    draw.polygon(pts, fill=tokens["WARN"], outline=tokens["BG"])
    sw, sh = draw.textbbox((0, 0), "STOP", font=load_font(15, bold=True))[2:]
    draw.text((cx - sw // 2, cy - sh // 2 - 2), "STOP", font=load_font(15, bold=True), fill=tokens["BG"])


def draw_tool_log(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str], empty: bool = True) -> None:
    rounded_panel(draw, box, fill=tokens["TEXT"], outline=tokens["TEXT"], radius=18, width=3)
    draw.text((box.x + 24, box.y + 20), "tool-call log", font=load_font(24, bold=True), fill=tokens["BG"])
    if empty:
        draw.text((box.x + 34, box.y + 72), "0", font=load_font(94, bold=True), fill=tokens["WARN"])
        draw_wrapped_text(draw, (box.x + 122, box.y + 88), "actions executed", load_font(27, bold=True), box.width - 150, tokens["BG"], line_gap=6)
    else:
        for i, text in enumerate(["create file", "validate schema", "run tests"]):
            draw.text((box.x + 34, box.y + 72 + i * 38), f"[x] {text}", font=load_font(24, bold=True), fill=tokens["SUCCESS"])


def draw_failure_grid(draw: ImageDraw.ImageDraw, x: int, y: int, tokens: dict[str, str], cell: int = 42) -> None:
    for i in range(8):
        col = i % 4
        row = i // 4
        fill = tokens["RED_BG"] if i in (1, 4, 6) else tokens["TEAL_BG"]
        outline = tokens["WARN"] if i in (1, 4, 6) else tokens["SUCCESS"]
        draw.rounded_rectangle((x + col * (cell + 10), y + row * (cell + 10), x + col * (cell + 10) + cell, y + row * (cell + 10) + cell), radius=8, fill=fill, outline=outline, width=3)
    draw.text((x, y + 2 * (cell + 10) + 8), "3 of 8 failed", font=load_font(25, bold=True), fill=tokens["WARN"])


def render_linkedin_card_pack() -> None:
    width, height = PLATFORM_SIZES["linkedin_card"]

    # Card 1: broken bridge / gap metaphor
    tokens = get_tokens("default")
    image = Image.new("RGB", (width, height), tokens["BG"])
    draw = ImageDraw.Draw(image)
    draw.text((70, 50), "01 / 05", font=load_font(28, bold=True), fill=tokens["ACCENT"])
    title(draw, "SWE-bench is not your production eval", "A high capability signal can still leave a behavior gap.", tokens, width, 112)
    draw.rounded_rectangle((80, 700, 455, 865), radius=24, fill=tokens["BLUE_BG"], outline=tokens["ACCENT"], width=5)
    draw.rounded_rectangle((625, 700, 1000, 865), radius=24, fill=tokens["RED_BG"], outline=tokens["WARN"], width=5)
    draw.text((112, 724), "74-78%", font=load_font(58, bold=True), fill=tokens["ACCENT"])
    draw.text((112, 792), "SWE-bench Verified", font=load_font(26, bold=True), fill=tokens["TEXT"])
    draw.text((657, 724), "35-50%", font=load_font(58, bold=True), fill=tokens["WARN"])
    draw.text((657, 792), "PR acceptance", font=load_font(26, bold=True), fill=tokens["TEXT"])
    draw.line((455, 775, 540, 735), fill=tokens["ACCENT"], width=16)
    draw.line((625, 775, 540, 815), fill=tokens["WARN"], width=16)
    draw.polygon([(520, 730), (560, 730), (540, 770)], fill=tokens["BG"], outline=tokens["TEXT"])
    badge(draw, Box(438, 895, 205, 78), "behavior gap", tokens["RED_BG"], tokens["WARN"], tokens["WARN"])
    draw_gauge(draw, (270, 545), 135, 0.78, "capability", tokens, tokens["ACCENT"])
    draw_gauge(draw, (810, 545), 135, 0.50, "acceptance", tokens, tokens["WARN"])
    footer(draw, "Sources: SWE-bench; Presenc May 2026 vendor snapshot", tokens, width, height)
    save_png(image, OUT_DIR / "linkedin-card-01-hook.png")

    # Card 2: annotated empty tool-log scene
    tokens = get_tokens("ocean")
    image = Image.new("RGB", (width, height), tokens["BG"])
    draw = ImageDraw.Draw(image)
    draw.text((70, 50), "02 / 05", font=load_font(28, bold=True), fill=tokens["ACCENT"])
    title(draw, "The failure looks successful", "The answer is polished. The trace tells the truth.", tokens, width, 112)
    response = Box(70, 350, 520, 350)
    rounded_panel(draw, response, tokens["LIGHT_BG"], tokens["ACCENT"], radius=26, width=5)
    draw.text((response.x + 28, response.y + 28), "agent response", font=load_font(28, bold=True), fill=tokens["ACCENT"])
    draw_wrapped_text(draw, (response.x + 28, response.y + 92), '"I created the file and validated the schema."', load_font(42, bold=True), response.width - 56, tokens["TEXT"], line_gap=10)
    log = Box(620, 365, 370, 320)
    draw_tool_log(draw, log, tokens, empty=True)
    arrow(draw, (590, 520), (620, 520), tokens["WARN"], 7)
    badge(draw, Box(330, 755, 420, 92), "Fabrication Without Action", tokens["RED_BG"], tokens["WARN"], tokens["WARN"])
    draw_wrapped_text(draw, (110, 910), "Production evals inspect behavior, not just final text.", load_font(42, bold=True), width - 220, tokens["TEXT"], line_gap=10)
    footer(draw, "Source: AI Agent Evals failure taxonomy", tokens, width, height)
    save_png(image, OUT_DIR / "linkedin-card-02-problem.png")

    # Card 3: radial taxonomy map
    tokens = get_tokens("midnight")
    image = Image.new("RGB", (width, height), tokens["BG"])
    draw = ImageDraw.Draw(image)
    draw.text((70, 50), "03 / 05", font=load_font(28, bold=True), fill=tokens["ACCENT"])
    title(draw, "What benchmarks miss", "Behavior failures cluster around contracts, not syntax.", tokens, width, 112)
    center = (width // 2, 630)
    nodes = [
        ("no tool", 0, tokens["WARN"]),
        ("wrong tool", 60, tokens["WARN"]),
        ("skipped gate", 120, tokens["WARN"]),
        ("persona drift", 180, tokens["ACCENT_3"]),
        ("lost handoff", 240, tokens["ACCENT"]),
        ("silent regress", 300, tokens["WARN"]),
    ]
    for text, deg, color in nodes:
        ang = math.radians(deg)
        nx = center[0] + int(330 * math.cos(ang))
        ny = center[1] + int(300 * math.sin(ang))
        draw.line((center[0], center[1], nx, ny), fill=tokens["GRID"], width=4)
        box = Box(nx - 115, ny - 44, 230, 88)
        rounded_panel(draw, box, tokens["LIGHT_BG"], color, radius=22, width=4)
        draw_wrapped_text(draw, (box.x + 18, box.y + 22), text, load_font(26, bold=True), box.width - 36, tokens["TEXT"], line_gap=4)
    draw.ellipse((center[0] - 150, center[1] - 150, center[0] + 150, center[1] + 150), fill=tokens["PURPLE_BG"], outline=tokens["ACCENT_3"], width=6)
    draw_wrapped_text(draw, (center[0] - 108, center[1] - 48), "looks successful", load_font(34, bold=True), 216, tokens["TEXT"], line_gap=6)
    footer(draw, "Source: AI Agent Evals behavior taxonomy", tokens, width, height)
    save_png(image, OUT_DIR / "linkedin-card-03-taxonomy.png")

    # Card 4: CI factory line
    tokens = get_tokens("forest")
    image = Image.new("RGB", (width, height), tokens["BG"])
    draw = ImageDraw.Draw(image)
    draw.text((70, 50), "04 / 05", font=load_font(28, bold=True), fill=tokens["ACCENT"])
    title(draw, "A production eval is a gate", "Tasks move through graders before release.", tokens, width, 112)
    y = 580
    stations = [
        ("task suite", "real workflows", tokens["ACCENT"]),
        ("graders", "text + tools + judge", tokens["ACCENT_2"]),
        ("CI gate", "pass or block", tokens["WARN"]),
        ("history", "drift over time", tokens["ACCENT_3"]),
    ]
    x_positions = [80, 330, 580, 830]
    for i, ((name, detail, color), x) in enumerate(zip(stations, x_positions)):
        box = Box(x, y, 190, 210)
        rounded_panel(draw, box, tokens["LIGHT_BG"], color, radius=24, width=5)
        draw.ellipse((x + 58, y + 28, x + 132, y + 102), fill=tokens["BG"], outline=color, width=5)
        draw.text((x + 83, y + 48), str(i + 1), font=load_font(32, bold=True), fill=color)
        draw_wrapped_text(draw, (x + 20, y + 120), name, load_font(28, bold=True), 150, tokens["TEXT"], line_gap=4)
        draw_wrapped_text(draw, (x + 20, y + 160), detail, load_font(21), 150, tokens["TEXT_2"], line_gap=4)
        if i < len(stations) - 1:
            arrow(draw, (x + 200, y + 105), (x + 245, y + 105), tokens["ACCENT"], 5)
    badge(draw, Box(598, 840, 155, 72), "fail -> fix", tokens["RED_BG"], tokens["WARN"], tokens["WARN"])
    draw.line((675, 840, 675, 790), fill=tokens["WARN"], width=4)
    draw_wrapped_text(draw, (105, 965), "Run it on PRs that change agents, prompts, tools, policies, or models.", load_font(36, bold=True), width - 210, tokens["TEXT"], line_gap=10)
    footer(draw, "Source: AI Agent Evals implementation pattern", tokens, width, height)
    save_png(image, OUT_DIR / "linkedin-card-04-framework.png")

    # Card 5: action worksheet
    tokens = get_tokens("sunset")
    image = Image.new("RGB", (width, height), tokens["BG"])
    draw = ImageDraw.Draw(image)
    draw.text((70, 50), "05 / 05", font=load_font(28, bold=True), fill=tokens["ACCENT"])
    title(draw, "Write the first eval", "Start with one risky agent and one behavior boundary.", tokens, width, 112)
    worksheet = Box(105, 350, 870, 555)
    rounded_panel(draw, worksheet, tokens["LIGHT_BG"], tokens["ACCENT"], radius=34, width=6)
    rows = [
        ("1", "Risky agent", "Which agent can cause real damage?"),
        ("2", "Must do", "What tool/action must happen?"),
        ("3", "Must refuse", "What behavior is outside scope?"),
    ]
    for i, (num, label, prompt) in enumerate(rows):
        yrow = worksheet.y + 48 + i * 155
        draw.ellipse((worksheet.x + 38, yrow, worksheet.x + 98, yrow + 60), fill=tokens["BG"], outline=tokens["ACCENT"], width=4)
        draw.text((worksheet.x + 59, yrow + 12), num, font=load_font(28, bold=True), fill=tokens["ACCENT"])
        draw_wrapped_text(draw, (worksheet.x + 128, yrow - 2), label, load_font(34, bold=True), 260, tokens["TEXT"])
        draw.line((worksheet.x + 420, yrow + 38, worksheet.x + 805, yrow + 38), fill=tokens["GRID"], width=5)
        draw_wrapped_text(draw, (worksheet.x + 128, yrow + 48), prompt, load_font(24), 690, tokens["TEXT_2"], line_gap=5)
    draw_wrapped_text(draw, (100, 960), "Question to ship with: what behavior must never regress?", load_font(40, bold=True), width - 200, tokens["WARN"], line_gap=10)
    footer(draw, "Source: AI Agent Evals visual-first guide", tokens, width, height)
    save_png(image, OUT_DIR / "linkedin-card-05-cta.png")


def render_comic_storyboard() -> None:
    tokens = get_tokens("ocean")
    width, height = PLATFORM_SIZES["linkedin_card"]
    image = Image.new("RGB", (width, height), tokens["BG"])
    draw = ImageDraw.Draw(image)
    title(draw, "The Sourdough Test", "One absurd prompt exposes persona drift.", tokens, width, 58)
    panels = [
        Box(70, 245, 440, 430),
        Box(570, 245, 440, 430),
        Box(70, 730, 440, 430),
        Box(570, 730, 440, 430),
    ]
    fills = [tokens["BLUE_BG"], tokens["RED_BG"], tokens["TEAL_BG"], tokens["PURPLE_BG"]]
    outlines = [tokens["ACCENT"], tokens["WARN"], tokens["SUCCESS"], tokens["ACCENT_3"]]
    panel_titles = ["1. Prompt", "2. Drift", "3. Redirect", "4. CI blocks"]
    bubbles = ['"How do I bake sourdough?"', "Use 75% hydration...", "I handle Azure deployments.", "persona drift blocked"]
    captions = [
        "Same off-topic prompt goes to every agent.",
        "Deployment agent becomes a recipe assistant.",
        "Expected behavior stays inside scope.",
        "CI blocks the release before users notice.",
    ]
    states = ["neutral", "wrong", "correct", "blocked"]
    for i, panel in enumerate(panels):
        rounded_panel(draw, panel, fills[i], outlines[i], radius=28, width=5)
        draw.text((panel.x + 24, panel.y + 22), panel_titles[i], font=load_font(28, bold=True), fill=outlines[i])
        bubble = Box(panel.x + 24, panel.y + 66, panel.width - 48, 86)
        rounded_panel(draw, bubble, tokens["BG"], outlines[i], radius=18, width=3)
        draw_wrapped_text(draw, (bubble.x + 18, bubble.y + 16), bubbles[i], load_font(24, bold=True), bubble.width - 36, tokens["TEXT"], line_gap=5)
        agent_x = panel.x + panel.width // 2
        if i == 3:
            agent_x = panel.x + 300
        draw_agent(draw, (agent_x, panel.y + 290), tokens, states[i], 112)
        if i == 1:
            draw_bread(draw, panel.x + 92, panel.y + 318, tokens)
            badge(draw, Box(panel.x + 250, panel.y + 250, 150, 60), "DRIFT", tokens["BG"], tokens["WARN"], tokens["WARN"])
        if i == 2:
            badge(draw, Box(panel.x + 250, panel.y + 250, 150, 60), "ON TASK", tokens["BG"], tokens["SUCCESS"], tokens["SUCCESS"])
        if i == 3:
            draw_stop_sign(draw, panel.x + 96, panel.y + 188, tokens, 34)
            draw_failure_grid(draw, panel.x + 54, panel.y + 232, tokens, 30)
        draw_wrapped_text(draw, (panel.x + 24, panel.y + panel.height - 74), captions[i], load_font(23, bold=True), panel.width - 48, tokens["TEXT"], line_gap=4)
    footer(draw, "Source: first-party AI Agent Evals implementation; 3 of 8 agents failed", tokens, width, height)
    save_png(image, OUT_DIR / "comic-sourdough-test.png")


def render_one_page_eval_system() -> None:
    tokens = get_tokens("forest")
    width, height = PLATFORM_SIZES["linkedin_card"]
    image = Image.new("RGB", (width, height), tokens["BG"])
    draw = ImageDraw.Draw(image)
    title(draw, "The 4-layer eval factory", "Behavior contracts gate releases.", tokens, width, 62)
    conveyor_y = 555
    draw.rounded_rectangle((95, conveyor_y + 90, 980, conveyor_y + 135), radius=20, fill=tokens["GRID"])
    stations = [
        ("Task suite", "38 tasks", tokens["ACCENT"], 120),
        ("Graders", "3 types", tokens["ACCENT_2"], 350),
        ("CI gate", "pass/block", tokens["WARN"], 580),
        ("History", "drift log", tokens["ACCENT_3"], 810),
    ]
    for idx, (name, detail, color, x) in enumerate(stations):
        station = Box(x, 405, 165, 285)
        rounded_panel(draw, station, tokens["LIGHT_BG"], color, radius=26, width=5)
        draw.ellipse((x + 43, 435, x + 122, 514), fill=tokens["BG"], outline=color, width=5)
        if idx == 0:
            draw.rectangle((x + 63, 459, x + 101, 491), fill=color)
        elif idx == 1:
            draw.arc((x + 55, 452, x + 110, 507), 20, 330, fill=color, width=6)
            draw.line((x + 100, 500, x + 121, 520), fill=color, width=5)
        elif idx == 2:
            draw.rectangle((x + 57, 455, x + 109, 505), outline=color, width=6)
            draw.line((x + 57, 480, x + 109, 480), fill=color, width=6)
        else:
            for j, h in enumerate([28, 48, 68]):
                draw.rectangle((x + 56 + j * 22, 505 - h, x + 70 + j * 22, 505), fill=color)
        draw_wrapped_text(draw, (x + 16, 535), name, load_font(28, bold=True), 133, tokens["TEXT"], line_gap=4)
        draw_wrapped_text(draw, (x + 16, 585), detail, load_font(24, bold=True), 133, color, line_gap=4)
        if idx < 3:
            arrow(draw, (x + 168, conveyor_y + 112), (x + 218, conveyor_y + 112), tokens["ACCENT"], 5)
    input_box = Box(130, 795, 280, 105)
    rounded_panel(draw, input_box, tokens["BLUE_BG"], tokens["ACCENT"], radius=22, width=4)
    draw_wrapped_text(draw, (input_box.x + 20, input_box.y + 20), "agent PR change enters", load_font(28, bold=True), input_box.width - 40, tokens["TEXT"], line_gap=5)
    fail_box = Box(465, 775, 195, 145)
    rounded_panel(draw, fail_box, tokens["RED_BG"], tokens["WARN"], radius=22, width=4)
    draw_wrapped_text(draw, (fail_box.x + 20, fail_box.y + 22), "fail -> debug trace", load_font(27, bold=True), fail_box.width - 40, tokens["WARN"], line_gap=5)
    pass_box = Box(725, 795, 220, 105)
    rounded_panel(draw, pass_box, tokens["TEAL_BG"], tokens["SUCCESS"], radius=22, width=4)
    draw_wrapped_text(draw, (pass_box.x + 20, pass_box.y + 20), "pass -> release confidence", load_font(27, bold=True), pass_box.width - 40, tokens["TEXT"], line_gap=5)
    draw.line((662, 842, 725, 842), fill=tokens["SUCCESS"], width=5)
    draw.line((580, 690, 562, 775), fill=tokens["WARN"], width=5)
    draw_wrapped_text(draw, (110, 1000), "Minimum viable system: real tasks, behavior graders, CI gate, regression history.", load_font(34, bold=True), width - 220, tokens["TEXT"], line_gap=9)
    footer(draw, "Source: original implementation: 8 agents, 38 tasks, 14 suites, 3 grader types", tokens, width, height)
    save_png(image, OUT_DIR / "one-page-eval-system.png")


def render_executive_exhibit() -> None:
    tokens = get_tokens("midnight")
    width, height = PLATFORM_SIZES["linkedin_exhibit"]
    image = Image.new("RGB", (width, height), tokens["BG"])
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, 92), fill=tokens["TEXT"])
    draw.text((52, 29), "EXHIBIT 1", font=load_font(22, bold=True), fill=tokens["BG"])
    draw_wrapped_text(draw, (52, 118), "Benchmark confidence can break before production acceptance", load_font(34, bold=True), width - 104, tokens["TEXT"], line_gap=8)
    left_center = (305, 375)
    right_center = (895, 375)
    draw_gauge(draw, left_center, 132, 0.78, "SWE-bench Verified", tokens, tokens["ACCENT"])
    draw_gauge(draw, right_center, 132, 0.50, "PR acceptance", tokens, tokens["WARN"])
    draw.text((left_center[0] - 88, 310), "74-78%", font=load_font(42, bold=True), fill=tokens["ACCENT"])
    draw.text((right_center[0] - 82, 310), "35-50%", font=load_font(42, bold=True), fill=tokens["WARN"])
    # Bridge-to-gap-to-bridge band: one bold center block avoids floating segments.
    gap_box = Box(468, 342, 264, 82)
    draw.line((438, 385, gap_box.x, 385), fill=tokens["ACCENT"], width=18)
    draw.line((gap_box.x + gap_box.width, 385, 762, 385), fill=tokens["WARN"], width=18)
    draw.line((gap_box.x, 360, gap_box.x, 410), fill=tokens["ACCENT"], width=6)
    draw.line((gap_box.x + gap_box.width, 360, gap_box.x + gap_box.width, 410), fill=tokens["WARN"], width=6)
    rounded_panel(draw, gap_box, fill=tokens["RED_BG"], outline=tokens["WARN"], radius=18, width=4)
    draw.text((gap_box.x + 25, gap_box.y + 24), "BEHAVIOR GAP", font=load_font(31, bold=True), fill=tokens["WARN"])
    draw_wrapped_text(draw, (70, 515), "Treat benchmark scores as capability signals. Production readiness needs behavior contracts.", load_font(23, bold=True), width - 140, tokens["TEXT"], line_gap=5)
    footer(draw, "Sources: SWE-bench; Presenc May 2026 vendor snapshot; AI Agent Evals series", tokens, width, height, 52)
    save_png(image, OUT_DIR / "exhibit-01-benchmark-gap.png")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    render_linkedin_card_pack()
    render_comic_storyboard()
    render_one_page_eval_system()
    render_executive_exhibit()
    print(f"Rendered infographic-first assets to {OUT_DIR}")


if __name__ == "__main__":
    main()
