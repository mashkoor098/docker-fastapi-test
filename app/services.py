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
            f.write('{"data": []}')  # Initialize the file with an empty array

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
        # Read existing user data
        users = read_usersdata()

        # Add the new user to the data
        if "data" in users:
            users["data"].append(user)  # Append new user to the existing list
        else:
            users["data"] = [user]  # If no users exist, initialize with a list

        # Write the updated data back to the JSON file
        with open(datasource, "w") as f:
            json.dump(users, f, indent=2)  # Dump the data with pretty formatting
        print("User data added successfully!")

    except Exception as e:
        print(f"Error adding user data: {e}")

