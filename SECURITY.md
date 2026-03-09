# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| main branch | :white_check_mark: |
| Older commits | :x: |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead:

1. **Email**: Send details to the repository owner via GitHub's private vulnerability reporting feature
2. **GitHub Security Advisories**: Use [Report a vulnerability](../../security/advisories/new) to submit privately

### What to Include

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response Timeline

- **Acknowledgment**: Within 48 hours
- **Assessment**: Within 7 days
- **Fix/Resolution**: Depends on severity, typically within 30 days

## Security Considerations

This project contains:
- **Shell scripts** (`scripts/archive-content.sh`) — review for command injection if modifying
- **Python renderers** (`content/visuals/*.py`) — execute locally only, not in production
- **Copilot agent definitions** — no credentials or secrets should be stored in agent files

### Best Practices for Contributors

- Never commit API keys, tokens, or credentials
- Never commit `.env` files
- Review shell scripts for injection vulnerabilities before submitting
- Python scripts should not make network requests unless explicitly documented
