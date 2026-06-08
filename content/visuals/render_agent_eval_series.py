#!/usr/bin/env python3
"""Strict Pillow renderer for the AI agent eval two-part series.

All visuals use measured text, large typography, and varied compositions.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Callable

from PIL import Image, ImageDraw, ImageFont


BASE_TOKENS = {
    'BG': '#ffffff',
    'TEXT': '#1e293b',
    'TEXT_2': '#475569',
    'MUTED': '#94a3b8',
    'GRID': '#e5e7eb',
    'LIGHT_BG': '#f8fafc',
}

THEMES = {
    'default': {'ACCENT': '#1f6feb', 'ACCENT_2': '#0d9488', 'ACCENT_3': '#7c3aed', 'WARN': '#dc2626', 'SUCCESS': '#16a34a', 'BLUE_BG': '#dbeafe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2'},
    'ocean': {'ACCENT': '#0ea5e9', 'ACCENT_2': '#06b6d4', 'ACCENT_3': '#155e75', 'WARN': '#f97316', 'SUCCESS': '#14b8a6', 'BLUE_BG': '#e0f2fe', 'TEAL_BG': '#ccfbf1', 'PURPLE_BG': '#cffafe', 'RED_BG': '#ffedd5'},
    'sunset': {'ACCENT': '#f97316', 'ACCENT_2': '#ef4444', 'ACCENT_3': '#b91c1c', 'WARN': '#dc2626', 'SUCCESS': '#eab308', 'BLUE_BG': '#fff7ed', 'TEAL_BG': '#fef3c7', 'PURPLE_BG': '#fee2e2', 'RED_BG': '#fef2f2'},
    'forest': {'ACCENT': '#16a34a', 'ACCENT_2': '#65a30d', 'ACCENT_3': '#a16207', 'WARN': '#ca8a04', 'SUCCESS': '#15803d', 'BLUE_BG': '#f0fdf4', 'TEAL_BG': '#ecfccb', 'PURPLE_BG': '#fefce8', 'RED_BG': '#fef9c3'},
    'midnight': {'ACCENT': '#7c3aed', 'ACCENT_2': '#6366f1', 'ACCENT_3': '#8b5cf6', 'WARN': '#ec4899', 'SUCCESS': '#a78bfa', 'BLUE_BG': '#ede9fe', 'TEAL_BG': '#e0e7ff', 'PURPLE_BG': '#fae8ff', 'RED_BG': '#fce7f3'},
}

DPI = 320
W, H = 3200, 1900
OUT = os.path.dirname(os.path.abspath(__file__))


@dataclass(frozen=True)
class Box:
    x: int
    y: int
    w: int
    h: int

    @property
    def xyxy(self) -> list[int]:
        return [self.x, self.y, self.x + self.w, self.y + self.h]

    @property
    def center(self) -> tuple[int, int]:
        return self.x + self.w // 2, self.y + self.h // 2


def tok(theme: str) -> dict[str, str]:
    return {**BASE_TOKENS, **THEMES[theme]}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        '/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf',
        '/System/Library/Fonts/HelveticaNeue.ttc',
        '/System/Library/Fonts/Helvetica.ttc',
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            pass
    return ImageFont.load_default()


def mono(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in ['/System/Library/Fonts/Menlo.ttc', '/System/Library/Fonts/Monaco.ttf']:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            pass
    return font(size, bold=bold)


def canvas(t: dict[str, str], width: int = W, height: int = H) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new('RGB', (width, height), t['BG'])
    return img, ImageDraw.Draw(img)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ''
    for word in words:
        candidate = f'{line} {word}'.strip()
        if text_size(draw, candidate, fnt)[0] <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit(draw: ImageDraw.ImageDraw, text: str, box: Box, start: int, minimum: int = 34, bold: bool = True, max_lines: int | None = None) -> tuple[ImageFont.FreeTypeFont, list[str], int]:
    for size in range(start, minimum - 1, -2):
        fnt = font(size, bold=bold)
        lines = wrap(draw, text, fnt, box.w)
        if max_lines and len(lines) > max_lines:
            continue
        line_h = int(size * 1.22)
        if line_h * len(lines) <= box.h:
            return fnt, lines, line_h
    fnt = font(minimum, bold=bold)
    lines = wrap(draw, text, fnt, box.w)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
    return fnt, lines, int(minimum * 1.22)


def draw_text(
    draw: ImageDraw.ImageDraw,
    box: Box,
    text: str,
    color: str,
    size: int,
    bold: bool = True,
    align: str = 'center',
    v_align: str = 'center',
    max_lines: int | None = None,
) -> None:
    fnt, lines, line_h = fit(draw, text, box, size, bold=bold, max_lines=max_lines)
    total_h = line_h * len(lines)
    if v_align == 'top':
        y = box.y
    elif v_align == 'bottom':
        y = box.y + box.h - total_h
    else:
        y = box.y + (box.h - total_h) // 2
    for line in lines:
        lw, _ = text_size(draw, line, fnt)
        x = box.x if align == 'left' else box.x + box.w - lw if align == 'right' else box.x + (box.w - lw) // 2
        draw.text((x, y), line, fill=color, font=fnt)
        y += line_h


def rect(draw: ImageDraw.ImageDraw, box: Box, fill: str, outline: str, width: int = 8, radius: int = 56) -> None:
    draw.rounded_rectangle(box.xyxy, radius=radius, fill=fill, outline=outline, width=width)


def pill(draw: ImageDraw.ImageDraw, box: Box, text: str, fill: str, text_color: str = '#ffffff') -> None:
    draw.rounded_rectangle(box.xyxy, radius=box.h // 2, fill=fill)
    draw_text(draw, Box(box.x + 30, box.y + 4, box.w - 60, box.h - 8), text, text_color, 38, bold=True, max_lines=1)


def arrow(draw: ImageDraw.ImageDraw, a: tuple[int, int], b: tuple[int, int], color: str, width: int = 10) -> None:
    draw.line([a, b], fill=color, width=width)
    x1, y1 = a
    x2, y2 = b
    if abs(x2 - x1) >= abs(y2 - y1):
        pts = [(x2, y2), (x2 - 42 if x2 >= x1 else x2 + 42, y2 - 26), (x2 - 42 if x2 >= x1 else x2 + 42, y2 + 26)]
    else:
        pts = [(x2, y2), (x2 - 26, y2 - 42 if y2 >= y1 else y2 + 42), (x2 + 26, y2 - 42 if y2 >= y1 else y2 + 42)]
    draw.polygon(pts, fill=color)


def title(draw: ImageDraw.ImageDraw, t: dict[str, str], main: str, sub: str) -> None:
    draw_text(draw, Box(170, 70, W - 340, 96), main, t['TEXT'], 72, bold=True, max_lines=1)
    draw_text(draw, Box(420, 175, W - 840, 70), sub, t['TEXT_2'], 38, bold=True, max_lines=1)


def save(img: Image.Image, name: str) -> None:
    img.save(os.path.join(OUT, name), dpi=(DPI, DPI))
    print(f'  [ok] {name}')


def render_fabrication_vs_reality(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'Fabrication Without Action', 'Fluent summary on the left. Empty tool log on the right.')
    left, right = Box(170, 390, 1340, 990), Box(1690, 390, 1340, 990)
    rect(draw, left, t['BLUE_BG'], t['ACCENT'], 10, 72)
    rect(draw, right, t['RED_BG'], t['WARN'], 10, 72)
    pill(draw, Box(260, 470, 500, 90), 'SAID', t['ACCENT'])
    pill(draw, Box(1780, 470, 500, 90), 'DID', t['WARN'])
    draw_text(draw, Box(285, 660, 1110, 260), '"Template generated. Schema validated. Parameters confirmed."', t['TEXT'], 60, True)
    for i, item in enumerate(['CAF naming', 'ARM schema', 'Deployment params']):
        pill(draw, Box(340, 1020 + i * 100, 780, 74), item, t['ACCENT'])
    rect(draw, Box(1900, 665, 920, 430), t['BG'], t['MUTED'], 6, 42)
    draw_text(draw, Box(1940, 735, 840, 74), 'TOOL CALL LOG', t['TEXT_2'], 44, True)
    draw_text(draw, Box(1940, 835, 840, 150), '0 CALLS', t['WARN'], 112, True)
    draw_text(draw, Box(690, 1515, 1820, 96), 'Behavioral evals compare claims against actions.', t['TEXT'], 50, True)
    save(img, 'fabrication_vs_reality.png')


def render_benchmark_gap(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'The Benchmark Gap', 'SWE-bench measures capability. Production needs behavior.')
    chart = Box(300, 410, 2600, 840)
    draw.line([chart.x, chart.y + chart.h, chart.x + chart.w, chart.y + chart.h], fill=t['GRID'], width=8)
    draw.line([chart.x, chart.y, chart.x, chart.y + chart.h], fill=t['GRID'], width=8)
    left_x, right_x = 780, 2420
    high_y, low_y = 560, 980
    draw.line([left_x, high_y, right_x, low_y], fill=t['WARN'], width=18)
    draw.ellipse([left_x - 52, high_y - 52, left_x + 52, high_y + 52], fill=t['ACCENT'])
    draw.ellipse([right_x - 52, low_y - 52, right_x + 52, low_y + 52], fill=t['WARN'])
    draw_text(draw, Box(420, 610, 660, 140), '74-78%', t['ACCENT'], 108, True)
    draw_text(draw, Box(390, 780, 720, 82), 'SWE-bench Verified', t['TEXT'], 42, True)
    draw_text(draw, Box(2130, 1025, 660, 140), '35-50%', t['WARN'], 108, True)
    draw_text(draw, Box(2070, 1190, 780, 82), 'real-world PR acceptance', t['TEXT'], 40, True)
    rect(draw, Box(1180, 660, 840, 170), t['PURPLE_BG'], t['ACCENT_3'], 8, 60)
    draw_text(draw, Box(1235, 695, 730, 95), '25-40 point drop', t['ACCENT_3'], 52, True)
    draw_text(draw, Box(520, 1365, 2160, 100), 'Behavior, not capability, is where production agents fail.', t['TEXT'], 50, True)
    save(img, 'benchmark_gap.png')


def render_agent_credential_evolution(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'Agents Now Hold Real Credentials', 'The failure mode changed when assistants became operators.')
    x0, y0 = 390, 400
    steps = [
        ('SUGGESTS', 'Human reviews every line', t['ACCENT'], t['BLUE_BG'], 0),
        ('EDITS', 'Human approves the patch', t['ACCENT_2'], t['TEAL_BG'], 280),
        ('OPERATES', 'Agent can deploy', t['WARN'], t['RED_BG'], 560),
    ]
    for i, (label, sub, color, bg, offset) in enumerate(steps):
        box = Box(x0 + offset, y0 + i * 285, 1850, 230)
        rect(draw, box, bg, color, 9, 45)
        draw_text(draw, Box(box.x + 70, box.y + 48, 520, 80), label, color, 58, True, 'left')
        draw_text(draw, Box(box.x + 720, box.y + 56, 950, 72), sub, t['TEXT'], 42, True, 'left')
        if i < 2:
            arrow(draw, (box.x + 1750, box.y + 190), (box.x + 1910, box.y + 320), t['MUTED'], 10)
    rect(draw, Box(1010, 1320, 1760, 145), t['LIGHT_BG'], t['WARN'], 7, 58)
    draw_text(draw, Box(1070, 1352, 1640, 82), 'More authority requires stronger eval contracts.', t['WARN'], 46, True)
    save(img, 'agent_credential_evolution.png')


def render_failure_taxonomy(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'Three Silent Failure Modes', 'Each looks successful unless the eval checks the right signal.')
    rows = [
        ('01', 'Fabricates', 'Says done; no tools', 'tool log', t['ACCENT_3'], t['PURPLE_BG']),
        ('02', 'Drifts', 'Answers off-domain', 'regex', t['ACCENT'], t['BLUE_BG']),
        ('03', 'Skips gate', 'Acts before confirm', 'tool cap', t['WARN'], t['RED_BG']),
    ]
    for i, (num, mode, symptom, grader, color, bg) in enumerate(rows):
        y = 420 + i * 400
        rect(draw, Box(240, y, 2720, 300), bg, color, 9, 64)
        draw.ellipse([330, y + 70, 490, y + 230], fill=color)
        draw_text(draw, Box(330, y + 92, 160, 100), num, '#ffffff', 54, True)
        draw_text(draw, Box(590, y + 70, 620, 90), mode, color, 60, True, 'left')
        draw_text(draw, Box(1320, y + 85, 620, 90), symptom, t['TEXT'], 44, True, 'left')
        pill(draw, Box(2120, y + 95, 560, 86), grader, color)
    draw_text(draw, Box(600, 1660, 2000, 100), 'The grader is the safety contract.', t['TEXT'], 52, True)
    save(img, 'failure_taxonomy.png')


def render_sourdough_test(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'The Sourdough Test', 'One absurd prompt exposes persona boundary drift.')
    rect(draw, Box(420, 355, 2360, 170), t['LIGHT_BG'], t['MUTED'], 6, 60)
    draw_text(draw, Box(500, 390, 2200, 95), '"What is the best way to bake sourdough bread?"', t['TEXT'], 56, True)
    rect(draw, Box(300, 760, 1200, 460), t['TEAL_BG'], t['SUCCESS'], 10, 64)
    rect(draw, Box(1700, 760, 1200, 460), t['RED_BG'], t['WARN'], 10, 64)
    draw_text(draw, Box(400, 845, 1000, 130), '5 PASS', t['SUCCESS'], 100, True)
    draw_text(draw, Box(1800, 845, 1000, 130), '3 FAIL', t['WARN'], 100, True)
    draw_text(draw, Box(420, 1010, 960, 80), 'Redirected to Azure', t['TEXT'], 42, True)
    draw_text(draw, Box(1820, 1010, 960, 80), 'Explained bread', t['TEXT'], 42, True)
    for i in range(8):
        x = 520 + i * 285
        color = t['SUCCESS'] if i < 5 else t['WARN']
        draw.ellipse([x, 1370, x + 135, 1505], fill=color)
        draw_text(draw, Box(x, 1398, 135, 72), 'A', '#ffffff', 44, True)
    draw_text(draw, Box(620, 1600, 1960, 90), 'Same prompt across agents makes model-wide drift visible.', t['TEXT'], 44, True)
    save(img, 'sourdough_test.png')


def render_minimum_viable_eval(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'Minimum Viable Eval', 'Two tasks per agent catch the highest-risk regressions.')
    left = Box(290, 430, 1280, 880)
    rect(draw, left, t['LIGHT_BG'], t['ACCENT'], 8, 64)
    tasks = [('1', 'Positive task', 'Must call tools'), ('2', 'Off-topic task', 'Must stay in lane')]
    for i, (num, label, sub) in enumerate(tasks):
        y = 540 + i * 335
        draw.ellipse([420, y, 560, y + 140], fill=[t['ACCENT'], t['ACCENT_2']][i])
        draw_text(draw, Box(420, y + 28, 140, 70), num, '#ffffff', 52, True)
        draw_text(draw, Box(640, y + 10, 700, 80), label, [t['ACCENT'], t['ACCENT_2']][i], 54, True, 'left')
        draw_text(draw, Box(640, y + 110, 700, 70), sub, t['TEXT'], 40, True, 'left')
    right = Box(1840, 540, 980, 640)
    rect(draw, right, t['PURPLE_BG'], t['ACCENT_3'], 10, 72)
    draw_text(draw, Box(1950, 645, 760, 105), 'PR COMMENT', t['ACCENT_3'], 62, True)
    draw_text(draw, Box(1950, 810, 760, 125), 'PASS / FAIL', t['TEXT'], 70, True)
    draw_text(draw, Box(1950, 980, 760, 70), 'visible where engineers work', t['TEXT_2'], 34, True)
    arrow(draw, (1580, 870), (1810, 870), t['MUTED'], 14)
    rect(draw, Box(770, 1380, 1660, 120), t['RED_BG'], t['WARN'], 7, 58)
    draw_text(draw, Box(830, 1405, 1540, 70), '$3-8/run: cheap enough for every risky PR', t['WARN'], 44, True)
    save(img, 'minimum_viable_eval.png')


def render_tool_name_translation(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'Tool Name Translation', 'Use SDK names in graders, not chat tool names.')
    left, right = Box(300, 520, 960, 920), Box(1940, 520, 960, 920)
    rect(draw, left, t['RED_BG'], t['WARN'], 10, 70)
    rect(draw, right, t['TEAL_BG'], t['SUCCESS'], 10, 70)
    draw_text(draw, Box(390, 610, 780, 90), 'WRONG COLUMN', t['WARN'], 56, True)
    draw_text(draw, Box(2030, 610, 780, 90), 'GRADER COLUMN', t['SUCCESS'], 56, True)
    pairs = [('execute', 'bash'), ('read', 'view'), ('search', 'grep'), ('editFile', 'edit'), ('createFile', 'create')]
    for i, (a, b) in enumerate(pairs):
        y = 800 + i * 115
        draw.text((470, y), a, fill=t['WARN'], font=font(52, True))
        draw.text((2180, y), b, fill=t['SUCCESS'], font=font(52, True))
        arrow(draw, (1300, y + 30), (1900, y + 30), t['MUTED'], 8)
    rect(draw, Box(1030, 1480, 1140, 145), t['LIGHT_BG'], t['ACCENT'], 6, 58)
    draw_text(draw, Box(1090, 1512, 1020, 82), 'expect_tools: "bash|view|edit|create"', t['ACCENT'], 40, True)
    save(img, 'tool_name_translation.png')


def render_grading_decision_tree(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'Grading Decision Tree', 'Pick the cheapest grader that catches the failure.')
    nodes = [
        (Box(280, 470, 780, 260), 'TEXT?', 'keywords / refusal', t['ACCENT'], t['BLUE_BG']),
        (Box(1210, 770, 780, 260), 'TOOLS?', 'called / not called', t['ACCENT_2'], t['TEAL_BG']),
        (Box(2140, 1070, 780, 260), 'JUDGMENT?', 'multi-criterion behavior', t['WARN'], t['RED_BG']),
    ]
    results = [
        (Box(430, 1060, 560, 190), 'text', '$0 instant', t['ACCENT']),
        (Box(1360, 1360, 560, 190), 'tool_constraint', '$0 instant', t['ACCENT_2']),
        (Box(2290, 1370, 560, 190), 'prompt', '$$ judge', t['WARN']),
    ]
    for box, q, sub, color, bg in nodes:
        rect(draw, box, bg, color, 9, 64)
        draw_text(draw, Box(box.x + 55, box.y + 52, box.w - 110, 80), q, color, 62, True)
        draw_text(draw, Box(box.x + 65, box.y + 150, box.w - 130, 64), sub, t['TEXT'], 36, True)
    for box, name, cost, color in results:
        rect(draw, box, t['LIGHT_BG'], color, 7, 50)
        draw_text(draw, Box(box.x + 45, box.y + 35, box.w - 90, 62), name, color, 42, True, max_lines=1)
        draw_text(draw, Box(box.x + 45, box.y + 105, box.w - 90, 50), cost, t['TEXT'], 32, True, max_lines=1)
    arrow(draw, (1060, 600), (1210, 860), t['MUTED'], 10)
    arrow(draw, (1990, 900), (2140, 1160), t['MUTED'], 10)
    arrow(draw, (670, 730), (680, 1060), t['ACCENT'], 10)
    arrow(draw, (1600, 1030), (1610, 1360), t['ACCENT_2'], 10)
    arrow(draw, (2530, 1330), (2540, 1370), t['WARN'], 10)
    pill(draw, Box(650, 900, 145, 68), 'YES', t['ACCENT'])
    pill(draw, Box(1580, 1200, 145, 68), 'YES', t['ACCENT_2'])
    pill(draw, Box(2510, 1305, 145, 68), 'YES', t['WARN'])
    save(img, 'grading_decision_tree.png')


def render_binary_vs_score(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'Binary Grading Beats Score Ambiguity', 'CI needs merge/no-merge, not a debate over 3.7 out of 5.')
    rect(draw, Box(180, 470, 1320, 840), t['RED_BG'], t['WARN'], 9, 70)
    rect(draw, Box(1700, 470, 1320, 840), t['TEAL_BG'], t['SUCCESS'], 9, 70)
    draw_text(draw, Box(280, 570, 1120, 90), 'SCORE', t['WARN'], 58, True)
    draw_text(draw, Box(280, 735, 1120, 160), '3.7 / 5', t['WARN'], 118, True)
    draw_text(draw, Box(280, 990, 1120, 110), 'Ship? Block? Change threshold?', t['TEXT'], 46, True)
    draw_text(draw, Box(1800, 570, 1120, 90), 'BINARY', t['SUCCESS'], 58, True)
    draw_text(draw, Box(1800, 735, 1120, 160), 'FAIL', t['WARN'], 122, True)
    draw_text(draw, Box(1800, 990, 1120, 110), 'Missing step-1 gate. Block merge.', t['TEXT'], 46, True)
    rect(draw, Box(790, 1490, 1620, 130), t['LIGHT_BG'], t['ACCENT'], 6, 58)
    draw_text(draw, Box(850, 1518, 1500, 80), 'Binary = reproducible + actionable + CI-native', t['ACCENT'], 44, True)
    save(img, 'binary_vs_score_grading.png')


def render_task_pattern_matrix(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'The Four Task Patterns', 'A behavioral contract matrix for agent eval design.')
    x0, y0, cw, ch = 520, 470, 1040, 480
    cells = [
        (0, 0, 'Happy path', 'Should act', t['SUCCESS'], t['TEAL_BG']),
        (1, 0, 'Safety gate', 'Refuse until confirmed', t['WARN'], t['RED_BG']),
        (0, 1, 'Invalid zone', 'Off-topic action', t['MUTED'], t['LIGHT_BG']),
        (1, 1, 'Sourdough', 'Off-topic refusal', t['ACCENT'], t['BLUE_BG']),
    ]
    draw_text(draw, Box(x0, 335, cw, 70), 'SHOULD ACT', t['TEXT'], 40, True)
    draw_text(draw, Box(x0 + cw, 335, cw, 70), 'SHOULD REFUSE', t['TEXT'], 40, True)
    draw_text(draw, Box(170, y0 + 160, 300, 90), 'ON-TOPIC', t['TEXT'], 38, True)
    draw_text(draw, Box(170, y0 + ch + 160, 300, 90), 'OFF-TOPIC', t['TEXT'], 38, True)
    for col, row, label, sub, color, bg in cells:
        box = Box(x0 + col * cw, y0 + row * ch, cw - 36, ch - 36)
        rect(draw, box, bg, color, 8, 56)
        draw_text(draw, Box(box.x + 80, box.y + 100, box.w - 160, 90), label, color, 58, True)
        draw_text(draw, Box(box.x + 100, box.y + 225, box.w - 200, 90), sub, t['TEXT'], 38, True)
    save(img, 'task_pattern_matrix.png')


def render_eval_pipeline_flow(t: dict[str, str]) -> None:
    img, draw = canvas(t, 3200, 1650)
    draw_text(draw, Box(170, 70, 2860, 96), 'PR to PR Comment', t['TEXT'], 72, True, max_lines=1)
    draw_text(draw, Box(520, 175, 2160, 70), 'Eight stages, one automated safety signal.', t['TEXT_2'], 38, True, max_lines=1)
    stages = ['PR', 'Filter', 'Discover', 'Sync', 'Budget', 'Session', 'Grade', 'Comment']
    y_positions = [470, 710, 950, 710, 470, 710, 950, 710]
    for i, stage in enumerate(stages):
        x = 145 + i * 370
        color = [t['ACCENT'], t['ACCENT_2'], t['ACCENT_3'], t['WARN']][i % 4]
        bg = [t['BLUE_BG'], t['TEAL_BG'], t['PURPLE_BG'], t['RED_BG']][i % 4]
        box = Box(x, y_positions[i], 285, 205)
        rect(draw, box, bg, color, 8, 48)
        draw_text(draw, Box(x + 30, y_positions[i] + 50, 225, 85), stage, color, 40, True, max_lines=1)
        if i < len(stages) - 1:
            arrow(draw, (x + 295, y_positions[i] + 102), (x + 360, y_positions[i + 1] + 102), t['MUTED'], 8)
    rect(draw, Box(570, 1290, 2060, 150), t['LIGHT_BG'], t['ACCENT'], 6, 62)
    draw_text(draw, Box(635, 1323, 1930, 84), '15-25 min | $3-8/run | PR comment is the safety surface', t['ACCENT'], 44, True)
    save(img, 'eval_pipeline_flow.png')


def render_regression_timeline(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'Three Regressions Caught', 'Trigger, detection, and prevented impact in one CI loop.')
    items = [('Model bump', '3 sourdough fails', 'Persona drift'), ('Agent edit', '0 tool calls', 'Fabrication'), ('Deploy prompt', '>3 tools', 'Gate skip')]
    for i, (trigger, signal, impact) in enumerate(items):
        x = 360 + i * 900
        draw.ellipse([x, 620, x + 220, 840], fill=[t['ACCENT'], t['ACCENT_2'], t['WARN']][i])
        draw_text(draw, Box(x, 675, 220, 90), str(i + 1), '#ffffff', 64, True)
        rect(draw, Box(x - 180, 960, 580, 360), [t['BLUE_BG'], t['TEAL_BG'], t['RED_BG']][i], [t['ACCENT'], t['ACCENT_2'], t['WARN']][i], 8, 58)
        draw_text(draw, Box(x - 120, 1015, 460, 70), trigger, [t['ACCENT'], t['ACCENT_2'], t['WARN']][i], 42, True)
        draw_text(draw, Box(x - 120, 1120, 460, 70), signal, t['TEXT'], 38, True)
        draw_text(draw, Box(x - 120, 1215, 460, 60), impact, t['TEXT_2'], 34, True)
        if i < 2:
            arrow(draw, (x + 240, 730), (x + 710, 730), t['MUTED'], 10)
    draw_text(draw, Box(620, 1510, 1960, 100), 'CI caught the behavior before the agent reached production.', t['TEXT'], 48, True)
    save(img, 'regression_timeline.png')


def render_eval_cost_comparison(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'Eval Cost vs Failure Cost', '$3-8 per run is cheap insurance for autonomous agents.')
    axis_x, axis_y = 420, 990
    draw.line([axis_x, axis_y, 2820, axis_y], fill=t['GRID'], width=10)
    draw.rounded_rectangle([axis_x, 760, axis_x + 430, 990], radius=40, fill=t['TEAL_BG'], outline=t['SUCCESS'], width=8)
    draw.rounded_rectangle([axis_x + 620, 520, 2820, 990], radius=58, fill=t['RED_BG'], outline=t['WARN'], width=10)
    draw_text(draw, Box(axis_x + 45, 800, 340, 70), 'Eval run', t['SUCCESS'], 38, True)
    draw_text(draw, Box(axis_x + 45, 875, 340, 85), '$3-8', t['SUCCESS'], 62, True)
    draw_text(draw, Box(axis_x + 820, 640, 1300, 125), 'Failed agent loop', t['WARN'], 58, True)
    draw_text(draw, Box(axis_x + 830, 790, 1280, 130), '$47K', t['WARN'], 118, True)
    rect(draw, Box(1040, 1110, 1120, 130), t['PURPLE_BG'], t['ACCENT_3'], 7, 58)
    draw_text(draw, Box(1100, 1138, 1000, 76), 'Cost gap is the argument for CI evals', t['ACCENT_3'], 40, True)
    draw_text(draw, Box(620, 1390, 1960, 95), 'Run evals where the blast radius is bigger than the token bill.', t['TEXT'], 44, True)
    save(img, 'eval_cost_comparison.png')


def render_four_week_playbook(t: dict[str, str]) -> None:
    img, draw = canvas(t, W, 1650)
    title(draw, t, 'The 4-Week Playbook', 'From first task to CI-integrated agent safety gates.')
    weeks = [('1', 'Inventory risks'), ('2', 'Two tasks/agent'), ('3', 'Add safety gates'), ('4', 'Wire PR CI')]
    for i, (num, label) in enumerate(weeks):
        x = 430 + i * 560
        y = 470 + i * 170
        color = [t['ACCENT'], t['ACCENT_2'], t['ACCENT_3'], t['SUCCESS']][i]
        bg = [t['BLUE_BG'], t['TEAL_BG'], t['PURPLE_BG'], t['TEAL_BG']][i]
        draw.polygon([(x, y), (x + 470, y), (x + 560, y + 150), (x + 90, y + 150)], fill=bg, outline=color)
        draw.line([(x, y), (x + 470, y), (x + 560, y + 150), (x + 90, y + 150), (x, y)], fill=color, width=8)
        draw_text(draw, Box(x + 85, y + 30, 170, 70), f'W{num}', color, 52, True)
        draw_text(draw, Box(x + 250, y + 38, 260, 65), label, t['TEXT'], 34, True)
    rect(draw, Box(705, 1325, 1790, 130), t['LIGHT_BG'], t['ACCENT'], 6, 58)
    draw_text(draw, Box(765, 1353, 1670, 76), 'Do not start with 38 tasks. Start with the riskiest two.', t['ACCENT'], 42, True)
    save(img, 'four_week_playbook.png')


def render_all() -> None:
    renderers: list[tuple[Callable[[dict[str, str]], None], str]] = [
        (render_fabrication_vs_reality, 'default'),
        (render_benchmark_gap, 'ocean'),
        (render_agent_credential_evolution, 'sunset'),
        (render_failure_taxonomy, 'midnight'),
        (render_sourdough_test, 'forest'),
        (render_minimum_viable_eval, 'default'),
        (render_tool_name_translation, 'sunset'),
        (render_grading_decision_tree, 'ocean'),
        (render_binary_vs_score, 'forest'),
        (render_task_pattern_matrix, 'midnight'),
        (render_eval_pipeline_flow, 'default'),
        (render_regression_timeline, 'sunset'),
        (render_eval_cost_comparison, 'forest'),
        (render_four_week_playbook, 'midnight'),
    ]
    print(f'Rendering {len(renderers)} AI agent eval visuals...')
    for fn, theme in renderers:
        fn(tok(theme))
    print(f'Done. {len(renderers)} PNGs written to {OUT}/')


if __name__ == '__main__':
    render_all()
