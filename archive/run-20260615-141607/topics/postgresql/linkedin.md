# LinkedIn Post — PostgreSQL × AI performance (visual-first)

> **Visual-first.** Lead asset: the 9-slide carousel PDF `visuals/distilled/postgresql-practitioner/postgresql-carousel.pdf` (upload via LinkedIn's "Add a document" option). Links to the canonical blog. Unicode bold/italic — copy-paste ready.

── START COPY ──

𝗥𝗲𝗮𝗹-𝗹𝗶𝗳𝗲 𝗹𝗲𝘀𝘀𝗼𝗻𝘀 — 𝗛𝗼𝘄 𝗔𝗜 𝗔𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗛𝗲𝗹𝗽𝘀 𝗬𝗼𝘂 𝗙𝗶𝘅 𝗣𝗼𝘀𝘁𝗴𝗿𝗲𝗦𝗤𝗟 𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲 𝗣𝗿𝗼𝗯𝗹𝗲𝗺𝘀 (𝗮𝗻𝗱 𝗪𝗵𝗲𝗿𝗲 𝗜𝘁 𝗟𝗶𝗲𝘀)

𝗔𝗜 𝘄𝗼𝗻'𝘁 𝗳𝗶𝘅 𝘆𝗼𝘂𝗿 𝗣𝗼𝘀𝘁𝗴𝗿𝗲𝘀 𝗽𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲. 𝗕𝘂𝘁 𝗶𝘁 𝗰𝗮𝗻 𝗺𝗮𝗸𝗲 𝘆𝗼𝘂 𝟭𝟬𝘅 𝗳𝗮𝘀𝘁𝗲𝗿 𝗮𝘁 𝗳𝗶𝗻𝗱𝗶𝗻𝗴 𝘁𝗵𝗲 𝗳𝗶𝘅.

I spent a year handing parts of the 2 a.m. slow-query loop to LLMs on customers' Postgres fleets. These are the real-life lessons — exactly where it helps, where it lies, and how to keep a human in the loop. 👇

━━━━━━━━━━━━━━━━━━━━

The #1 rule: 𝘢𝘯 𝘓𝘓𝘔 𝘤𝘢𝘯'𝘵 𝘴𝘦𝘦 𝘺𝘰𝘶𝘳 𝘥𝘢𝘵𝘢𝘣𝘢𝘴𝘦. On the BIRD benchmark, GPT-4 gets just 𝟱𝟰.𝟴𝟵% SQL accuracy on real databases vs 𝟵𝟮.𝟵𝟲% for humans. The fix isn't a better model — it's 𝗴𝗿𝗼𝘂𝗻𝗱𝗶𝗻𝗴: feed real EXPLAIN (ANALYZE, BUFFERS) + pg_stat_statements + your version into every prompt.

━━━━━━━━━━━━━━━━━━━━

𝗪𝗵𝗲𝗿𝗲 𝗔𝗜 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗵𝗲𝗹𝗽𝘀 (𝗮𝗻𝗱 𝘄𝗵𝗲𝗿𝗲 𝗶𝘁 𝗹𝗶𝗲𝘀):

▸ Triage & summarize pg_stat_statements — 𝗛𝗶𝗴𝗵
▸ Read EXPLAIN plans in plain English — 𝗛𝗶𝗴𝗵
▸ Index & rewrite suggestions — 𝗠𝗲𝗱𝗶𝘂𝗺 (validate with hypopg, never auto-apply)
▸ Anomaly detection (DevOps Guru for RDS, pganalyze) — 𝗛𝗶𝗴𝗵
▸ Internals & DDL — 𝗟𝗼𝘄 / 𝗿𝗶𝘀𝗸𝘆 (human in front, always)

𝗢𝗻𝗲 𝗿𝗲𝗮𝗹 𝗲𝘅𝗮𝗺𝗽𝗹𝗲: a non-sargable date_trunc() on a 50M-row table, 4,200 ms. Fed the plan to Claude → it spotted the seq scan + missing composite index. Validated with 𝘩𝘺𝘱𝘰𝘱𝘨, built it CONCURRENTLY → 𝟯𝟴 𝗺𝘀 (~𝟭𝟭𝟬𝘅 𝗳𝗮𝘀𝘁𝗲𝗿). The AI got me to the right hypothesis in 30 seconds; hypopg made it safe.

━━━━━━━━━━━━━━━━━━━━

➡️ 𝗦𝘄𝗶𝗽𝗲 𝘁𝗵𝗲 𝗰𝗮𝗿𝗼𝘂𝘀𝗲𝗹 for the 9-step version (the grounding rule, the help/hurt matrix, the playbook).

📄 𝗙𝘂𝗹𝗹 𝗳𝗶𝗲𝗹𝗱 𝗴𝘂𝗶𝗱𝗲 (with SQL, the pgvector HNSW vs IVFFlat trade-off, and sources):
https://sendtoshailesh.github.io/blog/ai-postgresql-performance.html

Has AI helped or misled you on Postgres tuning? 👇

#PostgreSQL #Database #AI #DBA #Performance #pgvector

── END COPY ──
