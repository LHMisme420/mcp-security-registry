# MCP Security Registry - Findings Report

**Date:** October 12, 2026
**Researcher:** Leroy (VATA)
**Servers Scanned:** 17
**Vulnerabilities Found:** 2

## Critical Finding: Citedy MCP

**Server:** https://mcp.citedy.com/mcp
**Issue:** Unauthenticated endpoints expose infrastructure metadata
**Severity:** HIGH

### Details

GET /sse and GET /tools/list return server metadata without authentication.

### Impact
Unauthenticated access to infrastructure endpoints increases reconnaissance surface. Remediation required.

### Remediation
- Require authentication on /sse and /tools/list endpoints
- Implement role-based access control for metadata endpoints
- Obfuscate or remove version information from responses

**Disclosure Timeline:**
- 2026-10-12: Vulnerability identified and documented
- 2026-10-18: Published in VATA registry with remediation guidance
- Status: Awaiting vendor response

---

## Clean Servers (16)

Tavily, Daloopa, BetterBugs, Lusha, AntiMetal, FlowStudio, Hunter.io, PointFive, Context7, DYPAI, ByteRover, ItJuzi, BurnBar, Exa, IcePanel, CircleCI

All properly require authentication.
