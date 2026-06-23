"""Final styled render of the eight harness-engineering blog visuals.

Each visual is rendered in the STYLE assigned by the Visual Versatility System
router (see ``content/visual-style-map.md`` and
``scripts/visuals/styles/route_harness.py``). This replaces the rejected
single-style data-exhibit pack with a genuinely mixed, package-diverse set:

    v01-harness-quote        -> typographic            (text-as-art)
    v02-maturity-arc         -> hand-drawn             (matplotlib xkcd steps)
    v03-harness-anatomy      -> blueprint              (technical schematic)
    v04-building-blocks      -> data-exhibit           (clean metric exhibit)
    v05-context-switch-cost  -> typographic            (oversized 40% stat)
    v06-pipeline-case-study  -> hand-drawn             (Rough.js flow)
    v07-risk-limits          -> editorial-illustration (flat metaphor scene)
    v08-playbook-checklist   -> hand-drawn             (matplotlib xkcd)

Sequence has no adjacent style repeats; 5 of 6 styles used (diagram-as-code is
the moderator's overlooked style but its engines are not installed, so v06 stays
a hand-drawn flow).

Run from the repo root:
    PYTHONPATH=. python content/visuals/render_harness_engineering_styled.py
"""

from __future__ import annotations

from pathlib import Path

from scripts.visuals.html.render import render_html_to_png
from scripts.visuals.styles.blueprint import blueprint_hub_and_beams
from scripts.visuals.styles.editorial import editorial_guardrail
from scripts.visuals.styles.sketch_mpl import sketch_checklist, sketch_maturity_steps
from scripts.visuals.styles.sketch_rough import sketch_flow_pipeline
from scripts.visuals.styles.typographic import typographic_quote

# Reuse the refined data-exhibit factory for v04 (the one clean exhibit).
from content.visuals.render_harness_engineering import v04_building_blocks

OUT_DIR = Path(__file__).resolve().parent / "harness-engineering"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    # v01 quote -> typographic text-as-art.
    written.append(
        typographic_quote(
            OUT_DIR / "v01-harness-quote.png",
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
            OUT_DIR / "v02-maturity-arc.png",
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

    # v03 anatomy -> blueprint schematic: model hub wrapped by the harness rails.
    written.append(
        blueprint_hub_and_beams(
            OUT_DIR / "v03-harness-anatomy.png",
            title="What makes an agent more than a model",
            subtitle="Feed-forward (top) shapes the first move. Feedback (bottom) corrects it.",
            center_label="MODEL",
            beams=[
                ("Feed-forward", "Conventions, specs, examples", "Better first move"),
                ("Context", "Architecture + design systems", "Lazy-loaded"),
                ("Feedback", "Tests, types, static analysis", "Auto-correction"),
                ("Review loop", "Adversarial gates before humans", "Cheap rejects"),
            ],
            source="Source: InfoQ podcast, feed-forward and feedback framework",
            eyebrow="anatomy",
            center_sub="the core generator",
            theme="default",
        )
    )

    # v04 building blocks -> the one refined data-exhibit (existing factory).
    written.append(
        render_html_to_png(
            v04_building_blocks(), OUT_DIR / "v04-building-blocks.png", scale=2
        )
    )

    # v05 context-switch cost -> typographic oversized stat.
    written.append(
        typographic_quote(
            OUT_DIR / "v05-context-switch-cost.png",
            kicker="cost of ad-hoc work",
            quote="Up to 40% of focus is lost to context switching.",
            accent_word="40%",
            context=(
                "Private prompting rebuilds that state every session. A versioned "
                "harness keeps context, tools, and checks reusable."
            ),
            source="Source: Towards Data Science, citing APA multitasking research",
            theme="sunset",
        )
    )

    # v06 pipeline case study -> hand-drawn Rough.js flow.
    written.append(
        sketch_flow_pipeline(OUT_DIR / "v06-pipeline-case-study.png", theme="default")
    )

    # v07 risk limits -> editorial metaphor illustration.
    written.append(
        editorial_guardrail(
            OUT_DIR / "v07-risk-limits.png",
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
            OUT_DIR / "v08-playbook-checklist.png",
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
