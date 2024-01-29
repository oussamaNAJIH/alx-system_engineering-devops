#!/usr/bin/python3
import requests
import sys

# Check if the correct number of command-line arguments is provided
employee_id = int(sys.argv[1])
# Fetch employee data that means his name
users_url = "https://jsonplaceholder.typicode.com/users"
params1 = {"id": employee_id}
employee_data = requests.get(users_url, params=params1)
employee_data_json = employee_data.json()
if isinstance(employee_data_json, list):
    employee_data_json = employee_data_json[0]
EMPLOYEE_NAME = employee_data_json.get("name")

# Fetch employee's TODO list that means his NUMBER_OF_DONE_TASKS
# and TOTAL_NUMBER_OF_TASKS
todos_url = "https://jsonplaceholder.typicode.com/todos"
params2 = {"userId": employee_id}
NUMBER_OF_DONE_TASKS = 0
list_titles = []
todo_data = requests.get(todos_url, params=params2).json()
for key in todo_data:
    if key.get("completed"):
        NUMBER_OF_DONE_TASKS += 1
        list_titles.append(key.get("title"))

TOTAL_NUMBER_OF_TASKS = len(todo_data)
print(f"Employee {EMPLOYEE_NAME} is done with tasks "
      f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
for title in list_titles:
    print(f"\t{title}")
