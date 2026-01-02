# 📝 Todo In-Memory Console App

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Phase%20I-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Code Style](https://img.shields.io/badge/Code%20Style-Ruff-000000?style=for-the-badge)

A lightning-fast, beautiful command-line task manager built with **Python**, **Typer**, and **Rich**. Designed for speed and simplicity, it features a persistent interactive mode, colorful output, and efficient in-memory state management.

---

## ✨ Features

- **🚀 Interactive REPL Mode**: A persistent shell session with command history and auto-completion.
- **🎨 Rich UI**: Beautifully formatted tables, panels, and status indicators using `rich`.
- **⚡ Zero Latency**: In-memory storage ensures instant feedback for all operations.
- **🛠️ Robust CLI**: Fully featured command-line interface for scripting and single-command usage.
- **✅ Task Management**: Full lifecycle support: Create, Read, Update, Delete, and Complete tasks.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.13** or higher
- **[uv](https://github.com/astral-sh/uv)** (The blazing fast Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd phase-i
   ```

2. **Sync dependencies**
   ```bash
   uv sync
   ```

---

## 📖 Usage Guide

You can use the application in two ways: **Interactive Mode** (Recommended) or **Single Command Mode**.

### 🌟 Interactive Mode
Launch the persistent shell to manage tasks efficiently without restarting the app.

```bash
uv run todo
```

**Inside the shell:**
```text
todo > add "Finish the report" -d "Due by Friday"
todo > list
todo > complete 1
todo > update 1 --title "Submit report"
todo > delete 1
todo > exit
```

### ⚡ Single Command Mode
Run commands directly from your terminal.

| Action | Command |
| :--- | :--- |
| **Add a Task** | `uv run todo add "Buy Coffee" -d "Dark Roast"` |
| **List Tasks** | `uv run todo list` |
| **Complete Task** | `uv run todo complete <id>` |
| **Update Task** | `uv run todo update <id> --title "New Title"` |
| **Delete Task** | `uv run todo delete <id>` |
| **Help** | `uv run todo --help` |

---

## 📂 Project Structure

```text
phase-i/
├── pyproject.toml       # Project dependencies and metadata
├── uv.lock              # Lock file for reproducible builds
├── src/
│   ├── __init__.py
│   ├── cli.py           # Typer application & CLI entry point
│   ├── main.py          # App entry wrapper
│   ├── models.py        # Data models (Task, TaskStatus)
│   ├── services.py      # Business logic (TaskManager)
│   └── utils.py         # Helper functions
├── tests/
│   ├── test_cli.py      # Integration tests for CLI commands
│   ├── test_models.py   # Unit tests for data models
│   └── test_services.py # Unit tests for business logic
└── specs/               # Project documentation & specifications
```

---

## 🧪 Development

This project follows **Spec-Driven Development**. All features are defined in `specs/` before implementation.

### Running Tests
Ensure reliability with our comprehensive test suite.

```bash
uv run pytest -v
```

### Code Formatting
Maintain code quality with standard tools (configured via `uv`).

```bash
uv run ruff check .
uv run ruff format .
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.