# Reel Script — You Don't Need 50 MCP Servers

**Duration**: 60 seconds (primary) · 90 seconds (LinkedIn extended cut — see addendum)
**Format**: D — Hot Take / Contrarian Opener
**Platforms**: Instagram Reels, YouTube Shorts, LinkedIn Video
**Aspect ratio**: 9:16 (1080 × 1920)
**Target audience**: Developers using Claude Code, Cursor, Copilot, or Windsurf
**Core message**: You don't need 50 MCP servers. You need 3 that remove one daily bottleneck.

---

## Shot List — 60-Second Cut (Instagram Reels / YouTube Shorts)

| Time     | Visual                                                                                                                                    | Voiceover                                                                                                                       | Text Overlay                          |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| 0:00–0:04 | **Motion graphic** — dark background, bold white phrase `50 MCP servers?` hard-cuts to `3` in accent colour (electric blue or amber) | *"You don't need fifty MCP servers. You need three."*                                                                            | `Don't install 50. Install 3.`        |
| 0:04–0:10 | **Screen recording** — VS Code 1.101+ Settings panel, zoomed to MCP Servers section; cursor clicks "Add Server", types a remote URL; browser OAuth popup appears and user clicks "Authorize" | *"Here's why: in 2026, remote MCP finally got real. VS Code 1.101 connects to any remote server with one OAuth click — no config files, no tokens living in plaintext JSON."* | `2026: One click. No config files.`   |
| 0:10–0:15 | **Split-screen graphic** — left: old four-step flow (JSON block → PAT copy → gitignore → repeat × 3 machines); right: new single OAuth popup. Annotate "Before: 4 steps" and "After: 1 click" | *"Old setup? Four manual steps per service. Secrets you hoped weren't in a git commit. Now? One browser popup."*                | `Before: 4 steps → After: 1 click`   |
| 0:15–0:24 | **Screen recording** — GitHub MCP connected in VS Code; agent chat visible; user types "summarise open PRs against the v2 milestone"; agent returns a real PR list with authors and status | *"GitHub MCP — first-party from GitHub, version 1.1.0, OAuth-ready. Summarise PRs, search issues, trigger Actions runs — without leaving your IDE."* | `GitHub MCP → PRs, issues, Actions`   |
| 0:24–0:36 | **Screen recording** — Playwright MCP terminal startup (`npx @playwright/mcp@latest`), then agent navigating to a broken checkout page, taking a screenshot, and generating a `test.spec.ts` file | *"Playwright MCP — describe a UI bug, the agent navigates to it, screenshots the failure, and writes the Playwright test. That loop used to take twenty to forty minutes. Now it's under five."* | `Playwright MCP → 20–40 min → under 5`  |
| 0:36–0:45 | **Screen recording** — agent chat; user asks about a library method; Context7 tool call fires and returns versioned docs inline in the conversation; hallucination-free answer rendered | *"Context7 — live doc grounding. No more agents hallucinating stale API signatures. It fetches real, version-specific docs on every call."* | `Context7 → live docs. No guessing.` |
| 0:45–0:53 | **Screen recording** — GitHub MCP OAuth scope selection screen; cursor deliberately unchecks write permissions; only read-only repo and issues boxes remain checked | *"One security caveat: be ruthless about OAuth scopes. Start read-only on everything. Write access comes later — after you've actually tested the agent's judgment."* | `Security: start read-only. Always.`  |
| 0:53–1:00 | **Motion graphic** — same dark bg as opener; text reads "Full guide — 10 servers + threat model" with arrow pointing down; follow / subscribe icon pulses | *"Full breakdown of all ten servers plus the security threat model — link in bio."*                                              | `Full guide → link in bio 🔗`         |

---

## Screen Recording Notes

### Tools to have open
- **VS Code 1.101+** — open to Settings → MCP Servers panel
- **Browser (Chrome)** — staged GitHub OAuth popup ready to authorize
- **Terminal** — `npx @playwright/mcp@latest` already running, output visible
- **Agent chat window** (Claude Code / Cursor) — connected to GitHub MCP and Context7

### Settings to make visible
- VS Code MCP panel: at least one remote server already connected (GitHub MCP) so the workflow looks real, not empty
- Terminal: zoom to 140 % font size so `npx @playwright/mcp@latest` reads clearly at 1080 p vertical
- Agent chat: increase chat font size; hide sidebar panels that aren't relevant

### Zoom guidance
- **0:04–0:10**: zoom to the right half of VS Code (the MCP Servers panel + browser popup only — cut out any distracting file tree)
- **0:15–0:24**: zoom to the chat input and the agent's PR list response; hide the repo file explorer
- **0:24–0:36**: first zoom to the terminal startup (3 seconds), then hard-cut to the agent chat + screenshot thumbnail side-by-side; zoom to the generated `test.spec.ts` tab
- **0:36–0:45**: zoom to the agent chat message thread only; the Context7 tool call result should be fully readable on screen
- **0:45–0:53**: zoom to the OAuth scope checkbox panel in the browser; cursor moves deliberately — no rushed clicking

### Actions to perform (in order)
1. Open VS Code 1.101+ → Settings → MCP Servers → "Add Server" → type GitHub MCP remote URL → OAuth popup appears → click "Authorize"
2. In agent chat: type `"summarise open PRs against the v2 milestone"` → scroll to show 2–3 real PR results
3. In terminal: show `npx @playwright/mcp@latest` startup output (3–4 lines)
4. In agent chat: show the Playwright screenshot result (broken checkout page) + generated test file in a split or tab-switch
5. In agent chat: type a library method question → show Context7 tool call firing + versioned docs returned
6. In browser: navigate to GitHub MCP OAuth scope screen → uncheck write permissions, keep read-only boxes

---

## Voiceover Script — 60-Second Cut (Full, Word-for-Word)

> Delivery notes: conversational, slightly fast, developer-to-developer energy. No corporate announcer voice. Treat the numbered servers like you're rattling them off to a friend. Breathe naturally on the em-dashes — those are your pause moments.

---

**[0:00–0:04]**
"You don't need fifty MCP servers. You need three."

**[0:04–0:10]**
"Here's why: in 2026, remote MCP finally got real. VS Code 1.101 connects to any remote server with one OAuth click — no config files, no tokens living in plaintext JSON."

**[0:10–0:15]**
"Old setup? Four manual steps per service. Secrets you hoped weren't in a git commit. Now? One browser popup."

**[0:15–0:24]**
"GitHub MCP — first-party from GitHub, version 1.1.0, OAuth-ready. Summarise PRs, search issues, trigger Actions runs — without leaving your IDE."

**[0:24–0:36]**
"Playwright MCP — describe a UI bug, the agent navigates to it, screenshots the failure, and writes the Playwright test. That loop used to take twenty to forty minutes. Now it's under five."

**[0:36–0:45]**
"Context7 — live doc grounding. No more agents hallucinating stale API signatures. It fetches real, version-specific docs on every call."

**[0:45–0:53]**
"One security caveat: be ruthless about OAuth scopes. Start read-only on everything. Write access comes later — after you've actually tested the agent's judgment."

**[0:53–1:00]**
"Full breakdown of all ten servers plus the security threat model — link in bio."

---

**Word count: ~144 words · Estimated delivery at 145 wpm conversational pace: 59–61 seconds ✓**

---

## LinkedIn Extended Cut — Addendum (add after 0:53, extend to ~90 seconds)

> Replace the 0:53–1:00 CTA with the block below. The main 60-second body stays identical.

### Extra Shot List (0:53–1:30)

| Time       | Visual                                                                                                                              | Voiceover                                                                                                                                                                                       | Text Overlay                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| 0:53–1:04  | **Screen recording** — agent chat; a GitHub issue contains a suspicious instruction inside its body text; approval flow dialog fires before the agent acts | *"One more thing: prompt injection is real. An attacker can embed tool instructions inside a GitHub issue or a database row your agent reads. Enable approval flows in your IDE — require a manual confirm before any write or destructive action."* | `Prompt injection is real. Enable approvals.` |
| 1:04–1:15  | **Graphic** — three-column stack map: Repo stack (Filesystem + Git + GitHub MCP) · Debug stack (Playwright + Fetch) · Docs stack (Context7 + Memory) | *"And pick one loop to start with. Repo work, browser debugging, or docs lookup. Install the smallest stack that removes one tab-hop from that loop this week."*                                | `Pick one loop. Install one stack.`       |
| 1:15–1:25  | **Motion graphic** — same dark bg as opener; "Full guide" text appears; URL hint visible | *"Full guide — ten servers, ranking rubric, three build projects, and the threat model most MCP lists skip — link below."*                                                                      | `Full guide → link below 🔗`             |
| 1:25–1:30  | **Engagement prompt graphic** — text on screen only                                                                                 | *"What's the one daily loop you'd most want to remove? Drop it in the comments."*                                                                                                               | `What loop do you want to remove? 👇`    |

### Extended Voiceover (0:53–1:30, word-for-word)

**[0:53–1:04]**
"One more thing: prompt injection is real. An attacker can embed tool instructions inside a GitHub issue or a database row your agent reads. Enable approval flows in your IDE — require a manual confirm before any write or destructive action runs."

**[1:04–1:15]**
"And pick one loop to start with. Repo work, browser debugging, or docs lookup. Install the smallest stack that removes one tab-hop from that loop this week."

**[1:15–1:25]**
"Full guide — ten servers, ranking rubric, three build projects, and the threat model most MCP lists skip — link below."

**[1:25–1:30]**
"What's the one daily loop you'd most want to remove? Drop it in the comments."

> **LinkedIn word count (full script): ~218 words · Estimated delivery: 88–92 seconds ✓**

---

## Captions & Hashtags

### Instagram Reels / YouTube Shorts

```text
START
You don't need 50 MCP servers. You need 3 that remove one daily bottleneck.

In 2026, remote MCP changed how developers set this up — VS Code 1.101+ connects via OAuth in one click. No config files. No plaintext tokens.

The 3 that actually matter:
→ GitHub MCP (v1.1.0) — PRs, issues, Actions from your IDE
→ Playwright MCP — bug → screenshot → failing test in under 5 min
→ Context7 — live, versioned docs so your agent stops hallucinating APIs

Security caveat: start read-only on every OAuth scope. Always.

Full breakdown of all 10 servers + the threat model most lists bury → link in bio.

#MCPServers #AIDevTools #ClaudeCode #CursorAI #DeveloperTools #AgenticIDE #GitHubMCP #PlaywrightMCP #RemoteMCP #DevProductivity #SoftwareDevelopment #AITools2026
END
```

### LinkedIn Video

```text
START
Most MCP server lists are already stale.

Here's what changed in 2026: remote MCP went from experiment to vendor-backed developer infrastructure. VS Code 1.101+ connects to remote endpoints with a single OAuth flow — no personal access tokens in plaintext JSON config files, no .gitignore workarounds.

For a team of 5 using 3 MCP-connected services, that shift goes from 60 individual manual steps to 15 browser-authorization clicks.

The three servers worth your attention first:

1. GitHub MCP (v1.1.0, first-party) — summarise PRs, search issues, trigger workflow runs from your agentic IDE
2. Playwright MCP (Microsoft, first-party) — describe a UI bug, get a screenshot + Playwright test in under 5 minutes instead of 20–40
3. Context7 — live doc grounding so your agent stops hallucinating outdated API signatures

One non-negotiable: start every remote server on read-only OAuth scopes. Prompt injection is real — an attacker can embed tool instructions in a GitHub issue or database row your agent reads. Approval flows before any write action are mandatory, not optional.

Full guide — 10 servers ranked on a defensible rubric (not GitHub stars), three starter stacks by workflow, three build projects, and the full security threat model — link in the first comment.

What's the daily developer loop you'd most want to hand off to an agent? Let me know below.

#MCPServers #DeveloperTools #AIEngineering #AgenticIDE #RemoteMCP #GitHubMCP #PlaywrightMCP #Context7 #DevProductivity #SoftwareDevelopment #AITools #ClaudeCode #CursorAI
END
```

---

## Thumbnail / Cover Frame Description

**Concept**: High-contrast dark background (near-black `#0D0D0D`). Two elements only:

1. **Top two-thirds**: Large, bold, sans-serif (Helvetica Neue Heavy or equivalent) white text reading:
   ```
   You need
   3 MCP servers.
   ```
   The number `3` should be rendered in electric blue (`#3B82F6`) or bright amber (`#F59E0B`) — whichever aligns with brand tokens. No other colour on the frame.

2. **Bottom third**: Three small pill-shaped labels in a horizontal row, each containing a single server name in monospace font:
   ```
   [ github-mcp ]   [ playwright-mcp ]   [ context7 ]
   ```
   Pills: dark-grey fill (`#1E1E1E`), 1 px white border, white monospace text. Spacing even. No icons, no logos — text only for clarity at small sizes.

**No face, no stock image, no gradient backgrounds.** The thumbnail must be readable at 100 × 100 px (the minimum Instagram grid preview size).

---

## Music & Pacing Notes

### Vibe
Upbeat, slightly urgent, technical — think the kind of background track used in developer tool launch videos or fast-cut coding tutorials. Not a hype-drop, not lofi-chill. Something with a consistent forward momentum that doesn't compete with the voiceover.

**Describe to a music tool / royalty-free library**: *"Fast-tempo electronic instrumental with punchy synth hits, around 120–130 BPM, minimal vocals, clean mid-range so spoken word sits on top without muddying. Energetic but not chaotic. Think 'product reveal' rather than 'gaming montage'."*

### Pacing & Transition Cues

| Cue Point     | Timing    | Action                                                                                  |
|---------------|-----------|-----------------------------------------------------------------------------------------|
| Hard cut      | 0:04      | `50 MCP servers?` → `3` graphic slash; sync with a single sharp synth hit              |
| Quick cut     | 0:10      | Split-screen before/after appears; music tempo feel tightens slightly                   |
| Jump cut ×3   | 0:15, 0:24, 0:36 | Each server intro: fast cut to new screen recording; these three cuts should feel rhythmic and evenly spaced — like a countdown |
| Dramatic pause | 0:32–0:34 | Voiceover lands "forty minutes" — let the music drop very slightly here before the "now it's under five" line hits. This is the single biggest wow moment; give it half a second of space. |
| Tone shift    | 0:45      | Security caveat section: music stays same tempo but slightly lower mix volume — signals the "important" register without feeling like a buzzkill |
| Music swell   | 0:53      | CTA card; music back to full volume for the final 7 seconds                             |

### Text Overlay Timing
- Each overlay stays on screen for its full shot duration
- Use a fast fade-in (3–4 frames) with no fade-out — cut hard with the next shot
- Font: bold, uppercase or mixed-case depending on brand tokens; recommended weight ≥ 700
- Stroke / drop shadow: 2 px black outline so text reads on any screen recording background

---

## Production Checklist

- [ ] Record VS Code screen at 1080 × 1920 native (or record 1920 × 1080 and reframe to 9:16 — letterbox the screen recording in the upper 70% of the frame, leave room for text overlays at bottom)
- [ ] Close notifications, disable system alerts before recording
- [ ] Use a real repository with real data for GitHub MCP demo — fabricated PR lists are obvious
- [ ] Playwright MCP demo: use a simple localhost app, not a production URL
- [ ] Context7 demo: pick a library with a recent breaking API change (e.g. a Node.js or React recent release) so the "live docs" value is visually clear
- [ ] Review OAuth scope screenshot for any personally identifying information (account name, email) — blur or crop if visible
- [ ] Caption file: export `.srt` auto-captions and manually review for "MCP", "OAuth", "Playwright", "Context7" — auto-captioners frequently mis-transcribe these terms
- [ ] Post time: Tuesday or Wednesday, 9–11 AM in the primary audience's time zone (engineering audiences on LinkedIn peak mid-morning weekdays; Reels/Shorts are more time-agnostic)

---

## Source Notes

- GitHub MCP Server — https://github.com/github/github-mcp-server
- Playwright MCP — https://github.com/microsoft/playwright-mcp
- Context7 — https://github.com/upstash/context7
- Supabase MCP security guidance — https://github.com/supabase/mcp/blob/main/README.md
- MCP spec / ToolAnnotations — https://modelcontextprotocol.io/specification/2025-03-26/server/tools#toolannotations

---

*Script version: 1.0 · Created: 2026-06-28 · Topic workspace: `content/topics/mcp-servers-2026/` · Source: `blog.md`, `creative-brief.md`, `strategy.md`*
