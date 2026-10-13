# MCP Security Registry - 728 Servers Audited

**728 Servers Scanned | 99% Secure | 0 Critical Vulnerabilities**

First comprehensive security audit of the MCP ecosystem.

## Results

- Servers: 728
- CRITICAL: 0
- HIGH: 4 (CORS)
- Secure: 722
- Score: 99%

## Methodology

We score by EXPLOITABILITY, not just endpoint access.
- CRITICAL = tools/call works without auth (real exploitation)
- HIGH = CORS wildcard or tools/list without auth
- MEDIUM = Information disclosure

Result: 0 CRITICAL because no servers allow unauthenticated tool execution.

[Full Reports](docs/COMPREHENSIVE_SCAN_RESULTS.md) | [Tool](https://github.com/LHMisme420/mcp-authscan)
