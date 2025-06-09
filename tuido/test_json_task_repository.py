import datetime
import pytest
import json
import tempfile
from pathlib import Path

from tuido.json_task_repository import JsonTaskRepository
from tuido.task_data import TaskData
from tuido.task import Task


class TestJsonTaskRepository:
    
    @pytest.fixture
    def temp_file(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_path = Path(f.name)
        yield temp_path
        if temp_path.exists():
            temp_path.unlink()
    
    @pytest.fixture
    def repo(self, temp_file):
        return JsonTaskRepository(temp_file)
    
    def test_load_tasks_when_file_does_not_exist(self):
        """Returns empty TaskData when file doesn't exist."""
        repo = JsonTaskRepository(Path("non_existent.json"))
        task_data = repo.load_data()
        
        assert task_data.tasks == []
        assert task_data.next_id == 1
    
    def test_save_and_load_tasks(self, repo):
        """Can save and load tasks correctly."""
        tasks = [
            Task(id=1, description='Desc 1'),
            Task(id=2, description='Desc 2', completed_at=datetime.datetime.now())
        ]
        task_data = TaskData(tasks=tasks, next_id=3)
        
        repo.save_data(task_data)
        loaded_data = repo.load_data()
        
        assert len(loaded_data.tasks) == 2
        assert loaded_data.next_id == 3
        assert loaded_data.tasks[0].description == 'Desc 1'
        assert loaded_data.tasks[1].completed_at is not None
    
    def test_load_tasks_with_empty_file(self, temp_file, repo):
        """Handles empty JSON file gracefully."""
        temp_file.write_text('{}')
        
        task_data = repo.load_data()
        
        assert task_data.tasks == []
        assert task_data.next_id == 1