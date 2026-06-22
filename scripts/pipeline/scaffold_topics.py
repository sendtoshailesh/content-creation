#!/usr/bin/env python3
"""Scaffold per-topic content pipelines under content/topics/<slug>/.

For each configured topic this generates an isolated workspace:
  - pipeline-config.md   (topic-scoped, Topic preset, outputs land in the workspace)
  - feed-sources.md      (topic-relevant feeds + subject filters)
  - idea-queue.md        (seeded with candidate source material clustered from your
                          Apple Notes + Chrome bookmarks)
and a top-level content/topics/README.md registry.

Source material is clustered by keyword. Employer-internal / personal items are filtered
out (never written to committed files). Run `@feed-curator` inside a topic workspace to turn
the seeded candidates into ranked, scored ideas.

Usage:
  python scripts/pipeline/scaffold_topics.py            # generate all topics
  python scripts/pipeline/scaffold_topics.py --dry-run  # print clustering only
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

REPO = Path(__file__).resolve().parents[2]
TOPICS_DIR = REPO / "content" / "topics"
BOOKMARKS = (
    Path.home()
    / "Library/Application Support/Google/Chrome/Default/Bookmarks"
)

# --- topic definitions ---------------------------------------------------------------

TOPICS: dict[str, dict] = {
    "postgresql": {
        "title": "PostgreSQL",
        "desc": "PostgreSQL internals, performance, pgvector/AI-on-Postgres, search.",
        "tags": ["Databases", "PostgreSQL", "Performance"],
        "keywords": ["postgres", "pgvector", "pgvectorscale", "pgai", "pg_", "psql",
                     "bitmap-and", "bm25", "planet postgres", "awesome-postgres"],
        "feeds": [
            ("Planet PostgreSQL", "https://planet.postgresql.org/rss20.xml", "rss"),
            ("PostgreSQL Weekly", "https://postgresweekly.com/rss", "rss"),
        ],
    },
    "agentic-ai": {
        "title": "Agentic AI",
        "desc": "Agent design patterns, eval harnesses, failure taxonomies, MCP, RAG.",
        "tags": ["AI & LLM", "Agentic AI", "Architecture"],
        "keywords": ["agent", "agentic", "mcp", " rag", "react pattern", "autonomous",
                     "openclaw", "tool use", "eval harness", "failure taxonomy",
                     "computer use", "multi-agent", "orchestrat"],
        "feeds": [
            ("Simon Willison's Weblog", "https://simonwillison.net/atom/everything/", "rss"),
            ("TLDR AI", "https://tldr.tech/ai", "newsletter-archive"),
        ],
    },
    "ai-general": {
        "title": "AI (general)",
        "desc": "LLMs, frontier models, prompting, doc AI, cost, safety.",
        "tags": ["AI & LLM"],
        "keywords": ["llm", "gpt", "claude", "gemini", "anthropic", "openai", "prompt",
                     "arc-agi", "doc ai", "ocr", "generative ai", "abuse monitoring",
                     "karpathy", "reasoning"],
        "feeds": [
            ("DeepLearning.AI Batch", "https://www.deeplearning.ai/the-batch", "newsletter-archive"),
            ("TLDR AI", "https://tldr.tech/ai", "newsletter-archive"),
        ],
    },
    "machine-learning": {
        "title": "Machine Learning",
        "desc": "ML math, NLP, transfer learning, semantic search, ML systems.",
        "tags": ["AI & LLM", "Machine Learning", "Data Science"],
        "keywords": ["machine learning", "transfer learning", "tf-idf", "nlp",
                     "quantum machine learning", "transformers", "semantic",
                     "summarization", "embedding", "math needed", "ml system"],
        "feeds": [
            ("Towards Data Science", "https://towardsdatascience.com/feed", "rss"),
            ("DeepLearning.AI Batch", "https://www.deeplearning.ai/the-batch", "newsletter-archive"),
        ],
    },
    "python": {
        "title": "Python",
        "desc": "Python language, tooling, interview prep, dev-productivity CLIs.",
        "tags": ["Python", "DevTools"],
        "keywords": ["python", "pythonweekly", "pip ", "django", "flask", "fastapi",
                     "copilot cli", "interview", "pytest"],
        "feeds": [
            ("Real Python", "https://realpython.com/atom.xml", "rss"),
            ("Python Weekly", "https://www.pythonweekly.com/", "newsletter-archive"),
        ],
    },
    "azure-ms-ai": {
        "title": "Azure / Microsoft AI",
        "desc": "Azure AI, Microsoft Foundry, platform engineering for the agentic era.",
        "tags": ["Azure", "AI & LLM", "Platform Engineering"],
        "keywords": ["azure", "microsoft foundry", "foundry", "learn.microsoft",
                     "platform engineering", "ptu", "well-architected", "copilot"],
        "feeds": [
            ("Azure Blog", "https://azure.microsoft.com/en-us/blog/feed/", "rss"),
            ("InfoQ", "https://feed.infoq.com/", "rss"),
        ],
    },
    "ai-native-dev": {
        "title": "AI-native software development",
        "desc": "Spec-driven dev, vibe coding, AI-edited codebases, drift detection.",
        "tags": ["AI & LLM", "DevTools", "Developer Productivity"],
        "keywords": ["spec driven", "spec-driven", "vibe coding", "drift detector",
                     "ai-edited", "ai native app", "figma to selenium", "ai-dlc",
                     "code review", "coherence"],
        "feeds": [
            ("GitHub Blog", "https://github.blog/feed/", "rss"),
            ("The Pragmatic Engineer", "https://newsletter.pragmaticengineer.com/", "newsletter-archive"),
        ],
    },
    "cloud-databases": {
        "title": "Cloud databases",
        "desc": "Aurora, DSQL, RDS, DynamoDB, MongoDB, AWS vs Azure data services.",
        "tags": ["Databases", "Cloud", "Architecture"],
        "keywords": ["aurora", "dsql", "rds", "dynamodb", "mongodb", "aws vs azure",
                     " s3 ", "cloud database", "kiro", "database blog"],
        "feeds": [
            ("AWS Database Blog", "https://aws.amazon.com/blogs/database/feed/", "rss"),
            ("InfoQ", "https://feed.infoq.com/", "rss"),
        ],
    },
}

# --- filtering -----------------------------------------------------------------------

# Employer-internal / private domains — never written to committed files.
BLOCK_DOMAIN = (
    "w.amazon.com", "broadcast.amazon.com", "wisdom.corp", "phonetool",
    "awsapps.com", "quip-amazon", "code.amazon", "hub.amazon.dev", "guide.aws.dev",
    ".corp.", "sharepoint.com", "my.sharepoint", "my.oracle.com", "ouweb",
    "highspot.com", "amazon.awsapps", "notebooklm.google.com", "phonetool.amazon",
)
# Personal / noise note titles.
NOISE_TITLE = re.compile(
    r"^(new note|saved photo|call with|untitled|conrad|jaideep|6 websites)",
    re.I,
)
NOISE_SUBSTR = (
    "papa mummy", "reet mishra", "supplement", "ikigai", "career planning",
    "pmc bank", "perk application", "youtube music", "agar hum", "want to part of research",
)


def is_internal(url: str) -> bool:
    u = (url or "").lower()
    return any(b in u for b in BLOCK_DOMAIN)


def is_noise(title: str) -> bool:
    t = (title or "").strip().lower()
    if len(t) < 8:
        return True
    if NOISE_TITLE.match(t):
        return True
    return any(s in t for s in NOISE_SUBSTR)


# --- source readers ------------------------------------------------------------------

def read_notes() -> list[dict]:
    try:
        out = subprocess.run(
            [sys.executable, str(REPO / "scripts/pipeline/apple_notes_reader.py"),
             "--time-range", "all"],
            capture_output=True, text=True, timeout=120,
        ).stdout
        data = json.loads(out)
    except Exception as e:  # pragma: no cover
        print(f"WARN: could not read notes ({e})", file=sys.stderr)
        return []
    items = data if isinstance(data, list) else data.get("items") or data.get("notes") or []
    res = []
    for it in items:
        title = (it.get("title") or "").strip()
        url = (it.get("url") or "")
        # pull first URL out of snippet/body if title has none
        body = (it.get("snippet") or it.get("body") or "")
        if not url:
            m = re.search(r"https?://\S+", f"{title} {body}")
            url = m.group(0).rstrip(").,") if m else ""
        res.append({"title": title, "url": url, "text": f"{title} {body}", "src": "Apple Note"})
    return res


def read_reading_list() -> list[dict]:
    """Pull Chrome reading list via reading_list_reader.py (which reads the sync LevelDB)."""
    try:
        out = subprocess.run(
            [sys.executable, str(REPO / "scripts/pipeline/reading_list_reader.py"),
             "--time-range", "all"],
            capture_output=True, text=True, timeout=120,
        ).stdout
        data = json.loads(out)
    except Exception as e:  # pragma: no cover
        print(f"WARN: could not read reading list ({e})", file=sys.stderr)
        return []
    res = []
    for it in data.get("items", []):
        title = (it.get("title") or "").strip()
        url = it.get("url") or ""
        res.append({"title": title, "url": url, "text": f"{title} {url}", "src": "Reading List"})
    return res


def read_bookmarks() -> list[dict]:
    if not BOOKMARKS.is_file():
        return []
    data = json.loads(BOOKMARKS.read_text())
    out: list[dict] = []

    def walk(node, folder):
        if node.get("type") == "folder":
            for c in node.get("children", []):
                walk(c, node.get("name", folder))
        elif node.get("type") == "url":
            out.append({
                "title": (node.get("name") or "").strip(),
                "url": node.get("url") or "",
                "text": f"{node.get('name','')} {folder} {node.get('url','')}",
                "src": "Bookmark",
            })

    for r in data.get("roots", {}).values():
        if isinstance(r, dict):
            walk(r, "")
    return out


# --- clustering ----------------------------------------------------------------------

def cluster(items: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {k: [] for k in TOPICS}
    seen: set[str] = set()
    for it in items:
        if is_internal(it["url"]):
            continue
        # Noise-title filter applies only to items without a URL (e.g. scratch notes).
        if not it["url"] and is_noise(it["title"]):
            continue
        key = (it["url"] or it["title"]).lower()
        if key in seen:
            continue
        seen.add(key)
        text = it["text"].lower()
        scored = []
        for slug, meta in TOPICS.items():
            hits = sum(1 for kw in meta["keywords"] if kw in text)
            if hits:
                scored.append((hits, slug))
        scored.sort(reverse=True)
        for _, slug in scored[:2]:  # assign to at most 2 best-matching topics
            buckets[slug].append(it)
    return buckets


# --- rendering -----------------------------------------------------------------------

def render_config(slug: str, meta: dict) -> str:
    return f"""# Pipeline Config — {meta['title']}

> Topic-scoped pipeline. The orchestrator reads this when run with topic `{slug}`
> (e.g. `/topic-pipeline {slug}`). Outputs land in this workspace
> (`content/topics/{slug}/`). Persistent files: `feed-sources.md`, `idea-queue.md`.

## Pipeline Status

| Field | Value |
|-------|-------|
| **Status** | `not-started` |
| **Topic** | {meta['title']} |
| **Topic slug** | `{slug}` |
| **Output path** | `content/topics/{slug}/` |
| **Started** | _(set on first run)_ |
| **Current Step** | _(set on first run)_ |
| **Series** | `pending-assessment` |

### Step Checklist

- [ ] Step 0: Reference analysis
- [ ] Steps 1-2: Creative brief + strategy + outline
- [ ] Step 2b-2e: Scope, dimensions, visual map, art direction
- [ ] Step 3: Blog post
- [ ] Step 3b: Visual assets
- [ ] Step 3b-img: Hero/illustrative imagery (optional)
- [ ] Step 3c: Quality review
- [ ] Step 3e: Grounded content review (web-verified)
- [ ] Step 3d: SEO optimization
- [ ] Step 4a: Social distribution strategy
- [ ] Step 4a-visual: Visual-first pack (carousel/exhibit via visual-pack-generator)
- [ ] Step 4: Social posts (LinkedIn always; visual-first + canonical link)
- [ ] Step 7: Brand audit (severity-gated)
- [ ] Step 10: Web publishing
- [ ] Step 11: Social publishing
- [ ] Step 12: Platform distillation (Medium / Substack / LinkedIn Article + canonical URL)

**Status values:** `not-started` | `in-progress` | `completed` | `blocked`

---

## Image Generation (hybrid AI imagery)

| Field | Value |
|-------|-------|
| **mode** | `programmatic` |
| **provider** (ai mode) | `openai` |
| **model** (ai mode) | `gpt-image-1` |
| **size** | `1024x1024` |
| **max_images_per_run** | `3` |

## Visual-First Distribution

> Step 4a-visual generates a visual asset pack before social/long-form distribution.
> Read by: `visual-pack-generator` skill, `social-linkedin`, `social-twitter`, `platform-distiller`.

| Field | Value |
|-------|-------|
| **distillation_persona_mode** | `practitioner` |
| **distillation_slug** | `{slug}` |

> `practitioner` = 10-slide LinkedIn carousel (1080×1080). `executive` = 3–5 exhibits (1200×627).
> Output: `content/visuals/distilled/{slug}-{mode}/`.

## Output Preferences

- **Blog target length**: ~3,000 words per part
- **Output path**: `content/topics/{slug}/`

### Social Platform Selection

- [x] LinkedIn (always — visual-first when a pack exists, links to canonical blog)
- [ ] X/Twitter
- [ ] Reddit
- [ ] Reel/Short video
- [ ] YouTube

### Long-Form Platform Distribution (Step 12)

> `platform-distiller` produces ONE unified excerpt for all three, pointing to the GitHub Pages
> canonical URL. Visual-first when a distilled pack exists; text-only otherwise.

- [x] Medium (700–900 words; Import tool sets canonical — SEO safe)
- [x] Substack (300–500-word excerpt / Note)
- [x] LinkedIn Article (700–900 words, distinct angle — not a republish of the LinkedIn post)

## Online References

> Topic source material is seeded in `idea-queue.md`. Add specific reference URLs here
> before a run, or let `@reference-discovery` populate them.

<!-- - [description](URL) — what to extract -->
"""


def render_feeds(slug: str, meta: dict) -> str:
    rows = "\n".join(
        f"| {n} | {u} | {t} | daily | {', '.join(meta['tags'])} |"
        for (n, u, t) in meta["feeds"]
    )
    return f"""# Feed Sources — {meta['title']}

> Topic-scoped feed registry for `{slug}`. `@feed-curator` reads this when run in this
> workspace. Persists across runs.

## Source Registry

| Name | URL | Type | Frequency | Tags |
|------|-----|------|-----------|------|
{rows}

## Subject Area Filters

> Keep ideas focused on this topic. Tags: {', '.join(meta['tags'])}.

| Subject area | Priority | Keywords |
|--------------|----------|----------|
| {meta['title']} | high | {', '.join(k.strip() for k in meta['keywords'][:8])} |
"""


def render_queue(slug: str, meta: dict, items: list[dict]) -> str:
    notes = [i for i in items if i["src"] == "Apple Note"][:30]
    marks = [i for i in items if i["src"] == "Bookmark"][:40]
    rlist = [i for i in items if i["src"] == "Reading List"][:40]

    def fmt(i):
        t = (i["title"][:100] or i["url"]).replace("|", "/")
        return f"- [{t}]({i['url']})" if i["url"] else f"- {t}"

    note_block = "\n".join(fmt(i) for i in notes) or "_(none clustered)_"
    mark_block = "\n".join(fmt(i) for i in marks) or "_(none clustered)_"
    rlist_block = "\n".join(fmt(i) for i in rlist) or "_(none clustered)_"
    return f"""# Idea Queue — {meta['title']}

> **Candidate source material** clustered from your Apple Notes + Chrome bookmarks + Chrome
> reading list ({len(items)} items matched this topic). These are raw inputs, not yet scored.
> Run `@feed-curator` (or `@reading-list-curator`) in this workspace to synthesize and
> rank them into content ideas, then `@content-pipeline` / `/topic-pipeline {slug}` to write.

Last seeded: {date.today().isoformat()} by `scripts/pipeline/scaffold_topics.py`
(employer-internal and personal links excluded).

---

## Candidate source material

### From Apple Notes
{note_block}

### From Chrome bookmarks
{mark_block}

### From Chrome reading list
{rlist_block}

---

## Queued Ideas

<!-- Synthesized, scored ideas are appended here by @feed-curator. -->
"""


def render_registry(buckets: dict[str, list[dict]]) -> str:
    rows = "\n".join(
        f"| {TOPICS[s]['title']} | `{s}` | {len(buckets[s])} | `not-started` | "
        f"[config](./{s}/pipeline-config.md) · [ideas](./{s}/idea-queue.md) |"
        for s in TOPICS
    )
    return f"""# Topic Pipelines

> Each topic has an isolated content pipeline workspace. Run a topic with
> `/topic-pipeline <slug>` or `@content-pipeline` after `cd`-ing your focus to the
> topic folder. Idea queues are seeded from your Apple Notes + Chrome bookmarks.

Last scaffolded: {date.today().isoformat()} via `scripts/pipeline/scaffold_topics.py`.

| Topic | Slug | Seeded candidates | Status | Links |
|-------|------|-------------------|--------|-------|
{rows}

## How to use

1. Pick a topic and open `content/topics/<slug>/idea-queue.md` — review the seeded candidates.
2. Run `@feed-curator` (scoped to the topic's `feed-sources.md`) to fetch fresh articles and
   synthesize ranked ideas.
3. Run `/topic-pipeline <slug>` (or `@content-pipeline` with the topic) — the orchestrator
   reads `content/topics/<slug>/pipeline-config.md` and writes outputs into that workspace.
4. Topics are independent: you can run several in parallel without collisions.

## Re-seed

Re-run `python scripts/pipeline/scaffold_topics.py` after capturing new notes/bookmarks.
It regenerates idea queues; it will **not** overwrite an existing `pipeline-config.md` whose
status is not `not-started` (in-flight runs are preserved).
"""


# --- driver --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scaffold per-topic content pipelines.")
    parser.add_argument("--dry-run", action="store_true", help="Print clustering only.")
    args = parser.parse_args(argv)

    items = read_notes() + read_bookmarks() + read_reading_list()
    buckets = cluster(items)

    print("Clustered candidates per topic:")
    for slug in TOPICS:
        print(f"  {slug:18s} {len(buckets[slug]):4d}")
    if args.dry_run:
        return 0

    TOPICS_DIR.mkdir(parents=True, exist_ok=True)
    for slug, meta in TOPICS.items():
        d = TOPICS_DIR / slug
        d.mkdir(exist_ok=True)
        cfg = d / "pipeline-config.md"
        # Preserve in-flight runs: only (re)write config if absent or not-started.
        if not cfg.exists() or "`not-started`" in cfg.read_text():
            cfg.write_text(render_config(slug, meta), encoding="utf-8")
        (d / "feed-sources.md").write_text(render_feeds(slug, meta), encoding="utf-8")
        (d / "idea-queue.md").write_text(render_queue(slug, meta, buckets[slug]), encoding="utf-8")
    (TOPICS_DIR / "README.md").write_text(render_registry(buckets), encoding="utf-8")
    print(f"\nScaffolded {len(TOPICS)} topic workspaces under {TOPICS_DIR.relative_to(REPO)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
