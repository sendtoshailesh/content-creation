"""Style adapters: render the same content in genuinely different visual styles.

Each adapter is a thin, deterministic renderer that shares the design tokens but
produces a distinct *look* (medium), decoupled from the infographic *type*.

Adapters in this package:
    typographic   - text-as-art via HTML/CSS + Chromium
    sketch_mpl    - hand-drawn charts/timelines via matplotlib xkcd()
    sketch_rough  - hand-drawn diagrams via Rough.js (Chromium bridge)
"""
