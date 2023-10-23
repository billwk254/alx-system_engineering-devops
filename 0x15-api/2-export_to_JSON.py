#!/usr/bin/python3


"""
Script to fetch and export an employee's tasks to a JSON file using a REST API.
"""


import json
import requests
import sys


def get_employee_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_id = user_data['id']
    employee_name = user_data['username']

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Create a JSON file for the user
    json_filename = f'{employee_id}.json'
    user_tasks = {str(employee_id): []}

    for task in todos_data:
        task_completed = task['completed']
        user_tasks[str(employee_id)].append({"task": task['title'], "completed": task_completed, "username": employee_name})

    with open(json_filename, 'w') as json_file:
        json.dump(user_tasks, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
