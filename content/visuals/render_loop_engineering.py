"""Render the 9 blog companion visuals for the merged single post
``content/from-prompts-to-loop-engineering.md`` (Step 3b).

Each visual is rendered in the STYLE assigned by the Visual Versatility System
(see ``content/visual-opportunity-map.md`` and ``content/visual-style-map.md``).
The map was authored for a 2-part series; the post is now ONE merged post, so all
ten planned companions collapse to nine rendered assets (the SWE-bench trajectory
P1-04 and the Stripe before/after P2-04 are merged into one combo exhibit, #8).

    marker line  id          style                    renderer
    -----------  ----------  -----------------------  --------------------------
    line 9       p1-05       typographic              styles.typographic (HTML)
    line 17      p1-01 HERO  diagram-as-code          crisp matplotlib schematic
    line 36      p1-02       hand-drawn               matplotlib xkcd (3 panels)
    line 50      p2-01 HERO  diagram-as-code          d2 engine (cycle graph)
    line 60      p1-03       editorial-illustration   HTML/SVG split-screen
    line 77      p2-02       hand-drawn               matplotlib xkcd (4 panels)
    line 87      p2-03       data-exhibit             matplotlib (directional)
    line 95      p2-04       data-exhibit             matplotlib (combo exhibit)
    line 116     p2-05       hand-drawn               styles.sketch_mpl checklist

Design tokens only; Helvetica Neue; 320 DPI for matplotlib output (HTML assets
render at Chromium device-scale 2). ASCII glyphs only inside matplotlib.

Run from the repo root:
    PYTHONPATH=. python3 content/visuals/render_loop_engineering.py
"""

from __future__ import annotations

import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Arc,
    Circle,
    FancyArrowPatch,
    FancyBboxPatch,
    Rectangle,
)

from scripts.visuals.html.render import render_html_to_png
from scripts.visuals.styles.diagram_as_code import render_diagram
from scripts.visuals.styles.sketch_mpl import sketch_checklist
from scripts.visuals.styles.typographic import typographic_quote
from scripts.visuals.tokens import BASE_TOKENS, THEMES

OUT = Path(__file__).resolve().parent
DPI = 320

T = {**BASE_TOKENS, **THEMES["default"]}
# Era color ramp (paired with text labels everywhere for accessibility).
ERA = {
    "word": T["ACCENT_3"],     # prompt engineering
    "context": T["ACCENT_2"],  # context engineering
    "rig": T["ACCENT"],        # harness engineering
    "loop": T["SUCCESS"],      # loop engineering
}

FONT_STACK = ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans", "sans-serif"]


def _crisp_font() -> None:
    plt.rcParams["font.family"] = FONT_STACK
    plt.rcParams["svg.fonttype"] = "none"


# ---------------------------------------------------------------------------
# Auto-fit text helpers — measure rendered text in DATA units so labels are
# wrapped and shrunk to fit a fixed-width card instead of overflowing it.
# This is the root-cause fix for text spilling outside its box.
# ---------------------------------------------------------------------------
def _text_width_data(ax, fig, s: str, fontsize: float, weight: str = "normal") -> float:
    """Width of string ``s`` in axis DATA units at the given font."""
    t = ax.text(0, 0, s, fontsize=fontsize, fontweight=weight)
    fig.canvas.draw()
    bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
    inv = ax.transData.inverted()
    (x0, _), (x1, _) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
    t.remove()
    return abs(x1 - x0)


def _wrap_words(ax, fig, s: str, fontsize: float, max_w: float, weight: str = "normal"):
    """Greedy word-wrap so each line fits ``max_w`` data units."""
    lines, cur = [], []
    for w in s.split():
        trial = " ".join(cur + [w])
        if cur and _text_width_data(ax, fig, trial, fontsize, weight) > max_w:
            lines.append(" ".join(cur))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(" ".join(cur))
    return lines


def _fit_text_lines(ax, fig, s: str, max_w: float, *, base: float,
                    min_size: float, max_lines: int, weight: str = "normal"):
    """Shrink the font until the wrapped text fits ``max_w`` and ``max_lines``.

    Returns ``(lines, fontsize)``. Falls back to ``min_size`` if nothing fits.
    """
    fs = base
    lines = [s]
    while fs >= min_size:
        lines = _wrap_words(ax, fig, s, fs, max_w, weight)
        if len(lines) <= max_lines:
            widest = max(_text_width_data(ax, fig, ln, fs, weight) for ln in lines)
            if widest <= max_w:
                return lines, fs
        fs -= 0.5
    return lines, max(fs, min_size)


# ---------------------------------------------------------------------------
# #2  p1-01 — The four-era staircase  (HERO, diagram-as-code via d2)
# ---------------------------------------------------------------------------
# Migrated from hand-placed matplotlib to D2 (auto-layout) to eliminate the
# hand-geometry defect class. `direction: up` makes the four eras read as an
# ascending staircase: WORD (base) -> CONTEXT -> RIG -> LOOP (top), with the
# upward arrows + numbering carrying the rise.
def staircase(out_path: Path) -> Path:
    edge = f'{{style.stroke: "{T["TEXT_2"]}"; style.stroke-width: 2}}'
    src = f"""
direction: up

title: |md
# The staircase: four eras, one moving target
Each step automates the craft below it and pushes your effort up a level.
|
title.shape: text
title.near: top-center
title.style.font-size: 30
title.style.font-color: "{T['TEXT']}"

word: |md
### 1 · WORD
**Prompt engineering** engineer the wording of one call

`2022-2024`
|
word.style.fill: "{T['PURPLE_BG']}"
word.style.stroke: "{ERA['word']}"
word.style.border-radius: 12
word.style.font-color: "{T['TEXT']}"

context: |md
### 2 · CONTEXT
**Context engineering** engineer what the model sees

`~Jun 2025`
|
context.style.fill: "{T['TEAL_BG']}"
context.style.stroke: "{ERA['context']}"
context.style.border-radius: 12
context.style.font-color: "{T['TEXT']}"

rig: |md
### 3 · RIG
**Harness engineering** engineer everything around the model

`Feb 2026`
|
rig.style.fill: "{T['BLUE_BG']}"
rig.style.stroke: "{ERA['rig']}"
rig.style.border-radius: 12
rig.style.font-color: "{T['TEXT']}"

loop: |md
### 4 · LOOP
**Loop engineering** engineer the iteration cycle itself

`Sep 2025 -> Mar 2026`
|
loop.style.fill: "#dcfce7"
loop.style.stroke: "{ERA['loop']}"
loop.style.border-radius: 12
loop.style.font-color: "{T['TEXT']}"

word -> context: automates the craft below {edge}
context -> rig: automates the craft below {edge}
rig -> loop: automates the craft below {edge}

sources: "Sources: trend-research; Fowler 'Exploring Gen AI' index; Bockeler (Feb 2026); Willison (Sep 2025)."
sources.shape: text
sources.near: bottom-center
sources.style.font-size: 18
sources.style.font-color: "{T['MUTED']}"
"""
    return render_diagram(out_path, source=src, lang="d2", sketch=False, theme="default")


# ---------------------------------------------------------------------------
# #4  p2-01 — The loop diagram  (HERO, diagram-as-code via d2)
# ---------------------------------------------------------------------------
def loop_diagram(out_path: Path) -> Path:
    src = f"""
direction: down

plan: "Plan -- goal + success criterion"
plan.style.fill: "{T['PURPLE_BG']}"
plan.style.stroke: "{ERA['word']}"
plan.style.font-color: "{T['TEXT']}"
plan.style.border-radius: 10
plan.style.bold: true

act: "Act -- use the tools"
act.style.fill: "{T['TEAL_BG']}"
act.style.stroke: "{ERA['context']}"
act.style.font-color: "{T['TEXT']}"
act.style.border-radius: 10

observe: "Observe -- read the sensors"
observe.style.fill: "{T['BLUE_BG']}"
observe.style.stroke: "{ERA['rig']}"
observe.style.font-color: "{T['TEXT']}"
observe.style.border-radius: 10

verify: "Verify -- the gate"
verify.shape: diamond
verify.style.fill: "#dcfce7"
verify.style.stroke: "{T['SUCCESS']}"
verify.style.font-color: "{T['TEXT']}"
verify.style.bold: true

correct: "Correct -- adjust + retry"
correct.style.fill: "{T['LIGHT_BG']}"
correct.style.stroke: "{T['TEXT_2']}"
correct.style.font-color: "{T['TEXT']}"
correct.style.border-radius: 10

stop: "STOP -- goal met OR max iterations"
stop.style.fill: "{T['RED_BG']}"
stop.style.stroke: "{T['WARN']}"
stop.style.font-color: "{T['TEXT']}"
stop.style.border-radius: 10
stop.style.bold: true

plan -> act
act -> observe
observe -> verify
verify -> correct: needs work
correct -> plan: iterate (inner loop)
verify -> stop: goal met / cap hit
"""
    return render_diagram(out_path, source=src, lang="d2", sketch=False, theme="default")


# ---------------------------------------------------------------------------
# small hand-drawn primitives (xkcd context)
# ---------------------------------------------------------------------------
def _loop_glyph(ax, cx, cy, r, color, lw=2.4, arrows=True):
    """A circular flow loop with arrowheads, drawn inside an xkcd context."""
    ax.add_patch(Arc((cx, cy), 2 * r, 2 * r, theta1=0, theta2=360,
                     edgecolor=color, lw=lw, fill=False))
    if arrows:
        import math
        for ang in (60, 240):
            a = math.radians(ang)
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            # tangent direction (counter-clockwise)
            tx, ty = -math.sin(a), math.cos(a)
            ax.add_patch(FancyArrowPatch(
                (x - tx * 0.02, y - ty * 0.02), (x + tx * 0.02, y + ty * 0.02),
                arrowstyle="-|>", mutation_scale=20, lw=lw, color=color))


def _figure(ax, x, y, s, color):
    """A small stick figure centered at (x, y), height ~s."""
    head_r = s * 0.16
    ax.add_patch(Circle((x, y + s * 0.42), head_r, fill=False, edgecolor=color, lw=2.2))
    ax.plot([x, x], [y + s * 0.26, y - s * 0.18], color=color, lw=2.2)        # body
    ax.plot([x - s * 0.22, x + s * 0.22], [y + s * 0.10, y + s * 0.10], color=color, lw=2.2)  # arms
    ax.plot([x, x - s * 0.18], [y - s * 0.18, y - s * 0.5], color=color, lw=2.2)  # leg
    ax.plot([x, x + s * 0.18], [y - s * 0.18, y - s * 0.5], color=color, lw=2.2)  # leg


# ---------------------------------------------------------------------------
# #3  p1-02 — Era ceilings small-multiple  (hand-drawn xkcd, 3 panels)
# ---------------------------------------------------------------------------
def ceilings(out_path: Path) -> Path:
    import numpy as np

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with plt.xkcd(scale=1.0, length=110, randomness=2):
            fig, axes = plt.subplots(1, 3, figsize=(13.5, 5.4), dpi=DPI)
            fig.patch.set_facecolor(T["BG"])

            panels = [
                ("Prompt ceiling", "diminishing returns on", "wording one call", ERA["word"]),
                ("Context ceiling", "a static window", "can't act / iterate", ERA["context"]),
                ("Harness ceiling", "a great rig still needs", "a cycle to run in", ERA["rig"]),
            ]

            for ax, (title, l1, l2, color) in zip(axes, panels):
                ax.set_xlim(0, 10)
                ax.set_ylim(0, 10)
                ax.axis("off")
                ax.set_facecolor(T["BG"])
                # panel frame
                ax.add_patch(Rectangle((0.3, 0.3), 9.4, 9.4, fill=False,
                                       edgecolor=T["GRID"], lw=2.0))
                ax.text(5, 9.3, title, ha="center", va="top",
                        fontsize=16, fontweight="bold", color=color)

            # Panel 1: diminishing-returns curve flattening under a ceiling line.
            ax = axes[0]
            xs = np.linspace(1.2, 8.8, 60)
            ys = 2.2 + 4.6 * (1 - np.exp(-(xs - 1.2) / 1.7))
            ax.plot(xs, ys, color=ERA["word"], lw=3.0)
            ax.plot([1.0, 9.0], [7.2, 7.2], color=T["WARN"], lw=2.2, linestyle=(0, (5, 4)))
            ax.text(8.9, 7.5, "ceiling", ha="right", va="bottom",
                    fontsize=11.5, color=T["WARN"])
            ax.annotate("better wording", xy=(7.8, ys[-1]), xytext=(3.2, 3.0),
                        fontsize=11, color=T["TEXT_2"],
                        arrowprops=dict(arrowstyle="->", color=T["MUTED"], lw=1.6))

            # Panel 2: context window box full of dots; arrow can't exit (hits wall).
            ax = axes[1]
            ax.add_patch(Rectangle((1.6, 3.0), 4.0, 4.6, fill=False,
                                   edgecolor=ERA["context"], lw=2.8))
            ax.text(3.6, 7.9, "the window", ha="center", va="bottom",
                    fontsize=11.5, color=ERA["context"])
            rng = np.random.default_rng(7)
            for _ in range(16):
                ax.add_patch(Circle((rng.uniform(2.0, 5.2), rng.uniform(3.4, 7.1)),
                                    0.12, color=T["ACCENT_2"], alpha=0.6))
            # wall on the right + blocked arrow
            ax.plot([7.4, 7.4], [2.8, 7.8], color=T["WARN"], lw=3.2)
            ax.add_patch(FancyArrowPatch((5.7, 5.3), (7.0, 5.3),
                         arrowstyle="-|>", mutation_scale=22, lw=2.6, color=T["TEXT_2"]))
            ax.text(7.55, 5.3, "can't\nact", ha="left", va="center",
                    fontsize=11.5, color=T["WARN"])

            # Panel 3: a rig (gear-ish box) with an OPEN loop arrow that doesn't close.
            ax = axes[2]
            ax.add_patch(FancyBboxPatch((3.4, 4.2), 3.2, 2.4,
                         boxstyle="round,pad=0.05,rounding_size=0.2",
                         fill=False, edgecolor=ERA["rig"], lw=2.8))
            ax.text(5.0, 5.4, "the rig", ha="center", va="center",
                    fontsize=12.5, fontweight="bold", color=ERA["rig"])
            # broken / open loop: an arc that stops short, its arrowhead anchored
            # to the arc's lower-left terminus so the stroke reads as continuous.
            cx, cy, aw, ah = 5.0, 5.4, 5.6, 4.6
            ax.add_patch(Arc((cx, cy), aw, ah, theta1=300, theta2=210,
                             edgecolor=T["TEXT_2"], lw=2.6))
            ex = cx + (aw / 2) * np.cos(np.radians(210))
            ey = cy + (ah / 2) * np.sin(np.radians(210))
            px = cx + (aw / 2) * np.cos(np.radians(204))
            py = cy + (ah / 2) * np.sin(np.radians(204))
            ax.add_patch(FancyArrowPatch((px, py), (ex, ey),
                         arrowstyle="-|>", mutation_scale=20, lw=2.6, color=T["TEXT_2"]))
            ax.plot([6.9, 7.7], [3.3, 4.0], color=T["WARN"], lw=3.0)
            ax.plot([7.7, 6.9], [3.3, 4.0], color=T["WARN"], lw=3.0)
            ax.text(7.0, 3.0, "no cycle", ha="center", va="top",
                    fontsize=11.5, color=T["WARN"])

            for ax, (title, l1, l2, color) in zip(axes, panels):
                ax.text(5, 2.0, l1, ha="center", va="center",
                        fontsize=12, color=T["TEXT"])
                ax.text(5, 1.35, l2, ha="center", va="center",
                        fontsize=12, color=T["TEXT"])

            fig.suptitle("Why each era hit a ceiling and pushed you up a level",
                         fontsize=18, fontweight="bold", color=T["TEXT"], y=1.02)
            fig.text(0.5, -0.02,
                     "Proof tie-in: a minimal harness (mini-SWE-agent) hits 65% on SWE-bench Verified in ~100 lines (swebench.com, Jul 2025).",
                     ha="center", fontsize=10.5, color=T["MUTED"])
            fig.savefig(out_path, dpi=DPI, bbox_inches="tight",
                        facecolor=T["BG"], pad_inches=0.2)
            plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# #6  p2-02 — Four-posture panel  (hand-drawn xkcd, 4 panels)
# ---------------------------------------------------------------------------
def postures(out_path: Path) -> Path:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with plt.xkcd(scale=1.0, length=110, randomness=2):
            fig, axes = plt.subplots(1, 4, figsize=(14.5, 5.2), dpi=DPI)
            fig.patch.set_facecolor(T["BG"])
            for ax in axes:
                ax.set_xlim(0, 10)
                ax.set_ylim(0, 10)
                ax.axis("off")
                ax.add_patch(Rectangle((0.3, 0.3), 9.4, 9.4, fill=False,
                                       edgecolor=T["GRID"], lw=2.0))

            # Panel 1 — Outside the loop.
            ax = axes[0]
            _loop_glyph(ax, 6.4, 6.0, 1.8, T["ACCENT"])
            _figure(ax, 2.4, 6.0, 3.0, T["TEXT"])
            ax.add_patch(FancyArrowPatch((3.2, 6.0), (4.4, 6.0),
                         arrowstyle="-|>", mutation_scale=20, lw=2.4, color=T["TEXT_2"]))
            ax.text(5, 9.0, "OUTSIDE", ha="center", fontsize=15,
                    fontweight="bold", color=T["ACCENT"])
            ax.text(5, 2.4, "vibe coding --", ha="center", fontsize=11.5, color=T["TEXT"])
            ax.text(5, 1.7, "own only the why", ha="center", fontsize=11.5, color=T["TEXT"])

            # Panel 2 — In the loop (bottleneck).
            ax = axes[1]
            _loop_glyph(ax, 5.0, 6.0, 1.9, T["MUTED"])
            _figure(ax, 5.0, 6.0, 2.6, T["WARN"])
            ax.add_patch(FancyBboxPatch((2.7, 8.0), 4.6, 0.9,
                         boxstyle="round,pad=0.05,rounding_size=0.2",
                         facecolor=T["RED_BG"], edgecolor=T["WARN"], lw=2.2))
            ax.text(5.0, 8.45, "[!] BOTTLENECK", ha="center", va="center",
                    fontsize=12.5, fontweight="bold", color=T["WARN"])
            ax.text(5, 2.4, "gatekeep every line --", ha="center", fontsize=11.5, color=T["TEXT"])
            ax.text(5, 1.7, "you are the limit", ha="center", fontsize=11.5, color=T["WARN"])
            ax.text(5, 9.2, "IN", ha="center", fontsize=15,
                    fontweight="bold", color=T["WARN"])

            # Panel 3 — On the loop.
            ax = axes[2]
            _loop_glyph(ax, 5.0, 5.2, 1.9, T["SUCCESS"])
            _figure(ax, 5.0, 8.0, 2.2, T["TEXT"])
            # wrench / tuning arrow down onto the loop
            ax.add_patch(FancyArrowPatch((5.0, 7.0), (5.0, 6.0),
                         arrowstyle="-|>", mutation_scale=20, lw=2.4, color=T["SUCCESS"]))
            ax.text(5, 9.2, "ON", ha="center", fontsize=15,
                    fontweight="bold", color=T["SUCCESS"])
            ax.text(5, 2.4, "build + tune the loop --", ha="center", fontsize=11, color=T["TEXT"])
            ax.text(5, 1.7, "loop engineering lives here", ha="center", fontsize=11, color=T["SUCCESS"])

            # Panel 4 — The agentic flywheel.
            ax = axes[3]
            _loop_glyph(ax, 3.7, 5.4, 1.2, T["ACCENT_2"])
            _loop_glyph(ax, 6.6, 6.4, 1.5, T["ACCENT"])
            _figure(ax, 5.0, 8.2, 2.0, T["TEXT"])
            ax.add_patch(FancyArrowPatch((4.4, 7.6), (3.9, 6.5),
                         arrowstyle="-|>", mutation_scale=18, lw=2.2, color=T["ACCENT_3"]))
            ax.add_patch(FancyArrowPatch((5.6, 7.6), (6.4, 7.0),
                         arrowstyle="-|>", mutation_scale=18, lw=2.2, color=T["ACCENT_3"]))
            ax.text(5, 9.2, "FLYWHEEL", ha="center", fontsize=14,
                    fontweight="bold", color=T["ACCENT_3"])
            ax.text(5, 2.4, "direct agents to", ha="center", fontsize=11.5, color=T["TEXT"])
            ax.text(5, 1.7, "improve the loop", ha="center", fontsize=11.5, color=T["TEXT"])

            fig.suptitle("Who sits where: humans outside, in, on the loop -- and the flywheel",
                         fontsize=17, fontweight="bold", color=T["TEXT"], y=1.02)
            fig.text(0.5, -0.03,
                     "Pivot: IN = fix the output (you edit).  ON = fix the loop that produced it (you engineer).   Source: Kief Morris, Mar 2026.",
                     ha="center", fontsize=10.5, color=T["MUTED"])
            fig.savefig(out_path, dpi=DPI, bbox_inches="tight",
                        facecolor=T["BG"], pad_inches=0.2)
            plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# #7  p2-03 — The validation inversion (bottleneck)  (data-exhibit, DIRECTIONAL)
# ---------------------------------------------------------------------------
def bottleneck(out_path: Path) -> Path:
    import numpy as np

    _crisp_font()
    fig, ax = plt.subplots(figsize=(12.5, 7.0), dpi=DPI)
    fig.patch.set_facecolor(T["BG"])
    ax.set_facecolor(T["BG"])

    x = np.linspace(0, 10, 50)
    gen = 1.0 + 0.62 * x                      # generation throughput, rising
    val = 1.6 + 0.06 * x                      # validation / deploys, ~flat

    ax.fill_between(x, val, gen, color=T["RED_BG"], alpha=0.7, zorder=1)
    ax.plot(x, gen, color=T["ACCENT"], lw=4.0, zorder=3,
            label="Code generation throughput")
    ax.plot(x, val, color=T["MUTED"], lw=4.0, linestyle=(0, (6, 4)), zorder=3,
            label="Validation / production deploys")

    ax.text(9.9, gen[-1] + 0.2, "generation", ha="right", va="bottom",
            fontsize=14, fontweight="bold", color=T["ACCENT"])
    ax.text(9.9, val[-1] - 0.55, "validation (flat)", ha="right", va="top",
            fontsize=14, fontweight="bold", color=T["TEXT_2"])
    ax.text(6.4, 4.6, "the widening\nbottleneck", ha="center", va="center",
            fontsize=13.5, fontweight="bold", color=T["WARN"])

    # Inner-loop callout box.
    box_txt = ("Fix: pull verification INTO the inner loop\n"
               "CircleCI Chunk Sidecars  |  Dropbox Nova  |  Claude Code")
    ax.add_patch(FancyBboxPatch((0.35, 5.55), 5.2, 1.25,
                 boxstyle="round,pad=0.12,rounding_size=0.18",
                 facecolor=T["LIGHT_BG"], edgecolor=T["SUCCESS"], lw=2.4,
                 transform=ax.transData, zorder=5))
    ax.text(0.6, 6.18, box_txt, ha="left", va="center", fontsize=12,
            color=T["TEXT"], zorder=6)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.2)
    ax.set_xlabel("time ->", fontsize=12.5, color=T["TEXT_2"])
    ax.set_ylabel("relative volume (directional)", fontsize=12.5, color=T["TEXT_2"])
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(T["GRID"])

    # DIRECTIONAL flag.
    ax.add_patch(FancyBboxPatch((8.05, 0.35), 1.85, 0.62,
                 boxstyle="round,pad=0.08,rounding_size=0.14",
                 facecolor=T["BG"], edgecolor=T["WARN"], lw=2.0, zorder=6))
    ax.text(8.97, 0.66, "DIRECTIONAL", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=T["WARN"], zorder=7)

    ax.set_title("Why now: validation, not generation, is the bottleneck",
                 fontsize=19, fontweight="bold", color=T["TEXT"], loc="left", pad=14)
    fig.text(0.5, 0.012,
             "Schematic / directional -- CircleCI's claim is qualitative; axes carry no measured values.   Source: CircleCI via InfoQ, Jun 2026.",
             ha="center", fontsize=10.5, color=T["MUTED"])
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", facecolor=T["BG"], pad_inches=0.18)
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# #8  p2-04 — Stripe before/after + SWE-bench trajectory  (data-exhibit combo)
# ---------------------------------------------------------------------------
def stripe_swebench(out_path: Path) -> Path:
    _crisp_font()
    fig, (axL, axR) = plt.subplots(
        1, 2, figsize=(14.0, 6.8), dpi=DPI, gridspec_kw={"width_ratios": [1.0, 1.25]}
    )
    fig.patch.set_facecolor(T["BG"])

    # ---- Left: Stripe before/after bars ----
    axL.set_facecolor(T["BG"])
    labels = ["Before", "After"]
    vals = [1000, 1300]
    colors = [T["MUTED"], T["ACCENT"]]
    bars = axL.bar([0, 1], vals, width=0.56, color=colors, zorder=3)
    axL.set_xlim(-0.6, 1.6)
    axL.set_ylim(0, 1600)
    axL.set_xticks([0, 1])
    axL.set_xticklabels(labels, fontsize=13, color=T["TEXT"])
    axL.set_yticks([])
    for sp in ("top", "right", "left"):
        axL.spines[sp].set_visible(False)
    axL.spines["bottom"].set_color(T["GRID"])
    axL.text(0, 1000 + 55, "~1,000", ha="center", fontsize=14,
             fontweight="bold", color=T["TEXT_2"])
    axL.text(1, 1300 + 88, "1,300+", ha="center", fontsize=16,
             fontweight="bold", color=T["ACCENT"])
    # Growth arrow ends at the top-left of the After bar, clear of the 1,300+ label.
    axL.annotate("", xy=(0.80, 1300), xytext=(0.24, 1075),
                 arrowprops=dict(arrowstyle="-|>", color=T["SUCCESS"], lw=2.4))
    axL.text(0.44, 1430, "+30%", ha="center", fontsize=13,
             fontweight="bold", color=T["SUCCESS"])
    axL.set_title("Stripe Minions: PRs / week", fontsize=15.5,
                  fontweight="bold", color=T["TEXT"], loc="left", pad=10)
    axL.text(-0.55, -190,
             "Zero human-written code (all human-reviewed)  |  underpins \\$1T+ annual payment volume",
             ha="left", fontsize=10.8, color=T["TEXT_2"])
    axL.text(-0.55, -300, "Source: InfoQ -> Stripe, Mar 2026",
             ha="left", fontsize=10, color=T["MUTED"])

    # ---- Right: SWE-bench trajectory + cost band ----
    axR.set_facecolor(T["BG"])
    px = [0, 1, 2]
    py = [12.47, 65.0, 76.8]
    plabels = ["SWE-agent\nMar 2024", "mini-SWE-agent\nJul 2025", "Claude 4.5 Opus\nFeb 2026"]
    axR.plot(px, py, color=T["ACCENT"], lw=3.6, marker="o", markersize=11,
             markerfacecolor=T["BG"], markeredgecolor=T["ACCENT"], markeredgewidth=3, zorder=4)
    for i, (xx, yy) in enumerate(zip(px, py)):
        txt = f"{yy:.1f}%".replace(".0%", "%")
        if i == 0:
            # First point sits low and the line climbs steeply up-and-right;
            # place its label up-and-left so the line never crosses the text.
            axR.text(xx - 0.06, yy + 6.0, txt, ha="right", va="center",
                     fontsize=13, fontweight="bold", color=T["ACCENT"], zorder=5)
        else:
            axR.text(xx, yy + 5.5, txt, ha="center", va="center",
                     fontsize=13, fontweight="bold", color=T["ACCENT"], zorder=5)
    axR.set_xlim(-0.6, 2.4)
    axR.set_ylim(0, 100)
    axR.set_xticks(px)
    axR.set_xticklabels(plabels, fontsize=10.5, color=T["TEXT"])
    axR.set_yticks([0, 25, 50, 75, 100])
    axR.set_yticklabels(["0%", "25%", "50%", "75%", "100%"], fontsize=11, color=T["TEXT_2"])
    axR.grid(axis="y", color=T["GRID"], lw=1.0)
    axR.set_axisbelow(True)
    for sp in ("top", "right"):
        axR.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        axR.spines[sp].set_color(T["GRID"])

    # per-task cost band callout -- box sized to the measured text so it never
    # overflows; a plain rectangle avoids the distorted corners that mismatched
    # x/y data scales produce with a rounded box.
    band_txt = "per-task cost band: ~\\$0.05 - \\$0.96 / instance"
    band_fs = 10.5
    bx0, by0, bh = 0.05, 84.0, 12.0
    bw = _text_width_data(axR, fig, band_txt, band_fs, "bold") + 0.20
    axR.add_patch(Rectangle((bx0, by0), bw, bh,
                  facecolor=T["LIGHT_BG"], edgecolor=T["WARN"], lw=2.0, zorder=3))
    axR.text(bx0 + 0.10, by0 + bh / 2, band_txt,
             ha="left", va="center", fontsize=band_fs, fontweight="bold",
             color=T["WARN"], zorder=4)
    axR.text(0.05, 7,
             "Same harness, different model -- 500 human-filtered instances.",
             ha="left", fontsize=11, style="italic", color=T["TEXT_2"])
    axR.set_title("SWE-bench Verified: ~6x in two years",
                  fontsize=15.5, fontweight="bold", color=T["TEXT"], loc="left", pad=10)
    axR.text(-0.35, -16,
             "Source: swebench.com, Feb 2026 (v2.0.0).  Pricing 'still very subsidized' (Bockeler, Jun 2026).",
             ha="left", fontsize=10, color=T["MUTED"])

    fig.suptitle("Proof at scale: Stripe Minions and the SWE-bench trajectory",
                 fontsize=18, fontweight="bold", color=T["TEXT"], x=0.06, ha="left", y=1.0)
    fig.subplots_adjust(bottom=0.2, top=0.86, wspace=0.18)
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", facecolor=T["BG"], pad_inches=0.2)
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# #5  p1-03 — Harness vs. loop clarifier  (editorial-illustration, HTML/SVG)
# ---------------------------------------------------------------------------
def harness_vs_loop(out_path: Path) -> Path:
    t = T
    font = "'Helvetica Neue', Helvetica, Arial, sans-serif"
    accent = t["ACCENT"]
    teal = t["ACCENT_2"]
    warn = t["WARN"]
    text = t["TEXT"]
    text2 = t["TEXT_2"]
    muted = t["MUTED"]
    light = t["LIGHT_BG"]

    # Left scene: gym + equipment (nouns). Right scene: rep-scheme + coach (verbs).
    # All copy is real DOM (overlaid), never baked into the SVG.
    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ background:{t['BG']}; }}
  #stage {{
    width:1640px; height:840px; background:{t['BG']}; font-family:{font};
    position:relative; overflow:hidden;
    display:grid; grid-template-columns: 1fr 96px 1fr;
  }}
  .panel {{ position:relative; padding:54px 50px 0 50px; }}
  .left {{ background:{light}; }}
  .right {{ background:{t['BG']}; }}
  .eyebrow {{ font-size:19px; letter-spacing:0.26em; text-transform:uppercase; font-weight:800; }}
  .ttl {{ font-size:40px; font-weight:800; color:{text}; letter-spacing:-0.01em; margin-top:8px; line-height:1.08; }}
  .sub {{ font-size:21px; color:{text2}; margin-top:10px; font-weight:600; }}
  .chips {{ position:absolute; left:50px; right:50px; bottom:120px; display:flex; flex-wrap:wrap; gap:12px; }}
  .chip {{ font-size:18px; font-weight:600; color:{text}; background:{t['BG']};
           border:2px solid {muted}; border-radius:999px; padding:8px 16px; }}
  .left .chip {{ border-color:{accent}; }}
  .right .chip {{ border-color:{teal}; }}
  .cap {{ position:absolute; left:50px; right:50px; bottom:60px; font-size:18px; color:{text2}; font-weight:600; }}
  .scene {{ position:absolute; left:50%; top:188px; transform:translateX(-50%); }}
  .divider {{ display:flex; align-items:center; justify-content:center; }}
  .neq {{ width:84px; height:84px; border-radius:50%; background:{t['BG']};
          border:3px solid {warn}; display:flex; align-items:center; justify-content:center;
          font-size:46px; font-weight:800; color:{warn}; }}
  .vline {{ position:absolute; top:0; bottom:0; width:2px; background:{t['GRID']}; left:50%; }}
  .test {{ position:absolute; left:0; right:0; bottom:0; height:64px; }}
</style></head>
<body>
  <div id="stage">
    <div class="panel left">
      <div class="eyebrow" style="color:{accent};">Harness = the rig</div>
      <div class="ttl">Nouns</div>
      <div class="sub">the gym and the equipment</div>
      <div class="scene">
        <svg width="420" height="300" viewBox="0 0 420 300">
          <!-- dumbbell -->
          <rect x="150" y="120" width="120" height="20" rx="6" fill="{accent}"/>
          <circle cx="140" cy="130" r="34" fill="{t['BLUE_BG']}" stroke="{accent}" stroke-width="6"/>
          <circle cx="280" cy="130" r="34" fill="{t['BLUE_BG']}" stroke="{accent}" stroke-width="6"/>
          <!-- equipment rack -->
          <rect x="40" y="200" width="150" height="70" rx="10" fill="none" stroke="{teal}" stroke-width="5"/>
          <line x1="40" y1="235" x2="190" y2="235" stroke="{teal}" stroke-width="4"/>
          <line x1="90" y1="200" x2="90" y2="270" stroke="{teal}" stroke-width="4"/>
          <line x1="140" y1="200" x2="140" y2="270" stroke="{teal}" stroke-width="4"/>
          <!-- wrench / tool -->
          <g transform="translate(250 210) rotate(35)">
            <rect x="0" y="14" width="120" height="16" rx="8" fill="{t['ACCENT_3']}"/>
            <circle cx="6" cy="22" r="20" fill="none" stroke="{t['ACCENT_3']}" stroke-width="8"/>
          </g>
          <!-- checklist board -->
          <rect x="300" y="40" width="90" height="120" rx="10" fill="none" stroke="{muted}" stroke-width="5"/>
          <line x1="316" y1="74" x2="374" y2="74" stroke="{muted}" stroke-width="5"/>
          <line x1="316" y1="100" x2="374" y2="100" stroke="{muted}" stroke-width="5"/>
          <line x1="316" y1="126" x2="374" y2="126" stroke="{muted}" stroke-width="5"/>
        </svg>
      </div>
      <div class="chips">
        <span class="chip">skills</span><span class="chip">CLIs</span>
        <span class="chip">tests</span><span class="chip">linters</span>
        <span class="chip">type checkers</span><span class="chip">guardrails</span>
      </div>
      <div class="cap">"Everything except the model." What tools and sensors does the agent have?</div>
    </div>

    <div class="panel divider"><div class="neq">&ne;</div></div>

    <div class="panel right">
      <div class="eyebrow" style="color:{teal};">Loop = the cycle</div>
      <div class="ttl">Verbs</div>
      <div class="sub">the rep-scheme and the coach</div>
      <div class="scene">
        <svg width="420" height="300" viewBox="0 0 420 300">
          <!-- cyclic arrows -->
          <g fill="none" stroke="{teal}" stroke-width="9" stroke-linecap="round">
            <path d="M210 70 A 90 90 0 1 1 120 160"/>
          </g>
          <polygon points="120,160 104,134 144,140" fill="{teal}"/>
          <!-- inner loop marker -->
          <circle cx="210" cy="160" r="44" fill="none" stroke="{accent}" stroke-width="6" stroke-dasharray="10 10"/>
          <!-- whistle (coach decides when done) -->
          <g transform="translate(286 196)">
            <circle cx="0" cy="0" r="30" fill="{t['TEAL_BG']}" stroke="{teal}" stroke-width="6"/>
            <rect x="22" y="-12" width="40" height="22" rx="6" fill="{teal}"/>
            <circle cx="0" cy="0" r="9" fill="{t['BG']}"/>
          </g>
          <!-- stop sign (stop condition) -->
          <g transform="translate(86 196)">
            <polygon points="-14,-34 14,-34 34,-14 34,14 14,34 -14,34 -34,14 -34,-14"
                     fill="{t['RED_BG']}" stroke="{warn}" stroke-width="6"/>
          </g>
        </svg>
      </div>
      <div class="chips">
        <span class="chip">act</span><span class="chip">observe</span>
        <span class="chip">verify</span><span class="chip">retry</span>
        <span class="chip">stop</span>
      </div>
      <div class="cap">The evaluator-optimizer cycle. How does it iterate, and what makes it stop?</div>
    </div>
  </div>
</body></html>"""
    return render_html_to_png(doc, out_path, scale=2)


# ---------------------------------------------------------------------------
def main() -> None:
    written: list[tuple[str, Path]] = []

    # #1 p1-05 — pull-quote (typographic).
    written.append(("p1-05 typographic", typographic_quote(
        OUT / "p1-05-pull-quote.png",
        kicker="the reframe",
        quote="You're not getting better at prompting. The level you work at is moving up the stack.",
        accent_word="moving",
        context="Prompt -> context -> rig -> loop: each step automates the craft below it and pushes your effort up a level.",
        source="From Prompts to Loop Engineering -- the four-era arc",
        theme="default",
        height=820,
    )))

    # #2 p1-01 — four-era staircase HERO (diagram-as-code: crisp schematic).
    written.append(("p1-01 diagram-as-code (HERO)", staircase(OUT / "p1-01-staircase.png")))

    # #3 p1-02 — era ceilings small-multiple (hand-drawn).
    written.append(("p1-02 hand-drawn", ceilings(OUT / "p1-02-ceilings.png")))

    # #4 p2-01 — loop diagram HERO (diagram-as-code via d2).
    written.append(("p2-01 diagram-as-code (HERO)", loop_diagram(OUT / "p2-01-loop.png")))

    # #5 p1-03 — harness vs. loop clarifier (editorial-illustration).
    written.append(("p1-03 editorial-illustration", harness_vs_loop(OUT / "p1-03-harness-vs-loop.png")))

    # #6 p2-02 — four-posture panel (hand-drawn).
    written.append(("p2-02 hand-drawn", postures(OUT / "p2-02-postures.png")))

    # #7 p2-03 — validation inversion / bottleneck (data-exhibit, directional).
    written.append(("p2-03 data-exhibit", bottleneck(OUT / "p2-03-bottleneck.png")))

    # #8 p2-04 — Stripe + SWE-bench combo (data-exhibit).
    written.append(("p2-04 data-exhibit", stripe_swebench(OUT / "p2-04-stripe-swebench.png")))

    # #9 p2-05 — your first loop checklist (hand-drawn).
    written.append(("p2-05 hand-drawn", sketch_checklist(
        OUT / "p2-05-first-loop-checklist.png",
        title="Your first loop: ship one this week",
        subtitle="Take one task where you babysit the agent line-by-line, and give it four things.",
        steps=[
            ("1", "A clear goal with a success criterion"),
            ("2", "The tools to iterate -- CLI, test runner, linter"),
            ("3", "One machine-checkable feedback signal"),
            ("4", "A stop condition -- max iterations or a definition of done"),
        ],
        source="Source: Anthropic evaluator-optimizer + stop condition; this run's own loop.",
        theme="forest",
    )))

    for style, p in written:
        print(f"wrote {p.name:34s} [{style}]")


if __name__ == "__main__":
    main()
