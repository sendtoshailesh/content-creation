# X/Twitter Thread — Part 2

**Source blog:** [Build the Eval System: Three Graders, 38 Tasks, and the $3-8 Safety Net](https://sendtoshailesh.github.io/blog/agent-eval-part-2.html)

**Supporting reference for the $47,000 failure comparison:** [Vectara — awesome-agent-failures](https://github.com/vectara/awesome-agent-failures)

## Thread

── START COPY ──
1/12 Most agent failures don't look broken. They look 𝗵𝗲𝗹𝗽𝗳𝘂𝗹. For 𝗣𝗮𝗿𝘁 𝟮 𝗼𝗳 𝟮, I built an eval system with 3 grader layers, 38 tasks, and a $3-8/run safety net. If you want agent CI that catches silent regressions, start here.

2/12 𝗟𝗮𝘆𝗲𝗿 𝟭 = `text` grader. Cost: $0. I use regex for off-topic refusal tests like sourdough. If the agent says "outside my scope" or redirects to Azure, pass. If it starts explaining hydration ratios, fail. Cheap, deterministic, fast.

3/12 𝗟𝗮𝘆𝗲𝗿 𝟮 = `tool_constraint`. Cost: $0. This checks what the agent 𝗱𝗶𝗱, not what it 𝘀𝗮𝗶𝗱. "I created the template" + no `create` call in the log = fail. This is how I catch fabrication without action.

4/12 Biggest setup gotcha: VS Code tool names != eval SDK names. `execute` -> `bash`, `read` -> `view`, `search` -> `grep`, `editFile` -> `edit`, `createFile` -> `create`. Get this wrong and every happy-path task looks broken.

5/12 𝗟𝗮𝘆𝗲𝗿 𝟯 = `prompt` grader. Cost: $$. I only pay for a judge when the contract is complex: gated steps, auth checks, "ask for 3+ inputs," or "don't claim work you never did." Cheapest grader first is the whole game.

6/12 One more trap: `continue_session: true`. Without it, the judge sees empty context, grades against nothing, and your eval goes red for the wrong reason. If you use LLM-as-judge, this flag is mandatory.

7/12 I used to think binary grading was a limitation. Now I think it's the feature. 𝗣𝗮𝘀𝘀/𝗳𝗮𝗶𝗹 is reproducible, actionable, and CI-friendly. "Did it ask for confirmation?" beats "3.7/5" every time when someone has to decide whether to merge.

8/12 Across 38 tasks, the failures collapsed into 4 patterns: happy-path, off-topic, safety gate, and gated step-1. That framing made new eval design simpler because I stopped inventing custom tests for every agent and started testing behavior classes.

9/12 Regression #1: persona erosion. After a helpfulness-tuned model update, 3 of 8 agents started answering the sourdough prompt instead of refusing. The $0 regex grader caught it fast, and the shared prompt made root cause obvious: model drift, not one bad agent file.

10/12 Regression #2 + #3 were scarier: one agent treated "deploy this" as implicit confirmation, and others narrated work without calling tools. No crashes. No errors. Perfectly coherent output. The eval stack caught both before those behaviors shipped with real credentials.

11/12 Cost profile: 8 agents, 16+ task executions, 15-25 min, ~200K-400K tokens, and about $3-8/run. Compared with a documented $47,000 agent failure loop, that spend is not overhead. It's insurance. https://github.com/vectara/awesome-agent-failures

12/12 My 4-week playbook: Week 1 = your riskiest agent + 2 tasks. Week 2 = sourdough across every agent. Week 3 = advisory PR comments in CI. Week 4 = safety gates + prompt graders. This concludes Part 2 of 2: https://sendtoshailesh.github.io/blog/agent-eval-part-2.html
── END COPY ──

## Standalone Single-Tweet Summary

── START COPY ──
𝗣𝗮𝗿𝘁 𝟮 𝗼𝗳 𝟮: 3 graders ($0 / $0 / $$), 38 tasks, 3 regressions caught, $3-8/run, and a 4-week rollout. Use regex for refusal, tool logs for action, and LLM judges for complex behavior. Cheapest grader first. https://sendtoshailesh.github.io/blog/agent-eval-part-2.html
── END COPY ──
