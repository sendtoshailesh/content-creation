---
description: "Generate content ideas from your authenticated social saves — LinkedIn Saved posts, X/Twitter Bookmarks & Likes, Medium reading list, Reddit Saved, GitHub Stars, and YouTube Watch Later. Reads your own logged-in session (Playwright, read-only), categorizes by subject area, clusters related saves into themes, and queues ideas interactively."
agent: "social-saves-curator"
argument-hint: "Optionally name a platform: linkedin, twitter, medium, reddit, github, youtube, or all"
---

Generate content ideas from your social saves (LinkedIn, X/Twitter, Medium, Reddit, GitHub, YouTube).

1. **Platform** — Pick linkedin, twitter, medium, reddit, github, youtube, or all (bookmarks vs likes for X; username for reddit/github)
2. **Fetch** — Read your own saved items via your logged-in browser session (read-only; one-time login per platform)
3. **Categorize** — Auto-classify saves against your subject area filters
4. **Cluster** — Group related saves into theme clusters; cross-platform overlap is the strongest signal
5. **Score** — Smart priority scoring (recency via save-rank, relevance, cluster size)
6. **Curate** — Interactively keep, dismiss, merge, or explore ideas
7. **Queue** — Save accepted ideas to `content/idea-queue.md`
8. **Reference** — Optionally batch-add URLs to `content/pipeline-config.md` references

Items you bookmark mid-scroll are high-intent signals — you already found each one worth saving.
