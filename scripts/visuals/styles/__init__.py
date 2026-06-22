"""Style adapters: render the same content in genuinely different visual styles.

Each adapter is a thin, deterministic renderer that shares the design tokens but
produces a distinct *look* (medium), decoupled from the infographic *type*. This is the
"HOW it looks" axis of the Visual Versatility System (see
``agents-and-skills/visual-versatility-system.md``).

Six first-class styles (the ``visual-style-router`` picks one per asset):

    data-exhibit           - clean cards / bars / metrics (HTML/CSS + Chromium)
    typographic            - text-as-art, oversized editorial type
    hand-drawn             - sketchy boxes / arrows / charts (Rough.js or matplotlib xkcd)
    blueprint              - dark technical schematic, grid paper, mono labels
    editorial-illustration - flat-vector metaphor scene, text overlaid (never baked)
    diagram-as-code        - real flow / architecture graphs from text (D2 / Mermaid / dot)

``STYLE_REGISTRY`` maps each ``style_id`` to the renderer entrypoints it offers, so the
router and renderer can dispatch by id and the reviewer can verify package diversity.
``data-exhibit`` intentionally has no adapter here — it is the existing
``scripts/visuals/html`` path, referenced by id for completeness.
"""

from __future__ import annotations

from scripts.visuals.styles.blueprint import blueprint_hub_and_beams
from scripts.visuals.styles.diagram_as_code import available_engine, render_diagram
from scripts.visuals.styles.editorial import editorial_guardrail
from scripts.visuals.styles.sketch_mpl import sketch_checklist, sketch_maturity_steps
from scripts.visuals.styles.sketch_rough import sketch_anatomy, sketch_flow_pipeline
from scripts.visuals.styles.typographic import typographic_quote

# style_id -> {"renderer": engine-name, "module": ..., "entrypoints": {composition: callable}}
# ``renderer`` is the medium the reviewer/inspector expects; ``entrypoints`` are the
# concrete composition factories currently available for that style.
STYLE_REGISTRY: dict[str, dict] = {
    "data-exhibit": {
        "renderer": "html-css-chromium",
        "module": "scripts.visuals.html",
        "entrypoints": {},  # uses the existing scripts/visuals/html page() builder
    },
    "typographic": {
        "renderer": "html-css-chromium",
        "module": "scripts.visuals.styles.typographic",
        "entrypoints": {"quote": typographic_quote},
    },
    "hand-drawn": {
        "renderer": "rough.js / matplotlib-xkcd",
        "module": "scripts.visuals.styles.sketch_rough + sketch_mpl",
        "entrypoints": {
            "anatomy": sketch_anatomy,
            "flow": sketch_flow_pipeline,
            "maturity_steps": sketch_maturity_steps,
            "checklist": sketch_checklist,
        },
    },
    "blueprint": {
        "renderer": "html-css-chromium+svg",
        "module": "scripts.visuals.styles.blueprint",
        "entrypoints": {"hub_and_beams": blueprint_hub_and_beams},
    },
    "editorial-illustration": {
        "renderer": "html-css-chromium+svg",
        "module": "scripts.visuals.styles.editorial",
        "entrypoints": {"guardrail": editorial_guardrail},
    },
    "diagram-as-code": {
        "renderer": "d2 / mermaid / graphviz (opt-in)",
        "module": "scripts.visuals.styles.diagram_as_code",
        "entrypoints": {"diagram": render_diagram},
    },
}

STYLE_IDS = tuple(STYLE_REGISTRY)

__all__ = [
    "STYLE_REGISTRY",
    "STYLE_IDS",
    "available_engine",
    "render_diagram",
    "typographic_quote",
    "sketch_anatomy",
    "sketch_flow_pipeline",
    "sketch_maturity_steps",
    "sketch_checklist",
    "blueprint_hub_and_beams",
    "editorial_guardrail",
]
