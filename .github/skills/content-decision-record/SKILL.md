---
name: content-decision-record
description: "Record consequential, hard-to-reverse content decisions ADR-style with the alternatives that were rejected and why. Append a short entry whenever a real fork is taken — thesis framing, single-post vs series split, primary audience, format/channel, a scope cut, or a review override. Writes content/content-decision-log.md. Optional, lightweight, never a publishing gate; its rejected alternatives feed the post-run reflection."
argument-hint: "Describe the decision just taken, the alternatives weighed, and why one won"
---

# Content Decision Record Skill

## When to Use

Log a decision the moment a content run takes a **consequential fork that a real alternative
lost** — the kind of choice a future reader (or a later phase) would otherwise reverse-engineer
or silently re-open. This is the ADR (Architecture Decision Record) pattern pointed at content
instead of code: capture *what* was decided, *why*, and crucially *what was rejected and why*,
while the reasoning is still fresh.

> Methodology: ADR / Decision Record. The value is not the chosen option — it is the **preserved
> context and the rejected alternatives**. Six weeks later "why didn't we make this a series?" has
> an answer instead of a re-litigation. The rejected options also become raw material for the
> next run (see Hand-off).

### Decisions worth a record

| Phase | Example decision | Real alternative that lost |
|-------|------------------|----------------------------|
| Brief | The thesis framing / angle | a different framing that was considered |
| Scope | Single post vs N-part series; where parts split | the other split, or staying single |
| Brief | Primary audience / persona | the secondary persona it could have led with |
| Strategy | Format & channel emphasis (blog-first, carousel-first, video-first) | the format not chosen |
| Writing | A scope cut ("we will not cover X here") | covering X now |
| Review | An override of a gate finding ("ship despite the SEO flag because …") | following the finding |
| Visual | A medium/style call that excludes an obvious option | the excluded medium |

### Not worth a record

Reversible, low-stakes, or uncontested choices (word-level edits, palette tweaks with no
trade-off, anything with no real alternative). A log full of trivia hides the decisions that
matter. **If no alternative was genuinely on the table, do not write an entry.**

## Output

Append to `content/content-decision-log.md` (create from the template below if missing). One
entry per decision, newest first. Keep each entry tight — a few lines per field, not an essay.

### Entry format

```markdown
### CDR-NNN — <short decision title>

- **Date / phase**: 2026-06-25 · Scope assessment
- **Status**: accepted   <!-- proposed | accepted | superseded by CDR-XXX -->
- **Decision**: The one sentence we committed to.
- **Context / forces**: What made this a fork — the constraint, signal, or tension that forced a choice.
- **Alternatives rejected**:
  - *<Option B>* — why it lost (the deciding trade-off).
  - *<Option C>* — why it lost.
- **Consequences**: What this commits us to downstream (and any debt it creates).
```

`Status` lets a later run **supersede** a decision honestly rather than quietly contradicting it:
mark the old entry `superseded by CDR-XXX` and write the new one — never edit history away.

## Procedure

1. **Detect the fork.** When a phase commits to one option over a real alternative, pause and
   draft an entry. Most runs produce a handful — brief framing, the scope split, maybe one review
   override — not dozens.
2. **Capture the loser, not just the winner.** The rejected alternative + the deciding trade-off
   is the whole point. "We considered a 3-part series but split into 2 because Part 3's payoff
   could not be grounded in a first-party source yet" is worth more than the chosen number.
3. **Append, newest first**, with the next `CDR-NNN` id. Set `Status: accepted` (or `proposed`
   if still under review).
4. **Supersede, don't overwrite.** If this run reverses an earlier decision, flag the old entry
   `superseded by …` and cross-link both ways.

## Hand-off to discovery

`post-run-reflection` reads this log's **rejected alternatives** as candidate follow-up ideas — a
framing or scope you deliberately set aside is often the next piece's strongest angle (origin tag
`cut-scope` or `pivot-angle`). Recording the loser here is what makes that harvest possible; an
unrecorded rejected option is a lead lost.

## Relationship to the other memory artifacts

| Artifact | Captures | Horizon |
|----------|----------|---------|
| `content-decision-log.md` (this) | *why we chose X over Y* this run | per-run, durable |
| `critique-memory.md` | confirmed **recurring review misses** | cross-run rubric fixes |
| `hypothesis-ledger.md` | predicted vs actual **engagement** per piece | per-run go/no-go |

A decision record is the *forethought*; the ledger is the *afterthought*; critique-memory is the
*pattern* across both. Keep them distinct — do not log engagement outcomes here.

## Constraints

- **Only log real forks** — an entry with no genuinely rejected alternative is noise; skip it.
- **Always record the rejected option and the deciding trade-off**, not just the winner.
- **Never rewrite history** — supersede with a new entry and a status pointer.
- **Never blocks** a run; the log is a record, not a gate.
- Keep entries short; this is a decision *index*, not a design doc.
