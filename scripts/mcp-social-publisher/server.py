#!/usr/bin/env python3
"""
Social Publisher MCP Server — X/Twitter + YouTube posting tools.

Covers platforms NOT handled by existing free MCP servers:
- reddit-mcp-server (npm) handles Reddit
- mcp-linkedin (npm) handles LinkedIn

This server handles:
- X/Twitter posting via tweepy (API v2)
- YouTube metadata updates via Google API
- Content preview for any platform
- Credential validation

All posting tools require explicit human confirmation via a two-step
dry-run/confirm pattern. Nothing is posted without the user calling
the tool with dry_run=False.
"""

import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load .env from workspace root
_workspace = Path(__file__).resolve().parent.parent.parent
load_dotenv(_workspace / ".env")

mcp = FastMCP(
    "social-publisher",
    instructions=(
        "Social media publishing tools for X/Twitter and YouTube. "
        "LinkedIn is handled by the mcp-linkedin server; Reddit by reddit-mcp-server. "
        "All posting tools default to dry_run=True — preview first, then confirm."
    ),
)

# ── Paths ────────────────────────────────────────────────────────────────────

CONTENT_DIR = _workspace / "content"
DEFAULT_FILES = {
    "twitter": CONTENT_DIR / "x-twitter-thread.md",
    "youtube": CONTENT_DIR / "youtube-script.md",
    "linkedin": CONTENT_DIR / "linkedin-post.md",
    "reddit": CONTENT_DIR / "reddit-post.md",
    "reel": CONTENT_DIR / "reel-script.md",
}


# ── Helpers ──────────────────────────────────────────────────────────────────

def _read_content(file_path: str | None, platform: str) -> str:
    """Read content from the given file or the platform default."""
    path = Path(file_path) if file_path else DEFAULT_FILES.get(platform)
    if not path or not path.exists():
        raise FileNotFoundError(
            f"Content file not found: {path}. "
            f"Generate content first with the pipeline."
        )
    return path.read_text(encoding="utf-8")


def _parse_twitter_thread(content: str) -> list[str]:
    """Parse X/Twitter thread file into individual tweets.

    Looks for numbered tweet patterns like '1/' or '**1.**' or 'Tweet 1:'.
    Falls back to splitting on '---' separators.
    """
    # Try numbered pattern: "1/ ..." or "**1.** ..."
    pattern = r"(?:^|\n)(?:\*\*)?(\d+)[./](?:\*\*)?\s*(.*?)(?=\n(?:\*\*)?(?:\d+)[./]|\Z)"
    matches = re.findall(pattern, content, re.DOTALL)
    if matches:
        tweets = [text.strip() for _, text in matches if text.strip()]
        if tweets:
            return tweets

    # Fallback: split on --- separators
    parts = re.split(r"\n---+\n", content)
    tweets = [p.strip() for p in parts if p.strip() and len(p.strip()) < 500]
    return tweets if tweets else [content[:280]]


def _log_publish(platform: str, url: str, status: str) -> None:
    """Append a publish event to content/publishing-log.md."""
    log_path = CONTENT_DIR / "publishing-log.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    entry = f"| {ts} | {platform} | {url} | {status} |\n"

    if not log_path.exists():
        header = (
            "# Publishing Log\n\n"
            "| Timestamp | Platform | URL | Status |\n"
            "|-----------|----------|-----|--------|\n"
        )
        log_path.write_text(header + entry, encoding="utf-8")
    else:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(entry)


# ── Tools ────────────────────────────────────────────────────────────────────

@mcp.tool()
def check_credentials() -> str:
    """Check which social media platform credentials are configured.

    Returns a status report showing which platforms have credentials set
    and which are missing. Does not validate tokens — only checks env vars.
    """
    checks = {
        "X/Twitter (custom MCP)": all(
            os.environ.get(k)
            for k in [
                "TWITTER_API_KEY",
                "TWITTER_API_SECRET",
                "TWITTER_ACCESS_TOKEN",
                "TWITTER_ACCESS_SECRET",
            ]
        ),
        "YouTube (custom MCP)": all(
            os.environ.get(k)
            for k in ["YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET"]
        ),
        "LinkedIn (mcp-linkedin)": all(
            os.environ.get(k) for k in ["UNIPILE_API_KEY", "UNIPILE_DSN"]
        ),
        "Reddit (reddit-mcp-server)": all(
            os.environ.get(k)
            for k in ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET"]
        ),
    }
    lines = ["## Credential Status\n"]
    for platform, ok in checks.items():
        icon = "✅" if ok else "❌"
        lines.append(f"- {icon} **{platform}**: {'Configured' if ok else 'Missing'}")

    configured = sum(1 for v in checks.values() if v)
    lines.append(f"\n**{configured}/{len(checks)}** platforms ready.")
    return "\n".join(lines)


@mcp.tool()
def preview_content(platform: str, file_path: str | None = None) -> str:
    """Preview social media content for any platform before posting.

    Args:
        platform: One of 'twitter', 'linkedin', 'reddit', 'youtube', 'reel'
        file_path: Optional path to content file. Defaults to standard location.

    Returns:
        Formatted preview of the content that would be posted.
    """
    content = _read_content(file_path, platform)

    if platform == "twitter":
        tweets = _parse_twitter_thread(content)
        preview_lines = [f"## X/Twitter Thread Preview ({len(tweets)} tweets)\n"]
        for i, tweet in enumerate(tweets, 1):
            char_count = len(tweet)
            status = "✅" if char_count <= 280 else f"⚠️ {char_count}/280 chars"
            preview_lines.append(f"**{i}/{len(tweets)}** [{status}]")
            preview_lines.append(f"> {tweet[:300]}\n")
        return "\n".join(preview_lines)

    # For other platforms, show content summary
    lines = content.split("\n")
    char_count = len(content)
    word_count = len(content.split())
    return (
        f"## {platform.title()} Content Preview\n\n"
        f"- **Characters**: {char_count:,}\n"
        f"- **Words**: {word_count:,}\n"
        f"- **Lines**: {len(lines):,}\n\n"
        f"### First 500 characters:\n\n"
        f"> {content[:500]}..."
    )


@mcp.tool()
def post_to_twitter(
    file_path: str | None = None,
    dry_run: bool = True,
) -> str:
    """Post a thread to X/Twitter from the generated content file.

    IMPORTANT: dry_run defaults to True. Call with dry_run=True first to preview,
    then call again with dry_run=False to actually post. Nothing is published
    without explicit confirmation.

    Args:
        file_path: Path to the X/Twitter thread file. Defaults to content/x-twitter-thread.md
        dry_run: If True (default), returns preview without posting. Set False to post.

    Returns:
        Preview (dry_run=True) or posted tweet URLs (dry_run=False).
    """
    content = _read_content(file_path, "twitter")
    tweets = _parse_twitter_thread(content)

    if not tweets:
        return "❌ No tweets found in content file. Check the format."

    # Validate tweet lengths
    over_limit = [(i, len(t)) for i, t in enumerate(tweets, 1) if len(t) > 280]

    if dry_run:
        lines = [
            "## 🐦 X/Twitter Thread — DRY RUN PREVIEW\n",
            f"**Tweets**: {len(tweets)}",
        ]
        if over_limit:
            lines.append(
                f"**⚠️ Over 280 chars**: {', '.join(f'#{i} ({c} chars)' for i, c in over_limit)}"
            )
        lines.append("")
        for i, tweet in enumerate(tweets, 1):
            lines.append(f"**{i}/{len(tweets)}** ({len(tweet)} chars)")
            lines.append(f"> {tweet}\n")
        lines.append("---")
        lines.append("**To post**: Call `post_to_twitter` with `dry_run=False`")
        return "\n".join(lines)

    # ── Actually post ────────────────────────────────────────────────
    for key in ["TWITTER_API_KEY", "TWITTER_API_SECRET", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"]:
        if not os.environ.get(key):
            return f"❌ Missing credential: {key}. See docs/social-api-setup.md"

    try:
        import tweepy
    except ImportError:
        return "❌ tweepy not installed. Run: pip install -r requirements.txt"

    client = tweepy.Client(
        consumer_key=os.environ["TWITTER_API_KEY"],
        consumer_secret=os.environ["TWITTER_API_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_SECRET"],
    )

    posted_urls = []
    reply_to_id = None

    for i, tweet_text in enumerate(tweets):
        if len(tweet_text) > 280:
            tweet_text = tweet_text[:277] + "..."

        response = client.create_tweet(
            text=tweet_text,
            in_reply_to_tweet_id=reply_to_id,
        )
        tweet_id = response.data["id"]
        url = f"https://x.com/i/status/{tweet_id}"
        posted_urls.append(url)
        reply_to_id = tweet_id

    # Log results
    _log_publish("X/Twitter", posted_urls[0], f"Thread posted ({len(posted_urls)} tweets)")

    lines = [f"## ✅ X/Twitter Thread Posted ({len(posted_urls)} tweets)\n"]
    for i, url in enumerate(posted_urls, 1):
        lines.append(f"{i}. {url}")
    return "\n".join(lines)


@mcp.tool()
def update_youtube_metadata(
    video_id: str,
    title: str | None = None,
    description: str | None = None,
    tags: list[str] | None = None,
    dry_run: bool = True,
) -> str:
    """Update YouTube video title, description, and/or tags.

    IMPORTANT: dry_run defaults to True. Preview first, then confirm.
    Does NOT upload videos — only updates metadata on existing videos.

    Args:
        video_id: YouTube video ID (the part after v= in the URL)
        title: New video title. If None, keeps current.
        description: New description. If None, reads from content/youtube-script.md.
        tags: List of tags. If None, keeps current.
        dry_run: If True (default), shows what would change. Set False to update.

    Returns:
        Preview of changes (dry_run=True) or confirmation (dry_run=False).
    """
    if not description:
        try:
            content = _read_content(None, "youtube")
            # Extract description section if present
            desc_match = re.search(
                r"(?:## Description|## Video Description)\s*\n(.*?)(?=\n## |\Z)",
                content,
                re.DOTALL,
            )
            if desc_match:
                description = desc_match.group(1).strip()
        except FileNotFoundError:
            pass

    if dry_run:
        lines = [
            "## 📺 YouTube Metadata — DRY RUN PREVIEW\n",
            f"**Video ID**: {video_id}",
            f"**URL**: https://youtube.com/watch?v={video_id}\n",
        ]
        if title:
            lines.append(f"**New title**: {title}")
        if description:
            lines.append(f"**New description** ({len(description)} chars):")
            lines.append(f"> {description[:300]}...")
        if tags:
            lines.append(f"**Tags**: {', '.join(tags)}")
        lines.append("\n---")
        lines.append("**To update**: Call `update_youtube_metadata` with `dry_run=False`")
        return "\n".join(lines)

    # ── Actually update ──────────────────────────────────────────────
    for key in ["YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET"]:
        if not os.environ.get(key):
            return f"❌ Missing credential: {key}. See docs/social-api-setup.md"

    try:
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
    except ImportError:
        return "❌ google-api-python-client not installed. Run: pip install -r requirements.txt"

    token_path = _workspace / ".youtube-token.json"
    if not token_path.exists():
        return (
            "❌ YouTube OAuth token not found. Run the one-time auth flow:\n"
            "  python scripts/mcp-social-publisher/youtube_auth.py"
        )

    token_data = json.loads(token_path.read_text())
    creds = Credentials.from_authorized_user_info(token_data)
    youtube = build("youtube", "v3", credentials=creds)

    # Get current video metadata
    video_response = youtube.videos().list(part="snippet", id=video_id).execute()
    if not video_response.get("items"):
        return f"❌ Video not found: {video_id}"

    snippet = video_response["items"][0]["snippet"]
    if title:
        snippet["title"] = title
    if description:
        snippet["description"] = description
    if tags:
        snippet["tags"] = tags

    youtube.videos().update(
        part="snippet",
        body={"id": video_id, "snippet": snippet},
    ).execute()

    url = f"https://youtube.com/watch?v={video_id}"
    _log_publish("YouTube", url, "Metadata updated")

    return (
        f"## ✅ YouTube Metadata Updated\n\n"
        f"**Video**: {url}\n"
        f"**Title**: {snippet['title']}\n"
        f"**Tags**: {', '.join(snippet.get('tags', []))}"
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
