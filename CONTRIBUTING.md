# Contributing to Content Creation Pipeline

Thank you for considering contributing! This project automates an 8-step content strategy pipeline using GitHub Copilot custom agents, and we welcome contributions that improve the agents, skills, visual system, or documentation.

## How to Contribute

### Reporting Issues

- Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template for bugs
- Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template for ideas
- Check existing issues before opening a new one

### Pull Requests

1. **Fork** the repository
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** — keep PRs focused on a single concern
4. **Test your changes**:
   - If modifying an agent: test it in VS Code Copilot Chat
   - If modifying visuals: run the Python renderer and verify output at 320 DPI
   - If modifying scripts: run them locally
5. **Commit** with clear messages:
   ```
   feat: add new agent for podcast script generation
   fix: correct design token hex value for ACCENT_2
   docs: update README with new prompt shortcut
   ```
6. **Push** and open a Pull Request against `main`

### Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Use For |
|--------|---------|
| `feat:` | New features (agents, skills, prompts) |
| `fix:` | Bug fixes |
| `docs:` | Documentation changes |
| `style:` | Formatting, no code change |
| `refactor:` | Code restructuring |
| `chore:` | Maintenance (deps, scripts, CI) |

### What to Contribute

**Great first contributions:**
- Improve agent instructions for better output quality
- Add new design tokens or visual templates
- Fix typos or improve documentation
- Add new social platform adapters

**Larger contributions (open an issue first):**
- New pipeline agents
- Changes to the archive mechanism
- Modifications to the design token system
- New skills

## Code Standards

### Agent Files (`.agent.md`)
- Keep frontmatter minimal — don't hardcode `model`
- Restrict tools to the minimum needed
- Include clear constraints section

### Visual Assets
- Use the shared design token system (see `.github/skills/visual-rendering/references/design-tokens.md`)
- 320 DPI for all PNG output
- Helvetica Neue font family
- No Unicode glyphs in matplotlib — use ASCII equivalents

### Content Quality
- Every claim needs concrete data
- No vague generalities
- First-person practitioner tone

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## Questions?

Open a [Discussion](../../discussions) or an issue — we're happy to help.
