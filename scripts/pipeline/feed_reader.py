#!/usr/bin/env python3
"""
Feed Reader — Multi-format blog roll / RSS / newsletter ingestion for the content pipeline.

Reads source configuration from content/feed-sources.md and fetches articles from:
  - RSS/Atom feeds (via feedparser)
  - Newsletter archive pages (via trafilatura link extraction)
  - Direct URLs (via trafilatura text extraction)
  - OPML subscription exports (parsed to RSS feed URLs)

Output: JSON array of articles written to stdout.

Usage:
  python scripts/pipeline/feed_reader.py
  python scripts/pipeline/feed_reader.py --sources content/feed-sources.md
  python scripts/pipeline/feed_reader.py --max-age 7
  python scripts/pipeline/feed_reader.py --sources content/feed-sources.md --max-age 14 --max-articles 50

Requires: feedparser, trafilatura, readability-lxml, requests
"""

import argparse
import json
import logging
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

try:
    import feedparser
except ImportError:
    sys.exit("ERROR: 'feedparser' package required. Install with: pip install feedparser")

try:
    import trafilatura
except ImportError:
    sys.exit("ERROR: 'trafilatura' package required. Install with: pip install trafilatura")

try:
    import requests
except ImportError:
    sys.exit("ERROR: 'requests' package required. Install with: pip install requests")

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger(__name__)

DEFAULT_SOURCES = "content/feed-sources.md"
DEFAULT_MAX_AGE_DAYS = 14
DEFAULT_MAX_ARTICLES = 100
REQUEST_TIMEOUT = 15
USER_AGENT = (
    "ContentPipeline-FeedReader/1.0 "
    "(+https://github.com/sendtoshailesh/content-creation)"
)


# ── Source config parsing ────────────────────────────────────────────────


def parse_sources_config(config_path: str) -> list[dict]:
    """Parse the source registry table from feed-sources.md."""
    path = Path(config_path)
    if not path.exists():
        log.error("Sources config not found: %s", config_path)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    sources = []

    # Find the Source Registry table — look for the header row pattern
    in_table = False
    header_seen = False
    for line in text.splitlines():
        stripped = line.strip()

        # Detect table header row: | Name | URL | Type | ...
        if not in_table and re.match(r"^\|\s*Name\s*\|", stripped, re.IGNORECASE):
            in_table = True
            header_seen = True
            continue

        # Skip separator row: |---|---|---|...|
        if in_table and re.match(r"^\|[\s\-:]+\|", stripped):
            continue

        # End of table
        if in_table and (not stripped.startswith("|") or stripped.startswith("###")):
            break

        if in_table and header_seen:
            cells = [c.strip() for c in stripped.split("|")]
            # Remove empty first/last from leading/trailing |
            cells = [c for c in cells if c]
            if len(cells) >= 4:
                sources.append(
                    {
                        "name": cells[0],
                        "url": cells[1],
                        "type": cells[2].lower(),
                        "frequency": cells[3].lower() if len(cells) > 3 else "daily",
                        "tags": [
                            t.strip()
                            for t in (cells[4].split(",") if len(cells) > 4 else [])
                        ],
                    }
                )

    log.info("Loaded %d sources from %s", len(sources), config_path)
    return sources


def parse_opml(opml_path: str) -> list[dict]:
    """Parse an OPML file and return a list of RSS feed source dicts."""
    path = Path(opml_path)
    if not path.exists():
        log.warning("OPML file not found: %s", opml_path)
        return []

    tree = ET.parse(path)  # noqa: S314 — trusted local file
    sources = []
    for outline in tree.iter("outline"):
        xml_url = outline.get("xmlUrl")
        if xml_url:
            title = outline.get("title") or outline.get("text") or xml_url
            sources.append(
                {
                    "name": title,
                    "url": xml_url,
                    "type": "rss",
                    "frequency": "daily",
                    "tags": [],
                }
            )
    log.info("Loaded %d feeds from OPML: %s", len(sources), opml_path)
    return sources


def parse_opml_paths_from_config(config_path: str) -> list[str]:
    """Extract OPML file paths from the feed-sources.md config."""
    path = Path(config_path)
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    paths = []
    in_opml_section = False
    for line in text.splitlines():
        if "OPML Import" in line or "OPML files" in line:
            in_opml_section = True
            continue
        if in_opml_section:
            if line.startswith("---") or (line.startswith("#") and "OPML" not in line):
                break
            match = re.match(r"^-\s+(.+\.opml)\s*$", line.strip())
            if match:
                paths.append(match.group(1).strip())
    return paths


# ── Feed fetching ────────────────────────────────────────────────────────


def fetch_rss(source: dict, max_age: timedelta) -> list[dict]:
    """Fetch and parse an RSS/Atom feed, returning articles within max_age."""
    url = source["url"]
    log.info("Fetching RSS: %s", url)

    feed = feedparser.parse(url, agent=USER_AGENT)
    if feed.bozo and not feed.entries:
        log.warning("Feed parse error for %s: %s", url, feed.bozo_exception)
        return []

    cutoff = datetime.now(timezone.utc) - max_age
    articles = []

    for entry in feed.entries:
        published = _parse_feed_date(entry)
        if published and published < cutoff:
            continue

        article = {
            "source_name": source["name"],
            "source_url": source["url"],
            "source_tags": source.get("tags", []),
            "title": entry.get("title", "").strip(),
            "url": entry.get("link", "").strip(),
            "published": published.isoformat() if published else None,
            "summary": _clean_html(entry.get("summary", "")),
            "full_text": None,
        }
        if article["url"]:
            articles.append(article)

    log.info("  Found %d articles within %d days", len(articles), max_age.days)
    return articles


def fetch_newsletter_archive(source: dict, max_age: timedelta) -> list[dict]:
    """Fetch a newsletter archive page, extract article links, return articles."""
    url = source["url"]
    log.info("Fetching newsletter archive: %s", url)

    try:
        resp = requests.get(
            url, timeout=REQUEST_TIMEOUT, headers={"User-Agent": USER_AGENT}
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        log.warning("Failed to fetch archive %s: %s", url, e)
        return []

    # Extract all links from the archive page
    links = trafilatura.extract_metadata(resp.text)
    # Fallback: parse links from HTML
    article_urls = _extract_links_from_html(resp.text, url)

    articles = []
    for article_url in article_urls[:20]:  # Cap to avoid fetching hundreds
        article = {
            "source_name": source["name"],
            "source_url": source["url"],
            "source_tags": source.get("tags", []),
            "title": "",
            "url": article_url,
            "published": None,
            "summary": "",
            "full_text": None,
        }
        articles.append(article)

    log.info("  Found %d article links from archive", len(articles))
    return articles


def fetch_direct_url(source: dict) -> list[dict]:
    """Fetch a single direct URL and extract its content."""
    url = source["url"]
    log.info("Fetching direct URL: %s", url)

    return [
        {
            "source_name": source["name"],
            "source_url": source["url"],
            "source_tags": source.get("tags", []),
            "title": source["name"],
            "url": url,
            "published": None,
            "summary": "",
            "full_text": None,
        }
    ]


def extract_full_text(article: dict) -> dict:
    """Fetch and extract full article text using trafilatura."""
    url = article["url"]
    if not url:
        return article

    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            text = trafilatura.extract(
                downloaded,
                include_comments=False,
                include_tables=True,
                favor_precision=True,
            )
            if text:
                article["full_text"] = text

            # Extract metadata for title/date if missing
            metadata = trafilatura.extract_metadata(downloaded)
            if metadata:
                if not article["title"] and metadata.title:
                    article["title"] = metadata.title
                if not article["published"] and metadata.date:
                    article["published"] = metadata.date
                if not article["summary"] and metadata.description:
                    article["summary"] = metadata.description
    except Exception as e:
        log.warning("Failed to extract text from %s: %s", url, e)

    return article


# ── Helpers ──────────────────────────────────────────────────────────────


def _parse_feed_date(entry) -> Optional[datetime]:
    """Parse a date from a feedparser entry."""
    for attr in ("published_parsed", "updated_parsed"):
        parsed = getattr(entry, attr, None)
        if parsed:
            try:
                from time import mktime

                return datetime.fromtimestamp(mktime(parsed), tz=timezone.utc)
            except (ValueError, OverflowError, OSError):
                continue
    return None


def _clean_html(text: str) -> str:
    """Strip HTML tags from a string."""
    if not text:
        return ""
    return re.sub(r"<[^>]+>", "", text).strip()


def _extract_links_from_html(html: str, base_url: str) -> list[str]:
    """Extract article-like links from an HTML page."""
    # Simple regex extraction — avoids heavy dependencies
    link_pattern = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
    matches = link_pattern.findall(html)

    parsed_base = urlparse(base_url)
    article_urls = []
    seen = set()

    for href in matches:
        # Resolve relative URLs
        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)

        # Filter: same domain or subdomain, looks like an article path
        if parsed.netloc and (
            parsed.netloc == parsed_base.netloc
            or parsed.netloc.endswith("." + parsed_base.netloc)
        ):
            # Skip obvious non-article paths
            path_lower = parsed.path.lower()
            if any(
                skip in path_lower
                for skip in [
                    "/tag/",
                    "/category/",
                    "/author/",
                    "/page/",
                    "/wp-content/",
                    "/wp-admin/",
                    "/feed",
                    "/rss",
                    ".xml",
                    ".css",
                    ".js",
                    ".png",
                    ".jpg",
                    ".gif",
                    "#",
                ]
            ):
                continue

            # Must have a meaningful path (not just /)
            if len(parsed.path) > 5 and full_url not in seen:
                seen.add(full_url)
                article_urls.append(full_url)

    return article_urls


# ── Main ─────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Feed Reader — Multi-format blog roll ingestion for the content pipeline"
    )
    parser.add_argument(
        "--sources",
        "-s",
        default=DEFAULT_SOURCES,
        help=f"Path to feed-sources.md config (default: {DEFAULT_SOURCES})",
    )
    parser.add_argument(
        "--max-age",
        "-a",
        type=int,
        default=DEFAULT_MAX_AGE_DAYS,
        help=f"Max article age in days (default: {DEFAULT_MAX_AGE_DAYS})",
    )
    parser.add_argument(
        "--max-articles",
        "-m",
        type=int,
        default=DEFAULT_MAX_ARTICLES,
        help=f"Max total articles to return (default: {DEFAULT_MAX_ARTICLES})",
    )
    parser.add_argument(
        "--full-text",
        action="store_true",
        default=False,
        help="Fetch full article text via trafilatura (slower but richer)",
    )
    parser.add_argument(
        "--source-name",
        help="Only fetch from this specific source (by name)",
    )
    args = parser.parse_args()

    max_age = timedelta(days=args.max_age)

    # Load sources from config
    sources = parse_sources_config(args.sources)

    # Load OPML sources if configured
    opml_paths = parse_opml_paths_from_config(args.sources)
    for opml_path in opml_paths:
        sources.extend(parse_opml(opml_path))

    if not sources:
        log.error("No sources found in %s", args.sources)
        json.dump({"error": "No sources configured", "config_path": args.sources}, sys.stdout, indent=2)
        sys.exit(1)

    # Filter to specific source if requested
    if args.source_name:
        sources = [s for s in sources if s["name"].lower() == args.source_name.lower()]
        if not sources:
            log.error("Source not found: %s", args.source_name)
            sys.exit(1)

    # Fetch articles from all sources
    all_articles: list[dict] = []
    source_health: list[dict] = []

    for source in sources:
        try:
            source_type = source["type"]
            if source_type == "rss":
                articles = fetch_rss(source, max_age)
            elif source_type == "newsletter-archive":
                articles = fetch_newsletter_archive(source, max_age)
            elif source_type == "direct-url":
                articles = fetch_direct_url(source)
            elif source_type == "opml":
                # OPML sources are expanded into RSS feeds during config loading
                continue
            else:
                log.warning("Unknown source type '%s' for %s", source_type, source["name"])
                continue

            source_health.append(
                {
                    "name": source["name"],
                    "articles_found": len(articles),
                    "status": "ok" if articles else "empty",
                }
            )
            all_articles.extend(articles)

        except Exception as e:
            log.warning("Failed to process source %s: %s", source["name"], e)
            source_health.append(
                {"name": source["name"], "articles_found": 0, "status": f"error: {e}"}
            )

    # Deduplicate by URL
    seen_urls: set[str] = set()
    unique_articles = []
    for article in all_articles:
        url_key = article["url"].lower().rstrip("/")
        if url_key not in seen_urls:
            seen_urls.add(url_key)
            unique_articles.append(article)
    all_articles = unique_articles

    # Fetch full text if requested
    if args.full_text:
        log.info("Extracting full text for %d articles...", len(all_articles))
        for i, article in enumerate(all_articles):
            if i >= args.max_articles:
                break
            all_articles[i] = extract_full_text(article)

    # Cap output
    all_articles = all_articles[: args.max_articles]

    # Output
    output = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "sources_processed": len(sources),
        "total_articles": len(all_articles),
        "max_age_days": args.max_age,
        "source_health": source_health,
        "articles": all_articles,
    }

    json.dump(output, sys.stdout, indent=2, ensure_ascii=False, default=str)


if __name__ == "__main__":
    main()
