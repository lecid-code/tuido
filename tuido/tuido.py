import sys
from tuido.task_cli import TaskCLI

def main():
    cli = TaskCLI()
    return cli.run()

if __name__ == '__main__':
    sys.exit(main())