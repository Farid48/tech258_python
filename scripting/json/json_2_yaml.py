import json
import os
import sys
import yaml


def load_json() -> dict:
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):  # Check if that second argument is actually a file name and if it exists
            file = open(sys.argv[1], "r")
            data = json.load(file)
            file.close()
            print("JSON IS VALID!")
            return data

        else:
            print(sys.argv[1] + "NOT FOUND")
    else:
        print("Usage: Python check_json.py <file>")


def create_yaml(data: dict):
    filename = sys.argv[1].split(".")[0]

    with open(f"{filename}.yaml", "w") as file:
        yaml.dump(data, file,default_flow_style=False, sort_keys=False)
        print(f"SUCCESSFULLY WRITTEN TO {filename}.yaml")


json_dict = load_json()
create_yaml(json_dict)
