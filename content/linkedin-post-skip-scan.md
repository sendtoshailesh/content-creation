<!-- LinkedIn post for: content/postgresql-18-skip-scan.md -->
<!-- Canonical URL (FIRST COMMENT ONLY): https://sendtoshailesh.github.io/blog/postgresql-18-skip-scan-redundant-index.html -->
<!-- Voice: first-person practitioner. LinkedIn native formatting only. -->

# LinkedIn Post — PostgreSQL 18 Skip Scan

**Attach (in this order):** `content/visuals/pg-01-index-ladder.png` (lead), `content/visuals/pg-03-explain-flip.png` (second)

── START COPY (Plain) ──

The cheapest performance win in PostgreSQL 18 is the index you get to delete.

For years we all had the same reflex: a multicolumn index on (tenant_id, status), a query filters only on status, you see a seq scan, so you add a second index on status. Reads get fast. But every index is a tax you pay on every single write.

PostgreSQL 18 (25 Sep 2025) retires that reflex with skip scan: a multicolumn B-tree can now serve a query that omits its leading column. So the duplicate index can finally go.

One DROP INDEX, three wins:
▸ Faster reads — the query you covered with a duplicate now rides the index you already had
▸ Faster writes — one fewer index to maintain on every INSERT/UPDATE/DELETE
▸ Less disk — reclaimed storage + smaller backups

The before/after is clean:
PG 17 → Seq Scan on status, add idx_status
PG 18 → Index Only Scan (skip scan), drop idx_status

Honest caveat: skip scan shines when the leading column is low-cardinality (a few tenants/statuses). High-cardinality lead? Keep the targeted index.

This week: on a replica, find your biggest single-column index that duplicates a wider index's lead column, upgrade to 18, drop it, and watch EXPLAIN show the skip scan. Which redundant index would you delete first? 👇

#PostgreSQL #PostgreSQL18 #Database #Performance #DBA #CostOptimization

── END COPY ──

---

── UNICODE VERSION ──

𝗧𝗵𝗲 𝗰𝗵𝗲𝗮𝗽𝗲𝘀𝘁 𝗽𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲 𝘄𝗶𝗻 𝗶𝗻 𝗣𝗼𝘀𝘁𝗴𝗿𝗲𝗦𝗤𝗟 18 𝗶𝘀 𝘁𝗵𝗲 𝗶𝗻𝗱𝗲𝘅 𝘆𝗼𝘂 𝗴𝗲𝘁 𝘁𝗼 𝗱𝗲𝗹𝗲𝘁𝗲.

For years we all had the same reflex: a multicolumn index on (tenant_id, status), a query filters only on status, you see a seq scan, so you add a second index on status. Reads get fast. But every index is a tax you pay on every single write.

PostgreSQL 18 (25 Sep 2025) retires that reflex with 𝘀𝗸𝗶𝗽 𝘀𝗰𝗮𝗻: a multicolumn B-tree can now serve a query that omits its leading column. So the duplicate index can finally go.

One DROP INDEX, three wins:
▸ 𝗙𝗮𝘀𝘁𝗲𝗿 𝗿𝗲𝗮𝗱𝘀 — the query you covered with a duplicate now rides the index you already had
▸ 𝗙𝗮𝘀𝘁𝗲𝗿 𝘄𝗿𝗶𝘁𝗲𝘀 — one fewer index to maintain on every INSERT/UPDATE/DELETE
▸ 𝗟𝗲𝘀𝘀 𝗱𝗶𝘀𝗸 — reclaimed storage + smaller backups

The before/after is clean:
PG 17 → Seq Scan on status, add idx_status
PG 18 → Index Only Scan (skip scan), drop idx_status

Honest caveat: skip scan shines when the leading column is low-cardinality (a few tenants/statuses). High-cardinality lead? Keep the targeted index.

This week: on a replica, find your biggest single-column index that duplicates a wider index's lead column, upgrade to 18, drop it, and watch EXPLAIN show the skip scan. 𝗪𝗵𝗶𝗰𝗵 𝗿𝗲𝗱𝘂𝗻𝗱𝗮𝗻𝘁 𝗶𝗻𝗱𝗲𝘅 𝘄𝗼𝘂𝗹𝗱 𝘆𝗼𝘂 𝗱𝗲𝗹𝗲𝘁𝗲 𝗳𝗶𝗿𝘀𝘁? 👇

#PostgreSQL #PostgreSQL18 #Database #Performance #DBA #CostOptimization

── END COPY ──

**First comment:** Full write-up → https://sendtoshailesh.github.io/blog/postgresql-18-skip-scan-redundant-index.html
