---
description: 'Select a content idea from the idea queue and auto-populate pipeline-config.md to start a new content pipeline run. Use when you have curated ideas in the queue and want to turn one into a full content piece.'
mode: 'agent'
---

# Select Idea for Content Pipeline

Read the idea queue and help the user pick an idea to create content from.

## Steps

1. Read `content/idea-queue.md` and list all ideas with status `queued`
2. If the queue is empty, suggest running `@feed-curator` first to discover ideas
3. Present each queued idea in a compact format:
   ```
   [1] Idea Title (Score: X/25)
       Subjects: AI, Architecture | Sources: N articles
       Angle: Brief content angle
   ```
4. Ask: "Which idea would you like to create content for? Reply with the number."
5. When the user picks an idea:
   a. Read `content/pipeline-config.md`
   b. Check if Pipeline Status is `in-progress` — if so, warn the user and ask to confirm (they may need to archive first)
   c. Reset the Pipeline Status:
      - Status: `not-started`
      - Topic: idea title + content angle
      - Started: _(empty)_
      - Current Step: _(empty)_
      - Uncheck all steps in the Step Checklist
   d. Populate Reference URLs with the idea's source article URLs under appropriate categories
   e. Update the idea's status in `content/idea-queue.md` from `queued` to `selected`
   f. Confirm: "Pipeline configured with '[topic]'. Run `@content-pipeline` to start."
