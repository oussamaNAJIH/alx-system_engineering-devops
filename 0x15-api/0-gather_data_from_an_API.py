#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    try:
        # Check if the correct number of command-line arguments is provided
        if len(sys.argv) != 2:
            print("Usage: script.py <employee_id>")
            sys.exit(1)

        # Convert the employee ID to an integer
        employee_id = int(sys.argv[1])

        # Fetch employee data (name)
        users_url = "https://jsonplaceholder.typicode.com/users"
        params1 = {"id": employee_id}
        employee_data = requests.get(users_url, params=params1)
        employee_data.raise_for_status()  # Check if the request was successful
        employee_data_json = employee_data.json()

        if isinstance(employee_data_json, list):
            employee_data_json = employee_data_json[0]
        EMPLOYEE_NAME = employee_data_json.get("name")

        # Fetch employee's TODO list
        todos_url = "https://jsonplaceholder.typicode.com/todos"
        params2 = {"userId": employee_id}
        NUMBER_OF_DONE_TASKS = 0
        list_titles = []
        todo_data = requests.get(todos_url, params=params2)
        todo_data.raise_for_status()  # Check if the request was successful
        todo_data_json = todo_data.json()

        for key in todo_data_json:
            if key.get("completed"):
                NUMBER_OF_DONE_TASKS += 1
                list_titles.append(key.get("title"))

        TOTAL_NUMBER_OF_TASKS = len(todo_data_json)
        print(f"Employee {EMPLOYEE_NAME} is done with tasks "
              f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for title in list_titles:
            print(f"\t{title}")

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        sys.exit(1)
