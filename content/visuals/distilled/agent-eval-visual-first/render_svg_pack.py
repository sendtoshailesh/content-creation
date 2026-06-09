"""SVG-first rebuild of the AI Agent Evals key visuals.

Built on scripts.visuals.svg.design so that:
- text only uses the fixed TYPE_SCALE (uniform sizing),
- arrows use marker arrowheads in strong colors, snapped to box edges,
- no internal numbering / exhibit labels are emitted.

Validated by scripts.visuals.svg.inspect before rendering to PNG.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.visuals.svg.design import SVG, Box, tokens  # noqa: E402
from scripts.visuals.svg.inspect import inspect_files  # noqa: E402
from scripts.visuals.svg.render import render_many  # noqa: E402

OUT = Path(__file__).resolve().parent


def gauge(svg: SVG, cx: int, cy: int, r: int, value: float, color: str, track: str) -> None:
    import math

    svg.raw(
        f'<path d="M{cx - r},{cy} A{r},{r} 0 0 1 {cx + r},{cy}" fill="none" '
        f'stroke="{track}" stroke-width="22" stroke-linecap="round"/>'
    )
    end = math.radians(180 + 180 * value)
    ex, ey = cx + r * math.cos(end), cy + r * math.sin(end)
    large = 1 if value > 0.5 else 0
    svg.raw(
        f'<path d="M{cx - r},{cy} A{r},{r} 0 0 {large} {ex:.1f},{ey:.1f}" fill="none" '
        f'stroke="{color}" stroke-width="22" stroke-linecap="round"/>'
    )
    nx, ny = cx + (r - 26) * math.cos(end), cy + (r - 26) * math.sin(end)
    svg.line(cx, cy, int(nx), int(ny), tokens()["TEXT"], 6)
    svg.circle(cx, cy, 9, tokens()["TEXT"])


def exhibit_benchmark_gap() -> tuple[str, Path]:
    t = tokens("default")
    W, H = 1200, 627
    s = SVG(W, H, t["BG"], "default")
    s.text(60, 40, "Capability is not behavior", "title", t["TEXT"])
    s.text(62, 110, "A high benchmark score still leaves a production behavior gap.", "subtitle", t["TEXT_2"])

    left = Box(110, 250, 300, 210)
    right = Box(790, 250, 300, 210)
    s.rect(left, t["BLUE_BG"], t["ACCENT"], 5, 26)
    s.rect(right, t["RED_BG"], t["WARN"], 5, 26)
    gauge(s, left.cx, 360, 92, 0.76, t["ACCENT"], t["GRID"])
    gauge(s, right.cx, 360, 92, 0.42, t["WARN"], t["GRID"])
    s.text(left.cx, 372, "74-78%", "value", t["ACCENT"], anchor="middle")
    s.text(right.cx, 372, "35-50%", "value", t["WARN"], anchor="middle")
    s.text(left.cx, 470, "SWE-bench Verified", "label", t["TEXT"], anchor="middle")
    s.text(right.cx, 470, "real PR acceptance", "label", t["TEXT"], anchor="middle")

    gap = Box(470, 320, 260, 86)
    s.rect(gap, t["PURPLE_BG"], t["ACCENT_3"], 5, 18)
    s.text(gap.cx, 345, "BEHAVIOR GAP", "label", t["ACCENT_3"], anchor="middle")
    s.connect(left, "right", gap, "left", t["ACCENT_3"], 7)
    s.connect(gap, "right", right, "left", t["ACCENT_3"], 7)

    s.text(60, 560, "Sources: SWE-bench; Presenc May 2026 vendor snapshot", "caption", t["TEXT_2"])
    return s.tostring(), OUT / "exhibit-01-benchmark-gap.png"


def eval_pipeline_flow() -> tuple[str, Path]:
    t = tokens("ocean")
    W, H = 1080, 1080
    s = SVG(W, H, t["BG"], "ocean")
    s.text(70, 70, "The eval pipeline", "title", t["TEXT"])
    s.text(72, 140, "Tasks move through graders before any release ships.", "subtitle", t["TEXT_2"])

    stages = [
        ("tasks", "real workflows", t["ACCENT"], t["BLUE_BG"]),
        ("graders", "text + tool checks", t["ACCENT_2"], t["TEAL_BG"]),
        ("CI gate", "pass or block", t["WARN"], t["RED_BG"]),
        ("history", "drift over time", t["ACCENT_3"], t["PURPLE_BG"]),
    ]
    bx, bw, bh = 150, 780, 150
    boxes = []
    for i, (name, detail, color, fill) in enumerate(stages):
        b = Box(bx, 250 + i * 195, bw, bh)
        boxes.append((b, color))
        s.rect(b, fill, color, 5, 26)
        s.circle(b.x + 80, b.cy, 40, t["BG"], color, 5)
        s.text(b.x + 80, b.cy - 22, str(i + 1), "value", color, anchor="middle")
        s.text(b.x + 160, b.y + 38, name, "label", t["TEXT"])
        s.text(b.x + 160, b.y + 84, detail, "caption", t["TEXT_2"])
    for i in range(len(boxes) - 1):
        s.connect(boxes[i][0], "bottom", boxes[i + 1][0], "top", t["ACCENT"], 7)

    s.text(70, 1010, "Source: First-party AI Agent Evals implementation pattern", "caption", t["TEXT_2"])
    return s.tostring(), OUT / "one-page-eval-system.png"


ASSETS = [exhibit_benchmark_gap, eval_pipeline_flow]


def main() -> int:
    built = [fn() for fn in ASSETS]
    # write SVGs next to PNGs for inspection
    svg_paths = []
    for svg, png in built:
        sp = png.with_suffix(".svg")
        sp.write_text(svg)
        svg_paths.append(str(sp))
    results = inspect_files(svg_paths)
    failed = False
    for path, issues in results.items():
        if issues:
            failed = True
            print(f"FAIL  {Path(path).name}")
            for i in issues:
                print(f"      - {i}")
        else:
            print(f"PASS  {Path(path).name}")
    if failed:
        print("\nInspection failed — not rendering PNGs.")
        return 1
    render_many([(svg, png) for svg, png in built], scale=2)
    print(f"\nRendered {len(built)} assets to PNG.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
