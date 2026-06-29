# Content Decision Log (ADR-style)

Durable, per-run record of the **consequential forks** a content run took — and the alternatives
that lost. The `content-decision-record` skill appends here whenever a real choice is made
(thesis framing, single-post vs series, primary audience, format/channel, a scope cut, a review
override). The value is the **preserved context + rejected alternatives**, so a later run answers
"why did we decide that?" instead of re-litigating it.

## How to use

- **Append**, newest first, one `CDR-NNN` entry per decision — only when a real alternative was on
  the table. Reversible or uncontested choices do not belong here.
- **Always capture the rejected option** and the deciding trade-off, not just the winner.
- **Supersede, never overwrite**: to reverse an earlier decision, mark the old entry
  `superseded by CDR-XXX` and cross-link both ways.
- `post-run-reflection` mines the **Alternatives rejected** fields as candidate follow-up ideas
  (origin tags `cut-scope` / `pivot-angle`).

## Entry format

```markdown
### CDR-NNN — <short decision title>

- **Date / phase**: YYYY-MM-DD · <phase>
- **Status**: accepted   <!-- proposed | accepted | superseded by CDR-XXX -->
- **Decision**: The one sentence we committed to.
- **Context / forces**: What made this a fork.
- **Alternatives rejected**:
  - *<Option B>* — why it lost.
- **Consequences**: What this commits us to downstream.
```

## Entries

_No decision records yet. Append the first `CDR-001` when a run takes its first real fork._
