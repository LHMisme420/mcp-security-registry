# VATA MCP Security Platform - REST API

## Authentication

### Register Organization
```bash
POST /auth/register
Content-Type: application/json

{
  "org_name": "Your Company"
}

Response:
{
  "org_id": 1,
  "api_key": "uuid-here",
  "message": "Organization created"
}
```

### Get JWT Token
```bash
POST /auth/login
Content-Type: application/json

{
  "api_key": "your-api-key"
}

Response:
{
  "access_token": "jwt-token-here"
}
```

## Scanning

### Create Scan
```bash
POST /api/scans
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "server_url": "https://example-mcp.com",
  "scan_type": "comprehensive"
}

Response:
{
  "scan_id": 1,
  "status": "pending",
  "message": "Scan queued"
}
```

### Get Scan Results
```bash
GET /api/scans/{scan_id}
Authorization: Bearer {access_token}

Response:
{
  "id": 1,
  "org_id": 1,
  "server_url": "https://example-mcp.com",
  "status": "completed",
  "result": {...},
  "severity": "HIGH",
  "created_at": "2026-10-14T06:00:00"
}
```

### List Findings
```bash
GET /api/findings
Authorization: Bearer {access_token}

Response:
{
  "findings": [
    {
      "id": 1,
      "server_url": "https://example-mcp.com",
      "vector_type": "rate_limiting_missing",
      "severity": "MEDIUM",
      "cvss_score": 5.3,
      "remediation": "Implement rate limiting at 5 req/sec"
    }
  ]
}
```

## Reporting

### Generate Compliance Report
```bash
POST /api/reports/compliance
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "framework": "SOC2"
}

Response:
{
  "report_id": 1,
  "compliance_score": 78.5,
  "framework": "SOC2",
  "severity_breakdown": {
    "CRITICAL": 0,
    "HIGH": 2,
    "MEDIUM": 5,
    "LOW": 3
  }
}
```

## Health Check
```bash
GET /health

Response:
{
  "status": "healthy"
}
```
