#!/usr/bin/python3
"""export data in the CSV format"""
import requests
import json
import csv
from sys import argv

user_id = None

try:
    user_id = argv[1]
except Exception as e:
    pass

todos_requests = requests.get(f"https://jsonplaceholder"
                              f".typicode.com/users/{user_id}/todos")
user_request = requests.get(f"https://jsonplaceholder"
                            f".typicode.com/users/{user_id}")
dicted_user = json.loads(user_request.text)
dicted_todos = json.loads(todos_requests.text)
completed_tasks = []
for x in dicted_todos:
    completed_tasks.append(x)

if __name__ == "__main__":
    """only execute the code when is main"""
    with open(f"{user_id}.csv", mode="w") as f:
        for values in dicted_todos:
            f.write(f'"{user_id}",')
            f.write(f'"{dicted_user.get("username")}",')
            f.write(f'"{values.get("completed")}",')
            f.write(f'"{values.get("title")}"')
            f.write('\n')
