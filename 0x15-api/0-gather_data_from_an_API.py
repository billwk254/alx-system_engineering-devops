#!/usr/bin/python3


"""
Script to fetch and display an employee's TODO list progress using a REST API.
"""


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
    employee_name = user_data['name']

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task['completed'])

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
