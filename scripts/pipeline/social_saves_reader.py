#!/usr/bin/env python3
"""
Social Saves Reader — authenticated "save for later" ingestion for the content pipeline.

Reads YOUR OWN saved items from social platforms using YOUR OWN logged-in browser
session (Playwright persistent context). These saves are high-intent idea signals —
you already found each item interesting enough to bookmark.

Supported platforms:
  - linkedin : your Saved posts/articles      (https://www.linkedin.com/my-items/saved-posts/)
  - twitter  : your X/Twitter Bookmarks or Likes (https://x.com/i/bookmarks)
  - medium   : your Medium reading list / queue (https://medium.com/me/list/queue)
  - reddit   : your saved posts/comments       (https://old.reddit.com/user/<handle>/saved/)
  - github   : your starred repositories       (https://github.com/<handle>?tab=stars)
  - youtube  : your Watch Later queue          (https://www.youtube.com/playlist?list=WL)

Output: JSON to stdout (same item schema as feed_reader.py / reading_list_reader.py),
so the downstream curator agent can classify, cluster, and score uniformly.

Auth model (read-only, personal use):
  This script never automates engagement (no liking, posting, following). It only
  *reads* items you already saved, through a browser profile you log into once. The
  session is stored in a dedicated Playwright user-data dir (NOT your real Chrome
  profile), so it stays isolated and you can delete it any time.

First-time setup (one login per platform, persists afterwards):
  python scripts/pipeline/social_saves_reader.py --platform linkedin --login
  python scripts/pipeline/social_saves_reader.py --platform twitter  --login
  python scripts/pipeline/social_saves_reader.py --platform medium   --login
  python scripts/pipeline/social_saves_reader.py --platform reddit   --login
  python scripts/pipeline/social_saves_reader.py --platform youtube  --login
  # GitHub stars are public — no login needed, but --login lets you see private stars.

Normal use (headless, reuses the saved session):
  python scripts/pipeline/social_saves_reader.py --platform linkedin --limit 40 --full-text
  python scripts/pipeline/social_saves_reader.py --platform twitter --list bookmarks --limit 50
  python scripts/pipeline/social_saves_reader.py --platform twitter --list likes --handle myhandle
  python scripts/pipeline/social_saves_reader.py --platform medium --limit 30
  python scripts/pipeline/social_saves_reader.py --platform reddit --handle myhandle --limit 50
  python scripts/pipeline/social_saves_reader.py --platform github --handle myhandle --limit 40
  python scripts/pipeline/social_saves_reader.py --platform youtube --limit 40

Requires: playwright (`pip install playwright && python -m playwright install chromium`)
Optional: trafilatura (for --full-text)
"""

import argparse
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Platform configuration
# ---------------------------------------------------------------------------

PLATFORMS = {
    "linkedin": {
        "name": "LinkedIn Saved",
        "saved_url": "https://www.linkedin.com/my-items/saved-posts/",
        "login_url": "https://www.linkedin.com/login",
        "logged_in_signal": "linkedin.com/feed",
        "source_url": "https://www.linkedin.com/my-items/saved-posts/",
    },
    "twitter": {
        "name": "X/Twitter",
        "saved_url": "https://x.com/i/bookmarks",
        "likes_url": "https://x.com/{handle}/likes",
        "login_url": "https://x.com/login",
        "logged_in_signal": "x.com/home",
        "source_url": "https://x.com/i/bookmarks",
    },
    "medium": {
        "name": "Medium Reading List",
        "saved_url": "https://medium.com/me/list/queue",
        "login_url": "https://medium.com/m/signin",
        "logged_in_signal": "medium.com",
        "source_url": "https://medium.com/me/list/queue",
    },
    "reddit": {
        "name": "Reddit Saved",
        # old.reddit.com has stable server-rendered HTML and shares the .reddit.com
        # session cookie set during login on www.reddit.com. limit=100 = one page.
        "saved_url": "https://old.reddit.com/user/{handle}/saved/?limit=100",
        "login_url": "https://www.reddit.com/login/",
        "logged_in_signal": "reddit.com",
        "source_url": "https://www.reddit.com/user/{handle}/saved/",
        "requires_handle": True,
    },
    "github": {
        "name": "GitHub Stars",
        # Starred repos are public; pagination is via &page=N (30 per page).
        "saved_url": "https://github.com/{handle}?tab=stars",
        "login_url": "https://github.com/login",
        "logged_in_signal": "github.com",
        "source_url": "https://github.com/{handle}?tab=stars",
        "requires_handle": True,
    },
    "youtube": {
        "name": "YouTube Watch Later",
        # The Watch Later playlist (list=WL) is private to your account; it loads
        # videos lazily as ytd-playlist-video-renderer rows via infinite scroll.
        "saved_url": "https://www.youtube.com/playlist?list=WL",
        "login_url": "https://accounts.google.com/ServiceLogin?service=youtube",
        "logged_in_signal": "youtube.com",
        "source_url": "https://www.youtube.com/playlist?list=WL",
    },
}

DEFAULT_USER_DATA_DIR = Path.home() / ".content-pipeline" / "pw-social-profile"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def domain_of(url: str) -> str:
    try:
        return urlparse(url).netloc
    except Exception:
        return ""


def extract_full_text(url: str) -> Optional[str]:
    """Fetch and extract full article text using trafilatura (best-effort)."""
    try:
        import trafilatura
    except ImportError:
        log.warning("trafilatura not installed; skipping full-text extraction.")
        return None
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            return trafilatura.extract(
                downloaded,
                include_comments=False,
                include_tables=True,
                favor_precision=True,
            )
    except Exception as e:  # noqa: BLE001 - best-effort enrichment
        log.warning("Full-text extraction failed for %s: %s", url, e)
    return None


def make_item(
    *,
    title: str,
    url: str,
    platform_name: str,
    source_url: str,
    author: str = "",
    post_text: str = "",
    saved_rank: Optional[int] = None,
) -> dict:
    """Build a feed-reader-compatible item dict."""
    title = (title or "").strip()
    post_text = (post_text or "").strip()
    if not title and post_text:
        title = post_text[:120]
    return {
        "title": title[:200],
        "url": url,
        "date_added": None,          # platforms rarely expose a reliable save date
        "date_last_used": None,
        "read_status": "unknown",
        "domain": domain_of(url),
        "author": author.strip(),
        "post_text": post_text,
        "saved_rank": saved_rank,    # 1 = top of the saved list (most recent save)
        "full_text": None,
        # Feed-reader compatible fields
        "source_name": platform_name,
        "source_url": source_url,
        "source_tags": [],
        "published": None,
        "summary": post_text[:500],
    }


def scroll_to_load(page, target: int, max_scrolls: int = 40, pause_ms: int = 1200) -> None:
    """Scroll the page until item growth stalls or we have enough on-screen height."""
    last_height = 0
    stagnant = 0
    for _ in range(max_scrolls):
        page.mouse.wheel(0, 20000)
        page.wait_for_timeout(pause_ms)
        height = page.evaluate("document.body.scrollHeight")
        if height <= last_height:
            stagnant += 1
            if stagnant >= 3:
                break
        else:
            stagnant = 0
        last_height = height
        # Heuristic: enough scrolling for the requested item count.
        if height > target * 600:
            break


# ---------------------------------------------------------------------------
# Per-platform extractors (defensive: degrade gracefully if selectors drift)
# ---------------------------------------------------------------------------

def scrape_linkedin(page, limit: int) -> list:
    scroll_to_load(page, limit)
    js = r"""
    () => {
      const out = [];
      const seen = new Set();
      const anchors = Array.from(document.querySelectorAll('a[href]'));
      for (const a of anchors) {
        const href = a.href || '';
        if (!/linkedin\.com\/(posts|pulse)\//.test(href)) continue;
        const clean = href.split('?')[0];
        if (seen.has(clean)) continue;
        seen.add(clean);
        // Walk up to a card container to grab post text + author.
        let card = a.closest('li, article, div.feed-shared-update-v2, div.entity-result');
        let text = card ? (card.innerText || '') : (a.innerText || '');
        text = text.replace(/\s+/g, ' ').trim();
        let author = '';
        if (card) {
          const nameEl = card.querySelector('span.entity-result__title-text, span.feed-shared-actor__name, a span[aria-hidden="true"]');
          if (nameEl) author = (nameEl.innerText || '').replace(/\s+/g, ' ').trim();
        }
        out.push({ url: clean, text: text.slice(0, 1200), author });
      }
      return out;
    }
    """
    raw = page.evaluate(js)
    items = []
    for i, r in enumerate(raw[:limit], start=1):
        items.append(make_item(
            title=r.get("text", "")[:120],
            url=r["url"],
            platform_name=PLATFORMS["linkedin"]["name"],
            source_url=PLATFORMS["linkedin"]["source_url"],
            author=r.get("author", ""),
            post_text=r.get("text", ""),
            saved_rank=i,
        ))
    return items


def scrape_twitter(page, limit: int) -> list:
    scroll_to_load(page, limit)
    js = r"""
    () => {
      const out = [];
      const seen = new Set();
      const tweets = Array.from(document.querySelectorAll('article[data-testid="tweet"]'));
      for (const t of tweets) {
        const permalink = t.querySelector('a[href*="/status/"]');
        if (!permalink) continue;
        const url = permalink.href.split('?')[0];
        if (seen.has(url)) continue;
        seen.add(url);
        const textEl = t.querySelector('div[data-testid="tweetText"]');
        const text = textEl ? (textEl.innerText || '').replace(/\s+/g, ' ').trim() : '';
        const authorEl = t.querySelector('div[data-testid="User-Name"]');
        const author = authorEl ? (authorEl.innerText || '').split('\n')[0].trim() : '';
        // Prefer an outbound link inside the tweet if present.
        let outbound = '';
        for (const a of t.querySelectorAll('a[href^="http"]')) {
          if (!/(twitter|x)\.com/.test(a.href)) { outbound = a.href.split('?')[0]; break; }
        }
        out.push({ url: outbound || url, status_url: url, text: text.slice(0, 600), author });
      }
      return out;
    }
    """
    raw = page.evaluate(js)
    items = []
    for i, r in enumerate(raw[:limit], start=1):
        items.append(make_item(
            title=r.get("text", "")[:120],
            url=r["url"],
            platform_name=PLATFORMS["twitter"]["name"],
            source_url=r.get("status_url", PLATFORMS["twitter"]["source_url"]),
            author=r.get("author", ""),
            post_text=r.get("text", ""),
            saved_rank=i,
        ))
    return items


def scrape_medium(page, limit: int) -> list:
    scroll_to_load(page, limit)
    js = r"""
    () => {
      const out = [];
      const seen = new Set();
      const articles = Array.from(document.querySelectorAll('article'));
      for (const art of articles) {
        const titleEl = art.querySelector('h2, h3');
        const link = art.querySelector('a[href*="/p/"], a[href*="medium.com"], a[data-action="open-post"]');
        if (!link) continue;
        const url = link.href.split('?')[0];
        if (seen.has(url)) continue;
        seen.add(url);
        const title = titleEl ? (titleEl.innerText || '').replace(/\s+/g, ' ').trim() : '';
        let author = '';
        const authorEl = art.querySelector('a[href*="/@"], p');
        if (authorEl) author = (authorEl.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80);
        out.push({ url, title, author });
      }
      return out;
    }
    """
    raw = page.evaluate(js)
    items = []
    for i, r in enumerate(raw[:limit], start=1):
        items.append(make_item(
            title=r.get("title", ""),
            url=r["url"],
            platform_name=PLATFORMS["medium"]["name"],
            source_url=PLATFORMS["medium"]["source_url"],
            author=r.get("author", ""),
            post_text="",
            saved_rank=i,
        ))
    return items


def scrape_reddit(page, limit: int) -> list:
    # old.reddit.com renders saves server-side as div.thing rows (no infinite scroll).
    js = r"""
    () => {
      const out = [];
      const seen = new Set();
      const things = Array.from(document.querySelectorAll('div.thing'));
      for (const t of things) {
        const titleEl = t.querySelector('a.title');
        const permalink = t.getAttribute('data-permalink') || '';
        const dataUrl = t.getAttribute('data-url') || '';
        let url = '';
        if (dataUrl && /^https?:/.test(dataUrl)) url = dataUrl;
        else if (titleEl && titleEl.href) url = titleEl.href;
        else if (permalink) url = 'https://www.reddit.com' + permalink;
        if (!url) continue;
        const clean = url.split('?')[0];
        if (seen.has(clean)) continue;
        seen.add(clean);
        const title = titleEl ? (titleEl.innerText || '').replace(/\s+/g, ' ').trim() : '';
        const subreddit = t.getAttribute('data-subreddit') || '';
        const author = t.getAttribute('data-author') || '';
        out.push({ url: clean, title, author, subreddit });
      }
      return out;
    }
    """
    raw = page.evaluate(js)
    items = []
    for i, r in enumerate(raw[:limit], start=1):
        sub = (r.get("subreddit") or "").strip()
        author = (r.get("author") or "").strip()
        byline = f"r/{sub}" if sub else ""
        if author:
            byline = f"{byline} · u/{author}" if byline else f"u/{author}"
        items.append(make_item(
            title=r.get("title", ""),
            url=r["url"],
            platform_name=PLATFORMS["reddit"]["name"],
            source_url=PLATFORMS["reddit"]["source_url"],
            author=byline,
            post_text=r.get("title", ""),
            saved_rank=i,
        ))
    return items


def scrape_github(page, limit: int) -> list:
    # GitHub stars paginate at 30/page via &page=N. Walk pages until we hit the limit.
    js = r"""
    () => {
      const out = [];
      const seen = new Set();
      const cards = Array.from(document.querySelectorAll('div.col-12'));
      for (const c of cards) {
        const a = c.querySelector('h3 a[href]');
        if (!a) continue;
        const href = (a.getAttribute('href') || '').split('?')[0];
        if (!/^\/[^\/]+\/[^\/]+\/?$/.test(href)) continue;
        const repo = href.replace(/^\//, '').replace(/\/$/, '');
        const url = 'https://github.com/' + repo;
        if (seen.has(url)) continue;
        seen.add(url);
        const p = c.querySelector('p');
        const desc = p ? (p.innerText || '').replace(/\s+/g, ' ').trim() : '';
        const langEl = c.querySelector('[itemprop="programmingLanguage"]');
        const lang = langEl ? (langEl.innerText || '').trim() : '';
        out.push({ url, repo, desc, lang });
      }
      return out;
    }
    """
    base = page.url.split("&page=")[0].split("?page=")[0]
    max_pages = max(1, (limit + 29) // 30)
    collected = []
    seen = set()
    for pnum in range(1, max_pages + 1):
        if pnum > 1:
            sep = "&" if "?" in base else "?"
            page.goto(f"{base}{sep}page={pnum}", wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(1500)
        raw = page.evaluate(js)
        new_on_page = 0
        for r in raw:
            if r["url"] in seen:
                continue
            seen.add(r["url"])
            collected.append(r)
            new_on_page += 1
        if len(collected) >= limit or new_on_page == 0:
            break

    items = []
    for i, r in enumerate(collected[:limit], start=1):
        lang = (r.get("lang") or "").strip()
        author = f"{lang}" if lang else ""
        items.append(make_item(
            title=r.get("repo", ""),
            url=r["url"],
            platform_name=PLATFORMS["github"]["name"],
            source_url=PLATFORMS["github"]["source_url"],
            author=author,
            post_text=r.get("desc", ""),
            saved_rank=i,
        ))
    return items


def scrape_youtube(page, limit: int) -> list:
    # The Watch Later playlist lazy-loads ytd-playlist-video-renderer rows on scroll.
    scroll_to_load(page, limit)
    js = r"""
    () => {
      const out = [];
      const seen = new Set();
      const rows = Array.from(document.querySelectorAll('ytd-playlist-video-renderer'));
      for (const r of rows) {
        const a = r.querySelector('a#video-title, a#wc-endpoint');
        if (!a) continue;
        let href = a.getAttribute('href') || '';
        // Normalise to a clean watch URL, dropping playlist/index params.
        const m = href.match(/[?&]v=([^&]+)/) || href.match(/\/watch\/([^?&]+)/);
        if (!m) continue;
        const url = 'https://www.youtube.com/watch?v=' + m[1];
        if (seen.has(url)) continue;
        seen.add(url);
        const title = (a.getAttribute('title') || a.innerText || '').replace(/\s+/g, ' ').trim();
        const chanEl = r.querySelector('ytd-channel-name a, #channel-name a, ytd-channel-name #text');
        const channel = chanEl ? (chanEl.innerText || '').replace(/\s+/g, ' ').trim() : '';
        out.push({ url, title, channel });
      }
      return out;
    }
    """
    raw = page.evaluate(js)
    items = []
    for i, r in enumerate(raw[:limit], start=1):
        items.append(make_item(
            title=r.get("title", ""),
            url=r["url"],
            platform_name=PLATFORMS["youtube"]["name"],
            source_url=PLATFORMS["youtube"]["source_url"],
            author=(r.get("channel") or "").strip(),
            post_text=r.get("title", ""),
            saved_rank=i,
        ))
    return items


def enrich_youtube(page, items: list) -> None:
    """Visit each Watch Later video with the logged-in page and pull its description.

    YouTube descriptions are JS-rendered, so the generic HTTP-based
    ``extract_full_text`` cannot read them. We reuse the authenticated Playwright
    page to navigate to each watch URL and read the description DOM in place.
    Best-effort: a failure on one video leaves its ``full_text`` unset and
    continues with the rest.
    """
    js = r"""
    () => {
      const pick = (sel) => {
        const el = document.querySelector(sel);
        return el ? (el.innerText || '').replace(/\u00a0/g, ' ').trim() : '';
      };
      // Collapsed or expanded, the full description text is present in the DOM.
      let desc = pick('#description-inline-expander #expanded')
             || pick('ytd-text-inline-expander#description-inline-expander')
             || pick('#description-inline-expander')
             || pick('ytd-watch-metadata #description');
      if (!desc) {
        const meta = document.querySelector('meta[name="description"]');
        desc = meta ? (meta.getAttribute('content') || '').trim() : '';
      }
      return desc;
    }
    """
    for it in items:
        try:
            log.info("Extracting YouTube description: %s", it["url"])
            page.goto(it["url"], wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(1500)
            desc = page.evaluate(js)
            if desc:
                it["full_text"] = desc
        except Exception as e:  # noqa: BLE001 - best-effort enrichment
            log.warning("YouTube description extraction failed for %s: %s", it["url"], e)


SCRAPERS = {
    "linkedin": scrape_linkedin,
    "twitter": scrape_twitter,
    "medium": scrape_medium,
    "reddit": scrape_reddit,
    "github": scrape_github,
    "youtube": scrape_youtube,
}


# ---------------------------------------------------------------------------
# Browser orchestration
# ---------------------------------------------------------------------------

def run(
    platform: str,
    *,
    user_data_dir: Path,
    login: bool,
    limit: int,
    full_text: bool,
    list_type: str,
    handle: Optional[str],
) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {
            "error": "playwright is not installed.",
            "hint": "pip install playwright && python -m playwright install chromium",
        }

    cfg = PLATFORMS[platform]
    user_data_dir.mkdir(parents=True, exist_ok=True)

    # Resolve the target URL (Twitter likes / Reddit / GitHub need the handle).
    if platform == "twitter" and list_type == "likes":
        if not handle:
            return {"error": "X likes require --handle (your @handle without the @)."}
        target_url = cfg["likes_url"].format(handle=handle.lstrip("@"))
    elif cfg.get("requires_handle"):
        if not handle:
            return {"error": f"{cfg['name']} requires --handle (your username, without @)."}
        target_url = cfg["saved_url"].format(handle=handle.lstrip("@"))
    else:
        target_url = cfg["saved_url"]

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(user_data_dir),
            headless=not login,
            viewport={"width": 1280, "height": 1400},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()

        try:
            if login:
                log.info("Opening %s for login. Complete the sign-in in the browser window.", cfg["name"])
                page.goto(cfg["login_url"], wait_until="domcontentloaded", timeout=60000)
                log.info("After you finish logging in, return here and press Enter to save the session...")
                try:
                    input()
                except EOFError:
                    page.wait_for_timeout(45000)
                context.close()
                return {
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                    "platform": platform,
                    "login": True,
                    "user_data_dir": str(user_data_dir),
                    "note": f"Session saved for {cfg['name']}. Re-run without --login to fetch saves.",
                    "items": [],
                }

            log.info("Navigating to %s saves: %s", cfg["name"], target_url)
            page.goto(target_url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(3000)

            # Detect an auth wall by URL.
            current = page.url.lower()
            if "login" in current or "signin" in current or "/i/flow/login" in current:
                context.close()
                return {
                    "error": f"Not logged in to {cfg['name']} (redirected to a login page).",
                    "hint": f"Run once with --login: "
                            f"python scripts/pipeline/social_saves_reader.py --platform {platform} --login",
                }

            scraper = SCRAPERS[platform]
            items = scraper(page, limit)

            if full_text and platform == "youtube":
                # YouTube descriptions are JS-rendered; enrich via the logged-in page.
                enrich_youtube(page, items)
            elif full_text:
                for it in items:
                    # Only enrich genuine external article URLs (skip platform permalinks).
                    if it["domain"] and it["domain"] not in (
                        "www.linkedin.com", "linkedin.com", "x.com", "twitter.com",
                        "www.reddit.com", "reddit.com", "old.reddit.com",
                        "github.com", "www.github.com",
                        "www.youtube.com", "youtube.com", "m.youtube.com", "youtu.be",
                    ):
                        log.info("Extracting full text: %s", it["url"])
                        it["full_text"] = extract_full_text(it["url"])

            context.close()
        except Exception as e:  # noqa: BLE001 - surface as structured error
            try:
                context.close()
            except Exception:
                pass
            return {"error": f"Scrape failed for {cfg['name']}: {e}"}

    list_label = list_type if platform == "twitter" else {
        "github": "stars",
        "youtube": "watch-later",
    }.get(platform, "saved")
    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "source": f"{platform}-saves",
        "platform": platform,
        "list_type": list_label,
        "target_url": target_url,
        "user_data_dir": str(user_data_dir),
        "total_items": len(items),
        "filtered_items": len(items),
        "items": items,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Social Saves Reader — read your own LinkedIn/X/Medium/Reddit/GitHub/YouTube saved items via Playwright.",
    )
    parser.add_argument(
        "--platform", "-P", required=True, choices=sorted(PLATFORMS.keys()),
        help="Which platform's saved items to read.",
    )
    parser.add_argument(
        "--login", action="store_true", default=False,
        help="Open a headed browser to log in once; persists the session for future headless runs.",
    )
    parser.add_argument(
        "--limit", "-n", type=int, default=40,
        help="Max number of saved items to collect (default: 40).",
    )
    parser.add_argument(
        "--list", dest="list_type", choices=["bookmarks", "likes"], default="bookmarks",
        help="X/Twitter only: read bookmarks (default) or likes.",
    )
    parser.add_argument(
        "--handle", default=None,
        help="Your username/@handle (no @). Required for X --list likes, Reddit saved, and GitHub stars.",
    )
    parser.add_argument(
        "--full-text", action="store_true", default=False,
        help="Fetch full article text for external URLs via trafilatura; for YouTube, "
             "visit each video to pull its description (slower, richer).",
    )
    parser.add_argument(
        "--user-data-dir", default=str(DEFAULT_USER_DATA_DIR),
        help=f"Playwright profile dir for persistent login (default: {DEFAULT_USER_DATA_DIR}).",
    )
    args = parser.parse_args()

    result = run(
        args.platform,
        user_data_dir=Path(args.user_data_dir).expanduser(),
        login=args.login,
        limit=args.limit,
        full_text=args.full_text,
        list_type=args.list_type,
        handle=args.handle,
    )

    if "error" in result:
        log.error(result["error"])
        if "hint" in result:
            log.info(result["hint"])
        json.dump(result, sys.stdout, indent=2)
        print()
        sys.exit(2)

    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
