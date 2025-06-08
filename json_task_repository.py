import datetime
from task_repository import TaskRepository
from task_data import TaskData
from task import Task
import json
from pathlib import Path

class JsonTaskRepository(TaskRepository):
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def load_data(self) -> TaskData:
        if not self.file_path.exists():
            return TaskData()

        with self.file_path.open('r') as file:
            data = json.load(file)
            tasks = [self._dict_to_task(task) for task in data.get('tasks', [])]
            next_id = data.get('next_id', 1)
            return TaskData(tasks=tasks, next_id=next_id)

    def save_data(self, tasks: TaskData) -> None:
        with self.file_path.open('w') as file:
            data = {
                'tasks': [self._task_to_dict(task) for task in tasks.tasks],
                'next_id': tasks.next_id
            }
            json.dump(data, file, indent=4)

    def _task_to_dict(self, task: Task) -> dict:
        return {
            'id': task.id,
            'description': task.description,
            'created_at': task.created_at.isoformat(),
            'completed_at': task.completed_at.isoformat() if task.completed_at else None
        }
    
    def _dict_to_task(self, data: dict) -> Task:
        return Task(
            id=data['id'],
            description=data['description'],
            created_at=datetime.datetime.fromisoformat(data['created_at']),
            completed_at=datetime.datetime.fromisoformat(data['completed_at']) if data['completed_at'] else None
        )