"""Repository for managing tasks stored in a JSON file."""
import datetime
import json
import os
import sys
from pathlib import Path

from tuido.task import Task
from tuido.task_data import TaskData
from tuido.task_repository import TaskRepository


class JsonTaskRepository(TaskRepository):
    """Repository for managing tasks stored in a JSON file."""
    def __init__(self, file_path: str) -> None:
        """Initialize the repository with the given file path."""
        self.file_path = Path(os.path.expanduser(file_path))

    def load_data(self) -> TaskData:
        """Load tasks from the JSON file."""
        if not self.file_path.exists():
            return TaskData()

        with self.file_path.open("r", encoding='utf-8') as file:
            data = json.load(file)
            tasks = [self._dict_to_task(task) for task in data.get("tasks", [])]
            next_id = data.get("next_id", 1)
            return TaskData(tasks=tasks, next_id=next_id)

    def save_data(self, tasks: TaskData) -> None:
        """Save tasks to the JSON file."""
        try:
            # Ensure parent directory exists
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

            with open(self.file_path, mode="w", encoding="utf-8") as file:
                data = {
                    "tasks": [self._task_to_dict(task) for task in tasks.tasks],
                    "next_id": tasks.next_id,
                }
                json.dump(data, file, indent=4)

        except PermissionError:
            print(f"Error: Permission denied writing to {self.file_path}")
            print("Check file permissions or try running with appropriate privileges")
            sys.exit(1)
        except FileNotFoundError:
            print(f"Error: Directory not found for {self.file_path}")
            print("Ensure the directory exists")
            sys.exit(1)
        except OSError as e:
            print(f"Error: System error writing file - {e}")
            sys.exit(1)

    def _task_to_dict(self, task: Task) -> dict:
        return {
            "id": task.id,
            "description": task.description,
            "created_at": task.created_at.isoformat(),
            "completed_at": (
                task.completed_at.isoformat() if task.completed_at else None
            ),
        }

    def _dict_to_task(self, data: dict) -> Task:
        return Task(
            id=data["id"],
            description=data["description"],
            created_at=datetime.datetime.fromisoformat(data["created_at"]),
            completed_at=(
                datetime.datetime.fromisoformat(data["completed_at"])
                if data["completed_at"]
                else None
            ),
        )
