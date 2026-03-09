---
description: "Archive current content and prepare workspace for a new content pipeline run"
---

## Archive Content

Before archiving, show the user what will be archived:

1. List all files in `content/` (excluding `pipeline-config.md`) 
2. Show the current archive count in `archive/`
3. **Ask the user to confirm** before proceeding

If confirmed, run:
```bash
./scripts/archive-content.sh --yes
```

After archiving, confirm:
- What was archived and the archive folder name
- How many archives remain (max 3; oldest are auto-pruned)
- That `content/` is clean and ready for a new pipeline run
