"""Key-free, offline self-test for the generated-imagery path.

Exercises the **default** (`programmatic`) pipeline end to end without any API key or network:
render a hero backdrop, then run the deterministic inspector and assert it does not FAIL.
Run in CI or locally to keep the path from rotting:

    python -m scripts.visuals.generated.selftest
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

from .inspect_image import inspect_image
from .programmatic import STYLES, render_hero


def run(style: str = "gradient-mesh", theme: str = "ocean") -> int:
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "selftest-hero.png"
        render_hero(out, style=style, theme=theme, negative_space="right")
        assert out.exists() and out.stat().st_size > 1000, "hero PNG not written"
        assert Path(str(out) + ".json").exists(), "sidecar JSON not written"
        findings = inspect_image(out, theme)
        errors = [m for sev, m in findings if sev == "Error"]
        for sev, msg in findings:
            print(f"  [{sev}] {msg}")
        if errors:
            print(f"SELFTEST FAIL ({style}/{theme}): {len(errors)} error(s)")
            return 1
    print(f"SELFTEST PASS ({style}/{theme})")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    style = argv[0] if argv else "gradient-mesh"
    if style not in STYLES:
        print(f"unknown style {style!r}; choose from {STYLES}")
        return 2
    return run(style)


if __name__ == "__main__":
    raise SystemExit(main())
