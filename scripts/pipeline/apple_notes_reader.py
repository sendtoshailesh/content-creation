#!/usr/bin/env python3
"""
Apple Notes Reader — Apple Notes ingestion for the content pipeline.

Reads the Apple Notes SQLite database (NoteStore.sqlite), extracts notes
with title, snippet, body text, folder, and timestamps. Filters by time
range and folder name.

Output: JSON to stdout (compatible with feed_reader.py / reading_list_reader.py schema).

Usage:
  python scripts/pipeline/apple_notes_reader.py
  python scripts/pipeline/apple_notes_reader.py --time-range 7d
  python scripts/pipeline/apple_notes_reader.py --time-range 1m --folder "AI tools"
  python scripts/pipeline/apple_notes_reader.py --time-range 2w --list-folders

Time ranges: 1d, 3d, 7d, 2w, 3w, 1m, 3m, 6m, all, or Xd/Xw/Xm for custom.

No external dependencies — uses only Python stdlib (sqlite3, zlib, re).
"""

import argparse
import json
import logging
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import zlib
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger(__name__)

# Apple Core Data timestamps are seconds since 2001-01-01 00:00:00 UTC
APPLE_EPOCH_OFFSET = 978307200  # seconds between 1970-01-01 and 2001-01-01


def get_notes_db_path() -> Path:
    """Return the Apple Notes SQLite database path."""
    return (
        Path.home()
        / "Library"
        / "Group Containers"
        / "group.com.apple.notes"
        / "NoteStore.sqlite"
    )


def apple_timestamp_to_datetime(apple_ts: Optional[float]) -> Optional[datetime]:
    """Convert an Apple Core Data timestamp to datetime."""
    if apple_ts is None or apple_ts == 0:
        return None
    try:
        unix_ts = apple_ts + APPLE_EPOCH_OFFSET
        return datetime.fromtimestamp(unix_ts, tz=timezone.utc)
    except (ValueError, OverflowError, OSError):
        return None


def is_notes_running() -> bool:
    """Check if the Notes app is currently running."""
    try:
        result = subprocess.run(
            ["pgrep", "-x", "Notes"],
            capture_output=True, text=True, timeout=5,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def extract_text_from_note_data(data: bytes) -> str:
    """Extract readable text from Apple Notes ZDATA blob.

    The blob is gzip-compressed protobuf. We decompress it and extract
    readable text strings rather than fully parsing protobuf (which would
    require the undocumented schema).
    """
    if not data:
        return ""

    try:
        decompressed = zlib.decompress(data, 16 + zlib.MAX_WBITS)
    except zlib.error:
        decompressed = data

    # Extract readable text from the protobuf bytes
    text = decompressed.decode("utf-8", errors="ignore")
    # Filter to printable chars and newlines
    readable = re.sub(r"[^\x20-\x7E\n\t]", " ", text)
    # Collapse whitespace
    readable = re.sub(r"[ \t]{2,}", " ", readable)
    readable = re.sub(r"\n{3,}", "\n\n", readable)
    return readable.strip()


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
        return timedelta(days=value * 30)

    return None


def copy_db_for_safe_read(db_path: Path) -> Path:
    """Copy the database to a temp location for safe concurrent reading.

    Apple Notes may have the DB locked. Copying avoids lock conflicts.
    """
    tmp_dir = tempfile.mkdtemp(prefix="apple_notes_")
    tmp_db = Path(tmp_dir) / "NoteStore.sqlite"
    shutil.copy2(db_path, tmp_db)

    # Also copy WAL and SHM files if they exist for consistency
    for suffix in ("-wal", "-shm"):
        src = db_path.parent / (db_path.name + suffix)
        if src.exists():
            shutil.copy2(src, tmp_db.parent / (tmp_db.name + suffix))

    return tmp_db


def list_folders(db_path: Path) -> list[dict]:
    """List all folders in Apple Notes."""
    tmp_db = copy_db_for_safe_read(db_path)
    try:
        conn = sqlite3.connect(str(tmp_db), timeout=5)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("""
            SELECT Z_PK, ZTITLE2 as name, ZFOLDERTYPE as folder_type
            FROM ZICCLOUDSYNCINGOBJECT
            WHERE ZTITLE2 IS NOT NULL
              AND ZMARKEDFORDELETION != 1
              AND ZFOLDERTYPE IS NOT NULL
            ORDER BY ZTITLE2
        """)

        folders = []
        for row in cur.fetchall():
            # Count notes in this folder
            cur2 = conn.cursor()
            cur2.execute(
                "SELECT COUNT(*) FROM ZICCLOUDSYNCINGOBJECT WHERE ZFOLDER = ? AND ZTITLE1 IS NOT NULL AND ZMARKEDFORDELETION != 1",
                (row["Z_PK"],),
            )
            count = cur2.fetchone()[0]
            folders.append({
                "name": row["name"],
                "note_count": count,
                "type": "smart" if row["folder_type"] == 2 else "regular",
            })

        conn.close()
        return folders
    finally:
        shutil.rmtree(tmp_db.parent, ignore_errors=True)


def read_apple_notes(
    time_range: Optional[timedelta] = None,
    folder_filter: Optional[str] = None,
    include_body: bool = True,
) -> dict:
    """Read Apple Notes and return structured data."""

    db_path = get_notes_db_path()

    if not db_path.exists():
        return {
            "error": f"Apple Notes database not found at {db_path}",
            "hint": "Ensure Apple Notes has been used on this machine.",
        }

    notes_running = is_notes_running()
    if notes_running:
        log.info("Notes app is running. Using a copy of the database for safe reading.")

    # Copy DB to avoid lock issues
    tmp_db = copy_db_for_safe_read(db_path)

    try:
        conn = sqlite3.connect(str(tmp_db), timeout=5)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        now = datetime.now(timezone.utc)
        cutoff_apple = None
        if time_range:
            cutoff_dt = now - time_range
            cutoff_apple = cutoff_dt.timestamp() - APPLE_EPOCH_OFFSET

        # Build query
        query = """
            SELECT
                n.Z_PK as pk,
                n.ZTITLE1 as title,
                n.ZSNIPPET as snippet,
                n.ZCREATIONDATE3 as created,
                n.ZMODIFICATIONDATE1 as modified,
                n.ZFOLDER as folder_pk,
                f.ZTITLE2 as folder_name
        """

        if include_body:
            query += ", nd.ZDATA as body_data"

        query += """
            FROM ZICCLOUDSYNCINGOBJECT n
            LEFT JOIN ZICCLOUDSYNCINGOBJECT f ON n.ZFOLDER = f.Z_PK
        """

        if include_body:
            query += " LEFT JOIN ZICNOTEDATA nd ON nd.ZNOTE = n.Z_PK"

        query += """
            WHERE n.ZTITLE1 IS NOT NULL
              AND n.ZMARKEDFORDELETION != 1
        """

        params = []

        if cutoff_apple is not None:
            query += " AND n.ZMODIFICATIONDATE1 >= ?"
            params.append(cutoff_apple)

        if folder_filter:
            query += " AND f.ZTITLE2 = ?"
            params.append(folder_filter)

        query += " ORDER BY n.ZMODIFICATIONDATE1 DESC"

        cur.execute(query, params)
        rows = cur.fetchall()

        # Get total count (unfiltered)
        cur.execute(
            "SELECT COUNT(*) FROM ZICCLOUDSYNCINGOBJECT WHERE ZTITLE1 IS NOT NULL AND ZMARKEDFORDELETION != 1"
        )
        total_count = cur.fetchone()[0]

        items = []
        for row in rows:
            created_dt = apple_timestamp_to_datetime(row["created"])
            modified_dt = apple_timestamp_to_datetime(row["modified"])

            body_text = ""
            if include_body and row["body_data"]:
                body_text = extract_text_from_note_data(row["body_data"])

            # Extract URLs from body text
            urls = re.findall(r"https?://[^\s<>\"')\]]+", body_text) if body_text else []

            item = {
                "title": (row["title"] or "").strip(),
                "snippet": (row["snippet"] or "").strip(),
                "body_text": body_text,
                "folder": row["folder_name"] or "Notes",
                "date_created": created_dt.isoformat() if created_dt else None,
                "date_modified": modified_dt.isoformat() if modified_dt else None,
                "urls_in_note": urls[:10],  # Cap extracted URLs
                # Feed-reader compatible fields
                "source_name": f"Apple Notes ({row['folder_name'] or 'Notes'})",
                "source_url": "apple-notes://",
                "source_tags": [],
                "url": urls[0] if urls else "",
                "published": created_dt.isoformat() if created_dt else None,
                "summary": (row["snippet"] or "").strip(),
                "full_text": body_text,
            }
            items.append(item)

        conn.close()

        return {
            "fetched_at": now.isoformat(),
            "source": "apple-notes",
            "time_range": str(time_range) if time_range else "all",
            "folder_filter": folder_filter,
            "total_notes": total_count,
            "filtered_notes": len(items),
            "notes_app_running": notes_running,
            "items": items,
        }

    except sqlite3.OperationalError as e:
        return {
            "error": f"Failed to read Apple Notes database: {e}",
            "hint": "The database may be locked. Try closing the Notes app.",
        }
    finally:
        shutil.rmtree(tmp_db.parent, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(
        description="Apple Notes Reader — Apple Notes ingestion for the content pipeline"
    )
    parser.add_argument(
        "--time-range", "-t",
        default="7d",
        help=(
            "Time range filter for notes (by modification date). "
            "Examples: 1d, 3d, 7d, 2w, 1m, 3m, 6m, all. "
            "Use Xd (days), Xw (weeks), Xm (months). Default: 7d"
        ),
    )
    parser.add_argument(
        "--folder", "-f",
        default=None,
        help="Filter to a specific folder name (exact match). Use --list-folders to see options.",
    )
    parser.add_argument(
        "--list-folders",
        action="store_true",
        default=False,
        help="List all folders and their note counts, then exit.",
    )
    parser.add_argument(
        "--no-body",
        action="store_true",
        default=False,
        help="Skip extracting note body text (faster, title/snippet only).",
    )
    args = parser.parse_args()

    db_path = get_notes_db_path()

    # List folders mode
    if args.list_folders:
        if not db_path.exists():
            log.error("Apple Notes database not found at %s", db_path)
            sys.exit(1)

        folders = list_folders(db_path)
        output = {"folders": folders}
        json.dump(output, sys.stdout, indent=2)
        return

    time_range = parse_time_range(args.time_range)

    result = read_apple_notes(
        time_range=time_range,
        folder_filter=args.folder,
        include_body=not args.no_body,
    )

    if "error" in result:
        log.error(result["error"])
        if "hint" in result:
            log.info(result["hint"])
        json.dump(result, sys.stdout, indent=2)
        sys.exit(1)

    log.info(
        "Found %d notes (from %d total, time range: %s%s)",
        result["filtered_notes"],
        result["total_notes"],
        args.time_range,
        f", folder: {args.folder}" if args.folder else "",
    )

    json.dump(result, sys.stdout, indent=2, ensure_ascii=False, default=str)


if __name__ == "__main__":
    main()
