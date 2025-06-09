import pytest
from unittest.mock import Mock
from tuido.task_cli import TaskCLI


class TestTaskCLI:
    
    @pytest.fixture
    def cli(self):
        console = Mock()
        return TaskCLI(console=console), console
    
    @pytest.fixture
    def mock_task_manager(self):
        return Mock()

    def test_add_task_success(self, cli, mock_task_manager):
        task_cli, console = cli
        
        # Mock the returned task
        new_task = Mock()
        new_task.id = 1
        new_task.description = "Test task"
        mock_task_manager.add_task.return_value = new_task
        
        task_cli._handle_add(mock_task_manager, "Test task")
        
        mock_task_manager.add_task.assert_called_once_with("Test task")
        console.print.assert_called_once()

    def test_add_empty_task_fails(self, cli, mock_task_manager):
        task_cli, console = cli
        
        with pytest.raises(SystemExit):
            task_cli._handle_add(mock_task_manager, "")
        
        mock_task_manager.add_task.assert_not_called()

    def test_add_task_strips_whitespace(self, cli, mock_task_manager):
        task_cli, console = cli
        mock_task_manager.add_task.return_value = Mock(id=1, description="Test")
        
        task_cli._handle_add(mock_task_manager, "  Test  ")
        
        mock_task_manager.add_task.assert_called_once_with("Test")

    def test_complete_task_success(self, cli, mock_task_manager):
        task_cli, console = cli
        mock_task_manager.set_task_complete.return_value = True
        
        task_cli._handle_do(mock_task_manager, 1)
        
        mock_task_manager.set_task_complete.assert_called_once_with(1)

    def test_complete_nonexistent_task_fails(self, cli, mock_task_manager):
        task_cli, console = cli
        mock_task_manager.set_task_complete.return_value = False
        
        with pytest.raises(SystemExit):
            task_cli._handle_do(mock_task_manager, 999)

    def test_undo_task_success(self, cli, mock_task_manager):
        task_cli, console = cli
        mock_task_manager.set_task_pending.return_value = True
        
        task_cli._handle_undo(mock_task_manager, 1)
        
        mock_task_manager.set_task_pending.assert_called_once_with(1)

    def test_delete_task_success(self, cli, mock_task_manager):
        task_cli, console = cli
        deleted_task = Mock(id=1, description="Deleted task")
        mock_task_manager.delete_task.return_value = deleted_task
        
        task_cli._handle_delete(mock_task_manager, 1)
        
        mock_task_manager.delete_task.assert_called_once_with(1)

    def test_delete_nonexistent_task_fails(self, cli, mock_task_manager):
        task_cli, console = cli
        mock_task_manager.delete_task.return_value = None
        
        with pytest.raises(SystemExit):
            task_cli._handle_delete(mock_task_manager, 999)

    def test_list_empty_tasks(self, cli, mock_task_manager):
        task_cli, console = cli
        mock_task_manager.all_tasks.return_value = []
        
        task_cli._handle_list(mock_task_manager)
        
        mock_task_manager.all_tasks.assert_called_once()
        console.print.assert_called_once()