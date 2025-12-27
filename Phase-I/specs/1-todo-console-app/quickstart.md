# Quickstart: Todo In-Memory Console App

## Prerequisites
- Python 3.13+
- `uv` installed (`pip install uv`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone [repo-url]
   cd [repo-name]
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

## Running the App

The app entry point is managed via `uv run`.

```bash
# Add a task
uv run todo add "Buy Groceries" -d "Milk, Eggs, Bread"

# List tasks
uv run todo list

# Complete a task
uv run todo complete 1

# Delete a task
uv run todo delete 1
```

## Running Tests

```bash
uv run pytest
```
