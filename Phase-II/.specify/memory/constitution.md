<!--
SYNC IMPACT REPORT
Version: 1.0.0 -> 2.0.0 (Major Architecture Shift)
- Principles:
  - I. Spec-Driven Agentic Workflow (Retained)
  - II. AI-Native Full-Stack Architecture (Updated for ChatKit/Agents SDK)
  - III. Stateless Agentic Architecture (New - replaces generic stateless auth)
  - IV. Model Context Protocol (MCP) Standard (New)
  - V. Secure Data Isolation (Updated for SQLModel/Neon)
  - VI. Testable Deliverables (Retained)
- Templates Status:
  - .specify/templates/plan-template.md: ✅ Compatible
  - .specify/templates/spec-template.md: ✅ Compatible
  - .specify/templates/tasks-template.md: ✅ Compatible
-->
# Taskoo AI: Spec-Driven Fullstack Assistant Constitution

## Core Principles

### I. Spec-Driven Agentic Workflow
**No manual coding allowed without explicit exception.** We strictly follow the `Spec -> Plan -> Tasks -> Implement` cycle using AI agents. Every feature starts with a written specification, followed by a detailed plan and task breakdown before any code is generated. This ensures clarity, verifiability, and reduces regression risks.

### II. AI-Native Full-Stack Architecture
**Built for Agents, not just Users.** The application is built as an intelligent distributed system:
- **Frontend**: OpenAI ChatKit (Next.js) for a natural language user interface.
- **Backend**: Python FastAPI hosting the OpenAI Agents SDK and Official MCP SDK.
- **Infrastructure**: Neon Serverless PostgreSQL for all persistence.
- **AI Logic**: Logic flows through the OpenAI Agents SDK, utilizing MCP tools for all side effects.

### III. Stateless Agentic Architecture
**Memory is in the Database, not the Server.** The backend MUST remain stateless to ensure scalability and resilience.
- **Cycle**: Receive Message -> Fetch History (DB) -> Run Agent -> Store Result (DB) -> Return.
- The server must handle restarts without losing conversation context.
- All conversation history and task data must be persisted in Neon PostgreSQL via SQLModel.

### IV. Model Context Protocol (MCP) Standard
**Standardized Tooling Interface.** The AI agent must interact with the application domain strictly through the Model Context Protocol (MCP).
- **Tools**: `add_task`, `list_tasks`, `complete_task`, `delete_task`, `update_task`.
- **Contract**: All tools must use strict Pydantic models for input/output validation.
- **Routing**: The AI Agent routes natural language intent to these specific MCP tools; the backend does not parse intent manually.

### V. Secure Data Isolation
**Trust but Verify.**
- **Authentication**: Managed by **Better Auth**.
- **Isolation**: Every database query and MCP tool invocation must be scoped to the `user_id`.
- **Security**: The ChatKit frontend must be on the OpenAI Domain Allowlist. Secrets (Keys, DB URLs) are strictly managed via `.env`.

### VI. Testable Deliverables
**If it isn't tested, it doesn't exist.** Every feature must include acceptance criteria.
- **MCP Tests**: Each MCP tool must have unit tests verifying it correctly modifies the database.
- **Agent Tests**: Integration tests should verify the Agent selects the correct tool for a given prompt.

## Governance

**Amendments**:
- Principles may be amended only through the `sp.constitution` command or explicit consensus documented in the project history.

**Versioning**:
- **MAJOR (2.x)**: Fundamental architecture changes (e.g., this shift to Agents/MCP).
- **MINOR (x.1)**: Adding new tools or significant module changes.
- **PATCH (x.x.1)**: Clarifications or non-semantic text updates.

**Version**: 2.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
