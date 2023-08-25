#!/usr/bin/python3
"""export data in the JSON format"""
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    """export data in the JSON format"""
    user_id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{user_id}"
    todos_endpoint = f"{base_url}/todos/?userId={user_id}"

    user_data = get(user_endpoint).json()
    user_name = user_data.get("username")
    todos_data = get(todos_endpoint).json()

    json_data = {
        str(user_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name
            }
            for task in todos_data
        ]
    }

    filename = f"{user_id}.json"
    with open(filename, mode="w") as json_file:
        dump(json_data, json_file)
