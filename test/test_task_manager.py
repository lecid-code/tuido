"""Unit tests for the TaskManager class in the tuido module."""

from unittest.mock import Mock

import pytest

from tuido.task_manager import TaskManager


class MockData:
    """Mock data class to simulate a task repository."""

    def __init__(self):
        """Initialize with an empty task list and a next ID."""
        self.tasks = []
        self.next_id = 1


    @pytest.fixture
    def task_manager(self):
        """Fixture to create a TaskManager instance with a mock repository."""
        repo = Mock()
        repo.load_data.return_value = MockData()
        return TaskManager(repo)


    def test_add_task(self):
        """Test adding a new task to the task manager."""
        task = self.task_manager.add_task("Test task")

        assert task.id == 1
        assert task.description == "Test task"
        assert len(self.task_manager.all_tasks()) == 1


    def test_delete_task(self):
        """Test deleting a task from the task manager."""
        task = self.task_manager.add_task("Task to delete")

        assert self.task_manager.delete_task(task.id).id == task.id
        assert len(self.task_manager.all_tasks()) == 0
        assert self.task_manager.delete_task(999) is None


    def test_complete_task(self):
        """Test marking a task as complete."""
        task = self.task_manager.add_task("Task to complete")

        assert self.task_manager.set_task_complete(task.id) is True
        assert task.is_complete() is True
        assert self.task_manager.set_task_complete(task.id) is False  # Already complete


    def test_pending_task(self):
        """Test marking a task as pending."""
        task = self.task_manager.add_task("Task to make pending")
        self.task_manager.set_task_complete(task.id)

        assert self.task_manager.set_task_pending(task.id) is True
        assert task.is_complete() is False
        assert self.task_manager.set_task_pending(task.id) is False  # Already pending


    def test_all_tasks(self):
        """Test retrieving all tasks from the task manager."""
        assert self.task_manager.all_tasks() == []

        task1 = self.task_manager.add_task("Task 1")
        task2 = self.task_manager.add_task("Task 2")

        tasks = self.task_manager.all_tasks()
        assert len(tasks) == 2
        assert task1 in tasks
        assert task2 in tasks
