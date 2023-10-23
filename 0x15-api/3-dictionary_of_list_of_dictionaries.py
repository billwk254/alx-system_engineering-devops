#!/usr/bin/python3


"""
Exports data in JSON format.
"""


import json
import requests


if __name__ == "__main":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(user_url).json()

    data = {}

    for user in users:
        user_id = user.get("id")
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
        todos = requests.get(todo_url).json()

        tasks = []
        for todo in todos:
            tasks.append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            })
        data[str(user_id)] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file, sort_keys=True)
