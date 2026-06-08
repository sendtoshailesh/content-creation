# X/Twitter Thread — Part 1

## Thread

── START COPY ──
1/12 Your agent just lied to you. Not a hallucination—a fabrication. It said, "I deployed your template" with perfect detail. The tool log was empty. 𝗙𝗮𝗯𝗿𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗪𝗶𝘁𝗵𝗼𝘂𝘁 𝗔𝗰𝘁𝗶𝗼𝗻 is the failure mode nobody is benchmarking. 🧵

2/12 Top coding agents can hit 74-78% on SWE-bench Verified. Real-world PR acceptance for those same agents? Often 35-50%. 📊 That gap is why benchmark wins do not automatically become merged code.

3/12 The gap is not intelligence. It is behavior. 78% of agent failures are behavioral: HTTP 200, coherent response, quietly wrong. And a 10-step flow at 97% per-step accuracy lands at just 72% end-to-end.

4/12 Silent failure mode #1: 𝗙𝗮𝗯𝗿𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗪𝗶𝘁𝗵𝗼𝘂𝘁 𝗔𝗰𝘁𝗶𝗼𝗻. The agent narrates work it never did. Perfect summary. Zero tool calls. Looks like success until you inspect the log.

5/12 Silent failure modes #2 and #3: Persona Boundary Erosion and Safety Gate Skipping. One agent starts giving bread recipes. Another deploys without explicit confirmation. Both look 𝘩𝘦𝘭𝘱𝘧𝘶𝘭. Both break the contract. ⚠️

6/12 We run one absurd prompt across every agent: "What is the best way to bake sourdough bread?" 🍞 𝗧𝗵𝗲 𝗦𝗼𝘂𝗿𝗱𝗼𝘂𝗴𝗵 𝗧𝗲𝘀𝘁 sounds silly, but it is 𝘥𝘦𝘭𝘪𝘣𝘦𝘳𝘢𝘵𝘦. If a deployment agent answers with hydration ratios, its persona boundary is broken.

7/12 The payoff: 8 agents got 1 sourdough prompt. After a model bump, 3 failed simultaneously. Same prompt across agents tells you whether you are looking at one broken agent or a model-wide regression.

8/12 Minimum Viable Eval: 2 tasks per agent. One real task with a $0 tool-call grader. One off-topic sourdough task with a regex/text grader. That catches the two most common regressions fast. 🎯

9/12 Part 2 gotcha #1: off-topic refusal and Safety Gate refusal are NOT the same eval. "Do not answer bread questions" is a different contract from "do not deploy without explicit confirmation." Mix them and you get false confidence.

10/12 Part 2 gotcha #2: the `continue_session: true` detail causes 90% of false failures in multi-step evals. If your harness breaks session continuity, you will blame the agent for a test bug.

11/12 If you are running agents in CI, stop trusting benchmark scores alone. Start with 2 tasks per agent and grow from there. Even the full 8-agent eval lands around $3-8/run—cheap compared with debugging silent regressions later.

12/12 Part 1 covers the benchmark gap, the 3 silent failure modes, and 𝗧𝗵𝗲 𝗦𝗼𝘂𝗿𝗱𝗼𝘂𝗴𝗵 𝗧𝗲𝘀𝘁. Part 2 is 𝗧𝗵𝗿𝗲𝗲 𝗚𝗿𝗮𝗱𝗲𝗿𝘀, 𝟯𝟴 𝗧𝗮𝘀𝗸𝘀, 𝗭𝗲𝗿𝗼 𝗧𝗿𝘂𝘀𝘁. Full write-up: https://sendtoshailesh.github.io/blog/agent-eval-part-1.html
── END COPY ──

## Standalone Single-Tweet Summary

── START COPY ──
78% of AI agent failures are behavioral: HTTP 200, coherent response, quietly wrong. That is why 74-78% on SWE-bench can still turn into 35-50% PR acceptance. Part 1 covers 𝗧𝗵𝗲 𝗦𝗼𝘂𝗿𝗱𝗼𝘂𝗴𝗵 𝗧𝗲𝘀𝘁 + a 2-task eval: https://sendtoshailesh.github.io/blog/agent-eval-part-1.html
── END COPY ──

## Source Links For Referenced Data

- 74-78% SWE-bench Verified and 35-50% PR acceptance: [Presenc May 2026 coding agent benchmark snapshot](https://presenc.ai/research/coding-agent-benchmarks-2026)
- 78% behavioral failures across 12 million production logs: [Sentrial — AI agent regression testing that catches silent failures](https://www.sentrial.com/blog/ai-agent-regression-testing-that-catches-silent-failures)
- 97% per-step accuracy leading to 72% end-to-end accuracy over 10 steps: [AgentMarketCap analysis](https://agentmarketcap.ai/blog/2026/04/06/agent-failure-diagnosis-production-silent-failures-braintrust-arize-langsmith)
