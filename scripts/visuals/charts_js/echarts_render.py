"""Render an ECharts option to a static PNG via Chromium (opt-in advanced-chart bridge).

Python API:
    from scripts.visuals.charts_js.echarts_render import render_echarts
    render_echarts(option_dict, "content/visuals/foo.png", theme="ocean")

CLI:
    python -m scripts.visuals.charts_js.echarts_render --spec spec.json --out out.png --theme ocean

`spec.json` is a raw ECharts option. Brand series colors are injected when the option has no
`color`, and **animation is always forced off** (the critical static-export guardrail).
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import time
from pathlib import Path

from scripts.visuals.tokens import BASE_TOKENS, THEMES

_HERE = Path(__file__).resolve().parent
_REPO = _HERE.parents[2]


def palette(theme: str = "default") -> list[str]:
    """Brand series colors for a theme (ordered for categorical series)."""
    t = THEMES[theme]
    return [t["ACCENT"], t["ACCENT_2"], t["ACCENT_3"], t["SUCCESS"], t["WARN"]]


def locate_echarts() -> str:
    """Return the contents of a vendored echarts.min.js, or raise with install help."""
    candidates = [
        _HERE / "node_modules/echarts/dist/echarts.min.js",
        _REPO / "node_modules/echarts/dist/echarts.min.js",
    ]
    env = os.getenv("ECHARTS_JS")
    if env:
        candidates.insert(0, Path(env))
    for c in candidates:
        if c.is_file():
            return c.read_text(encoding="utf-8")
    raise RuntimeError(
        "echarts.min.js not found. Install it once:\n"
        "  cd scripts/visuals/charts_js && npm install\n"
        "or set ECHARTS_JS to the path of echarts.min.js."
    )


def enforce_static(option: dict, theme: str) -> dict:
    """Force animation off and inject the brand palette when absent. Returns a copy."""
    opt = copy.deepcopy(option)
    opt["animation"] = False  # critical: animated charts screenshot mid-flight -> wrong output
    opt.setdefault("color", palette(theme))
    opt.setdefault("backgroundColor", BASE_TOKENS["BG"])
    # Deterministic guardrail.
    assert opt.get("animation") is False, "animation must be disabled for static export"
    return opt


def _build_html(echarts_js: str, option: dict, width: int, height: int) -> str:
    option_json = json.dumps(option, ensure_ascii=False)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>*{{margin:0}}#stage{{width:{width}px;height:{height}px;background:{BASE_TOKENS['BG']};}}</style>
<script>{echarts_js}</script></head>
<body><div id="stage"></div>
<script>
  const c = echarts.init(document.getElementById('stage'), null, {{renderer:'svg'}});
  c.setOption({option_json});
  window.__done = true;
</script></body></html>"""


def _render_png(html: str, out_path: Path, width: int, height: int) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        page.set_content(html, wait_until="load")
        page.wait_for_function("window.__done === true")
        page.wait_for_timeout(150)
        stage = page.query_selector("#stage")
        if stage is None:
            raise RuntimeError("internal: #stage missing")
        stage.screenshot(path=str(out_path))
        browser.close()


def render_echarts(
    option: dict,
    out_path: str | Path,
    *,
    width: int = 1600,
    height: int = 1000,
    theme: str = "default",
) -> Path:
    if theme not in THEMES:
        raise ValueError(f"Unknown theme {theme!r}; expected one of {tuple(THEMES)}.")
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    opt = enforce_static(option, theme)
    html = _build_html(locate_echarts(), opt, width, height)
    _render_png(html, out_path, width, height)

    meta = {
        "renderer": "scripts.visuals.charts_js.echarts_render",
        "lib": "echarts",
        "theme": theme,
        "size": f"{width}x{height}",
        "animation": False,
        "static_only": True,
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "note": "advanced-chart bridge; standard charts use matplotlib",
    }
    Path(str(out_path) + ".json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[echarts->png] {out_path} (theme={theme}, animation=off)")
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render an ECharts option to static PNG.")
    parser.add_argument("--spec", required=True, help="Path to a JSON ECharts option.")
    parser.add_argument("--out", required=True, help="Output PNG path.")
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--height", type=int, default=1000)
    parser.add_argument("--theme", default="default", choices=tuple(THEMES))
    args = parser.parse_args(argv)

    option = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    render_echarts(option, args.out, width=args.width, height=args.height, theme=args.theme)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
