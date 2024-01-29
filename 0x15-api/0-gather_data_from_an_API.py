#!/usr/bin/python3
"""
A Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        # Check if the correct number of command-line arguments is provided
        if len(argv) != 2:
            print("Usage: script.py <employee_id>")
            exit(1)

        employee_id = argv[1]
        todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

        with requests.Session() as sessionReq:
            employee_data = sessionReq.get(employee_url)
            todos_data = sessionReq.get(todos_url)

            employee_name = employee_data.json().get('name')
            todos_json = todos_data.json()

            NUMBER_OF_DONE_TASKS = sum(1 for task in todos_json if task['completed'])

            print(f"Employee {employee_name} is done with tasks({NUMBER_OF_DONE_TASKS}/{len(todos_json)}):")

            for task in todos_json:
                if task['completed']:
                    print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        exit(1)
