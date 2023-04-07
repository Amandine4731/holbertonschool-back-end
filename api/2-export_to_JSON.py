#!/usr/bin/python3
"""
    program to gather data from a database (use REST API)
"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    """ to execute this program - entry point """

    id = int(argv[1])
    # retrieve the database
    url_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/?userId={id}").json()
    # retrieve database of all users
    # the required first parameter of the 'get' method is the 'url'
    url_users = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}").json()

    USER_ID = url_users['id']
    list = []
    new_dict = {}

    for key in url_todos:
        if key['userId'] == id:
            new_dict = dict(task=key['title'],
                            completed=key['completed'],
                            username=url_users['username'])
            list.append(new_dict)
    json_file = {f"{USER_ID}": list}
    print(json_file)

    with open(f"{USER_ID}.json", 'w') as new_file:
        json.dump(json_file, new_file)
