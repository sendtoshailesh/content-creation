"""Deterministic style-selection router for the Visual Versatility System.

Implements Section 6 of ``agents-and-skills/visual-versatility-system.md``: pick a
``style_id`` per asset from its burning question / infographic type / audience, enforce
package-level diversity, and surface a *moderator move* (one overlooked style the default
rules missed). Pure, deterministic, no I/O — the ``visual-style-router`` skill and the
``visual-strategist`` agent call this; the renderer dispatches by id via STYLE_REGISTRY.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from scripts.visuals.styles import STYLE_IDS

# Audience -> preferred style order (Section 5 affinities); first match wins as tie-breaker.
AUDIENCE_AFFINITY: dict[str, tuple[str, ...]] = {
    "developer": ("hand-drawn", "diagram-as-code", "blueprint"),
    "ic": ("hand-drawn", "diagram-as-code", "blueprint"),
    "tech-lead": ("blueprint", "diagram-as-code", "data-exhibit"),
    "architect": ("blueprint", "diagram-as-code", "data-exhibit"),
    "manager": ("data-exhibit", "typographic", "editorial-illustration"),
    "exec": ("data-exhibit", "typographic", "editorial-illustration"),
    "broad": ("typographic", "hand-drawn", "editorial-illustration"),
}

_DEFAULT_AFFINITY = ("data-exhibit", "hand-drawn", "typographic")


@dataclass
class AssetRequest:
    """One planned visual the router must style."""

    id: str
    burning_question: str
    infographic_type: str  # process | comparison | timeline | hierarchy | statistical | concept | checklist | quote | architecture | mood
    audience: str          # developer | tech-lead | exec | broad ...
    platform: str = "blog"
    data_density: str = "medium"  # low | medium | high


@dataclass
class StyleDecision:
    id: str
    style_id: str
    renderer: str
    rationale: str
    guardrails: list[str] = field(default_factory=list)


def _base_style(req: AssetRequest) -> str:
    """Steps 1-6 of the router: map intent -> a first-choice style."""
    t = req.infographic_type.lower().strip()
    q = req.burning_question.lower()

    if t in ("statistical", "comparison", "scorecard") or req.data_density == "high":
        return "data-exhibit"
    if t in ("process", "architecture", "hierarchy") and ("pipeline" in q or "graph" in q or "depend" in q or "topo" in q):
        return "diagram-as-code"
    if t in ("quote", "hook") or "one big idea" in q or "quote" in q:
        return "typographic"
    if t in ("concept", "mental-model", "checklist"):
        return "hand-drawn"
    if t in ("architecture", "system") or "how it" in q or "built" in q or "anatomy" in q:
        return "blueprint"
    if t in ("mood", "opener", "metaphor") or req.data_density == "low":
        return "editorial-illustration"
    return "data-exhibit"


def _affinity(audience: str) -> tuple[str, ...]:
    return AUDIENCE_AFFINITY.get(audience.lower().strip(), _DEFAULT_AFFINITY)


def route(assets: list[AssetRequest]) -> list[StyleDecision]:
    """Route a whole package, enforcing 'adjacent visuals must differ in style'."""
    from scripts.visuals.styles import STYLE_REGISTRY

    decisions: list[StyleDecision] = []
    prev_style: str | None = None
    for req in assets:
        style = _base_style(req)
        # Audience tie-break: if the base style is not in this audience's lead set, prefer
        # the audience's top affinity *only* when the base choice is the generic fallback.
        affinity = _affinity(req.audience)
        if style == "data-exhibit" and "data-exhibit" not in affinity[:1] and req.data_density != "high":
            style = affinity[0]
        # Diversity guard: never repeat the previous asset's style.
        if style == prev_style:
            for alt in (*affinity, *STYLE_IDS):
                if alt != prev_style:
                    style = alt
                    break
        renderer = STYLE_REGISTRY[style]["renderer"]
        decisions.append(
            StyleDecision(
                id=req.id,
                style_id=style,
                renderer=renderer,
                rationale=f"type={req.infographic_type}, audience={req.audience}, density={req.data_density}",
                guardrails=_guardrails(style),
            )
        )
        prev_style = style
    return decisions


def _guardrails(style: str) -> list[str]:
    common = ["design tokens only", "320 DPI", "no stray internal labels"]
    extra = {
        "data-exhibit": ["bars not gauges", "one focal number"],
        "typographic": ["TYPE_SCALE display role", "<=12 words"],
        "hand-drawn": ["crisp digits (path-effect Normal)", "edge-to-edge arrows"],
        "blueprint": ["mono labels", "no baked slide numbers"],
        "editorial-illustration": ["NO baked text — overlay only", "~30% negative space"],
        "diagram-as-code": ["pre-render to PNG (no live JS)", "opt-in engine required"],
    }
    return common + extra.get(style, [])


def style_matrix(decisions: list[StyleDecision]) -> dict[str, int]:
    """Package-level style histogram — the reviewer's pre-render diversity input."""
    hist: dict[str, int] = {}
    for d in decisions:
        hist[d.style_id] = hist.get(d.style_id, 0) + 1
    return hist


def moderator_move(decisions: list[StyleDecision]) -> str | None:
    """Co-STORM moderator: name one *unused* style worth trying for variety."""
    used = {d.style_id for d in decisions}
    for style in STYLE_IDS:
        if style not in used and style != "data-exhibit":
            return style
    return None
