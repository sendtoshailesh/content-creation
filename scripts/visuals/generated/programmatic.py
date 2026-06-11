"""Deterministic, offline, zero-cost hero/backdrop generator.

This is the **default** AI-imagery path. It needs no API key, no network, and no
per-image cost, and it is fully reproducible — the Copilot model parameterizes a
deterministic render here, exactly the way it already authors diagrams. Use it for
hero/backdrop/scene slots that carry mood, not information.

The companion paid path (``generate.py``) calls an external image model and is opt-in
(``image_generation: ai``) only when a photoreal/illustrative look is genuinely required.

Backdrops are authored as full-bleed HTML/CSS and rasterized by Chromium, reusing the
shared design tokens. A reserved negative-space band is included so text can be overlaid
programmatically (no text is ever baked into the image).
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from scripts.visuals.tokens import BASE_TOKENS, THEMES

GENERATED_DIR = Path("content/visuals/generated")

STYLES = ("gradient-mesh", "geometric", "duotone-bands", "contour-glow", "grid-pulse")


def _theme(theme: str) -> dict[str, str]:
    return {**BASE_TOKENS, **THEMES[theme]}


def _backdrop_css(style: str, t: dict[str, str], negative_space: str) -> str:
    """Return CSS for a full-bleed backdrop in the given style + theme."""
    a, a2, a3 = t["ACCENT"], t["ACCENT_2"], t["ACCENT_3"]
    light = t["LIGHT_BG"]

    # The negative-space panel is a near-uniform tint reserved for text overlay,
    # placed as a hard-edged band on the chosen side (CSS gradient, not position math).
    if negative_space == "right":
        panel = f"linear-gradient(90deg, transparent 0 58%, {light}f2 72% 100%)"
    elif negative_space == "left":
        panel = f"linear-gradient(90deg, {light}f2 0 28%, transparent 42% 100%)"
    else:
        panel = None

    backgrounds = {
        "gradient-mesh": (
            f"radial-gradient(120% 120% at 18% 12%, {a}73 0%, transparent 46%),"
            f"radial-gradient(120% 120% at 88% 24%, {a3}5e 0%, transparent 52%),"
            f"radial-gradient(150% 150% at 70% 98%, {a2}54 0%, transparent 56%),"
            f"linear-gradient(135deg, {light} 0%, #ffffff 100%)"
        ),
        "geometric": (
            f"conic-gradient(from 210deg at 78% 22%, {a3}40, transparent 40%),"
            f"linear-gradient(120deg, {a}1f 0 30%, transparent 30%),"
            f"linear-gradient(300deg, {a2}26 0 26%, transparent 26%),"
            f"linear-gradient(135deg, #ffffff, {light})"
        ),
        "duotone-bands": (
            f"repeating-linear-gradient(115deg, {a}14 0 38px, transparent 38px 92px),"
            f"linear-gradient(160deg, {a}26 0%, {a3}1f 55%, {a2}26 100%),"
            f"linear-gradient(135deg, #ffffff, {light})"
        ),
        "contour-glow": (
            f"radial-gradient(60% 80% at 30% 50%, {a2}3a 0%, transparent 60%),"
            f"repeating-radial-gradient(circle at 30% 50%, transparent 0 26px, {a}12 26px 28px),"
            f"linear-gradient(135deg, {light}, #ffffff)"
        ),
        "grid-pulse": (
            f"radial-gradient(90% 90% at 75% 30%, {a3}38 0%, transparent 55%),"
            f"linear-gradient({a}10 1px, transparent 1px) 0 0 / 46px 46px,"
            f"linear-gradient(90deg, {a}10 1px, transparent 1px) 0 0 / 46px 46px,"
            f"linear-gradient(135deg, #ffffff, {light})"
        ),
    }
    bg = backgrounds.get(style, backgrounds["gradient-mesh"])
    layers = bg if panel is None else f"{panel}, {bg}"
    return layers


def build_hero_html(
    style: str = "gradient-mesh",
    theme: str = "default",
    width: int = 1536,
    height: int = 1024,
    negative_space: str = "right",
    eyebrow: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
) -> str:
    """Author a full-bleed backdrop as an HTML document with a #stage of fixed size.

    When ``title``/``subtitle``/``eyebrow`` are given, text is composited as a **CSS layer**
    over the reserved negative-space band (the repo's compositing standard — browser text, not
    Pillow). The backdrop itself stays text-free; the overlay is the intentional final text.
    """
    if style not in STYLES:
        raise ValueError(f"Unknown style {style!r}; expected one of {STYLES}.")
    if theme not in THEMES:
        raise ValueError(f"Unknown theme {theme!r}; expected one of {tuple(THEMES)}.")
    t = _theme(theme)
    layers = _backdrop_css(style, t, negative_space)

    overlay = ""
    if any((eyebrow, title, subtitle)):
        from scripts.visuals.html.design import esc

        side_css = "right:0;align-items:flex-end;text-align:right;" if negative_space != "left" \
            else "left:0;align-items:flex-start;text-align:left;"
        parts = []
        if eyebrow:
            parts.append(
                f'<div style="font:700 {round(width*0.018)}px Inter,sans-serif;'
                f'letter-spacing:.12em;text-transform:uppercase;color:{t["ACCENT"]}">{esc(eyebrow)}</div>'
            )
        if title:
            parts.append(
                f'<div style="font:800 {round(width*0.052)}px Inter,sans-serif;'
                f'line-height:1.08;color:{t["TEXT"]};margin-top:.35em">{esc(title)}</div>'
            )
        if subtitle:
            parts.append(
                f'<div style="font:500 {round(width*0.024)}px Inter,sans-serif;'
                f'line-height:1.3;color:{t["TEXT_2"]};margin-top:.6em">{esc(subtitle)}</div>'
            )
        overlay = (
            f'<div style="position:absolute;top:0;bottom:0;{side_css}width:36%;'
            f'display:flex;flex-direction:column;justify-content:center;'
            f'padding:0 {round(width*0.03)}px">{"".join(parts)}</div>'
        )

    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ background: #ffffff; }}
  #stage {{
    position: relative;
    width: {width}px; height: {height}px;
    background: {layers};
    background-blend-mode: normal;
  }}
</style></head>
<body><div id="stage" data-style="{style}" data-theme="{theme}">{overlay}</div></body></html>"""


def render_hero(
    out_path: str | Path,
    *,
    style: str = "gradient-mesh",
    theme: str = "default",
    width: int = 1536,
    height: int = 1024,
    negative_space: str = "right",
    eyebrow: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc = build_hero_html(style, theme, width, height, negative_space, eyebrow, title, subtitle)
    from scripts.visuals.html.render import render_html_to_png

    render_html_to_png(doc, out_path, scale=2)

    has_overlay = bool(eyebrow or title or subtitle)
    meta = {
        "mode": "programmatic",
        "deterministic": True,
        "license": "generated-own (no third-party assets)",
        "safety_reviewed": "n/a (abstract backdrop, no people/scenes)",
        "style": style,
        "theme": theme,
        "size": f"{width}x{height}",
        "negative_space": negative_space,
        "has_overlay": has_overlay,
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "family": "ai-generated-imagery",
        "renderer": "scripts.visuals.generated.programmatic",
        "constraints": ["brand-color-fidelity", "reserved negative space"]
        + ([] if has_overlay else ["no-embedded-text"]),
    }
    Path(str(out_path) + ".json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[programmatic hero] {out_path} (style={style}, theme={theme}, overlay={has_overlay})")
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render a deterministic hero/backdrop image.")
    parser.add_argument("--out", required=True, help="Output PNG path.")
    parser.add_argument("--style", default="gradient-mesh", choices=STYLES)
    parser.add_argument("--theme", default="default", choices=tuple(THEMES))
    parser.add_argument("--width", type=int, default=1536)
    parser.add_argument("--height", type=int, default=1024)
    parser.add_argument(
        "--negative-space", default="right", choices=("left", "right", "none")
    )
    parser.add_argument("--eyebrow", default=None, help="Optional CSS-overlay eyebrow text.")
    parser.add_argument("--title", default=None, help="Optional CSS-overlay title text.")
    parser.add_argument("--subtitle", default=None, help="Optional CSS-overlay subtitle text.")
    args = parser.parse_args(argv)
    render_hero(
        args.out,
        style=args.style,
        theme=args.theme,
        width=args.width,
        height=args.height,
        negative_space=args.negative_space,
        eyebrow=args.eyebrow,
        title=args.title,
        subtitle=args.subtitle,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
