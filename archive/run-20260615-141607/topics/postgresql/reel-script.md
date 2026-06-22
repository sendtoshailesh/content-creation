# Reel / Short Script — PostgreSQL × AI performance

**Format:** 60–90 sec vertical (1080×1920). Screen recording + voiceover. Platforms: Instagram
Reels, YouTube Shorts, LinkedIn video.
**Hook visual:** the before/after latency chart (`visuals/before-after-latency.png`).

| # | Time | On-screen (screen recording cue) | Voiceover |
|---|------|----------------------------------|-----------|
| 1 | 0:00–0:05 | Hard cut to the before/after chart: a tall red **4,200 ms** bar next to a tiny green **38 ms** bar. | "This Postgres query went from four thousand milliseconds to thirty-eight. AI helped — but not the way you think." |
| 2 | 0:05–0:14 | Terminal: `EXPLAIN (ANALYZE, BUFFERS)` output scrolling; highlight a red "Seq Scan" line. | "The rule nobody tells you: an LLM can't see your database. No version, no buffers, no stats. Out of the box it hallucinates and quotes stale defaults." |
| 3 | 0:14–0:26 | Split screen: left = pasting the EXPLAIN plan + `pg_stat_statements` row into a chat; right = the model's reply spotting the seq scan. | "So you ground it. Paste the real EXPLAIN ANALYZE, the stat row, your version. Now it spots the non-sargable `date_trunc` and the missing composite index in seconds." |
| 4 | 0:26–0:38 | Show the suggested fix: a sargable range rewrite + `CREATE INDEX`, then a `hypopg_create_index(...)` call and a re-planned EXPLAIN showing "Index Scan". | "But you don't run it on faith. Validate with hypopg — a hypothetical index — confirm the planner switches to an index scan, *then* build it CONCURRENTLY." |
| 5 | 0:38–0:50 | Cut back to the before/after chart; animate the green bar dropping; overlay "~110x faster". | "Result: a hundred-and-ten-x speedup. The AI didn't do anything you couldn't — it just got you to the right hypothesis in thirty seconds instead of thirty minutes." |
| 6 | 0:50–1:00 | Quick flash of the matrix: High/High/Medium/High/Low rows; linger on "Internals & DDL — keep a human in front." | "Use it for triage, plan-reading, and index ideas. Keep a human in front of anything that takes a lock. Grounded prompts, validated changes — that's the whole game." |
| 7 | 1:00–1:05 | End card: "Feed your slowest query its EXPLAIN ANALYZE this week." + handle. | "Try it on one slow query this week. Follow for the next one." |

## Captions / on-screen text (burned-in)
- 0:00 "4,200 ms → 38 ms"
- 0:07 "An LLM can't see your DB"
- 0:16 "Ground it: EXPLAIN ANALYZE + stats + version"
- 0:28 "Validate with hypopg → then CREATE INDEX CONCURRENTLY"
- 0:40 "~110x faster"
- 0:52 "Keep a human in front of DDL"

## Notes
- Keep numbers consistent with the blog (4,200 ms → 38 ms, ~110x).
- All metrics illustrative of a common composite-index fix; mechanisms/tools are real.
