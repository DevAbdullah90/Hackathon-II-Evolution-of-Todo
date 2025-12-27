from typer.testing import CliRunner
from src.cli import app
from src.services import TaskManager
from src.models import TaskStatus

runner = CliRunner()

def test_add_command():
    result = runner.invoke(app, ["add", "Buy Milk", "-d", "Skimmed"])
    assert result.exit_code == 0
    # Match the new fancy output format
    assert "Task added:" in result.stdout
    assert "Buy Milk" in result.stdout

def test_list_command():
    manager = TaskManager()
    manager.add_task("Buy Milk", "Skimmed")
    
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "1" in result.stdout
    assert "Buy Milk" in result.stdout
    assert "Skimmed" in result.stdout

def test_update_command():
    manager = TaskManager()
    task = manager.add_task("Original")
    result = runner.invoke(app, ["update", str(task.id), "--title", "Updated"])
    assert result.exit_code == 0
    assert "Task 1 updated" in result.stdout
    assert manager.tasks[1].title == "Updated"

def test_complete_command():
    manager = TaskManager()
    task = manager.add_task("To Do")
    result = runner.invoke(app, ["complete", str(task.id)])
    assert result.exit_code == 0
    assert "Task 1 marked as completed" in result.stdout
    assert manager.tasks[1].status == TaskStatus.COMPLETED

def test_delete_command():
    manager = TaskManager()
    task = manager.add_task("To Delete")
    result = runner.invoke(app, ["delete", str(task.id)])
    assert result.exit_code == 0
    assert "Task 1 deleted" in result.stdout
    assert len(manager.tasks) == 0