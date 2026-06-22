# Topic Pipelines

> Each topic has an isolated content pipeline workspace. Run a topic with
> `/topic-pipeline <slug>` or `@content-pipeline` after `cd`-ing your focus to the
> topic folder. Idea queues are seeded from your Apple Notes + Chrome bookmarks.

Last scaffolded: 2026-06-11 via `scripts/pipeline/scaffold_topics.py`.

| Topic | Slug | Seeded candidates | Status | Links |
|-------|------|-------------------|--------|-------|
| PostgreSQL | `postgresql` | 97 | `not-started` | [config](./postgresql/pipeline-config.md) · [ideas](./postgresql/idea-queue.md) |
| Agentic AI | `agentic-ai` | 45 | `not-started` | [config](./agentic-ai/pipeline-config.md) · [ideas](./agentic-ai/idea-queue.md) |
| AI (general) | `ai-general` | 72 | `not-started` | [config](./ai-general/pipeline-config.md) · [ideas](./ai-general/idea-queue.md) |
| Machine Learning | `machine-learning` | 26 | `not-started` | [config](./machine-learning/pipeline-config.md) · [ideas](./machine-learning/idea-queue.md) |
| Python | `python` | 35 | `not-started` | [config](./python/pipeline-config.md) · [ideas](./python/idea-queue.md) |
| Azure / Microsoft AI | `azure-ms-ai` | 49 | `not-started` | [config](./azure-ms-ai/pipeline-config.md) · [ideas](./azure-ms-ai/idea-queue.md) |
| AI-native software development | `ai-native-dev` | 15 | `not-started` | [config](./ai-native-dev/pipeline-config.md) · [ideas](./ai-native-dev/idea-queue.md) |
| Cloud databases | `cloud-databases` | 229 | `not-started` | [config](./cloud-databases/pipeline-config.md) · [ideas](./cloud-databases/idea-queue.md) |

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
