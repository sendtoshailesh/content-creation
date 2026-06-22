"""Render HTML/CSS documents to PNG using Chromium (Playwright).

The screenshot is clipped to the ``#stage`` element so output dimensions are
exactly the authored width/height. ``device_scale_factor=2`` yields crisp,
high-DPI output. Fonts are awaited before capture so text metrics are final.
"""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright


def _shoot(page, out_path: Path) -> None:
    page.wait_for_load_state("networkidle")
    # Make sure fonts are ready so text metrics are final.
    page.evaluate("async () => { if (document.fonts) { await document.fonts.ready; } }")
    stage = page.query_selector("#stage")
    if stage is None:
        raise ValueError("HTML must contain an element with id='stage'")
    stage.screenshot(path=str(out_path))


def render_html_to_png(doc: str, out_path: str | Path, scale: int = 2) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=scale)
        page.set_content(doc, wait_until="networkidle")
        _shoot(page, out_path)
        browser.close()
    return out_path


def render_many(items: list[tuple[str, str | Path]], scale: int = 2) -> list[Path]:
    """Render a list of (html_doc, out_path) pairs in one browser session."""
    out: list[Path] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for doc, path in items:
            path = Path(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            page = browser.new_page(device_scale_factor=scale)
            page.set_content(doc, wait_until="networkidle")
            _shoot(page, path)
            page.close()
            out.append(path)
        browser.close()
    return out
