import pytest
import os
from unittest.mock import patch
from argument_parser import ArgumentParser, DEFAULT_TASK_FILE


class TestArgumentParser:
    """Test the ArgumentParser configuration and setup."""
    
    def test_default_file_uses_environment_variable(self):
        """Test that TODO_FILE environment variable is respected."""
        with patch.dict(os.environ, {'TODO_FILE': '/custom/path/tasks.json'}):
            parser = ArgumentParser()
            args = parser.parse_args(['list'])
            assert args.file == '/custom/path/tasks.json'
    
    def test_default_file_fallback(self):
        """Test that it falls back to DEFAULT_TASK_FILE when env var not set."""
        with patch.dict(os.environ, {}, clear=True):
            parser = ArgumentParser()
            args = parser.parse_args(['list'])
            assert args.file == DEFAULT_TASK_FILE
    
    def test_all_subcommands_are_registered(self):
        """Test that all expected subcommands are registered."""
        parser = ArgumentParser()
        expected_commands = ['add', 'list', 'do', 'undo', 'delete']
        
        # Get the subparsers from the parser
        subparsers_actions = [
            action for action in parser.parser._actions 
            if hasattr(action, 'choices') and action.dest == 'command'
        ]
        
        assert len(subparsers_actions) == 1
        actual_commands = list(subparsers_actions[0].choices.keys())
        
        for command in expected_commands:
            assert command in actual_commands
    
    def test_required_arguments_are_configured(self):
        """Test that required arguments are properly configured for each command."""
        parser = ArgumentParser()
        
        # Test 'add' requires description
        args = parser.parse_args(['add', 'Test task'])
        assert args.command == 'add'
        assert args.description == 'Test task'
        
        # Test 'do' requires task_id and parses as int
        args = parser.parse_args(['do', '5'])
        assert args.command == 'do'
        assert args.task_id == 5
        assert isinstance(args.task_id, int)
        
        # Test 'undo' requires task_id
        args = parser.parse_args(['undo', '3'])
        assert args.command == 'undo'
        assert args.task_id == 3
        
        # Test 'delete' requires task_id  
        args = parser.parse_args(['delete', '7'])
        assert args.command == 'delete'
        assert args.task_id == 7
        
        # Test 'list' requires no additional arguments
        args = parser.parse_args(['list'])
        assert args.command == 'list'