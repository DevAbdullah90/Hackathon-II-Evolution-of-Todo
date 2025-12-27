import pytest
from src.services import TaskManager

@pytest.fixture(autouse=True)
def reset_task_manager():
    manager = TaskManager()
    manager.reset()
