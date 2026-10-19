# MCP Security Registry

**Comprehensive security audit of 2,028 MCP servers.**

## Audit Results

## Data Files

- `data/final_scan_v2.json` - Phase 1: 728 servers
- `data/phase2_deepdive_audit.json` - Phase 2: 1,300 servers
- `data/phase2_vata_scores.json` - VATA scores, all 2,028
- `data/phase2_exploitation_pocs.json` - 308 vulnerability candidates flagged for review (149 command injection patterns, 80 credential disclosure patterns, 79 missing authentication checks)

## Key Finding

**Rate limiting missing across 98.6% of ecosystem** (2,000/2,028)
→ Infrastructure vulnerability: Agent DoS at scale

**Authentication and authorization gaps identified** across Phase 2 batch
→ Pattern analysis flagged 308 vulnerability candidates across three categories. All candidates require manual verification to confirm actual exploitability.

## Methodology

VATA 7-category framework:
- TLS/HTTPS
- Input Validation
- Information Disclosure
- Rate Limiting
- Tool Output Safety
- Resource Isolation
- Known Vulnerabilities

## Registry

- Scanner: [mcp-authscan](https://github.com/LHMisme420/mcp-authscan)
- Methodology: Transparent, reproducible
- Data: Public, machine-readable

---

**Audit Date:** October 13, 2026
**Researcher:** Leroy (VATA)
**Motto:** Receipts Over Promises

---

## OWASP MCP Top 10 Compliance Mapping

**mcp-authscan** audits your infrastructure against the OWASP MCP Top 10 security standard.

### Coverage Matrix

| OWASP MCP | Vulnerability | Coverage | Finding |
|-----------|---------------|----------|---------|
| MCP05 | Insufficient Rate Limiting | ✅ DETECTED | 98.6% of ecosystem missing |
| MCP07 | Insufficient Authentication | ✅ DETECTED | 149 command injection patterns, 80 credential patterns, 79 auth-check patterns flagged |
| MCP03 | Excessive Tool Functionality | ✅ DETECTED | Pattern analysis across all 1,300 Phase 2 servers |
| MCP09 | Shadow MCP Servers | ✅ DETECTED | 1,300 additional servers identified |
| MCP01 | Insufficient Input Validation | ⚠️ PARTIAL | SQL/command injection vectors identified |
| MCP02 | Insecure Output Handling | ⚠️ PARTIAL | Info disclosure in error messages |
| MCP06 | Insecure Defaults | ✅ DETECTED | No auth required by default |
| MCP04 | Poor Tool Validation | ✅ DETECTED | Tools accept arbitrary parameters |
| MCP08 | Insecure Deserialization | 🔍 PENDING | Covered in Phase 3 audit |
| MCP10 | Inadequate Monitoring | 🔍 PENDING | Covered in Phase 3 audit |

### Enterprise Compliance

Use `mcp-authscan` to audit your MCP infrastructure against OWASP MCP Top 10:

```bash
mcp-authscan --target https://your-mcp-gateway.com
```

Generates compliance report for security reviews and audits.

---
