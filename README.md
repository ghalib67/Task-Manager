# Task-Manager
# Task Manager CLI

A command-line task manager written in Python that allows you to manage tasks directly from the terminal. Tasks are stored in a local JSON file.

## Features

- Add, update, and delete tasks.
- Mark tasks as **In Progress** or **Done**.
- List all tasks or filter by status: all, done, in progress, or not done.
- Automatically creates a `tasks.json` file if it does not exist.
- Simple and lightweight command-line interface.

## Installation

1. Ensure you have Python 3 installed.
2. Clone this repository or download the `task.py` file.
3. Make sure the file `tasks.json` is in the same directory as `task.py` (the script will create it if missing).

## Usage

Run commands from your terminal:

### Add a Task
```bash
    python task_manager.py add "Task description"
```
### Update a task
```bash
    python task.py update <id> "Text to append to the task"
```
### Delete a Task
```bash
    python task.py delete <id>
```
### Mark as done
```bash
    python task.py mark-done <id>
```
### Mark a Task as In Progress
```bash
    python task.py mark-in-progress <id>
```
### List Tasks
```bash
    python task.py list              # Lists all tasks
    python task.py list all          # Lists all tasks
    python task.py list done         # Lists tasks marked as Done
    python task.py list progress     # Lists tasks marked as In Progress
    python task.py list todo         # Lists tasks that are not done

```
## File structure
task.py – Main Python script for the task manager.

tasks.json – JSON file where all tasks are stored (created automatically).

### Notes
Task IDs are automatically incremented.

All timestamps are in YYYY-MM-DD HH:MM:SS format.






for more info:https://roadmap.sh/projects/task-tracker
