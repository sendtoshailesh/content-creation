---
name: practitioner-projects
description: "Turn a blog post's core concept into a hands-on 'Build it yourself' section of three structured, GitHub-grounded projects (beginner → intermediate → advanced) plus a build-focused call-to-action. Use after the blog draft exists and before quality review, and when adapting the CTA for LinkedIn, reel, deck, Medium/Substack, and X. Makes content thought leadership, not a link roundup."
argument-hint: "Provide the blog file path (and the concept the projects should let readers build)"
---

# Practitioner Projects Skill

## When to Use

Run after a blog draft exists (Step 3, before quality review) to add a mandatory **practitioner
projects** section, and again whenever a distribution agent (`social-linkedin`, `reel-video`,
`deck-builder`, `platform-distiller`, `social-twitter`) writes its call-to-action. The goal:
every piece hands the reader something concrete to **build**, so the content reads as thought
leadership and shows the art of the possible — not a summary of internet sources.

This skill satisfies the **Practitioner Projects & Art of the Possible (mandatory)** rule in
`content-quality.instructions.md`.

## Output

Add a section to the blog (and propagate a one-line build CTA to every channel). Recommended
heading: `## Build it yourself: 3 projects to try this week`. Place it immediately before the
final wrap-up / CTA so the reader leaves with an action, not a summary.

## The three projects (beginner → intermediate → advanced)

Pick three concepts the post already explained and turn each into a buildable project. The
ladder must show progression: project 1 is doable in an afternoon by one engineer; project 3
is a meaningful weekend-plus build that demonstrates the full idea.

| # | Level | Litmus test |
|---|-------|-------------|
| 1 | Beginner | One engineer, ~1-2 hours, no infra. Proves the core concept once. |
| 2 | Intermediate | ~Half a day. Adds a real feedback signal / measurement / iteration. |
| 3 | Advanced | Weekend+. Demonstrates the full concept end-to-end at small scale. |

## Required structure per project (all fields mandatory)

```
### Project N — <verb-first title>  (<Beginner|Intermediate|Advanced>)

**Goal.** One sentence: what the reader will have built and what it proves.
**Prerequisites.** Tools, accounts, languages, prior project (if it builds on #N-1).
**Steps.**
1. …concrete, numbered, each step a checkable action…
2. …
3. …
**Success signal.** A machine-checkable outcome — a test passes, a metric moves, an output
matches a target. The reader must be able to tell, without judgement, that it worked.
**Time.** Honest estimate (e.g. "~90 min", "a weekend").
**Stretch goal.** One concrete extension that pushes into the next level.
**Start from.** A real, verified GitHub repo / template / tool link — or an explicit
from-scratch path if none fits.
```

## Grounding rules (non-negotiable)

1. **Every "Start from" link is real and verified.** Fetch the URL before publishing; confirm
   the repo/tool exists and matches the description. Never fabricate or guess a link, never
   cite a repo you have not confirmed. Prefer canonical/official repos over forks.
2. **Prefer Microsoft/GitHub-owned repos first (Source-of-Truth Precedence).** When picking a
   "Start from" repo, lead with Microsoft- or GitHub-owned repos and AI Foundry samples
   (e.g. `Azure-Samples/*`, `microsoft/*`, `github/*`, `Azure/*`, Foundry quickstart repos)
   that fit the skill level. Reach for other public repos only when no first-party repo fits.
   Cross-check `content/browsing-signals.md` Tier 3 for repos the author has actually used.
3. **If no suitable repo exists, say so** and give a from-scratch path ("no template needed —
   start with an empty repo and …"). An honest from-scratch path beats a fake link.
4. **Projects derive from the post.** Each maps to a named concept the post already taught;
   reference that section. No generic "build a todo app" filler.
5. **Self-serve for an individual.** A practitioner must be able to start without manager
   sign-off, paid infra they don't have, or proprietary data.
6. **Success signals are objective.** "It feels better" is not a success signal; "the eval
   score goes from X to Y" or "the test suite passes on the agent's PR" is.

## Call-to-action propagation (per channel)

The CTA in every channel names at least one concrete project and links the repo or canonical
URL. Pattern: *"go build X"*, never *"go read my blog"*.

| Channel | CTA shape |
|---------|-----------|
| Blog | Full 3-project section + closing line pointing at Project 1 as the on-ramp. |
| LinkedIn | Close with Project 1 (the afternoon build) + canonical URL in first comment; tease Project 3 as the ambition. |
| Reel / Short | Spoken: "Try the first one this week — link in the description." Repo URL in description block. |
| Slide deck | A "Build it yourself" slide listing the 3 projects; speaker note adds the repo links. |
| Medium / Substack distill | Keep the full projects section; canonical URL + repo links inline. |
| X / Twitter | One line naming Project 1 + repo link (use a footnote if char-constrained). |

## Quality bar (checked by `quality-reviewer` and Tier 0 preflight)

- Exactly 3 projects, clearly laddered beginner → intermediate → advanced.
- All required fields present in each (Goal, Prerequisites, Steps, Success signal, Time,
  Stretch goal, Start from).
- Every "Start from" link resolves and is inline-linked per the citation standard.
- Each project traces to a concept named in the post.
- Every channel's CTA names a concrete project, not the blog itself.

## Handoff

- `blog-writer` invokes this after drafting → projects section added → `quality-reviewer` and
  Tier 0 preflight verify the quality bar.
- `social-linkedin`, `reel-video`, `deck-builder`, `platform-distiller`, `social-twitter`
  read the projects section and apply the per-channel CTA shape above.
