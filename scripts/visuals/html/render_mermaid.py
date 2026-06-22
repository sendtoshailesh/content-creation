"""Render a Mermaid (.mmd) file to a static, on-brand PNG using Chromium.

Mermaid source only becomes a diagram when mermaid.js runs in a browser. To keep
the published page JavaScript-free, we rasterize the diagram here (loading
mermaid.js inside Playwright's Chromium) and embed the resulting PNG as an
``<img>``. Colors come from the design-token palette so the diagram matches the
rest of the visual pack.

Usage:
    python3 -m scripts.visuals.html.render_mermaid <input.mmd> <output.png>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Design tokens (kept in sync with .github/instructions/visual-standards).
TOKENS = {
    "BG": "#ffffff",
    "ACCENT": "#1f6feb",
    "TEXT": "#1e293b",
    "TEXT_2": "#475569",
    "MUTED": "#94a3b8",
    "LIGHT_BG": "#f8fafc",
    "GRID": "#e5e7eb",
}

_HTML = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  html, body {{ margin: 0; padding: 0; background: {bg}; }}
  #frame {{
    display: inline-block;
    background: {bg};
    padding: 28px 32px;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  }}
  #out svg {{ display: block; }}
</style>
</head>
<body>
  <div id="frame"><div id="out"></div></div>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{
      startOnLoad: false,
      theme: 'base',
      fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif",
      themeVariables: {{
        background: '{bg}',
        primaryColor: '{light}',
        primaryBorderColor: '{muted}',
        primaryTextColor: '{text}',
        lineColor: '{accent}',
        edgeLabelBackground: '{bg}',
        fontSize: '16px'
      }},
      flowchart: {{ curve: 'basis', useMaxWidth: false, htmlLabels: true, padding: 12 }}
    }});
    const graph = {graph};
    try {{
      const {{ svg }} = await mermaid.render('diagram', graph);
      document.getElementById('out').innerHTML = svg;
      const el = document.querySelector('#out svg');
      el.removeAttribute('width');
      el.removeAttribute('height');
      el.style.width = (el.viewBox.baseVal.width) + 'px';
      el.style.height = (el.viewBox.baseVal.height) + 'px';
      window.__mermaidDone = true;
    }} catch (e) {{
      document.body.innerHTML = '<pre style="color:#dc2626">' + e.message + '</pre>';
      window.__mermaidError = e.message;
      window.__mermaidDone = true;
    }}
  </script>
</body>
</html>
"""


def render_mmd_to_png(mmd_path: str | Path, out_path: str | Path, scale: int = 2) -> Path:
    mmd_path = Path(mmd_path)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    graph = mmd_path.read_text()
    doc = _HTML.format(
        bg=TOKENS["BG"],
        light=TOKENS["LIGHT_BG"],
        muted=TOKENS["MUTED"],
        text=TOKENS["TEXT"],
        accent=TOKENS["ACCENT"],
        graph=json.dumps(graph),
    )
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=scale)
        page.set_content(doc, wait_until="networkidle")
        page.wait_for_function("window.__mermaidDone === true", timeout=30000)
        err = page.evaluate("window.__mermaidError || null")
        if err:
            browser.close()
            raise RuntimeError(f"Mermaid render failed: {err}")
        page.evaluate("async () => { if (document.fonts) { await document.fonts.ready; } }")
        frame = page.query_selector("#frame")
        frame.screenshot(path=str(out_path))
        browser.close()
    return out_path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    out = render_mmd_to_png(sys.argv[1], sys.argv[2])
    print(f"Rendered {sys.argv[1]} -> {out}")
