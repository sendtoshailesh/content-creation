## Tier 0 Preflight

Checked 3 artifact(s) - Error: 0  Warning: 3  Info: 0

| Severity | Category | Asset / location | Finding | Required fix |
|----------|----------|------------------|---------|--------------|
| Warning | design-token | content/topics/mcp-servers-2026/visuals/render_mcp_servers_2026.py | savefig() present without dpi=320 | Pass dpi=320 to every savefig call |
| Warning | design-token | content/topics/mcp-servers-2026/visuals/render_mcp_servers_2026.py:1111 | Non-token color #fff8f0 | Use a design-token hex from visual-standards, or justify |
| Warning | design-token | content/topics/mcp-servers-2026/visuals/render_mcp_servers_2026.py:41 | Non-token color #d97706 | Use a design-token hex from visual-standards, or justify |

GATE: PASS
