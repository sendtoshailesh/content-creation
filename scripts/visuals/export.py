"""Export helpers for generated visual assets."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

from .tokens import DPI


def save_png(image: Image.Image, path: str | Path, dpi: int = DPI) -> None:
    """Save a PNG with the repository-standard DPI and parent creation."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="PNG", dpi=(dpi, dpi))

