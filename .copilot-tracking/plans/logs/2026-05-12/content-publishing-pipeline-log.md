# Planning Log — Content Publishing Pipeline Redesign

## Session: 2026-05-12

---

## Research Phase (completed before this log)

| Item | Status | Notes |
|------|--------|-------|
| Repo structure exploration | ✅ Done | Full content/, docs/, agents-and-skills/, .github/agents/ |
| pipeline-config.md analysis | ✅ Done | Step 10 done; [link] placeholders unresolved; no Medium/Substack/LinkedIn Article |
| GitHub Pages URL pattern confirmed | ✅ Done | `https://sendtoshailesh.github.io/blog/{slug}.html` |
| Social post gap analysis | ✅ Done | [link] never resolved; image posting notes in X/Twitter files |
| Agent inventory | ✅ Done | No platform-distiller exists; web-publisher and social-publisher need updates |
| Platform algorithm research | ✅ Done | X/Twitter suppression, LinkedIn suppression, Reddit text post, Medium Import canonical, Substack no canonical |
| User clarifications | ✅ Done | Retroactive + forward; active Substack; series index primary + individual parts secondary |
| Approach selected | ✅ Done | Scenario B: Refactor Publishing Stage |

---

## Planning Phase

| Item | Status | Notes |
|------|--------|-------|
| Plan file created | ✅ Done | `.copilot-tracking/plans/2026-05-12/content-publishing-pipeline-plan.instructions.md` |
| Details file created | ✅ Done | `.copilot-tracking/details/2026-05-12/content-publishing-pipeline-details.md` |
| Planning log created | ✅ Done | This file |
| Plan Validator run | ⬜ Pending | Run after user approves plan |

---

## Implementation Tracking

### Phase 1: Infrastructure (create new files)

| Task | File | Status | Notes |
|------|------|--------|-------|
| 1.1 Create publishing-log.md | `content/publishing-log.md` | ⬜ Pending | Template + back-fill 3-part series URLs |
| 1.2 Create platform-distiller agent | `.github/agents/platform-distiller.agent.md` | ⬜ Pending | New Step 12 agent |
| 1.3 Create series index page | `sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html` | ⬜ Pending | Hub page; primary social sharing URL |

### Phase 2: Agent Updates

| Task | File | Status | Notes |
|------|------|--------|-------|
| 2.1 web-publisher: write canonical URL | `.github/agents/web-publisher.agent.md` | ⬜ Pending | Add Step 5 to publishing sequence |
| 2.2 social-publisher: URL injection + text-only + link placement | `.github/agents/social-publisher.agent.md` | ⬜ Pending | 4 enforcement changes |
| 2.3 Agent registry: add platform-distiller | `agents-and-skills/*.md` | ⬜ Pending | Step 12 entry |

### Phase 3: Config Updates

| Task | File | Status | Notes |
|------|------|--------|-------|
| 3.1 pipeline-config.md: 5 additions | `content/pipeline-config.md` | ⬜ Pending | Platforms, canonical URL, steps, publish sequence, URLs table |

### Phase 4: Retroactive Content

| Task | File | Status | Notes |
|------|------|--------|-------|
| 4.1 Back-fill publishing-log.md | `content/publishing-log.md` | ⬜ Pending | All 3 parts already live on GitHub Pages |
| 4.2 Fix [link] in existing social posts | Various `content/*.md` | ⬜ Pending | Replace with actual canonical URLs |
| 4.2 Remove image notes from X/Twitter | `content/x-twitter-thread.md` | ⬜ Pending | Remove "Attach image" guidance |
| 4.3 Generate Medium summaries | `content/medium-post-part{1,2,3}.md` | ⬜ Pending | 700–900 words each |
| 4.3 Generate Substack excerpts | `content/substack-post-part{1,2,3}.md` | ⬜ Pending | 300–500 words each |
| 4.3 Generate LinkedIn Articles | `content/linkedin-article-part{1,2,3}.md` | ⬜ Pending | 700–900 words, unique angle each |

### Phase 5: Validation

| Check | Status | Notes |
|-------|--------|-------|
| No image refs in platform summaries | ⬜ Pending | Grep for ![, .png, .svg, <img |
| No remaining [link] placeholders | ⬜ Pending | Grep content/*.md |
| publishing-log.md has all 3 parts | ⬜ Pending | |
| Series index page renders | ⬜ Pending | Visual check |
| pipeline-config.md has Step 10a and 12 | ⬜ Pending | |
| All platform outputs have START/END COPY markers | ⬜ Pending | |

---

## Decisions Log

| Decision | Rationale | Date |
|----------|-----------|------|
| Scenario B (Refactor Publishing Stage) over Scenario A (wrapper agent) | Cleaner step separation; easier to debug and maintain; social-publisher handles URL injection as pre-flight | 2026-05-12 |
| Series index as primary social sharing URL | Builds topical authority; all 3 parts get traffic from one shareable link | 2026-05-12 |
| Substack: excerpt only (300–500 words) | Substack has no canonical URL protection; full republish risks Google duplicate content penalty | 2026-05-12 |
| LinkedIn Article: unique angle, not republish | Google indexes LinkedIn Articles; exact republish causes duplicate content penalty | 2026-05-12 |
| X/Twitter: link in last tweet only | External links in early tweets cause 50–90% algorithmic reach suppression on X/Twitter | 2026-05-12 |
| Medium: Import tool only, never paste | Import tool auto-sets canonical URL to GitHub Pages source; preserves SEO attribution | 2026-05-12 |

---

## Risks and Mitigations

| Risk | Mitigation |
|------|-----------|
| Substack full republish causes duplicate content penalty | Excerpt-only instruction enforced in platform-distiller agent prompt |
| X/Twitter image attachment suppresses non-follower reach | Remove image guidance from social-publisher; text-only instruction added |
| LinkedIn Article republish cannibalizes blog SEO | Unique angle requirement enforced in platform-distiller; agent explicitly forbids blog recap structure |
| [link] placeholders go un-replaced if web-publisher doesn't write publishing-log.md | Step 10a explicitly reads publishing-log.md first; fails loudly if file missing |
