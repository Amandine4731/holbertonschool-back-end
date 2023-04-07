#!/usr/bin/python3
"""
    program to gather data from a database (use REST API)
"""


import csv
import requests
from sys import argv


if __name__ == '__main__':
    """ to execute this program - entry point """

    # retrieve the database
    api_url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()

    USER_ID = int(argv[1])

    # retrieve database of all users
    # the required first parameter of the 'get' method is the 'url'
    api_url_users = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{USER_ID}").json()

    with open(f"{USER_ID}.csv", 'wt') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for key in api_url_todos:
            new_list = []
            new_list.append(key['userId'])
            new_list.append(api_url_users['username'])
            new_list.append(key['completed'])
            new_list.append(key['title'])

            writer.writerow(new_list)
        f.close()
