# Scanning Methodology

## Detection Rules

### D1 - Zero-Auth Endpoints
Endpoints returning data without Authorization header.

**Test:**
```bash
curl https://mcp.server.com/mcp/sse
# Should require auth but doesn't
```

### D3 - Token Validation Bypass
Invalid tokens accepted as valid.

### E1 - Session Isolation
Cross-session context exposure.

### E2 - Secrets in Logs
Credentials in error messages or output.

### E3 - Injection Vectors
Parameter injection in tool calls.

## Scanning Process

1. **Enumerate** - Find live MCP servers from public repos
2. **Probe** - Test standard endpoints (/sse, /tools/list, /message)
3. **Auth Test** - Attempt access without/with invalid credentials
4. **Verify** - Confirm findings are reproducible
5. **Analyze** - Assess impact and provide remediation

## Tool: mcp-authscan

Automated OAuth vulnerability scanner for MCP servers.

```bash
python3 ~/vata/mcp-authscan/mcp_authscan.py https://server.com/mcp
```

---

All findings verified and reproducible.
