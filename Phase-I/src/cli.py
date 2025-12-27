import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from src.services import TaskManager
from src.models import TaskStatus
from typing import Optional
import shlex
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

app = typer.Typer()
console = Console()
manager = TaskManager()

COMMANDS = ["add", "list", "update", "complete", "delete", "help", "exit", "quit"]

def print_help_panel():
    """Display the interactive mode help panel."""
    commands_md = """
- **add <title>**: Create a new task (e.g., `add "Buy Milk"`)
- **list**: Show all tasks
- **update <id>**: Modify a task (e.g., `update 1 --title "New Name"`)
- **complete <id>**: Mark a task as done (e.g., `complete 1`)
- **delete <id>**: Remove a task (e.g., `delete 1`)
- **help**: Show this menu
- **exit** / **quit**: Exit the application
    """
    panel = Panel(
        Markdown(commands_md),
        title="[bold green]Available Commands[/bold green]",
        border_style="blue",
        expand=False
    )
    console.print(panel)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Todo In-Memory Console App.
    Run without arguments to start Interactive Mode.
    """
    if ctx.invoked_subcommand is None:
        interactive()

@app.command(name="add")
def add_task(title: str, description: str = typer.Option("", "--description", "-d")):
    """Add a new task."""
    try:
        task = manager.add_task(title, description)
        console.print(f'[green]✓ Task added:[/green] [bold]{task.title}[/bold] (ID: {task.id})')
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command(name="list")
def list_tasks(show_completed: bool = typer.Option(True, "--show-completed/--no-show-completed")):
    """List all tasks."""
    tasks = manager.get_all_tasks()
    if not tasks:
        console.print(Panel("No tasks found. Use 'add <title>' to create one!", style="yellow"))
        return

    table = Table(title="My Tasks", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="cyan", width=4)
    table.add_column("Status", justify="center", width=8)
    table.add_column("Title", style="white")
    table.add_column("Description", style="dim")

    for task in tasks:
        if not show_completed and task.status.value == "Completed":
            continue
        
        is_done = task.status.value == "Completed"
        status_mark = "[green]DONE[/green]" if is_done else "[yellow]TODO[/yellow]"
        title_text = f"[strike]{task.title}[/strike]" if is_done else task.title
        
        table.add_row(str(task.id), status_mark, title_text, task.description)
    
    console.print(table)

@app.command(name="update")
def update_task_cmd(
    task_id: int, 
    title: Optional[str] = typer.Option(None, "--title", "-t"), 
    description: Optional[str] = typer.Option(None, "--description", "-d")
):
    """Update an existing task."""
    try:
        task = manager.update_task(task_id, title=title, description=description)
        console.print(f'[green]✓ Task {task.id} updated.[/green]')
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command(name="complete")
def complete_task_cmd(task_id: int):
    """Mark a task as completed."""
    try:
        task = manager.complete_task(task_id)
        console.print(f'[green]✓ Task {task.id} marked as completed.[/green]')
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command(name="delete")
def delete_task_cmd(task_id: int):
    """Delete a task."""
    try:
        manager.delete_task(task_id)
        console.print(f'[green]✓ Task {task_id} deleted.[/green]')
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command(name="interactive")
def interactive():
    """Start the interactive REPL with history and autocompletion."""
    console.clear()
    console.print(Panel.fit(
        "[bold blue]Welcome to your Todo App![/bold blue]\n"
        "Manage your tasks simply and efficiently.",
        border_style="green"
    ))
    print_help_panel()
    
    history = InMemoryHistory()
    completer = WordCompleter(COMMANDS, ignore_case=True)
    
    style = Style.from_dict({
        'prompt': 'cyan bold',
    })
    
    session = PromptSession(history=history, completer=completer, style=style)

    while True:
        try:
            command = session.prompt([('class:prompt', 'todo > ')])
            
            if not command.strip():
                continue
            
            if command.lower() in ("exit", "quit"):
                console.print("[yellow]Goodbye![/yellow]")
                break
            
            if command.lower() in ("help", "?"):
                print_help_panel()
                continue
            
            try:
                args = shlex.split(command)
            except ValueError as e:
                console.print(f"[red]Error parsing command: {e}[/red]")
                continue

            cmd_name = args[0]
            
            if cmd_name in COMMANDS:
                try:
                    app(args, standalone_mode=False, prog_name="todo")
                except SystemExit:
                    pass
                except Exception as e:
                    console.print(f"[red]Unexpected error: {e}[/red]")
            else:
                console.print(f"[red]Unknown command: '{cmd_name}'[/red]")
                console.print(f"Did you mean: [bold green]add \"{command}\"[/bold green]?")
                console.print("Type [bold]help[/bold] to see available commands.")

        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting...[/yellow]")
            break
        except EOFError:
            break

if __name__ == "__main__":
    app()