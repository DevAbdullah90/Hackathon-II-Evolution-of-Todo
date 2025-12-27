import pytest
from src.models import Task, TaskStatus

def test_create_task():
    task = Task(id=1, title="Test")
    assert task.id == 1
    assert task.title == "Test"
    assert task.status == TaskStatus.PENDING

def test_empty_title_raises_error():
    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task(id=1, title="")
