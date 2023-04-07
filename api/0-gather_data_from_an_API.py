#!/usr/bin/python3
"""
    program to gather data from a database (use REST API)
"""

import requests
from sys import argv


if __name__ == '__main__':
    """ to execute this program - entry point """

    unique_id = int(argv[1])

    # retrieve all databases
    # the required first parameter of the 'get' method is the 'url'
    api_url_users = requests.get(f"https://jsonplaceholder.typicode.com/users/{unique_id}").json()

    api_url_todos = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # I created all the variables that I need
    # Initialize variables to count
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    EMPLOYEE_NAME = api_url_users['name']

    # Loop that calculates the number of tasks to do and tasks performed by the same user/employee
    for data in api_url_todos:
        if data['userId'] == unique_id:
            TOTAL_NUMBER_OF_TASKS += 1 # Count all tasks TO DO for the same user user/employee
            if data['completed']:
                NUMBER_OF_DONE_TASKS += 1 # Count all tasks REALISED for the same user user/employee
    # Create the program : Here, just print sentence with retrieved variables
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    # Loop that retrieves title of done tasks
    for data in api_url_todos:
        if data['completed'] and data['userId'] == unique_id:
            TASK_TITLE = data['title']
            print(f"\t {TASK_TITLE}")
