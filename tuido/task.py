"""A module for managing tasks with completion status."""

import datetime
from dataclasses import dataclass, field


@dataclass
class Task:
    """A class representing a task with an ID, description, and completion status."""

    id: int
    description: str
    created_at: datetime = field(default_factory=datetime.datetime.now)
    completed_at: datetime = None

    def is_complete(self) -> bool:
        """Check if the task is complete."""
        return self.completed_at is not None

    def mark_complete(self) -> bool:
        """Mark the task as complete."""
        if self.is_complete():
            return False
        self.completed_at = datetime.datetime.now()
        return True

    def mark_pending(self) -> bool:
        """Mark the task as pending."""
        if not self.is_complete():
            return False
        self.completed_at = None
        return True
