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
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated at" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    data.append(new_task)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    AddTask("eat")
