"""SVG-first design system for infographic assets.

Why SVG instead of hand-drawn Pillow primitives:
- Typography is governed by a fixed TYPE_SCALE, so text never ends up wildly
  uneven (the old renderers mixed 11px and 138px in the same asset).
- Arrows use a shared SVG <marker>, so arrowheads are always crisp and never
  distorted, and connectors snap to box-edge anchors so they line up with boxes.
- Connectors use a strong token color (never a faded gray), preserving the
  transition meaning between boxes.
- No internal numbering/labels (e.g. "02 / 10", "EXHIBIT 1") are emitted; those
  carried no reader value and were called out as noise.

Render with Chromium (via render.py) for production output; the SVG DOM is also
what the Playwright inspector (inspect.py) measures for automated QA.
"""

from __future__ import annotations

import html
from dataclasses import dataclass, field

from scripts.visuals.tokens import BASE_TOKENS, THEMES

# Fixed type scale. Every text element MUST use one of these roles. Sibling
# elements that play the same role (e.g. all box labels) use the same size, so
# text reads uniform within and across boxes.
TYPE_SCALE = {
    "display": 92,   # one hero number per asset, used sparingly
    "title": 50,
    "subtitle": 30,
    "value": 40,     # the numeric/headline value inside a box
    "body": 24,
    "label": 23,     # box labels — identical across sibling boxes
    "caption": 18,   # source / footnote line
}

FONT_STACK = "Helvetica Neue, Helvetica, Arial, sans-serif"


def tokens(theme: str = "default") -> dict[str, str]:
    return {**BASE_TOKENS, **THEMES[theme]}


def _esc(text: str) -> str:
    return html.escape(str(text), quote=True)


@dataclass
class Box:
    x: int
    y: int
    w: int
    h: int

    @property
    def cx(self) -> int:
        return self.x + self.w // 2

    @property
    def cy(self) -> int:
        return self.y + self.h // 2

    @property
    def right(self) -> int:
        return self.x + self.w

    @property
    def bottom(self) -> int:
        return self.y + self.h

    def anchor(self, side: str) -> tuple[int, int]:
        return {
            "left": (self.x, self.cy),
            "right": (self.right, self.cy),
            "top": (self.cx, self.y),
            "bottom": (self.cx, self.bottom),
            "center": (self.cx, self.cy),
        }[side]


@dataclass
class SVG:
    width: int
    height: int
    bg: str = "#ffffff"
    theme: str = "default"
    _els: list[str] = field(default_factory=list)
    _arrow_colors: set[str] = field(default_factory=set)

    @property
    def t(self) -> dict[str, str]:
        return tokens(self.theme)

    # --- primitives -------------------------------------------------------
    def rect(self, box: Box, fill: str, stroke: str | None = None, sw: int = 4, radius: int = 22) -> "SVG":
        s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self._els.append(
            f'<rect x="{box.x}" y="{box.y}" width="{box.w}" height="{box.h}" '
            f'rx="{radius}" ry="{radius}" fill="{fill}"{s}/>'
        )
        return self

    def circle(self, cx: int, cy: int, r: int, fill: str, stroke: str | None = None, sw: int = 4) -> "SVG":
        s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self._els.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}/>')
        return self

    def line(self, x1: int, y1: int, x2: int, y2: int, color: str, sw: int = 4) -> "SVG":
        self._els.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round"/>'
        )
        return self

    def text(self, x: int, y: int, content: str, role: str, color: str,
             anchor: str = "start", bold: bool = True, width: int | None = None,
             line_height: float = 1.18) -> "SVG":
        """Place text using a TYPE_SCALE role. Optional width wraps the text."""
        if role not in TYPE_SCALE:
            raise ValueError(f"text role must be one of {list(TYPE_SCALE)}, got {role!r}")
        size = TYPE_SCALE[role]
        weight = 700 if bold else 400
        if width is None:
            self._els.append(
                f'<text x="{x}" y="{y + size}" font-family="{FONT_STACK}" '
                f'font-size="{size}" font-weight="{weight}" fill="{color}" '
                f'data-role="{role}" text-anchor="{anchor}">{_esc(content)}</text>'
            )
            return self
        # naive width-based wrapping using an average glyph width estimate
        avg = size * 0.55
        max_chars = max(1, int(width / avg))
        words, lines, cur = content.split(), [], ""
        for w in words:
            trial = f"{cur} {w}".strip()
            if len(trial) <= max_chars:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        step = int(size * line_height)
        spans = "".join(
            f'<tspan x="{x}" dy="{0 if i == 0 else step}">{_esc(l)}</tspan>'
            for i, l in enumerate(lines)
        )
        self._els.append(
            f'<text x="{x}" y="{y + size}" font-family="{FONT_STACK}" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'data-role="{role}" text-anchor="{anchor}">{spans}</text>'
        )
        return self

    def arrow(self, a: tuple[int, int], b: tuple[int, int], color: str, sw: int = 6) -> "SVG":
        """Straight connector with a crisp marker arrowhead in a STRONG color."""
        self._arrow_colors.add(color)
        mid = self._marker_id(color)
        self._els.append(
            f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" '
            f'data-role="arrow" marker-end="url(#{mid})"/>'
        )
        return self

    def connect(self, box_a: Box, side_a: str, box_b: Box, side_b: str, color: str, sw: int = 6) -> "SVG":
        """Arrow from one box edge to another box edge — always aligned to boxes."""
        return self.arrow(box_a.anchor(side_a), box_b.anchor(side_b), color, sw)

    def raw(self, markup: str) -> "SVG":
        self._els.append(markup)
        return self

    # --- output -----------------------------------------------------------
    @staticmethod
    def _marker_id(color: str) -> str:
        return "arrow_" + color.lstrip("#")

    def _defs(self) -> str:
        markers = []
        for color in sorted(self._arrow_colors):
            mid = self._marker_id(color)
            markers.append(
                f'<marker id="{mid}" viewBox="0 0 12 12" refX="9" refY="6" '
                f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                f'<path d="M1,1 L11,6 L1,11 z" fill="{color}"/></marker>'
            )
        return f"<defs>{''.join(markers)}</defs>" if markers else ""

    def tostring(self) -> str:
        body = "".join(self._els)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" '
            f'height="{self.height}" viewBox="0 0 {self.width} {self.height}">'
            f'{self._defs()}'
            f'<rect width="{self.width}" height="{self.height}" fill="{self.bg}"/>'
            f'{body}</svg>'
        )
