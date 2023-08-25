#!/usr/bin/python3
"""gather data from api"""
from requests import get
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_ep = f"{base_url}/users/{user_id}"
    todos_ep = f"{base_url}/todos/?userId={user_id}"

    user_data = get(user_ep).json()
    user_name = user_data.get("name")
    todos_data = get(todos_ep).json()

    completed_tasks = []

    for task in todos_data:
        if task["completed"]:
            completed_tasks.append(task["title"])

    total_tasks = len(todos_data)
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {user_name} is done with tasks"
          f"({num_completed_tasks}/{total_tasks}):")

    for task_title in completed_tasks:
        print(f"\t {task_title}")
