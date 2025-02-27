#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
"""
import requests


USER_URL = 'https://jsonplaceholder.typicode.com/users'
TODO_URL = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(USER_URL)


def extract_data(user_id):
    employee = requests.get(f"{USER_URL}/{user_id}").json()
    employee_todos = requests.get(f"{TODO_URL}?userId={user_id}").json()

    completed_tasks = []
    employee_name = employee["name"]

    for todo in employee_todos:
        if todo["completed"]:
            completed_tasks.append(todo)

    done_tasks = len(employee_todos)
    print(done_tasks)
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          len(completed_tasks),
                                                          done_tasks))
