"""Pilot: re-render ALL EIGHT harness-engineering visuals, each in a distinct style.

Proves the Visual Versatility System (see
``agents-and-skills/visual-versatility-system.md``) end-to-end: the same source content
that today renders as eight near-identical data-exhibits becomes eight visibly different
looks, chosen by content type + audience and rotated for package diversity.

    v01 quote            -> typographic           (HTML/CSS text-as-art)
    v02 maturity arc     -> hand-drawn sketch      (matplotlib xkcd staircase)
    v03 anatomy          -> hand-drawn diagram     (Rough.js)
    v04 four beams       -> blueprint              (technical schematic, HTML/CSS+SVG)
    v05 40% stat         -> data-exhibit           (the one refined clean exhibit)
    v06 pipeline study   -> hand-drawn flow        (Rough.js)
    v07 risk limits      -> editorial illustration (flat metaphor scene)
    v08 playbook         -> hand-drawn checklist   (matplotlib xkcd)

Run from the repo root:
    PYTHONPATH=. python content/visuals/render_harness_styles_pilot.py
"""

from __future__ import annotations

from pathlib import Path

from scripts.visuals.html.render import render_html_to_png
from scripts.visuals.styles.blueprint import blueprint_hub_and_beams
from scripts.visuals.styles.editorial import editorial_guardrail
from scripts.visuals.styles.sketch_mpl import sketch_checklist, sketch_maturity_steps
from scripts.visuals.styles.sketch_rough import sketch_anatomy, sketch_flow_pipeline
from scripts.visuals.styles.typographic import typographic_quote

# The existing single-style factory supplies the one refined data-exhibit (v05).
from content.visuals.render_harness_engineering import v05_context_switch_cost

OUT_DIR = Path(__file__).resolve().parent / "harness-engineering" / "pilot"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    # v01 quote -> typographic text-as-art.
    written.append(
        typographic_quote(
            OUT_DIR / "v01-typographic.png",
            kicker="core reframe",
            quote="So far, the developer was the harness.",
            accent_word="harness",
            context=(
                "Harness engineering moves that hidden scaffolding into versioned, "
                "reviewable workflow artifacts."
            ),
            source="Source: InfoQ podcast with Birgitta Boeckeler, Jun 2026",
            theme="default",
        )
    )

    # v02 maturity arc -> hand-drawn ascending steps.
    written.append(
        sketch_maturity_steps(
            OUT_DIR / "v02-sketch.png",
            title="From autocomplete to harness engineering",
            subtitle="Each step makes more of the workflow explicit.",
            stages=[
                ("1", "Autocomplete", "Next line or function"),
                ("2", "Vibe coding", "Larger chunks, weak ownership"),
                ("3", "Context engineering", "Better input context"),
                ("4", "Harness engineering", "Context plus feedback loops"),
            ],
            source="Sources: InfoQ podcast; QCon London 2025; 2025 context-engineering wave",
            theme="ocean",
        )
    )

    # v03 anatomy -> hand-drawn Rough.js diagram.
    written.append(sketch_anatomy(OUT_DIR / "v03-rough.png", theme="default"))

    # v04 building blocks -> blueprint technical schematic.
    written.append(
        blueprint_hub_and_beams(
            OUT_DIR / "v04-blueprint.png",
            title="Four beams around the model",
            subtitle="A harness is a system, not a longer prompt.",
            center_label="MODEL",
            beams=[
                ("Custom agents", ".agent.md workflows", "Reviewable"),
                ("Skills", "Lazy-loaded context", "Angular v20"),
                ("Routing", "HyDRA economics", "72.5% savings"),
                ("Orchestration", "Selective delegation", "23% fewer failures"),
            ],
            source="Sources: GitHub Blog Jun 2026; InfoQ Angular skills Jun 2026",
            theme="default",
        )
    )

    # v05 context-switch cost -> the one refined data-exhibit (existing factory).
    written.append(
        render_html_to_png(
            v05_context_switch_cost(), OUT_DIR / "v05-exhibit.png", scale=2
        )
    )

    # v06 pipeline case study -> hand-drawn Rough.js flow.
    written.append(sketch_flow_pipeline(OUT_DIR / "v06-rough-flow.png", theme="default"))

    # v07 risk limits -> editorial metaphor illustration.
    written.append(
        editorial_guardrail(
            OUT_DIR / "v07-editorial.png",
            kicker="honest limits",
            title="Harnesses guide models. They don't prove correctness.",
            formula="Risk = probability x impact x detectability",
            gap_note=(
                "Behavior harnesses stay weak when agents write their own tests."
            ),
            source="Source: InfoQ podcast and Angular skills coverage critique",
            theme="midnight",
        )
    )

    # v08 playbook -> hand-drawn checklist.
    written.append(
        sketch_checklist(
            OUT_DIR / "v08-sketch-checklist.png",
            title="Start with one repeatable harness",
            subtitle="The first win is narrow, reviewable, and easy to validate.",
            steps=[
                ("1", "Choose one repeated AI task"),
                ("2", "Move reusable context into an agent or skill"),
                ("3", "Add one automated feedback signal"),
                ("4", "Review the harness like production code"),
                ("5", "When it fails, improve the harness first"),
            ],
            source="Source: InfoQ podcast and practitioner playbook from this run",
            theme="forest",
        )
    )

    for p in written:
        print(f"wrote {p}")


if __name__ == "__main__":
    main()
