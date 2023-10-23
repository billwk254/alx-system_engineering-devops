#!/usr/bin/python3
"""
Python script that exports user data in CSV format.
"""

import csv
import requests
import sys

def export_user_data(user_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    with open(f"{user_id}_todos.csv", mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["User ID", "Username", "Completed", "Title"])

        for todo in todos_data:
            csv_writer.writerow([user_id, user_data["username"], todo["completed"], todo["title"]])

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_user_data(user_id)
