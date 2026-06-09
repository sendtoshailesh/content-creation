"""Automated visual QA for HTML/CSS assets — the agentic inspector gate.

Loads each authored HTML doc into Chromium and measures the live DOM to catch
the exact classes of defect review has reported:

1. Oversized / uneven text -> any text whose computed font-size is not one of
   the fixed TYPE_SCALE sizes, more than one "display" focal number, or more
   than seven distinct sizes on the canvas.
2. Clipped / overflowing text -> any text element whose content overflows its
   own box (scrollWidth/Height exceeds clientWidth/Height), or content that
   overflows the stage. CSS layout removes coordinate bugs but text can still
   be clipped if a box is too small; this catches it.
3. Stray internal labels -> "02 / 10", "EXHIBIT 1", "Fig 3", "Page 2".
4. Missing flow direction -> a multi-step flow with no connectors.

Run:  python3 -m scripts.visuals.html.inspect <file1.html> [file2.html ...]
Exit is non-zero if any asset FAILS. Gate the renderer on this.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from scripts.visuals.html.design import TYPE_SCALE

# Allowed computed font sizes (kept in sync with design.TYPE_SCALE).
ALLOWED_SIZES = set(TYPE_SCALE.values())
DISPLAY_SIZE = TYPE_SCALE["display"]
MAX_DISTINCT_SIZES = len(TYPE_SCALE)  # 7

STRAY_LABEL = re.compile(
    r"^\s*(\d+\s*/\s*\d+|exhibit\s*\d+|fig(?:ure)?\.?\s*\d+|page\s*\d+|slide\s*\d+)\s*$",
    re.I,
)

_MEASURE_JS = r"""
() => {
  const roleEls = [...document.querySelectorAll('[data-role]')];
  const texts = roleEls.map(el => ({
    content: el.textContent.trim(),
    size: Math.round(parseFloat(getComputedStyle(el).fontSize)),
    role: el.getAttribute('data-role'),
    overflowX: el.scrollWidth - el.clientWidth,
    overflowY: el.scrollHeight - el.clientHeight,
  }));
  const stage = document.querySelector('#stage');
  const stageOverflow = {
    x: stage.scrollWidth - stage.clientWidth,
    y: stage.scrollHeight - stage.clientHeight,
  };
  const connectors = document.querySelectorAll('.connector').length;
  const flows = document.querySelectorAll('.flow').length;
  const steps = document.querySelectorAll('.flow .card, .flow .step').length;
  return {
    texts, stageOverflow, connectors, flows, steps,
    scale: parseFloat(stage.getAttribute('data-scale') || '1'),
  };
}
"""


def _inspect_one(page, doc: str, name: str) -> list[str]:
    page.set_content(doc, wait_until="networkidle")
    page.evaluate("async () => { if (document.fonts) await document.fonts.ready; }")
    data = page.evaluate(_MEASURE_JS)
    fails: list[str] = []

    scale = float(data.get("scale") or 1.0)
    allowed = {round(v * scale) for v in TYPE_SCALE.values()}

    sizes_seen: set[int] = set()
    display_count = 0
    for t in data["texts"]:
        if not t["content"]:
            continue
        size = t["size"]
        sizes_seen.add(size)
        if size not in allowed:
            fails.append(
                f"off-scale text {size}px (role={t['role']}, allowed={sorted(allowed)}): "
                f"{t['content'][:42]!r}"
            )
        if t["role"] == "display":
            display_count += 1
        # Text overflowing its own box -> clipped / cramped.
        if t["overflowX"] > 1 or t["overflowY"] > 1:
            fails.append(
                f"text overflows its box (+{t['overflowX']}x/+{t['overflowY']}y): "
                f"{t['content'][:42]!r}"
            )
        if STRAY_LABEL.match(t["content"]):
            fails.append(f"stray internal label: {t['content']!r}")

    if len(sizes_seen) > MAX_DISTINCT_SIZES:
        fails.append(
            f"too many distinct text sizes ({len(sizes_seen)} > {MAX_DISTINCT_SIZES}): "
            f"{sorted(sizes_seen)}"
        )
    if display_count > 1:
        fails.append(
            f"more than one focal 'display' number ({display_count}); allow exactly one"
        )

    so = data["stageOverflow"]
    if so["x"] > 1 or so["y"] > 1:
        fails.append(f"content overflows the canvas (+{so['x']}x/+{so['y']}y)")

    # A flow with multiple steps must show direction.
    if data["flows"] and data["steps"] >= 2 and data["connectors"] == 0:
        fails.append("flow has multiple steps but no connectors (no visible direction)")

    return fails


def inspect_files(paths: list[str | Path]) -> bool:
    all_ok = True
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=1)
        for path in paths:
            path = Path(path)
            doc = path.read_text(encoding="utf-8")
            fails = _inspect_one(page, doc, path.name)
            if fails:
                all_ok = False
                print(f"FAIL  {path.name}")
                for f in fails:
                    print(f"   - {f}")
            else:
                print(f"PASS  {path.name}")
        browser.close()
    return all_ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python3 -m scripts.visuals.html.inspect <file.html> ...")
        raise SystemExit(2)
    ok = inspect_files(sys.argv[1:])
    raise SystemExit(0 if ok else 1)
