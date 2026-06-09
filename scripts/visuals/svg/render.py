"""Render SVG documents to PNG using Chromium (Playwright).

Chromium gives the most faithful font + anti-aliasing result and is the same
engine the inspector measures, so what QA sees is what ships. A device scale of
2 yields crisp, high-DPI output suitable for social platforms.
"""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright


def render_svg_to_png(svg: str, out_path: str | Path, scale: int = 2) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # width/height live in the <svg> root; read them back for the viewport
    import re

    m = re.search(r'width="(\d+)"\s+height="(\d+)"', svg)
    if not m:
        raise ValueError("SVG must declare integer width and height on the root element")
    width, height = int(m.group(1)), int(m.group(2))
    page_html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<style>*{margin:0;padding:0}html,body{background:#fff}</style></head>"
        f"<body>{svg}</body></html>"
    )
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": width, "height": height}, device_scale_factor=scale
        )
        page.set_content(page_html, wait_until="networkidle")
        el = page.query_selector("svg")
        el.screenshot(path=str(out_path))
        browser.close()
    return out_path


def render_many(items: list[tuple[str, str | Path]], scale: int = 2) -> list[Path]:
    """Render a list of (svg_string, out_path) in one browser session."""
    import re

    out: list[Path] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for svg, path in items:
            path = Path(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            m = re.search(r'width="(\d+)"\s+height="(\d+)"', svg)
            width, height = int(m.group(1)), int(m.group(2))
            page = browser.new_page(
                viewport={"width": width, "height": height}, device_scale_factor=scale
            )
            page.set_content(
                "<!doctype html><html><head><meta charset='utf-8'>"
                "<style>*{margin:0;padding:0}html,body{background:#fff}</style>"
                f"</head><body>{svg}</body></html>",
                wait_until="networkidle",
            )
            page.query_selector("svg").screenshot(path=str(path))
            page.close()
            out.append(path)
        browser.close()
    return out
