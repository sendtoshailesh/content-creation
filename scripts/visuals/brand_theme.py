"""Export the design-token palette as theme payloads for the chart/mermaid MCP servers.

Single source of truth is ``scripts/visuals/tokens.py``. Both the self-hosted
AntV GPT-Vis-SSR render service (used by the ``chart`` MCP server via
``VIS_REQUEST_SERVER``) and the ``mermaid`` MCP server should consume the JSON
emitted here so MCP-generated visuals match the matplotlib/D2/ECharts pack.

Writes two files next to the chart bridge:
  - ``scripts/visuals/charts_js/brand-theme.json``  (GPT-Vis-SSR theme registration)
  - ``scripts/visuals/charts_js/mermaid-theme.json`` (Mermaid initialize themeVariables)

CLI:
    python3 -m scripts.visuals.brand_theme [--theme default]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.visuals.tokens import FONT, get_tokens

_OUT_DIR = Path(__file__).resolve().parent / "charts_js"


def categorical_palette(t: dict[str, str]) -> list[str]:
    """Ordered brand series colors (matches echarts_render.palette)."""
    return [t["ACCENT"], t["ACCENT_2"], t["ACCENT_3"], t["SUCCESS"], t["WARN"]]


def gpt_vis_theme(theme_name: str = "default") -> dict:
    """A GPT-Vis-SSR theme payload derived from the design tokens."""
    t = get_tokens(theme_name)
    return {
        "name": f"how2genmodel-{theme_name}",
        "type": "light",
        "fontFamily": FONT,
        "backgroundColor": t["BG"],
        "textColor": t["TEXT"],
        "subTextColor": t["TEXT_2"],
        "axisLineColor": t["MUTED"],
        "gridColor": t["GRID"],
        "palette": categorical_palette(t),
        "semantic": {
            "warn": t["WARN"],
            "success": t["SUCCESS"],
        },
    }


def mermaid_theme(theme_name: str = "default") -> dict:
    """Mermaid ``initialize`` themeVariables derived from the design tokens.

    Mirrors scripts/visuals/html/render_mermaid.py so MCP previews and the
    brand-grade rasterizer agree on colors.
    """
    t = get_tokens(theme_name)
    return {
        "theme": "base",
        "fontFamily": FONT,
        "themeVariables": {
            "background": t["BG"],
            "primaryColor": t["LIGHT_BG"],
            "primaryBorderColor": t["MUTED"],
            "primaryTextColor": t["TEXT"],
            "lineColor": t["ACCENT"],
            "edgeLabelBackground": t["BG"],
            "fontSize": "16px",
        },
    }


def export(theme_name: str = "default") -> tuple[Path, Path]:
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    chart_path = _OUT_DIR / "brand-theme.json"
    mermaid_path = _OUT_DIR / "mermaid-theme.json"
    chart_path.write_text(
        json.dumps(gpt_vis_theme(theme_name), indent=2) + "\n", encoding="utf-8"
    )
    mermaid_path.write_text(
        json.dumps(mermaid_theme(theme_name), indent=2) + "\n", encoding="utf-8"
    )
    return chart_path, mermaid_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theme", default="default", help="token theme name")
    args = parser.parse_args()
    chart_path, mermaid_path = export(args.theme)
    print(f"wrote {chart_path}")
    print(f"wrote {mermaid_path}")


if __name__ == "__main__":
    main()
