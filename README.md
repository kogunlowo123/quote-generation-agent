# Quote Generation Agent

[![CI](https://github.com/kogunlowo123/quote-generation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/quote-generation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Sales | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Quote generation agent that configures product bundles, calculates pricing with discounts and approvals, generates professional quote documents, manages quote expiration, and tracks quote-to-close conversion.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `configure_quote` | Configure a quote with products, quantities, and pricing |
| `apply_discount` | Apply discount rules and check approval requirements |
| `generate_document` | Generate a professional quote document |
| `manage_expiration` | Set and manage quote expiration dates and reminders |
| `track_conversion` | Track quote-to-close conversion and cycle time |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/quote-generation/execute` | Execute primary action |
| `POST` | `/api/v1/quote-generation/analyze` | Run analysis |
| `GET` | `/api/v1/quote-generation/metrics` | Get metrics |
| `PUT` | `/api/v1/quote-generation/configure` | Configure settings |
| `POST` | `/api/v1/quote-generation/report` | Generate report |

## Features

- Quote
- Generation
- Analytics
- Automation

## Integrations

- Salesforce
- Hubspot
- Outreach
- Apollo
- Linkedin Sales Navigator

## Architecture

```
quote-generation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── quote_generation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CRM + Sales Engagement + LLM**

---

Built as part of the Enterprise AI Agent Platform.
