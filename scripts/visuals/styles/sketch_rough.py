"""Hand-drawn diagram style via Rough.js, rendered to PNG through Chromium.

Reuses the same static-pre-render model as the ECharts bridge: a headless Chromium
draws sketchy SVG (hachure fills, wobbly strokes) and we screenshot ``#stage``. No
client JS ever ships to a published page.

Rough.js is a self-contained ES module. Browsers block ``file://`` module imports
(CORS, origin ``null``), so we inline it as a ``data:`` URL module import — the ``data:``
scheme is allowed. Run ``npm install`` in ``scripts/visuals/charts_js`` once to vendor it.
"""

from __future__ import annotations

import base64
import json
from pathlib import Path

from scripts.visuals.tokens import BASE_TOKENS, THEMES

_HERE = Path(__file__).resolve().parent
_BRIDGE = _HERE.parent / "charts_js"
_ROUGH = _BRIDGE / "node_modules/roughjs/bundled/rough.esm.js"

FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"


def _require_rough() -> None:
    if not _ROUGH.is_file():
        raise RuntimeError(
            "rough.esm.js not found. Install it once:\n"
            "  cd scripts/visuals/charts_js && npm install roughjs"
        )


def _rough_data_url() -> str:
    raw = _ROUGH.read_bytes()
    b64 = base64.b64encode(raw).decode("ascii")
    return f"data:text/javascript;base64,{b64}"


def _html(width: int, height: int, draw_js: str) -> str:
    rough_url = _rough_data_url()
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background:{BASE_TOKENS['BG']}; }}
  #stage {{ width:{width}px; height:{height}px; background:{BASE_TOKENS['BG']};
            font-family:{FONT}; position:relative; }}
  svg {{ display:block; }}
  text {{ font-family:{FONT}; }}
</style></head>
<body>
  <div id="stage">
    <svg id="rc" width="{width}" height="{height}" viewBox="0 0 {width} {height}"></svg>
  </div>
  <script type="module">
    import rough from '{rough_url}';
    const NS = 'http://www.w3.org/2000/svg';
    const svg = document.getElementById('rc');
    const rc = rough.svg(svg);
    const add = (n) => svg.appendChild(n);

    function text(x, y, s, o) {{
      o = o || {{}};
      const el = document.createElementNS(NS, 'text');
      el.setAttribute('x', x); el.setAttribute('y', y);
      el.setAttribute('fill', o.fill || '#1e293b');
      el.setAttribute('font-size', o.size || 26);
      el.setAttribute('font-weight', o.weight || '400');
      el.setAttribute('text-anchor', o.anchor || 'middle');
      el.setAttribute('letter-spacing', o.ls || '0');
      el.textContent = s; add(el); return el;
    }}
    function lines(cx, y0, arr, o) {{
      o = o || {{}}; const lh = o.lh || 30;
      arr.forEach((s, i) => text(cx, y0 + i * lh, s, o));
    }}
    function box(x, y, w, h, fill, stroke) {{
      add(rc.rectangle(x, y, w, h, {{
        roughness: 1.7, bowing: 1.4, fill: fill, fillStyle: 'hachure',
        hachureGap: 7, fillWeight: 1.4, stroke: stroke, strokeWidth: 2.4,
      }}));
    }}
    function arrow(x1, y1, x2, y2, stroke) {{
      add(rc.line(x1, y1, x2, y2, {{ roughness: 1.6, bowing: 2, stroke: stroke, strokeWidth: 2.6 }}));
      const a = Math.atan2(y2 - y1, x2 - x1), L = 18, d = 0.5;
      add(rc.line(x2, y2, x2 - L * Math.cos(a - d), y2 - L * Math.sin(a - d),
        {{ roughness: 1.0, stroke: stroke, strokeWidth: 2.6 }}));
      add(rc.line(x2, y2, x2 - L * Math.cos(a + d), y2 - L * Math.sin(a + d),
        {{ roughness: 1.0, stroke: stroke, strokeWidth: 2.6 }}));
    }}

    {draw_js}

    window.__done = true;
  </script>
</body></html>"""


def _render(html: str, out_path: Path, width: int, height: int) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        page.set_content(html, wait_until="load")
        page.wait_for_function("window.__done === true")
        page.wait_for_timeout(120)
        stage = page.query_selector("#stage")
        if stage is None:
            raise RuntimeError("internal: #stage missing")
        stage.screenshot(path=str(out_path))
        browser.close()


def sketch_anatomy(
    out_path: str | Path,
    *,
    theme: str = "default",
    width: int = 1600,
    height: int = 760,
) -> Path:
    """Hand-drawn 'Agent = model + harness' anatomy diagram."""
    _require_rough()
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    t = THEMES[theme]

    colors = {
        "accent": t["ACCENT"], "blue_bg": t["BLUE_BG"],
        "teal": t["ACCENT_2"], "teal_bg": t["TEAL_BG"],
        "green": t["SUCCESS"], "green_bg": "#dcfce7",
        "text": BASE_TOKENS["TEXT"], "text2": BASE_TOKENS["TEXT_2"],
        "muted": BASE_TOKENS["MUTED"], "purple": t["ACCENT_3"],
    }
    c = {k: json.dumps(v) for k, v in colors.items()}

    draw = f"""
    // Title + subtitle
    text(800, 72, 'Agent = model + harness', {{ size: 42, weight: '800', fill: {c['text']} }});
    text(800, 116, 'Feed-forward improves the first move. Feedback improves correction.',
      {{ size: 22, fill: {c['text2']} }});

    // Feed-forward (left)
    box(96, 250, 380, 250, {c['teal_bg']}, {c['teal']});
    text(286, 300, 'FEED-FORWARD', {{ size: 23, weight: '800', fill: {c['teal']}, ls: '0.06em' }});
    lines(286, 348, ['Conventions, architecture', 'context, specs, examples,',
      'and design systems.'], {{ size: 20, fill: {c['text2']}, lh: 34 }});

    // Model (center, larger)
    box(610, 208, 380, 312, {c['blue_bg']}, {c['accent']});
    text(800, 352, 'MODEL', {{ size: 38, weight: '800', fill: {c['accent']}, ls: '0.04em' }});
    text(800, 398, 'The generator is only the core.', {{ size: 21, fill: {c['text2']} }});

    // Feedback (right)
    box(1124, 250, 380, 250, {c['green_bg']}, {c['green']});
    text(1314, 300, 'FEEDBACK', {{ size: 23, weight: '800', fill: {c['green']}, ls: '0.06em' }});
    lines(1314, 348, ['Tests, compiler errors,', 'static analysis, coverage,',
      'and adversarial review.'], {{ size: 20, fill: {c['text2']}, lh: 34 }});

    // Flow arrows
    arrow(478, 340, 606, 340, {c['teal']});
    arrow(994, 340, 1122, 340, {c['green']});

    // Feedback loop along the bottom, label clear above the arrow
    text(800, 582, 'feedback loop \u2014 catches cheap failures before human review',
      {{ size: 19, weight: '700', fill: {c['purple']} }});
    arrow(1300, 622, 320, 622, {c['purple']});

    text(800, 712, 'Source: InfoQ podcast — feed-forward and feedback framework',
      {{ size: 16, fill: {c['muted']} }});
    """
    _render(_html(width, height, draw), out_path, width, height)
    return out_path

def sketch_flow_pipeline(
    out_path: str | Path,
    *,
    theme: str = "default",
    width: int = 1600,
    height: int = 760,
) -> Path:
    """Hand-drawn 'this pipeline is a harness' flow: config.md -> agents/skills/scripts/gates."""
    _require_rough()
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    t = THEMES[theme]
    colors = {
        "accent": t["ACCENT"], "blue_bg": t["BLUE_BG"],
        "teal": t["ACCENT_2"], "teal_bg": t["TEAL_BG"],
        "purple": t["ACCENT_3"], "purple_bg": t["PURPLE_BG"],
        "green": t["SUCCESS"], "green_bg": "#dcfce7",
        "warn": t["WARN"], "red_bg": t["RED_BG"],
        "text": BASE_TOKENS["TEXT"], "text2": BASE_TOKENS["TEXT_2"],
        "muted": BASE_TOKENS["MUTED"],
    }
    c = {k: json.dumps(v) for k, v in colors.items()}

    draw = f"""
    text(800, 66, 'This pipeline is a harness', {{ size: 40, weight: '800', fill: {c['text']} }});
    text(800, 108, 'The model can change. The workflow contract stays inspectable.',
      {{ size: 21, fill: {c['text2']} }});

    // Config artifact (left)
    box(86, 232, 372, 322, {c['blue_bg']}, {c['accent']});
    text(272, 286, 'pipeline-config.md', {{ size: 26, weight: '800', fill: {c['accent']} }});
    lines(272, 340, ['Topic, platforms,', 'status, gates,', 'and current step.'],
      {{ size: 20, fill: {c['text2']}, lh: 36 }});
    text(272, 506, 'one reviewable contract', {{ size: 17, fill: {c['muted']} }});

    function node(x, y, name, l1, l2, fill, stroke) {{
      box(x, y, 372, 142, fill, stroke);
      text(x + 186, y + 46, name, {{ size: 24, weight: '800', fill: stroke }});
      lines(x + 186, y + 82, [l1, l2], {{ size: 18, fill: {c['text2']}, lh: 28 }});
    }}
    node(712, 218, 'Agents', 'Strategy, writing, visuals,', 'review, social, publishing', {c['teal_bg']}, {c['teal']});
    node(1126, 218, 'Skills', 'Scope, dimensions,', 'visual planning, rendering', {c['purple_bg']}, {c['purple']});
    node(712, 396, 'Scripts', 'Rendering, publishing,', 'validation helpers', {c['green_bg']}, {c['green']});
    node(1126, 396, 'Gates', 'Scope, blog approval,', 'publishing approval', {c['red_bg']}, {c['warn']});

    // Clean left-to-right pipeline: config feeds the left column, which feeds the right.
    arrow(458, 300, 708, 289, {c['teal']});
    arrow(458, 460, 708, 467, {c['green']});
    arrow(1086, 289, 1122, 289, {c['purple']});
    arrow(1086, 467, 1122, 467, {c['warn']});

    text(800, 712, 'Source: this repository, current run, 2026-06-20',
      {{ size: 16, fill: {c['muted']} }});
    """
    _render(_html(width, height, draw), out_path, width, height)
    return out_path