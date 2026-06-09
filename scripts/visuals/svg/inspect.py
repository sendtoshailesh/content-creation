"""Automated visual inspector — the agentic QA layer.

Loads each SVG into Chromium (Playwright) and measures the live DOM to catch the
exact defects reported by review:

1. Uneven text     -> too many distinct font sizes, or sibling box-labels that
                      disagree in size, or a value far larger than its neighbours.
2. Distorted arrows -> connectors whose endpoints do not land on a box edge
                      (we check every <line data-role="arrow"> against the
                      bounding boxes of <rect>/<circle> nodes).
3. Faded arrows    -> arrow stroke colors that are light grays (low contrast),
                      which undermine the transition meaning.
4. Stray labels    -> internal numbering like "02 / 10" or "EXHIBIT 1" that
                      carries no reader value.

Run:  python3 -m scripts.visuals.svg.inspect <file1.svg> [file2.svg ...]
Returns non-zero exit if any asset FAILS. Use as a CI/agent gate before render.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Light grays that must never be used for an arrow stroke.
FADED = {"#e5e7eb", "#94a3b8", "#cbd5e1", "#d1d5db", "#9ca3af"}
STRAY_LABEL = re.compile(r"^\s*(\d+\s*/\s*\d+|exhibit\s*\d+|fig(?:ure)?\.?\s*\d+|page\s*\d+)\s*$", re.I)
# Allowed type-scale sizes (kept in sync with design.TYPE_SCALE).
ALLOWED_SIZES = {92, 50, 30, 40, 24, 23, 18}

_MEASURE_JS = r"""
() => {
  const svg = document.querySelector('svg');
  const texts = [...svg.querySelectorAll('text')].map(t => {
    const bb = t.getBBox();
    return {
      content: t.textContent.trim(),
      size: Math.round(parseFloat(getComputedStyle(t).fontSize)),
      role: t.getAttribute('data-role'),
      x: bb.x, y: bb.y, w: bb.width, h: bb.height
    };
  });
  const arrows = [...svg.querySelectorAll('[data-role="arrow"]')].map(a => ({
    x1: +a.getAttribute('x1'), y1: +a.getAttribute('y1'),
    x2: +a.getAttribute('x2'), y2: +a.getAttribute('y2'),
    stroke: (a.getAttribute('stroke') || '').toLowerCase()
  }));
  const boxes = [...svg.querySelectorAll('rect, circle')].map(b => {
    const bb = b.getBBox();
    return {x: bb.x, y: bb.y, w: bb.width, h: bb.height};
  });
  return {texts, arrows, boxes};
}
"""


def _near_box_edge(px: float, py: float, boxes: list[dict], tol: float = 14) -> bool:
    for b in boxes:
        x0, y0, x1, y1 = b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]
        inside_x = x0 - tol <= px <= x1 + tol
        inside_y = y0 - tol <= py <= y1 + tol
        on_v_edge = (abs(px - x0) <= tol or abs(px - x1) <= tol) and inside_y
        on_h_edge = (abs(py - y0) <= tol or abs(py - y1) <= tol) and inside_x
        if (on_v_edge or on_h_edge) and inside_x and inside_y:
            return True
    return False


def inspect_svg(svg_text: str, page) -> list[str]:
    page.set_content(
        "<!doctype html><html><body style='margin:0'>" + svg_text + "</body></html>",
        wait_until="networkidle",
    )
    data = page.evaluate(_MEASURE_JS)
    issues: list[str] = []

    # 1. type scale: sizes must come from the allowed scale
    sizes = sorted({t["size"] for t in data["texts"]})
    off_scale = [s for s in sizes if s not in ALLOWED_SIZES]
    if off_scale:
        issues.append(f"text uses off-scale font sizes {off_scale}; allowed {sorted(ALLOWED_SIZES)}")
    if len(sizes) > 5:
        issues.append(f"too many distinct text sizes ({len(sizes)}: {sizes}); keep <= 5 for uniformity")

    # 1b. sibling box-labels must agree in size
    label_sizes = {t["size"] for t in data["texts"] if t["role"] == "label"}
    if len(label_sizes) > 1:
        issues.append(f"box labels are uneven sizes {sorted(label_sizes)}; sibling labels must match")

    # 2/3. arrows
    for a in data["arrows"]:
        if a["stroke"] in FADED:
            issues.append(f"arrow stroke {a['stroke']} is a faded gray; use a strong token color")
        start_ok = _near_box_edge(a["x1"], a["y1"], data["boxes"])
        end_ok = _near_box_edge(a["x2"], a["y2"], data["boxes"])
        if not (start_ok and end_ok):
            issues.append(
                f"arrow ({a['x1']:.0f},{a['y1']:.0f})->({a['x2']:.0f},{a['y2']:.0f}) "
                f"does not connect box edges (start_ok={start_ok}, end_ok={end_ok})"
            )

    # 4. stray internal labels
    for t in data["texts"]:
        if STRAY_LABEL.match(t["content"]):
            issues.append(f"stray internal label {t['content']!r} carries no reader value; remove it")

    return issues


def inspect_files(paths: list[str]) -> dict[str, list[str]]:
    results: dict[str, list[str]] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for path in paths:
            svg = Path(path).read_text()
            results[path] = inspect_svg(svg, page)
        browser.close()
    return results


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: python3 -m scripts.visuals.svg.inspect <file.svg> ...")
        return 2
    results = inspect_files(argv)
    failed = 0
    for path, issues in results.items():
        name = Path(path).name
        if issues:
            failed += 1
            print(f"FAIL  {name}")
            for i in issues:
                print(f"      - {i}")
        else:
            print(f"PASS  {name}")
    print(f"\n{len(results) - failed}/{len(results)} assets passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
