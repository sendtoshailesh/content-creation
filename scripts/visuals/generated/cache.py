"""Prompt-hash cache for generated images.

Generation is the expensive/non-deterministic step, so we key outputs by a hash of the
exact request (provider, model, size, quality, prompt). A cache hit reuses the existing
PNG, which controls spend and keeps series visuals consistent across reruns.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

GENERATED_DIR = Path("content/visuals/generated")


def cache_key(prompt: str, *, provider: str, model: str, size: str, quality: str) -> str:
    """Stable short hash of the full image request."""
    payload = json.dumps(
        {
            "provider": provider,
            "model": model,
            "size": size,
            "quality": quality,
            "prompt": prompt,
        },
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def sidecar_path(image_path: str | Path) -> Path:
    """Sidecar JSON path for a given image (``hero.png`` -> ``hero.png.json``)."""
    return Path(str(image_path) + ".json")


def find_cached(key: str, directory: str | Path = GENERATED_DIR) -> Path | None:
    """Return an existing image whose sidecar matches ``key``, if any."""
    directory = Path(directory)
    if not directory.exists():
        return None
    for sidecar in directory.glob("*.json"):
        try:
            meta = json.loads(sidecar.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if meta.get("cache_key") == key:
            image = Path(str(sidecar)[: -len(".json")])
            if image.exists():
                return image
    return None
