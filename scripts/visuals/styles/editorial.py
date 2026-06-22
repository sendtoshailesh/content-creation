"""Editorial-illustration style: a flat-vector metaphor scene with overlaid copy.

Deterministic SVG illustration (no AI pixels, no baked-in raster text \u2014 all text is real
DOM) rendered through Chromium. Best for openers, mood, and conceptual metaphors where a
data exhibit would be the wrong register.
"""

from __future__ import annotations

from pathlib import Path

from scripts.visuals.html.design import esc
from scripts.visuals.html.render import render_html_to_png
from scripts.visuals.tokens import BASE_TOKENS, THEMES

FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"


def editorial_guardrail(
    out_path: str | Path,
    *,
    kicker: str,
    title: str,
    formula: str,
    gap_note: str,
    source: str,
    theme: str = "midnight",
    width: int = 1600,
    height: int = 760,
) -> Path:
    """A guided-lane metaphor: rails steer the path, but one rail has a gap (the limit)."""
    t = THEMES[theme]
    accent = t["ACCENT"]
    warn = t["WARN"]
    text = BASE_TOKENS["TEXT"]
    text2 = BASE_TOKENS["TEXT_2"]
    muted = BASE_TOKENS["MUTED"]
    light = BASE_TOKENS["LIGHT_BG"]

    # Left illustration panel ~ 0..880, right copy panel ~ 880..1600.
    # Perspective lane: wide at bottom, narrow at top. Posts along both rails;
    # one right-rail segment is missing/red to signal the limit.
    left_rail = "M180 660 L470 150"
    right_rail = "M820 660 L530 150"

    def posts(x1, y1, x2, y2, n, color, skip=()):
        out = []
        for i in range(n):
            f = i / (n - 1)
            x = x1 + (x2 - x1) * f
            y = y1 + (y2 - y1) * f
            h = 46 * (1 - f) + 14 * f  # shorter toward the horizon
            col = warn if i in skip else color
            out.append(
                f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x:.0f}" y2="{y - h:.0f}" '
                f'stroke="{col}" stroke-width="{4 * (1 - f) + 2:.1f}" stroke-linecap="round"/>'
            )
        return "".join(out)

    left_posts = posts(180, 660, 470, 150, 8, accent)
    right_posts = posts(820, 660, 530, 150, 8, accent, skip=(3,))

    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background:{BASE_TOKENS['BG']}; }}
  #stage {{
    width:{width}px; height:{height}px; position:relative; overflow:hidden;
    background:{BASE_TOKENS['BG']}; font-family:{FONT};
    display:grid; grid-template-columns: 900px 1fr;
  }}
  .scene {{ position:relative; background:{light}; }}
  .copy {{ padding:84px 72px 0 56px; display:flex; flex-direction:column; gap:24px; justify-content:center; }}
  .eyebrow {{ font-size:19px; letter-spacing:0.3em; text-transform:uppercase; font-weight:700; color:{accent}; }}
  .title {{ font-size:46px; line-height:1.12; font-weight:800; color:{text}; letter-spacing:-0.015em; }}
  .formula {{ font-size:23px; font-weight:600; color:{text2}; padding:14px 18px;
              background:{t['PURPLE_BG']}; border-left:5px solid {t['ACCENT_3']}; border-radius:8px; }}
  .gap {{ display:flex; gap:14px; align-items:flex-start; font-size:21px; color:{text}; }}
  .gap .dot {{ flex:0 0 auto; width:16px; height:16px; border-radius:50%; background:{warn}; margin-top:7px; }}
  .src {{ position:absolute; left:56px; bottom:34px; font-size:16px; color:{muted}; }}
  .cap {{ position:absolute; left:60px; bottom:64px; width:760px; font-size:19px;
          font-weight:600; color:{text2}; }}
</style></head>
<body>
  <div id="stage">
    <div class="scene">
      <svg width="900" height="760" viewBox="0 0 900 760">
        <!-- lane -->
        <path d="M180 660 L470 150 L530 150 L820 660 Z" fill="{t['BLUE_BG']}" opacity="0.7"/>
        <!-- centre dashes -->
        <line x1="500" y1="640" x2="500" y2="170" stroke="{muted}" stroke-width="4" stroke-dasharray="14 16"/>
        <!-- rails -->
        <path d="{left_rail}" fill="none" stroke="{accent}" stroke-width="6" stroke-linecap="round"/>
        <path d="{right_rail}" fill="none" stroke="{accent}" stroke-width="6" stroke-linecap="round"/>
        {left_posts}
        {right_posts}
        <!-- the agent token travelling the lane -->
        <g>
          <rect x="455" y="470" width="90" height="64" rx="14" fill="{accent}"/>
          <circle cx="478" cy="540" r="13" fill="{text}"/>
          <circle cx="522" cy="540" r="13" fill="{text}"/>
        </g>
        <!-- gap marker on the right rail -->
        <circle cx="690" cy="394" r="22" fill="none" stroke="{warn}" stroke-width="4" stroke-dasharray="5 5"/>
      </svg>
      <div class="cap">The harness rails steer the path &mdash; but one rail still has a gap.</div>
      <div class="src">{esc(source)}</div>
    </div>
    <div class="copy">
      <div class="eyebrow">{esc(kicker)}</div>
      <div class="title">{esc(title)}</div>
      <div class="formula">{esc(formula)}</div>
      <div class="gap"><div class="dot"></div><div>{esc(gap_note)}</div></div>
    </div>
  </div>
</body></html>"""
    return render_html_to_png(doc, out_path, scale=2)
