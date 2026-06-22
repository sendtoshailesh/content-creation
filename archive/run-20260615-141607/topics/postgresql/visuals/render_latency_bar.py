"""matplotlib bar chart for the PostgreSQL performance post (V4).

before-after-latency.png — log-scale before/after query latency for the
missing-composite-index example (4,200 ms -> 38 ms, ~110x faster).

    python3 content/topics/postgresql/visuals/render_latency_bar.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

from scripts.visuals.tokens import DPI, get_tokens  # noqa: E402

OUT = Path(__file__).resolve().parent / "before-after-latency.png"

# Explicit red/green semantics are required for this chart, so use the default
# theme tokens (WARN = #dc2626 red, SUCCESS = #16a34a green).
T = get_tokens("default")


def _font():
    for name in ("Helvetica Neue", "Helvetica", "Arial"):
        try:
            font_manager.findfont(name, fallback_to_default=False)
            return name
        except Exception:
            continue
    return "DejaVu Sans"


def render() -> Path:
    plt.rcParams["font.family"] = _font()

    fig, ax = fig_ax = plt.subplots(figsize=(7.4, 5.2), dpi=DPI)

    labels = ["Before\n(seq scan + sort)", "After\n(composite index)"]
    values = [4200, 38]
    colors = [T["WARN"], T["SUCCESS"]]
    x = [0, 1]

    bars = ax.bar(x, values, width=0.56, color=colors, zorder=3,
                  edgecolor="white", linewidth=1.2)

    # Log-scale y so 38 ms and 4,200 ms are both readable.
    ax.set_yscale("log")
    ax.set_ylim(10, 12000)

    # Bold value labels above each bar.
    value_text = ["4,200 ms", "38 ms"]
    for bar, txt in zip(bars, value_text):
        ax.annotate(
            txt,
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 8), textcoords="offset points",
            ha="center", va="bottom",
            fontsize=15, fontweight="bold", color=T["TEXT"],
        )

    # "~110x faster" annotation: arc from the tall bar down to the short bar.
    ax.annotate(
        "~110x faster",
        xy=(1, 70), xytext=(0.46, 1700),
        ha="center", va="center",
        fontsize=16, fontweight="bold", color=T["ACCENT_3"],
        arrowprops=dict(arrowstyle="-|>", color=T["ACCENT_3"], lw=2.2,
                        connectionstyle="arc3,rad=-0.32"),
        zorder=5,
    )

    # Axes cosmetics: maximize data-ink.
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=13, color=T["TEXT_2"])
    ax.set_ylabel("Query latency (ms, log scale)", fontsize=13, color=T["TEXT_2"])
    ax.tick_params(axis="y", labelsize=11, colors=T["TEXT_2"])
    ax.tick_params(axis="x", length=0)
    ax.set_xlim(-0.65, 1.65)

    ax.set_title("Example: a missing composite index",
                 fontsize=19, fontweight="bold", color=T["TEXT"],
                 pad=16, loc="left")

    ax.grid(axis="y", color=T["GRID"], linewidth=1, zorder=0)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(T["GRID"])

    # Muted source line.
    fig.text(0.012, 0.012,
             "Illustrative of a common composite-index fix.",
             fontsize=9.5, color=T["MUTED"], ha="left", va="bottom")

    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(OUT, dpi=DPI, facecolor=T["BG"])
    plt.close(fig)
    return OUT


if __name__ == "__main__":
    p = render()
    print(f"Rendered {p}")
