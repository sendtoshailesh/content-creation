# Visual Taxonomy Reference

This taxonomy defines the approved visual families for the mandatory visual editorial system.

## First-Milestone Families

| Visual family | Best for | Primary audience | Primary platforms | Renderer |
|---|---|---|---|---|
| Architecture / flow diagram | Systems, agent workflows, API/data flow, governance loops | Practitioners, platform engineers | Blog, LinkedIn, Medium/LinkedIn Article | Mermaid (Graphviz/DOT for dense) |
| Infographic / one-pager | Saveable summaries, key metrics, checklists, frameworks | Practitioners, decision-makers | Blog, LinkedIn, Substack Note | HTML/CSS + Chromium |
| Comic explainer / storyboard | Human scenarios, failure stories, before/after behavior, memorable analogies | Broad technical audience | Blog, LinkedIn | HTML/CSS + Chromium (text); SVG/CSS shapes |
| LinkedIn social card pack | Swipeable framework, checklist, teardown, or narrative sequence | Practitioners | LinkedIn | HTML/CSS + Chromium |
| Executive exhibit | ROI, risk, cost, operational decision-making, evidence | Leaders, decision-makers | Blog, LinkedIn Article, Medium | matplotlib; JS bridge (ECharts) for advanced charts |
| AI-generated imagery (hero/illustrative) | Hero/backdrop shots, scene-setting, conceptual illustration, mood — never data | Broad audience | Blog hero, LinkedIn, Medium/Substack hero | `scripts.visuals.generated` (AI image model) |

## Follow-On Families

| Visual family | Use later when |
|---|---|
| Visual essay | The content needs a long narrative arc across 5-8 images |
| Editorial cartoon | The content has a sharp opinion or industry critique |
| Teardown poster | A flawed system or workflow needs annotated diagnosis |
| Interactive visual | GitHub Pages needs interactive HTML/SVG beyond static assets |

## Format Selection Rules

- Choose architecture / flow diagrams when the reader needs to understand structure or sequence.
- Choose infographics / one-pagers when the reader should save and reuse the idea.
- Choose comic/storyboards when the insight depends on human behavior, failure modes, or a before/after moment.
- Choose LinkedIn card packs when the asset is meant to drive dwell time and saves.
- Choose executive exhibits when the message is a decision, risk, cost, ROI, or leadership trade-off.
- Choose AI-generated imagery **only** for hero/backdrop/scene/illustration slots that carry mood, not information. It is gated behind `image_generation: on`, must contain **no embedded text**, must honor brand colors, and goes through `image-content-agent` + `vision-grounding`. Never use it for diagrams, charts, infographics, or exhibits.

## Anti-Patterns

- Do not use a carousel for every topic.
- Do not use a comic when the concept requires precise architecture.
- Do not use an executive exhibit for emotional storytelling.
- Do not use an infographic as a dumping ground for every section.
- Do not use AI-generated imagery for any data-bearing or structural visual (diagram, chart, infographic, exhibit); it is for mood/hero/illustration only, and must never contain embedded text.
- Do not render any data-bearing visual without a visible source line.

