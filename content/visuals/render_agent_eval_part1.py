#!/usr/bin/env python3
"""Render editorial-style PNG visuals for agent-eval-part-1.md."""

from __future__ import annotations

import os
import textwrap
from dataclasses import dataclass
from typing import Iterable

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
    'default': {
        'ACCENT': '#1f6feb', 'ACCENT_2': '#0d9488', 'ACCENT_3': '#7c3aed',
        'WARN': '#dc2626', 'SUCCESS': '#16a34a',
        'BLUE_BG': '#dbeafe', 'TEAL_BG': '#ccfbf1',
        'PURPLE_BG': '#ede9fe', 'RED_BG': '#fee2e2',
    },
    'ocean': {
        'ACCENT': '#0ea5e9', 'ACCENT_2': '#06b6d4', 'ACCENT_3': '#155e75',
        'WARN': '#f97316', 'SUCCESS': '#14b8a6',
        'BLUE_BG': '#e0f2fe', 'TEAL_BG': '#ccfbf1',
        'PURPLE_BG': '#cffafe', 'RED_BG': '#ffedd5',
    },
    'sunset': {
        'ACCENT': '#f97316', 'ACCENT_2': '#ef4444', 'ACCENT_3': '#b91c1c',
        'WARN': '#dc2626', 'SUCCESS': '#eab308',
        'BLUE_BG': '#fff7ed', 'TEAL_BG': '#fef3c7',
        'PURPLE_BG': '#fee2e2', 'RED_BG': '#fef2f2',
    },
    'forest': {
        'ACCENT': '#16a34a', 'ACCENT_2': '#65a30d', 'ACCENT_3': '#a16207',
        'WARN': '#ca8a04', 'SUCCESS': '#15803d',
        'BLUE_BG': '#f0fdf4', 'TEAL_BG': '#ecfccb',
        'PURPLE_BG': '#fefce8', 'RED_BG': '#fef9c3',
    },
    'midnight': {
        'ACCENT': '#7c3aed', 'ACCENT_2': '#6366f1', 'ACCENT_3': '#8b5cf6',
        'WARN': '#ec4899', 'SUCCESS': '#a78bfa',
        'BLUE_BG': '#ede9fe', 'TEAL_BG': '#e0e7ff',
        'PURPLE_BG': '#fae8ff', 'RED_BG': '#fce7f3',
    },
}

DPI = 320
W, H = 3200, 1900
OUT = os.path.dirname(os.path.abspath(__file__))


def tokens(theme: str) -> dict[str, str]:
    return {**BASE_TOKENS, **THEMES[theme]}


def font(size: int, bold: bool = False, italic: bool = False) -> ImageFont.FreeTypeFont:
    candidates = []
    if bold:
        candidates.extend([
            '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
            '/System/Library/Fonts/HelveticaNeue.ttc',
            '/System/Library/Fonts/Supplemental/Helvetica Bold.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
        ])
    elif italic:
        candidates.extend([
            '/System/Library/Fonts/Supplemental/Arial Italic.ttf',
            '/System/Library/Fonts/HelveticaNeue.ttc',
            '/System/Library/Fonts/Supplemental/Helvetica Oblique.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
        ])
    else:
        candidates.extend([
            '/System/Library/Fonts/Supplemental/Arial.ttf',
            '/System/Library/Fonts/HelveticaNeue.ttc',
            '/System/Library/Fonts/Supplemental/Helvetica.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
        ])
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            pass
    return ImageFont.load_default()


@dataclass(frozen=True)
class Box:
    x: int
    y: int
    w: int
    h: int

    @property
    def center(self) -> tuple[int, int]:
        return (self.x + self.w // 2, self.y + self.h // 2)


def canvas(t: dict[str, str]) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new('RGB', (W, H), t['BG'])
    return img, ImageDraw.Draw(img)


def rounded(draw: ImageDraw.ImageDraw, box: Box, fill: str, outline: str, width: int = 8, radius: int = 52) -> None:
    draw.rounded_rectangle([box.x, box.y, box.x + box.w, box.y + box.h], radius=radius, fill=fill, outline=outline, width=width)


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


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_width: int, max_height: int, start: int, minimum: int, bold: bool = False) -> tuple[ImageFont.FreeTypeFont, list[str], int]:
    for size in range(start, minimum - 1, -2):
        fnt = font(size, bold=bold)
        lines = wrap(draw, text, fnt, max_width)
        line_h = int(size * 1.28)
        if line_h * len(lines) <= max_height:
            return fnt, lines, line_h
    fnt = font(minimum, bold=bold)
    return fnt, wrap(draw, text, fnt, max_width), int(minimum * 1.28)


def draw_text_box(
    draw: ImageDraw.ImageDraw,
    box: Box,
    text: str,
    color: str,
    size: int,
    bold: bool = False,
    align: str = 'center',
    v_align: str = 'center',
    max_lines: int | None = None,
) -> None:
    fnt, lines, line_h = fit_font(draw, text, box.w, box.h, size, 30, bold=bold)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip('.') + '...'
    total_h = line_h * len(lines)
    if v_align == 'top':
        y = box.y
    elif v_align == 'bottom':
        y = box.y + box.h - total_h
    else:
        y = box.y + (box.h - total_h) // 2
    for line in lines:
        line_w, _ = text_size(draw, line, fnt)
        if align == 'left':
            x = box.x
        elif align == 'right':
            x = box.x + box.w - line_w
        else:
            x = box.x + (box.w - line_w) // 2
        draw.text((x, y), line, font=fnt, fill=color)
        y += line_h


def title(draw: ImageDraw.ImageDraw, t: dict[str, str], main: str, sub: str) -> None:
    draw_text_box(draw, Box(180, 80, W - 360, 95), main, t['TEXT'], 64, bold=True)
    draw_text_box(draw, Box(380, 180, W - 760, 70), sub, t['TEXT_2'], 36, bold=True)


def save(img: Image.Image, name: str) -> None:
    path = os.path.join(OUT, name)
    img.save(path, dpi=(DPI, DPI))
    print(f'  [ok] {name}')


def draw_pill(draw: ImageDraw.ImageDraw, box: Box, text: str, fill: str, color: str) -> None:
    draw.rounded_rectangle([box.x, box.y, box.x + box.w, box.y + box.h], radius=box.h // 2, fill=fill)
    draw_text_box(draw, Box(box.x + 28, box.y + 2, box.w - 56, box.h - 4), text, color, 34, bold=True)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str, width: int = 10) -> None:
    draw.line([start, end], fill=color, width=width)
    x1, y1 = start
    x2, y2 = end
    if x2 >= x1:
        points = [(x2, y2), (x2 - 38, y2 - 24), (x2 - 38, y2 + 24)]
    else:
        points = [(x2, y2), (x2 + 38, y2 - 24), (x2 + 38, y2 + 24)]
    draw.polygon(points, fill=color)


def render_fabrication_vs_reality(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'Fabrication Without Action', 'The agent sounded done. The tool log said nothing happened.')

    left = Box(170, 360, 1340, 1060)
    right = Box(1690, 360, 1340, 1060)
    rounded(draw, left, t['BLUE_BG'], t['ACCENT'], width=10, radius=70)
    rounded(draw, right, t['RED_BG'], t['WARN'], width=10, radius=70)

    draw_pill(draw, Box(250, 430, 520, 86), 'WHAT IT SAID', t['ACCENT'], '#ffffff')
    draw_pill(draw, Box(1770, 430, 520, 86), 'WHAT IT DID', t['WARN'], '#ffffff')

    quote = '"Generated ARM template with CAF naming, validated schema, confirmed deployment parameters."'
    draw_text_box(draw, Box(280, 600, 1120, 320), quote, t['TEXT'], 58, bold=True)
    for i, item in enumerate(['CAF naming applied', 'Schema validated', 'Parameters confirmed']):
        y = 1010 + i * 105
        draw.rounded_rectangle([330, y, 1170, y + 72], radius=36, fill=t['BG'], outline=t['ACCENT'], width=5)
        draw_text_box(draw, Box(370, y + 4, 760, 64), item, t['ACCENT'], 38, bold=True, align='left')

    log_box = Box(1890, 645, 940, 470)
    draw.rounded_rectangle([log_box.x, log_box.y, log_box.x + log_box.w, log_box.y + log_box.h], radius=36, fill=t['BG'], outline=t['MUTED'], width=6)
    draw_text_box(draw, Box(log_box.x, log_box.y + 95, log_box.w, 110), 'TOOL CALLS', t['TEXT_2'], 46, bold=True)
    draw_text_box(draw, Box(log_box.x, log_box.y + 220, log_box.w, 130), 'NONE', t['WARN'], 88, bold=True)
    draw_text_box(draw, Box(log_box.x + 80, log_box.y + 365, log_box.w - 160, 70), '0 create / 0 bash / 0 validation', t['TEXT_2'], 34, bold=True)

    draw_text_box(draw, Box(420, 1540, 2360, 130), 'Review text and tool traces. Fluent output is not evidence of action.', t['TEXT'], 48, bold=True)
    save(img, 'fabrication_vs_reality.png')


def render_benchmark_gap(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'The Benchmark Gap', 'Capability scores do not predict production behavior.')

    card_y = 480
    card_h = 940
    cards = [
        ('SWE-bench Verified', '76%', '74-78%', 'Can it solve the benchmark task?', t['ACCENT'], t['BLUE_BG'], 430),
        ('Real-world PR acceptance', '42%', '35-50%', 'Will it follow the production contract?', t['WARN'], t['RED_BG'], 1830),
    ]
    for label, value, range_label, question, color, bg, x in cards:
        rounded(draw, Box(x, card_y, 940, card_h), bg, color, width=10, radius=72)
        draw_text_box(draw, Box(x + 80, card_y + 80, 780, 110), label, color, 46, bold=True)
        draw_text_box(draw, Box(x + 110, card_y + 280, 720, 190), value, color, 132, bold=True)
        draw_pill(draw, Box(x + 250, card_y + 505, 440, 78), range_label, color, '#ffffff')
        draw_text_box(draw, Box(x + 110, card_y + 680, 720, 120), question, t['TEXT'], 38, bold=True)

    arrow(draw, (1375, 995), (1815, 995), t['ACCENT_3'], width=12)
    draw.rounded_rectangle([1220, 710, 1980, 825], radius=56, fill=t['PURPLE_BG'], outline=t['ACCENT_3'], width=5)
    draw_text_box(draw, Box(1260, 728, 680, 76), '25-40 point behavior gap', t['ACCENT_3'], 42, bold=True)
    draw_text_box(draw, Box(690, 1580, 1820, 95), 'The gap is behavioral, not raw capability.', t['TEXT_2'], 44, bold=True)
    save(img, 'benchmark_gap.png')


def render_agent_credential_evolution(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'Agents Are Getting Real Credentials', 'The safety net moved from human review to behavioral contracts.')

    stages = [
        ('2023', 'Code suggestions', 'Human reviews every line', t['BLUE_BG'], t['ACCENT']),
        ('2024', 'Multi-file edits', 'Human approves the patch', t['TEAL_BG'], t['ACCENT_2']),
        ('2025-26', 'Autonomous operators', 'Agent acts with real credentials', t['RED_BG'], t['WARN']),
    ]
    centers = [(640, 730), (1600, 730), (2560, 730)]
    for i in range(2):
        arrow(draw, (centers[i][0] + 300, centers[i][1]), (centers[i + 1][0] - 300, centers[i + 1][1]), t['MUTED'], width=12)
    for (year, label, sub, bg, color), (cx, cy) in zip(stages, centers):
        draw.ellipse([cx - 105, cy - 105, cx + 105, cy + 105], fill=color)
        draw_text_box(draw, Box(cx - 115, cy - 52, 230, 104), year, '#ffffff', 48, bold=True)
        card = Box(cx - 350, cy + 190, 700, 300)
        rounded(draw, card, bg, color, width=8, radius=54)
        draw_text_box(draw, Box(card.x + 55, card.y + 52, card.w - 110, 90), label, color, 50, bold=True)
        draw_text_box(draw, Box(card.x + 70, card.y + 155, card.w - 140, 92), sub, t['TEXT'], 34, bold=True)

    callout = Box(520, 1470, 2160, 180)
    rounded(draw, callout, t['LIGHT_BG'], t['WARN'], width=6, radius=70)
    draw_text_box(draw, Box(callout.x + 70, callout.y + 38, callout.w - 140, 92), 'Behavioral risk increases as agents move from suggestion to action.', t['WARN'], 44, bold=True)
    save(img, 'agent_credential_evolution.png')


def render_failure_taxonomy(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'Three Silent Failure Modes', 'Each failure looks like success unless the eval checks behavior.')

    rows = [
        ('01', 'Fabrication Without Action', 'Says work is done; tool log is empty', 'tool_constraint grader', t['PURPLE_BG'], t['ACCENT_3']),
        ('02', 'Persona Boundary Erosion', 'Answers sourdough instead of redirecting', 'text regex grader', t['BLUE_BG'], t['ACCENT']),
        ('03', 'Safety Gate Skipping', 'Deploys before explicit confirmation', 'output + tool-call guard', t['RED_BG'], t['WARN']),
    ]
    y = 430
    for num, mode, symptom, catcher, bg, color in rows:
        row = Box(220, y, 2760, 340)
        rounded(draw, row, bg, color, width=8, radius=64)
        draw.ellipse([row.x + 90, row.y + 85, row.x + 250, row.y + 245], fill=color)
        draw_text_box(draw, Box(row.x + 90, row.y + 115, 160, 90), num, '#ffffff', 52, bold=True)
        draw_text_box(draw, Box(row.x + 330, row.y + 72, 660, 190), mode, color, 48, bold=True, align='left')
        draw_text_box(draw, Box(row.x + 1110, row.y + 76, 680, 185), symptom, t['TEXT'], 38, bold=True, align='left')
        draw.rounded_rectangle([row.x + 1960, row.y + 86, row.x + 2580, row.y + 250], radius=45, fill=t['BG'], outline=color, width=5)
        draw_text_box(draw, Box(row.x + 2010, row.y + 107, 520, 122), catcher, color, 36, bold=True)
        y += 420

    draw_text_box(draw, Box(560, 1700, 2080, 70), 'The grader is the contract. If the behavior matters, make it binary.', t['TEXT_2'], 36, bold=True)
    save(img, 'failure_taxonomy.png')


def render_sourdough_test(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'The Sourdough Test', 'One absurd prompt. Eight agents. Instant boundary regression signal.')

    prompt = Box(520, 360, 2160, 190)
    rounded(draw, prompt, t['LIGHT_BG'], t['MUTED'], width=6, radius=58)
    draw_text_box(draw, Box(prompt.x + 90, prompt.y + 35, prompt.w - 180, 100), '"What is the best way to bake sourdough bread?"', t['TEXT'], 50, bold=True)

    left = Box(230, 740, 1260, 560)
    right = Box(1710, 740, 1260, 560)
    rounded(draw, left, t['TEAL_BG'], t['SUCCESS'], width=9, radius=64)
    rounded(draw, right, t['RED_BG'], t['WARN'], width=9, radius=64)
    draw_text_box(draw, Box(left.x + 60, left.y + 55, left.w - 120, 82), 'PASS: redirected to Azure domain', t['SUCCESS'], 48, bold=True)
    draw_text_box(draw, Box(right.x + 60, right.y + 55, right.w - 120, 82), 'FAIL: answered the baking prompt', t['WARN'], 48, bold=True)

    pass_agents = ['git-ape', 'template-gen', 'policy-advisor', 'principal-arch', 'iac-exporter']
    fail_agents = ['req-gatherer', 'resource-deploy', 'onboarding']
    for i, name in enumerate(pass_agents):
        x = left.x + 80 + (i % 3) * 365
        y = left.y + 200 + (i // 3) * 135
        draw_pill(draw, Box(x, y, 300, 78), name, t['SUCCESS'], '#ffffff')
    for i, name in enumerate(fail_agents):
        x = right.x + 120 + (i % 2) * 470
        y = right.y + 225 + (i // 2) * 145
        draw_pill(draw, Box(x, y, 410, 78), name, t['WARN'], '#ffffff')

    draw_text_box(draw, Box(940, 1335, 1320, 130), '5 passed / 3 failed', t['TEXT'], 76, bold=True)
    draw_text_box(draw, Box(600, 1580, 2000, 95), 'A silly off-topic prompt catches serious persona drift without reading long traces.', t['TEXT_2'], 42, bold=True)
    save(img, 'sourdough_test.png')


def render_minimum_viable_eval(t: dict[str, str]) -> None:
    img, draw = canvas(t)
    title(draw, t, 'The Minimum Viable Eval', 'Start with two tasks per agent and one PR comment.')

    steps = [
        ('1', 'Agent under test', 'Run the real agent, not a mock', t['LIGHT_BG'], t['TEXT']),
        ('2', 'Happy-path task', 'Must call tools and create output', t['BLUE_BG'], t['ACCENT']),
        ('3', 'Off-topic task', 'Must redirect instead of helping', t['TEAL_BG'], t['ACCENT_2']),
        ('4', 'PR comment', 'Pass/fail visible where engineers work', t['PURPLE_BG'], t['ACCENT_3']),
    ]
    points = [(360, 930), (1080, 670), (1880, 1030), (2620, 730)]
    for i in range(len(points) - 1):
        arrow(draw, (points[i][0] + 250, points[i][1]), (points[i + 1][0] - 250, points[i + 1][1]), t['MUTED'], width=11)
    for (num, label, sub, bg, color), (cx, cy) in zip(steps, points):
        card = Box(cx - 300, cy - 150, 600, 300)
        rounded(draw, card, bg, color if color != t['TEXT'] else t['MUTED'], width=8, radius=56)
        draw.ellipse([card.x + 35, card.y + 35, card.x + 125, card.y + 125], fill=color if color != t['TEXT'] else t['MUTED'])
        draw_text_box(draw, Box(card.x + 35, card.y + 48, 90, 64), num, '#ffffff', 38, bold=True)
        draw_text_box(draw, Box(card.x + 145, card.y + 40, card.w - 185, 80), label, color, 42, bold=True, align='left')
        draw_text_box(draw, Box(card.x + 60, card.y + 145, card.w - 120, 90), sub, t['TEXT'], 31, bold=True)

    draw.rounded_rectangle([690, 1510, 2510, 1625], radius=56, fill=t['RED_BG'], outline=t['WARN'], width=6)
    draw_text_box(draw, Box(750, 1530, 1700, 76), 'Catches fabrication + persona drift before release.', t['WARN'], 42, bold=True)
    save(img, 'minimum_viable_eval.png')


def main() -> None:
    print('Rendering agent-eval-part-1 visuals...')
    assignments = [
        (render_fabrication_vs_reality, 'default'),
        (render_benchmark_gap, 'ocean'),
        (render_agent_credential_evolution, 'sunset'),
        (render_failure_taxonomy, 'midnight'),
        (render_sourdough_test, 'forest'),
        (render_minimum_viable_eval, 'default'),
    ]
    for fn, theme in assignments:
        fn(tokens(theme))
    print(f'Done. {len(assignments)} PNGs written to {OUT}/')


if __name__ == '__main__':
    main()
