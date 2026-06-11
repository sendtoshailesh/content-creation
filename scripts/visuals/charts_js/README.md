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
