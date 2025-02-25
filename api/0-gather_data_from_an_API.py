#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
"""
import requests


USER_URL = 'https://jsonplaceholder.typicode.com/users'
TODO_URL = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(USER_URL)

def extract_data(user_id):
    employee = requests.get(f"{USER_URL}/{user_id}")
    employee_todos = requests.get(f"{TODO_URLT}?userId=T{user_id}")
    completed_tasks = []
    employee_name = employee["name"]

    for todo in employee_todos:
        if todo["completed"]:
            completed_tasks.append(todo)

    print(f"Employee {employee_name} is done with task({len(completed_tasks)} {len(employee_name)})")
