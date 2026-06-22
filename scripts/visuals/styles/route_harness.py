"""Route the harness-engineering blog visual pack through the style router.

Run from the repo root so the package import resolves:

    PYTHONPATH=. python3 scripts/visuals/styles/route_harness.py

Builds one AssetRequest per planned blog visual (v01-v08), routes the whole pack so
package-level diversity is enforced, prints the per-asset style decision table, the
package style matrix, the moderator move, and the diagram-as-code engine availability
(diagram-as-code is opt-in and only renderable when an engine is installed).
"""

from __future__ import annotations

from scripts.visuals.styles import available_engine
from scripts.visuals.styles.router import (
    AssetRequest,
    moderator_move,
    route,
    style_matrix,
)

# One request per planned blog companion visual. infographic_type / audience /
# data_density are chosen from each asset's art-direction brief in
# content/visual-opportunity-map.md. Burning questions avoid the diagram-as-code
# trigger keywords (pipeline/graph/depend/topo) because no diagram engine is installed.
ASSETS = [
    AssetRequest(
        id="v01-harness-quote",
        burning_question="Why does it matter that the developer was the harness?",
        infographic_type="quote",
        audience="broad",
        platform="blog",
        data_density="low",
    ),
    AssetRequest(
        id="v02-maturity-arc",
        burning_question="How did AI coding mature from autocomplete into harness engineering?",
        infographic_type="timeline",
        audience="developer",
        platform="blog",
        data_density="medium",
    ),
    AssetRequest(
        id="v03-harness-anatomy",
        burning_question="What parts make an AI agent more than a model?",
        infographic_type="architecture",
        audience="architect",
        platform="blog",
        data_density="medium",
    ),
    AssetRequest(
        id="v04-building-blocks",
        burning_question="What should a team actually build around the model?",
        infographic_type="comparison",
        audience="tech-lead",
        platform="blog",
        data_density="high",
    ),
    AssetRequest(
        id="v05-context-switch-cost",
        burning_question="How much efficiency is lost to context switching?",
        infographic_type="statistical",
        audience="exec",
        platform="blog",
        data_density="medium",
    ),
    AssetRequest(
        id="v06-pipeline-case-study",
        burning_question="What does a real harness look like in this repository?",
        infographic_type="concept",
        audience="developer",
        platform="blog",
        data_density="medium",
    ),
    AssetRequest(
        id="v07-risk-limits",
        burning_question="What are the honest limits and risks of harness engineering?",
        infographic_type="mood",
        audience="tech-lead",
        platform="blog",
        data_density="low",
    ),
    AssetRequest(
        id="v08-playbook-checklist",
        burning_question="What can I ship this week to start harness engineering?",
        infographic_type="checklist",
        audience="developer",
        platform="blog",
        data_density="medium",
    ),
]


def main() -> None:
    decisions = route(ASSETS)
    matrix = style_matrix(decisions)
    overlooked = moderator_move(decisions)

    print("=== Per-asset style decisions ===")
    print(f"{'asset id':<24} {'style_id':<22} {'renderer'}")
    print("-" * 78)
    prev = None
    for d in decisions:
        flag = "  <-- ADJACENT REPEAT" if d.style_id == prev else ""
        print(f"{d.id:<24} {d.style_id:<22} {d.renderer}{flag}")
        prev = d.style_id

    print("\n=== Package style matrix (histogram) ===")
    for style, count in sorted(matrix.items()):
        print(f"{style:<24} {count}")
    print(f"\nstyles represented: {len(matrix)} of 6")

    print("\n=== Moderator move (overlooked style) ===")
    print(overlooked if overlooked else "(none — package already varied)")

    print("\n=== diagram-as-code engine availability ===")
    engine = available_engine()
    print(engine if engine else "None installed (d2 / dot / mmdc all absent)")


if __name__ == "__main__":
    main()
