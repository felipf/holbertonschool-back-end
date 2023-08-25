#!/usr/bin/python3
"""gather data from api"""
import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    response = requests.get(url)
    name = response.json().get('name')

    url = "https://jsonplaceholder.typicode.com/todos?userId=" + user_id
    response = requests.get(url)
    todos = response.json()
    completed = []
    for todo in todos:
        if todo.get('completed') is True:
            completed.append(todo.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(name,
          len(completed), len(todos)))
    for todo in completed:
        print("\t {}".format(todo))
