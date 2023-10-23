#!/usr/bin/python3


"""
This script fetches data from an API, organizes it into a specific format, and saves it as a JSON file.
"""


import json
import requests
from sys import argv


def fetch_and_organize_tasks():
    """
    Fetch data from the API, organize it into the required format, and save it as a JSON file.
    """
    if len(argv) == 1 or not argv[1].isdigit():
        exit()

    user_id = argv[1]

    users_url = 'https://jsonplaceholder.typicode.com/users'
    tasks_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url)
    tasks_response = requests.get(tasks_url)

    if users_response.status_code != 200 or tasks_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        exit()

    users = users_response.json()
    tasks = tasks_response.json()

    user_tasks = {}
    for user in users:
        user_id = str(user['id'])
        user_tasks[user_id] = []

    for task in tasks:
        task_data = {
            "username": next(user['username'] for user in users if user['id'] == task['userId']),
            "task": task['title'],
            "completed": task['completed']
        }
        user_tasks[str(task['userId'])].append(task_data)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file)

if __name__ == "__main__":
    fetch_and_organize_tasks()
