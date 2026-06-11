---
description: "Run the content pipeline scoped to a single topic workspace under content/topics/<slug>/. Use to create content for one of the configured topics (postgresql, agentic-ai, ai-general, machine-learning, python, azure-ms-ai, ai-native-dev, cloud-databases)."
agent: "content-pipeline"
argument-hint: "Provide the topic slug (e.g. postgresql) — see content/topics/README.md"
---

# Topic-scoped content pipeline

Run the full content pipeline for **one topic workspace**. The argument is a topic slug from
`content/topics/README.md`.

## Topic scoping (do this first)

1. Resolve the topic slug to its workspace `content/topics/<slug>/`. If the slug is missing or
   unknown, read `content/topics/README.md`, list the available topics, and ask which one.
2. **Use the topic workspace files in place of the root ones for this run:**
   - Config: `content/topics/<slug>/pipeline-config.md` (instead of `content/pipeline-config.md`)
   - Feed sources: `content/topics/<slug>/feed-sources.md`
   - Idea queue: `content/topics/<slug>/idea-queue.md`
   - **All outputs** (blog, visuals, social, briefs) go under `content/topics/<slug>/` (use a
     `visuals/` subfolder there), NOT the repo-root `content/`.
3. Read the topic config's **Pipeline Status** and resume/start exactly as the
   `content-pipeline` orchestrator normally does, but scoped to this workspace.

## Then run the standard pipeline

Follow the normal `content-pipeline` orchestration (creative brief → strategy → scope →
dimensions → visual map → blog → visuals → reviews → distribution), reading the seeded
`idea-queue.md` candidates as starting material. If the queue holds only raw candidates
(not yet scored), run `@feed-curator` scoped to this workspace first to synthesize ranked ideas.

Topics are independent — running this for one slug must not touch another topic's workspace or
the repo-root `content/` files.
