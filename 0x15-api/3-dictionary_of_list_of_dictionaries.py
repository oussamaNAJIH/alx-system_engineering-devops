#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    all_data_json = requests.get(url).json()
    all_records = []
    # Check if the correct number of command-line arguments is provided
    for key in all_data_json:

        employee_id = key.get("id")
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

        data_to_write = {}
        list_tasks = []
        for key in todo_data:
            if key.get("userId") == employee_id:
                dict = {}
                dict["username"] = user_name
                dict["task"] = key.get("title")
                dict["completed"] = key.get("completed")
            list_tasks.append(dict)
        data_to_write[employee_id] = list_tasks
        all_records.append(data_to_write)
    with open("todo_all_employees.json", "a") as file:
        json.dump(all_records, file)
