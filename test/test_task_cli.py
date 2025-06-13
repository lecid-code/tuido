"""Unit tests for the TaskCLI class in the tuido module."""

from unittest.mock import Mock

import pytest

from tuido.task_cli import TaskCLI


class TestTaskCLI:
    """Unit tests for the TaskCLI class in the tuido module."""

    @pytest.fixture
    def cli(self):
        """Fixture to create a TaskCLI instance with a mock console."""
        console = Mock()
        return TaskCLI(console=console), console

    @pytest.fixture
    def mock_task_manager(self):
        """Fixture to create a mock TaskManager."""
        return Mock()

    def test_add_task_success(self, cli, mock_task_manager):
        """Test adding a task successfully."""
        task_cli, console = cli

        # Mock the returned task
        new_task = Mock()
        new_task.id = 1
        new_task.description = "Test task"
        mock_task_manager.add_task.return_value = new_task

        task_cli._handle_add(  # pylint: disable=protected-access
            mock_task_manager, "Test task"
        )

        mock_task_manager.add_task.assert_called_once_with("Test task")
        console.print.assert_called_once()

    def test_add_empty_task_fails(self, cli, mock_task_manager):
        """Test adding an empty task raises SystemExit."""
        task_cli, _ = cli

        with pytest.raises(SystemExit):
            task_cli._handle_add(  # pylint: disable=protected-access
                mock_task_manager, ""
            )

        mock_task_manager.add_task.assert_not_called()

    def test_add_task_strips_whitespace(self, cli, mock_task_manager):
        """Test that adding a task strips leading and trailing whitespace."""
        task_cli, _ = cli
        mock_task_manager.add_task.return_value = Mock(id=1, description="Test")

        task_cli._handle_add(  # pylint: disable=protected-access
            mock_task_manager, "  Test  "
        )

        mock_task_manager.add_task.assert_called_once_with("Test")

    def test_complete_task_success(self, cli, mock_task_manager):
        """Test completing a task successfully."""
        task_cli, _ = cli
        mock_task_manager.set_task_complete.return_value = True

        task_cli._handle_do(mock_task_manager, 1)  # pylint: disable=protected-access

        mock_task_manager.set_task_complete.assert_called_once_with(1)

    def test_complete_nonexistent_task_fails(self, cli, mock_task_manager):
        """Test completing a nonexistent task raises SystemExit."""
        task_cli, _ = cli
        mock_task_manager.set_task_complete.return_value = False

        with pytest.raises(SystemExit):
            task_cli._handle_do(  # pylint: disable=protected-access
                mock_task_manager, 999
            )

    def test_undo_task_success(self, cli, mock_task_manager):
        """Test undoing a completed task successfully."""
        task_cli, _ = cli
        mock_task_manager.set_task_pending.return_value = True

        task_cli._handle_undo(mock_task_manager, 1)  # pylint: disable=protected-access

        mock_task_manager.set_task_pending.assert_called_once_with(1)

    def test_delete_task_success(self, cli, mock_task_manager):
        """Test deleting a task successfully."""
        task_cli, _ = cli
        deleted_task = Mock(id=1, description="Deleted task")
        mock_task_manager.delete_task.return_value = deleted_task

        task_cli._handle_delete(  # pylint: disable=protected-access
            mock_task_manager, 1
        )

        mock_task_manager.delete_task.assert_called_once_with(1)

    def test_delete_nonexistent_task_fails(self, cli, mock_task_manager):
        """Test deleting a nonexistent task raises SystemExit."""
        task_cli, _ = cli
        mock_task_manager.delete_task.return_value = None

        with pytest.raises(SystemExit):
            task_cli._handle_delete(  # pylint: disable=protected-access
                mock_task_manager, 999
            )

    def test_list_empty_tasks(self, cli, mock_task_manager):
        """Test listing tasks when there are no tasks."""
        task_cli, console = cli
        mock_task_manager.all_tasks.return_value = []

        task_cli._handle_list(mock_task_manager)  # pylint: disable=protected-access

        mock_task_manager.all_tasks.assert_called_once()
        console.print.assert_called_once()
