#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    r = requests.get(url)
    name = r.json().get("name")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    r = requests.get(url)
    total = len(r.json())
    done = [task for task in r.json() if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(name, len(done), total))
    for task in done:
        print("\t {}".format(task.get("title")))
