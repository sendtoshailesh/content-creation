# JS-charting bridge (opt-in)

Render **advanced** chart types that matplotlib handles poorly (sankey, treemap, network/graph,
calendar/heatmap, non-gauge radial) to **static PNG** via ECharts + headless Chromium. Standard
bar/line/scatter/pie charts stay in matplotlib; text-heavy designed visuals stay in
HTML/CSS+Chromium.

## Setup (once)

```bash
cd scripts/visuals/charts_js
npm install            # vendors echarts into ./node_modules (git-ignored)
```

## Use

```bash
# spec.json is a raw ECharts option (https://echarts.apache.org/en/option.html)
python -m scripts.visuals.charts_js.echarts_render --spec spec.json --out content/visuals/foo.png --theme ocean
```

Or from Python:

```python
from scripts.visuals.charts_js.echarts_render import render_echarts
render_echarts(option_dict, "content/visuals/foo.png", theme="ocean")
```

## Guarantees

- **`animation: false` is forced** — an animated chart screenshotted mid-flight exports
  silently-wrong values. This is the critical static-export guardrail.
- Brand series colors are injected when the option has no `color`.
- Output is a static PNG (+ sidecar JSON). **No client JS is shipped to published pages.**
- Charts then go through `visual-reviewer` (the hero-only `inspect_image` no-text check does not
  apply to charts — pass `--allow-text` if you use it).

## MCP chart/diagram servers (opt-in, brand-wired)

Two MCP servers in [`.vscode/mcp.json`](../../../.vscode/mcp.json) extend the pack with
agent-driven generation. They are **drafting/preview** tools — final publish-grade assets still
go through the in-repo renderers and the `visual-reviewer` / REVR gates.

| Server | Package | Role |
|--------|---------|------|
| `chart` | `@antv/mcp-server-chart` | 26+ chart types (sankey, fishbone, mind-map, treemap, network, dual-axis…) beyond matplotlib |
| `mermaid` | `mcp-mermaid` | Validate + render the Mermaid the visual agents already emit |

### Single source of truth for color/font

Both servers draw from the design tokens via a generated theme. Regenerate after any
`tokens.py` change:

```bash
PYTHONPATH=. python3 -m scripts.visuals.brand_theme   # add --theme ocean|sunset|forest|midnight
# writes brand-theme.json (GPT-Vis-SSR) + mermaid-theme.json (Mermaid themeVariables)
```

### `chart` — control colors/fonts via self-hosted GPT-Vis-SSR

By default the AntV server renders through its public service. To enforce brand tokens, run the
bundled self-hosted [GPT-Vis-SSR](https://github.com/antvis/GPT-Vis) endpoint (it loads
`brand-theme.json` and injects the palette/background/font), then point the MCP server at it:

```bash
# 1. regenerate the theme from tokens.py (single source of truth)
PYTHONPATH=. python3 -m scripts.visuals.brand_theme

# 2. start the SSR render endpoint
cd scripts/visuals/charts_js/ssr
npm install        # installs @antv/gpt-vis-ssr + express into ./node_modules (git-ignored)
npm start          # -> http://localhost:3000/api/gpt-vis  (GET /healthz to check)

# 3. point the chart MCP server at it (reload the VS Code window after exporting)
export VIS_REQUEST_SERVER="http://localhost:3000/api/gpt-vis"
# optional: trim the toolset, e.g. export CHART_DISABLED_TOOLS="generate_geographic_map"
```

Leave `VIS_REQUEST_SERVER` unset to use the public renderer (colors then come from the spec, not
the brand theme). Change `PORT` to use a different port.

### `mermaid` — validate fast, finalize on-brand

Use the `mermaid` server to syntax-check and preview diagrams. For brand-grade final output,
rasterize with the token-themed renderer (it already applies `mermaid-theme.json`'s palette):

```bash
python3 -m scripts.visuals.html.render_mermaid <input.mmd> content/visuals/<out>.png
```
