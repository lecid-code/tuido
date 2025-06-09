
from dataclasses import dataclass, field
import datetime

@dataclass
class Task:
    id: int
    description: str
    created_at: datetime = field(default_factory=datetime.datetime.now)
    completed_at: datetime = None

    def is_complete(self) -> bool:
        return self.completed_at is not None
    
    def mark_complete(self) -> bool:
        if self.is_complete():
            return False
        self.completed_at = datetime.datetime.now()
        return True
    
    def mark_pending(self) -> bool:
        if not self.is_complete():
            return False
        self.completed_at = None
        return True