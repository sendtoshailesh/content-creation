#!/usr/bin/env python3
"""
Reading List Reader — Chrome Reading List ingestion for the content pipeline.

Reads Chrome's local Bookmarks JSON file, extracts Reading List entries,
filters by time range and read status, and optionally fetches full article text.

Output: JSON to stdout (compatible with feed_reader.py schema).

Usage:
  python scripts/pipeline/reading_list_reader.py
  python scripts/pipeline/reading_list_reader.py --time-range 7d
  python scripts/pipeline/reading_list_reader.py --time-range 1m --read-status unread
  python scripts/pipeline/reading_list_reader.py --time-range 2w --full-text --profile Default

Time ranges: 1d, 3d, 7d, 2w, 3w, 1m, 3m, 6m, all, or Xd/Xw/Xm for custom.

Requires: trafilatura (optional, for --full-text)
"""

import argparse
import json
import logging
import os
import platform
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger(__name__)

# Chrome timestamps are microseconds since 1601-01-01 00:00:00 UTC
CHROME_EPOCH_OFFSET = 11644473600  # seconds between 1601-01-01 and 1970-01-01


def get_chrome_profile_path(profile: str = "Default") -> Path:
    """Return the Chrome profile directory path for the current OS."""
    system = platform.system()
    home = Path.home()

    if system == "Darwin":
        base = home / "Library" / "Application Support" / "Google" / "Chrome"
    elif system == "Linux":
        base = home / ".config" / "google-chrome"
    elif system == "Windows":
        local_app = os.environ.get("LOCALAPPDATA", str(home / "AppData" / "Local"))
        base = Path(local_app) / "Google" / "Chrome" / "User Data"
    else:
        log.error("Unsupported OS: %s", system)
        sys.exit(1)

    return base / profile


def chrome_timestamp_to_datetime(chrome_ts: str) -> Optional[datetime]:
    """Convert a Chrome timestamp (microseconds since 1601-01-01 UTC) to datetime."""
    try:
        ts = int(chrome_ts)
        if ts == 0:
            return None
        unix_ts = (ts / 1_000_000) - CHROME_EPOCH_OFFSET
        return datetime.fromtimestamp(unix_ts, tz=timezone.utc)
    except (ValueError, OverflowError, OSError):
        return None


def is_chrome_running() -> bool:
    """Check if Chrome is currently running (best-effort)."""
    system = platform.system()
    try:
        if system == "Darwin":
            result = subprocess.run(
                ["pgrep", "-x", "Google Chrome"],
                capture_output=True, text=True, timeout=5,
            )
            return result.returncode == 0
        elif system == "Linux":
            result = subprocess.run(
                ["pgrep", "-f", "chrome"],
                capture_output=True, text=True, timeout=5,
            )
            return result.returncode == 0
        elif system == "Windows":
            result = subprocess.run(
                ["tasklist", "/FI", "IMAGENAME eq chrome.exe"],
                capture_output=True, text=True, timeout=5,
            )
            return "chrome.exe" in result.stdout.lower()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return False


def parse_time_range(time_range: str) -> Optional[timedelta]:
    """Parse a time range string into a timedelta. Returns None for 'all'."""
    if time_range == "all":
        return None

    match = re.match(r"^(\d+)([dwm])$", time_range.lower())
    if not match:
        log.error("Invalid time range: '%s'. Use Xd, Xw, Xm, or 'all'.", time_range)
        sys.exit(1)

    value = int(match.group(1))
    unit = match.group(2)

    if unit == "d":
        return timedelta(days=value)
    elif unit == "w":
        return timedelta(weeks=value)
    elif unit == "m":
        return timedelta(days=value * 30)  # approximate months

    return None


def extract_full_text(url: str) -> Optional[str]:
    """Fetch and extract full article text using trafilatura."""
    try:
        import trafilatura
    except ImportError:
        log.warning("trafilatura not installed. Skipping full-text extraction.")
        return None

    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            text = trafilatura.extract(
                downloaded,
                include_comments=False,
                include_tables=True,
                favor_precision=True,
            )
            return text
    except Exception as e:
        log.warning("Failed to extract text from %s: %s", url, e)

    return None


def read_chrome_reading_list(
    profile: str = "Default",
    time_range: Optional[timedelta] = None,
    read_status: str = "both",
    full_text: bool = False,
) -> dict:
    """Read Chrome reading list and return structured data."""

    profile_path = get_chrome_profile_path(profile)
    bookmarks_path = profile_path / "Bookmarks"

    if not bookmarks_path.exists():
        return {
            "error": f"Bookmarks file not found at {bookmarks_path}",
            "hint": "Check your Chrome profile name or ensure Chrome has been used on this machine.",
        }

    # Warn about Chrome being open
    if is_chrome_running():
        log.warning(
            "Chrome appears to be running. Reading list data may be slightly stale. "
            "For the most accurate data, close Chrome first."
        )

    # Parse bookmarks JSON
    try:
        data = json.loads(bookmarks_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        return {"error": f"Failed to parse Bookmarks file: {e}"}

    # Navigate to reading list
    roots = data.get("roots", {})
    reading_list_node = roots.get("reading_list", {})
    children = reading_list_node.get("children", [])

    if not children:
        return {
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "source": "chrome-reading-list",
            "profile": profile,
            "time_range": str(time_range) if time_range else "all",
            "total_items": 0,
            "filtered_items": 0,
            "items": [],
            "note": "Reading list is empty or the 'reading_list' key was not found in Bookmarks.",
        }

    now = datetime.now(timezone.utc)
    cutoff = (now - time_range) if time_range else None

    items = []
    skipped_by_time = 0
    skipped_by_status = 0

    for entry in children:
        if entry.get("type") != "url":
            continue

        date_added = chrome_timestamp_to_datetime(entry.get("date_added", "0"))
        date_last_used = chrome_timestamp_to_datetime(entry.get("date_last_used", "0"))

        # Time range filter
        if cutoff and date_added and date_added < cutoff:
            skipped_by_time += 1
            continue

        # Read status filter
        is_read = entry.get("read", False)
        # Some Chrome versions use numeric read_status instead of boolean read
        if "read_status" in entry:
            is_read = entry["read_status"] == 1

        entry_status = "read" if is_read else "unread"

        if read_status == "unread" and is_read:
            skipped_by_status += 1
            continue
        if read_status == "read" and not is_read:
            skipped_by_status += 1
            continue

        url = entry.get("url", "")
        from urllib.parse import urlparse
        domain = urlparse(url).netloc if url else ""

        item = {
            "title": entry.get("name", "").strip(),
            "url": url,
            "date_added": date_added.isoformat() if date_added else None,
            "date_last_used": date_last_used.isoformat() if date_last_used else None,
            "read_status": entry_status,
            "domain": domain,
            "full_text": None,
            # Feed-reader compatible fields
            "source_name": "Chrome Reading List",
            "source_url": "chrome://reading-list",
            "source_tags": [],
            "published": date_added.isoformat() if date_added else None,
            "summary": "",
        }

        # Full text extraction
        if full_text and url:
            log.info("Extracting full text: %s", url)
            item["full_text"] = extract_full_text(url)

        items.append(item)

    # Sort by date_added descending (newest first)
    items.sort(
        key=lambda x: x.get("date_added") or "0000",
        reverse=True,
    )

    return {
        "fetched_at": now.isoformat(),
        "source": "chrome-reading-list",
        "profile": profile,
        "time_range": str(time_range) if time_range else "all",
        "total_items": len(children),
        "filtered_items": len(items),
        "skipped_by_time": skipped_by_time,
        "skipped_by_status": skipped_by_status,
        "chrome_running": is_chrome_running(),
        "items": items,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Reading List Reader — Chrome Reading List ingestion for the content pipeline"
    )
    parser.add_argument(
        "--time-range", "-t",
        default="7d",
        help=(
            "Time range filter for reading list items. "
            "Examples: 1d, 3d, 7d, 2w, 1m, 3m, 6m, all. "
            "Use Xd (days), Xw (weeks), Xm (months). Default: 7d"
        ),
    )
    parser.add_argument(
        "--read-status", "-r",
        choices=["unread", "read", "both"],
        default="both",
        help="Filter by read status (default: both)",
    )
    parser.add_argument(
        "--profile", "-p",
        default="Default",
        help="Chrome profile name (default: Default)",
    )
    parser.add_argument(
        "--full-text",
        action="store_true",
        default=False,
        help="Fetch full article text via trafilatura (slower but richer)",
    )
    args = parser.parse_args()

    time_range = parse_time_range(args.time_range)

    result = read_chrome_reading_list(
        profile=args.profile,
        time_range=time_range,
        read_status=args.read_status,
        full_text=args.full_text,
    )

    if "error" in result:
        log.error(result["error"])
        if "hint" in result:
            log.info(result["hint"])
        json.dump(result, sys.stdout, indent=2)
        sys.exit(1)

    log.info(
        "Found %d items (filtered from %d total, skipped %d by time, %d by status)",
        result["filtered_items"],
        result["total_items"],
        result.get("skipped_by_time", 0),
        result.get("skipped_by_status", 0),
    )

    json.dump(result, sys.stdout, indent=2, ensure_ascii=False, default=str)


if __name__ == "__main__":
    main()
