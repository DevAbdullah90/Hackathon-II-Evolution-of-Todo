import pytest
from src.services import TaskManager
from src.models import TaskStatus

def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Buy Milk", "Skimmed")
    assert task.id == 1
    assert task.title == "Buy Milk"
    assert task.description == "Skimmed"
    assert task.status == TaskStatus.PENDING
    
    task2 = manager.add_task("Walk Dog")
    assert task2.id == 2

def test_get_all_tasks():
    manager = TaskManager()
    manager.add_task("T1")
    manager.add_task("T2")
    tasks = manager.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "T1"
    assert tasks[1].title == "T2"

def test_update_task():
    manager = TaskManager()
    task = manager.add_task("Old Title")
    updated = manager.update_task(task.id, title="New Title", description="New Desc")
    assert updated.title == "New Title"
    assert updated.description == "New Desc"
    
    with pytest.raises(ValueError, match="not found"):
        manager.update_task(999, title="X")

def test_complete_task():
    manager = TaskManager()
    task = manager.add_task("To Do")
    completed = manager.complete_task(task.id)
    assert completed.status == TaskStatus.COMPLETED
    
    with pytest.raises(ValueError, match="not found"):
        manager.complete_task(999)

def test_delete_task():
    manager = TaskManager()
    task = manager.add_task("To Delete")
    manager.delete_task(task.id)
    assert len(manager.tasks) == 0
    
    with pytest.raises(ValueError, match="not found"):
        manager.delete_task(999)