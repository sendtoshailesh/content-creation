---
title: PowerShell README Validator Research Subagent
description: Repository-local research on how to add a PowerShell validator that ensures docs subfolders contain README.md
author: GitHub Copilot
ms.date: 2026-03-16
ms.topic: reference
keywords:
  - powershell
  - validation
  - docs
  - readme
  - repository research
estimated_reading_time: 5
---

## Research Scope

* Topic: What is needed to create a PowerShell script for this repository that validates every subfolder under docs/ contains a README.md file.
* Goals covered:
  * Inspect whether docs/ exists and what its structure looks like.
  * Inspect scripts/linting/ for existing PowerShell script patterns, coding style, parameter usage, output style, and exit code behavior.
  * Inspect the repository for PSScriptAnalyzer settings, suppressions, or PowerShell lint conventions.
  * Inspect package.json and any npm script structure if it exists.
  * Inspect contributor and README documentation for script conventions and validation behavior.
  * Recommend a repo-aligned location and behavior for a new PowerShell validator script.
  * Capture exact evidence using workspace-relative paths and line numbers where possible.
* Research-only constraints followed:
  * Repository-local evidence only.
  * No implementation changes outside this research artifact.

## Agent Instruction Check

* Searched for .github/agents/**/researcher-subagent.agent.md in the workspace.
* Result: no repo-local researcher-subagent agent file exists.
* Checked the HVE Core fallback location referenced by .github/instructions/shared/hve-core-location.instructions.md.
* Result: no fallback researcher-subagent agent file was found there either.

## Search Coverage

### File and folder checks

The following direct checks were used to determine whether the expected folders and files exist:

* docs/ directory listing failed with ENOENT, which means the directory does not currently exist.
* scripts/linting/ directory listing failed with ENOENT, which means the directory does not currently exist.
* File search for **/docs/** returned no results.
* File search for **/scripts/linting/** returned no results.
* File search for **/*.ps1 returned no repo-local results.
* File search for **/PSScriptAnalyzerSettings.psd1 returned no results.
* File search for **/package.json returned no results.

### Text and documentation checks

The following files were inspected because they define current repository behavior:

* README.md
* CONTRIBUTING.md
* .github/PULL_REQUEST_TEMPLATE.md
* scripts/archive-content.sh
* scripts/customize-hve-core.sh
* .gitignore

## Key Findings

### docs/ does not exist today

There is currently no docs/ tree in the repository.

Evidence:

* File search for **/docs/** returned no results.
* README.md documents the project structure starting at README.md:129 and lists content/ at README.md:145 plus scripts/ at README.md:156, but does not list a docs/ directory.

Implication:

* A validator that hard-fails when docs/ is missing would fail immediately in the current repository state.

### scripts/linting/ does not exist today

There is currently no scripts/linting/ folder to inherit patterns from.

Evidence:

* File search for **/scripts/linting/** returned no results.
* scripts/ currently contains only two top-level shell utilities: scripts/archive-content.sh and scripts/customize-hve-core.sh.
* README.md:156 shows the repository documents a flat scripts/ directory.
* README.md:157 documents scripts/archive-content.sh as the only script in the published project structure.

Implication:

* There is no existing linting-specific subfolder convention in this repository yet.

### The current script conventions come from shell scripts, not PowerShell

The closest local convention comes from the two bash scripts under scripts/.

Evidence from scripts/archive-content.sh:

* scripts/archive-content.sh:10 uses strict shell mode with set -euo pipefail.
* scripts/archive-content.sh:19 and scripts/archive-content.sh:20 print a plain message and exit 0 when the target directory is missing or empty.
* scripts/archive-content.sh:45 and scripts/archive-content.sh:46 print Aborted. and exit 0 for a user-cancelled no-op.
* scripts/archive-content.sh:56, scripts/archive-content.sh:65, and scripts/archive-content.sh:79 show simple plain-text progress output.

Evidence from scripts/customize-hve-core.sh:

* scripts/customize-hve-core.sh:11 introduces a Usage block.
* scripts/customize-hve-core.sh:31 and scripts/customize-hve-core.sh:32 print an Error: message to stderr and exit 1 when a required dependency is missing.
* scripts/customize-hve-core.sh:56 and scripts/customize-hve-core.sh:58 exit 1 for invalid arguments.
* scripts/customize-hve-core.sh:93 through scripts/customize-hve-core.sh:95 show plain error text plus corrective guidance.
* scripts/customize-hve-core.sh:99 and scripts/customize-hve-core.sh:100 show concise success output.

Implication:

* Repo-aligned script behavior is plain-text, non-fancy console output.
* No-op states are allowed to exit 0.
* Real errors and invalid usage exit 1.
* Help and parameters are documented explicitly.

### There are no repo-owned PowerShell conventions yet

The repository does not currently contain tracked PowerShell automation or PowerShell lint configuration.

Evidence:

* File search for **/*.ps1 returned no repo-local results.
* File search for **/PSScriptAnalyzerSettings.psd1 returned no results.
* Repository searches for PSScriptAnalyzer, SuppressMessage, pwsh, and powershell found no repo-owned conventions in README.md, CONTRIBUTING.md, .github/PULL_REQUEST_TEMPLATE.md, or scripts/.
* The only PowerShell file found during broader search was .venv/bin/activate.ps1, but .gitignore:11 ignores .venv/ and .venv/bin/activate.ps1:3 shows it is a generated virtual environment activation script rather than repository automation.

Implication:

* A new PowerShell validator would establish the first repo-owned PowerShell pattern.
* There is no existing PSScriptAnalyzer baseline, suppression model, or parameter naming pattern to mirror.

### npm integration is not available today

The repository has no Node manifest or npm script runner.

Evidence:

* File search for **/package.json returned no results.
* CONTRIBUTING.md:24 tells contributors to run scripts locally.
* README.md:197 documents direct shell execution with ./scripts/archive-content.sh rather than an npm wrapper.

Implication:

* npm integration is not possible without first introducing package.json and a Node-based task wrapper.
* That would be a larger tooling decision, not a natural extension of the current repo state.

### Validation and script changes are verified manually

The contributor flow expects local execution and manual verification rather than a formal lint runner.

Evidence:

* CONTRIBUTING.md:21 starts the testing guidance with Test your changes.
* CONTRIBUTING.md:24 says script changes should be run locally.
* .github/PULL_REQUEST_TEMPLATE.md:11 has a Script/tooling change checkbox.
* .github/PULL_REQUEST_TEMPLATE.md:27 asks how the change was verified.
* .github/PULL_REQUEST_TEMPLATE.md:31 specifically expects contributors to run the archive script locally.

Implication:

* A new validator script should be runnable directly with pwsh and easy to verify manually.

## Repo-Aligned Recommendation

### Recommended location

The most repo-aligned location for a new validator today is:

* scripts/Validate-DocsReadme.ps1

Why this is the better fit right now:

* The repository already uses a flat scripts/ directory rather than a nested linting tool tree.
* scripts/linting/ does not exist, so adding that folder would introduce a new structure with no current local precedent.
* README.md already documents scripts/ as a first-class top-level area at README.md:156.

When scripts/linting/ would make sense instead:

* If the team plans to add multiple validation utilities soon, then introducing scripts/linting/ could be justified as a broader tooling organization step.
* That is not required for the first validator.

### Recommended behavior

Recommended runtime behavior for the new PowerShell script:

* Run non-interactively.
* Default to the repository's docs/ path relative to the script location.
* Accept an optional path parameter, such as -DocsPath, for flexibility.
* If docs/ does not exist, print a clear no-op message and exit 0.
* If docs/ exists but one or more subfolders are missing README.md, print each failing folder and exit 1.
* If all subfolders contain README.md, print a short success summary and exit 0.

Why missing docs/ should exit 0 in this repository:

* scripts/archive-content.sh:19 and scripts/archive-content.sh:20 already treat a missing target directory as a successful no-op.
* The current repository has no docs/ directory, so a hard failure on missing docs/ would make the validator unusable until the repository structure changes.

### Recommended output style

Use the same output style the existing scripts already use:

* Plain text messages.
* Short success summaries.
* Error-prefixed failure lines for actionable problems.
* Exit 1 only for real validation failures or invalid parameters.

Examples of repo-aligned output shape:

```text
Nothing to validate - docs/ is missing.
```

```text
Error: Missing README.md in docs/guides
Error: Missing README.md in docs/reference/api
```

```text
Validated 12 docs subfolders.
```

### Recommended integration approach

Recommended initial integration:

* Run directly with pwsh ./scripts/Validate-DocsReadme.ps1.
* Document the command in README.md if the script is added.
* Verify it manually during PRs, consistent with CONTRIBUTING.md:24 and .github/PULL_REQUEST_TEMPLATE.md:27.

Not recommended right now:

* Adding package.json only to expose an npm script wrapper.
* Introducing PSScriptAnalyzer configuration before there is at least a small set of repo-owned PowerShell scripts.

## Important Gaps and Blockers

* There is no docs/ directory yet, so the team must decide whether the future validator should treat a missing docs root as skip or failure. The repo evidence supports skip with exit 0.
* There are no existing PowerShell scripts or PSScriptAnalyzer settings to inherit from, so the first PowerShell script will also define the style baseline.
* There is no package.json, so npm-based invocation is not available without adding new tooling.
* There is no scripts/linting/ directory, so placing the first validator there would be an organizational choice rather than a convention match.

## Recommended Next Research

* Confirm whether the intended rule applies to every nested directory under docs/ or only documentation leaf folders.
* Confirm whether docs/ missing should remain a no-op permanently or only until a docs tree is introduced.
* If the script will be implemented, inspect whether a future CI or VS Code task should invoke pwsh ./scripts/Validate-DocsReadme.ps1 directly.

## Research Status

* Status: Complete.
* Confidence: High for repository-state findings because they are based on direct directory checks, file searches, and line-level evidence from the current workspace.