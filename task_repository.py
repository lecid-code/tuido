from abc import ABC, abstractmethod

from task_data import TaskData

class TaskRepository(ABC):
    @abstractmethod
    def load_data(self) -> TaskData:
        """Load tasks from the repository."""
        pass

    @abstractmethod
    def save_data(self, tasks: TaskData) -> None:    
        """Save tasks to the repository."""
        pass