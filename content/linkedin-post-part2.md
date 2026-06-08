# LinkedIn Post — Agent Eval Part 2 (Series Finale): Three Graders, 38 Tasks, and the $3-8 Safety Net

## Plain Text Version (copy-paste ready)

── START COPY ──

$3-8 per eval run.

A $47K agent loop ran for 11 days because nobody tested behavior. Three of our model regressions were caught before production — for less than the cost of a latte.

Here's the system (Part 2 of 2 — the finale of "SWE-bench Isn't Enough").

We built a three-layer grading stack across 38 tasks and 8 agents. The design principle: always use the cheapest grader that catches the failure.

Layer 1: Text grader — regex match on the response. Catches persona drift. Cost: $0.
Layer 2: Tool constraint — checks the tool call log, not the text. Catches fabrication (agent says "I deployed" but called zero tools). Cost: $0.
Layer 3: LLM judge — sends the full conversation to a second model with a rubric. Catches complex behavioral contracts. Cost: real tokens.

Two of three graders are free. That's by design.

What we actually caught:

- 3 agents simultaneously started answering sourdough bread questions after a model update. Text grader flagged all three — root cause was model-wide, not agent-specific.
- Our deployer agent decided a request carried "implicit confirmation" and started an Azure deployment without asking. Safety gate task caught it before real resources spun up.
- Agents stopped calling tools entirely — narrating work instead of doing it. Tool constraint grader caught empty call logs behind perfect-looking output.

The cost math: $3-8/run, 15-25 min parallel execution, 200K-400K tokens. During active dev, ~$180-800/month. Compare that to one rogue deployment with real billing.

Where to start: Week 1, pick your riskiest agent, write 2 YAML tasks (one happy-path, one off-topic). Both use $0 graders. Prove the concept before wiring CI. By Week 4, you have safety gates and LLM judges running on every PR.

Full 4-week playbook, all the YAML, and the 5 gotchas that cost me days — link in the first comment.

#AIAgents #AgentEval #GitHubCopilot #DevOps #AIEngineering

── END COPY ──


## FIRST COMMENT COPY

The complete build guide — three graders, four task patterns, CI pipeline, three regressions caught, and the 4-week playbook: https://sendtoshailesh.github.io/blog/agent-eval-part-2.html

Series finale. Start from Part 1 (the gap benchmarks miss): https://sendtoshailesh.github.io/blog/agent-eval-part-1.html

#AgentEval #AIEngineering

## END FIRST COMMENT COPY

Post the FIRST COMMENT within 60 seconds of publishing (link-in-body = reach penalty on LinkedIn).
