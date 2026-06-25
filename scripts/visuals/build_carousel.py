"""Assemble a blog's publish-ready visuals into one LinkedIn carousel PDF.

Deterministic, manifest-driven distribution step. Stitches a blog's rendered
PNGs in narrative order, wraps each in a captioned 1080x1350 (4:5) slide, and
adds a cover + CTA slide so the deck tells the blog's story standalone. Output
is a single PDF for LinkedIn document upload (renders as a swipeable carousel --
the highest-reach native LinkedIn format).

The slide spine (cover content, story order, per-slide kicker + caption, and the
CTA) is curated by an agent into a JSON manifest so captions read well rather
than being mechanically scraped from alt text. This renderer only lays out what
the manifest specifies.

Usage:
    python scripts/visuals/build_carousel.py <manifest.json>
    python scripts/visuals/build_carousel.py            # default loop manifest
"""

from __future__ import annotations

import os
import sys

# This script lives next to a local `html/` dir that would shadow the stdlib
# `html` package (pyparsing -> matplotlib import it). Drop our own dir from path.
_here = os.path.dirname(os.path.abspath(__file__))
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != _here]

import json
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle
from PIL import Image

# --- Design tokens (shared system) ---
BG = "#ffffff"
ACCENT = "#1f6feb"
ACCENT_2 = "#0d9488"
TEXT = "#1e293b"
TEXT_2 = "#475569"
MUTED = "#94a3b8"
LIGHT_BG = "#f8fafc"
FONT = "Helvetica Neue"

plt.rcParams["font.family"] = FONT

# --- Canvas (4:5 portrait, LinkedIn carousel ideal) ---
W, H = 1080, 1350
DPI = 100

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "content" / "visuals" / "loop-engineering-carousel.manifest.json"


def new_page():
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def wrap(text, width):
    return "\n".join(textwrap.wrap(text, width=width))


def place_image(fig, path, box):
    """Contain-fit a PNG into box=(x0,y0,x1,y1) in figure-fraction coords."""
    img = Image.open(path).convert("RGBA")
    iw, ih = img.size
    bx0, by0, bx1, by1 = box
    bw = (bx1 - bx0) * W
    bh = (by1 - by0) * H
    scale = min(bw / iw, bh / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    arr = np.asarray(img)
    xo = int(bx0 * W + (bw - nw) / 2)
    yo = int(by0 * H + (bh - nh) / 2)
    fig.figimage(arr, xo, yo, zorder=1)


def footer(ax, handle, n, total):
    ax.add_patch(Rectangle((0, 0), 1, 0.045, color=LIGHT_BG, zorder=0))
    ax.text(0.045, 0.022, handle, fontsize=11, color=MUTED, va="center", ha="left")
    ax.text(0.955, 0.022, f"{n} / {total}", fontsize=11, color=MUTED,
            va="center", ha="right")


def content_slide(fig, ax, handle, n, total, kicker, caption):
    ax.add_patch(Rectangle((0, 0.86), 1, 0.14, color=LIGHT_BG, zorder=0))
    ax.add_patch(Rectangle((0.045, 0.875), 0.006, 0.11, color=ACCENT, zorder=1))
    ax.text(0.075, 0.955, kicker, fontsize=14, color=ACCENT, va="top", ha="left",
            fontweight="bold")
    ax.text(0.075, 0.925, wrap(caption, 60), fontsize=18, color=TEXT, va="top",
            ha="left", linespacing=1.25)
    footer(ax, handle, n, total)


def cover_slide(m, total):
    fig, ax = new_page()
    handle = m["handle"]
    title_lines = m["title_lines"]
    ax.add_patch(Rectangle((0.07, 0.74), 0.10, 0.012, color=ACCENT, zorder=1))
    ax.text(0.07, 0.70, title_lines[0], fontsize=30, color=TEXT_2, va="top",
            ha="left", fontweight="bold")
    ax.text(0.07, 0.625, title_lines[1] if len(title_lines) > 1 else "",
            fontsize=52, color=ACCENT, va="top", ha="left", fontweight="bold")
    ax.text(0.07, 0.545, wrap(m["subtitle"], 34), fontsize=24, color=TEXT,
            va="top", ha="left", linespacing=1.3)
    ax.text(0.07, 0.40, m["tagline"], fontsize=22, color=ACCENT_2, va="top",
            ha="left", fontweight="bold")
    ax.text(0.07, 0.31, wrap(m["cover_note"], 46), fontsize=18, color=TEXT_2,
            va="top", ha="left", linespacing=1.3)
    ax.text(0.07, 0.14, "Swipe ->", fontsize=18, color=MUTED, va="top", ha="left")
    footer(ax, handle, 1, total)
    return fig


def cta_slide(m, n, total):
    fig, ax = new_page()
    handle = m["handle"]
    ax.add_patch(Rectangle((0, 0), 1, 1, color=ACCENT, zorder=0))
    ax.text(0.07, 0.78, wrap(m["cta_headline"], 22), fontsize=44, color="#ffffff",
            va="top", ha="left", fontweight="bold", linespacing=1.15)
    ax.text(0.07, 0.55, wrap(m["cta_body"], 40), fontsize=22, color="#dbeafe",
            va="top", ha="left", linespacing=1.35)
    ax.add_patch(Rectangle((0.07, 0.30), 0.86, 0.001, color="#93c5fd", zorder=1))
    ax.text(0.07, 0.26, "READ THE FULL ARC", fontsize=15, color="#bfdbfe",
            va="top", ha="left", fontweight="bold")
    ax.text(0.07, 0.215, wrap(m["canonical"], 52), fontsize=15, color="#ffffff",
            va="top", ha="left", linespacing=1.3)
    ax.text(0.07, 0.075, handle, fontsize=14, color="#dbeafe", va="center",
            ha="left")
    ax.text(0.955, 0.075, f"{n} / {total}", fontsize=14, color="#dbeafe",
            va="center", ha="right")
    return fig


def build(manifest_path: Path):
    m = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    visuals_dir = (ROOT / m["visuals_dir"]).resolve()
    out = (ROOT / m["output"]).resolve()
    handle = m["handle"]
    slides = m["slides"]
    total = len(slides) + 2  # cover + slides + cta

    missing = [s["image"] for s in slides if not (visuals_dir / s["image"]).exists()]
    if missing:
        raise FileNotFoundError(f"Missing visuals in {visuals_dir}: {missing}")

    out.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(out) as pdf:
        pdf.savefig(cover_slide(m, total), facecolor=BG)
        plt.close("all")
        for i, s in enumerate(slides, start=2):
            fig, ax = new_page()
            place_image(fig, visuals_dir / s["image"], box=(0.045, 0.06, 0.955, 0.84))
            content_slide(fig, ax, handle, i, total, s["kicker"], s["caption"])
            pdf.savefig(fig, facecolor=BG)
            plt.close(fig)
        pdf.savefig(cta_slide(m, total, total), facecolor=ACCENT)
        plt.close("all")
    print(f"Wrote {out} ({total} pages)")


def main():
    manifest = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MANIFEST
    build(manifest)


if __name__ == "__main__":
    main()
