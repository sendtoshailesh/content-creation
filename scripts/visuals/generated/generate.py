"""Generate a hero/illustrative image from a prompt and persist it with a sidecar.

Usage:
    python -m scripts.visuals.generated.generate \
        --prompt "Editorial wide shot of an empty modern test lab, soft blue key light, ~30% negative space on the right, no text" \
        --out content/visuals/generated/part1-hero.png

Every output writes ``<image>.json`` recording provider, model, prompt, size, quality, and
cache key for reproducibility and audit. A prompt-hash cache reuses identical requests.

Constraints (enforced by the prompt grammar in the vision-grounding skill, not here):
no embedded text, brand-color fidelity, ~30% negative space.
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
import time
from pathlib import Path

from .cache import cache_key, find_cached, sidecar_path
from .provider import ImageSettings, get_client, get_settings


def _b64_from_response(response) -> str:
    data = response.data[0]
    b64 = getattr(data, "b64_json", None)
    if b64:
        return b64
    # Some providers return a URL instead of base64; fetch it.
    url = getattr(data, "url", None)
    if url:
        import urllib.request

        with urllib.request.urlopen(url) as fh:  # noqa: S310 - provider-controlled URL
            return base64.b64encode(fh.read()).decode("ascii")
    raise RuntimeError("Image response contained neither b64_json nor url.")


def generate_image(
    prompt: str,
    out_path: str | Path,
    *,
    settings: ImageSettings | None = None,
    size: str | None = None,
    quality: str | None = None,
    force: bool = False,
    retries: int = 3,
) -> Path:
    settings = settings or get_settings()
    size = size or settings.size
    quality = quality or settings.quality
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    key = cache_key(
        prompt,
        provider=settings.provider,
        model=settings.image_model,
        size=size,
        quality=quality,
    )
    if not force:
        hit = find_cached(key, out_path.parent)
        if hit is not None:
            print(f"[cache hit] {hit} (key={key})", file=sys.stderr)
            return hit

    client = get_client(settings, for_images=True)

    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = client.images.generate(
                model=settings.image_model,
                prompt=prompt,
                size=size,
                quality=quality,
                n=1,
            )
            b64 = _b64_from_response(response)
            out_path.write_bytes(base64.b64decode(b64))
            break
        except Exception as err:  # pragma: no cover - network/provider errors
            last_err = err
            wait = 2**attempt
            print(
                f"[retry {attempt}/{retries}] {type(err).__name__}: {err} "
                f"(waiting {wait}s)",
                file=sys.stderr,
            )
            time.sleep(wait)
    else:
        raise RuntimeError(f"Image generation failed after {retries} attempts") from last_err

    meta = {
        "cache_key": key,
        "provider": settings.provider,
        "model": settings.image_model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "family": "ai-generated-imagery",
        "constraints": ["no-embedded-text", "brand-color-fidelity", "~30% negative space"],
    }
    sidecar_path(out_path).write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[generated] {out_path} (key={key})", file=sys.stderr)
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a hero/illustrative image.")
    parser.add_argument("--prompt", required=True, help="Consolidated image prompt.")
    parser.add_argument("--out", required=True, help="Output PNG path.")
    parser.add_argument("--size", default=None, help="Override IMAGE_SIZE.")
    parser.add_argument("--quality", default=None, help="Override IMAGE_QUALITY.")
    parser.add_argument("--force", action="store_true", help="Ignore the cache.")
    args = parser.parse_args(argv)

    generate_image(
        args.prompt,
        args.out,
        size=args.size,
        quality=args.quality,
        force=args.force,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
