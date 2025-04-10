import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
datafolder = os.path.join(BASE_DIR, "data")
datasource = os.path.join(datafolder, "users.json")

def check_dataset_exists():
    if not os.path.exists(datafolder):
        os.mkdir(datafolder)
    if not os.path.exists(datasource):
        with open(datasource, "w") as f:
            f.write('{"data": []}') 

def read_usersdata():
    check_dataset_exists()
    with open(datasource, "r") as f:
        content = f.read()
        if content == "":
            content = '{"data": []}'
        users = json.loads(content)
    return users
def add_userdata(user: dict):
    try:
       
        users = read_usersdata()

     
        if "data" in users:
            users["data"].append(user) 
        else:
            users["data"] = [user] 


        with open(datasource, "w") as f:
            json.dump(users, f, indent=2)  
        print("User data added successfully!")

    except Exception as e:
        print(f"Error adding user data: {e}")

