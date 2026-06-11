"""Deterministic QA pre-screen for generated images (programmatic OR AI).

The HTML/SVG inspectors cannot validate raster pixels, which left generated-image QA
subjective (vision/human only). This module adds objective, offline checks that run
*before* the visual-reviewer's manual/vision pass:

1. no-text       — OCR (tesseract) must find no confident words baked into the image.
2. color-fidelity — prominent saturated colors must be near a brand-token color.
3. negative-space — a usable fraction of low-variance area must exist for text overlay.

Findings use the shared severity schema (.github/instructions/shared/compliance-severity.md):
Error blocks publishing, Warning needs justification, Info is advisory.

Usage:
    python -m scripts.visuals.generated.inspect_image content/visuals/generated/*.png
    python -m scripts.visuals.generated.inspect_image hero.png --theme ocean
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageStat

from scripts.visuals.tokens import BASE_TOKENS, THEMES

# Neutral colors that may legitimately dominate a backdrop without being "brand" colors.
_NEUTRALS = ("#ffffff", "#000000", "#f8fafc", "#1e293b", "#475569", "#94a3b8", "#e5e7eb")


def _hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _dist(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> float:
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


def _saturation(rgb: tuple[int, int, int]) -> int:
    return max(rgb) - min(rgb)


def _brand_palette(theme: str | None) -> list[tuple[int, int, int]]:
    themes = [theme] if theme else list(THEMES)
    colors: set[str] = set(_NEUTRALS)
    for th in themes:
        colors |= set(v for k, v in THEMES[th].items() if v.startswith("#"))
    colors |= set(v for v in BASE_TOKENS.values() if isinstance(v, str) and v.startswith("#"))
    return [_hex_to_rgb(c) for c in colors]


# --- check 1: no embedded text -------------------------------------------------------

def check_no_text(path: Path) -> tuple[str, str]:
    """Return (severity, message). Uses tesseract if available."""
    if shutil.which("tesseract") is None:
        return ("Warning", "tesseract not installed — no-text check skipped (manual review).")
    try:
        out = subprocess.run(
            ["tesseract", str(path), "stdout", "--psm", "11"],
            capture_output=True,
            text=True,
            errors="ignore",
            timeout=60,
        ).stdout
    except (subprocess.SubprocessError, OSError) as err:  # pragma: no cover
        return ("Warning", f"tesseract failed ({err}) — no-text check skipped.")
    words = [w for w in out.split() if len(w) >= 3 and any(ch.isalpha() for ch in w)]
    if words:
        sample = ", ".join(words[:6])
        return ("Error", f"image-no-text: OCR found baked-in text ({len(words)} tokens: {sample}).")
    return ("Info", "image-no-text: no legible text detected.")


# --- check 2: brand-color fidelity ---------------------------------------------------

def check_color_fidelity(path: Path, theme: str | None) -> tuple[str, str]:
    palette = _brand_palette(theme)
    img = Image.open(path).convert("RGB")
    small = img.resize((160, 160))
    quant = small.quantize(colors=8).convert("RGB")
    counts = quant.getcolors(160 * 160) or []
    counts.sort(reverse=True)
    total = sum(n for n, _ in counts) or 1

    worst = 0.0
    worst_color: tuple[int, int, int] | None = None
    off_share = 0.0
    for n, color in counts:
        if _saturation(color) < 40:  # ignore near-neutral/background colors
            continue
        d = min(_dist(color, p) for p in palette)
        share = n / total
        if d > worst:
            worst, worst_color = d, color
        if d > 60:
            off_share += share

    if worst_color is None:
        return ("Info", "image-fidelity: no strongly saturated colors to check (neutral backdrop).")
    if off_share > 0.15:
        return (
            "Error",
            f"image-fidelity: {off_share:.0%} of the image is a saturated color far from the "
            f"brand palette (worst RGB {worst_color}, distance {worst:.0f}).",
        )
    if worst > 90:
        return ("Warning", f"image-fidelity: a saturated color (RGB {worst_color}) drifts from brand tokens (distance {worst:.0f}).")
    return ("Info", "image-fidelity: prominent colors are close to the brand palette.")


# --- check 3: negative space ---------------------------------------------------------

def check_negative_space(path: Path, min_ratio: float = 0.22) -> tuple[str, str]:
    img = Image.open(path).convert("RGB")
    w, h = img.size
    cols, rows = 12, 8
    cw, ch = max(1, w // cols), max(1, h // rows)
    calm = 0
    cells = 0
    for r in range(rows):
        for c in range(cols):
            box = (c * cw, r * ch, min((c + 1) * cw, w), min((r + 1) * ch, h))
            tile = img.crop(box)
            stddev = ImageStat.Stat(tile).stddev
            cells += 1
            if max(stddev) < 16:  # low variance => calm area usable for overlay
                calm += 1
    ratio = calm / max(1, cells)
    if ratio < min_ratio:
        return (
            "Warning",
            f"negative-space: only {ratio:.0%} calm area (< {min_ratio:.0%}); text overlay may be hard to place.",
        )
    return ("Info", f"negative-space: {ratio:.0%} calm area available for overlay.")


# --- driver --------------------------------------------------------------------------

_RANK = {"Error": 0, "Warning": 1, "Info": 2}


def inspect_image(
    path: str | Path, theme: str | None = None, *, allow_text: bool = False
) -> list[tuple[str, str]]:
    path = Path(path)
    text = check_no_text(path)
    if allow_text and text[0] == "Error":
        # Composited heroes (CSS title overlay) and charts legitimately contain text.
        text = ("Info", "image-no-text: text present and allowed (composited overlay / chart).")
    return [
        text,
        check_color_fidelity(path, theme),
        check_negative_space(path),
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Deterministic QA for generated images.")
    parser.add_argument("paths", nargs="+", help="PNG files to inspect.")
    parser.add_argument("--theme", default=None, choices=tuple(THEMES), help="Restrict color check to one theme.")
    parser.add_argument("--allow-text", action="store_true", help="Allow text (composited heroes / charts): downgrade no-text Error to Info.")
    args = parser.parse_args(argv)

    overall_fail = False
    print("| Severity | Asset | Finding |")
    print("|----------|-------|---------|")
    for p in args.paths:
        findings = inspect_image(p, args.theme, allow_text=args.allow_text)
        findings.sort(key=lambda f: _RANK[f[0]])
        for sev, msg in findings:
            print(f"| {sev} | {Path(p).name} | {msg} |")
            if sev == "Error":
                overall_fail = True
    verdict = "FAIL" if overall_fail else "PASS"
    print(f"\nGATE: {verdict}")
    return 1 if overall_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
