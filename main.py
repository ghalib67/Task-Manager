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

def updateTask(task):
    with open("files/tasks.json","r") as f:
        data = json.load(f)

    for i in data:
        if i["id"] == task:
            progress = input("change the status to:\n1: Done \n2: In progress \n3: To-Do ")
            match progress:
                case "1":
                    i["status"] = "Done"
                case "2":
                    i["status"] = "In progress"
                case "3":
                    i["status"] = "To-Do"
                
            i["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("files/tasks.json", "w") as f:
                json.dump(data, f, indent=4)
            return
    print("could not find the task")
    
def AllTasks():
    with open("files/tasks.json","r") as f:
        data = json.load(f)
    
    for i in data:
        for key, value in i.items():
            print(f"{key}: {value}")

def doneTasks():
    with open("files/tasks.json","r") as f:
        data = json.load(f)
    
    for i in data:
        if i["status"] == "Done":
            for key, value in i.items():
                print(f"{key}: {value}")

def inProgress():
    with open("files/tasks.json","r") as f:
        data = json.load(f)
        
    for i in data:
        if i["status"] == "In progress":
            for key, value in i.items():
                print(f"{key}: {value}")  

def notDone():
    with open("files/tasks.json","r") as f:
        data = json.load(f)
        
    for i in data:
        if i["status"] != "Done":
            for key, value in i.items():
                print(f"{key}: {value}")      

def deleteTask(task):
    with open("files/tasks.json", "r") as f:
        data = json.load(f)

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
        command = int(input("Please input a command:\n1: Add, Update or Delete a task\n2: List Tasks\n3: Exit Task Manager\nInput "))
        match command:
            case 1:
                cmd = int(input("Please input a command:\n1: Add a task\n2: update a task\n3: Delete a task\nInput: "))
                match cmd:
                    case 1:
                        AddTask(input("Input the task you wish to add"))
                    
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


