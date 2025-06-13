"""Unit tests for the Task class in the tuido module."""

from tuido.task import Task


def test_new_task_is_pending():
    """Test that a new task is created in a pending state."""
    task = Task(id=1, description="Test task")
    assert not task.is_complete()
    assert task.completed_at is None


def test_mark_completed():
    """Test marking a task as complete."""
    task = Task(id=1, description="Test task")

    result = task.mark_complete()

    assert result is True
    assert task.is_complete()
    assert task.completed_at is not None


def test_mark_completed_twice_returns_false():
    """Test that marking a task as complete twice returns False."""
    task = Task(id=1, description="Test task")
    task.mark_complete()

    result = task.mark_complete()

    assert result is False


def test_mark_pending():
    """Test marking a task as pending."""
    task = Task(id=1, description="Test task")
    task.mark_complete()

    result = task.mark_pending()

    assert result is True
    assert not task.is_complete()
    assert task.completed_at is None


def test_mark_pending_on_pending_task_returns_false():
    """Test that marking a pending task as pending returns False."""
    task = Task(id=1, description="Test task")

    result = task.mark_pending()

    assert result is False
