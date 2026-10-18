# MCP Security Registry Dashboard

## 📊 Overview

**Servers Scanned:** 17  
**Vulnerabilities Found:** 2  
**Security Score:** 94% (16/17 clean)

## Findings

- **1 Critical** - Citedy MCP (unauthenticated infrastructure endpoints)
- **0 High** - Other servers clean
- **16 Verified Secure**

## Citedy MCP Vulnerability

**Issue:** Unauthenticated endpoints expose infrastructure metadata

**Affected Endpoints:**
- GET /sse
- GET /tools/list

**Status:** Disclosed with remediation guidance (2026-10-18)

**Remediation:** Require authentication; implement access controls; remove/obfuscate sensitive metadata from responses

## Clean Servers

Tavily, Daloopa, BetterBugs, Lusha, AntiMetal, FlowStudio, Hunter.io, PointFive, Context7, DYPAI, ByteRover, ItJuzi, BurnBar, Exa, IcePanel, CircleCI

---

**Last Updated:** 2026-10-18 | **Next Scan:** 2026-11-18
