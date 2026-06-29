---
seo:
  title: "10 Best Free MCP Servers for Developers (2026)"
  description: "Best free MCP servers ranked by workflow value, security posture, and real free-tier utility. Covers GitHub, Playwright, Filesystem, Supabase, and 6 more."
  slug: "best-free-mcp-servers"
  keywords:
    primary: "best free MCP servers"
    secondary:
      - "MCP server list 2026"
      - "remote MCP server setup"
      - "model context protocol servers"
      - "MCP server security"
      - "free MCP servers for developers"
---

# 10 Best Free MCP Servers for Developers in 2026

*Published: 2026-06-28 · ~3,000 words · First-person practitioner field guide*

---

## MCP is No Longer a Hobbyist Sidecar

Twelve months ago, wiring up an MCP server meant editing a JSON config file, generating a personal access token, and hoping the community repo you found hadn't been abandoned since the demo video. Today, GitHub ships a [first-party MCP server at v1.1.0](https://github.com/github/github-mcp-server) with remote OAuth support, VS Code 1.101+ connects to remote MCP endpoints natively without touching a config file, and Cloudflare maintains a suite covering 13 of their own services under a single remote endpoint. The protocol itself has a stable Streamable HTTP transport nailed down in [spec version 2025-03-26](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#toolannotations).

That's the shift that makes most existing MCP lists stale: they were written when "remote MCP" was an experiment and vendor-maintained servers were rare. Today the best servers come from the teams that own the platforms — they move fast, document security boundaries, and don't disappear after a conference talk.

But that also means the catalog has exploded. I've spent the last several months watching which servers actually compress a dev loop versus which ones just look good in a demo. Here's my honest field guide.

> **TL;DR for time-poor scanners:** If you install only three things this week, make it **GitHub MCP + Playwright MCP + MCP Filesystem**. That stack covers the three loops most developers repeat daily — repo/PR work, browser debugging, and local file context — with low setup friction and clear trust boundaries. Everything else on this list is additive.

---

## The Ranking Rubric: How I Decided What "Best" Means

I'm not ranking these by GitHub stars. Stars tell you a server got promoted, not that it works in production or is maintained past the initial spike. I'm ranking by five criteria that actually matter for daily use:

1. **Loop value** — Does this server remove a friction point I hit multiple times per day? Not "could you use this in theory" but "do real developers reach for it repeatedly?"

2. **Maintenance signal** — Is there a release in the last 60 days? Is it vendor-maintained or community-maintained? Community servers are fine; abandoned community servers are not.

3. **Setup friction** — How many steps from zero to working? Does it require a PAT in plaintext, or does it support OAuth? Local-only is fine if that's the right fit; friction penalty applies when setup is unnecessarily complex.

4. **Free-tier reality** — Some servers are "free" but connect to services that paywall the features you actually need. I only list servers where the core developer workflow is genuinely free.

5. **Security posture** — Does the server document its threat model? Does it name the risks? Servers that ship without mentioning prompt injection, SSRF, or token scope get a trust penalty regardless of features.

No server I've listed scores perfectly on all five. I'll say so when they don't.

[VISUAL: Scorecard matrix — 10 servers × 5 criteria (Loop Value / Maintenance / Setup Friction / Free Tier / Security Posture), each cell rated High/Medium/Low, color-coded green/yellow/red. Useful for readers scanning to compare picks.]

---

## The 10 Best Free MCP Servers for Developers in 2026

### 1. GitHub MCP Server

**First-party from GitHub · [github.com/github/github-mcp-server](https://github.com/github/github-mcp-server) · Current release: v1.1.0**

If you spend more than two hours a day in GitHub, this is the highest-ROI install on this list. The GitHub MCP Server connects your agentic IDE to repos, pull requests, issues, code search, Actions runs, and notifications. The practical upshot: you can ask your agent to summarize open PRs against a milestone, find the last issue mentioning a specific error string, or trigger a workflow run without switching tabs.

What changed in 2026 is the setup story. The v1.1.0 remote endpoint supports OAuth-based onboarding, which means VS Code 1.101+ can connect with no PAT in any config file. That's a meaningfully different trust boundary from the local mode where your token lived in a JSON file a typo away from a `git commit`.

**Free-tier reality:** Works on free GitHub accounts. The remote OAuth mode is free. Private repo access works within your account's existing permissions.

**One caveat:** OAuth scope selection matters a lot here. The agent will ask for the scopes you grant it. Resist the urge to grant everything — start with read-only on repositories, add write access incrementally only for workflows where you've tested the agent's judgment.

---

### 2. Playwright MCP

**First-party from Microsoft · [github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · Current release: v0.0.76**

Browser debugging is one of the most tab-intensive developer loops that exists. Playwright MCP connects your agent to a real Chromium, Firefox, or WebKit browser — navigation, clicking, form-filling, screenshotting, and accessibility tree inspection all become callable tools.

The genuine workflow win here is bug reproduction: describe a broken flow, let the agent navigate to it and screenshot the failure state, then generate a Playwright test that captures the repro. In my own bug loops, that work regularly shrinks from roughly 20–40 minutes of manual back-and-forth to under 5 once the repro is clear.

Worth reading directly from the Playwright MCP README: the maintainers explicitly note that for coding agents that primarily need token-efficient tool calls, CLI plus skills may be a better fit, and MCP shines for iterative, **persistent-state** workflows — long automations where browser state needs to survive across multiple tool calls.

**Free-tier reality:** Fully open source, no API key, no account needed. Just install Node.js and run it.

**One caveat:** Browser state includes your cookies and session tokens. Don't run this server against a browser profile you're logged into production systems with, and don't paste the full `playwright_evaluate` tool output into a log you share publicly. The server's README names unsafe code execution as a known sensitive operation — take that warning seriously.

---

### 3. MCP Filesystem Server

**Official reference implementation · [modelcontextprotocol/servers/src/filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)**

This is the local foundation most other stacks build on. The Filesystem server gives your agent read and write access to directories you explicitly configure, with tools for reading files, listing directories, searching content, and creating or editing files. It's the lowest-ceremony way to give an agent real project context without copying and pasting code.

The `roots` configuration is what makes this safe. You pass a list of allowed directories at startup; the server rejects any path outside those roots. Set it to `~/projects/my-app` and the agent cannot reach `~/.ssh` or `/etc`.

**Free-tier reality:** Part of the official `modelcontextprotocol/servers` reference repo. Zero cost, fully open source.

**One honest caveat the maintainers themselves state:** The reference servers repo is explicitly described as containing reference implementations, not production-ready defaults. For a solo developer in a sandboxed environment, Filesystem is excellent. For a team deploying this in CI or on shared infra, do your own security review before treating it as production-hardened.

---

### 4. Supabase MCP

**First-party from Supabase · [github.com/supabase/mcp](https://github.com/supabase/mcp) · Docs: [supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp)**

Full-stack developers often spend significant time context-switching between their IDE, the Supabase dashboard, and their database terminal. Supabase MCP collapses that. It exposes tools for querying your database, inspecting table schemas, running migrations, managing auth settings, and viewing Edge Function logs — all from your agent IDE.

The remote OAuth onboarding is the cleanest on this list. You connect once via OAuth, the server handles token refresh, and nothing lives in your config file. Read-only mode is a first-class configuration option, and the Supabase MCP README explicitly discusses prompt injection as a risk — naming specific attack patterns where malicious table data could attempt to redirect agent actions.

**Free-tier reality (verified 2026-06-28):** Supabase's free tier covers 2 projects with 500MB storage and 50,000 monthly active users. For development workflows, that's plenty.

**One caveat:** Even in read-only mode, your database schema is exposed to the model's context window. If your schema contains sensitive information in column names or comments, be aware that it will be visible in the conversation.

---

### 5. MCP Fetch Server

**Official reference implementation · [modelcontextprotocol/servers/src/fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)**

Sometimes you just need the agent to read a web page — a specific library changelog, an API reference, a Stack Overflow thread — without you copy-pasting it into the chat. Fetch does that. It makes HTTP(S) requests to URLs you specify and returns the content, with optional Markdown conversion for cleaner context.

The use case I reach for most often: "check the current SDK docs for this method and tell me if the signature changed in the last release." That saves 3-4 minutes of manual tab work every time.

**Free-tier reality:** No API key, no account, fully open source.

**One caveat the official docs state explicitly:** SSRF (Server-Side Request Forgery) is a real risk. If your agent can call the Fetch tool and an attacker can influence what URLs it fetches — through a prompt injection in a file it reads, for example — they could redirect requests to internal network addresses like `http://169.254.169.254` (cloud metadata endpoints). Don't run the Fetch server in environments where it can reach internal services unless you've added network-level controls.

---

### 6. Cloudflare MCP Suite

**First-party from Cloudflare · [github.com/cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) · Coverage: 13 Cloudflare services**

If you deploy to Cloudflare's edge platform, this suite is unusually complete. The Cloudflare MCP server covers 13 services in a single remote endpoint, including Workers, KV, D1, R2, Vectorize, AI Gateway, and more. You can query KV namespaces, inspect D1 database tables, deploy Workers scripts, and manage R2 buckets — all from your IDE without touching the Cloudflare dashboard.

Cloudflare has leaned into remote MCP hard: their endpoint supports the [Streamable HTTP transport from the 2025-03-26 spec](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#toolannotations), and the onboarding flow works with VS Code 1.101+'s native remote MCP connection UI.

**Free-tier reality (verified 2026-06-28):** The MCP server itself is open source and free. Cloudflare's free tier includes 100,000 Workers requests/day, 1GB KV storage, and a usable D1 database — plenty for development.

**One caveat:** Thirteen services is a wide surface area. I'd encourage using the Cloudflare MCP server with explicit tool allowlists in your client config rather than granting blanket access to the full suite. If you only need D1 queries for a project, configure accordingly.

[VISUAL: "Starter stack by workflow" map — three columns (Repo Work / Browser Debugging / Docs & Database) with recommended server combinations and arrows showing how they connect. Practical decision aid for choosing between the 10 servers.]

---

### 7. Context7

**Maintained by Upstash · [github.com/upstash/context7](https://github.com/upstash/context7) · README translated to 16+ languages**

Context7 is the most focused entry on this list: its single job is live-doc grounding. Before Context7, asking an agent about a library often meant getting plausibly-worded but slightly outdated API information — a hallucination problem rooted in training data staleness. Context7 fetches current, version-specific documentation for the library you're using and injects it into your agent's context.

The adoption signal here is unusually strong for a relatively young project. The README has been translated into 16+ languages by community contributors, which is a meaningful indicator of genuine global developer use rather than just hype.

**Free-tier reality:** Free remote endpoint with a usable free tier for basic doc-grounding workflows.

**One caveat:** Context7 is a third-party remote service. If the Upstash endpoint is unavailable, your agent falls back to its training data — which is exactly the staleness problem you were solving. It's a soft dependency, not a hard one, but worth knowing.

---

### 8. MCP Git Server

**Official reference implementation · [modelcontextprotocol/servers/src/git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) · 12 tools**

The Git server brings 12 git operations into your agent's toolbox: `git_status`, `git_diff`, `git_log`, `git_commit`, `git_add`, `git_create_branch`, and more. For workflows where you want the agent to understand your repo's state — "what changed since main?", "what's in this diff?", "which files are staged?" — this is the right local tool.

The meaningful distinction from GitHub MCP: this is local git operations only, no GitHub API calls. It's faster for offline or air-gapped work, and the trust boundary is clean — it never touches the network. Pair it with GitHub MCP when you need both local state and remote actions.

**Free-tier reality:** Open source reference implementation, zero cost.

**One caveat:** Like all reference servers, the official docs note these are early-development implementations. `git_commit` with an agent in the loop is powerful; make sure your agent IDE's approval flow requires explicit confirmation before commits run. Don't assume the default configuration won't auto-approve destructive operations.

---

### 9. MCP Memory Server

**Official reference implementation · [modelcontextprotocol/servers/src/memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)**

This one is harder to pitch in a sentence because the value is cumulative rather than immediate. The Memory server maintains a local knowledge graph — entities, relations, and observations — that persists across sessions. You can tell the agent "remember that we use snake_case for database columns in this project" and it will recall that convention next session without you re-pasting a CONTRIBUTING.md excerpt.

For long-running projects, persistent context is genuinely useful: team conventions, architectural decisions, deployment gotchas, API keys you're tired of looking up in 1Password. The graph lives as a local JSON file, so it travels with your dotfiles if you manage them.

**Free-tier reality:** Fully open source, local-only, no external dependencies.

**One caveat:** The knowledge graph is stored unencrypted as a local JSON file. Don't use it as a secure credential store. Also note it doesn't automatically prune stale observations — a fact the agent "remembered" six months ago about a deprecated API may still surface unless you actively curate the graph.

---

### 10. Sequential Thinking Server

**Official reference implementation · [modelcontextprotocol/servers/src/sequentialthinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)**

I'm including this last because it's the most abstract entry and the one where I'd push back hardest on anyone rushing to install it. The Sequential Thinking server scaffolds step-by-step reasoning chains: it gives the agent a structured tool for decomposing complex problems into numbered steps, revising previous steps, and branching into alternative approaches.

It's most useful in agentic pipeline contexts — multi-step build automation, complex debugging sequences, or research workflows where you want the agent's reasoning visible and revisable. For simple IDE code completions, it's overhead you don't need.

**Free-tier reality:** Open source, no external dependencies.

**One caveat:** The concrete workflow value here is lower than every other server on this list for most developers. Install this if you're building multi-step agentic pipelines; skip it if you primarily want code assistance.

---

## Case Study — The Setup Flow That Changed in 2026

The clearest before/after story I can tell about MCP in 2026 isn't about a specific server — it's about the **onboarding cost** for remote-first servers.

### Before: Local JSON + PAT juggling (mid-2025)

Connecting any remote service to your MCP client looked roughly like this:

1. **Find or write a server config block** in `~/.claude/config.json` or a project-local `mcp.json`. Format the JSON correctly, get the command and args right.
2. **Generate a PAT** (Personal Access Token) on the service's dashboard. Navigate through settings, pick the right scopes — and if you've never used the service's MCP integration before, guess at which scopes you actually need.
3. **Copy the token** and paste it as a plaintext value in your config file. Hope you're not in a directory that's tracked by git. Add the config file to `.gitignore`. Tell your teammates to do the same.
4. **Repeat for every machine** you work on. The token isn't synced anywhere. If you rotate it, you update 3 config files.

That's **4 manual steps per service, every machine, with secrets in plaintext config files.** For a team of 5 developers using 3 MCP-connected services, that's 60 individual manual steps to bootstrap the stack — before any actual developer work happens.

### After: Remote OAuth onboarding (mid-2026, VS Code 1.101+)

With first-party remote servers like [GitHub MCP v1.1.0](https://github.com/github/github-mcp-server) and [Supabase MCP](https://supabase.com/docs/guides/getting-started/mcp):

1. In VS Code 1.101+, open the MCP servers panel and add a server by its remote URL.
2. A browser OAuth popup appears. One click to authorize with scopes the server already defines as appropriate defaults.

That's it. **1 step per service, no secrets in config files, works on every machine the developer authenticates on.**

For a team of 5 using 3 remote servers, that's 15 authorization clicks versus 60 manual config-edit/token-copy steps. No secrets management. No `.gitignore` workarounds. Token rotation happens server-side. When a teammate joins, they repeat step 1 and 2 — nothing to sync, nothing to share.

The latency cost is real: remote MCP adds a network round-trip per tool call that local servers don't have. For quick tool calls (search, read) this is typically imperceptible. For long-running browser automation (Playwright), local is still faster. The friction-to-security tradeoff now clearly favors remote OAuth for service integrations, and local process for filesystem/git operations.

[VISUAL: Before/After comparison — left side shows 4-step local config flow with PAT in JSON file, right side shows 2-step remote OAuth flow. Annotate with friction counts (steps × team size). Clean side-by-side table or swimlane diagram.]

---

## The Caveats Most MCP Roundups Bury

I've dropped individual caveats into each server entry. Here's the threat model in one place, because you need to understand it as a system, not piecemeal.

### Prompt Injection

An adversary can embed MCP tool-call instructions inside content your agent reads — a GitHub issue, a web page fetched via Fetch, a database row, a code comment. If the agent processes that content and the embedded instruction looks like a tool call, some agents will execute it. [Supabase's MCP README](https://github.com/supabase/mcp/blob/main/README.md) documents specific examples of how malicious table data can attempt to redirect agent behavior. The mitigation is **approval flows**: require explicit user confirmation before any write or destructive tool executes. Most agentic IDEs now support this; enable it.

### SSRF (Server-Side Request Forgery)

As the [Fetch server docs](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) document explicitly: if an attacker can influence what URLs your agent fetches — through a prompt injection in a file the agent reads — they can redirect fetch calls to internal network addresses, cloud metadata endpoints, or local services. Don't deploy the Fetch server in environments where it can reach sensitive internal infrastructure without network-level controls.

### File Overreach

The [Filesystem server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) protects you with roots, but only if you configure them. An unconfigured or overly broad roots list is a serious risk: the agent can read your `.env` files, SSH keys, and shell history. Always specify the narrowest possible directory path in roots — the project directory, not your home directory.

### Token Leakage

Even with OAuth-based servers, the token that grants agent access has a scope. When an agent includes tool call responses in its context window and you export or share a conversation, you may inadvertently share token-bearing responses or session identifiers. Be careful about copy-pasting agent chat logs to public issue trackers or Slack channels.

### Stale Servers

The community MCP ecosystem has hundreds of servers, many of which haven't been updated since their demo moment. A stale server isn't just a maintenance problem — it may have unfixed security issues or depend on deprecated API endpoints that silently return wrong data. The [modelcontextprotocol/servers reference repo](https://github.com/modelcontextprotocol/servers) is the canonical exception: it's actively maintained, but it still carries the "reference implementation, not production-ready" caveat on every entry.

**My rule:** If a server hasn't had a commit in 90 days and isn't vendor-maintained, treat it as unvetted. Verify before you install.

### Local vs. Remote Trust Boundaries

Local servers (Filesystem, Git, Memory, Sequential Thinking) and remote servers (GitHub, Supabase, Cloudflare) have fundamentally different threat models:

- **Local servers** trust your machine's security. If your machine is compromised, local servers offer no additional protection. But they have no network exposure, no API tokens leaving your system, and no third-party dependency.
- **Remote servers** introduce network round-trips, OAuth token management, and dependency on a third party's uptime and security practices. They also remove secrets from local config files, which reduces a common accidental-exposure vector.

Neither model is strictly safer. They're different. Design your stack to match your actual threat model, not whichever feels more modern.

[VISUAL: Local vs. Remote MCP trust boundary diagram — two columns showing local server flow (agent → local process → filesystem/git, no network) and remote server flow (agent → network → OAuth token → vendor API). Annotate threat vectors at each hop: prompt injection point, token exposure point, SSRF vector. This is the diagram most MCP articles skip.]

---

## Start Here: The Smallest Useful Stacks

Rather than installing all 10 and wondering why your agent is slow, start with one loop and one stack.

**Repo work stack — `Filesystem + Git + GitHub MCP`**

This covers 80% of the repo-related tasks developers do daily: read and write project files (Filesystem), understand local git state (Git), and interact with GitHub PRs, issues, and search (GitHub MCP). Start with Filesystem and Git locally, add GitHub MCP via remote OAuth once you've tested the first two.

**Browser / debug stack — `Playwright + Fetch`**

Playwright for UI interaction and screenshot-based debugging. Fetch for pulling API references, changelogs, or error pages the agent needs to understand. These two together handle almost every browser-debugging loop without requiring any external account setup.

**Docs and database stack — `Context7 + Supabase MCP + Memory`**

Context7 keeps your library docs current. Supabase MCP makes your database queryable from your IDE. Memory preserves context across sessions so the agent doesn't forget your project conventions. Start Context7 and Memory locally, connect Supabase via remote OAuth once your Supabase project is set up.

---

## Build It Yourself: 3 Projects to Try This Week

[VISUAL: Project ladder infographic — three-rung build path (Beginner: repo-aware assistant -> Intermediate: browser bug reproduction loop -> Advanced: remote OAuth least-privilege stack), each rung showing goal, success signal, and time estimate.]

### Project 1 (Beginner): Repo-Aware Assistant

**Goal:** Give your AI assistant read access to your local project files and git history so it can answer context-specific questions without you pasting code into chat.

**Prerequisites:**
- Node.js 18+ installed
- An MCP-compatible client: [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Cursor](https://cursor.sh), or [VS Code with Copilot](https://code.visualstudio.com/docs/copilot/overview)
- An existing local git repository to test against

**Steps:**

1. Install the MCP Filesystem server: follow the setup instructions in the [official README](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem). Configure roots to point only at your project directory — for example, `["~/projects/my-app"]`.
2. Install the [MCP Git server](https://github.com/modelcontextprotocol/servers/tree/main/src/git) and point it at the same repository.
3. Connect both servers to your MCP client via its local server configuration.
4. Test with a prompt like: *"Summarize the last 5 commits and tell me which files changed most frequently in the last week."*

**Success signal:** The agent uses `git_log` and returns a commit summary grounded in your actual repo history — not a generic template.

**Time estimate:** 30–45 minutes including first-time setup.

**Stretch goal:** Add the [GitHub MCP Server](https://github.com/github/github-mcp-server) via remote OAuth and ask the agent to cross-reference local history with open PRs on the same repo.

---

### Project 2 (Intermediate): Browser Bug Reproduction Loop

**Goal:** Reproduce a UI bug using Playwright MCP — the agent navigates to the broken state, screenshots it, and drafts a failing test.

**Prerequisites:**
- Node.js 18+ installed
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) installed (`npx @playwright/mcp@latest`)
- An MCP-compatible client that supports tool approval
- A local or staging web app with a known bug to reproduce

**Steps:**

1. Start the Playwright MCP server and connect it to your client.
2. Enable explicit tool approval in your client settings — you want to confirm before any form submission or click runs.
3. Give the agent the URL of the broken page and describe the bug: *"Navigate to http://localhost:3000/checkout and click the 'Place Order' button while the cart is empty. Screenshot the result."*
4. Review the screenshot and ask the agent: *"Write a Playwright test that reproduces this failure."*
5. Run the generated test with `npx playwright test`. Expect it to fail in the same way the agent described.

**Success signal:** The agent produces a `test.spec.ts` file that fails with a meaningful assertion error matching the real bug — not a timeout or generic selector failure.

**Time estimate:** 1–2 hours, depending on your app's complexity.

**Stretch goal:** Add the [MCP Fetch server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) and ask the agent to also fetch and parse any error logs from your staging error endpoint before writing the test.

---

### Project 3 (Advanced): Remote MCP Starter Stack with Least-Privilege Config

**Goal:** Wire up GitHub MCP and Supabase MCP using remote OAuth, with explicit least-privilege scope selection — no PATs in config files, read-only defaults where possible.

**Prerequisites:**
- [VS Code 1.101+](https://code.visualstudio.com/) (required for native remote MCP support)
- A free [GitHub account](https://github.com) with an existing repository
- A free [Supabase account](https://supabase.com) with an existing project containing at least one table
- ~2 hours of focused setup time

**Steps:**

1. Open VS Code 1.101+ and navigate to Settings → MCP Servers. Click "Add Server" and enter the [GitHub MCP remote endpoint URL](https://github.com/github/github-mcp-server). Complete the OAuth flow in the browser popup — when prompted for scopes, select **read-only on repositories** and **read on issues/PRs** only. Do not grant write access on the first pass.

2. Verify by asking your agent: *"List the last 3 open pull requests in [repo-name] with their authors and status."* Confirm the agent returns real PR data, not a fabricated response.

3. Add the [Supabase MCP server](https://supabase.com/docs/guides/getting-started/mcp) following the Supabase docs for VS Code. During setup, configure it in **read-only mode** — the Supabase MCP documentation describes this as a first-class config option.

4. Test the database connection: *"Describe the schema of my `users` table and tell me how many rows it has."* Confirm the response matches your actual schema.

5. Deliberately test the least-privilege boundary: ask the agent to *"insert a test row into the users table."* With read-only mode configured, this should fail gracefully. If it succeeds, review your Supabase MCP configuration.

**Success signal:** Both servers connect via OAuth with no secrets in any config file. The agent can query GitHub and Supabase. The attempted write to Supabase in step 5 is rejected by the server, not by the agent declining.

**Time estimate:** 2–3 hours including troubleshooting OAuth scope edge cases.

**Stretch goal:** Add the [Cloudflare MCP server](https://github.com/cloudflare/mcp-server-cloudflare) and configure it to expose only D1 database tools — practice using Cloudflare's modular server configuration to avoid granting access to all 13 services when you only need one.

---

## Decision Checklist Before You Install

Use this before adding any MCP server — new or familiar:

- [ ] **Is this server actively maintained?** Check the last commit date and release history. Anything without a commit in 90 days that isn't explicitly vendor-maintained: verify before trusting.
- [ ] **Do I know what trust boundary it opens?** Local server = trusts your machine. Remote server = trusts the vendor's infrastructure and your OAuth token management. Neither is wrong; know which you're choosing.
- [ ] **Have I read the security section of the README?** If there isn't one, that's a signal. The best servers (Supabase, Fetch, Playwright, Filesystem) name their own risks.
- [ ] **Are my roots or scopes configured as narrowly as possible?** Filesystem: project directory only, not home. GitHub: read-only to start. Supabase: read-only by default. Cloudflare: specific services, not all 13.
- [ ] **Does my client require explicit approval for write/destructive tools?** Enable this. It's the most practical mitigation against prompt injection turning into an unintended write.
- [ ] **Do I understand the [ToolAnnotations](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#toolannotations) surface of this server?** The 2025-03-26 spec introduced structured annotations for tools — destructive, read-only, external-effects. Well-maintained servers use these; they tell your client which tools need extra approval.
- [ ] **Am I installing this because it solves a real loop friction point, or because it looked cool in a tweet?** Be honest. A server that doesn't touch your daily workflow is just attack surface.

---

## The Takeaway

The best free MCP servers in 2026 aren't the ones with the longest feature lists. They're the ones that **shorten one real developer loop you repeat every day**, with maintenance you can trust and a permission boundary you understand.

If I had to tell one developer where to start today, I'd say: pick the loop you've been meaning to automate longest — repo triage, browser debugging, docs lookup — and install the smallest stack that covers it. For most developers that's two or three servers, not ten.

The protocol is stable at [spec 2025-03-26](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#toolannotations). VS Code 1.101+ ships remote OAuth natively. The ecosystem has vendor-backed servers with real security documentation. There's never been a better time to build a deliberate MCP stack.

Pick one loop. Install the smallest server set that removes one tab-hop from it. Run it for two weeks. Then add the next one.

---

*Found this useful? I'd genuinely like to hear which stack you landed on — GitHub + Playwright, or something else from this list. Drop a comment with your specific combination. If you disagree with a ranking or think a server I didn't mention belongs here, I want that argument too.*
