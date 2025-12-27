---
description: "Task list for Todo In-Memory Console App implementation"
---

# Tasks: Todo In-Memory Console App

**Input**: Design documents from `specs/1-todo-console-app/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli-api.md
**Tests**: OPTIONAL (included as per plan for unit/integration verification)
**Organization**: Tasks grouped by user story to enable independent implementation and testing.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [x] T001 Initialize Python project with `uv init` and gitignore
- [x] T002 Add dependencies: `typer`, `rich`, `pytest` via `uv add`
- [x] T003 Create project structure: `src/` and `tests/` folders with `__init__.py` files
- [x] T003a Create empty module files: `src/models.py`, `src/services.py`, `src/cli.py`, `src/utils.py`, `src/main.py`
- [x] T004 Create `README.md` and `CLAUDE.md` placeholders

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data models and services required by all user stories.

- [x] T005 [P] Implement `TaskStatus` Enum in `src/models.py`
- [x] T006 [P] Implement `Task` dataclass in `src/models.py` with factory method for creation
- [x] T007 Implement `test_models.py` to verify Task validation (empty title)
- [x] T008 Implement `TaskManager` class skeleton in `src/services.py` (singleton/store pattern)
- [x] T009 Implement `conftest.py` in `tests/` with fixture to reset `TaskManager` state
- [x] T010 Setup `src/main.py` entry point and `src/cli.py` Typer app skeleton

**Checkpoint**: Core data structures exist. CLI entry point runs (even if empty).

## Phase 3: User Story 1 - Create and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can add tasks and see them in a list.
**Independent Test**: `uv run todo add "Test"` -> `uv run todo list` shows "Test".

### Tests (Unit & Integration)
- [x] T011 [US1] Create unit tests for `TaskManager.add_task` and `get_all_tasks` in `tests/test_services.py`
- [x] T012 [US1] Create CLI integration tests for `add` and `list` commands in `tests/test_cli.py`

### Implementation
- [x] T013 [US1] Implement `add_task` logic in `src/services.py` (auto-increment ID)
- [x] T014 [US1] Implement `get_all_tasks` logic in `src/services.py`
- [x] T015 [US1] Implement `add` command in `src/cli.py` (using `rich` for success msg)
- [x] T016 [US1] Implement `list` command in `src/cli.py` (using `rich.table` for output, refactor to `src/utils.py` if complex)

**Checkpoint**: Basic MVP functional. Can add and list tasks.

## Phase 4: User Story 2 - Update and Complete Tasks (Priority: P2)

**Goal**: Users can modify tasks and mark them as done.
**Independent Test**: Add task -> Update title -> Verify list. Add task -> Complete -> Verify status.

### Tests
- [x] T017 [US2] Create unit tests for `TaskManager.update_task` and `complete_task` in `tests/test_services.py`
- [x] T018 [US2] Create CLI integration tests for `update` and `complete` commands in `tests/test_cli.py`

### Implementation
- [x] T019 [US2] Implement `update_task` logic in `src/services.py` (handle not found)
- [x] T020 [US2] Implement `complete_task` logic in `src/services.py` (toggle status)
- [x] T021 [US2] Implement `update` command in `src/cli.py`
- [x] T022 [US2] Implement `complete` command in `src/cli.py`

**Checkpoint**: Lifecycle management (Edit/Complete) functional.

## Phase 5: User Story 3 - Delete Tasks (Priority: P3)

**Goal**: Users can remove tasks.
**Independent Test**: Add task -> Delete -> Verify list is empty.

### Tests
- [x] T023 [US3] Create unit tests for `TaskManager.delete_task` in `tests/test_services.py`
- [x] T024 [US3] Create CLI integration tests for `delete` command in `tests/test_cli.py`

### Implementation
- [x] T025 [US3] Implement `delete_task` logic in `src/services.py`
- [x] T026 [US3] Implement `delete` command in `src/cli.py`

**Checkpoint**: Full CRUD lifecycle complete.

## Phase 6: User Story 4 - Interactive Mode (Priority: P2)

**Goal**: Users can interact with the app via a REPL.
**Independent Test**: Run `uv run todo interactive`, type `add "Test"`, then `list`, check output.

- [x] T027 [US4] Implement `interactive` command in `src/cli.py` using `rich.console.input` loop
- [x] T028 [US4] Implement command parsing logic to map input strings ("add ...") to Typer commands or Service methods
- [x] T029 [US4] Verify `exit` / `quit` command functionality

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Cleanup, documentation, and final validation.

- [x] T030 Refactor `src/utils.py` to centralize formatting logic (if duplicated)
- [x] T031 Update `README.md` with concrete usage examples from implementation
- [x] T032 Run full regression suite (`uv run pytest`) and fix any regressions
- [x] T033 Verify startup time < 1s manually

## Dependencies & Execution Order

1. **Setup (Phase 1)**: Blocks everything.
2. **Foundational (Phase 2)**: Blocks all User Stories. Models must exist before Services.
3. **User Stories (Phase 3-5)**: 
   - US1 (Add/List) is prerequisite for US2/US3 testing (need tasks to update/delete).
   - US2 and US3 can technically be built in parallel, but US1 is the blocker.

## Parallel Execution Examples

**Phase 2 (Foundational)**:
- T005 (`TaskStatus`), T006 (`Task`), T010 (`main.py`) can be written in parallel.

**Phase 3 (US1)**:
- T011 (Tests) and T013/T014 (Service Logic) can be parallelized (TDD style).
- T015/T016 (CLI commands) depend on Service Logic.

## Implementation Strategy

1. **MVP**: Complete Phase 1, 2, and 3. This delivers a working "Add & List" tool.
2. **Increment 1**: Add Phase 4 (Update/Complete).
3. **Increment 2**: Add Phase 5 (Delete) + Phase 6 (Polish).