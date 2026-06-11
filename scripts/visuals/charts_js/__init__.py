"""Opt-in JS-charting bridge: ECharts authored in Python, rasterized to static PNG via Chromium.

Use this **only** for advanced chart types that matplotlib handles poorly (sankey, treemap,
network/graph, calendar/heatmap, non-gauge radial). Standard bar/line/scatter/pie charts stay
in matplotlib; text-heavy designed visuals stay in HTML/CSS+Chromium.

The chart `option` is authored as a Python dict (brand colors injected), serialized to JSON,
embedded in an HTML page with a vendored ECharts bundle, and screenshotted by the same
Playwright/Chromium pipeline the rest of the visuals use. Output is a static PNG — **no client
JS is ever shipped to published pages**.

Hard guardrail: animation is forced off (an animated chart screenshotted mid-flight produces a
silently wrong static export). See `scripts/visuals/charts_js/echarts_render.py`.
"""
