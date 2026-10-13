# MCP Security Registry

**First comprehensive public security audit of 2,028 MCP servers.**

## V2 Comprehensive Scan Results

```
CRITICAL:   2 servers (Input validation: SQL injection, code injection)
HIGH:       6 servers (CORS wildcards, path traversal, XSS)
MEDIUM:   2,000 servers (Rate limiting gaps)
SECURE:       2 servers (0 findings)
Score: 0.1% | Scan: 2026-10-13
```

## Critical Vulnerabilities (2 servers)

**ae.genosys/genosys** - SQL Injection + Code Injection
**ae.propick/propick** - SQL Injection + Code Injection

## High Severity (6 servers)

CORS Wildcards: ac.snag, ae.projectory, africa.ugc, agency.goji
Path Traversal & XSS: ae.genosys, ae.propick

## Methodology

7 security test categories: TLS/HTTPS, Input validation, Information disclosure, Rate limiting, Tool output safety, Resource isolation, Known vulnerabilities

## Scan Overview

Servers: 2,028 | CRITICAL: 2 | HIGH: 6 | MEDIUM: 700 | SECURE: 20 | Score: 0.1%

[Scanner](https://github.com/LHMisme420/mcp-authscan) | [Raw Data](data/comprehensive_scan_v2.json)

Built with VATA: Receipts Over Promises
lhmisme2011@gmail.com | GitHub: LHMisme420
