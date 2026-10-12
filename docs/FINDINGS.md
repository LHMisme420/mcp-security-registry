# MCP Security Registry - Findings Report

**Date:** October 12, 2026
**Researcher:** Leroy (VATA)
**Servers Scanned:** 17
**Vulnerabilities Found:** 2

## Critical Finding: Citedy MCP

**Server:** https://mcp.citedy.com/mcp
**Issue:** Zero-auth endpoints expose server metadata
**Severity:** HIGH

### Details

GET /sse returns:

GET /tools/list also requires no auth.

### Impact
- Server version disclosure
- Technology stack enumeration
- Low impact (no sensitive data exposed in this case)

### Fix
Require authentication on /sse and /tools/list endpoints.

---

## Clean Servers (16)

Tavily, Daloopa, BetterBugs, Lusha, AntiMetal, FlowStudio, Hunter.io, PointFive, Context7, DYPAI, ByteRover, ItJuzi, BurnBar, Exa, IcePanel, CircleCI

All properly require authentication.
