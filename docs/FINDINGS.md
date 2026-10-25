# MCP Security Registry - Findings Report

**Date:** October 12, 2026
**Researcher:** Leroy (VATA)
**Servers Scanned:** 17
**Vulnerabilities Found:** 2


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
