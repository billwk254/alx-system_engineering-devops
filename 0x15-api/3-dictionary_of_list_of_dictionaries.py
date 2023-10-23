#!/usr/bin/python3


"""
Exports users' tasks to a JSON file in the format:
{
  "USER_ID": [
    {
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS,
      "username": "USERNAME"
    },
    ...
  ],
  ...
}
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = argv[1]
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        try:
            user = user_response.json()
            todos = todo_response.json()

            username = user.get("username")
            user_id = user.get("id")

            task_list = [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                }
                for task in todos
            ]

            user_tasks = {str(user_id): task_list}

            with open("{}.json".format(employee_id), 'w') as json_file:
                json.dump(user_tasks, json_file)
        except ValueError:
            print("Not a valid JSON")
