#!/usr/bin/env python3
"""Harvest Chrome + Edge browsing history and saved bookmarks into a tiered,
topic-filtered grounding digest for the content pipeline.

Why: the Source-of-Truth Precedence rule requires content to lead with first-party
Microsoft/GitHub material the author actually uses. This script surfaces the
author's real navigation so writers ground in genuine sources instead of generic
web search. Microsoft and GitHub domains are promoted to tiers 2-3; relevant
public domains become tier-4 corroboration.

Read-only: history/bookmarks databases are copied to a temp dir before querying
(the live files are locked while the browser runs). Nothing is written back to any
browser profile. A privacy denylist drops obviously sensitive domains (mail, auth,
banking, etc.) so private browsing never leaks into published content.

Usage:
    python3 scripts/pipeline/harvest_browsing.py "topic kw1" "kw2" ...
    python3 scripts/pipeline/harvest_browsing.py --days 180 --top 40 ai agent copilot

Output: content/browsing-signals.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# ---- Source classification -------------------------------------------------
MICROSOFT_DOMAINS = (
    "microsoft.com", "learn.microsoft.com", "docs.microsoft.com", "azure.com",
    "ai.azure.com", "azure.microsoft.com", "devblogs.microsoft.com",
    "techcommunity.microsoft.com", "microsoft.github.io", "msdn.com",
    "research.microsoft.com", "microsoftresearch", "visualstudio.com",
    "office.com", "windows.com", "msrc.microsoft.com",
)
GITHUB_DOMAINS = (
    "github.com", "github.blog", "github.io", "githubnext.com",
    "githubuniverse.com", "docs.github.com", "githubusercontent.com",
    "copilot.github.com", "resources.github.com",
)
# Domains/paths we never surface, even if topic-relevant. Two reasons:
# (1) privacy — auth-gated, personal, or financial; (2) not citable — internal
# corporate portals and private workspaces are navigation noise, not references.
DENY_SUBSTRINGS = (
    # privacy / financial / personal
    "mail.google", "accounts.google", "outlook.", "login.", "signin", "auth.",
    "bank", "paypal", "venmo", "chase.", "wellsfargo", "amex",
    "localhost", "127.0.0.1", "0.0.0.0", "calendar.google", "drive.google",
    "whatsapp", "messenger", "instagram.com/direct", "icloud.com",
    "health", "medical", "patient", "passport", "irs.gov", "tax",
    # internal / auth-gated corporate + private workspaces (not citable)
    "sharepoint.com", "-my.sharepoint", "dev.azure.com", "expense.",
    "careerhub", "msconnect", "repos.opensource.microsoft", ".corp.microsoft.com",
    "gsamportal", "rightcrowd", "go.microsoft.com/fwlink", "portal.azure.com",
    "ai.azure.com/nextgen", "/settings/", "/saml/", "myaccount", "admin.",
    "office.com", "microsoftapc", "microsofteur", "teams.microsoft.com",
    "myapps.microsoft", "myaccess", "/account", "viva.",
    # product app shells / portals (use the docs/blog URL, not the app)
    "ai.azure.com/login", "ai.azure.com/home", "ai.azure.com/?", "ai.azure.com/",
    "getconnected", "engage.cloud", "/forbidden", "demos.microsoft.com",
    "sre.azure.com", "techconnect.microsoft.com",
)
DEFAULT_KEYWORDS = (
    "ai", "agent", "copilot", "foundry", "azure", "github", "llm", "model",
    "prompt", "swe", "coding", "developer", "rag", "eval", "mcp", "openai",
    "anthropic", "claude", "gpt", "context", "harness", "loop", "devops",
)

CHROME_EPOCH_OFFSET = 11644473600  # seconds between 1601-01-01 and 1970-01-01

PROFILES = [
    ("Chrome", "Google/Chrome/Default"),
    ("Chrome", "Google/Chrome/Profile 1"),
    ("Edge", "Microsoft Edge/Default"),
    ("Edge", "Microsoft Edge/Profile 1"),
]


def chrome_time_to_dt(raw: int) -> datetime | None:
    if not raw:
        return None
    try:
        return datetime.fromtimestamp(raw / 1_000_000 - CHROME_EPOCH_OFFSET, tz=timezone.utc)
    except (OverflowError, OSError, ValueError):
        return None


def classify_tier(url: str) -> str | None:
    u = url.lower()
    if any(d in u for d in DENY_SUBSTRINGS):
        return None
    if any(d in u for d in MICROSOFT_DOMAINS):
        return "T2"
    if any(d in u for d in GITHUB_DOMAINS):
        return "T3"
    return "T4"


def is_relevant(url: str, title: str, keywords: list[str]) -> bool:
    blob = f"{url} {title}".lower()
    return any(kw in blob for kw in keywords)


def host_of(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url)
    return m.group(1).lower() if m else ""


# ---- History ---------------------------------------------------------------
def read_history(db_path: Path, browser: str, days: int, keywords: list[str]) -> list[dict]:
    rows: list[dict] = []
    cutoff = (datetime.now(tz=timezone.utc).timestamp() + CHROME_EPOCH_OFFSET) * 1_000_000
    cutoff_min = cutoff - days * 86400 * 1_000_000
    tmp = Path(tempfile.mkdtemp()) / "h.db"
    try:
        shutil.copy2(db_path, tmp)
        con = sqlite3.connect(f"file:{tmp}?mode=ro", uri=True)
        cur = con.execute(
            "SELECT url, title, visit_count, typed_count, last_visit_time "
            "FROM urls WHERE hidden=0 AND last_visit_time>=? ORDER BY visit_count DESC",
            (cutoff_min,),
        )
        for url, title, visits, typed, last in cur.fetchall():
            if not url or not url.startswith("http"):
                continue
            tier = classify_tier(url)
            if tier is None:
                continue
            title = title or ""
            relevant = is_relevant(url, title, keywords)
            # First-party kept if relevant OR frequently used; public must be relevant.
            if tier == "T4" and not relevant:
                continue
            if tier in ("T2", "T3") and not relevant and (visits or 0) < 3:
                continue
            dt = chrome_time_to_dt(last)
            rows.append({
                "url": url, "title": title.strip(), "tier": tier,
                "visits": visits or 0, "typed": typed or 0,
                "last": dt, "browser": browser, "source": "history",
            })
        con.close()
    except sqlite3.Error as exc:
        print(f"  warn: could not read {browser} history ({exc})", file=sys.stderr)
    finally:
        shutil.rmtree(tmp.parent, ignore_errors=True)
    return rows


# ---- Bookmarks (the "saved for later / reading list" signal) ---------------
def walk_bookmarks(node: dict, out: list[dict], browser: str, keywords: list[str]) -> None:
    if not isinstance(node, dict):
        return
    if node.get("type") == "url":
        url = node.get("url", "")
        title = node.get("name", "") or ""
        if url.startswith("http"):
            tier = classify_tier(url)
            if tier is not None and (tier in ("T2", "T3") or is_relevant(url, title, keywords)):
                added = node.get("date_added")
                dt = chrome_time_to_dt(int(added)) if added and str(added).isdigit() else None
                out.append({
                    "url": url, "title": title.strip(), "tier": tier,
                    "visits": 0, "typed": 0, "last": dt,
                    "browser": browser, "source": "bookmark",
                })
    for child in node.get("children", []) or []:
        walk_bookmarks(child, out, browser, keywords)


def read_bookmarks(path: Path, browser: str, keywords: list[str]) -> list[dict]:
    out: list[dict] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        for root in (data.get("roots") or {}).values():
            walk_bookmarks(root, out, browser, keywords)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"  warn: could not read {browser} bookmarks ({exc})", file=sys.stderr)
    return out


# ---- Aggregation -----------------------------------------------------------
def score(row: dict) -> float:
    s = row["visits"] * 2 + row["typed"] * 3
    if row["source"] == "bookmark":
        s += 4  # deliberately saved
    if row["last"]:
        age_days = (datetime.now(tz=timezone.utc) - row["last"]).days
        if age_days <= 30:
            s += 10
        elif age_days <= 90:
            s += 5
    return s


def dedupe(rows: list[dict]) -> list[dict]:
    best: dict[str, dict] = {}
    for r in rows:
        key = r["url"].split("#")[0].rstrip("/").lower()
        if key not in best or score(r) > score(best[key]):
            # merge visit counts across duplicates/browsers
            if key in best:
                r["visits"] = max(r["visits"], best[key]["visits"])
            best[key] = r
    return list(best.values())


def fmt_date(dt: datetime | None) -> str:
    return dt.strftime("%Y-%m-%d") if dt else "-"


def render(rows: list[dict], top: int, keywords: list[str]) -> str:
    tiers = {"T2": [], "T3": [], "T4": []}
    for r in rows:
        tiers[r["tier"]].append(r)
    for k in tiers:
        tiers[k].sort(key=score, reverse=True)

    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Browsing Signals (auto-generated)",
        "",
        f"Generated: {now}  ",
        f"Keywords: {', '.join(keywords)}  ",
        "Source: Chrome + Edge history and saved bookmarks (read-only copy).  ",
        "",
        "These are sources the author has actually visited or saved. Per the "
        "Source-of-Truth Precedence rule, lead with Tier 2 (Microsoft) and Tier 3 "
        "(GitHub) first-party signals; use Tier 4 (public) as corroboration. "
        "**Verify and fetch any URL before citing it** — presence here is a "
        "navigation signal, not a fact-check.",
        "",
    ]
    titles = {
        "T2": "Tier 2 — Microsoft first-party (lead with these)",
        "T3": "Tier 3 — GitHub first-party (lead with these)",
        "T4": "Tier 4 — Public / third-party (corroboration only)",
    }
    for k in ("T2", "T3", "T4"):
        sel = tiers[k][:top]
        lines.append(f"## {titles[k]}")
        lines.append("")
        if not sel:
            lines.append("_No topic-relevant entries found._")
            lines.append("")
            continue
        lines.append("| Title | URL | Visits | Last | Via |")
        lines.append("|---|---|---|---|---|")
        for r in sel:
            t = (r["title"] or host_of(r["url"]))[:70].replace("|", "\\|")
            url = r["url"][:90].replace("|", "\\|")
            via = f"{r['browser']}/{r['source']}"
            lines.append(f"| {t} | {url} | {r['visits']} | {fmt_date(r['last'])} | {via} |")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Harvest Chrome/Edge browsing into a tiered grounding digest.")
    ap.add_argument("keywords", nargs="*", help="Topic keywords to filter on (default: AI/dev set).")
    ap.add_argument("--days", type=int, default=365, help="History lookback window in days (default 365).")
    ap.add_argument("--top", type=int, default=40, help="Max entries per tier (default 40).")
    ap.add_argument("--out", default=None, help="Output path (default content/browsing-signals.md).")
    args = ap.parse_args()

    keywords = [k.lower() for k in args.keywords] or list(DEFAULT_KEYWORDS)
    base = Path.home() / "Library" / "Application Support"
    repo = Path(__file__).resolve().parents[2]
    out_path = Path(args.out) if args.out else repo / "content" / "browsing-signals.md"

    all_rows: list[dict] = []
    found_any = False
    for browser, rel in PROFILES:
        prof = base / rel
        hist = prof / "History"
        if hist.exists():
            found_any = True
            print(f"reading {browser} history: {rel}")
            all_rows += read_history(hist, browser, args.days, keywords)
        bm = prof / "Bookmarks"
        if bm.exists():
            print(f"reading {browser} bookmarks: {rel}")
            all_rows += read_bookmarks(bm, browser, keywords)

    if not found_any:
        print("No Chrome or Edge profiles found — skipping browsing harvest.", file=sys.stderr)
        return 0

    rows = dedupe(all_rows)
    md = render(rows, args.top, keywords)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")

    counts = {"T2": 0, "T3": 0, "T4": 0}
    for r in rows:
        counts[r["tier"]] += 1
    print(f"\nWrote {out_path}")
    print(f"  Tier 2 Microsoft: {counts['T2']}  |  Tier 3 GitHub: {counts['T3']}  |  Tier 4 public: {counts['T4']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
