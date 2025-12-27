# Feature Specification: Todo In-Memory Console App

**Feature Branch**: `1-todo-console-app`
**Created**: 2025-12-27
**Status**: Draft
**Input**: User description: "I want to implement the basic CLI structure and task management features Phase I..."

## User Scenarios & Testing

### User Story 1 - Create and View Tasks (Priority: P1)

As a user, I want to add new tasks and view them in a list so that I can capture and track my work items.

**Why this priority**: Core functionality. Without adding and viewing tasks, the application serves no purpose.

**Independent Test**: Can be fully tested by launching the app, adding a task, and verifying it appears in the list output.

**Acceptance Scenarios**:

1. **Given** the app is started, **When** I enter the command to add a task with title "Buy Milk" and description "Skimmed", **Then** the system confirms the task was added with a unique ID.
2. **Given** I have added tasks, **When** I enter the command to list tasks, **Then** the system displays all added tasks with their IDs, titles, and current status (default: Pending).
3. **Given** the app is restarted, **When** I list tasks, **Then** the list is empty (in-memory constraint).

---

### User Story 2 - Update and Complete Tasks (Priority: P2)

As a user, I want to modify task details and mark them as complete so that I can keep my todo list accurate and track progress.

**Why this priority**: Essential for managing the lifecycle of a task.

**Independent Test**: Can be tested by adding a task, then modifying it and verifying the change in the list view.

**Acceptance Scenarios**:

1. **Given** a task exists with ID 1, **When** I update task 1's title to "Buy Soy Milk", **Then** the system confirms the update and the list view shows the new title.
2. **Given** a task exists with ID 1 (Pending), **When** I mark task 1 as complete, **Then** the list view shows the task status as [X] or "Complete".
3. **Given** a task exists with ID 1 (Complete), **When** I mark task 1 as incomplete, **Then** the list view shows the task status as [ ] or "Pending".

---

### User Story 3 - Delete Tasks (Priority: P3)

As a user, I want to remove tasks by their ID so that I can declutter my list from erroneous or unwanted items.

**Why this priority**: Important for list maintenance but less critical than creating/completing.

**Independent Test**: Can be tested by adding a task, deleting it, and verifying it is gone.

**Acceptance Scenarios**:

1. **Given** a task exists with ID 1, **When** I delete task 1, **Then** the system confirms deletion and the task no longer appears in the list.
2. **Given** no task exists with ID 99, **When** I try to delete task 99, **Then** the system displays an error message stating the ID was not found.

---

### User Story 4 - Interactive Mode (Priority: P2)

As a user, I want to start the application once and interact with it via a continuous prompt (REPL) so that I don't have to restart the command for every action.

**Why this priority**: Enhances user experience significantly for a "console app".

**Independent Test**: Launch `uv run todo interactive`, then type `add "Test"`, then `list`, then `exit`.

**Acceptance Scenarios**:

1. **Given** I run `uv run todo interactive`, **When** the app starts, **Then** I see a prompt (e.g. `todo>`).
2. **Given** I am in interactive mode, **When** I type `add "My Task"`, **Then** the task is added and I see the prompt again.
3. **Given** I am in interactive mode, **When** I type `exit` or `quit`, **Then** the application exits.

### Edge Cases

- **Empty Input**: User provides empty title or description. System should reject or provide default? (Assume reject empty title).
- **Invalid ID**: User provides non-numeric ID or ID not in list. System should show error.
- **Concurrency**: Not applicable (single user CLI).
- **Memory Limit**: Python process memory limits apply; assumed sufficient for "Basic Level".

## Requirements

### Functional Requirements

- **FR-001**: System MUST allow adding a task with a `title` (required) and `description` (optional).
- **FR-002**: System MUST assign a unique auto-incrementing integer ID to each new task.
- **FR-003**: System MUST display all tasks in a formatted list showing ID, Status, and Title.
- **FR-004**: System MUST allow updating a task's title and/or description using its ID.
- **FR-005**: System MUST allow toggling a task's status between "Pending" and "Completed".
- **FR-006**: System MUST allow deleting a task using its ID.
- **FR-007**: System MUST store all data in memory ONLY. Data MUST NOT persist after the application exits.
- **FR-008**: System MUST provide a command-line interface (CLI) for all interactions (no GUI).
- **FR-009**: System MUST handle invalid inputs (e.g., non-existent IDs) gracefully with user-friendly error messages.
- **FR-010**: System MUST provide an interactive REPL mode where state is maintained during the session.

### Key Entities

- **Task**:
  - `id`: Integer (Unique)
  - `title`: String
  - `description`: String (Optional)
  - `status`: Enum/Boolean (Pending/Completed)
  - `created_at`: Timestamp (Optional, good practice)

## Success Criteria

### Measurable Outcomes

- **SC-001**: User can perform the full lifecycle (Add -> View -> Update -> Complete -> Delete) of a task without errors.
- **SC-002**: Application startup time is under 1 second.
- **SC-003**: 100% of data is cleared upon application restart (verified by testing).
- **SC-004**: Application adheres to Python 3.13+ standards (verified by `uv` and linting).
- **SC-005**: User can execute at least 5 commands in a single interactive session.