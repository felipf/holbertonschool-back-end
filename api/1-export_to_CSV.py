#!/usr/bin/python3
"""export data in the CSV format"""
from csv import writer, QUOTE_ALL
from requests import get
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_ep = f"{base_url}/users/{user_id}"
    todo_ep = f"{base_url}/todos/?userId={user_id}"

    user_data = get(user_ep).json()
    user_name = user_data.get("username")
    todo_data = get(todo_ep).json()

    with open(f"{user_id}.csv", "w") as csv_file:
        csv_writer = writer(csv_file, quoting=QUOTE_ALL)
        for task in todo_data:
            csv_writer.writerow([user_id, user_name,
                                 task["completed"], task["title"]])
