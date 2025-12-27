# Research: Todo In-Memory Console App

**Feature**: Todo In-Memory Console App
**Date**: 2025-12-27

## Decision 1: CLI Library Selection

**Context**: The project requires a command-line interface. The constitution mandates "Minimal external dependencies; standard library preferred for core logic" but also "Modern Python Standards" and "Clean Code".

**Options**:
1.  **argparse** (Standard Library)
2.  **Typer** (External, built on Click)
3.  **Click** (External)

**Decision**: **Typer**

**Rationale**:
- **Modern Python**: Typer leverages Python 3.6+ type hints heavily, aligning perfectly with the "Modern Python Standards" principle.
- **Clean Code**: It drastically reduces boilerplate compared to `argparse`, making the code easier to read and maintain for both humans and agents.
- **Agentic Development**: Agents (Claude Code) are very effective at generating Typer code due to its declarative nature.
- **Dependency**: While it adds a dependency, `uv` makes management trivial, and the DX/maintainability gain outweighs the cost of one lightweight dependency. It is the de-facto standard for modern Python CLIs.

## Decision 2: Testing Framework

**Context**: Robust testing is required.

**Options**:
1.  **unittest** (Standard Library)
2.  **pytest** (External)

**Decision**: **pytest**

**Rationale**:
- **Industry Standard**: `pytest` is the overwhelming standard for modern Python testing.
- **Simplicity**: Supports simple assert statements (no `self.assertEqual`), reducing boilerplate.
- **Fixtures**: Powerful fixture system for managing state (even in-memory state).
- **Alignment**: Fits "Modern Python Standards" better than `unittest`'s Java-esque style.

## Decision 3: Data Modeling

**Context**: Storing tasks in memory.

**Options**:
1.  **Standard Classes**
2.  **dataclasses** (Standard Library)
3.  **Pydantic** (External)

**Decision**: **dataclasses** (with `enums`)

**Rationale**:
- **Minimalism**: For an in-memory app without complex serialization/validation needs (like JSON APIs), standard `dataclasses` are sufficient and lightweight.
- **Standard Library**: Adheres to the preference for standard library for core logic where external tools aren't providing massive leverage (unlike CLI parsing).
- **Upgrade Path**: Easy to migrate to Pydantic later if persistence (JSON/DB) is added in Phase II.

## Decision 4: Project Structure

**Decision**: Single project structure with `src/` layout.

```text
src/
├── main.py          # Entry point
├── models.py        # Task dataclass
├── services.py      # Business logic (TaskManager)
├── cli.py           # Typer commands
└── utils.py         # Formatting helpers
tests/
├── test_models.py
├── test_services.py
└── test_cli.py
```

**Rationale**: Simple, modular, and separates concerns (CLI vs Logic vs Data) as required by "Proper Python project structure".
