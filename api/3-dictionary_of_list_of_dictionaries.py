#!/usr/bin/python3
"""
    program to gather data from a database (use REST API)
"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    """ to execute this program - entry point """

    api_url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()

    api_url_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/").json()

    user_tasks = []
    jsonfile = {}

    for all_user in api_url_user:
        USER_ID = all_user['id']
        USERNAME = all_user['username']
        user_tasks = []
        for task in api_url_todos:
            if task['userId'] == USER_ID:
                new_dict = {"username": USERNAME,
                            "task": task['title'],
                            "completed": task['completed']}
                user_tasks.append(new_dict)
        jsonfile[USER_ID] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(jsonfile, file)
