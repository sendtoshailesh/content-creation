"""Diagram-as-code style: real flow / architecture / dependency graphs from text.

A distinct *medium* for pipelines, dependency graphs, and cloud topologies. The source
is plain text (D2, Mermaid, or Graphviz DOT) and a layout engine places everything, so
there is no hand-computed geometry to invert. Everything is pre-rendered to a static PNG
server-side; no client JS ever ships to a published page.

Engines (opt-in, auto-detected in preference order):
    d2   - MPL-2.0, has a native *sketch* mode + many themes  (``brew install d2``)
    dot  - Graphviz, dense graphs with real layout            (``brew install graphviz``)
    mmdc - Mermaid CLI, standard flow/sequence/class diagrams (``npm i -g @mermaid-js/mermaid-cli``)

If none is installed the adapter raises a clear, actionable error naming the install
command — it never silently falls back to a different look.
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

# Preference order: D2 (sketch mode) > Graphviz (dense) > Mermaid (standard).
_ENGINES = ("d2", "dot", "mmdc")

_INSTALL_HINT = {
    "d2": "brew install d2",
    "dot": "brew install graphviz",
    "mmdc": "npm install -g @mermaid-js/mermaid-cli",
}


def available_engine() -> str | None:
    """Return the first installed diagram engine in preference order, or None."""
    for engine in _ENGINES:
        if shutil.which(engine):
            return engine
    return None


def _require_engine(prefer: str | None) -> str:
    if prefer:
        if shutil.which(prefer):
            return prefer
        raise RuntimeError(
            f"diagram-as-code engine '{prefer}' not found. Install it with: "
            f"{_INSTALL_HINT.get(prefer, prefer)}"
        )
    engine = available_engine()
    if engine:
        return engine
    hints = "  |  ".join(f"{e}: {_INSTALL_HINT[e]}" for e in _ENGINES)
    raise RuntimeError(
        "diagram-as-code requires one of d2 / graphviz(dot) / mermaid(mmdc); none is "
        f"installed (all are opt-in / offline once installed). Install one of:\n  {hints}"
    )


def _render_d2(source: str, out_path: Path, *, sketch: bool, theme_id: int) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".d2", delete=False) as fh:
        fh.write(source)
        src = fh.name
    cmd = ["d2", f"--theme={theme_id}", f"--scale=2"]
    if sketch:
        cmd.append("--sketch")
    cmd += [src, str(out_path)]
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    Path(src).unlink(missing_ok=True)


def _render_dot(source: str, out_path: Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".dot", delete=False) as fh:
        fh.write(source)
        src = fh.name
    subprocess.run(
        ["dot", "-Tpng", "-Gdpi=320", src, "-o", str(out_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    Path(src).unlink(missing_ok=True)


def _render_mmdc(source: str, out_path: Path, *, theme: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".mmd", delete=False) as fh:
        fh.write(source)
        src = fh.name
    subprocess.run(
        ["mmdc", "-i", src, "-o", str(out_path), "-t", theme, "-b", "white", "-s", "2"],
        check=True,
        capture_output=True,
        text=True,
    )
    Path(src).unlink(missing_ok=True)


def render_diagram(
    out_path: str | Path,
    *,
    source: str,
    lang: str = "d2",
    sketch: bool = True,
    theme: str = "default",
    prefer_engine: str | None = None,
) -> Path:
    """Render a text diagram (``lang`` = ``d2`` | ``dot`` | ``mermaid``) to a static PNG.

    ``sketch`` requests D2's hand-drawn mode (ignored by other engines). The engine is
    auto-detected unless ``prefer_engine`` pins one. Raises ``RuntimeError`` with an
    install hint when no engine is available — never falls back to a different look.
    """
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    engine = _require_engine(prefer_engine or _lang_default_engine(lang))

    # Map our 5 named themes onto each engine's theme space (best-effort, deterministic).
    theme_idx = {"default": 0, "ocean": 4, "sunset": 5, "forest": 8, "midnight": 200}.get(theme, 0)
    mermaid_theme = "default" if theme in ("default", "ocean", "forest") else "dark"

    if engine == "d2":
        _render_d2(source, out_path, sketch=sketch, theme_id=theme_idx)
    elif engine == "dot":
        _render_dot(source, out_path)
    elif engine == "mmdc":
        _render_mmdc(source, out_path, theme=mermaid_theme)
    return out_path


def _lang_default_engine(lang: str) -> str | None:
    return {"d2": "d2", "dot": "dot", "graphviz": "dot", "mermaid": "mmdc", "mmd": "mmdc"}.get(
        lang.lower()
    )
