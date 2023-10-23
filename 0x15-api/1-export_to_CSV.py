#!/usr/bin/python3
"""
Python script that exports user data in CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    tasks_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        tasks_response = requests.get(tasks_url)
        user_data = user_response.json()
        tasks_data = tasks_response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    if 'id' not in user_data:
        print(f"No user found for ID {employee_id}")
        sys.exit(1)

    user_id = user_data['id']
    username = user_data['username']
    csv_filename = f'{user_id}.csv'

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in tasks_data:
            task_id = task['id']
            task_title = task['title']
            task_completed = task['completed']
            csv_writer.writerow([user_id, username, task_completed, task_title])

    print(f"Data exported to {csv_filename}")
