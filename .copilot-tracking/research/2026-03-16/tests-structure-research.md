<!-- markdownlint-disable-file -->
# Task Research: Test Structure

Research the current test structure in this repository, including whether tests exist, where they live, how they are organized, and how they are expected to run.

## Task Implementation Requests

* Identify any existing automated test directories, files, scripts, or configs in the repo.
* Explain the current test structure in beginner-friendly terms for a Project manager learning HVE Core for the first time.

## Scope and Success Criteria

* Scope: Repository-local test structure only. Include source evidence from the codebase and docs. Exclude hypothetical future test design unless clearly marked as absent or a gap.
* Assumptions:
  * The user wants the current state of the repository, not generic testing advice.
  * If no tests exist, that absence is itself the main finding.
* Success Criteria:
  * Identify whether any test framework or test files exist.
  * Document how tests are structured and run, or state clearly that no test structure is present.

## Outline

1. Search repository for test-related files and folders.
2. Check documentation for any testing instructions.
3. Summarize findings with one selected conclusion about the repo's current test state.

## Potential Next Research

* Determine how a minimal test structure should be added if the user later asks for one.
  * Reasoning: Useful follow-up only if the repo currently lacks tests.
  * Reference: Repository findings pending.

## Research Executed

### File Analysis

* CONTRIBUTING.md
  * Lines 21-24 document manual verification steps by change type rather than an automated test command.
* .github/PULL_REQUEST_TEMPLATE.md
  * Lines 27-32 define a manual verification checklist for pull requests.
* README.md
  * Lines 157 and 197 reference operational script usage, not automated test execution.
* scripts/archive-content.sh
  * Lines 3, 7, and 8 describe archive workflow usage, not tests.
* scripts/customize-hve-core.sh
  * Documents HVE Core asset copy/list operations, not test commands.

### Code Search Results

* Search for test-related file paths found no real test directories or executable test assets.
* Search for spec-style file names found no results.
* Search for common test framework configuration files found no results.
* Search for .github/workflows found no results, indicating no CI workflow checked into this repo.

### External Research

* None. This question is repository-local.

### Project Conventions

* Standards referenced: Repository instructions from .github/copilot-instructions.md and HVE Core Task Researcher mode.
* Instructions followed: Research-only workflow, dated research artifact, repository-local evidence gathering.

## Key Discoveries

### Project Structure

The repository is structured as a content-generation and agent-customization workspace, not as a software package with a formal automated test suite.

### Implementation Patterns

Verification is currently handled manually:

* Agent changes are tested interactively in VS Code Copilot Chat.
* Visual changes are validated by running the Python renderer and reviewing output.
* Script changes are run locally.
* Generated Markdown is reviewed manually.

### Complete Examples

```text
Manual verification pattern:
- agent changes -> test in VS Code Copilot Chat
- visual changes -> run Python renderer, verify 320 DPI output
- script changes -> run locally
- content changes -> review generated Markdown manually
```

### API and Schema Documentation

No test API, schema, or runner configuration is present in the repository.

### Configuration Examples

```text
Missing from the repository:
- tests/ or test/ directories
- pytest.ini / tox.ini / noxfile.py / pyproject.toml
- package.json / jest / vitest / playwright / cypress configs
- .github/workflows/
```

## Technical Scenarios

### Current Repository Test Structure

The current test structure is manual and ad hoc rather than automated.

**Requirements:**

* Determine whether test assets exist.
* Identify any run commands or documented workflow.
* Present findings clearly for a non-developer stakeholder.

**Preferred Approach:**

* Inspect the repository for direct evidence and avoid guessing.
* Conclude based on file searches plus line-level documentation references.

```text
Current state:
- No automated test suite
- No CI workflow
- No single documented test command
- Manual validation documented in contributor guidance and PR checklist
```

**Implementation Details:**

Evidence-backed summary:

* CONTRIBUTING.md instructs contributors to manually validate changes.
* .github/PULL_REQUEST_TEMPLATE.md asks authors to mark manual verification steps.
* README.md and scripts/ only document operational workflows.
* Repository-wide searches found no test frameworks or test directories.

```text
Selected conclusion:
This repository currently has no automated tests. Its “test structure” is a manual verification workflow defined in docs and PR templates.
```

#### Considered Alternatives

* Generic assumptions about common test layouts were rejected because the user asked about this repository specifically.
* Inferring hidden CI or test automation was rejected because .github/workflows and common config files are absent.