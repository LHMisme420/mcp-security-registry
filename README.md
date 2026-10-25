# MCP Security Registry

**Automated security scanning of 2,028 MCP servers.** 
Analysis identifies patterns requiring manual verification before disclosure.

## Scan Results

## Data Files

- `data/final_scan_v2.json` - Phase 1: 728 servers scanned
- `data/phase2_deepdive_audit.json` - Phase 2: 1,300 servers scanned
- `data/phase2_vata_scores.json` - Aggregate scores across 2,028 servers
- `data/phase2_vulnerability_candidates.json` - 308 vulnerability candidates pending manual verification (149 command injection patterns, 80 credential disclosure patterns, 79 missing authentication checks)

## Key Findings (Automated Scanning)

**Rate limiting gaps flagged in 2,000/2,028 servers** (98.6%)
→ Pattern detected; pending manual verification for each affected server

**Authentication and authorization patterns identified** across Phase 2
→ 308 vulnerability candidates flagged. All require manual verification to confirm actual exploitability before any disclosure.

## Methodology

All findings are from automated pattern detection. No findings are filed or disclosed until reproduced on live targets.
