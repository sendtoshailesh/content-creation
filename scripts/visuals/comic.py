"""Programmatic comic and storyboard primitives."""

from __future__ import annotations

from PIL import Image, ImageDraw

from .panels import Box, grid_boxes, rounded_panel
from .text_layout import draw_wrapped_text, load_font
from .tokens import PLATFORM_SIZES, get_tokens


def create_canvas(platform: str = "linkedin_card", theme: str = "default") -> tuple[Image.Image, ImageDraw.ImageDraw, dict[str, str]]:
    """Create a tokenized RGB canvas for a platform preset."""
    size = PLATFORM_SIZES[platform]
    tokens = get_tokens(theme)
    image = Image.new("RGB", size, tokens["BG"])
    return image, ImageDraw.Draw(image), tokens


def draw_simple_character(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    scale: int,
    tokens: dict[str, str],
    accent: str | None = None,
) -> None:
    """Draw a simple symbolic character without external imagery."""
    cx, cy = center
    color = accent or tokens["ACCENT"]
    head_r = scale // 4
    draw.ellipse((cx - head_r, cy - scale, cx + head_r, cy - scale + 2 * head_r), fill=tokens["BLUE_BG"], outline=color, width=4)
    draw.rounded_rectangle((cx - scale // 3, cy - scale // 2, cx + scale // 3, cy + scale // 2), radius=scale // 8, fill=tokens["LIGHT_BG"], outline=color, width=4)
    draw.line((cx - scale // 3, cy, cx - scale // 2, cy + scale // 3), fill=color, width=5)
    draw.line((cx + scale // 3, cy, cx + scale // 2, cy + scale // 3), fill=color, width=5)
    draw.line((cx - scale // 6, cy + scale // 2, cx - scale // 4, cy + scale), fill=color, width=5)
    draw.line((cx + scale // 6, cy + scale // 2, cx + scale // 4, cy + scale), fill=color, width=5)


def speech_bubble(
    draw: ImageDraw.ImageDraw,
    box: Box,
    text: str,
    tokens: dict[str, str],
    pointer: tuple[int, int] | None = None,
) -> None:
    """Draw a measured speech bubble."""
    rounded_panel(draw, box, fill=tokens["BG"], outline=tokens["MUTED"], radius=20, width=3)
    if pointer:
        px, py = pointer
        draw.polygon([(box.x + 40, box.y + box.height), (box.x + 85, box.y + box.height), (px, py)], fill=tokens["BG"], outline=tokens["MUTED"])
    font = load_font(28, bold=True)
    draw_wrapped_text(draw, (box.x + 24, box.y + 22), text, font, box.width - 48, tokens["TEXT"], line_gap=8)


def storyboard_panels(width: int, height: int, count: int) -> list[Box]:
    """Return a readable panel grid for 3, 4, or 6 panel storyboards."""
    if count == 3:
        return grid_boxes(width, height, rows=3, cols=1, margin=80, gap=32)
    if count == 4:
        return grid_boxes(width, height, rows=2, cols=2, margin=80, gap=32)
    if count == 6:
        return grid_boxes(width, height, rows=3, cols=2, margin=70, gap=28)
    raise ValueError("Supported storyboard panel counts: 3, 4, 6")

