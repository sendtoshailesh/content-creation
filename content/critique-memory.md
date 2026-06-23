# Critique Memory (Reflexion buffer)

Episodic log of **confirmed, recurring** review misses. The `critic-review` skill loads this file first
on every run so the critic stops re-making the same mistakes and producers stop re-triggering them. This is
the "fix the loop, not the artifact" move: when an entry recurs, patch the rubric/constitution rather than
re-reviewing each artifact by hand.

## How to use

- **Read** at the start of every Tier 1 critic run — check the artifact against these known misses first.
- **Append** an entry only when a miss is *confirmed* (a human or the jury upheld it) **and** it has
  recurred or is likely to recur across runs. One-off slips do not belong here.
- **Promote** an entry to the constitution: when the same pattern appears 3+ times, add the rule to the
  relevant `*.instructions.md` and note "promoted" in the entry so it can be retired from this buffer.

## Entry format

| Date | Pattern (the recurring miss) | Where it shows up | The rule that catches it | Status |
|------|------------------------------|-------------------|--------------------------|--------|

## Entries

_No confirmed recurring misses recorded yet. Append rows as the cascade upholds them._
