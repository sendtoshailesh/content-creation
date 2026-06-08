# LinkedIn Post (Unicode Formatted) — Agent Eval Part 2 (Series Finale): Three Graders, 38 Tasks, and the $3-8 Safety Net

## Unicode Formatted Version (copy-paste ready)

── START COPY ──

$3-8 per eval run.

A $47K agent loop ran for 11 days because nobody tested behavior. Three of our model regressions were caught before production — for less than the cost of a latte.

━━━

🔬 Here's the system (Part 2 of 2 — the finale of "AI Agent Evals: Why SWE-bench Isn't Enough").

We built a three-layer grading stack across 38 tasks and 8 agents. The design principle: 𝗮𝗹𝘄𝗮𝘆𝘀 𝘂𝘀𝗲 𝘁𝗵𝗲 𝗰𝗵𝗲𝗮𝗽𝗲𝘀𝘁 𝗴𝗿𝗮𝗱𝗲𝗿 𝘁𝗵𝗮𝘁 𝗰𝗮𝘁𝗰𝗵𝗲𝘀 𝘁𝗵𝗲 𝗳𝗮𝗶𝗹𝘂𝗿𝗲.

━━━

📊 𝗧𝗵𝗲 𝗧𝗵𝗿𝗲𝗲 𝗟𝗮𝘆𝗲𝗿𝘀

▸ 𝗟𝗮𝘆𝗲𝗿 𝟭: Text grader — regex match on response. Catches persona drift. Cost: $0
▸ 𝗟𝗮𝘆𝗲𝗿 𝟮: Tool constraint — checks the tool call log, not text. Catches fabrication ("I deployed" but called zero tools). Cost: $0
▸ 𝗟𝗮𝘆𝗲𝗿 𝟯: LLM judge — sends full conversation to a second model with a rubric. Catches complex behavioral contracts. Cost: $$

Two of three graders are free. 𝘛𝘩𝘢𝘵'𝘴 𝘣𝘺 𝘥𝘦𝘴𝘪𝘨𝘯.

━━━

⚠️ 𝗧𝗵𝗿𝗲𝗲 𝗥𝗲𝗴𝗿𝗲𝘀𝘀𝗶𝗼𝗻𝘀 𝗪𝗲 𝗔𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗖𝗮𝘂𝗴𝗵𝘁

▸ 3 agents started answering sourdough questions after a model update — text grader flagged all three. Root cause: model-wide, not agent-specific
▸ Deployer agent decided a request was "implicit confirmation" — started Azure deployment without asking. Safety gate caught it before real resources spun up
▸ Agents stopped calling tools entirely — narrating work instead of doing it. Tool constraint grader caught empty call logs behind 𝘱𝘦𝘳𝘧𝘦𝘤𝘵-𝘭𝘰𝘰𝘬𝘪𝘯𝘨 output

━━━

💰 𝗧𝗵𝗲 𝗖𝗼𝘀𝘁 𝗠𝗮𝘁𝗵

▸ $3-8/run, 15-25 min parallel, 200K-400K tokens
▸ Active dev: ~$180-800/month
▸ Compare: one rogue deployment with real billing. Or a $47K runaway loop

━━━

🎯 𝗪𝗵𝗲𝗿𝗲 𝘁𝗼 𝗦𝘁𝗮𝗿𝘁

Week 1: Riskiest agent, 2 YAML tasks. Both use $0 graders
Week 2: Sourdough Test across all agents
Week 3: Wire into CI as advisory (not blocking)
Week 4: Safety gates + LLM judges on every PR

Full 4-week playbook, all the YAML, and the 5 gotchas that cost me days — link in the first comment 👇

#AIAgents #AgentEval #GitHubCopilot #DevOps #AIEngineering

── END COPY ──


## FIRST COMMENT COPY

The complete build guide — three graders, four task patterns, CI pipeline, three regressions caught, and the 4-week playbook: https://sendtoshailesh.github.io/blog/agent-eval-part-2.html

Series finale. Start from Part 1 (the gap benchmarks miss): https://sendtoshailesh.github.io/blog/agent-eval-part-1.html

#AgentEval #AIEngineering

## END FIRST COMMENT COPY

Post the FIRST COMMENT within 60 seconds of publishing (link-in-body = reach penalty on LinkedIn).
