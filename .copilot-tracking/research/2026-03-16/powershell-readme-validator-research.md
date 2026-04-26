<!-- markdownlint-disable-file -->
# Task Research: PowerShell README Validator Script

Research what is needed to create a PowerShell script for this repository that validates every subfolder under docs/ contains a README.md file.

## Task Implementation Requests

* Inspect existing PowerShell script patterns in scripts/linting/.
* Inspect PSScriptAnalyzer conventions and any repository settings.
* Inspect how npm scripts are structured in package.json.
* Determine the expected output format including exit codes and console messages.
* Identify any repository-specific gaps, such as a missing docs/ folder or missing package.json.

## Scope and Success Criteria

* Scope: Repository-local evidence only. Include script layout, conventions, and integration expectations for a future PowerShell validator script.
* Assumptions:
  * The user wants guidance for this repository's current structure, not generic PowerShell best practices alone.
  * If supporting files do not exist, that absence is an important finding.
* Success Criteria:
  * Identify whether scripts/linting/ exists and what patterns it uses.
  * Identify whether PSScriptAnalyzer settings or conventions exist.
  * Identify whether package.json exists and how scripts are organized.
  * Recommend the expected behavior of a new validator script based on evidence.

## Outline

1. Inspect repository for scripts/linting/, package.json, docs/, and PowerShell-related files.
2. Inspect documentation and existing scripts for style, output, and exit code patterns.
3. Evaluate viable implementation approaches and select the repo-aligned approach.

## Potential Next Research

* Determine the minimal implementation and npm wiring if the user asks to add the script.
  * Reasoning: Natural follow-up after the repository conventions are confirmed.
  * Reference: Findings pending.

## Research Executed

### File Analysis

* README.md
  * Lines 129-157 document the current project structure and show a flat scripts/ directory with no docs/ or scripts/linting/ tree.
  * Line 197 documents direct shell execution of a script rather than npm-based invocation.
* CONTRIBUTING.md
  * Lines 21-24 define manual verification expectations, including running scripts locally.
* .github/PULL_REQUEST_TEMPLATE.md
  * Lines 11 and 27-31 show the repo expects manual script verification during PRs.
* scripts/archive-content.sh
  * Lines 10, 19-20, 45-46, 56, 65, and 79 show current script behavior: strict mode, plain-text output, exit 0 for no-op states, and concise status messages.
* scripts/customize-hve-core.sh
  * Lines 11, 31-32, 56-58, 93-95, 99-100 show usage text, stderr error messages, and exit 1 for invalid usage.
* .gitignore
  * Line 11 shows .venv/ is ignored, confirming the only PowerShell file found during broader search is not repo-owned automation.

### Code Search Results

* No docs/ directory found.
* No scripts/linting/ directory found.
* No repo-local .ps1 files found.
* No PSScriptAnalyzerSettings.psd1 file found.
* No package.json found.
* No repository-owned references to PSScriptAnalyzer or PowerShell linting conventions found.

### External Research

* None. This question is repository-local.

### Project Conventions

* Standards referenced: Repository instructions from .github/copilot-instructions.md and HVE Core Task Researcher mode.
* Instructions followed: Research-only workflow, dated artifact, repository-local evidence gathering.

## Key Discoveries

### Project Structure

The repository currently has no docs/ tree, no scripts/linting/ subtree, and no Node package manifest. It uses a flat scripts/ directory for shell utilities.

### Implementation Patterns

The closest local script conventions come from bash scripts, not PowerShell:

* Use strict mode.
* Print plain-text status messages.
* Exit 0 for successful no-op states.
* Exit 1 for invalid usage or real failures.
* Keep usage/help concise and explicit.

### Complete Examples

```text
Repo-aligned validator behavior:
- pwsh ./scripts/Validate-DocsReadme.ps1
- if docs/ missing -> print no-op message, exit 0
- if a docs subfolder lacks README.md -> print one failure line per folder, exit 1
- if all pass -> print validated count summary, exit 0
```

### API and Schema Documentation

No PowerShell lint schema, no PSScriptAnalyzer baseline, and no npm script schema exists in the repository today.

### Configuration Examples

```text
Absent repository assets:
- docs/
- scripts/linting/
- *.ps1
- PSScriptAnalyzerSettings.psd1
- package.json
```

## Technical Scenarios

### Add a README Validator PowerShell Script

The repo-aligned first implementation should live in scripts/ and be runnable directly with pwsh rather than through npm.

**Requirements:**

* Validate that every immediate or nested subfolder under docs/ contains README.md.
* Match repository PowerShell conventions if they exist.
* Integrate with repository task runner if one exists.
* Emit useful console output and correct process exit codes.

**Preferred Approach:**

* Inspect the repository for direct evidence and avoid guessing.
* Choose a recommendation that matches the current flat scripts/ layout and manual verification workflow.

```text
Recommended location:
- scripts/Validate-DocsReadme.ps1

Recommended integration:
- direct pwsh execution
- document in README if added
- verify manually in PR workflow
```

**Implementation Details:**

Recommended runtime contract:

* Default to docs/ relative to repo root.
* Support an optional path override parameter.
* If docs/ is missing, print a clear skip message and exit 0.
* If one or more subfolders are missing README.md, print one error line per folder and exit 1.
* If validation succeeds, print a short summary with the validated folder count and exit 0.

Rationale:

* Missing-target no-op behavior matches scripts/archive-content.sh.
* There is no package.json, so npm integration would introduce new tooling with no current precedent.
* There is no existing PowerShell or PSScriptAnalyzer baseline, so the first script should stay simple.

```text
Selected conclusion:
Create the first validator as a standalone PowerShell script under scripts/, not scripts/linting/, and do not add npm wiring unless the repository later adopts package.json-based tooling.
```

#### Considered Alternatives

* Generic PowerShell recommendations without repository inspection were rejected because the user asked specifically about this repository.
* Putting the first validator under scripts/linting/ was rejected because that folder does not exist and the current repo documents a flat scripts/ layout.
* Adding npm script integration now was rejected because package.json does not exist and would add a new toolchain only to wrap one script.