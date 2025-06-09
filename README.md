# TuiDo

A simple, elegant terminal-based todo list manager built with Python. Keep track of your tasks without leaving the command line.

## Features

- ✅ Add, complete, and delete tasks
- 📋 List pending and completed tasks with timestamps
- 🔄 Mark completed tasks as pending again
- 💾 Persistent storage with JSON files
- 🎨 Beautiful terminal interface with Rich
- 📁 Support for multiple task files
- 🚀 Fast and lightweight

## Installation

### From Source (Recommended)

1. Clone or download this repository
2. Navigate to the project directory
3. Install using pip:

```bash
pip install .
```

For development installation (changes reflect immediately):
```bash
pip install -e .
```

### Prerequisites

- Python 3.7 or higher
- pip

Dependencies will be automatically installed:
- `rich` - for beautiful terminal output
- `humanize` - for human-readable timestamps

## Usage

Once installed, use the `tuido` command from anywhere in your terminal.

### Basic Commands

**Add a new task:**
```bash
tuido add "Buy groceries"
tuido add "Finish project report"
```

**List all tasks:**
```bash
tuido list
# or simply
tuido
```

**Complete a task:**
```bash
tuido do 1
```

**Mark a completed task as pending:**
```bash
tuido undo 2
```

**Delete a task:**
```bash
tuido delete 3
```

### Advanced Usage

**Use a custom task file:**
```bash
tuido --file work-tasks.json add "Review pull request"
tuido --file work-tasks.json list
```

**Verbose output:**
```bash
tuido --verbose list
```

**Get help:**
```bash
tuido --help
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
