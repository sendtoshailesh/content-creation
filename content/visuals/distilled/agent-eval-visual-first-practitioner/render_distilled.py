"""Render practitioner distilled assets for the AI Agent Evals visual guide."""

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
from scripts.visuals.text_layout import draw_wrapped_text, fit_font_size, load_font, text_size
from scripts.visuals.tokens import get_tokens

OUT_DIR = Path(__file__).resolve().parent
THEME_NAMES = ["default", "ocean", "sunset", "forest", "midnight"]


def theme(index: int) -> dict[str, str]:
    return get_tokens(THEME_NAMES[index % len(THEME_NAMES)])


def canvas(size: tuple[int, int], tokens: dict[str, str], dark: bool = False) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    bg = tokens["TEXT"] if dark else tokens["BG"]
    image = Image.new("RGB", size, bg)
    return image, ImageDraw.Draw(image)


def counter(draw: ImageDraw.ImageDraw, size: tuple[int, int], label: str, tokens: dict[str, str], dark: bool = False) -> None:
    fill = tokens["BG"] if dark else tokens["TEXT_2"]
    draw.text((size[0] - 150, size[1] - 76), label, font=load_font(24, bold=True), fill=fill)


def source(draw: ImageDraw.ImageDraw, size: tuple[int, int], text: str, tokens: dict[str, str], dark: bool = False) -> None:
    fill = tokens["BG"] if dark else tokens["TEXT_2"]
    draw_wrapped_text(draw, (70, size[1] - 72), text, load_font(18), size[0] - 240, fill, line_gap=4)


def headline(
    draw: ImageDraw.ImageDraw,
    text: str,
    tokens: dict[str, str],
    size: tuple[int, int],
    y: int = 72,
    dark: bool = False,
    font_size: int = 58,
) -> int:
    fill = tokens["BG"] if dark else tokens["TEXT"]
    return draw_wrapped_text(draw, (70, y), text, load_font(font_size, bold=True), size[0] - 140, fill, line_gap=10)


def subhead(draw: ImageDraw.ImageDraw, text: str, tokens: dict[str, str], size: tuple[int, int], y: int, dark: bool = False) -> int:
    fill = tokens["BLUE_BG"] if dark else tokens["TEXT_2"]
    return draw_wrapped_text(draw, (70, y), text, load_font(30, bold=True), size[0] - 140, fill, line_gap=8)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str, width: int = 5) -> None:
    draw.line((start, end), fill=color, width=width)
    sx, sy = start
    ex, ey = end
    angle = math.atan2(ey - sy, ex - sx)
    size = 16
    points = [
        (ex, ey),
        (ex - size * math.cos(angle - 0.48), ey - size * math.sin(angle - 0.48)),
        (ex - size * math.cos(angle + 0.48), ey - size * math.sin(angle + 0.48)),
    ]
    draw.polygon(points, fill=color)


def metric_card(
    draw: ImageDraw.ImageDraw,
    box: Box,
    value: str,
    label: str,
    tokens: dict[str, str],
    color: str,
    fill: str | None = None,
) -> None:
    rounded_panel(draw, box, fill or tokens["LIGHT_BG"], color, radius=24, width=5)
    value_font = fit_font_size(draw, value, box.width - 56, max(42, box.height // 2 - 18), 58, min_size=30, bold=True)
    draw.text((box.x + 28, box.y + 24), value, font=value_font, fill=color)
    _, value_h = text_size(draw, value, value_font)
    label_y = box.y + 34 + value_h
    label_font = fit_font_size(draw, label, box.width - 60, max(38, box.y + box.height - label_y - 22), 25, min_size=16, bold=True)
    draw_wrapped_text(draw, (box.x + 30, label_y), label, label_font, box.width - 60, tokens["TEXT"], line_gap=4)


def compact_metric_card(draw: ImageDraw.ImageDraw, box: Box, value: str, label: str, tokens: dict[str, str], color: str, fill: str | None = None) -> None:
    rounded_panel(draw, box, fill or tokens["LIGHT_BG"], color, radius=18, width=4)
    value_font = fit_font_size(draw, value, box.width - 36, box.height // 2 - 8, 40, min_size=22, bold=True)
    vw, vh = text_size(draw, value, value_font)
    draw.text((box.x + (box.width - vw) // 2, box.y + 15), value, font=value_font, fill=color)
    label_font = fit_font_size(draw, label, box.width - 36, box.height - vh - 34, 20, min_size=13, bold=True)
    lines_y = box.y + 22 + vh
    draw_wrapped_text(draw, (box.x + 18, lines_y), label, label_font, box.width - 36, tokens["TEXT"], line_gap=2)


def draw_gauge(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int, value: float, tokens: dict[str, str], color: str) -> None:
    cx, cy = center
    box = (cx - radius, cy - radius, cx + radius, cy + radius)
    draw.arc(box, 180, 360, fill=tokens["GRID"], width=22)
    draw.arc(box, 180, 180 + int(180 * value), fill=color, width=22)
    angle = math.radians(180 + 180 * value)
    nx = cx + int((radius - 28) * math.cos(angle))
    ny = cy + int((radius - 28) * math.sin(angle))
    draw.line((cx, cy, nx, ny), fill=tokens["TEXT"], width=6)
    draw.ellipse((cx - 10, cy - 10, cx + 10, cy + 10), fill=tokens["TEXT"])


def draw_tool_scene(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str]) -> None:
    left = Box(box.x, box.y, int(box.width * 0.56), box.height)
    right = Box(box.x + int(box.width * 0.62), box.y + 12, int(box.width * 0.35), box.height - 24)
    rounded_panel(draw, left, tokens["LIGHT_BG"], tokens["ACCENT"], radius=28, width=5)
    draw.text((left.x + 28, left.y + 28), "agent says", font=load_font(27, bold=True), fill=tokens["ACCENT"])
    draw_wrapped_text(draw, (left.x + 30, left.y + 92), '"I validated the schema and ran the checks."', load_font(36, bold=True), left.width - 60, tokens["TEXT"], line_gap=8)
    rounded_panel(draw, right, tokens["TEXT"], tokens["TEXT"], radius=24, width=4)
    draw.text((right.x + 26, right.y + 24), "tool log", font=load_font(26, bold=True), fill=tokens["BG"])
    draw.text((right.x + 34, right.y + 78), "0", font=load_font(86, bold=True), fill=tokens["WARN"])
    draw_wrapped_text(draw, (right.x + 122, right.y + 95), "actions executed", load_font(25, bold=True), right.width - 150, tokens["BG"], line_gap=4)
    arrow(draw, (left.x + left.width + 14, left.y + left.height // 2), (right.x - 10, right.y + right.height // 2), tokens["WARN"], 6)


def sourdough_strip(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str]) -> None:
    labels = [
        ("prompt", "bake sourdough?", "neutral"),
        ("wrong", "recipe answer", "fail"),
        ("expected", "redirect", "pass"),
        ("gate", "CI blocks", "blocked"),
    ]
    colors = [tokens["ACCENT"], tokens["WARN"], tokens["SUCCESS"], tokens["ACCENT_3"]]
    panel_w = (box.width - 45) // 4
    for i, ((label, detail, status), color) in enumerate(zip(labels, colors)):
        x = box.x + i * (panel_w + 15)
        panel = Box(x, box.y, panel_w, box.height)
        rounded_panel(draw, panel, tokens["LIGHT_BG"], color, radius=22, width=4)
        if i < 3:
            arrow(draw, (x + panel_w + 4, box.y + box.height // 2), (x + panel_w + 16, box.y + box.height // 2), tokens["TEXT_2"], 4)
        draw.ellipse((x + panel_w // 2 - 34, box.y + 44, x + panel_w // 2 + 34, box.y + 112), fill=tokens["BG"], outline=color, width=5)
        if i == 1:
            draw.arc((x + panel_w // 2 - 20, box.y + 75, x + panel_w // 2 + 20, box.y + 105), 180, 360, fill=tokens["WARN"], width=4)
            draw.rectangle((x + panel_w // 2 - 32, box.y + 22, x + panel_w // 2 + 32, box.y + 36), fill=tokens["RED_BG"], outline=tokens["WARN"], width=2)
        elif i == 2:
            draw.arc((x + panel_w // 2 - 20, box.y + 70, x + panel_w // 2 + 20, box.y + 104), 0, 180, fill=tokens["SUCCESS"], width=4)
        elif i == 3:
            draw.line((x + panel_w // 2 - 20, box.y + 78, x + panel_w // 2 + 20, box.y + 105), fill=tokens["WARN"], width=4)
            draw.line((x + panel_w // 2 + 20, box.y + 78, x + panel_w // 2 - 20, box.y + 105), fill=tokens["WARN"], width=4)
        else:
            draw.line((x + panel_w // 2 - 18, box.y + 92, x + panel_w // 2 + 18, box.y + 92), fill=tokens["TEXT"], width=4)
        draw.text((x + 22, box.y + 145), label, font=load_font(25, bold=True), fill=color)
        draw_wrapped_text(draw, (x + 22, box.y + 184), detail, load_font(22, bold=True), panel_w - 44, tokens["TEXT"], line_gap=4)
        status_fill = tokens["RED_BG"] if status in ("fail", "blocked") else tokens["TEAL_BG"]
        status_color = tokens["WARN"] if status in ("fail", "blocked") else tokens["SUCCESS"]
        draw.rounded_rectangle((x + 20, box.y + box.height - 54, x + panel_w - 20, box.y + box.height - 18), radius=12, fill=status_fill, outline=status_color, width=2)
        sw, _ = text_size(draw, status, load_font(18, bold=True))
        draw.text((x + (panel_w - sw) // 2, box.y + box.height - 47), status, font=load_font(18, bold=True), fill=status_color)


def eval_factory(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str]) -> None:
    steps = [
        ("tasks", "real workflows", tokens["ACCENT"]),
        ("graders", "text + tool checks", tokens["ACCENT_2"]),
        ("CI gate", "pass or block", tokens["WARN"]),
        ("history", "drift over time", tokens["ACCENT_3"]),
    ]
    w = (box.width - 72) // 4
    for i, (name, detail, color) in enumerate(steps):
        x = box.x + i * (w + 24)
        b = Box(x, box.y, w, box.height)
        rounded_panel(draw, b, tokens["LIGHT_BG"], color, radius=22, width=4)
        draw.ellipse((x + w // 2 - 32, box.y + 32, x + w // 2 + 32, box.y + 96), fill=tokens["BG"], outline=color, width=4)
        draw.text((x + w // 2 - 10, box.y + 48), str(i + 1), font=load_font(28, bold=True), fill=color)
        draw_wrapped_text(draw, (x + 20, box.y + 120), name, load_font(28, bold=True), w - 40, tokens["TEXT"], line_gap=5)
        draw_wrapped_text(draw, (x + 20, box.y + 162), detail, load_font(21, bold=True), w - 40, tokens["TEXT_2"], line_gap=5)
        if i < len(steps) - 1:
            arrow(draw, (x + w + 5, box.y + box.height // 2), (x + w + 22, box.y + box.height // 2), tokens["ACCENT"], 4)


def _layer_icon(draw: ImageDraw.ImageDraw, cx: int, cy: int, kind: str, color: str, tokens: dict[str, str]) -> None:
    """Draw a distinct glyph per eval layer so each band reads differently at a glance."""
    if kind == "tasks":
        for r in range(3):
            ly = cy - 26 + r * 26
            draw.rounded_rectangle((cx - 30, ly, cx - 14, ly + 16), radius=4, fill=tokens["BG"], outline=color, width=4)
            draw.line((cx - 6, ly + 8, cx + 30, ly + 8), fill=color, width=5)
    elif kind == "graders":
        draw.ellipse((cx - 30, cy - 30, cx + 14, cy + 14), outline=color, width=6)
        draw.line((cx + 8, cy + 8, cx + 30, cy + 30), fill=color, width=8)
        draw.line((cx - 22, cy - 6, cx - 12, cy + 4), fill=tokens["SUCCESS"], width=5)
        draw.line((cx - 12, cy + 4, cx + 6, cy - 20), fill=tokens["SUCCESS"], width=5)
    elif kind == "gate":
        draw.rectangle((cx - 32, cy - 26, cx - 22, cy + 30), fill=color)
        draw.rectangle((cx + 22, cy - 26, cx + 32, cy + 30), fill=color)
        for j in range(4):
            bx = cx - 22 + j * 12
            draw.polygon([(bx, cy - 18), (bx + 12, cy - 18), (bx, cy + 4), (bx - 12, cy + 4)], fill=tokens["WARN"] if j % 2 else tokens["BG"], outline=color)
    elif kind == "history":
        pts = [(cx - 32, cy + 24), (cx - 12, cy - 4), (cx + 6, cy + 8), (cx + 32, cy - 26)]
        draw.line(pts, fill=color, width=6, joint="curve")
        for px, py in pts:
            draw.ellipse((px - 6, py - 6, px + 6, py + 6), fill=color)


def layer_stack(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str]) -> None:
    """Stacked-layer view of the eval system: foundation at the bottom, each layer building upward."""
    layers = [
        ("4", "history", "drift by model, prompt, tool", tokens["ACCENT_3"], tokens["PURPLE_BG"], "history"),
        ("3", "CI gate", "pass or block the release", tokens["WARN"], tokens["RED_BG"], "gate"),
        ("2", "graders", "text + tool-call checks", tokens["ACCENT_2"], tokens["TEAL_BG"], "graders"),
        ("1", "tasks", "real production workflows", tokens["ACCENT"], tokens["BLUE_BG"], "tasks"),
    ]
    gap = 18
    band_h = (box.height - gap * (len(layers) - 1)) // len(layers)
    arrow(draw, (box.x - 28, box.y + box.height), (box.x - 28, box.y - 6), tokens["TEXT_2"], 5)
    draw.text((box.x - 62, box.y - 36), "builds on", font=load_font(19, bold=True), fill=tokens["TEXT_2"])
    for i, (num, name, detail, color, tint, icon) in enumerate(layers):
        y = box.y + i * (band_h + gap)
        band = Box(box.x, y, box.width, band_h)
        rounded_panel(draw, band, tint, color, radius=20, width=5)
        ccx, ccy = box.x + 60, y + band_h // 2
        draw.ellipse((ccx - 34, ccy - 34, ccx + 34, ccy + 34), fill=tokens["BG"], outline=color, width=5)
        nw, nh = text_size(draw, num, load_font(34, bold=True))
        draw.text((ccx - nw // 2, ccy - nh // 2 - 2), num, font=load_font(34, bold=True), fill=color)
        draw.text((box.x + 118, y + band_h // 2 - 34), name, font=load_font(36, bold=True), fill=tokens["TEXT"])
        draw.text((box.x + 120, y + band_h // 2 + 12), detail, font=load_font(23, bold=True), fill=tokens["TEXT_2"])
        _layer_icon(draw, box.x + box.width - 70, ccy, icon, color, tokens)
    foundation = layers[-1]
    draw.text((box.x + 118, box.y + box.height + 16), "foundation layer", font=load_font(21, bold=True), fill=foundation[3])


def route_map(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str]) -> None:
    points = [
        ("benchmark gap", tokens["WARN"], "74-78% vs 35-50%"),
        ("trace check", tokens["ACCENT"], "tool calls, gates"),
        ("Sourdough", tokens["ACCENT_3"], "persona drift"),
        ("CI gate", tokens["SUCCESS"], "block release"),
    ]
    coords = [
        (box.x + 115, box.y + 95),
        (box.x + 360, box.y + 215),
        (box.x + 615, box.y + 95),
        (box.x + 830, box.y + 245),
    ]
    for i in range(len(coords) - 1):
        arrow(draw, coords[i], coords[i + 1], tokens["TEXT_2"], 5)
    for (label, color, detail), (cx, cy) in zip(points, coords):
        draw.ellipse((cx - 78, cy - 78, cx + 78, cy + 78), fill=tokens["LIGHT_BG"], outline=color, width=6)
        draw_wrapped_text(draw, (cx - 58, cy - 36), label, load_font(24, bold=True), 116, tokens["TEXT"], line_gap=4)
        draw.rounded_rectangle((cx - 100, cy + 92, cx + 100, cy + 145), radius=14, fill=tokens["BG"], outline=color, width=3)
        draw_wrapped_text(draw, (cx - 82, cy + 104), detail, load_font(18, bold=True), 164, tokens["TEXT_2"], line_gap=2)


def workflow_branch_map(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str]) -> None:
    hub = (box.x + box.width // 2, box.y + box.height // 2)
    branches = [
        ("handoff", box.x + 70, box.y + 55, tokens["ACCENT"]),
        ("tool call", box.x + box.width - 250, box.y + 55, tokens["ACCENT_2"]),
        ("policy edge", box.x + 70, box.y + box.height - 130, tokens["WARN"]),
        ("weird request", box.x + box.width - 250, box.y + box.height - 130, tokens["SUCCESS"]),
    ]
    for label, x, y, color in branches:
        arrow(draw, hub, (x + 90, y + 45), color, 5)
        rounded_panel(draw, Box(x, y, 220, 90), tokens["LIGHT_BG"], color, radius=20, width=4)
        draw_wrapped_text(draw, (x + 22, y + 26), label, load_font(25, bold=True), 176, tokens["TEXT"], line_gap=4)
    draw.ellipse((hub[0] - 105, hub[1] - 105, hub[0] + 105, hub[1] + 105), fill=tokens["PURPLE_BG"], outline=tokens["ACCENT_3"], width=6)
    draw.ellipse((hub[0] - 83, hub[1] - 83, hub[0] + 83, hub[1] + 83), fill=tokens["BG"], outline=tokens["PURPLE_BG"], width=4)
    draw_wrapped_text(draw, (hub[0] - 62, hub[1] - 38), "38-task suite", load_font(30, bold=True), 124, tokens["TEXT"], line_gap=4)


def readiness_panel(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str]) -> None:
    labels = [
        ("tasks", tokens["ACCENT"], True),
        ("traces", tokens["ACCENT_2"], True),
        ("persona", tokens["ACCENT_3"], True),
        ("history", tokens["SUCCESS"], True),
        ("ship gate", tokens["WARN"], False),
    ]
    gate = Box(box.x + box.width - 250, box.y + 92, 210, 180)
    draw.rounded_rectangle((box.x + 70, box.y + 70, gate.x - 38, box.y + 290), radius=24, fill=tokens["LIGHT_BG"], outline=tokens["GRID"], width=3)
    for i, (label, color, ok) in enumerate(labels[:-1]):
        x = box.x + 115 + (i % 2) * 250
        y = box.y + 105 + (i // 2) * 105
        draw.line((x + 150, y + 22, gate.x, gate.y + 88), fill=tokens["GRID"], width=4)
        draw.ellipse((x, y, x + 52, y + 52), fill=tokens["TEAL_BG"], outline=tokens["SUCCESS"], width=4)
        draw.line((x + 14, y + 27, x + 25, y + 39), fill=tokens["SUCCESS"], width=5)
        draw.line((x + 25, y + 39, x + 42, y + 15), fill=tokens["SUCCESS"], width=5)
        draw.text((x + 68, y + 11), label, font=load_font(25, bold=True), fill=tokens["TEXT"])
    rounded_panel(draw, gate, tokens["RED_BG"], tokens["WARN"], radius=22, width=5)
    draw.line((gate.x + 55, gate.y + 58, gate.x + 155, gate.y + 122), fill=tokens["WARN"], width=10)
    draw.line((gate.x + 155, gate.y + 58, gate.x + 55, gate.y + 122), fill=tokens["WARN"], width=10)
    draw_wrapped_text(draw, (gate.x + 35, gate.y + 130), "ship gate blocked", load_font(24, bold=True), gate.width - 70, tokens["WARN"], line_gap=4)


def factory_conveyor(draw: ImageDraw.ImageDraw, box: Box, tokens: dict[str, str], compact: bool = False) -> None:
    belt_y = box.y + int(box.height * 0.58)
    draw.rounded_rectangle((box.x, belt_y, box.x + box.width, belt_y + 34), radius=14, fill=tokens["TEXT_2"])
    stations = [
        ("task suite", tokens["ACCENT"]),
        ("graders", tokens["ACCENT_2"]),
        ("CI gate", tokens["WARN"]),
        ("history", tokens["ACCENT_3"]),
    ]
    spacing = box.width // 4
    for i, (label, color) in enumerate(stations):
        cx = box.x + spacing * i + spacing // 2
        draw.rectangle((cx - 52, belt_y - 82, cx + 52, belt_y), fill=tokens["LIGHT_BG"], outline=color, width=4)
        draw.polygon([(cx - 62, belt_y - 82), (cx + 62, belt_y - 82), (cx + 34, belt_y - 122), (cx - 34, belt_y - 122)], fill=tokens["BLUE_BG"], outline=color)
        if label == "CI gate":
            draw.rounded_rectangle((cx - 64, belt_y + 58, cx + 64, belt_y + 104), radius=12, fill=tokens["RED_BG"], outline=tokens["WARN"], width=3)
            draw.text((cx - 35, belt_y + 70), "block", font=load_font(20, bold=True), fill=tokens["WARN"])
        elif label == "history":
            for j in range(3):
                draw.line((cx - 48, belt_y + 55 + j * 17, cx + 45, belt_y + 55 + j * 17), fill=color, width=4)
        else:
            draw.ellipse((cx - 34, belt_y + 58, cx + 34, belt_y + 126), fill=tokens["BG"], outline=color, width=4)
        font = load_font(20 if compact else 24, bold=True)
        draw_wrapped_text(draw, (cx - 72, belt_y - 170), label, font, 144, tokens["TEXT"], line_gap=4)


def slide_01() -> None:
    tokens = theme(0)
    size = (1080, 1080)
    image, draw = canvas(size, tokens, dark=True)
    draw.text((70, 82), "AI agent evals", font=load_font(34, bold=True), fill=tokens["BLUE_BG"])
    draw.text((70, 200), "74-78%", font=load_font(138, bold=True), fill=tokens["ACCENT"])
    draw_wrapped_text(draw, (75, 355), "is not production readiness", load_font(54, bold=True), 760, tokens["BG"], line_gap=10)
    draw.line((110, 610, 450, 520), fill=tokens["ACCENT"], width=20)
    draw.line((650, 520, 980, 610), fill=tokens["WARN"], width=20)
    draw.polygon([(515, 500), (565, 500), (540, 555)], fill=tokens["TEXT_2"], outline=tokens["BG"])
    draw.text((70, 810), "What is missing?", font=load_font(44, bold=True), fill=tokens["BG"])
    source(draw, size, "Source: SWE-bench; Presenc May 2026 vendor snapshot", tokens, dark=True)
    counter(draw, size, "01 / 10", tokens, dark=True)
    save_png(image, OUT_DIR / "slide-01-hook.png")


def slide_02() -> None:
    tokens = theme(1)
    size = (1080, 1080)
    image, draw = canvas(size, tokens)
    y = headline(draw, "The route from benchmark to release", tokens, size)
    subhead(draw, "Four visual checks close the behavior gap.", tokens, size, y + 10)
    route_map(draw, Box(80, 365, 920, 430), tokens)
    source(draw, size, "Source: SWE-bench; Presenc May 2026 vendor snapshot", tokens)
    counter(draw, size, "02 / 10", tokens)
    save_png(image, OUT_DIR / "slide-02-promise.png")


def slide_03() -> None:
    tokens = theme(2)
    size = (1080, 1080)
    image, draw = canvas(size, tokens)
    headline(draw, "The gap is behavioral", tokens, size)
    metric_card(draw, Box(85, 310, 390, 230), "74-78%", "SWE-bench Verified capability signal", tokens, tokens["ACCENT"], tokens["BLUE_BG"])
    metric_card(draw, Box(605, 310, 390, 230), "35-50%", "real-world PR acceptance estimate", tokens, tokens["WARN"], tokens["RED_BG"])
    arrow(draw, (475, 425), (605, 425), tokens["WARN"], 8)
    draw_wrapped_text(draw, (120, 650), "Benchmarks ask whether an agent can solve a task. Production evals ask whether it follows the behavior contract.", load_font(38, bold=True), 840, tokens["TEXT"], line_gap=10)
    source(draw, size, "Source: Presenc May 2026 vendor snapshot; SWE-bench", tokens)
    counter(draw, size, "03 / 10", tokens)
    save_png(image, OUT_DIR / "slide-03-problem.png")


def slide_04() -> None:
    tokens = theme(3)
    size = (1080, 1080)
    image, draw = canvas(size, tokens)
    headline(draw, "Four layers make evals real", tokens, size)
    layer_stack(draw, Box(135, 255, 865, 440), tokens)
    draw_wrapped_text(draw, (120, 760), "Start small: one task suite, behavior graders, a CI gate, and history by model, prompt, tool, and release.", load_font(36, bold=True), 840, tokens["TEXT"], line_gap=10)
    source(draw, size, "Source: First-party AI Agent Evals implementation pattern", tokens)
    counter(draw, size, "04 / 10", tokens)
    save_png(image, OUT_DIR / "slide-04-framework.png")


def slide_05() -> None:
    tokens = theme(4)
    size = (1080, 1080)
    image, draw = canvas(size, tokens)
    draw.text((70, 78), "01", font=load_font(98, bold=True), fill=tokens["ACCENT"])
    headline(draw, "Use real workflows first", tokens, size, y=205)
    workflow_branch_map(draw, Box(95, 415, 890, 360), tokens)
    metric_card(draw, Box(145, 820, 320, 140), "38", "workflow tasks", tokens, tokens["ACCENT"])
    metric_card(draw, Box(615, 820, 320, 140), "8", "agents tested", tokens, tokens["ACCENT_3"])
    source(draw, size, "Source: First-party/original implementation metrics", tokens)
    counter(draw, size, "05 / 10", tokens)
    save_png(image, OUT_DIR / "slide-05-step1.png")


def slide_06() -> None:
    tokens = theme(5)
    size = (1080, 1080)
    image, draw = canvas(size, tokens)
    draw.text((70, 78), "02", font=load_font(98, bold=True), fill=tokens["ACCENT"])
    headline(draw, "Grade the behavior trace", tokens, size, y=205)
    draw_tool_scene(draw, Box(95, 430, 890, 285), tokens)
    draw_wrapped_text(draw, (120, 775), "Final answer checks are not enough. Assert tool calls, refusal boundaries, and required confirmation gates.", load_font(35, bold=True), 840, tokens["TEXT"], line_gap=9)
    source(draw, size, "Source: OpenAI Evals guide; first-party behavior graders", tokens)
    counter(draw, size, "06 / 10", tokens)
    save_png(image, OUT_DIR / "slide-06-step2.png")


def slide_07() -> None:
    tokens = theme(6)
    size = (1080, 1080)
    image, draw = canvas(size, tokens)
    draw.text((70, 78), "03", font=load_font(98, bold=True), fill=tokens["ACCENT"])
    headline(draw, "Block regressions in CI", tokens, size, y=205)
    factory_conveyor(draw, Box(100, 430, 880, 330), tokens)
    compact_metric_card(draw, Box(105, 810, 275, 135), "$3-8", "per run", tokens, tokens["ACCENT"])
    compact_metric_card(draw, Box(405, 810, 275, 135), "200K-400K", "tokens", tokens, tokens["ACCENT_3"])
    compact_metric_card(draw, Box(705, 810, 275, 135), "15-25m", "runtime", tokens, tokens["WARN"])
    source(draw, size, "Source: First-party/original implementation metrics", tokens)
    counter(draw, size, "07 / 10", tokens)
    save_png(image, OUT_DIR / "slide-07-step3.png")


def slide_08() -> None:
    tokens = theme(7)
    size = (1080, 1080)
    image, draw = canvas(size, tokens, dark=True)
    draw.text((70, 95), "pattern interrupt", font=load_font(30, bold=True), fill=tokens["BLUE_BG"])
    draw_wrapped_text(draw, (92, 260), '"The answer can look perfect while the agent skipped the work."', load_font(62, bold=True), 875, tokens["BG"], line_gap=14)
    draw_tool_scene(draw, Box(120, 675, 840, 235), tokens)
    source(draw, size, "Source: AI Agent Evals failure taxonomy", tokens, dark=True)
    counter(draw, size, "08 / 10", tokens, dark=True)
    save_png(image, OUT_DIR / "slide-08-interrupt.png")


def slide_09() -> None:
    tokens = theme(8)
    size = (1080, 1080)
    image, draw = canvas(size, tokens)
    headline(draw, "Your release control panel", tokens, size)
    subhead(draw, "Green only counts when every behavior gate is wired.", tokens, size, 215)
    readiness_panel(draw, Box(90, 350, 900, 365), tokens)
    draw_wrapped_text(draw, (115, 800), "If the ship gate is missing, benchmark scores become decoration.", load_font(38, bold=True), 850, tokens["TEXT"], line_gap=10)
    source(draw, size, "Source: AI Agent Evals production-readiness guide", tokens)
    counter(draw, size, "09 / 10", tokens)
    save_png(image, OUT_DIR / "slide-09-recap.png")


def slide_10() -> None:
    tokens = theme(9)
    size = (1080, 1080)
    image, draw = canvas(size, tokens)
    headline(draw, "Save this before your next agent release", tokens, size)
    sourdough_strip(draw, Box(95, 315, 890, 370), tokens)
    rounded_panel(draw, Box(150, 770, 780, 115), tokens["BLUE_BG"], tokens["ACCENT"], radius=28, width=5)
    draw_wrapped_text(draw, (195, 800), "Full visual guide: link in comments", load_font(36, bold=True), 700, tokens["TEXT"], line_gap=8)
    draw_wrapped_text(draw, (160, 915), "The Sourdough Test turns persona drift into a visible release signal.", load_font(28, bold=True), 760, tokens["TEXT_2"], line_gap=6)
    counter(draw, size, "10 / 10", tokens)
    save_png(image, OUT_DIR / "slide-10-cta.png")


def x_card_01() -> None:
    tokens = theme(10)
    size = (1600, 900)
    image, draw = canvas(size, tokens, dark=True)
    draw.text((90, 90), "AI agent evals", font=load_font(44, bold=True), fill=tokens["BLUE_BG"])
    draw.text((90, 225), "74-78%", font=load_font(140, bold=True), fill=tokens["ACCENT"])
    draw_wrapped_text(draw, (100, 410), "is not production readiness", load_font(64, bold=True), 900, tokens["BG"], line_gap=12)
    draw.line((1050, 320, 1230, 250), fill=tokens["ACCENT"], width=22)
    draw.line((1350, 250, 1530, 320), fill=tokens["WARN"], width=22)
    source(draw, size, "Source: SWE-bench; Presenc May 2026 vendor snapshot", tokens, dark=True)
    save_png(image, OUT_DIR / "x-card-01.png")


def x_card_02() -> None:
    tokens = theme(11)
    size = (1600, 900)
    image, draw = canvas(size, tokens)
    headline(draw, "The answer is polished. The trace is empty.", tokens, size, font_size=58)
    draw_tool_scene(draw, Box(120, 300, 1360, 330), tokens)
    source(draw, size, "Source: AI Agent Evals failure taxonomy", tokens)
    save_png(image, OUT_DIR / "x-card-02.png")


def x_card_03() -> None:
    tokens = theme(12)
    size = (1600, 900)
    image, draw = canvas(size, tokens)
    headline(draw, "Use the Sourdough Test for persona drift", tokens, size, font_size=58)
    sourdough_strip(draw, Box(120, 285, 1360, 390), tokens)
    metric_card(draw, Box(1235, 92, 250, 145), "3 of 8", "failed after model update", tokens, tokens["WARN"], tokens["RED_BG"])
    source(draw, size, "Source: First-party/original implementation: 3 of 8 agents failed", tokens)
    save_png(image, OUT_DIR / "x-card-03.png")


def x_card_04() -> None:
    tokens = theme(13)
    size = (1600, 900)
    image, draw = canvas(size, tokens)
    headline(draw, "Production evals belong in CI", tokens, size, font_size=62)
    eval_factory(draw, Box(120, 350, 1360, 250), tokens)
    source(draw, size, "Source: AI Agent Evals implementation pattern", tokens)
    save_png(image, OUT_DIR / "x-card-04.png")


def medium_hero() -> None:
    tokens = theme(14)
    size = (1400, 800)
    image, draw = canvas(size, tokens)
    draw_wrapped_text(draw, (70, 70), "AI Agent Evals for Production Readiness", load_font(62, bold=True), 720, tokens["TEXT"], line_gap=10)
    draw.text((75, 250), "Benchmarks prove capability.", font=load_font(34, bold=True), fill=tokens["TEXT_2"])
    draw.text((75, 300), "Production evals prove behavior.", font=load_font(34, bold=True), fill=tokens["TEXT_2"])
    draw_gauge(draw, (980, 410), 118, 0.78, tokens, tokens["ACCENT"])
    draw_gauge(draw, (1210, 410), 118, 0.50, tokens, tokens["WARN"])
    rounded_panel(draw, Box(845, 545, 270, 95), tokens["BLUE_BG"], tokens["ACCENT"], radius=20, width=3)
    draw.text((875, 566), "SWE-bench 74-78%", font=load_font(27, bold=True), fill=tokens["ACCENT"])
    rounded_panel(draw, Box(1118, 545, 250, 95), tokens["RED_BG"], tokens["WARN"], radius=20, width=3)
    draw.text((1142, 566), "PR accept 35-50%", font=load_font(27, bold=True), fill=tokens["WARN"])
    source(draw, size, "Source: SWE-bench; Presenc May 2026 vendor snapshot", tokens)
    save_png(image, OUT_DIR / "medium-hero.png")


def medium_inline_01() -> None:
    tokens = theme(15)
    size = (1200, 800)
    image, draw = canvas(size, tokens)
    headline(draw, "Behavior gaps hide in traces", tokens, size, font_size=54)
    draw_tool_scene(draw, Box(90, 270, 1020, 300), tokens)
    source(draw, size, "Source: AI Agent Evals failure taxonomy", tokens)
    save_png(image, OUT_DIR / "medium-inline-01.png")


def medium_inline_02() -> None:
    tokens = theme(16)
    size = (1200, 800)
    image, draw = canvas(size, tokens)
    headline(draw, "The CI eval system has four layers", tokens, size, font_size=52)
    eval_factory(draw, Box(90, 330, 1020, 230), tokens)
    source(draw, size, "Source: First-party AI Agent Evals implementation pattern", tokens)
    save_png(image, OUT_DIR / "medium-inline-02.png")


def substack_hero() -> None:
    tokens = theme(17)
    size = (1200, 630)
    image, draw = canvas(size, tokens)
    draw_wrapped_text(draw, (60, 60), "Stop treating SWE-bench like a ship gate", load_font(54, bold=True), 720, tokens["TEXT"], line_gap=9)
    draw.text((65, 285), "Production evals test behavior.", font=load_font(34, bold=True), fill=tokens["TEXT_2"])
    metric_card(draw, Box(790, 85, 330, 165), "74-78%", "SWE-bench Verified capability", tokens, tokens["ACCENT"], tokens["BLUE_BG"])
    metric_card(draw, Box(790, 315, 330, 165), "35-50%", "PR acceptance estimate", tokens, tokens["WARN"], tokens["RED_BG"])
    source(draw, size, "Source: SWE-bench; Presenc May 2026 vendor snapshot", tokens)
    save_png(image, OUT_DIR / "substack-hero.png")


def linkedin_exhibit_01() -> None:
    tokens = theme(18)
    size = (1200, 627)
    image, draw = canvas(size, tokens)
    draw.text((60, 40), "Exhibit 1", font=load_font(22, bold=True), fill=tokens["TEXT_2"])
    draw_wrapped_text(draw, (60, 80), "Capability benchmarks leave a production-behavior gap", load_font(38, bold=True), 1000, tokens["TEXT"], line_gap=8)
    metric_card(draw, Box(90, 240, 420, 170), "74-78%", "SWE-bench Verified", tokens, tokens["ACCENT"], tokens["BLUE_BG"])
    metric_card(draw, Box(690, 240, 420, 170), "35-50%", "PR acceptance estimate", tokens, tokens["WARN"], tokens["RED_BG"])
    arrow(draw, (510, 325), (690, 325), tokens["WARN"], 7)
    source(draw, size, "Source: SWE-bench; Presenc May 2026 vendor snapshot", tokens)
    save_png(image, OUT_DIR / "linkedin-exhibit-01.png")


def linkedin_exhibit_02() -> None:
    tokens = theme(19)
    size = (1200, 627)
    image, draw = canvas(size, tokens)
    draw.text((60, 40), "Exhibit 2", font=load_font(22, bold=True), fill=tokens["TEXT_2"])
    draw_wrapped_text(draw, (60, 80), "A small eval factory can run at pull-request speed", load_font(38, bold=True), 1000, tokens["TEXT"], line_gap=8)
    factory_conveyor(draw, Box(70, 230, 650, 260), tokens, compact=True)
    compact_metric_card(draw, Box(760, 188, 330, 92), "$3-8", "per run", tokens, tokens["ACCENT"])
    compact_metric_card(draw, Box(760, 310, 330, 92), "200K-400K", "tokens", tokens, tokens["ACCENT_3"])
    compact_metric_card(draw, Box(760, 432, 330, 92), "15-25m", "parallel runtime", tokens, tokens["WARN"])
    source(draw, size, "Source: First-party/original implementation: $3-8/run, 200K-400K tokens, 15-25 min", tokens)
    save_png(image, OUT_DIR / "linkedin-exhibit-02.png")


VISUALS = [
    slide_01,
    slide_02,
    slide_03,
    slide_04,
    slide_05,
    slide_06,
    slide_07,
    slide_08,
    slide_09,
    slide_10,
    x_card_01,
    x_card_02,
    x_card_03,
    x_card_04,
    medium_hero,
    medium_inline_01,
    medium_inline_02,
    substack_hero,
    linkedin_exhibit_01,
    linkedin_exhibit_02,
]


if __name__ == "__main__":
    for visual in VISUALS:
        visual()
    print(f"Rendered {len(VISUALS)} practitioner distilled assets.")
