"""Typographic style: text-as-art. Oversized editorial type, asymmetric layout.

Best for quotes, single big ideas, hooks, and hero cards. Uses HTML/CSS + Chromium
so type metrics are crisp. Shares design tokens; no embedded raster text rules apply
only to AI illustration, not to this typographic medium.
"""

from __future__ import annotations

from pathlib import Path

from scripts.visuals.html.design import esc
from scripts.visuals.html.render import render_html_to_png
from scripts.visuals.tokens import BASE_TOKENS, THEMES

FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"


def typographic_quote(
    out_path: str | Path,
    *,
    kicker: str,
    quote: str,
    accent_word: str,
    context: str,
    source: str,
    theme: str = "default",
    width: int = 1600,
    height: int = 760,
) -> Path:
    """Render a quote as oversized typographic art with one accented word."""
    t = THEMES[theme]
    accent = t["ACCENT"]
    text = BASE_TOKENS["TEXT"]
    text2 = BASE_TOKENS["TEXT_2"]
    muted = BASE_TOKENS["MUTED"]

    # Accent a single word inside the quote without breaking escaping.
    safe_quote = esc(quote)
    safe_word = esc(accent_word)
    highlighted = safe_quote.replace(
        safe_word, f'<span style="color:{accent};">{safe_word}</span>', 1
    )

    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background:{BASE_TOKENS['BG']}; }}
  #stage {{
    width:{width}px; height:{height}px; background:{BASE_TOKENS['BG']};
    font-family:{FONT}; position:relative; overflow:hidden;
    padding:88px 96px; display:flex; flex-direction:column;
    justify-content:center; gap:30px;
  }}
  .mark {{
    position:absolute; top:-70px; left:40px; font-size:420px; line-height:1;
    color:{accent}; opacity:0.08; font-weight:800; user-select:none;
  }}
  .corner {{
    position:absolute; bottom:0; right:0; width:280px; height:280px;
    background:{t['BLUE_BG']}; opacity:0.45;
    clip-path:polygon(100% 0, 100% 100%, 0 100%);
  }}
  .eyebrow {{
    font-size:22px; letter-spacing:0.32em; text-transform:uppercase;
    font-weight:700; color:{accent}; z-index:1;
  }}
  .quote {{
    font-size:90px; line-height:1.04; font-weight:800; color:{text};
    letter-spacing:-0.015em; max-width:1180px; z-index:1;
  }}
  .rule {{ width:140px; height:8px; background:{accent}; border-radius:4px; z-index:1; }}
  .context {{ font-size:27px; line-height:1.45; color:{text2}; max-width:1040px; z-index:1; }}
  .src {{ font-size:18px; color:{muted}; letter-spacing:0.02em; z-index:1; }}
</style></head>
<body>
  <div id="stage">
    <div class="mark">&#8220;</div>
    <div class="corner"></div>
    <div class="eyebrow">{esc(kicker)}</div>
    <div class="quote">{highlighted}</div>
    <div class="rule"></div>
    <div class="context">{esc(context)}</div>
    <div class="src">{esc(source)}</div>
  </div>
</body></html>"""
    return render_html_to_png(doc, out_path, scale=2)
