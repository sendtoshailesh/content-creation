"""HTML/CSS visual design system rendered by Chromium.

Rationale
---------
Hand-built SVG/Pillow path math was the root cause of recurring quality
defects: inverted gauge arcs, arrows that did not anchor to box edges,
overlapping text, and type sizes that were wildly out of proportion with the
article body text.

This module replaces coordinate math with a browser layout engine:

* Layout is done with CSS Flexbox/Grid. Boxes, gaps, and connectors are
  positioned by the browser, so they cannot drift or overlap.
* Gauges are banned. Magnitude is shown with horizontal bars (a CSS width
  percentage) which is geometrically impossible to invert.
* Typography uses Inter (the same font as the blog) and a restrained, fixed
  ``TYPE_SCALE`` tuned so that, at the width an asset is displayed inside the
  article (~1000px), diagram text lands close to the article's own 17px body
  and ~24px headings instead of towering over them.

Every asset is authored as a small HTML template that pulls in :func:`css`.
The companion ``render.py`` rasterizes it with Chromium and ``inspect.py``
runs an automated DOM QA gate (overflow, off-scale text, stray labels).
"""

from __future__ import annotations

import html as _html

from scripts.visuals.tokens import BASE_TOKENS, THEMES

# ---------------------------------------------------------------------------
# Type scale (px). These are deliberately restrained. At a typical in-article
# display width of ~1000px an asset is shown at roughly its natural px size, so
# these land near the article's 17px body / 24px headings. Exactly ONE focal
# "display" number per asset is allowed to be large.
#
# inspect.py ALLOWED_SIZES MUST stay in sync with these values.
# ---------------------------------------------------------------------------
TYPE_SCALE = {
    "display": 76,   # one hero number per asset (focal point only)
    "title": 30,     # asset title
    "value": 34,     # metric value
    "subtitle": 21,  # supporting line under title
    "label": 20,     # box / bar label
    "body": 18,      # body copy inside cards
    "caption": 15,   # source line, footnotes
}

FONT_STACK = (
    "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, "
    "'Helvetica Neue', Arial, sans-serif"
)


def tokens(theme: str = "default") -> dict[str, str]:
    return {**BASE_TOKENS, **THEMES[theme]}


def esc(text: object) -> str:
    return _html.escape(str(text), quote=True)


def css(theme: str = "default", scale: float = 1.0) -> str:
    """Return the shared stylesheet with theme colors baked into CSS vars.

    ``scale`` multiplies the type scale and spacing. Use 1.0 for in-article
    figures (proportionate to the blog body) and ~1.6 for standalone social
    cards viewed full-screen. The inspector reads ``data-scale`` off #stage to
    recompute its allowed sizes, so this stays the single source of truth.
    """
    t = tokens(theme)

    def s(role: str) -> int:
        return round(TYPE_SCALE[role] * scale)

    return f"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root {{
  --scale: {scale};
  --bg: {t['BG']};
  --text: {t['TEXT']};
  --text2: {t['TEXT_2']};
  --muted: {t['MUTED']};
  --grid: {t['GRID']};
  --light: {t['LIGHT_BG']};
  --accent: {t['ACCENT']};
  --accent2: {t['ACCENT_2']};
  --accent3: {t['ACCENT_3']};
  --warn: {t['WARN']};
  --success: {t['SUCCESS']};
  --blue-bg: {t['BLUE_BG']};
  --teal-bg: {t['TEAL_BG']};
  --purple-bg: {t['PURPLE_BG']};
  --red-bg: {t['RED_BG']};

  --fs-display: {s('display')}px;
  --fs-title: {s('title')}px;
  --fs-value: {s('value')}px;
  --fs-subtitle: {s('subtitle')}px;
  --fs-label: {s('label')}px;
  --fs-body: {s('body')}px;
  --fs-caption: {s('caption')}px;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ background: var(--bg); }}
body {{
  font-family: {FONT_STACK};
  color: var(--text);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}}
.stage {{
  position: relative;
  background: var(--bg);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}}

/* ---- Type roles (data-role drives the QA inspector) ---- */
[data-role="display"]  {{ font-size: var(--fs-display);  font-weight: 800; line-height: 1.0; letter-spacing: -0.02em; }}
[data-role="title"]    {{ font-size: var(--fs-title);    font-weight: 700; line-height: 1.2; letter-spacing: -0.01em; }}
[data-role="value"]    {{ font-size: var(--fs-value);    font-weight: 800; line-height: 1.3; }}
[data-role="subtitle"] {{ font-size: var(--fs-subtitle); font-weight: 400; line-height: 1.35; color: var(--text2); }}
[data-role="label"]    {{ font-size: var(--fs-label);    font-weight: 600; line-height: 1.3; }}
[data-role="body"]     {{ font-size: var(--fs-body);     font-weight: 400; line-height: 1.5; color: var(--text2); }}
[data-role="caption"]  {{ font-size: var(--fs-caption);  font-weight: 500; line-height: 1.4; color: var(--muted); }}

/* ---- Card ---- */
.card {{
  background: var(--light);
  border: 1px solid var(--grid);
  border-radius: calc(16px * var(--scale));
  padding: calc(26px * var(--scale)) calc(30px * var(--scale));
  display: flex;
  flex-direction: column;
  gap: calc(10px * var(--scale));
}}
.card.accent {{ border-color: var(--accent); }}
.card.warn   {{ border-color: var(--warn); background: var(--red-bg); }}
.card.ok     {{ border-color: var(--success); background: var(--teal-bg); }}

/* ---- Eyebrow / kicker ---- */
.eyebrow {{
  font-size: var(--fs-caption);
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent);
}}

/* ---- Horizontal magnitude bar (replaces gauges) ---- */
.bar-row {{ display: flex; align-items: center; gap: 18px; }}
.bar-row .bar-label {{ flex: 0 0 var(--bar-label-w, 240px); }}
.bar-track {{
  flex: 1 1 auto;
  height: calc(var(--fs-label) * 1.5);
  background: var(--grid);
  border-radius: 999px;
  overflow: hidden;
}}
.bar-fill {{
  height: 100%;
  border-radius: 999px;
  background: var(--accent);
}}
.bar-fill.warn {{ background: var(--warn); }}
.bar-fill.ok   {{ background: var(--success); }}
.bar-row .bar-value {{ flex: 0 0 var(--bar-value-w, 150px); text-align: right; white-space: nowrap; }}

/* ---- Badge / pill ---- */
.badge {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
  min-width: calc(var(--fs-label) * 2.2);
  height: calc(var(--fs-label) * 2.2);
  padding: 0 calc(14px * var(--scale));
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
  font-weight: 800;
  font-size: var(--fs-label);
}}
.badge.warn {{ background: var(--warn); }}
.badge.ok   {{ background: var(--success); }}

/* ---- Vertical flow connector (straight line + chevron, no arc math) ---- */
.flow {{ display: flex; flex-direction: column; align-items: stretch; flex: 1 1 auto; }}
.flow > .card {{ flex: 1 1 0; justify-content: center; }}
.flow .connector {{
  align-self: center;
  width: 0;
  height: calc(26px * var(--scale));
  border-left: 3px solid var(--accent);
  position: relative;
}}
.flow .connector::after {{
  content: "";
  position: absolute;
  left: 50%;
  bottom: -2px;
  width: 12px;
  height: 12px;
  border-right: 3px solid var(--accent);
  border-bottom: 3px solid var(--accent);
  transform: translateX(-50%) rotate(45deg);
}}

/* ---- Delta bracket (shows the gap between two bar ends) ---- */
.gap-callout {{
  display: flex;
  align-items: center;
  gap: calc(14px * var(--scale));
  background: var(--purple-bg);
  border: 1px solid var(--accent3);
  border-radius: calc(14px * var(--scale));
  padding: calc(18px * var(--scale)) calc(24px * var(--scale));
}}
.gap-callout .gap-num {{ color: var(--accent3); font-weight: 800; }}

/* ---- Stat block (single focal number + label) ---- */
.stat {{
  display: flex;
  flex-direction: column;
  gap: calc(4px * var(--scale));
}}
.stat .stat-num {{ font-size: var(--fs-display); font-weight: 800; line-height: 1.18; letter-spacing: -0.02em; }}
.stat.warn .stat-num {{ color: var(--warn); }}
.stat.accent .stat-num {{ color: var(--accent); }}

/* ---- Metric card (value-sized number; safe to use several side by side) ---- */
.metric {{
  display: flex;
  flex-direction: column;
  gap: calc(8px * var(--scale));
  padding: calc(22px * var(--scale)) calc(26px * var(--scale));
  border-radius: calc(16px * var(--scale));
  background: var(--light);
  border: 1px solid var(--grid);
}}
.metric.accent {{ background: var(--blue-bg); border-color: var(--accent); }}
.metric.warn   {{ background: var(--red-bg);  border-color: var(--warn); }}
.metric.purple {{ background: var(--purple-bg); border-color: var(--accent3); }}
.metric .m-num {{ font-size: var(--fs-value); font-weight: 800; line-height: 1.3; }}
.metric.accent .m-num {{ color: var(--accent); }}
.metric.warn   .m-num {{ color: var(--warn); }}
.metric.purple .m-num {{ color: var(--accent3); }}

/* ---- Equal-width grid for side-by-side cards ---- */
.grid {{ display: grid; gap: calc(20px * var(--scale)); }}
.grid.two {{ grid-template-columns: 1fr 1fr; }}
.grid.three {{ grid-template-columns: 1fr 1fr 1fr; }}

/* ---- Big pull-quote ---- */
.quote {{ font-size: var(--fs-title); font-weight: 700; line-height: 1.25; letter-spacing: -0.01em; }}

.source {{
  position: absolute;
  left: var(--pad);
  right: var(--pad);
  bottom: var(--pad);
  color: var(--muted);
}}
"""


def page(width: int, height: int, body_html: str, theme: str = "default",
         pad: int = 56, scale: float = 1.0) -> str:
    """Wrap body HTML in a fixed-size stage for deterministic screenshots.

    ``scale`` is forwarded to :func:`css` and recorded on #stage as
    ``data-scale`` so the inspector can recompute its allowed type sizes.
    """
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<style>{css(theme, scale)}
:root {{ --pad: {round(pad * scale)}px; }}
.stage {{ width: {width}px; height: {height}px; padding: var(--pad); gap: calc(22px * var(--scale)); justify-content: center; padding-bottom: calc(var(--pad) + var(--fs-caption) + calc(18px * var(--scale))); }}
</style></head>
<body>
<div class="stage" id="stage" data-scale="{scale}">
{body_html}
</div>
</body></html>"""
