#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    all_data_json = requests.get(url).json()
    all_records = {}

    for user in all_data_json:
        employee_id = user.get("id")
        user_name = user.get("username")
        todos_url = "https://jsonplaceholder.typicode.com/todos"
        params = {"userId": employee_id}
        todo_data = requests.get(todos_url, params=params).json()
        list_tasks = []
        for task in todo_data:
            task_dict = {
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            list_tasks.append(task_dict)

        all_records[employee_id] = list_tasks

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_records, file)
