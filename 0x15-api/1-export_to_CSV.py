#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    employee_id = int(sys.argv[1])
    # Fetch employee data that means his name
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_data = requests.get(users_url)
    employee_data_json = employee_data.json()
    EMPLOYEE_NAME = employee_data_json.get("name")
    user_name = employee_data_json.get("username")

    # Fetch employee's TODO list that means his NUMBER_OF_DONE_TASKS
    # and TOTAL_NUMBER_OF_TASKS
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": employee_id}
    NUMBER_OF_DONE_TASKS = 0
    list_titles = []
    todo_data = requests.get(todos_url, params=params).json()
    for key in todo_data:
        if key.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            list_titles.append(key.get("title"))

    TOTAL_NUMBER_OF_TASKS = len(todo_data)
    with open(f"{employee_id}.csv", "a") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for key in todo_data:
            status = key.get("completed")
            title = key.get("title")
            data_to_append = [employee_id,
                              user_name, status, title]
            csv_writer.writerow(data_to_append)
