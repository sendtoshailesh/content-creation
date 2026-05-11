# X/Twitter Thread — Part 1: Context Engineering for AI Code Assistants

## Standalone Summary Tweet

── START COPY ──

Anthropic cut AI tool context by 85%. Accuracy jumped from 49% to 74%.

Five context engineering practices that make your AI code assistant produce better output while spending fewer tokens.

Thread below 🧵

── END COPY ──

---

## Full Thread (10 tweets)

── START COPY ──

1/ Anthropic loaded 50+ MCP tools into every prompt — 134,000 tokens before the conversation started.

They stripped it down to ~500 tokens.

Result: 𝟖𝟓% fewer tokens AND accuracy jumped from 49% to 74%.

Less context. Better output. 🧵

2/ This isn't an isolated finding.

SWEzze compressed code context by 6x — 51-71% fewer tokens.

Issue resolution improved by 5-9%.

The pattern is consistent: remove noise, get better results.

3/ Why? 30-70% of typical AI prompt context is noise.

▸ Stale files from a previous task
▸ Redundant info loaded through multiple paths
▸ Tool definitions you'll never use

Every noisy token dilutes the model's focus.

4/ 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗲 𝟏: Single-Task Focus

Close files unrelated to your current task before prompting.

12 files open, asking about 1 of them? The other 11 are noise.

Fewer files = more focused suggestions.

5/ 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗲 𝟐: Thread Hygiene

Start a new chat thread when you switch tasks.

Old auth logic in your chat history while you work on pagination? The model tries to reconcile both.

One thread per task. Two seconds. Clean slate.

6/ 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗲 𝟑: Targeted References

Use #file references instead of relying on "everything open."

Anthropic's Programmatic Tool Calling cut tokens by 37% while improving accuracy from 25.6% to 28.5%.

Targeted input > broad input.

7/ 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗲 𝟒: Front-Load Intent

State what you want in the first sentence. Details second.

"Add cursor-based pagination to #file:src/routes/users.ts with default page size 50."

Intent first. Context second.

8/ 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗲 𝟓: Stable Instructions

Create .github/copilot-instructions.md with your tech stack, conventions, and constraints.

The model starts every interaction with accurate project context instead of guessing.

Also enables prompt caching (up to 90% off).

9/ June 1, 2026: GitHub Copilot moves to usage-based billing.

Every token of junk context now has a visible cost.

But these 5 practices are worth doing even if AI were free. Better input = better output. Always.

10/ Part 1 of 3.

Next: prompt caching (90% savings) and the 120x model spread.

Full blog: [link]

What's your best context engineering tip? 👇

── END COPY ──

---

## Posting Notes

- **Best timing**: Tuesday-Thursday, 8-10am EST
- **Image**: Attach `content/visuals/context-quality-paradox.png` to tweet 1
- **Cadence**: Post all tweets in rapid succession (thread)
- **Engagement**: Reply to responses within 2 hours of posting
