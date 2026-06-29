#!/usr/bin/env python3
"""Render db1-one-engine-one-story-ops.png (v02, P1 — hand-drawn / Rough.js).

Five duplicated operational stacks (Backup, HA/failover, Security model, On-call,
Skills to hire) x5 collapse into ONE of each. Left = five messy duplicated boxes
per row; right = one clean box per row. Leader/CTO framing: "five ops stories -> one."

Hand-drawn via Rough.js (vendored in scripts/visuals/charts_js/node_modules),
rasterized through headless Chromium at device_scale_factor=2 (no client JS ships).
Grounding: content/just-use-postgres.md §3 ops payoff; visual-style-map.md (v02).
Qualitative by design (one anchor count from the anecdote, not invented).

Run from the repo root so `scripts` is importable:

    PYTHONPATH=. python3 content/visuals/render_db1_ops_card.py
"""
from __future__ import annotations

import json
from pathlib import Path

from scripts.visuals.styles.sketch_rough import _html, _render, _require_rough

# --- Shared design tokens (exact) -------------------------------------------
TOK = {
    "BG": "#ffffff", "ACCENT": "#1f6feb", "ACCENT_2": "#0d9488",
    "ACCENT_3": "#7c3aed", "WARN": "#dc2626", "SUCCESS": "#16a34a",
    "TEXT": "#1e293b", "TEXT_2": "#475569", "MUTED": "#94a3b8",
    "GRID": "#e5e7eb", "LIGHT_BG": "#f8fafc", "BLUE_BG": "#dbeafe",
    "TEAL_BG": "#ccfbf1", "SUCCESS_BG": "#dcfce7",
}
c = {k: json.dumps(v) for k, v in TOK.items()}

W, H = 1600, 1000

ROWS = ["Backup", "HA / failover", "Security model", "On-call", "Skills to hire"]


def build_draw_js() -> str:
    parts = []
    # Title + subtitle
    parts.append(
        f"text(800, 70, 'Five systems  ->  one story', "
        f"{{ size: 46, weight: '800', fill: {c['TEXT']} }});"
    )
    parts.append(
        f"text(800, 116, 'Collapse five datastores and you collapse five copies "
        f"of every ops chore.', {{ size: 22, fill: {c['TEXT_2']} }});"
    )

    # Column headers
    parts.append(f"text(470, 196, 'FIVE SYSTEMS', "
                 f"{{ size: 24, weight: '800', fill: {c['MUTED']}, ls: '0.06em' }});")
    parts.append(f"text(470, 226, '5 of every ops chore', "
                 f"{{ size: 18, fill: {c['MUTED']} }});")
    parts.append(f"text(1234, 196, 'ONE ENGINE', "
                 f"{{ size: 24, weight: '800', fill: {c['ACCENT']}, ls: '0.06em' }});")
    parts.append(f"text(1234, 226, '1 of each', "
                 f"{{ size: 18, fill: {c['ACCENT']} }});")

    # Rows
    centers = [288, 386, 484, 582, 680]
    for name, cy in zip(ROWS, centers):
        # concern label (far left)
        parts.append(
            f"text(64, {cy + 8}, {json.dumps(name)}, "
            f"{{ size: 24, weight: '800', fill: {c['TEXT']}, anchor: 'start' }});"
        )
        # five messy duplicate boxes (muted)
        x0, bw, gap, bh = 296, 54, 14, 54
        for i in range(5):
            bx = x0 + i * (bw + gap)
            parts.append(
                f"box({bx}, {cy - bh/2}, {bw}, {bh}, {c['LIGHT_BG']}, {c['MUTED']});"
            )
        # one clean accent box (right) with a green check
        rbx, rbw, rbh = 1044, 380, 56
        parts.append(
            f"box({rbx}, {cy - rbh/2}, {rbw}, {rbh}, {c['BLUE_BG']}, {c['ACCENT']});"
        )
        parts.append(
            f"text({rbx + rbw/2 + 18}, {cy + 8}, {json.dumps(name)}, "
            f"{{ size: 22, weight: '700', fill: {c['TEXT']} }});"
        )
        # hand-drawn green check inside the clean box (two rough lines)
        chx, chy = rbx + 36, cy
        parts.append(
            f"add(rc.line({chx-14}, {chy}, {chx-2}, {chy+12}, "
            f"{{ roughness: 1.0, stroke: {c['SUCCESS']}, strokeWidth: 4 }}));"
        )
        parts.append(
            f"add(rc.line({chx-2}, {chy+12}, {chx+18}, {chy-14}, "
            f"{{ roughness: 1.0, stroke: {c['SUCCESS']}, strokeWidth: 4 }}));"
        )

    # Big central collapsing arrow: whole left stack -> whole right column
    parts.append(
        f"arrow(672, 484, 1030, 484, {c['ACCENT_2']});"
    )
    parts.append(
        f"text(851, 446, '5  ->  1', "
        f"{{ size: 40, weight: '800', fill: {c['ACCENT_2']} }});"
    )

    # Anchor count callout (from the anecdote, not invented)
    parts.append(f"box(296, 768, 560, 64, {c['SUCCESS_BG']}, {c['SUCCESS']});")
    parts.append(
        f"text(576, 808, '5 backup stories to test  ->  1', "
        f"{{ size: 26, weight: '800', fill: {c['SUCCESS']} }});"
    )

    # Caption
    parts.append(
        f"text(800, 894, \"Every datastore you don't add is an incident class you "
        f"never have.\", {{ size: 23, weight: '700', fill: {c['TEXT']} }});"
    )
    # Source line
    parts.append(
        f"text(800, 944, 'Source: just-use-postgres.md (consolidation dividend); "
        f"qualitative by design.', {{ size: 16, fill: {c['MUTED']} }});"
    )

    return "\n".join(parts)


def main() -> None:
    _require_rough()
    out_path = Path(__file__).resolve().parent / "db1-one-engine-one-story-ops.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    html = _html(W, H, build_draw_js())
    _render(html, out_path, W, H)
    print(f"wrote {out_path} ({W * 2}x{H * 2} px @ device_scale_factor=2)")


if __name__ == "__main__":
    main()
