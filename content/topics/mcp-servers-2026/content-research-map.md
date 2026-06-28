# Content Research Map

## Content thesis
The right way to pick free MCP servers in 2026 is not by catalog size or hype, but by how safely
each server shortens a real developer loop: repo work, browser work, docs grounding, incident
triage, or persistent context.

## Perspectives discovered
- **IC implementer** — wants the fastest useful stack and concrete install value.
- **Burned skeptic** — wants stale-server risk and security caveats called out early.
- **Tech lead** — wants a ranking framework that a team can standardize.
- **Tool explorer** — wants the buzzy remote-MCP angle and new server categories.
- **Time-poor scanner** — wants a quick "start with these three" answer near the top.

## Contradiction map

| Clash | Source/Persona A | Source/Persona B | Resolution | Becomes thesis? | Blind spot |
|---|---|---|---|---|---|
| Catalog breadth vs. trusted picks | Tool explorer wants exhaustive lists | Burned skeptic wants only maintained servers | Rank by loop value + maintenance + security posture | yes | "starter stack" framing |
| Local-first safety vs. remote convenience | Filesystem/Git are simpler trust boundaries | GitHub/Supabase/Cloudflare remove setup friction with OAuth | Treat local and remote as different threat models, not good vs bad | no | decision matrix by trust boundary |
| MCP everywhere vs. CLI/skills | Playwright notes MCP overhead for coding agents | Exploratory workflows still benefit from MCP state | Show when MCP is the right shape and when it is not | no | "don't install MCP just because it exists" |

## Ranked argument plan

| # | Claim | Evidence | Supports / Challenges | Persona | Confidence |
|---|---|---|---|---|---|
| 1 | Remote MCP is the biggest workflow shift in 2026 | GitHub, Supabase, Cloudflare remote endpoints; VS Code 1.101+ | supports: tool explorer, time-poor scanner | all | 9 |
| 2 | GitHub, Playwright, and Filesystem are the most universal first installs | first-party docs, setup paths, broad task coverage | supports: IC implementer; challenge: local-only purists | IC | 9 |
| 3 | Security caveats are part of ranking quality, not a footnote | Supabase prompt-injection docs, Fetch SSRF caution, Filesystem scoping | supports: burned skeptic, tech lead | skeptic/lead | 10 |
| 4 | Live-doc grounding is now a top-tier developer use case | Context7 positioning around up-to-date docs | supports: IC implementer | IC | 8 |
| 5 | Not every useful MCP server connects to an external SaaS | Memory and Sequential Thinking improve persistent context and reasoning | supports: tool explorer; challenge: people who only value API integrations | explorer | 7 |

## Self peer-review
- **Weakest claim:** Sequential Thinking belongs in a top-10 "server" list for developers; it is
  defensible, but less concrete than repo/browser/database tools.
- **Bias / dominance check:** PASS — vendor sources dominate because they are the best primary
  sources for maintenance/setup/security, but the thesis is vendor-neutral and the ranking logic
  does not privilege any one publisher.
- **Missing perspective:** infrastructure/platform engineer; Cloudflare covers some of this, but a
  deeper infra angle could add Kubernetes/AWS if researched further.
- **Overall grade:** A-

## Outline tree

topic
  - why MCP lists are noisy in 2026
    - claim: remote MCP changed setup expectations {evidence: GitHub/Supabase/Cloudflare, persona: all, confidence: 9}
    - claim: vendor-backed servers now outcompete many hobby wrappers {evidence: primary repos, persona: lead, confidence: 8}
  - ranking framework
    - claim: best means loop value + maintenance + security + free-tier utility {evidence: research synthesis, persona: lead, confidence: 10}
  - the 10 best free servers
    - claim: GitHub/Playwright/Filesystem form the strongest universal top 3 {evidence: official docs, persona: IC, confidence: 9}
    - claim: Supabase/Cloudflare/Context7 represent the strongest remote-specialized picks {evidence: primary repos/docs, persona: IC, confidence: 8}
    - claim: Git/Memory/Sequential Thinking complete the stack for local workflow control {evidence: official docs, persona: explorer, confidence: 7}
  - caveats
    - claim: prompt injection, SSRF, token scope, and stale repos must be named explicitly {evidence: Supabase/Fetch/reference repo docs, persona: skeptic, confidence: 10}
  - build it yourself
    - claim: readers should start with one loop, not ten installs {evidence: thesis synthesis, persona: time-poor scanner, confidence: 9}
