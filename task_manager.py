import os
import json
import datetime
import sys

FILE_PATH = "tasks.json"

def ensure_file():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

def AddTask(task: str):
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    id_num = data[-1]["id"] + 1 if data else 1
    new_task = {
        "id": id_num,
        "description": task,
        "status": "To-Do",
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(new_task)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def updateTask(task_id: int, task: str):
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for i in data:
        if i["id"] == task_id:
            i["description"] += f" {task}"
            i["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(FILE_PATH, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Task {task_id} updated successfully.")
            return
    print("could not find the task")

def markInProgress(task_id):
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for i in data:
        if i["id"] == task_id:
            i["status"] = "In Progress"
            i["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(FILE_PATH, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Task {task_id} updated successfully.")
            return
    print("could not find the task")

def markDone(task_id):
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for i in data:
        if i["id"] == task_id:
            i["status"] = "Done"
            i["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(FILE_PATH, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Task {task_id} updated successfully.")
            return
    print("could not find the task")

def AllTasks():
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    print("\n===== ALL TASKS =====")
    for i in data:
        print(f"\nID: {i['id']}")
        print(f"Description: {i['description']}")
        print(f"Status: {i['status']}")
        print(f"Created At: {i['createdAt']}")
        print(f"Updated At: {i['updatedAt']}")
        print("-" * 30)

def doneTasks():
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    print("\n===== DONE TASKS =====")
    for i in data:
        if i["status"] == "Done":
            print(f"\nID: {i['id']}")
            print(f"Description: {i['description']}")
            print(f"Status: {i['status']}")
            print(f"Updated At: {i['updatedAt']}")
            print("-" * 30)

def inProgress():
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    print("\n===== IN PROGRESS TASKS =====")
    for i in data:
        if i["status"] == "In Progress":
            print(f"\nID: {i['id']}")
            print(f"Description: {i['description']}")
            print(f"Status: {i['status']}")
            print(f"Updated At: {i['updatedAt']}")
            print("-" * 30)

def notDone():
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    print("\n===== NOT DONE TASKS =====")
    for i in data:
        if i["status"] != "Done":
            print(f"\nID: {i['id']}")
            print(f"Description: {i['description']}")
            print(f"Status: {i['status']}")
            print(f"Updated At: {i['updatedAt']}")
            print("-" * 30)

def deleteTask(task_id):
    ensure_file()
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for i in data:
        if i["id"] == task_id:
            data.remove(i)
            with open(FILE_PATH, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Task {task_id} deleted successfully.")
            return
    print("Could not find the task!")

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Usage:")
        print("  python task.py add <description>")
        print("  python task.py update <id> <appending text>")
        print("  python task.py delete <id>")
        print("  python task.py mark-done <id>")
        print("  python task.py mark-in-progress <id>")
        print("  python task.py list [all|done|progress|todo]")
        sys.exit()

    command = args[1].lower()
    match command:
        case "add":
            if len(args) < 3:
                print("Please provide a task description.")
            else:
                AddTask(" ".join(args[2:]))

        case "update":
            if len(args) < 4:
                print("Please provide task id and task description.")                
            else:
                updateTask(int(args[2]), " ".join(args[3:]))

        case "delete":
            if len(args) < 3:
                print("Please provide a task id.")
            else:
                deleteTask(int(args[2]))

        case "mark-done":
            if len(args) < 3:
                print("Please provide a task id.")
            else:
                markDone(int(args[2]))

        case "mark-in-progress":
            if len(args) < 3:
                print("Please provide a task id.")
            else:
                markInProgress(int(args[2]))

        case "list":
            if len(args) < 3:
                AllTasks()
            else:
                sub = args[2].lower()
                if sub == "all":
                    AllTasks()
                elif sub == "done":
                    doneTasks()
                elif sub == "progress":
                    inProgress()
                elif sub == "todo":
                    notDone()
                else:
                    print("Unknown list type. Use: all, done, progress, or todo.")

        case _:
            print("Unknown command.")
