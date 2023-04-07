#!/usr/bin/python3
"""
    program to gather data from a database (use REST API)
"""


import requests
from sys import argv


if __name__ == '__main__':
    """ to execute this program - entry point """

    # retrieve the database
    api_url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()

    unique_id = int(argv[1])

    # retrieve database of all users
    # the required first parameter of the 'get' method is the 'url'
    api_url_users = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{unique_id}").json()


    # I created all the variables that I need
    # Initialize variables to count
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    EMPLOYEE_NAME = api_url_users['name']

    # Loop to calculate the number of tasksto do and to do and tasks performed
    for key in api_url_todos:
        if key['userId'] == unique_id:
            # Count all tasks TO DO for the same user user/employee
            TOTAL_NUMBER_OF_TASKS += 1
            if key['completed']:
                # Count all tasks REALISED for the same user user/employee
                NUMBER_OF_DONE_TASKS += 1
    # Create the program : Here, just print sentence with retrieved variables
    print(f"Employee {EMPLOYEE_NAME} is done with "
          f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    # Loop that retrieves title of done tasks
    for data in api_url_todos:
        if data['completed'] and data['userId'] == unique_id:
            TASK_TITLE = data['title']
            print(f"\t {TASK_TITLE}")
