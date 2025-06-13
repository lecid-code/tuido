"""Task Manager for TUIDO Application"""
from tuido.task import Task
from tuido.task_repository import TaskRepository


class TaskManager:
    """Manager for handling tasks in the TUIDO application."""
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository
        self.data = self.repository.load_data()

    def _get_task_by_id(self, task_id: int) -> Task | None:
        return next((t for t in self.data.tasks if t.id == task_id), None)

    def _save(self):
        self.repository.save_data(self.data)

    def add_task(self, description: str) -> Task:
        """Add a new task with the given description."""
        task = Task(id=self.data.next_id, description=description)
        self.data.tasks.append(task)
        self.data.next_id += 1
        self._save()
        return task

    def delete_task(self, task_id: int) -> Task | None:
        """Delete a task by its ID."""
        task = self._get_task_by_id(task_id)
        if task:
            self.data.tasks.remove(task)
            self._save()
        return task

    def set_task_complete(self, task_id: int) -> bool:
        """Mark a task as complete by its ID."""
        task = self._get_task_by_id(task_id)
        if task and not task.is_complete():
            task.mark_complete()
            self._save()
            return True
        return False

    def set_task_pending(self, task_id: int) -> bool:
        """Mark a task as pending by its ID."""
        task = self._get_task_by_id(task_id)
        if task and task.is_complete():
            task.mark_pending()
            self._save()
            return True
        return False

    def all_tasks(self) -> list[Task]:
        """Return all tasks, both pending and completed."""
        return self.data.tasks
