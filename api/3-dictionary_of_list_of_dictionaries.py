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

    for task in api_url_todos:
        new_dict = {"username": api_url_user['username'],
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": api_url_user['username']}
        user_tasks.append(new_dict)
    jsonfile[useriD]=new_dict

    with open(f'todo_all_employees.json', 'w') as file:
        json.dump(jsonfile, file)
