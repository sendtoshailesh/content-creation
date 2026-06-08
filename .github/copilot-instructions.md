# Content Strategy Pipeline — Workspace Instructions

## Project Purpose

This workspace automates a content strategy pipeline that takes a technical topic and produces a full distribution package: long-form blog (single post or multi-part series), social posts (LinkedIn + user-selected platforms), reel/short video scripts, and YouTube scripts.

### Key Pipeline Features

- **Comprehensiveness detection**: After strategy/outline creation, the pipeline assesses whether a topic is too broad for a single post and recommends a multi-part series when appropriate (based on pillar count, data density, audience breadth, and technical depth)
- **Multi-dimensional analysis**: Topics are analyzed across three dimension types — persona (developer, tech lead, manager), best practices (technology + governance), and Azure Well-Architected Framework pillars (Cost, Ops Excellence, Performance, Reliability, Security) — to inform series structure and social distribution angles
- **Multi-part series support**: Topics scoring 11+ on comprehensiveness (0-16 scale) are split into a series where each part runs through the full pipeline independently, with dimension-aligned part boundaries
- **Social platform selection**: LinkedIn is always generated; other platforms (X/Twitter, Reddit, Reel/Short video, YouTube) are user-selected after LinkedIn
- **Reel/Short video**: 60-90 second scripts with screen recording cues and voiceover narration for Instagram Reels, YouTube Shorts, and LinkedIn Video

## Folder Structure

```
content/                          # All generated content
  ├── *.md                        # Blog, social posts, scripts
  └── visuals/                    # PNGs, SVGs, Mermaid files, Python renderers
agents-and-skills/                # Pipeline documentation and agent definitions
.github/                          # Copilot customization (agents, skills, instructions, prompts)
```

## Design Tokens (Visual Assets)

All visual assets must use this shared token system:

| Token | Hex | Usage |
|-------|-----|-------|
| BG | `#ffffff` | Background |
| ACCENT | `#1f6feb` | Primary accent (blue) |
| ACCENT_2 | `#0d9488` | Secondary accent (teal) |
| ACCENT_3 | `#7c3aed` | Tertiary accent (purple) |
| WARN | `#dc2626` | Warning/attention (red) |
| SUCCESS | `#16a34a` | Positive indicator (green) |
| TEXT | `#1e293b` | Primary text |
| TEXT_2 | `#475569` | Secondary text |
| MUTED | `#94a3b8` | Muted text/borders |
| GRID | `#e5e7eb` | Grid lines/dividers |
| LIGHT_BG | `#f8fafc` | Card/panel background |
| BLUE_BG | `#dbeafe` | Blue highlight region |
| TEAL_BG | `#ccfbf1` | Teal highlight region |
| PURPLE_BG | `#ede9fe` | Purple highlight region |
| RED_BG | `#fee2e2` | Red/warning highlight region |

- **Font**: Helvetica Neue
- **DPI**: 320 for all PNG output
- **No Unicode glyphs** (→, ✓, ✗) in matplotlib — use ASCII equivalents (`->`, `[x]`, `[ ]`)
- **SVGs**: Generate via Python scripts, never terminal heredoc

## Content Quality Bar

- Every claim needs a concrete number, model name, or benchmark
- Use real pricing data, not placeholders
- Include at least one case study with before/after metrics
- All visuals must share the design token palette and typography
- No vague generalities — specific, actionable advice

## Tone & Voice

- First-person perspective: "sharing my learnings working with customers"
- Never corporate/Series-B/fundraising framing
- Conversational but data-driven
- Lead with problems/insights, not "I wrote a blog"

## Pipeline Configuration

Before starting a content run, edit `content/pipeline-config.md` to set:
- **Reference URLs**: Online sources (articles, pricing pages, research papers) that agents will fetch, analyze, and synthesize into `content/reference-brief.md` before writing begins
- **Model preferences**: The pipeline auto-detects which model family you're using (documented in config; actual model is selected via the VS Code model picker)
- **Output preferences**: Blog length, social platform targets, subreddits, YouTube duration

Select any model in the VS Code Copilot model picker — all agents inherit your selection. Review gates use GitHub Copilot's rubber-duck review feature, so the pipeline does not ask you to switch model families before quality review.

## Social Formatting Conventions

- **LinkedIn / X/Twitter**: Unicode Mathematical Bold Sans-Serif (𝗕𝗼𝗹𝗱) and Italic Sans-Serif (𝘐𝘵𝘢𝘭𝘪𝘤) for native formatting
- **Reddit**: Standard Markdown only (Reddit's native format). No Unicode bold/italic
- All social posts must be copy-paste ready

## Social Formatting Conventions

- **LinkedIn / X/Twitter**: Unicode Mathematical Bold Sans-Serif (𝗕𝗼𝗹𝗱) and Italic Sans-Serif (𝘐𝘵𝘢𝘭𝘪𝘤) for native formatting
- **Reddit**: Standard Markdown only (Reddit's native format). No Unicode bold/italic
- All social posts must be copy-paste ready
