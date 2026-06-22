"""Hand-drawn style via matplotlib xkcd(): sketchy, approachable charts and timelines.

Zero new dependencies. The sketch effect comes from matplotlib's path-sketch filter
(applied by ``plt.xkcd()``), so it works even when the Humor Sans font is absent.
Best for concepts, "napkin" mental models, and approachable maturity/timeline visuals.
"""

from __future__ import annotations

import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

from scripts.visuals.tokens import THEMES


def sketch_maturity_steps(
    out_path: str | Path,
    *,
    title: str,
    subtitle: str,
    stages: list[tuple[str, str, str]],
    source: str,
    theme: str = "ocean",
    width_px: int = 3200,
    height_px: int = 1520,
) -> Path:
    """Ascending hand-drawn step path. ``stages`` = list of (num, title, desc)."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    t = THEMES[theme]
    series = [t["ACCENT"], t["ACCENT_2"], t["ACCENT_3"], t["SUCCESS"]]

    dpi = 200
    fig_w, fig_h = width_px / dpi, height_px / dpi

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with plt.xkcd(scale=1.1, length=110, randomness=2):
            fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)
            ax.set_xlim(0, 4)
            ax.set_ylim(0, 4)
            ax.axis("off")

            n = len(stages)
            ys = [0.98 + i * (2.45 / max(1, n - 1)) for i in range(n)]
            xs = [0.62 + i * (2.78 / max(1, n - 1)) for i in range(n)]
            bw, bh = 0.98, 0.82

            # Connecting hand-drawn arrows first (so boxes sit on top).
            for i in range(n - 1):
                ax.add_patch(
                    FancyArrowPatch(
                        (xs[i] + bw / 2, ys[i] + bh / 2),
                        (xs[i + 1] - bw / 2, ys[i + 1] + bh / 2),
                        arrowstyle="-|>",
                        mutation_scale=26,
                        lw=2.4,
                        color=t["ACCENT_3"],
                        connectionstyle="arc3,rad=0.18",
                    )
                )

            for i, (num, label, desc) in enumerate(stages):
                color = series[i % len(series)]
                x, y = xs[i], ys[i]
                ax.add_patch(
                    FancyBboxPatch(
                        (x - bw / 2, y - bh / 2),
                        bw,
                        bh,
                        boxstyle="round,pad=0.02,rounding_size=0.06",
                        linewidth=2.6,
                        edgecolor=color,
                        facecolor="white",
                    )
                )
                ax.text(
                    x, y + 0.26, num, ha="center", va="center",
                    fontsize=26, fontweight="bold", color=color,
                )
                ax.text(
                    x, y + 0.04, label, ha="center", va="center",
                    fontsize=15, fontweight="bold", color="#1e293b",
                )
                # Wrap the description to two short lines.
                words = desc.split()
                mid = len(words) // 2 or 1
                line1 = " ".join(words[:mid])
                line2 = " ".join(words[mid:])
                ax.text(
                    x, y - 0.18, line1, ha="center", va="center",
                    fontsize=11, color="#475569",
                )
                if line2:
                    ax.text(
                        x, y - 0.28, line2, ha="center", va="center",
                        fontsize=11, color="#475569",
                    )

            ax.text(
                0.05, 3.85, title, ha="left", va="top",
                fontsize=27, fontweight="bold", color="#1e293b",
                transform=ax.transData,
            )
            ax.text(
                0.05, 3.50, subtitle, ha="left", va="top",
                fontsize=15, color="#475569", transform=ax.transData,
            )
            ax.text(
                0.05, 0.08, source, ha="left", va="bottom",
                fontsize=11, color="#94a3b8", transform=ax.transData,
            )

            fig.savefig(out_path, dpi=dpi, bbox_inches="tight", facecolor="white")
            plt.close(fig)
    return out_path


def sketch_checklist(
    out_path: str | Path,
    *,
    title: str,
    subtitle: str,
    steps: list[tuple[str, str]],
    source: str,
    theme: str = "ocean",
    width_px: int = 3200,
    height_px: int = 1520,
) -> Path:
    """Hand-drawn numbered checklist. ``steps`` = list of (num, text)."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    t = THEMES[theme]
    disc_color = t["ACCENT"]

    dpi = 200
    fig_w, fig_h = width_px / dpi, height_px / dpi
    n = len(steps)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with plt.xkcd(scale=1.0, length=120, randomness=2):
            fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 5)
            ax.axis("off")

            top, bottom = 3.55, 0.62
            ys = [top - i * ((top - bottom) / max(1, n - 1)) for i in range(n)]
            row_h = 0.62

            for i, (num, label) in enumerate(steps):
                y = ys[i]
                ax.add_patch(
                    FancyBboxPatch(
                        (0.6, y - row_h / 2),
                        8.8,
                        row_h,
                        boxstyle="round,pad=0.02,rounding_size=0.08",
                        linewidth=2.4,
                        edgecolor="#cbd5e1",
                        facecolor="white",
                    )
                )
                # Number disc (kept hand-drawn for character).
                ax.add_patch(
                    Circle((1.25, y), 0.27, color=disc_color, zorder=3)
                )
                # Crisp digit: disable the xkcd sketch filter so it stays legible.
                num_txt = ax.text(
                    1.25, y, num, ha="center", va="center",
                    fontsize=19, fontweight="bold", color="white", zorder=4,
                )
                num_txt.set_path_effects([pe.Normal()])
                ax.text(
                    1.95, y, label, ha="left", va="center",
                    fontsize=16, color="#1e293b",
                )

            ax.text(
                0.45, 4.85, title, ha="left", va="top",
                fontsize=27, fontweight="bold", color="#1e293b",
            )
            ax.text(
                0.45, 4.42, subtitle, ha="left", va="top",
                fontsize=15, color="#475569",
            )
            ax.text(
                0.45, 0.06, source, ha="left", va="bottom",
                fontsize=11, color="#94a3b8",
            )

            fig.savefig(out_path, dpi=dpi, bbox_inches="tight", facecolor="white")
            plt.close(fig)
    return out_path
