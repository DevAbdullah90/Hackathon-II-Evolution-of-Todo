from typing import Dict, List, Optional
from src.models import Task, TaskStatus

class TaskManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks: Dict[int, Task] = {}
            cls._instance.next_id = 1
        return cls._instance

    def reset(self):
        self.tasks = {}
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return list(self.tasks.values())

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        
        task = self.tasks[task_id]
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty")
            task.title = title
        if description is not None:
            task.description = description
        return task

    def complete_task(self, task_id: int) -> Task:
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        
        task = self.tasks[task_id]
        task.status = TaskStatus.COMPLETED
        return task

    def delete_task(self, task_id: int):
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        del self.tasks[task_id]