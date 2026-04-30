#!/usr/bin/env python3
"""
Bing Web Search API v7 — batch search CLI for the content pipeline.

Usage:
  python scripts/bing-search.py --query "PostgreSQL performance"
  python scripts/bing-search.py --queries queries.json
  python scripts/bing-search.py --query "AI benchmarks 2026" --count 5 --freshness Month

Output: JSON array of results grouped by query, written to stdout.

Requires:
  BING_SEARCH_API_KEY environment variable (or .env file in project root).
"""

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.parse import quote_plus

try:
    import requests
except ImportError:
    sys.exit("ERROR: 'requests' package required. Install with: pip install requests")

from typing import Optional


BING_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"
DEFAULT_COUNT = 10
DEFAULT_MKT = "en-US"


def load_api_key() -> Optional[str]:
    """Load Bing API key from env var or .env file."""
    key = os.environ.get("BING_SEARCH_API_KEY")
    if key:
        return key

    # Walk up from script location to find .env
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k.strip() == "BING_SEARCH_API_KEY":
                return v.strip().strip("\"'")
    return None


def search_bing(
    query: str,
    api_key: str,
    count: int = DEFAULT_COUNT,
    freshness: Optional[str] = None,
    mkt: str = DEFAULT_MKT,
) -> dict:
    """Execute a single Bing Web Search query and return structured results."""
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params: dict = {
        "q": query,
        "count": count,
        "mkt": mkt,
        "textFormat": "Raw",
        "safeSearch": "Moderate",
    }
    if freshness:
        params["freshness"] = freshness

    resp = requests.get(BING_ENDPOINT, headers=headers, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    results = []
    for page in data.get("webPages", {}).get("value", []):
        results.append(
            {
                "title": page.get("name", ""),
                "url": page.get("url", ""),
                "snippet": page.get("snippet", ""),
                "datePublished": page.get("dateLastCrawled", ""),
                "provider": page.get("displayUrl", ""),
            }
        )
    return {"query": query, "resultCount": len(results), "results": results}


def deduplicate(grouped_results: list) -> list:
    """Remove duplicate URLs across all query result groups."""
    seen_urls: set = set()
    for group in grouped_results:
        unique = []
        for r in group["results"]:
            url_lower = r["url"].lower().rstrip("/")
            if url_lower not in seen_urls:
                seen_urls.add(url_lower)
                unique.append(r)
        group["results"] = unique
        group["resultCount"] = len(unique)
    return grouped_results


def main():
    parser = argparse.ArgumentParser(
        description="Bing Web Search API v7 — batch search CLI"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--query", "-q", help="Single search query string")
    group.add_argument(
        "--queries",
        help="Path to JSON file with array of query objects: "
        '[{"query": "...", "category": "...", "count": 10}]',
    )
    parser.add_argument(
        "--count", "-c", type=int, default=DEFAULT_COUNT, help="Results per query"
    )
    parser.add_argument(
        "--freshness",
        "-f",
        choices=["Day", "Week", "Month"],
        help="Freshness filter",
    )
    parser.add_argument(
        "--mkt", default=DEFAULT_MKT, help="Market code (default: en-US)"
    )
    args = parser.parse_args()

    api_key = load_api_key()
    if not api_key:
        error = {
            "error": "BING_SEARCH_API_KEY not found",
            "message": "Set BING_SEARCH_API_KEY environment variable or add it to .env file. "
            "Create a Bing Search resource in Azure Portal: "
            "https://portal.azure.com/#create/Microsoft.BingSearch",
            "fallback": "Use Copilot's built-in web tool instead",
        }
        json.dump(error, sys.stdout, indent=2)
        sys.exit(1)

    # Build query list
    query_list: list = []
    if args.query:
        query_list.append(
            {
                "query": args.query,
                "category": "general",
                "count": args.count,
            }
        )
    else:
        queries_path = Path(args.queries)
        if not queries_path.exists():
            sys.exit(f"ERROR: Queries file not found: {args.queries}")
        query_list = json.loads(queries_path.read_text())

    # Execute searches
    all_results: list = []
    errors: list = []
    for q in query_list:
        query_str = q.get("query", "")
        category = q.get("category", "general")
        count = q.get("count", args.count)
        freshness = q.get("freshness", args.freshness)

        try:
            result = search_bing(
                query=query_str,
                api_key=api_key,
                count=count,
                freshness=freshness,
                mkt=args.mkt,
            )
            result["category"] = category
            all_results.append(result)
        except requests.exceptions.HTTPError as e:
            errors.append(
                {
                    "query": query_str,
                    "category": category,
                    "error": str(e),
                    "status_code": e.response.status_code if e.response else None,
                }
            )
        except requests.exceptions.RequestException as e:
            errors.append(
                {"query": query_str, "category": category, "error": str(e)}
            )

    # Deduplicate across queries
    all_results = deduplicate(all_results)

    output = {"results": all_results}
    if errors:
        output["errors"] = errors

    json.dump(output, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
