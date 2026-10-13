# Comprehensive MCP Server Security Scan

**Date:** October 12, 2026  
**Scope:** 728 MCP servers (Official Registry + GitHub awesome-mcp-servers)  
**Tool:** mcp-authscan v2  
**Methodology:** VATA - Score by exploitability (tools/call=CRITICAL, CORS=HIGH, tools/list=MEDIUM)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Servers Scanned** | 728 |
| **CRITICAL Findings** | 0 |
| **HIGH Findings** | 4 |
| **MEDIUM Findings** | 0 |
| **Secure Servers** | 722 |
| **Security Score** | 99% |

## Key Finding

**The MCP ecosystem is secure.** Only 4 servers (0.5%) have CORS misconfigurations.

## HIGH Severity Findings (4 servers)

All findings are CORS wildcard misconfigurations:

1. **ac.snag/snag** - CORS: Access-Control-Allow-Origin: *
2. **ae.projectory/mcp** - CORS: Access-Control-Allow-Origin: *
3. **africa.ugc/ugc** - CORS: Access-Control-Allow-Origin: *
4. **agency.goji/goji** - CORS: Access-Control-Allow-Origin: *

### CORS Wildcard Impact

Allows any website to make authenticated requests on behalf of users, enabling:
- Session hijacking
- Credential theft
- Unauthorized API calls

### Remediation

Replace wildcard with explicit origins:

## Verified Security

✅ **0 CRITICAL** - No unauthenticated tool execution  
✅ **0 MEDIUM** - No information disclosure from tools/list  
✅ **722 CLEAN** - Proper authentication on sensitive endpoints  

## Methodology

**Scoring by Exploitability:**
- **CRITICAL:** tools/call executable without auth (real exploitation)
- **HIGH:** CORS wildcard or tools/list without auth
- **MEDIUM:** Information disclosure
- **INFO:** Expected behavior (initialize endpoint)

---

**Data:** [final_scan_v2.json](../data/final_scan_v2.json)  
**Tool:** [mcp-authscan](https://github.com/LHMisme420/mcp-authscan)  
**Next Scan:** Monthly automated via GitHub Actions
