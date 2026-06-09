"""Publish-time QA gate for rendered blog pages.

The visual inspector (``inspect.py``) only checks generated ``#stage`` assets, so
it never looked at the published blog HTML. This checker closes that gap: it
scans published pages for content that will render as raw text instead of a
diagram — most importantly fenced Mermaid blocks emitted as
``<code class="language-mermaid">`` on a page that ships no mermaid.js runtime.

Exit code is non-zero if any problem is found, so it can gate publishing.

Usage:
    python3 -m scripts.visuals.html.check_published <page1.html> [page2.html ...]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Languages that are *diagram* sources, not code samples: if these appear as a
# raw <code class="language-XXX"> block they were meant to be rendered to an
# image and will otherwise show as literal text.
_DIAGRAM_LANGS = ("mermaid", "graphviz", "dot", "plantuml")


def check_page(path: Path) -> list[str]:
    html = path.read_text(errors="ignore")
    problems: list[str] = []

    for lang in _DIAGRAM_LANGS:
        if re.search(rf'class="[^"]*language-{lang}', html):
            has_runtime = lang in html.lower() and re.search(
                rf'<script[^>]*{lang}', html, re.I
            )
            if not has_runtime:
                problems.append(
                    f"raw <code class=\"language-{lang}\"> block with no "
                    f"{lang} runtime <script> on the page — it will render as "
                    f"literal text. Pre-render it to a PNG and embed as <img>."
                )

    # A bare ```lang fence that survived into HTML (converter passthrough).
    for lang in _DIAGRAM_LANGS:
        if f"```{lang}" in html:
            problems.append(
                f"literal ```{lang} fence found in published HTML — the "
                f"markdown converter did not process it."
            )

    return problems


def main(paths: list[str]) -> int:
    if not paths:
        print(__doc__)
        return 2
    failed = False
    for p in paths:
        path = Path(p)
        if not path.exists():
            print(f"[MISS] {p}: file not found")
            failed = True
            continue
        problems = check_page(path)
        if problems:
            failed = True
            print(f"[FAIL] {p}")
            for prob in problems:
                print(f"   - {prob}")
        else:
            print(f"[PASS] {p}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
