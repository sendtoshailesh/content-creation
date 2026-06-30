## Reel Script: When Not to Use Postgres — A Decision Framework for the Four Walls

**Duration**: 85 seconds
**Format**: D (Hot Take) + consolidation demo
**Platforms**: Instagram Reels, YouTube Shorts, LinkedIn Video
**Aspect ratio**: 9:16 (1080x1920)
**Voice**: Believer, first-person, conversational and data-driven

---

### Shot List

| Time | Visual + Screen-Recording Cue | Voiceover | Text Overlay |
|------|-------------------------------|-----------|--------------|
| 0:00-0:04 | **Cold open** on a live `psql` prompt, cursor blinking. Type fast: `CREATE EXTENSION vector;` and hit enter -> `CREATE EXTENSION`. | "You probably don't need a vector database." | "You don't need a vector DB." |
| 0:04-0:09 | Hard cut to full-screen title card: `content/visuals/db1-five-to-one-consolidation-hero.svg` (five boxes collapsing into one elephant). | "I've watched team after team run five datastores to serve one product — then collapse them into one Postgres." | "5 datastores -> 1" |
| 0:09-0:20 | Stay on the hero card; light-up each tag as named: vector / queue / time-series / search / document. | "Vectors? pgvector. Queues? pgmq. Time-series? TimescaleDB. Search? Full-text. Documents? JSONB. One engine — one backup, one failover, one on-call." | "pgvector · pgmq · Timescale · FTS · JSONB" |
| 0:20-0:30 | Back to `psql`. Run a similarity query: `SELECT id FROM docs ORDER BY embedding <=> $1 LIMIT 5;` -> results land instantly. Zoom on the `<=>` operator and the row times. | "Semantic search lives right next to your relational data. ACID, JOINs, point-in-time recovery — no second system to keep in sync." | "Similarity search, in your DB" |
| 0:30-0:40 | `psql` again. Show an enqueue inside a transaction: `BEGIN;` -> `INSERT INTO orders ...;` -> `SELECT pgmq.send('jobs', ...);` -> `COMMIT;`. Zoom on `BEGIN`/`COMMIT` wrapping both. | "Your job and the data it touches commit in the same transaction. The 'row saved but the job never fired' bug? Structurally gone." | "Job + data, one transaction" |
| 0:40-0:46 | Transition slate: "Believer, not zealot." Then cut to caveat card: `content/visuals/db1-four-breakpoints-panel.png` full-screen. | "So is Postgres always the answer? No. There are four walls — and each one has a number." | "4 walls. Each has a number." |
| 0:46-0:50 | Panel card, highlight card 1. | "Wall one: extreme writes. ScyllaDB-class — 7.5 million inserts a second at 4-millisecond P99." | "7.5M inserts/sec @ 4ms" |
| 0:50-0:54 | Highlight card 2. | "Wall two: planet-scale sharding. Vitess ran all of YouTube's database traffic for years." | "Vitess: ran all of YouTube" |
| 0:54-0:58 | Highlight card 3. | "Wall three: single-digit-millisecond key-value. DynamoDB-class — 500k-plus requests a second, five nines." | "500k+ req/s · 99.999%" |
| 0:58-1:02 | Highlight card 4. | "Wall four: petabyte OLAP scans. ClickHouse-class — about a billion rows a second." | "~1B rows/sec scans" |
| 1:02-1:08 | Quick note slate, neutral palette: logos/names side by side, none larger. | "These specialists are equals. Any one cloud's managed option is just one option among them — not the default." | "Specialists are equals" |
| 1:08-1:18 | Closing card: `content/visuals/db1-decision-rule-strip.svg` full-screen. | "So here's the rule. Default to Postgres. When you hit a wall, name it with a number. If you can't name the number — you don't have the wall yet." | "Name the wall with a number." |
| 1:18-1:25 | Split frame: decision strip holds, then end card with handle + "full decision framework linked." | "So run the audit on your own stack — for every datastore beyond Postgres, can your team name the wall and the number? Full framework's linked below. Follow for more." | "Name the wall, or consolidate. Link below." |

---

### Screen Recording Notes

- **App/tool to show:** A terminal running `psql` against a local Postgres 16+ with `pgvector` and `pgmq` installed. Use a large, high-contrast font (e.g. 18-20pt) so it reads on mobile.
- **Settings to have visible:** A seeded `docs` table with an `embedding vector(N)` column and an HNSW index, plus a `pgmq` queue named `jobs` already created — so every command returns instantly on screen.
- **Actions to perform, in order:**
  1. `CREATE EXTENSION vector;` (cold open — run against a fresh DB or one where it returns cleanly).
  2. Similarity query: `SELECT id, content FROM docs ORDER BY embedding <=> :query_vec LIMIT 5;` — let the ranked rows and timing flash on screen.
  3. Transactional enqueue: `BEGIN;` then `INSERT INTO orders (...) VALUES (...);` then `SELECT pgmq.send('jobs', '{"order_id": 42}');` then `COMMIT;`.
- **Zoom/crop:** Crop tight to the relevant lines. Push-in (digital zoom) on the `<=>` operator and on the `BEGIN`/`COMMIT` lines so the two key beats land. Never show a full cluttered terminal.

---

### Voiceover Script (Full)

> You probably don't need a vector database. I've watched team after team run five datastores to serve one product — then collapse them into one Postgres. Vectors? pgvector. Queues? pgmq. Time-series? TimescaleDB. Search? Full-text. Documents? JSONB. One engine — one backup, one failover, one on-call. Semantic search lives right next to your relational data: ACID, JOINs, point-in-time recovery — no second system to keep in sync. Your job and the data it touches commit in the same transaction. The "row saved but the job never fired" bug? Structurally gone.
>
> So is Postgres always the answer? No. There are four walls — and each one has a number. Wall one: extreme writes. ScyllaDB-class — 7.5 million inserts a second at 4-millisecond P99. Wall two: planet-scale sharding. Vitess ran all of YouTube's database traffic for years. Wall three: single-digit-millisecond key-value. DynamoDB-class — 500k-plus requests a second, five nines. Wall four: petabyte OLAP scans. ClickHouse-class — about a billion rows a second. These specialists are equals. Any one cloud's managed option is just one option among them — not the default.
>
> So here's the rule. Default to Postgres. When you hit a wall, name it with a number. If you can't name the number — you don't have the wall yet. So run the audit on your own stack: for every datastore beyond Postgres, can your team name the wall and the number? Full framework's linked below. Follow for more.

*Read length: ~83 seconds at a natural conversational pace. Trim the "five nines" aside if you run long.*

---

### Thumbnail / Cover Frame

A vertical split: left half is a dark `psql` terminal with `CREATE EXTENSION vector;` glowing in monospace; right half is the five-to-one elephant hero. Bold overlay headline: **"You don't need a vector DB."** Subline in smaller type: **"Until you hit one of 4 walls."**

---

### Music / Pacing Notes

- **Vibe:** Clean, confident lo-fi tech beat — steady pulse, not frantic. Think focused-coding energy.
- **Beat map:** Let the cold-open `CREATE EXTENSION` land in near-silence (1 percussive hit on the enter key) for a scroll-stop. Drop the beat on the hero card at 0:04.
- **Dramatic pause:** Tiny breath before "No." at 0:42 — kill the music bed for ~0.5s, then bring it back on "four walls."
- **Transitions:** A subtle whoosh on each hard cut between `psql` and full-screen cards. A single rising tick as each of the four breakpoint cards highlights.
- Do not use any copyrighted track — pick a royalty-free bed matching the vibe above.

---

### Captions & Hashtags

**Instagram Reels / YouTube Shorts:**

Five datastores became one Postgres — and the cloud bill went down with them.

Default to Postgres for vectors (pgvector), queues (pgmq), time-series (TimescaleDB), search (full-text), and documents (JSONB). One engine, one ops story.

The honest caveat: 4 walls where you genuinely need a specialist — and each one has a number.
→ 7.5M inserts/sec (ScyllaDB-class)
→ sharding that ran all of YouTube (Vitess)
→ 500k+ req/s single-digit-ms KV (DynamoDB-class)
→ ~1B rows/sec scans (ClickHouse-class)

The rule: name the wall with a number, or you don't have the wall yet. Run the audit on your own stack — full decision framework linked. 🐘

#PostgreSQL #Postgres #pgvector #DatabaseEngineering #BackendDevelopment #SoftwareArchitecture #DevOps #DataEngineering #VectorDatabase #BuildInPublic

**LinkedIn Video:**

Team after team I've worked with ran five datastores to serve one product — then collapsed them into one Postgres, and the architecture diagram stopped needing a meeting to explain.

The consolidation case: default to Postgres for vectors (pgvector), queues (pgmq), time-series (TimescaleDB), search (full-text/tsvector), and documents (JSONB). One backup to test, one failover to rehearse, one on-call rotation.

But believer, not zealot. There are four walls where I still reach for a specialist on purpose — and each is named with a number:
• Extreme writes — ScyllaDB-class, 7.5M inserts/sec @ 4ms P99
• Planet-scale sharding — Vitess, which ran all of YouTube's DB traffic for years
• Single-digit-ms key-value — DynamoDB-class, 500k+ req/s, 99.999%
• Petabyte OLAP scans — ClickHouse-class, ~1B rows/sec

These specialists are equals; any one cloud's managed option is one option among them, not the default.

The decision rule: default to Postgres, and when you hit a wall, name it with a number. If you can't name the number, you don't have the wall yet.

Run the audit: for every datastore beyond Postgres, can your team name the wall and the number? Full decision framework linked in the comments — https://sendtoshailesh.github.io/content-creation/blog/just-use-postgres.html. What consolidation — or specialization — call did you make, and which wall forced your hand?

#PostgreSQL #DatabaseArchitecture #SoftwareEngineering #pgvector #DataEngineering #BackendDevelopment
