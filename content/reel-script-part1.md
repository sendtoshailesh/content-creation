# Reel Script: Spend Fewer Tokens, Get Better Code

**Duration**: 60 seconds (Reels/Shorts) / 75 seconds (LinkedIn Video)
**Format**: A — "Did You Know?" (Data Shock)
**Platforms**: Instagram Reels, YouTube Shorts, LinkedIn Video
**Aspect ratio**: 9:16 (1080x1920)
**Source**: `content/context-engineering-part-1.md`

---

## Shot List

| Time | Visual | Voiceover | Text Overlay |
|------|--------|-----------|--------------|
| 0:00-0:04 | VS Code with 15+ file tabs open, Copilot Chat producing garbled/wrong output | "Your AI code assistant is drowning in context you don't need." | **Too much context.** |
| 0:04-0:10 | Cut to bold stat on dark screen, animated in | "Anthropic tested this. They cut tool context by eighty-five percent. Accuracy jumped from forty-nine to seventy-four percent." | **-85% context = +25 pts accuracy** |
| 0:10-0:17 | Cut to `context-noise-breakdown.png` visual, zoom into the stacked bar showing 65% noise | "Thirty to seventy percent of the context your AI sees is noise. Stale files. Old chat history. Tool definitions it will never use." | **30-70% is noise** |
| 0:17-0:25 | Screen recording: opening fresh Copilot Chat thread, typing a targeted prompt with #file reference | "The fix is context engineering. Close irrelevant files. Start fresh threads. Use file references for targeted context." | **Context engineering** |
| 0:25-0:35 | Screen recording: same prompt, now with 3 files open. Copilot producing clean, correct output | "Same prompt. Same model. Better context. Better output." | **Same model. Better results.** |
| 0:35-0:43 | Cut to `before-after-context.png` visual, zoom into the three scenarios | "SWEzze found the same thing. Six x compression gave five to nine percent better results with half the tokens." | **Less input = better output** |
| 0:43-0:50 | Screen recording: creating a copilot-instructions.md file in VS Code | "Start here. Close files you don't need. One thread per task. Add a copilot instructions file." | **5 min setup** |
| 0:50-0:60 | End card: series title + "Part 1 of 3" + follow prompt | "That's Part 1. Part 2 covers caching — ninety percent savings with zero quality trade-off. Follow for that." | **Part 1 of 3 | Follow** |

---

## Screen Recording Notes

- **App**: VS Code with GitHub Copilot extension active
- **Theme**: Dark theme (better contrast for vertical video)
- **Setup for "before" shot (0:00-0:04)**:
  - Open 15+ random files from a project (mix of config, tests, unrelated modules)
  - Open Copilot Chat, ask: "fix the null check in the auth middleware"
  - Show the model producing a confused or irrelevant response
- **Setup for "after" shot (0:25-0:35)**:
  - Close all files except auth/middleware.ts, auth/types.ts, auth/middleware.test.ts
  - Start a NEW Copilot Chat thread
  - Type: `#file:src/auth/middleware.ts Fix the null check on the session object at line 47`
  - Show the model producing a clean, correct fix
- **copilot-instructions.md shot (0:43-0:50)**:
  - Create new file `.github/copilot-instructions.md`
  - Type a few lines: tech stack, conventions, key constraints
  - Show the file being saved
- **Zoom**: 150-200% on the relevant UI area. Avoid showing full IDE chrome.

---

## Voiceover Script (Full)

> Your AI code assistant is drowning in context you don't need.
>
> Anthropic tested this. They cut tool context by eighty-five percent. Accuracy jumped from forty-nine to seventy-four percent.
>
> Thirty to seventy percent of the context your AI sees is noise. Stale files. Old chat history. Tool definitions it will never use.
>
> The fix is context engineering. Close irrelevant files. Start fresh threads. Use file references for targeted context.
>
> Same prompt. Same model. Better context. Better output.
>
> SWEzze found the same thing. Six x compression gave five to nine percent better results with half the tokens.
>
> Start here. Close files you don't need. One thread per task. Add a copilot instructions file.
>
> That's Part 1. Part 2 covers caching — ninety percent savings with zero quality trade-off. Follow for that.

**Word count**: ~120 words (~50-55 seconds at conversational pace)

---

## Captions & Hashtags

### Instagram Reels / YouTube Shorts

Anthropic cut AI context by 85%.
Accuracy IMPROVED from 49% to 74%.

Less noise = better output. Every time.

Five context engineering practices in 60 seconds.

Full breakdown with research data (link in bio).

#ContextEngineering #GitHubCopilot #AIEngineering #CodingTips #DeveloperTools #PromptEngineering #SoftwareEngineering

### LinkedIn Video

Anthropic reduced tool context by 85%. Accuracy improved from 49% to 74%.

SWEzze compressed context 6x. Issue resolution improved 5-9.2%.

The pattern: less noise = better AI output. Not a trade-off — a free lunch.

Five context engineering practices that improve your AI code assistant:
1. Close irrelevant files
2. One thread per task
3. Targeted #file references
4. Front-load intent
5. Stable copilot-instructions.md

Part 1 of 3 on engineering better AI interactions. Full blog in comments.

#ContextEngineering #GitHubCopilot #AIEngineering #DeveloperProductivity

---

## Thumbnail / Cover Frame

**Visual**: Dark background with a split composition.
- Left side: Cluttered VS Code with many tabs, red-tinted, with "49%" in large text
- Right side: Clean VS Code with 3 tabs, green-tinted, with "74%" in large text
- Center arrow pointing left to right
- Bottom: "Context Engineering" in white text
- Top corner: "Part 1/3" badge

---

## Music / Pacing Notes

- **Vibe**: Clean, minimal electronic. Think "calm tech explainer" — not hype, not corporate.
- **Beat drop**: Subtle at 0:04 when the stat appears (49% -> 74%)
- **Pace shift**: Slightly faster at 0:17 during the "fix" section (action-oriented)
- **Pause**: Brief 0.5s silence at 0:25 before "Same prompt. Same model." — let the before/after land
- **End**: Clean fade starting at 0:50
