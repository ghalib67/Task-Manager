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
        "status": "to do",
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    data.append(new_task)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def updateTask(task):
    with open("files/tasks.json","r") as f:
        data = json.load(f)
    if isinstance(task, str):
        for i in data:
            if i["description"] == task:
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
    
    if isinstance(task, int):
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
    
def listAllTasks():
    with open("files/tasks.json","r") as f:
        data = json.load(f)
    
    for i in data:
        for key, value in i.items():
            print(f"{key}: {value}")
    
if __name__ == "__main__":
    AddTask("Buy groceries")
    AddTask("Wash the car")
    AddTask("Do homework")
    updateTask("Wash the car")
    listAllTasks()


