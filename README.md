# MCP Security Registry

**17 servers scanned | 2 vulnerabilities found | 94% secure**

## Critical Finding: Citedy MCP

**Zero-Auth Endpoints Exposed**

Endpoint: `GET https://mcp.citedy.com/mcp/sse`

Returns server metadata without authentication:
```json
{
  "serverInfo": {"name": "citedy-mcp", "version": "3.0.0"},
  "protocolVersion": "2025-03-26"
}
```

Also vulnerable: `GET /tools/list`

**Fix:** Require authentication on both endpoints.

---

## Clean Servers (16/17)

Tavily, Daloopa, BetterBugs, Lusha, AntiMetal, FlowStudio, Hunter.io, PointFive, Context7, DYPAI, ByteRover, ItJuzi, BurnBar, Exa, IcePanel, CircleCI

---

## Detection Rules

- **D1** - Zero-auth endpoints
- **D3** - Token validation bypass
- **E1** - Session isolation
- **E2** - Secrets in logs
- **E3** - Injection vectors

---

**Researcher:** Leroy (VATA)  
**Updated:** 2026-10-12  
**Status:** Active scanning

[See Full Findings](docs/FINDINGS.md)
