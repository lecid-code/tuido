import pytest
from unittest.mock import Mock
from tuido.task_manager import TaskManager


class MockData:
    def __init__(self):
        self.tasks = []
        self.next_id = 1


@pytest.fixture
def task_manager():
    repo = Mock()
    repo.load_data.return_value = MockData()
    return TaskManager(repo)


def test_add_task(task_manager):
    task = task_manager.add_task("Test task")
    
    assert task.id == 1
    assert task.description == "Test task"
    assert len(task_manager.all_tasks()) == 1


def test_delete_task(task_manager):
    task = task_manager.add_task("Task to delete")
    
    assert task_manager.delete_task(task.id).id == task.id
    assert len(task_manager.all_tasks()) == 0
    assert task_manager.delete_task(999) is None


def test_complete_task(task_manager):
    task = task_manager.add_task("Task to complete")
    
    assert task_manager.set_task_complete(task.id) is True
    assert task.is_complete() is True
    assert task_manager.set_task_complete(task.id) is False  # Already complete


def test_pending_task(task_manager):
    task = task_manager.add_task("Task to make pending")
    task_manager.set_task_complete(task.id)
    
    assert task_manager.set_task_pending(task.id) is True
    assert task.is_complete() is False
    assert task_manager.set_task_pending(task.id) is False  # Already pending


def test_all_tasks(task_manager):
    assert task_manager.all_tasks() == []
    
    task1 = task_manager.add_task("Task 1")
    task2 = task_manager.add_task("Task 2")
    
    tasks = task_manager.all_tasks()
    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks