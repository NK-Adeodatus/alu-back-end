#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()  # Check for HTTP errors
        user_data = user_response.json()
        employee_name = user_data.get("name")  # Use .get()

        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}") # Filter tasks by userId
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        completed_tasks = [
            task for task in todos_data if task.get("completed")
        ]  # List comprehension for completed tasks
        num_completed = len(completed_tasks)
        total_tasks = len(todos_data)

        print(
            f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):"
        )

        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
        exit(1)
