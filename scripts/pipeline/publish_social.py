#!/usr/bin/env python3
"""
Publish social media content from generated Markdown files.

Standalone script for CI/CD or terminal use. Does NOT use MCP — calls
platform APIs directly via their Python clients.

Usage:
  python scripts/pipeline/publish_social.py --dry-run --platform linkedin,reddit
  python scripts/pipeline/publish_social.py --platform twitter
  python scripts/pipeline/publish_social.py --all --dry-run

Environment variables (loaded from .env):
  REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD
  UNIPILE_API_KEY, UNIPILE_DSN
  TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# Add workspace root to path
WORKSPACE = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = WORKSPACE / "content"

try:
    from dotenv import load_dotenv
    load_dotenv(WORKSPACE / ".env")
except ImportError:
    pass  # dotenv optional in CI (env vars set by GitHub Secrets)

DEFAULT_FILES = {
    "linkedin": CONTENT_DIR / "linkedin-post.md",
    "twitter": CONTENT_DIR / "x-twitter-thread.md",
    "reddit": CONTENT_DIR / "reddit-post.md",
    "youtube": CONTENT_DIR / "youtube-script.md",
}


def read_content(platform: str) -> str:
    """Read the content file for a platform."""
    path = DEFAULT_FILES.get(platform)
    if not path or not path.exists():
        # Try part-specific files
        for p in CONTENT_DIR.glob(f"*{platform}*part*.md"):
            return p.read_text(encoding="utf-8")
        raise FileNotFoundError(f"No content file found for {platform}: {path}")
    return path.read_text(encoding="utf-8")


def parse_twitter_thread(content: str) -> list[str]:
    """Parse X/Twitter thread into individual tweets."""
    # Extract content between START/END COPY markers for the thread section
    copy_blocks = re.findall(
        r"── START COPY ──\s*\n(.*?)\n\s*── END COPY ──",
        content,
        re.DOTALL,
    )
    if copy_blocks:
        content = max(copy_blocks, key=len)

    pattern = r"(?:^|\n)(?:\*\*)?(\d+)[./](?:\*\*)?\s*(.*?)(?=\n(?:\*\*)?(?:\d+)[./]|\Z)"
    matches = re.findall(pattern, content, re.DOTALL)
    if matches:
        tweets = [text.strip() for _, text in matches if text.strip()]
        if tweets:
            return tweets
    parts = re.split(r"\n---+\n", content)
    return [p.strip() for p in parts if p.strip() and len(p.strip()) < 500] or [content[:280]]


def log_result(platform: str, url: str, status: str) -> None:
    """Append to publishing-log.md."""
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


# ── Platform Publishers ──────────────────────────────────────────────────────

def publish_linkedin(dry_run: bool) -> dict:
    """Publish to LinkedIn via Unipile API."""
    content = read_content("linkedin")
    api_key = os.environ.get("UNIPILE_API_KEY", "")
    dsn = os.environ.get("UNIPILE_DSN", "")

    if not api_key or not dsn:
        return {"status": "error", "message": "Missing UNIPILE_API_KEY or UNIPILE_DSN"}

    # Extract the formatted post content (between START COPY / END COPY markers)
    copy_match = re.search(
        r"── START COPY ──\s*\n(.*?)\n\s*── END COPY ──",
        content,
        re.DOTALL,
    )
    post_text = copy_match.group(1).strip() if copy_match else content[:3000]

    if dry_run:
        return {
            "status": "dry_run",
            "platform": "LinkedIn",
            "chars": len(post_text),
            "preview": post_text[:200] + "...",
        }

    # Post via Unipile API
    url = f"https://{dsn}/api/v1/posts"
    payload = json.dumps({"text": post_text}).encode()
    req = Request(url, data=payload, method="POST")
    req.add_header("X-API-KEY", api_key)
    req.add_header("Content-Type", "application/json")

    try:
        with urlopen(req) as resp:
            result = json.loads(resp.read())
        post_url = result.get("url", "posted")
        log_result("LinkedIn", post_url, "Published")
        return {"status": "published", "platform": "LinkedIn", "url": post_url}
    except HTTPError as e:
        msg = e.read().decode() if e.fp else str(e)
        return {"status": "error", "platform": "LinkedIn", "message": msg}


def publish_twitter(dry_run: bool) -> dict:
    """Publish thread to X/Twitter via tweepy."""
    content = read_content("twitter")
    tweets = parse_twitter_thread(content)

    for key in ["TWITTER_API_KEY", "TWITTER_API_SECRET", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"]:
        if not os.environ.get(key):
            return {"status": "error", "message": f"Missing {key}"}

    if dry_run:
        over = [(i, len(t)) for i, t in enumerate(tweets, 1) if len(t) > 280]
        return {
            "status": "dry_run",
            "platform": "X/Twitter",
            "tweets": len(tweets),
            "over_limit": over,
            "preview": tweets[0][:200] + "..." if tweets else "",
        }

    try:
        import tweepy
    except ImportError:
        return {"status": "error", "message": "tweepy not installed"}

    client = tweepy.Client(
        consumer_key=os.environ["TWITTER_API_KEY"],
        consumer_secret=os.environ["TWITTER_API_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_SECRET"],
    )

    urls = []
    reply_to = None
    for tweet_text in tweets:
        if len(tweet_text) > 280:
            tweet_text = tweet_text[:277] + "..."
        resp = client.create_tweet(text=tweet_text, in_reply_to_tweet_id=reply_to)
        tid = resp.data["id"]
        urls.append(f"https://x.com/i/status/{tid}")
        reply_to = tid

    log_result("X/Twitter", urls[0], f"Thread ({len(urls)} tweets)")
    return {"status": "published", "platform": "X/Twitter", "urls": urls}


def publish_reddit(dry_run: bool, subreddit: str = "test") -> dict:
    """Publish to Reddit via PRAW."""
    content = read_content("reddit")

    for key in ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USERNAME", "REDDIT_PASSWORD"]:
        if not os.environ.get(key):
            return {"status": "error", "message": f"Missing {key}"}

    # Extract title (first # heading or first line)
    title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else content.split("\n")[0][:300]

    # Remove the title line from body
    body = re.sub(r"^#\s+.+\n*", "", content, count=1).strip()

    if dry_run:
        return {
            "status": "dry_run",
            "platform": "Reddit",
            "subreddit": f"r/{subreddit}",
            "title": title[:100] + "..." if len(title) > 100 else title,
            "body_chars": len(body),
            "preview": body[:200] + "...",
        }

    try:
        import praw
    except ImportError:
        return {"status": "error", "message": "praw not installed"}

    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        username=os.environ["REDDIT_USERNAME"],
        password=os.environ["REDDIT_PASSWORD"],
        user_agent=f"content-pipeline:v1.0 (by /u/{os.environ['REDDIT_USERNAME']})",
    )

    submission = reddit.subreddit(subreddit).submit(title=title, selftext=body)
    url = f"https://www.reddit.com{submission.permalink}"
    log_result("Reddit", url, f"Posted to r/{subreddit}")
    return {"status": "published", "platform": "Reddit", "url": url, "subreddit": f"r/{subreddit}"}


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Publish social media content from pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    parser.add_argument("--platform", type=str, default="", help="Comma-separated: linkedin,twitter,reddit")
    parser.add_argument("--all", action="store_true", help="Post to all platforms with content files")
    parser.add_argument("--subreddit", type=str, default="test", help="Target subreddit (default: test)")
    args = parser.parse_args()

    if args.all:
        platforms = ["linkedin", "twitter", "reddit"]
    elif args.platform:
        platforms = [p.strip().lower() for p in args.platform.split(",")]
    else:
        print("Specify --platform or --all", file=sys.stderr)
        sys.exit(1)

    results = []
    for platform in platforms:
        print(f"\n{'=' * 40}")
        print(f"  {platform.upper()}")
        print(f"{'=' * 40}")

        try:
            if platform == "linkedin":
                result = publish_linkedin(args.dry_run)
            elif platform == "twitter":
                result = publish_twitter(args.dry_run)
            elif platform == "reddit":
                result = publish_reddit(args.dry_run, args.subreddit)
            else:
                result = {"status": "skipped", "message": f"Unknown platform: {platform}"}
        except FileNotFoundError as e:
            result = {"status": "skipped", "message": str(e)}
        except Exception as e:
            result = {"status": "error", "message": str(e)}

        results.append(result)
        print(json.dumps(result, indent=2))

    # Summary
    print(f"\n{'=' * 40}")
    print("  SUMMARY")
    print(f"{'=' * 40}")
    for r in results:
        icon = {"published": "✅", "dry_run": "👀", "error": "❌", "skipped": "⏭️"}.get(r.get("status"), "?")
        print(f"  {icon} {r.get('platform', 'unknown')}: {r.get('status')}")

    # Output JSON for CI consumption
    json.dump(results, sys.stdout)
    print()


if __name__ == "__main__":
    main()
