"""TuiDo - Terminal-based Todo List Manager CLI Interface."""
import sys

import humanize
from rich.console import Console
from rich.panel import Panel

from tuido.argument_parser import DEFAULT_TASK_FILE, ArgumentParser
from tuido.json_task_repository import JsonTaskRepository
from tuido.task_manager import TaskManager


class TaskCLI:
    """Command-line interface for managing tasks in TuiDo."""
    def __init__(self, console: Console = None):
        self.parser = ArgumentParser(
            prog_name="TuiDo", description="A terminal-based todo list manager"
        )
        self.console = console or Console()

    def _initialize_task_manager(self, file_path: str) -> TaskManager:
        repository = JsonTaskRepository(file_path)
        return TaskManager(repository)

    def run(self, args=None):
        """Parse arguments and execute the appropriate command."""
        parsed_args = self.parser.parse_args(args)
        task_manager = self._initialize_task_manager(parsed_args.file)

        if parsed_args.verbose or parsed_args.file != DEFAULT_TASK_FILE:
            self.console.print(
                Panel(
                    f":file_folder: Using task file: [cyan]{parsed_args.file}[/cyan]",
                    border_style="cyan",
                )
            )
            self.console.print()

        if not parsed_args.command or parsed_args.command == "list":
            self._handle_list(task_manager)
        elif parsed_args.command == "add":
            self._handle_add(task_manager, parsed_args.description)
        elif parsed_args.command == "do":
            self._handle_do(task_manager, parsed_args.task_id)
        elif parsed_args.command == "undo":
            self._handle_undo(task_manager, parsed_args.task_id)
        elif parsed_args.command == "delete":
            self._handle_delete(task_manager, parsed_args.task_id)
        else:
            self.parser.parser.print_help()

        return 0

    def _handle_add(self, task_manager: TaskManager, description: str):
        description = description.strip()

        if not description:
            self.console.print("Error: Task description cannot be empty.")
            sys.exit(1)

        new_task = task_manager.add_task(description)
        self.console.print(
            f"[bold green]✓[/bold green] Added task {new_task.id}: '{new_task.description}'"
        )

    def _handle_list(self, task_manager: TaskManager):
        tasks = task_manager.all_tasks()

        # Separate tasks
        completed_tasks = [task for task in tasks if task.completed_at]
        pending_tasks = [task for task in tasks if not task.completed_at]

        if pending_tasks:
            self.console.print(f"[yellow]PENDING TASKS ({len(pending_tasks)})[/yellow]")
            for task in pending_tasks:
                self.console.print(
                    f"  {task.id}: {task.description} [dim](added {humanize.naturaltime(task.created_at)})[/dim]",
                    highlight=False,
                )

        if completed_tasks:
            self.console.print(
                f"[green]COMPLETED TASKS ({len(completed_tasks)})[/green]"
            )
            for task in completed_tasks:
                self.console.print(
                    f"  {task.id}: {task.description} [dim](completed {humanize.naturaltime(task.completed_at)})[/dim]",
                    highlight=False,
                )

        if not tasks:
            self.console.print(
                "[dim]No tasks found. Use 'add' command to create a new task.[/dim]"
            )

    def _handle_do(self, task_manager: TaskManager, task_id: int):
        if task_manager.set_task_complete(task_id):
            self.console.print(
                f"[bold green]✓[/bold green] Task {task_id} marked as complete."
            )
        else:
            self.console.print(f"⚠️  Task {task_id} not found or already complete.")
            sys.exit(1)

    def _handle_undo(self, task_manager: TaskManager, task_id: int):
        if task_manager.set_task_pending(task_id):
            self.console.print(
                f"[bold green]✓[/bold green] Task {task_id} marked pending."
            )
        else:
            self.console.print(f"⚠️  Task {task_id} not found or already pending.")
            sys.exit(1)

    def _handle_delete(self, task_manager: TaskManager, task_id: int):
        task = task_manager.delete_task(task_id)
        if task is not None:
            self.console.print(
                f"[bold green]✓[/bold green] Deleted task {task.id}: '{task.description}'."
            )
        else:
            self.console.print(f"⚠️  Task {task_id} not found.")
            sys.exit(1)
