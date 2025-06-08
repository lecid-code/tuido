from dataclasses import dataclass, field
from typing import List

from task import Task


@dataclass
class TaskData:
    tasks: List[Task] = field(default_factory=list)
    next_id: int = 1