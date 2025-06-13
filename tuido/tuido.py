"""TUIDO - Task Utility Interface for Daily Operations"""

import sys

from tuido.task_cli import TaskCLI


def main():
    """
    Main entry point for the TUIDO application."""
    cli = TaskCLI()
    return cli.run()


if __name__ == "__main__":
    sys.exit(main())
