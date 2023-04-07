#!/usr/bin/python3
"""
    program to gather data from a database (use REST API)
"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    """ to execute this program - entry point """

    id_user = int(argv[1])

    api_url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()

    api_url_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id_user}").json()

    user_tasks = []

    for task in api_url_todos:
        if task['userId'] == id_user:
            new_dict = {"username": api_url_user['username'],
                        "task": task['title'],
                        "completed": task['completed'],
                        "username": api_url_user['username']}
            user_tasks.append(new_dict)

    with open(f'{id_user}.json', 'w') as file:
        json.dump({str(id_user): user_tasks}, file)
