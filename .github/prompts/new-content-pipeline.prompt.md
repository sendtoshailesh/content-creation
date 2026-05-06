---
description: "Start a new content pipeline run. Kicks off the full content strategy pipeline for a given technical topic — from clarifying questions through to distribution."
agent: "content-pipeline"
argument-hint: "Provide the technical topic to create content about"
---

Start a new content pipeline run for the given topic. Follow the pipeline:

1. **Clarify** — Ask 8-12 targeted questions about the topic, audience, and goals
2. **Strategize** — Produce a content strategy document and distribution-aware outline
3. **Scope Assessment** — Evaluate comprehensiveness: single post vs. multi-part series
4. **Dimension Analysis** — Analyze topic across persona, best practice, and Azure WAF pillar dimensions to shape series structure and social angles
5. **Write** — Create the long-form blog post (~3,000 words per part) with concrete data
6. **Visualize** — Generate all visual assets (PNGs, SVGs, Mermaid diagrams)
7. **Review** — Audit content and visuals against quality standards
8. **LinkedIn** — Create plain-text and Unicode-formatted LinkedIn posts (always)
9. **Platform Selection** — Ask which additional platforms to generate for:
   - X/Twitter thread (10-12 tweets)
   - Reddit post (Markdown)
   - Reel/Short video (60-90 sec screen + voiceover script)
   - YouTube long-form script (8-12 min)
10. **Generate selected platforms** — Run only the chosen agents
11. **Brand audit** — Review all content for consistency

For multi-part series: complete Part 1 through the full pipeline before starting Part 2.

Save all output to the `content/` directory. Use `content/visuals/` for visual assets.

After each step, briefly confirm completion before proceeding to the next.
