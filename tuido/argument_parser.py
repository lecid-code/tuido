"""Provides a command-line argument parser for the TuiDo todo list manager."""

import argparse
import os
from typing import List, Optional

DEFAULT_TASK_FILE = "~/.tasks.json"


class ArgumentParser:
    """A wrapper around argparse for TuiDo todo list manager."""

    def __init__(
        self, prog_name: Optional[str] = None, description: Optional[str] = None
    ):
        """
        Initialize the ArgumentParser.

        Args:
            prog_name: Program name (useful for testing)
            description: Program description
        """
        self.parser = argparse.ArgumentParser(
            prog=prog_name,
            description=description
            or f"{prog_name} - A terminal-based todo list manager",
        )
        self._setup_arguments()

    def _setup_arguments(self) -> None:
        """Set up all command-line arguments and subcommands."""
        self._add_global_arguments()
        self._add_subcommands()

    def _add_global_arguments(self) -> None:
        """Add global arguments that apply to all commands."""
        default_file = os.getenv("TODO_FILE", DEFAULT_TASK_FILE)
        self.parser.add_argument(
            "--file", "-f", type=str, default=default_file, help="Task file to use"
        )

        self.parser.add_argument(
            "--verbose", "-v", action="store_true", help="Enable verbose output"
        )

    def _add_subcommands(self) -> None:
        """Add all subcommands and their arguments."""
        subparsers = self.parser.add_subparsers(
            title="commands", dest="command", help="Available commands"
        )

        self._add_add_command(subparsers)
        self._add_list_command(subparsers)
        self._add_complete_command(subparsers)
        self._add_undo_command(subparsers)
        self._add_delete_command(subparsers)

    def _add_add_command(self, subparsers) -> None:
        """Add the 'add' subcommand."""
        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("description", help="Task description")

    def _add_list_command(self, subparsers) -> None:
        """Add the 'list' subcommand."""
        subparsers.add_parser("list", help="List all tasks")

    def _add_complete_command(self, subparsers) -> None:
        """Add the 'do' subcommand."""
        complete_parser = subparsers.add_parser("do", help="Mark a task as complete")
        complete_parser.add_argument(
            "task_id", help="ID of the task to complete", type=int
        )

    def _add_undo_command(self, subparsers) -> None:
        """Add the 'undo' subcommand."""
        undo_parser = subparsers.add_parser(
            "undo", help="Mark a previously completed task as active"
        )

        undo_parser.add_argument("task_id", help="ID of the task to revert", type=int)

    def _add_delete_command(self, subparsers) -> None:
        """Add the 'delete' subcommand."""
        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("task_id", help="ID of the task to delete", type=int)

    def parse_args(self, args: Optional[List[str]] = None) -> argparse.Namespace:
        """
        Parse command-line arguments.

        Args:
            args: List of arguments to parse (defaults to sys.argv)

        Returns:
            Parsed arguments namespace
        """
        return self.parser.parse_args(args)
