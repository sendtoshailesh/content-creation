"""Describe a reference image with a vision model to ground image generation.

Mirrors the reference accelerator's ingestion step: a reference/brand/source image is sent
to a vision model, which returns a detailed text description (colors, materials, shape, key
features, composition, style). That description becomes grounding context in the consolidated
image prompt (see the ``vision-grounding`` skill).

Usage:
    python -m scripts.visuals.generated.describe --image path/or/url \
        [--append content/visuals/generated/reference-descriptions.md --label "Brand hero A"]
"""

from __future__ import annotations

import argparse
import base64
import mimetypes
import sys
import time
from pathlib import Path

from .provider import ImageSettings, get_client, get_settings

PROMPT = (
    "Describe this image in detail for use as grounding context in marketing/illustrative "
    "image generation. Include: dominant colors (with approximate hex if obvious), materials "
    "and textures, shapes, key visual features, composition and subject positioning, lighting, "
    "and overall style/aesthetic. Be specific enough that an image generator could recreate a "
    "similar look. Do not mention any text or letterforms in the image."
)


def _to_image_url(image: str) -> str:
    """Return a usable image_url: pass through http(s), else inline as a data URL."""
    if image.startswith(("http://", "https://", "data:")):
        return image
    path = Path(image)
    if not path.exists():
        raise FileNotFoundError(image)
    mime = mimetypes.guess_type(str(path))[0] or "image/png"
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def describe_image(
    image: str, *, settings: ImageSettings | None = None, retries: int = 3
) -> str:
    settings = settings or get_settings()
    client = get_client(settings, for_images=False)
    image_url = _to_image_url(image)

    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = client.chat.completions.create(
                model=settings.vision_model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": PROMPT},
                            {"type": "image_url", "image_url": {"url": image_url}},
                        ],
                    }
                ],
                max_tokens=500,
            )
            return (response.choices[0].message.content or "").strip()
        except Exception as err:  # pragma: no cover - network/provider errors
            last_err = err
            wait = 2**attempt
            print(
                f"[retry {attempt}/{retries}] {type(err).__name__}: {err} "
                f"(waiting {wait}s)",
                file=sys.stderr,
            )
            time.sleep(wait)
    raise RuntimeError(f"Vision description failed after {retries} attempts") from last_err


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Describe a reference image for grounding.")
    parser.add_argument("--image", required=True, help="Local path or http(s) URL.")
    parser.add_argument("--append", default=None, help="Markdown file to append to.")
    parser.add_argument("--label", default=None, help="Heading label for the appended block.")
    args = parser.parse_args(argv)

    description = describe_image(args.image)
    print(description)

    if args.append:
        target = Path(args.append)
        target.parent.mkdir(parents=True, exist_ok=True)
        label = args.label or args.image
        block = f"\n## {label}\n\n_Source: `{args.image}`_\n\n{description}\n"
        with target.open("a", encoding="utf-8") as fh:
            fh.write(block)
        print(f"[appended] {target}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
