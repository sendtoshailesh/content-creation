# Reel Script: The Complete Agent Eval System in 75 Seconds

**Duration:** 75 seconds
**Format:** Quick explainer
**Platforms:** Instagram Reels, YouTube Shorts, LinkedIn Video
**Source blog:** [Build the Eval System: Three Graders, 38 Tasks, and the $3-8 Safety Net](https://sendtoshailesh.github.io/blog/agent-eval-part-2.html)
**Supporting reference for the $47,000 failure hook:** [Vectara — awesome-agent-failures](https://github.com/vectara/awesome-agent-failures)

---

## Shot List

| Time | Screen Cue | Voiceover | Text Overlay |
|---|---|---|---|
| 0:00-0:06 | Talking head. Big cost graphic: `$3-8` vs `$47,000`. | "$3-8 per eval run catches what $47,000 in failures don't." | **$3-8 catches what $47K misses** |
| 0:06-0:16 | Fast cuts: sourdough prompt, regex match, PASS badge. | "Layer 1 is the `text` grader. Cost: zero. I use regex for off-topic refusal checks like the sourdough test." | **Layer 1: text grader / $0** |
| 0:16-0:26 | Split screen: polished agent reply on left, empty tool log on right. | "Layer 2 is `tool_constraint`. Also zero. It checks what the agent did, not what it said. Perfect answer, no tool call, fail." | **Layer 2: tool log / $0** |
| 0:26-0:36 | YAML rubric zoom-in. Highlight `continue_session: true`. | "Layer 3 is the `prompt` grader. That's where I spend money: gated steps, safety checks, and binary pass-fail judgments on complex behavior." | **Layer 3: prompt judge / $$** |
| 0:36-0:46 | Tool name mapping graphic and three red bug cards. | "This stack caught three silent regressions: 3 of 8 agents answering sourdough, one deploy flow skipping confirmation, and agents narrating work without calling tools. Plus one huge gotcha: `execute` maps to `bash`." | **3 regressions caught** |
| 0:46-0:56 | Cost dashboard: 8 agents, 16+ tasks, 15-25 min, 200K-400K tokens. | "The full run covers 8 agents and 16-plus task executions in 15 to 25 minutes, around 200K to 400K tokens, for about $3 to $8." | **8 agents / 16+ tasks / $3-8** |
| 0:56-1:08 | Four sticky notes animate in: Week 1, Week 2, Week 3, Week 4. | "My 4-week playbook is simple: Week 1, test your riskiest agent with 2 tasks. Week 2, run sourdough across every agent. Week 3, post advisory PR comments. Week 4, add safety gates and prompt graders." | **4-week rollout** |
| 1:08-1:15 | Talking head. Canonical URL lower third. | "That is the full eval system. This concludes Part 2 of 2. If your agents touch real credentials or real billing, evals are infrastructure. Full guide linked in the description." | **Part 2 of 2 / Full guide below** |

---

## Full Voiceover Script

> "$3-8 per eval run catches what $47,000 in failures don't."
>
> Layer 1 is the `text` grader. Cost: zero. I use regex for off-topic refusal checks like the sourdough test.
>
> Layer 2 is `tool_constraint`. Also zero. It checks what the agent did, not what it said. Perfect answer, no tool call, fail.
>
> Layer 3 is the `prompt` grader. That's where I spend money: gated steps, safety checks, and binary pass-fail judgments on complex behavior.
>
> This stack caught three silent regressions: 3 of 8 agents answering sourdough, one deploy flow skipping confirmation, and agents narrating work without calling tools. Plus one huge gotcha: `execute` maps to `bash`.
>
> The full run covers 8 agents and 16-plus task executions in 15 to 25 minutes, around 200K to 400K tokens, for about $3 to $8.
>
> My 4-week playbook is simple: Week 1, test your riskiest agent with 2 tasks. Week 2, run sourdough across every agent. Week 3, post advisory PR comments. Week 4, add safety gates and prompt graders.
>
> That is the full eval system. This concludes Part 2 of 2. If your agents touch real credentials or real billing, evals are infrastructure. Full guide linked in the description.

---

## Production Notes

- Keep cuts fast in the first 36 seconds so all three graders land before attention drops.
- Use one clean tool-name mapping visual: `execute -> bash`, `read -> view`, `search -> grep`, `editFile -> edit`, `createFile -> create`.
- Make the binary grading point visual with a large `PASS / FAIL` card, not a score dial.
- Show the cost card with all 4 numbers together: `8 agents`, `16+ tasks`, `200K-400K tokens`, `$3-8/run`.
- Lower-third URL on the final shot: `sendtoshailesh.github.io/blog/agent-eval-part-2.html`.

---

## Platform Captions

### Instagram Reels

── START COPY ──
$3-8 per eval run catches what $47,000 in failures don't.

That was the core lesson from building this agent eval stack:
- `text` grader for off-topic refusal checks
- `tool_constraint` for action vs narration
- `prompt` grader for gated behavior and safety contracts

It caught 3 silent regressions across 38 tasks, and the rollout path was a 4-week playbook, not a giant rewrite.

This concludes Part 2 of 2.
Full guide: https://sendtoshailesh.github.io/blog/agent-eval-part-2.html
Reference for the $47,000 failure example: https://github.com/vectara/awesome-agent-failures

#AIAgents #AgentEval #LLMOps #AIEngineering #DevOps #GitHubCopilot
── END COPY ──

### YouTube Shorts

── START COPY ──
The full agent eval system in 75 seconds:

3 graders.
38 tasks.
3 regressions caught.
$3-8 per run.

What mattered most was using the cheapest grader that catches the failure:
- regex for refusal
- tool logs for action
- LLM judge for complex behavior

This concludes Part 2 of 2.
Full post: https://sendtoshailesh.github.io/blog/agent-eval-part-2.html
Failure reference: https://github.com/vectara/awesome-agent-failures

#AIAgents #AgentEvaluation #Shorts #LLMOps #AIEngineering #CICD
── END COPY ──

### LinkedIn Video

── START COPY ──
𝗧𝗵𝗲 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲 𝗮𝗴𝗲𝗻𝘁 𝗲𝘃𝗮𝗹 𝘀𝘆𝘀𝘁𝗲𝗺, 𝗶𝗻 𝟳𝟱 𝘀𝗲𝗰𝗼𝗻𝗱𝘀.

The stack is simple:
▸ `text` grader for off-topic refusal checks
▸ `tool_constraint` for fabricated action
▸ `prompt` grader for safety gates and complex behavior

It caught 3 silent regressions, covered 38 tasks, and cost about $3-8 per run across 8 agents.

The most practical takeaway: start with your riskiest agent, then expand over 4 weeks.

This concludes Part 2 of 2.
Full guide: https://sendtoshailesh.github.io/blog/agent-eval-part-2.html
Reference for the $47,000 failure example: https://github.com/vectara/awesome-agent-failures

#AIAgents #AgentEval #AIEngineering #LLMOps #DevOps #GitHubCopilot
── END COPY ──
