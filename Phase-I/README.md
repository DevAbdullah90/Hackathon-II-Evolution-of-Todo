# Todo In-Memory Console App

A simple CLI todo app storing tasks in memory.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

### Interactive Mode (Recommended)

Just run the app without arguments:
```bash
uv run todo
```
Then type commands like:
- `add "Buy Milk"`
- `list`
- `complete 1`
- `delete 1`
- `exit`

### Single Command Mode

Use `uv run todo` to access the CLI directly.

```bash
# Add tasks
uv run todo add "Buy Milk" -d "Skimmed"
uv run todo add "Walk Dog"

# List tasks
uv run todo list
uv run todo list --show-completed

# Update task
uv run todo update 1 --title "Buy Soy Milk"

# Complete task
uv run todo complete 1

# Delete task
uv run todo delete 2
```

## Development

Run tests:
```bash
uv run pytest
```
