"""Infographic helpers for one-pagers and social cards."""

from __future__ import annotations

from PIL import Image, ImageDraw

from .panels import Box, rounded_panel
from .text_layout import draw_wrapped_text, load_font
from .tokens import PLATFORM_SIZES, get_tokens


def create_infographic(platform: str = "blog_infographic", theme: str = "default") -> tuple[Image.Image, ImageDraw.ImageDraw, dict[str, str]]:
    """Create an infographic canvas."""
    width, height = PLATFORM_SIZES[platform]
    tokens = get_tokens(theme)
    image = Image.new("RGB", (width, height), tokens["BG"])
    return image, ImageDraw.Draw(image), tokens


def title_block(draw: ImageDraw.ImageDraw, title: str, subtitle: str, tokens: dict[str, str], width: int, y: int = 80) -> int:
    """Draw a large title and subtitle, returning the next y position."""
    title_font = load_font(74, bold=True)
    subtitle_font = load_font(36)
    y = draw_wrapped_text(draw, (100, y), title, title_font, width - 200, tokens["TEXT"], line_gap=12)
    return draw_wrapped_text(draw, (100, y + 18), subtitle, subtitle_font, width - 200, tokens["TEXT_2"], line_gap=8) + 24


def metric_card(
    draw: ImageDraw.ImageDraw,
    box: Box,
    value: str,
    label: str,
    tokens: dict[str, str],
    accent: str | None = None,
) -> None:
    """Draw a metric card with a hero value and concise label."""
    rounded_panel(draw, box, fill=tokens["LIGHT_BG"], outline=accent or tokens["ACCENT"], radius=28, width=4)
    value_font = load_font(58, bold=True)
    label_font = load_font(30)
    draw.text((box.x + 34, box.y + 32), value, font=value_font, fill=accent or tokens["ACCENT"])
    draw_wrapped_text(draw, (box.x + 34, box.y + 108), label, label_font, box.width - 68, tokens["TEXT"], line_gap=8)


def source_line(draw: ImageDraw.ImageDraw, text: str, tokens: dict[str, str], width: int, height: int) -> None:
    """Draw a visible source line at the bottom of an asset."""
    font = load_font(24)
    draw.text((80, height - 60), text, font=font, fill=tokens["TEXT_2"])

