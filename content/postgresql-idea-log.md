# PostgreSQL Content Idea Log

> Curated content ideas for the PostgreSQL community, focused on the four angles the user requested: **performance optimization**, **cost optimization**, a **new feature in the latest PostgreSQL (18, released 25 Sep 2025)**, and **how that feature beats the old way it had to be done before**. Sources: PostgreSQL.org release notes/news, official 18 docs, and practitioner write-ups.

Curated: 2026-06-29 · Latest stable: PostgreSQL 18 (25 Sep 2025) · Scoring: relevance + data density + timeliness + community pull + old-vs-new clarity (5 each, /25)

---

## [1] Skip Scan: drop the redundant index PostgreSQL made you build  ⭐ SELECTED
- **Score**: 24/25 (R:5 D:5 T:5 C:5 O:4)
- **Angle**: PostgreSQL 18's B-tree **skip scan** lets a multicolumn index `(a, b)` serve queries that filter on `b` alone — so the single-column index you used to add just to cover that case can finally be dropped. One feature, all four reader payoffs: faster reads, cheaper writes + storage, a brand-new 18 capability, and a crisp before/after.
- **Performance**: query on a non-leading column goes from Seq Scan / bloated scan to an Index (skip) Scan; multi-x latency drop on selective predicates.
- **Cost**: each redundant index dropped = less disk + one fewer index to maintain on every INSERT/UPDATE/DELETE → faster writes, smaller backups.
- **New feature**: skip scan is new in 18; pre-18 the planner ignored `(a,b)` when `a` was missing.
- **Old vs new**: PG ≤17 → add `idx_b` or eat a seq scan; PG 18 → reuse `idx_ab`, delete `idx_b`.
- **Key data**: PG18 GA 25 Sep 2025; before = Seq Scan, after = Index Only Scan (skip scan); dropping a redundant index removes per-row write amplification + its storage.
- **Sources**: postgresql.org/about/news/postgresql-18-released-3142 · docs/current/release-18.html
- **Status**: `selected`

## [2] Asynchronous I/O: the up-to-3x read win you get just by upgrading
- **Score**: 22/25 (R:5 D:5 T:5 C:3 O:4)
- **Angle**: 18's new AIO subsystem (`io_method = worker | io_uring | sync`) replaces single-threaded OS readahead; sequential scans, bitmap heap scans and VACUUM go 2–3x faster, biggest on cloud/network storage. Performance-first, near-zero app change.
- **Old vs new**: pre-18 one blocking read at a time vs 18 concurrent in-flight reads; `pg_aios` view for observability.
- **Cost**: faster VACUUM/scans = fewer/smaller instances for the same workload.
- **Status**: `queued`

## [3] UUIDv7: stop paying the random-UUID tax on writes and index bloat
- **Score**: 20/25 (R:4 D:4 T:4 C:4 O:4)
- **Angle**: native `uuidv7()` gives time-ordered UUIDs → better index locality, less bloat, faster inserts vs random `uuidv4` keys. Cost + perf + old-vs-new in one.
- **Status**: `queued`

## [4] Virtual generated columns: compute-at-read, pay zero storage
- **Score**: 18/25 (R:4 D:3 T:4 C:4 O:3)
- **Angle**: 18 makes generated columns *virtual* (computed on read) by default vs stored; saves disk and write cost for derived values. Clean old(stored)-vs-new(virtual) cost story.
- **Status**: `queued`

---

**Pick:** [1] Skip Scan — highest score and the only idea that lands performance, cost, new-feature, and old-vs-new in a single tight narrative.
