"""Task repository interface for loading and saving tasks."""

from abc import ABC, abstractmethod

from tuido.task_data import TaskData


class TaskRepository(ABC):
    """Abstract base class for task repositories."""

    @abstractmethod
    def load_data(self) -> TaskData:
        """Load tasks from the repository."""

    @abstractmethod
    def save_data(self, tasks: TaskData) -> None:
        """Save tasks to the repository."""
