# Official MCP Registry Security Scan Results

**Date:** October 12, 2026  
**Scope:** Official MCP Registry (registry.modelcontextprotocol.io)  
**Endpoints Scanned:** 33  

## Summary

| Metric | Count |
|--------|-------|
| Total Endpoints | 33 |
| CRITICAL Findings | 0 |
| HIGH Findings | 5 |
| Clean Servers | 28 |
| Security Score | 85% |

## HIGH Findings: CORS Wildcard

| Server | Issue |
|--------|-------|
| ac.snag/snag | CORS wildcard allowed |
| ae.projectory/mcp | CORS wildcard allowed |
| africa.ugc/ugc | CORS wildcard allowed |
| agency.goji/goji | CORS wildcard allowed |

All servers should restrict CORS to trusted domains only.

---

**Scan Tool:** [mcp-authscan](https://github.com/LHMisme420/mcp-authscan)  
**Methodology:** [REGISTRY_SCAN_RESULTS.md](../docs/REGISTRY_SCAN_RESULTS.md)
