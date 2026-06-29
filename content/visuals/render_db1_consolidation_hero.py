#!/usr/bin/env python3
"""Render db1-five-to-one-consolidation-hero.svg (v01, P0 — THE STAR).

Five labeled specialist source boxes on the left, each tagged with the Postgres
feature that absorbs it, converge via arrows into ONE central Postgres engine on
the right. Headline: "Five systems, one engine — 5 -> 1".

Grounding: content/reference-brief.md §A-B, content/just-use-postgres.md §3.
Design tokens: .github/copilot-instructions.md (exact hexes below).
SVG is generated programmatically (no terminal heredoc). Reproducible:

    python3 content/visuals/render_db1_consolidation_hero.py
"""
from __future__ import annotations

import html
from pathlib import Path

# --- Shared design tokens (exact) -------------------------------------------
BG = "#ffffff"
ACCENT = "#1f6feb"      # blue  -> Postgres target
ACCENT_2 = "#0d9488"    # teal
ACCENT_3 = "#7c3aed"    # purple
WARN = "#dc2626"        # red (reserved: walls only; unused here)
SUCCESS = "#16a34a"     # green (reserved: the consolidation win)
TEXT = "#1e293b"
TEXT_2 = "#475569"
MUTED = "#94a3b8"
GRID = "#e5e7eb"
LIGHT_BG = "#f8fafc"
BLUE_BG = "#dbeafe"
TEAL_BG = "#ccfbf1"
PURPLE_BG = "#ede9fe"
RED_BG = "#fee2e2"
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"

W, H = 1600, 1000


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def text(x, y, s, *, size=26, weight=400, fill=TEXT, anchor="middle",
         ls="0", family=FONT):
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
        f'letter-spacing="{ls}">{esc(s)}</text>'
    )


def rrect(x, y, w, h, r, *, fill, stroke="none", sw=0):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def converge_arrow(x1, y1, x2, y2, color):
    """A gentle quadratic arrow from a source card to the engine focal point."""
    mx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    # control point pulled toward the focal y so arrows fan smoothly inward
    path = f"M {x1} {y1} Q {mx} {y1} {x2} {y2}"
    return (
        f'<path d="{path}" fill="none" stroke="{color}" stroke-width="4" '
        f'opacity="0.85" marker-end="url(#arrow)"/>'
    )


def elephant(ex, ey, k, fill):
    """Clean single-fill Postgres elephant silhouette from primitives (facing left)."""
    parts = []
    # ear
    parts.append(f'<ellipse cx="{ex-54*k}" cy="{ey-12*k}" rx="{22*k}" ry="{28*k}" fill="{fill}"/>')
    # body
    parts.append(f'<ellipse cx="{ex}" cy="{ey}" rx="{72*k}" ry="{46*k}" fill="{fill}"/>')
    # head
    parts.append(f'<circle cx="{ex-62*k}" cy="{ey-4*k}" r="{40*k}" fill="{fill}"/>')
    # trunk (thick round-cap stroke curving down)
    parts.append(
        f'<path d="M {ex-92*k} {ey-2*k} Q {ex-112*k} {ey+30*k} {ex-100*k} {ey+62*k}" '
        f'fill="none" stroke="{fill}" stroke-width="{20*k}" stroke-linecap="round"/>'
    )
    # tusk
    parts.append(
        f'<path d="M {ex-84*k} {ey+18*k} Q {ex-94*k} {ey+30*k} {ex-98*k} {ey+38*k}" '
        f'fill="none" stroke="{fill}" stroke-width="{6*k}" stroke-linecap="round"/>'
    )
    # legs
    for lx in (-46, -16, 18, 48):
        parts.append(
            f'<rect x="{ex+lx*k-9*k}" y="{ey+30*k}" width="{18*k}" height="{40*k}" '
            f'rx="{6*k}" fill="{fill}"/>'
        )
    # tail
    parts.append(
        f'<path d="M {ex+70*k} {ey-2*k} Q {ex+92*k} {ey+10*k} {ex+86*k} {ey+34*k}" '
        f'fill="none" stroke="{fill}" stroke-width="{6*k}" stroke-linecap="round"/>'
    )
    return "".join(parts)


def build_svg() -> str:
    # Five sources (workload -> Postgres feature). Token-compliant accent rotation;
    # WARN/SUCCESS never used on a source (reserved for walls / the win).
    sources = [
        ("Vectors", "pgvector", "HNSW + IVFFlat; ACID + JOINs + PITR", ACCENT_3, PURPLE_BG),
        ("Queues", "pgmq", "SQS-style; exactly-once in visibility timeout", ACCENT_2, TEAL_BG),
        ("Time-series", "TimescaleDB", "hypertables; 90%+ columnstore compression", ACCENT, BLUE_BG),
        ("Search", "Full-text (tsvector)", "tsvector + GIN; hybrid w/ pgvector", ACCENT_3, PURPLE_BG),
        ("Documents", "JSONB", "binary documents + GIN indexing", ACCENT_2, TEAL_BG),
    ]

    out = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">'
    )
    out.append(
        '<defs>'
        '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{ACCENT}"/></marker>'
        '</defs>'
    )
    out.append(rrect(0, 0, W, H, 0, fill=BG))

    # --- Title -------------------------------------------------------------
    out.append(text(70, 78, "Five systems, one engine", size=52, weight=800,
                    fill=TEXT, anchor="start"))
    out.append(text(72, 124, "Five specialist datastores collapse into one ACID Postgres.",
                    size=25, weight=400, fill=TEXT_2, anchor="start"))
    # big 5 -> 1 ribbon, top-right
    out.append(rrect(1170, 40, 360, 70, 14, fill=LIGHT_BG, stroke=GRID, sw=2))
    out.append(text(1350, 88, "5  ->  1", size=44, weight=800, fill=ACCENT))

    # Column headers
    out.append(text(290, 188, "FIVE SOURCE SYSTEMS", size=21, weight=800,
                    fill=MUTED, ls="0.08em"))
    out.append(text(1300, 188, "ONE ENGINE", size=21, weight=800,
                    fill=ACCENT, ls="0.08em"))

    # --- Source cards ------------------------------------------------------
    card_x, card_w = 70, 470
    top, card_h, gap = 210, 132, 16
    focal_x, focal_y = 1078, 560   # left edge of engine panel
    card_rights = []
    for i, (work, feat, detail, color, fillbg) in enumerate(sources):
        y = top + i * (card_h + gap)
        out.append(rrect(card_x, y, card_w, card_h, 16, fill=fillbg, stroke=color, sw=2.5))
        # accent spine
        out.append(rrect(card_x, y, 10, card_h, 5, fill=color))
        # workload name
        out.append(text(card_x + 34, y + 44, work, size=30, weight=800,
                        fill=TEXT, anchor="start"))
        # arrow glyph + feature tag pill
        out.append(text(card_x + 34, y + 84, "->", size=26, weight=800,
                        fill=color, anchor="start"))
        # extension pill
        pill_x = card_x + 78
        pill_w = 16 + len(feat) * 14.5
        out.append(rrect(pill_x, y + 62, pill_w, 34, 17, fill=color))
        out.append(text(pill_x + pill_w / 2, y + 85, feat, size=22, weight=800,
                        fill="#ffffff"))
        # detail line
        out.append(text(card_x + 34, y + 116, detail, size=17, weight=400,
                        fill=TEXT_2, anchor="start"))
        card_rights.append((card_x + card_w, y + card_h / 2))

    # --- Convergence arrows ------------------------------------------------
    for (rx, ry) in card_rights:
        out.append(converge_arrow(rx + 8, ry, focal_x - 6, focal_y, ACCENT))

    # --- Central Postgres engine panel ------------------------------------
    eng_x, eng_y, eng_w, eng_h = 1078, 300, 452, 520
    out.append(rrect(eng_x, eng_y, eng_w, eng_h, 28, fill=ACCENT, stroke="#1551b5", sw=3))
    ecx = eng_x + eng_w / 2
    # eyebrow
    out.append(text(ecx, eng_y + 56, "ONE ACID ENGINE", size=22, weight=800,
                    fill=BLUE_BG, ls="0.1em"))
    # elephant silhouette (white on blue)
    out.append(elephant(ecx, eng_y + 188, 1.05, "#ffffff"))
    # label
    out.append(text(ecx, eng_y + 320, "PostgreSQL", size=46, weight=800, fill="#ffffff"))
    # divider
    out.append(f'<line x1="{eng_x+44}" y1="{eng_y+352}" x2="{eng_x+eng_w-44}" '
               f'y2="{eng_y+352}" stroke="#ffffff" stroke-opacity="0.35" stroke-width="2"/>')
    # tagline (3 lines)
    for j, line in enumerate(["One backup. One failover.",
                              "One security model.",
                              "One on-call. One hire profile."]):
        out.append(text(ecx, eng_y + 392 + j * 36, line, size=24, weight=600,
                        fill="#eaf2ff"))
    # SUCCESS-green consolidation-win check badge
    out.append(f'<circle cx="{eng_x+eng_w-46}" cy="{eng_y+46}" r="26" fill="{SUCCESS}"/>')
    out.append(
        f'<path d="M {eng_x+eng_w-58} {eng_y+46} l 8 9 l 16 -18" fill="none" '
        f'stroke="#ffffff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    )

    # --- Footnote ----------------------------------------------------------
    out.append(text(70, 968,
                    "PostgreSQL 18 async I/O  ->  up to 3x read throughput.   "
                    "Source: reference-brief.md A-B; verified 2026-06-26.",
                    size=18, weight=400, fill=MUTED, anchor="start"))

    out.append("</svg>")
    return "".join(out)


def main() -> None:
    out_path = Path(__file__).resolve().parent / "db1-five-to-one-consolidation-hero.svg"
    out_path.write_text(build_svg(), encoding="utf-8")
    print(f"wrote {out_path} ({W}x{H})")


if __name__ == "__main__":
    main()
