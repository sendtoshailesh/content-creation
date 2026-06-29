# Feed Sources Configuration

> **Persistent configuration** for blog roll, newsletter, and RSS feed sources. This file survives across content pipeline runs (unlike `pipeline-config.md` which resets per run). Edit this to add/remove sources and tune subject area filters.

---

## Source Registry

> Add your blog rolls, newsletters, RSS feeds, and direct URLs here. The `feed-curator` agent reads this table to know where to fetch content from.

| Name | URL | Type | Frequency | Tags |
|------|-----|------|-----------|------|
| GitHub Blog | https://github.blog/feed/ | rss | daily | AI, DevTools, Engineering |
| Deeplearning AI Batch | https://www.deeplearning.ai/the-batch | newsletter-archive | daily | AI |
| Towards Data Science (Medium) | https://towardsdatascience.com/feed | rss | daily | AI, ML, Data Science |
| PostgreSQL weekly | https://postgresweekly.com/latest | newsletter-archive | weekly | Databases |
| Simon Willison's Weblog | https://simonwillison.net/atom/everything/ | rss | daily | AI, LLM, DevTools |
| TLDR AI | https://tldr.tech/ai | newsletter-archive | daily | AI, ML, LLM |
| InfoQ | https://feed.infoq.com/ | rss | daily | Architecture, Cloud, DevOps |
| Ahead of AI (Sebastian Raschka) | https://magazine.sebastianraschka.com/feed | rss | weekly | AI, LLM, Machine Learning |
| Lilian Weng | https://lilianweng.github.io/index.xml | rss | monthly | AI, LLM, Machine Learning |
| Latent Space | https://www.latent.space/feed | rss | weekly | AI, LLM, Engineering |
| Martin Fowler | https://martinfowler.com/feed.atom | rss | weekly | Architecture, Engineering |
| ByteByteGo (Alex Xu) | https://blog.bytebytego.com/feed | rss | weekly | Architecture, Solution Architecture |
| Jepsen (Kyle Kingsbury) | https://aphyr.com/posts.atom | rss | monthly | Databases, Distributed Systems |

### Source Types

| Type | Description | How It's Processed |
|------|-------------|-------------------|
| `rss` | Standard RSS or Atom feed | Parsed with `feedparser`, entries extracted with title/link/date/summary |
| `newsletter-archive` | Web archive page of a newsletter | Page fetched, article links extracted, each article fetched individually |
| `direct-url` | A specific article or page URL | Full text extracted directly via `trafilatura` |
| `opml` | OPML subscription export file | Parsed for feed URLs, each processed as `rss` type |

> **Note:** Chrome Reading List is handled by the dedicated `@reading-list-curator` agent (not via this feed-sources table). Run `@reading-list-curator` or `/reading-list-ideas` to generate ideas from your Chrome reading list. It uses the same subject area filters and scoring system defined below.

> **Note:** Authenticated social saves — **LinkedIn Saved posts, X/Twitter Bookmarks & Likes, the Medium reading list, Reddit Saved posts, GitHub Stars, and YouTube Watch Later** — are handled by the dedicated `@social-saves-curator` agent (not via this feed-sources table). Run `@social-saves-curator` or `/social-saves-ideas`. It reads your own logged-in browser session via Playwright (read-only, isolated profile; one-time login per platform) and uses the same subject area filters and scoring system defined below.

### How to Add Sources

1. Add a row to the table above with the source details
2. Set the **Type** to match how the source should be fetched
3. Add **Tags** that match your subject area filters below (comma-separated)
4. Run `@feed-curator` to test the new source

### OPML Import

> To bulk-import feeds from a feed reader (Feedly, Inoreader, The Old Reader), export your subscriptions as OPML and add the file path here.

**OPML files:**
<!-- Add paths to OPML files below. Format: - path/to/subscriptions.opml -->

---

## Subject Area Filters

> Define the topics you want to track. The feed curator uses these to classify and filter articles. Only articles matching at least one subject area (above the relevance threshold) are considered for the idea queue.

| Subject Area | Keywords | Priority |
|-------------|----------|----------|
| AI & LLM | artificial intelligence, large language model, LLM, GPT, Claude, Gemini, foundation model, prompt engineering, RAG, agentic AI, AI agent | 1 |
| Machine Learning | machine learning, deep learning, neural network, training, fine-tuning, MLOps, model serving, inference | 2 |
| Architecture | software architecture, system design, microservices, event-driven, distributed systems, scalability, design patterns | 1 |
| Distributed Systems | distributed systems, consensus, consistency, CAP theorem, replication, partitioning, Raft, Paxos, fault tolerance, linearizability, Jepsen | 2 |
| Solution Architecture | cloud architecture, reference architecture, well-architected, landing zone, migration, modernization | 1 |
| Databases | PostgreSQL, database, SQL, NoSQL, Cosmos DB, query optimization, indexing, data modeling, replication | 2 |
| Cloud & Infrastructure | Azure, AWS, GCP, Kubernetes, containers, serverless, IaC, Terraform, Bicep | 2 |
| DevOps & Platform Engineering | CI/CD, DevOps, platform engineering, SRE, observability, monitoring, deployment | 3 |
| Developer Productivity | developer experience, DX, code assistant, Copilot, IDE, tooling, workflow automation | 2 |

### Priority Levels

| Priority | Meaning | Minimum Relevance Score |
|----------|---------|------------------------|
| 1 | **Core** — Always interested, lower threshold for inclusion | 2/5 |
| 2 | **High** — Actively tracking, standard threshold | 3/5 |
| 3 | **Moderate** — Interested when particularly insightful | 4/5 |

---

## Extraction Preferences

> Tune how aggressively the feed curator filters and ranks content.

| Setting | Value | Description |
|---------|-------|-------------|
| **Default relevance threshold** | `3` | Minimum relevance score (1-5) for an article to be considered. Subject area priority can lower this. |
| **Max article age (days)** | `14` | Ignore articles older than this many days |
| **Dedup window (days)** | `30` | Check idea queue for duplicates within this window |
| **Max ideas per run** | `15` | Maximum number of ideas to present per curation run |
| **Full text extraction** | `yes` | Fetch full article text (not just RSS summary) for better classification |
| **Cross-source threshold** | `2` | Minimum number of sources covering a theme to boost its ranking |

---

## Feed Health

> Auto-updated by the feed curator. Tracks which sources are working and which need attention.

| Source | Last Fetched | Articles Found | Status |
|--------|-------------|----------------|--------|
| GitHub Blog | 2026-06-19 | 6 | ok |
| Deeplearning AI Batch | 2026-06-19 | 20 | ok |
| Towards Data Science (Medium) | 2026-06-19 | 20 | ok |
| PostgreSQL weekly | 2026-06-19 | 6 | ok |
| Simon Willison's Weblog | 2026-06-19 | 23 | ok |
| TLDR AI | 2026-06-19 | 2 | ok |
| InfoQ | 2026-06-19 | 15 | ok |
