"""Blueprint / technical-schematic style: dark navy surface, grid paper, mono labels.

A deliberately different *surface* from the light data-exhibit look. Best for "how it's
built" / system-anatomy content aimed at developers and architects. Rendered with
HTML/CSS + inline SVG through Chromium.
"""

from __future__ import annotations

from pathlib import Path

from scripts.visuals.html.design import esc
from scripts.visuals.html.render import render_html_to_png
from scripts.visuals.tokens import THEMES

MONO = "'SF Mono', 'JetBrains Mono', Menlo, Consolas, monospace"

# Blueprint surface palette (its own medium; intentionally not the white exhibit bg).
INK = "#0b1b2b"
INK_2 = "#10263b"
LINE = "rgba(96,165,250,0.16)"
CYAN = "#38bdf8"
PAPER = "#dbeafe"
TXT = "#e2e8f0"
TXT_2 = "#94b8d8"


def blueprint_hub_and_beams(
    out_path: str | Path,
    *,
    title: str,
    subtitle: str,
    center_label: str,
    beams: list[tuple[str, str, str]],
    source: str,
    theme: str = "default",
    width: int = 1600,
    height: int = 760,
) -> Path:
    """Central node + four labeled beams on a blueprint grid. ``beams`` = (name, desc, metric)."""
    t = THEMES[theme]
    accent = t["ACCENT"]

    # Four box anchor points (centers) and the hub center.
    cx, cy = width / 2, 452
    pos = [
        (360, 300),   # top-left
        (1240, 300),  # top-right
        (360, 588),   # bottom-left
        (1240, 588),  # bottom-right
    ]
    bw, bh = 360, 150

    beam_lines = "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{CYAN}" '
        f'stroke-width="2" stroke-dasharray="2 7" opacity="0.85"/>'
        f'<circle cx="{x}" cy="{y}" r="4" fill="{CYAN}"/>'
        for x, y in pos
    )

    boxes = ""
    for (x, y), (name, desc, metric) in zip(pos, beams):
        left = x - bw / 2
        top = y - bh / 2
        boxes += f"""
        <div class="bp-box" style="left:{left}px; top:{top}px; width:{bw}px; height:{bh}px;">
          <div class="bp-name">{esc(name)}</div>
          <div class="bp-desc">{esc(desc)}</div>
          <div class="bp-chip">{esc(metric)}</div>
        </div>
        """

    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background:{INK}; }}
  #stage {{
    width:{width}px; height:{height}px; position:relative; overflow:hidden;
    background:
      linear-gradient(135deg, {INK} 0%, {INK_2} 100%);
    font-family:{MONO}; color:{TXT};
  }}
  .grid {{ position:absolute; inset:0; }}
  .corner {{ position:absolute; width:26px; height:26px; border:2px solid {CYAN}; opacity:0.5; }}
  .c-tl {{ left:26px; top:26px; border-right:0; border-bottom:0; }}
  .c-tr {{ right:26px; top:26px; border-left:0; border-bottom:0; }}
  .c-bl {{ left:26px; bottom:26px; border-right:0; border-top:0; }}
  .c-br {{ right:26px; bottom:26px; border-left:0; border-top:0; }}
  .head {{ position:absolute; left:64px; top:54px; right:64px; }}
  .eyebrow {{ font-size:17px; letter-spacing:0.34em; text-transform:uppercase; color:{CYAN}; }}
  .title {{ font-size:38px; font-weight:700; color:{PAPER}; margin-top:12px; letter-spacing:-0.01em;
            font-family:'Helvetica Neue',Helvetica,Arial,sans-serif; }}
  .subtitle {{ font-size:20px; color:{TXT_2}; margin-top:8px;
               font-family:'Helvetica Neue',Helvetica,Arial,sans-serif; }}
  .hub {{
    position:absolute; left:{cx - 130}px; top:{cy - 78}px; width:260px; height:156px;
    border:2px solid {CYAN}; border-radius:12px;
    background:rgba(56,189,248,0.10);
    display:flex; flex-direction:column; align-items:center; justify-content:center; gap:6px;
    box-shadow:0 0 0 6px rgba(56,189,248,0.06);
  }}
  .hub .h-label {{ font-size:36px; font-weight:800; color:{PAPER}; letter-spacing:0.04em; }}
  .hub .h-sub {{ font-size:15px; color:{TXT_2}; }}
  .bp-box {{
    position:absolute; border:1.5px solid rgba(148,184,216,0.5); border-radius:10px;
    background:rgba(13,38,59,0.72); padding:18px 22px;
    display:flex; flex-direction:column; gap:7px;
  }}
  .bp-name {{ font-size:22px; font-weight:700; color:{PAPER};
              font-family:'Helvetica Neue',Helvetica,Arial,sans-serif; }}
  .bp-desc {{ font-size:15px; color:{TXT_2}; }}
  .bp-chip {{ align-self:flex-start; margin-top:auto; font-size:15px; font-weight:700;
              color:{INK}; background:{CYAN}; padding:4px 12px; border-radius:999px; }}
  .src {{ position:absolute; left:64px; bottom:40px; font-size:15px; color:{TXT_2}; }}
</style></head>
<body>
  <div id="stage">
    <svg class="grid" width="{width}" height="{height}">
      <defs>
        <pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">
          <path d="M40 0H0V40" fill="none" stroke="{LINE}" stroke-width="1"/>
        </pattern>
      </defs>
      <rect width="{width}" height="{height}" fill="url(#g)"/>
      {beam_lines}
    </svg>
    <div class="corner c-tl"></div><div class="corner c-tr"></div>
    <div class="corner c-bl"></div><div class="corner c-br"></div>
    <div class="head">
      <div class="eyebrow">building blocks</div>
      <div class="title">{esc(title)}</div>
      <div class="subtitle">{esc(subtitle)}</div>
    </div>
    {boxes}
    <div class="hub">
      <div class="h-label">{esc(center_label)}</div>
      <div class="h-sub">the core generator</div>
    </div>
    <div class="src">{esc(source)}</div>
  </div>
</body></html>"""
    return render_html_to_png(doc, out_path, scale=2)
