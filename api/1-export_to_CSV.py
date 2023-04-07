#!/usr/bin/python3
"""
    program to gather data from a database (use REST API)
"""


import csv
import requests
from sys import argv


if __name__ == '__main__':
    """ to execute this program - entry point """

    unique_id = int(argv[1])
    # retrieve the database
    url_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/?userId={unique_id}").json()
    # retrieve database of all users
    # the required first parameter of the 'get' method is the 'url'
    url_users = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{unique_id}").json()

    USER_ID = url_users['id']

    with open(f"{USER_ID}.csv", 'wt') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for key in url_todos:
            if key['userId'] == unique_id:
                new_list = []
                new_list.append(USER_ID)
                new_list.append(url_users['username'])
                new_list.append(key['completed'])
                new_list.append(key['title'])
            writer.writerow(new_list)
        f.close()
