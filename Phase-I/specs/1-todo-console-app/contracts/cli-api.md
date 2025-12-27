# CLI Contract: Todo In-Memory Console App

**Type**: Command Line Interface
**Framework**: Typer

## Global Options

- `--help`: Show help message and exit.
- `--version`: Show application version.

## Commands

### 1. Add Task
Create a new task.

**Usage**: `todo add [OPTIONS] TITLE`

**Arguments**:
- `TITLE` (Required): The title of the task.

**Options**:
- `--description`, `-d` (Optional): A description for the task.

**Output**:
- Success: `Task added: [ID] "Title"`
- Error: `Error: Title cannot be empty.`

---

### 2. List Tasks
Show all tasks in a table/list format.

**Usage**: `todo list [OPTIONS]`

**Options**:
- `--show-completed/--no-show-completed` (Optional): Filter to show/hide completed tasks. (Default: Show all)

**Output**:
```text
ID  | Status    | Title           | Description
--- | --------- | --------------- | -----------
1   | [ ]       | Buy Milk        | Skimmed
2   | [x]       | Walk Dog        |
```

---

### 3. Update Task
Modify an existing task.

**Usage**: `todo update [OPTIONS] TASK_ID`

**Arguments**:
- `TASK_ID` (Required): ID of the task to update.

**Options**:
- `--title`, `-t` (Optional): New title.
- `--description`, `-d` (Optional): New description.

**Output**:
- Success: `Task [ID] updated.`
- Error: `Error: Task with ID [ID] not found.`

---

### 4. Complete Task
Mark a task as completed.

**Usage**: `todo complete TASK_ID`

**Arguments**:
- `TASK_ID` (Required): ID of the task.

**Output**:
- Success: `Task [ID] marked as completed.`
- Error: `Error: Task with ID [ID] not found.`

---

### 5. Delete Task
Permanently remove a task.

**Usage**: `todo delete TASK_ID`

**Arguments**:
- `TASK_ID` (Required): ID of the task.

**Output**:
- Success: `Task [ID] deleted.`
- Error: `Error: Task with ID [ID] not found.`
