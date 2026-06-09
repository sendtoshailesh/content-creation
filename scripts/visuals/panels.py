"""Layout primitives for panel-based visuals."""

from __future__ import annotations

from dataclasses import dataclass

from PIL import ImageDraw


@dataclass(frozen=True)
class Box:
    x: int
    y: int
    width: int
    height: int

    @property
    def xyxy(self) -> tuple[int, int, int, int]:
        return (self.x, self.y, self.x + self.width, self.y + self.height)

    def inset(self, padding: int) -> "Box":
        return Box(
            self.x + padding,
            self.y + padding,
            self.width - 2 * padding,
            self.height - 2 * padding,
        )


def grid_boxes(
    width: int,
    height: int,
    rows: int,
    cols: int,
    margin: int = 80,
    gap: int = 32,
) -> list[Box]:
    """Return evenly spaced panel boxes."""
    usable_width = width - 2 * margin - (cols - 1) * gap
    usable_height = height - 2 * margin - (rows - 1) * gap
    cell_width = usable_width // cols
    cell_height = usable_height // rows
    boxes: list[Box] = []
    for row in range(rows):
        for col in range(cols):
            boxes.append(
                Box(
                    margin + col * (cell_width + gap),
                    margin + row * (cell_height + gap),
                    cell_width,
                    cell_height,
                )
            )
    return boxes


def rounded_panel(
    draw: ImageDraw.ImageDraw,
    box: Box,
    fill: str,
    outline: str,
    radius: int = 28,
    width: int = 4,
) -> None:
    """Draw a rounded panel."""
    draw.rounded_rectangle(box.xyxy, radius=radius, fill=fill, outline=outline, width=width)

