# Data Model: Todo In-Memory Console App

**Feature**: Todo In-Memory Console App
**Source**: `specs/1-todo-console-app/spec.md`

## Entities

### Task

Represents a single work item.

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `id` | `int` | Yes | Unique identifier | Auto-incrementing, > 0 |
| `title` | `str` | Yes | Brief summary | Non-empty |
| `description` | `str` | No | Detailed info | Optional, defaults to empty string |
| `status` | `TaskStatus` | Yes | Current state | Enum: PENDING, COMPLETED |
| `created_at` | `datetime` | Yes | Creation timestamp | Set automatically on creation |

### TaskStatus (Enum)

| Value | Description |
|-------|-------------|
| `PENDING` | Task is open and needs action |
| `COMPLETED` | Task is finished |

## In-Memory Store

The application state will be held in a singleton or simple manager class.

```python
class TaskManager:
    tasks: Dict[int, Task]
    next_id: int = 1
```

## Validation Rules

1. **Title**: Must not be empty or whitespace only.
2. **ID**: Must be a positive integer existing in the store for Update/Delete/Get operations.
3. **Status**: Transitions allowed: PENDING <-> COMPLETED.
