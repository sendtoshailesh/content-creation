# Reference Brief — PostgreSQL EXPLAIN BUFFERS

Generated: 2026-04-26

## Source Summary

### [Reading Buffer Statistics in EXPLAIN Output](https://boringsql.com/posts/explain-buffers/)

- **Author**: Radim Marek (boringSQL)
- **Published**: 2026-02-06
- **Credibility**: Expert PostgreSQL practitioner, conference speaker (PGConf Germany, PG Data Conference, PgDay UK)

#### Key Technical Concepts

1. **Shared Buffers: hit, read, dirtied, written**
   - `shared hit` = pages found in shared_buffers (cached, fast path, no disk I/O)
   - `shared read` = pages fetched from disk or OS cache (adds I/O latency)
   - `shared dirtied` = pages modified by query (hint bits, HOT chain pruning during reads is normal)
   - `shared written` = pages written to disk during execution (synchronous eviction — warning sign if background writer can't keep up)

2. **Buffer Hit Ratio Formula**
   - `hit_ratio = shared hit / (shared hit + shared read)`
   - Example: 13 / (13 + 857) = 1.5% — terrible for OLTP, expected for cold cache

3. **Interpreting Hit Ratios — Context Over Absolutes**
   - Reporting query scanning large date range: 10-30% is fine
   - Login page query: should be near 100%; drop to 80% means something changed
   - A query at 95% last week now at 40% deserves investigation
   - "The ratio is a diagnostic tool, not a scorecard"
   - Low ratio + high execution time = I/O bottleneck
   - High ratio + high execution time = look elsewhere (CPU, row count, bad plan)

4. **Local Buffers (Temp Tables)**
   - Track I/O for `CREATE TEMP TABLE` — per-backend memory via `temp_buffers` setting
   - No WAL generated, no checkpointing
   - `local hit/read` same concept as shared but for temp tables
   - `local written` rare unless `temp_buffers` severely undersized

5. **Temp Buffers (work_mem Spills)**
   - `temp read/written` = disk spill from sorts/hashes exceeding `work_mem`
   - NOT related to `temp_buffers` parameter (naming confusion)
   - Example: 256kB work_mem forced external merge sort, 9.7MB spill to disk
   - Fix: increase `work_mem` (per-operation, not per-query), optimize query to process fewer rows, add indexes to avoid sorts

6. **Planning Buffers (PG 13+)**
   - Planner reads system catalogs: `pg_class`, `pg_statistic`, `pg_index`
   - High `read` in planning = cold system catalogs or many tables/partitions
   - Planning overhead significant with many partitions — partition pruning matters

7. **PostgreSQL 18: BUFFERS by Default**
   - `EXPLAIN ANALYZE` automatically includes buffer stats starting PG 18
   - No longer need explicit `BUFFERS` flag

8. **Workload-Level Analysis via pg_stat_statements**
   - `shared_blks_hit`, `shared_blks_read`, `temp_blks_written` aggregated over time
   - More actionable than single-query analysis
   - Filter by `calls > 100`, order by `shared_blks_read DESC`

#### Key Data Points

- Example schema: 2,000 customers (13 pages), 100,000 orders (857 pages)
- Cold cache: 1.5% hit ratio; warm cache: approaches 100%
- work_mem at 256kB forced 9.7MB disk spill for 200K row sort
- Problematic query example: 50 hits vs 15,000 reads, 847 written, 2,500 temp spill, 156 planning reads

#### Tuning Levers Identified

| Problem Signal | Tuning Lever |
|---|---|
| Low shared hit ratio | `shared_buffers` sizing, indexing |
| `shared written` during SELECT | `bgwriter_lru_maxpages`, background writer tuning |
| `temp read/written` | `work_mem` increase, query optimization, indexing |
| High planning reads | Keep system catalogs hot, partition pruning |
| Per-operation spill | `work_mem` is per-operation, not per-query |

#### Unique Angle

- "The ratio is a diagnostic tool, not a scorecard" — challenges the common myth of targeting a specific buffer hit ratio
- Clarifies naming confusion between `temp_buffers` (parameter) and `temp read/written` (EXPLAIN output)
- Explains why SELECT queries can show `dirtied` pages (hint bits, HOT chain pruning)

## Cross-Source Analysis

### Gaps to Fill in Our Content

- Real-world e-commerce case study with business impact (revenue, latency SLAs)
- Step-by-step incident investigation workflow (how it was reported → traced → fixed)
- PostgreSQL version compatibility matrix for BUFFERS features
- Open-source tooling references (pgMustard, auto_explain, pganalyze, pg_stat_monitor)
- Long-term monitoring strategy beyond one-off EXPLAIN analysis
- Before/after metrics from a real performance fix
