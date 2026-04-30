---
description: "Search the web and curate references for the content pipeline. Discovers high-quality sources across 6 categories (general, benchmarks, competitor articles, docs, case studies, research papers) and lets you select which to keep."
agent: "reference-discovery"
argument-hint: "Provide the topic or search terms to discover references for"
---

Discover and curate web references for the content pipeline topic.

1. **Search** — Generate targeted queries across 6 reference categories
2. **Present** — Show results grouped by category with titles, URLs, and snippets
3. **Curate** — Select which references to keep (by number) or reject
4. **Save** — Write accepted references into `content/pipeline-config.md`

Uses Azure Bing Web Search API for structured results. Falls back to web search if API key is not configured.
