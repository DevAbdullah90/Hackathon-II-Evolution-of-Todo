<!--
SYNC IMPACT REPORT
Version: 2.0.0 -> 3.0.0 (Phase IV: Kubernetes & AIOps)
- Principles:
  - I. Spec-Driven Agentic Workflow (Retained & Reinforced)
  - II. AI-Assisted DevOps (AIOps) (New - Mandating Gordon, kubectl-ai, Kagent)
  - III. Cloud-Native Containerization (New - Docker & Gordon focus)
  - IV. Local Kubernetes Orchestration (New - Minikube & Helm focus)
  - V. Infrastructure as Code (New - Helm Charts required)
  - VI. Testable Deliverables (Retained)
- Templates Status:
  - .specify/templates/plan-template.md: ✅ Compatible
  - .specify/templates/spec-template.md: ✅ Compatible
  - .specify/templates/tasks-template.md: ✅ Compatible
-->
# Phase IV: Cloud Native Todo Chatbot Constitution

## Core Principles

### I. Spec-Driven Agentic Workflow
**No manual coding allowed without explicit exception.** We strictly follow the `Spec -> Plan -> Tasks -> Implement` cycle using AI agents.
- **Workflow**: Write Spec → Generate Plan → Break into Tasks → Implement via Agent.
- **Goal**: Zero manual coding. We rely on the Agentic Dev Stack to generate artifacts.
- **Review**: Every phase is reviewed to ensure the process, prompts, and iterations meet the standard.

### II. AI-Assisted DevOps (AIOps)
**Ops via AI Agents.** We leverage specialized AI tools for all infrastructure operations to maximize efficiency and learning.
- **Docker**: Use **Docker AI Agent (Gordon)** for container management and optimization.
- **Kubernetes**: Use **kubectl-ai** for declarative commands and **Kagent** for cluster analysis and optimization.
- **Mandate**: Prefer AI-generated commands and analysis over manual CLI crafting where possible.

### III. Cloud-Native Containerization
**Container First.** The application (Frontend & Backend) must be fully containerized.
- **Tooling**: Docker Desktop & Docker AI.
- **Standard**: Images must be optimized, secure, and ready for orchestration.
- **Agent Role**: Use Gordon to "generate docker run commands" or analyze container health if local Docker AI is available.

### IV. Local Kubernetes Orchestration
**Minikube is Production.** We deploy and validate strictly on a local Kubernetes cluster.
- **Platform**: **Minikube**.
- **Requirement**: The full stack (Frontend, Backend, DB) must run within the cluster.
- **Scalability**: Verify scaling capabilities (e.g., "scale backend to 2 replicas") using kubectl-ai.

### V. Infrastructure as Code (Helm)
**Declarative Deployment.** All Kubernetes resources must be managed via Helm Charts.
- **Generation**: Use AI tools (kubectl-ai/kagent) to generate and refine Helm charts.
- **Structure**: Maintain clean separation between values and templates.
- **Versioning**: Charts must be versioned and maintainable.

### VI. Testable Deliverables
**Verified Deployment.** A task is not done until it is running and verified in the cluster.
- **Verification**: Use `kubectl-ai` or `kagent` to check pod health ("check why pods are failing", "analyze cluster health").
- **Acceptance**: The Todo Chatbot must be accessible via localhost through the cluster ingress/port-forwarding and fully functional.

## Governance

**Amendments**:
- Principles may be amended only through the `sp.constitution` command or explicit consensus documented in the project history.

**Versioning**:
- **MAJOR (3.x)**: Phase IV - Shift to Kubernetes & AIOps.
- **MINOR (x.1)**: Adding new infrastructure components or AI tools.
- **PATCH (x.x.1)**: Documentation or script fixes.

**Version**: 3.0.0 | **Ratified**: 2026-01-10 | **Last Amended**: 2026-01-10