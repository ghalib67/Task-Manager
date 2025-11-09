import os
import json
import datetime



def AddTask(task: str):
    file_path = "files/tasks.json"

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)
    
    with open(file_path, "r") as f:
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
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def updateTask(task_id: int,task: str):
    with open("Files/tasks.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for i in data:
        if i["id"] == task_id:
            i["description"] += f" {task}"
            i["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("Files/tasks.json", "w") as f:
                json.dump(data, f, indent=4)
                
            print(f"Task {task_id} updated successfully.")
            return
    print("could not find the task")

def markInProgress(task_id):
    with open("Files/tasks.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for i in data:
        if i["id"] == task_id:
            i["status"] += "In Progress"
            i["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("Files/tasks.json", "w") as f:
                json.dump(data, f, indent=4)
                
            print(f"Task {task_id} updated successfully.")
            return
    print("could not find the task")

def markDone(task_id):
    with open("Files/tasks.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for i in data:
        if i["id"] == task_id:
            i["status"] += "Done"
            i["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("Files/tasks.json", "w") as f:
                json.dump(data, f, indent=4)
                
            print(f"Task {task_id} updated successfully.")
            return
    print("could not find the task")

def AllTasks():
    with open("Files/tasks.json", "r") as f:
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
    with open("Files/tasks.json", "r") as f:
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
    with open("Files/tasks.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
            
    print("\n===== IN PROGRESS TASKS =====")
    for i in data:
        if i["status"] == "In progress":
            print(f"\nID: {i['id']}")
            print(f"Description: {i['description']}")
            print(f"Status: {i['status']}")
            print(f"Updated At: {i['updatedAt']}")
            print("-" * 30)

def notDone():
    with open("Files/tasks.json", "r") as f:
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



def deleteTask(task):
    with open("files/tasks.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for i in data:
        if i["id"] == task:
            data.remove(i)
            with open("files/tasks.json","w") as f:
                json.dump(data , f, indent=4)
            return
    
    print("Could not find the task!")
        
if __name__ == "__main__":
    command = 0
    while command != 3:
        try:
            command = int(input("Please input a command:\n1: Add, Update or Delete a task\n2: List Tasks\n3: Exit Task Manager\nInput "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        match command:
            case 1:
                cmd = int(input("Please input a command:\n1: Add a task\n2: update a task\n3: Delete a task\nInput: "))
                match cmd:
                    case 1:
                        AddTask(input("Input the description ofthe task you wish to add: "))
                    
                    case 2:
                        updateTask(int(input("Enter the id of the task you wish to update: ")))
                    
                    case 3:
                        deleteTask(int(input("Input the id of the task you wish to remove")))
            case 2:
                command = int(input("Please input a command:\n1: List all tasks\n2: List done Tasks\n3: List in progress tasks\n4: List all tasks that arent done\nInput: "))
                match command:
                    case 1:
                        AllTasks()
                    
                    case 2:
                        doneTasks()
                    
                    case 3:
                        inProgress()
                    
                    case 4:
                        notDone()


