"""Task data management module for TUIDO."""
from dataclasses import dataclass, field
from typing import List

from tuido.task import Task


@dataclass
class TaskData:
    """Data structure to hold tasks and the next available task ID."""
    tasks: List[Task] = field(default_factory=list)
    next_id: int = 1
