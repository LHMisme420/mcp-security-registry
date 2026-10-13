# MCP Security Registry

**Comprehensive security audit of 2,028 MCP servers.**

## Audit Results

## Data Files

- `data/final_scan_v2.json` - Phase 1: 728 servers
- `data/phase2_deepdive_audit.json` - Phase 2: 1,300 servers
- `data/phase2_vata_scores.json` - VATA scores, all 2,028
- `data/phase2_exploitation_pocs.json` - 308 POC tests

## Key Finding

**Rate limiting missing across 98.6% of ecosystem** (2,000/2,028)
→ Infrastructure vulnerability: Agent DoS at scale

**Command execution available on 100% of Phase 2 batch** (1,300/1,300)
→ RCE vectors confirmed via 149 exploitation POCs

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
