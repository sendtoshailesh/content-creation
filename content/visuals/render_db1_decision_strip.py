#!/usr/bin/env python3
"""Render db1-decision-rule-strip.svg (v04, P1 — typographic).

Horizontal 3-step decision strip:
  "Default to Postgres"  ->  "Hitting one of the 4 walls? (name it with a number)"
  -> branches into  "YES -> Specialize" (WARN red)  and  "NO -> Just use Postgres" (SUCCESS green).

Mono-readable, social-card legible, yes/no labeled in text (not color-only).
Grounding: content/just-use-postgres.md §5; visual-style-map.md (v04).
ASCII '->' only (per v04 acceptance criteria). Reproducible:

    python3 content/visuals/render_db1_decision_strip.py
"""
from __future__ import annotations

import html
from pathlib import Path

# --- Shared design tokens (exact) -------------------------------------------
BG = "#ffffff"
ACCENT = "#1f6feb"
ACCENT_2 = "#0d9488"
ACCENT_3 = "#7c3aed"
WARN = "#dc2626"
SUCCESS = "#16a34a"
TEXT = "#1e293b"
TEXT_2 = "#475569"
MUTED = "#94a3b8"
GRID = "#e5e7eb"
LIGHT_BG = "#f8fafc"
BLUE_BG = "#dbeafe"
TEAL_BG = "#ccfbf1"
PURPLE_BG = "#ede9fe"
RED_BG = "#fee2e2"
SUCCESS_BG = "#dcfce7"
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"

W, H = 1600, 720


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def text(x, y, s, *, size=26, weight=400, fill=TEXT, anchor="middle", ls="0"):
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
        f'letter-spacing="{ls}">{esc(s)}</text>'
    )


def rrect(x, y, w, h, r, *, fill, stroke="none", sw=0):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def connector(x1, y1, x2, y2, color):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
        f'stroke-width="6" marker-end="url(#ar_{color[1:]})"/>'
    )


def marker(color):
    return (
        f'<marker id="ar_{color[1:]}" viewBox="0 0 10 10" refX="8" refY="5" '
        f'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{color}"/></marker>'
    )


def build_svg() -> str:
    out = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">'
    )
    out.append("<defs>" + marker(ACCENT) + marker(TEXT_2) + marker(WARN)
               + marker(SUCCESS) + "</defs>")
    out.append(rrect(0, 0, W, H, 0, fill=BG))

    # Eyebrow / title
    out.append(text(W / 2, 64, "THE DECISION RULE", size=22, weight=800,
                    fill=MUTED, ls="0.16em"))

    # --- Node 1: Default to Postgres --------------------------------------
    n1x, n1y, n1w, n1h = 70, 150, 360, 150
    out.append(rrect(n1x, n1y, n1w, n1h, 18, fill=BLUE_BG, stroke=ACCENT, sw=3))
    out.append(text(n1x + n1w / 2, n1y + 64, "Default to", size=28, weight=600, fill=TEXT_2))
    out.append(text(n1x + n1w / 2, n1y + 110, "Postgres", size=48, weight=800, fill=ACCENT))

    # arrow 1 -> 2
    out.append(connector(n1x + n1w + 6, n1y + n1h / 2, 592, n1y + n1h / 2, ACCENT))

    # --- Node 2: the test (decision) --------------------------------------
    n2x, n2y, n2w, n2h = 600, 132, 440, 186
    out.append(rrect(n2x, n2y, n2w, n2h, 18, fill=LIGHT_BG, stroke=TEXT, sw=3))
    out.append(text(n2x + n2w / 2, n2y + 50, "Hitting one of the 4 walls?",
                    size=32, weight=800, fill=TEXT))
    out.append(text(n2x + n2w / 2, n2y + 88, "Name it with a number.",
                    size=24, weight=700, fill=TEXT_2))
    out.append(text(n2x + n2w / 2, n2y + 138, "write rate  /  shard count",
                    size=20, weight=600, fill=MUTED))
    out.append(text(n2x + n2w / 2, n2y + 166, "latency floor  /  scan size",
                    size=20, weight=600, fill=MUTED))

    # Fork point
    fork_x = n2x + n2w + 6
    fork_y = n2y + n2h / 2

    # --- YES branch (WARN red, upper) -------------------------------------
    yx, yy, yw, yh = 1182, 150, 348, 110
    out.append(connector(fork_x, fork_y, yx - 6, yy + yh / 2, WARN))
    out.append(text((fork_x + yx) / 2 - 6, yy + yh / 2 - 18, "YES", size=22,
                    weight=800, fill=WARN))
    out.append(rrect(yx, yy, yw, yh, 16, fill=RED_BG, stroke=WARN, sw=3))
    out.append(text(yx + yw / 2, yy + 50, "-> Specialize.", size=30, weight=800, fill=WARN))
    out.append(text(yx + yw / 2, yy + 84, "Name the wall.", size=22, weight=600, fill=TEXT_2))

    # --- NO branch (SUCCESS green, lower) ---------------------------------
    nx, ny, nw, nh = 1182, 320, 348, 130
    out.append(connector(fork_x, fork_y, nx - 6, ny + nh / 2, SUCCESS))
    out.append(text((fork_x + nx) / 2 - 6, ny + nh / 2 + 30, "NO", size=22,
                    weight=800, fill=SUCCESS))
    out.append(rrect(nx, ny, nw, nh, 16, fill=SUCCESS_BG, stroke=SUCCESS, sw=3))
    out.append(text(nx + nw / 2, ny + 56, "-> Just use", size=28, weight=700, fill=TEXT_2))
    out.append(text(nx + nw / 2, ny + 100, "Postgres.", size=42, weight=800, fill=SUCCESS))

    # --- One-line manifesto + source --------------------------------------
    out.append(rrect(70, 520, 1460, 96, 16, fill=LIGHT_BG, stroke=GRID, sw=2))
    out.append(text(W / 2, 566,
                    "Can't name the wall with a number? You haven't hit one"
                    "  ->  just use Postgres.",
                    size=28, weight=800, fill=TEXT))
    out.append(text(W / 2, 600, "The four walls: write throughput  /  planet-scale "
                    "sharding  /  sub-ms key-value  /  petabyte OLAP.",
                    size=19, weight=500, fill=TEXT_2))
    out.append(text(70, 680, "Source: just-use-postgres.md (the decision rule); "
                    "verified 2026-06-26.", size=17, fill=MUTED, anchor="start"))

    out.append("</svg>")
    return "".join(out)


def main() -> None:
    out_path = Path(__file__).resolve().parent / "db1-decision-rule-strip.svg"
    out_path.write_text(build_svg(), encoding="utf-8")
    print(f"wrote {out_path} ({W}x{H})")


if __name__ == "__main__":
    main()
