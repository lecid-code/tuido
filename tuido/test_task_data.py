import pytest
from tuido.task_data import TaskData
from tuido.task import Task


def test_taskdata_default_initialization():
    """Test that TaskData initializes with safe defaults."""
    data = TaskData()
    assert data.tasks == []
    assert data.next_id == 1


def test_taskdata_list_isolation():
    """Test that each TaskData instance gets its own list (no shared mutable state)."""
    data1 = TaskData()
    data2 = TaskData()
    
    mock_task = Task(id=1, description='Test task')
    data1.tasks.append(mock_task)
    
    assert len(data1.tasks) == 1
    assert len(data2.tasks) == 0  # Should not be affected