# MCP Security Registry Dashboard

## 📊 Overview

**Servers Scanned:** 17  
**Vulnerabilities Found:** 2  
**Security Score:** 94% (16/17 clean)

## Findings

- **1 Critical** - Citedy MCP (zero-auth endpoints)
- **0 High** - Other servers clean
- **16 Verified Secure**

## Citedy MCP Vulnerability

**Endpoints exposed without authentication:**
- GET /sse → Returns server metadata
- GET /tools/list → Returns tool enumeration

**Status:** UNPATCHED (as of 2026-10-12)

## Clean Servers

Tavily, Daloopa, BetterBugs, Lusha, AntiMetal, FlowStudio, Hunter.io, PointFive, Context7, DYPAI, ByteRover, ItJuzi, BurnBar, Exa, IcePanel, CircleCI

---

**Last Updated:** 2026-10-12 | **Next Scan:** 2026-11-12
