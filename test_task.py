import pytest
import datetime
from task import Task


def test_new_task_is_pending():
    task = Task(id=1, description="Test task")
    assert not task.is_complete()
    assert task.completed_at is None


def test_mark_completed():
    task = Task(id=1, description="Test task")
    
    result = task.mark_complete()
    
    assert result is True
    assert task.is_complete()
    assert task.completed_at is not None


def test_mark_completed_twice_returns_false():
    task = Task(id=1, description="Test task")
    task.mark_complete()
    
    result = task.mark_complete()
    
    assert result is False


def test_mark_pending():
    task = Task(id=1, description="Test task")
    task.mark_complete()
    
    result = task.mark_pending()
    
    assert result is True
    assert not task.is_complete()
    assert task.completed_at is None


def test_mark_pending_on_pending_task_returns_false():
    task = Task(id=1, description="Test task")
    
    result = task.mark_pending()
    
    assert result is False