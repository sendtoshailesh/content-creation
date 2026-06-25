<!-- LinkedIn posts for: content/from-prompts-to-loop-engineering.md -->
<!-- Canonical URL (FIRST COMMENT ONLY): https://sendtoshailesh.github.io/blog/loop-engineering-ai-native-development.html -->
<!-- Sequence per content/social-strategy.md: Day 0 lead (staircase) → Day 4 follow-up (nouns vs verbs) → Day 7 data/leadership follow-up -->
<!-- Voice: first-person practitioner. Avoid corporate filler verbs. LinkedIn native formatting only. -->

# LinkedIn Post 1 — Day 0 Lead (Staircase angle)

**Attach (in this order):** `content/visuals/p1-01-staircase.png` (lead), `content/visuals/p1-05-pull-quote.png` (second image)
**Visual hook note:** Slide 1 is the four-era staircase — the hook narrates what the reader just saw climbing up the stack.

── START COPY (LinkedIn Post — Day 0 Lead) ──

You're not getting better at prompting. The skill didn't improve — it moved.

That staircase up top is the whole story: prompt → context → harness → loop. Every two years the place where your effort actually matters climbs one step higher, because the model keeps absorbing the floor below you.

Here's what I keep seeing when I sit with teams shipping real software with agents — the people getting the most out of these tools aren't the ones with the cleverest wording. They stopped optimizing the sentence and started optimizing everything around it.

The four eras, fast:

▸ Prompt engineering — the wording of one request. Ceiling: you can phrase it perfectly and still get a confident answer to the wrong problem.
▸ Context engineering — what the model sees (conventions, architecture, lazy-loaded skills). Ceiling: a well-fed model still can't act.
▸ Harness engineering — everything around the model. A 100-line rig (mini-SWE-agent) resolves 65% of SWE-bench Verified tasks. Ceiling: a rig still needs a cycle to run in.
▸ Loop engineering — the cycle itself: plan → act → observe → verify → correct, with a stop condition.

Why now: code generation got cheap, so validation — not generation — is the bottleneck. By the time conventional CI finds the bug, the agent has already moved on.

Your first agentic loop this week — take one task you babysit line-by-line and give it four things:

1. A clear goal with a success criterion the agent can aim at.
2. The tools to iterate — the CLI, the test runner, the linter.
3. One machine-checkable feedback signal — tests passing, types clean.
4. A stop condition — a max iteration count or a definition of done.
5. Then step ON the loop: next time it's wrong, fix the loop, not the output.

Proof it scales: Stripe's agents ship 1,300+ PRs a week (up from ~1,000) with zero human-written code, underpinning $1T+ in annual payment volume. Same direction on a fixed harness — SWE-bench Verified climbed from 12.47% (Mar 2024) to 76.8% (Feb 2026) on identical infrastructure.

This window won't reverse. As models absorb more of the work, the unit of work you own keeps rising. Right now it's the loop.

Don't just nod at this — close one loop this week. The lowest-friction start: open an agent with a verify→correct loop — GitHub Copilot agent mode, Aider, or Claude Code — give it a failing-test task, and watch it edit → run tests → read the failures → retry on its own (Copilot's Chat Debug View also lets you see the prompts and tool calls behind the run). You'll know it worked when your test command exits 0 on an edit you didn't write. Two harder builds (the loop on a managed runtime, then platform-engineering it with gates) in the first comment.

So which step are you standing on — word, context, rig, or loop? Tell me below. 👇

#AINativeDevelopment #LoopEngineering #HarnessEngineering #AgenticLoops #SoftwareEngineering

── END COPY ──

---

── UNICODE VERSION ──
── START COPY ──

𝗬𝗼𝘂'𝗿𝗲 𝗻𝗼𝘁 𝗴𝗲𝘁𝘁𝗶𝗻𝗴 𝗯𝗲𝘁𝘁𝗲𝗿 𝗮𝘁 𝗽𝗿𝗼𝗺𝗽𝘁𝗶𝗻𝗴. The skill didn't improve — 𝘪𝘵 𝘮𝘰𝘷𝘦𝘥.

That staircase up top is the whole story: prompt → context → harness → loop. Every two years the place where your effort actually matters climbs one step higher, because the model keeps absorbing the floor below you.

Here's what I keep seeing sitting with teams shipping real software with agents — the people getting the most out of these tools aren't the ones with the cleverest wording. They stopped optimizing the sentence and started optimizing everything around it.

━━━

📊 𝗧𝗵𝗲 𝗳𝗼𝘂𝗿 𝗲𝗿𝗮𝘀, 𝗳𝗮𝘀𝘁:

▸ 𝗣𝗿𝗼𝗺𝗽𝘁 — the wording of one request. Ceiling: perfect phrasing, wrong problem.
▸ 𝗖𝗼𝗻𝘁𝗲𝘅𝘁 — what the model sees. Ceiling: a well-fed model still can't 𝘢𝘤𝘵.
▸ 𝗛𝗮𝗿𝗻𝗲𝘀𝘀 — everything around the model. A 𝟭𝟬𝟬-𝗹𝗶𝗻𝗲 rig resolves 𝟲𝟱% of SWE-bench Verified. Ceiling: no cycle to run in.
▸ 𝗟𝗼𝗼𝗽 — the cycle itself: plan → act → observe → verify → correct, with a stop condition.

━━━

🎯 𝗪𝗵𝘆 𝗻𝗼𝘄: code generation got cheap, so 𝘃𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗼𝗻 — 𝗻𝗼𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 — 𝗶𝘀 𝘁𝗵𝗲 𝗯𝗼𝘁𝘁𝗹𝗲𝗻𝗲𝗰𝗸. By the time CI finds the bug, the agent has already moved on.

━━━

✅ 𝗬𝗼𝘂𝗿 𝗳𝗶𝗿𝘀𝘁 𝗮𝗴𝗲𝗻𝘁𝗶𝗰 𝗹𝗼𝗼𝗽 𝘁𝗵𝗶𝘀 𝘄𝗲𝗲𝗸:

1. A clear 𝗴𝗼𝗮𝗹 with a success criterion.
2. The 𝘁𝗼𝗼𝗹𝘀 to iterate — CLI, test runner, linter.
3. One machine-checkable 𝗳𝗲𝗲𝗱𝗯𝗮𝗰𝗸 𝘀𝗶𝗴𝗻𝗮𝗹.
4. A 𝘀𝘁𝗼𝗽 𝗰𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻 so the loop ends on purpose.
5. Then step 𝗢𝗡 the loop: next time it's wrong, 𝘧𝘪𝘹 𝘵𝘩𝘦 𝘭𝘰𝘰𝘱, 𝘯𝘰𝘵 𝘵𝘩𝘦 𝘰𝘶𝘵𝘱𝘶𝘵.

━━━

📊 𝗣𝗿𝗼𝗼𝗳 𝗶𝘁 𝘀𝗰𝗮𝗹𝗲𝘀: Stripe's agents ship 𝟭,𝟯𝟬𝟬+ 𝗣𝗥𝘀/𝘄𝗲𝗲𝗸 with 𝘇𝗲𝗿𝗼 𝗵𝘂𝗺𝗮𝗻-𝘄𝗿𝗶𝘁𝘁𝗲𝗻 𝗰𝗼𝗱𝗲, behind $𝟭𝗧+ in annual payments. On a fixed harness, SWE-bench Verified climbed 𝟭𝟮.𝟰𝟳% → 𝟳𝟲.𝟴% in two years.

The unit of work you own keeps rising. Right now it's 𝘁𝗵𝗲 𝗹𝗼𝗼𝗽.

🔨 𝗖𝗹𝗼𝘀𝗲 𝗼𝗻𝗲 𝗹𝗼𝗼𝗽 𝘁𝗵𝗶𝘀 𝘄𝗲𝗲𝗸: open an agent with a verify→correct loop (GitHub Copilot agent mode, Aider, or Claude Code) on a failing-test task and watch it run itself — Copilot's 𝗖𝗵𝗮𝘁 𝗗𝗲𝗯𝘂𝗴 𝗩𝗶𝗲𝘄 also shows the prompts and tool calls behind it. You'll know it worked when 𝘆𝗼𝘂𝗿 𝘁𝗲𝘀𝘁𝘀 𝗲𝘅𝗶𝘁 𝟬 on an edit 𝘺𝘰𝘶 𝘥𝘪𝘥𝘯'𝘵 𝘸𝘳𝘪𝘵𝘦. Two harder builds (a managed runtime, then platform-engineering with gates) in the first comment.

𝘞𝘩𝘪𝘤𝘩 𝘴𝘵𝘦𝘱 𝘢𝘳𝘦 𝘺𝘰𝘶 𝘴𝘵𝘢𝘯𝘥𝘪𝘯𝘨 𝘰𝘯 — word, context, rig, or loop? Tell me below. 👇

#AINativeDevelopment #LoopEngineering #HarnessEngineering #AgenticLoops #SoftwareEngineering

── END COPY ──

---

── FIRST COMMENT COPY ──

The full four-era breakdown — prompt → context → harness → loop, with the Stripe and SWE-bench data and the practitioners who named the arc (Willison, Böckeler, Morris, Anthropic): https://sendtoshailesh.github.io/blog/loop-engineering-ai-native-development.html

Three build-it-yourself projects from the post, beginner → advanced (each lists interchangeable tools — pick whichever you already have):
• Run a verify→correct loop in an agent — Copilot agent mode, Aider, or Claude Code: https://code.visualstudio.com/docs/agents/overview
• Build the loop on a managed runtime — Foundry Agent Service or Anthropic's agent patterns: https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent
• Platform-engineer the loop with gates — git-ape, hve-core, or mini-swe-agent: https://github.com/Azure/git-ape

Start with the first one — once you've watched a test suite close a loop you didn't babysit, the whole idea stops being abstract.
#AINativeDevelopment #LoopEngineering

── END FIRST COMMENT COPY ──

Post the FIRST COMMENT within 60 seconds of publishing (link-in-body = reach penalty on LinkedIn).

IMAGE UPLOAD:
- content/visuals/p1-01-staircase.png (lead image — the four-era staircase)
- content/visuals/p1-05-pull-quote.png (second image — the reframe pull-quote)

---
---

# LinkedIn Post 2 — Day 4 Follow-up (Harness vs. loop = nouns vs. verbs)

**Attach (in this order):** `content/visuals/p1-03-harness-vs-loop.png` (lead), `content/visuals/p2-02-postures.png` (second image)
**Visual hook note:** Slide 1 splits nouns (the assembled parts and sensors) from verbs (the act → observe → verify → retry cycle with a stop gate) — the hook narrates that split.

── START COPY (LinkedIn Post — Day 4 Follow-up) ──

Harness and loop are not the same thing. One is nouns. One is verbs. I conflated them for months, and almost every write-up still does.

Last week I argued the skill moved up a staircase — prompt → context → harness → loop. Here's the distinction inside that top step that took me too long to see clearly.

The harness is the rig — the equipment. It's nouns:

▸ The skills and CLIs the agent calls
▸ The test suite and the type checker
▸ The static analysis and the guardrails
▸ The VS Code team's breakdown: context assembly + tool exposure + tool execution — "the harness is the product"
▸ Böckeler's one-liner corroborates: a harness is "everything except the model"

The loop is the cycle — the verbs. It's what uses the rig:

▸ Act → observe the sensors → verify against the goal → decide retry or stop
▸ Anthropic's evaluator-optimizer: one model generates while another evaluates "in a loop"
▸ The part people skip: a stop condition — "a maximum number of iterations to maintain control"
▸ A loop without a stop condition isn't autonomy; it's a way to burn tokens

The test that separates them — the one diagnostic I now use on every team:

1. You're inside the work and you don't like what the agent produced.
2. Do you fix the OUTPUT? That's editing.
3. Or do you change the thing that PRODUCED it — the rig, and the cycle that runs against it? That's engineering.

This maps onto where you stand. Kief Morris names four postures: outside the loop (vibe coding), in the loop (you gatekeep every line), on the loop (you tune the cycle), and the flywheel (agents improve the loop itself).

The trap is "in the loop." It feels responsible — and you become the bottleneck the moment the agent generates faster than you can read. The whole move is from fixing the output to fixing the loop that produces it.

Mature production setups are both at once: Stripe's "blueprints," Anthropic's "Dynamic Workflows," and open frameworks like Azure/git-ape (a public, MIT-licensed agentic deploy loop) are each a harness PLUS an explicit, code-defined loop with verification and stop logic.

So: when you dislike the output, what do you change — the artifact, or the producer? That answer tells you which posture you're in.

Full write-up and the four-posture map in the first comment. 👇

#LoopEngineering #HarnessEngineering #AgenticLoops #AINativeDevelopment #SoftwareEngineering

── END COPY ──

---

── UNICODE VERSION ──
── START COPY ──

𝗛𝗮𝗿𝗻𝗲𝘀𝘀 𝗮𝗻𝗱 𝗹𝗼𝗼𝗽 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝘀𝗮𝗺𝗲 𝘁𝗵𝗶𝗻𝗴. One is 𝗻𝗼𝘂𝗻𝘀. One is 𝘃𝗲𝗿𝗯𝘀. I conflated them for months, and almost every write-up still does.

Last week I argued the skill moved up a staircase — prompt → context → harness → loop. Here's the distinction inside that top step that took me too long to see.

━━━

🏋️ 𝗧𝗵𝗲 𝗵𝗮𝗿𝗻𝗲𝘀𝘀 = 𝘁𝗵𝗲 𝗿𝗶𝗴 (𝗻𝗼𝘂𝗻𝘀):

▸ The skills and CLIs the agent calls
▸ The test suite and the type checker
▸ Static analysis and guardrails
▸ VS Code: context assembly + tool exposure + tool execution — 𝘵𝘩𝘦 𝘩𝘢𝘳𝘯𝘦𝘴𝘴 𝘪𝘴 𝘵𝘩𝘦 𝘱𝘳𝘰𝘥𝘶𝘤𝘵
▸ Böckeler corroborates: a harness is 𝘦𝘷𝘦𝘳𝘺𝘵𝘩𝘪𝘯𝘨 𝘦𝘹𝘤𝘦𝘱𝘵 𝘵𝘩𝘦 𝘮𝘰𝘥𝘦𝘭

━━━

🔁 𝗧𝗵𝗲 𝗹𝗼𝗼𝗽 = 𝘁𝗵𝗲 𝗰𝘆𝗰𝗹𝗲 (𝘃𝗲𝗿𝗯𝘀):

▸ Act → observe → verify → decide retry or stop
▸ Anthropic's evaluator-optimizer: generate while another model evaluates "in a loop"
▸ The part people skip: a 𝘀𝘁𝗼𝗽 𝗰𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻
▸ A loop without one isn't autonomy — it's a way to burn tokens

━━━

🎯 𝗧𝗵𝗲 𝘁𝗲𝘀𝘁 𝘁𝗵𝗮𝘁 𝘀𝗲𝗽𝗮𝗿𝗮𝘁𝗲𝘀 𝘁𝗵𝗲𝗺:

1. You don't like what the agent produced.
2. Fix the 𝗢𝗨𝗧𝗣𝗨𝗧? That's 𝘦𝘥𝘪𝘵𝘪𝘯𝘨.
3. Change what 𝗣𝗥𝗢𝗗𝗨𝗖𝗘𝗗 it — the rig and the cycle? That's 𝘦𝘯𝘨𝘪𝘯𝘦𝘦𝘳𝘪𝘯𝘨.

━━━

Morris names four postures: 𝗼𝘂𝘁𝘀𝗶𝗱𝗲 the loop (vibe coding), 𝗶𝗻 the loop (you gatekeep every line), 𝗼𝗻 the loop (you tune the cycle), and the 𝗳𝗹𝘆𝘄𝗵𝗲𝗲𝗹.

⚠️ The trap is 𝘪𝘯 𝘵𝘩𝘦 𝘭𝘰𝘰𝘱 — you become the bottleneck the moment the agent generates faster than you can read.

Mature setups are both at once: Stripe's "blueprints", Anthropic's "Dynamic Workflows", and open frameworks like Azure/git-ape (a public agentic deploy loop) = a harness 𝗽𝗹𝘂𝘀 an explicit, code-defined loop.

𝘞𝘩𝘦𝘯 𝘺𝘰𝘶 𝘥𝘪𝘴𝘭𝘪𝘬𝘦 𝘵𝘩𝘦 𝘰𝘶𝘵𝘱𝘶𝘵, 𝘸𝘩𝘢𝘵 𝘥𝘰 𝘺𝘰𝘶 𝘤𝘩𝘢𝘯𝘨𝘦 — the artifact, or the producer? 👇

#LoopEngineering #HarnessEngineering #AgenticLoops #AINativeDevelopment #SoftwareEngineering

── END COPY ──

---

── FIRST COMMENT COPY ──

The full breakdown — harness vs. loop, the four postures (outside/in/on the loop + flywheel), and why "in the loop" is the bottleneck: https://sendtoshailesh.github.io/blog/loop-engineering-ai-native-development.html

Want to feel the nouns-vs-verbs distinction instead of just reading it? Build the loop on a managed runtime — an agent + conversation + one tool, run with a capped iteration count as your stop condition (half a day). Pick whichever you have: Microsoft Foundry Agent Service (https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent) or Anthropic's `patterns/agents` recipes (https://github.com/anthropics/claude-cookbooks) — the loop is identical either way.
#LoopEngineering #HarnessEngineering

── END FIRST COMMENT COPY ──

Post the FIRST COMMENT within 60 seconds of publishing (link-in-body = reach penalty on LinkedIn).

IMAGE UPLOAD:
- content/visuals/p1-03-harness-vs-loop.png (lead image — nouns vs. verbs)
- content/visuals/p2-02-postures.png (second image — the four postures)

---
---

# LinkedIn Post 3 — Day 7 Data / Leadership Follow-up (Why now)

**Attach (in this order):** `content/visuals/p2-04-stripe-swebench.png` (lead), `content/visuals/p2-03-bottleneck.png` (second image)
**Visual hook note:** Slide 1 is the Stripe + SWE-bench data exhibit — the hook narrates the numbers the reader just saw.

── START COPY (LinkedIn Post — Day 7 Data/Leadership Follow-up) ──

Stripe ships 1,300+ pull requests a week with zero human-written code — underpinning $1 trillion+ in annual payment volume. If you're leading engineers, that number should reframe what you're budgeting for.

For two weeks I've argued the unit of work moved up a staircase — prompt → context → harness → loop. Here's the economic reason it happened in 2026 specifically: the bottleneck inverted.

The numbers worth carrying into a planning meeting:

▸ Stripe's autonomous agents: 1,300+ PRs/week (up from ~1,000), every one machine-generated and human-reviewed
▸ A public production loop you can read end to end: Azure/git-ape — an MIT-licensed agentic deploy harness (plan → PR → security/cost gate → deploy), one of several inspectable examples alongside mini-swe-agent and Aider
▸ SWE-bench Verified: 12.47% (Mar 2024) → 76.8% (Feb 2026) — illustrative, not a scoreboard; scores track the harness, which is why OpenAI stopped reporting it
▸ Per-task cost on that leaderboard: ~$0.05 to $0.96 per instance, depending on model
▸ The pricing is "still very subsidized" (Böckeler) — a snapshot, not a forecast. Re-pull before you budget on it.
▸ CircleCI's read on the cause: "by the time conventional CI discovers an issue, the AI agent has already moved on, losing valuable context"

What that means for how you run a team:

1. Generation is no longer the constraint — validation is. Plan capacity around review and verification, not typing speed.
2. Pull verification into the inner loop — CircleCI's Chunk Sidecars, Dropbox Nova, Claude Code's iterative validation all move the check inside the cycle.
3. Engineer the loop, not the output — the durable skill is governing the cycle: goal, tools, one feedback signal, a stop condition.
4. Budget for the failure modes — agentic laziness (declares done early), self-preferential bias (rates its own work too highly), goal drift. Verification gates are the defense.
5. Treat costs with an asterisk — today's per-token pricing is subsidized; model the real number before you commit.

The honest counterweight: this isn't a victory lap. The sources I trust most are the ones that name what still breaks — which is exactly why you engineer stop conditions instead of trusting the loop to police itself.

The trajectory is durable even if any single number isn't: as models absorb more of the work, the place where your effort matters keeps climbing. Right now it's the loop.

If you're sizing your 2026 engineering plan around lines of code, you're measuring the part that got cheap. What are you measuring instead? 👇

Full data and sources in the first comment.

#EngineeringLeadership #AINativeDevelopment #LoopEngineering #AIStrategy #SoftwareEngineering

── END COPY ──

---

── UNICODE VERSION ──
── START COPY ──

𝗦𝘁𝗿𝗶𝗽𝗲 𝘀𝗵𝗶𝗽𝘀 𝟭,𝟯𝟬𝟬+ 𝗽𝘂𝗹𝗹 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝘀 𝗮 𝘄𝗲𝗲𝗸 𝘄𝗶𝘁𝗵 𝘇𝗲𝗿𝗼 𝗵𝘂𝗺𝗮𝗻-𝘄𝗿𝗶𝘁𝘁𝗲𝗻 𝗰𝗼𝗱𝗲 — behind $𝟭 𝘁𝗿𝗶𝗹𝗹𝗶𝗼𝗻+ in annual payment volume. If you lead engineers, that number should reframe what you budget for.

For two weeks I've argued the unit of work moved up a staircase — prompt → context → harness → loop. Here's the economic reason it happened in 2026: 𝘁𝗵𝗲 𝗯𝗼𝘁𝘁𝗹𝗲𝗻𝗲𝗰𝗸 𝗶𝗻𝘃𝗲𝗿𝘁𝗲𝗱.

━━━

📊 𝗧𝗵𝗲 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝗽𝗹𝗮𝗻𝗻𝗶𝗻𝗴 𝗺𝗲𝗲𝘁𝗶𝗻𝗴:

▸ Stripe: 𝟭,𝟯𝟬𝟬+ 𝗣𝗥𝘀/𝘄𝗲𝗲𝗸, every one machine-generated and human-reviewed
▸ A public loop you can read: 𝗔𝘇𝘂𝗿𝗲/𝗴𝗶𝘁-𝗮𝗽𝗲 (MIT) — one of several inspectable examples, alongside mini-swe-agent and Aider
▸ SWE-bench Verified: 𝟭𝟮.𝟰𝟳% → 𝟳𝟲.𝟴% — illustrative; scores track the harness (OpenAI stopped reporting it)
▸ Per-task cost: ~$𝟬.𝟬𝟱 to $𝟬.𝟵𝟲 per instance
▸ Pricing is 𝘴𝘵𝘪𝘭𝘭 𝘷𝘦𝘳𝘺 𝘴𝘶𝘣𝘴𝘪𝘥𝘪𝘻𝘦𝘥 (Böckeler) — re-pull before you budget on it
▸ CircleCI: "by the time conventional CI discovers an issue, the agent has already moved on"

━━━

🎯 𝗪𝗵𝗮𝘁 𝗶𝘁 𝗺𝗲𝗮𝗻𝘀 𝗳𝗼𝗿 𝗿𝘂𝗻𝗻𝗶𝗻𝗴 𝗮 𝘁𝗲𝗮𝗺:

1. 𝗩𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗼𝗻 is the constraint now, not generation. Plan capacity around review.
2. Pull verification 𝗶𝗻𝘁𝗼 𝘁𝗵𝗲 𝗶𝗻𝗻𝗲𝗿 𝗹𝗼𝗼𝗽.
3. Engineer the 𝗹𝗼𝗼𝗽, not the output.
4. Budget for the 𝗳𝗮𝗶𝗹𝘂𝗿𝗲 𝗺𝗼𝗱𝗲𝘀 — laziness, self-preferential bias, goal drift.
5. Treat costs with an 𝗮𝘀𝘁𝗲𝗿𝗶𝘀𝗸 — today's pricing is subsidized.

━━━

⚠️ The honest counterweight: this isn't a victory lap. The sources I trust most name what still breaks — which is exactly why you engineer stop conditions instead of trusting the loop to police itself.

𝘐𝘧 𝘺𝘰𝘶'𝘳𝘦 𝘴𝘪𝘻𝘪𝘯𝘨 𝘺𝘰𝘶𝘳 𝟮𝟬𝟮𝟲 𝘱𝘭𝘢𝘯 𝘢𝘳𝘰𝘶𝘯𝘥 𝘭𝘪𝘯𝘦𝘴 𝘰𝘧 𝘤𝘰𝘥𝘦, you're measuring the part that got cheap. What are you measuring instead? 👇

#EngineeringLeadership #AINativeDevelopment #LoopEngineering #AIStrategy #SoftwareEngineering

── END COPY ──

---

── FIRST COMMENT COPY ──

The full data and sources — Stripe Minions, the SWE-bench trajectory (12.47% → 76.8% on a fixed harness), per-task costs, and the failure modes worth budgeting for: https://sendtoshailesh.github.io/blog/loop-engineering-ai-native-development.html

Want your own read on the economics instead of trusting mine? Platform-engineer your own deploy loop with gates — run git-ape headless (or hve-core, or mini-swe-agent): issue → PR → plan → security/cost gate → deploy, then tune a gate and re-run to change the outcome (a weekend): https://github.com/Azure/git-ape
#EngineeringLeadership #LoopEngineering

── END FIRST COMMENT COPY ──

Post the FIRST COMMENT within 60 seconds of publishing (link-in-body = reach penalty on LinkedIn).

IMAGE UPLOAD:
- content/visuals/p2-04-stripe-swebench.png (lead image — Stripe before/after + SWE-bench trajectory)
- content/visuals/p2-03-bottleneck.png (second image — generation vs. validation bottleneck)
