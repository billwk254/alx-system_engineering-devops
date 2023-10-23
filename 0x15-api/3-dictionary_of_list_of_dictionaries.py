#!/usr/bin/python3

"""
Script to fetch and display an employee's TODO list progress using a REST API.
"""

import json
import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Fetch and display the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['username']

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Create a dictionary to store the user's tasks
    user_tasks = {"username": employee_name, "tasks": []}
    
    for task in todos_data:
        user_tasks["tasks"].append({
            "task": task['title'],
            "completed": task['completed']
        })

    return user_tasks

def export_todo_data():
    """
    Fetch TODO list data for all employees and export to JSON file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    all_employees_tasks = {}
    
    for employee_id in range(1, 11):  # Assuming you have employees with IDs from 1 to 10
        user_tasks = get_employee_todo_list(employee_id)
        all_employees_tasks[str(employee_id)] = user_tasks

    # Save the data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

if __name__ == "__main__":
    export_todo_data()
