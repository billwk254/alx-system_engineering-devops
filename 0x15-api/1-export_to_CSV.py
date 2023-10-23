#!/usr/bin/python3


"""
Script to fetch and export an employee's tasks to a CSV file using a REST API.
"""


import requests
import csv
import sys


def get_employee_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_id = user_data['id']
    employee_name = user_data['username']

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Create a CSV file for the user
    csv_filename = f'{employee_id}.csv'

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_completed = "True" if task['completed'] else "False"
            csv_writer.writerow([employee_id, employee_name, task_completed, task['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
