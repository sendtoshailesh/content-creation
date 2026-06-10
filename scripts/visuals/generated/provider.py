"""Provider-agnostic client + settings for AI image generation and vision grounding.

Keeps OpenAI and Azure OpenAI behind one interface so switching providers is a config
change (``IMAGE_PROVIDER``) rather than a code change. Settings are read from environment
variables (see ``.env.example``); ``.env`` is loaded automatically when python-dotenv is
available.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

try:  # optional convenience: load .env if present
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # pragma: no cover - dotenv is optional at runtime
    pass


@dataclass(frozen=True)
class ImageSettings:
    provider: str
    image_model: str
    vision_model: str
    size: str
    quality: str
    # OpenAI
    openai_api_key: str | None
    # Azure OpenAI
    azure_endpoint: str | None
    azure_api_key: str | None
    azure_api_version: str
    azure_image_api_version: str


def get_settings() -> ImageSettings:
    """Read image/vision settings from the environment."""
    return ImageSettings(
        provider=os.getenv("IMAGE_PROVIDER", "openai").strip().lower(),
        image_model=os.getenv("IMAGE_MODEL_NAME", "gpt-image-1"),
        vision_model=os.getenv("VISION_MODEL_NAME", "gpt-4o"),
        size=os.getenv("IMAGE_SIZE", "1024x1024"),
        quality=os.getenv("IMAGE_QUALITY", "medium"),
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"),
        azure_image_api_version=os.getenv(
            "AZURE_OPENAI_IMAGE_API_VERSION", "2025-04-01-preview"
        ),
    )


def get_client(settings: ImageSettings | None = None, *, for_images: bool = True):
    """Return a configured OpenAI/AzureOpenAI client.

    ``for_images=True`` selects the image API version on Azure; ``False`` selects the
    chat/vision API version. On plain OpenAI the same client serves both.
    """
    settings = settings or get_settings()

    if settings.provider == "openai":
        from openai import OpenAI

        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is not set (IMAGE_PROVIDER=openai).")
        return OpenAI(api_key=settings.openai_api_key)

    if settings.provider == "azure_openai":
        from openai import AzureOpenAI

        if not (settings.azure_endpoint and settings.azure_api_key):
            raise RuntimeError(
                "AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set "
                "(IMAGE_PROVIDER=azure_openai)."
            )
        api_version = (
            settings.azure_image_api_version
            if for_images
            else settings.azure_api_version
        )
        return AzureOpenAI(
            azure_endpoint=settings.azure_endpoint,
            api_key=settings.azure_api_key,
            api_version=api_version,
        )

    raise ValueError(
        f"Unknown IMAGE_PROVIDER {settings.provider!r}; expected 'openai' or 'azure_openai'."
    )
