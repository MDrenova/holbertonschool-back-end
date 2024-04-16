#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format"""

import json
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com/"


def do_requests():
    e_id = sys.argv[1]

    response = requests.get(base_url + "users/" + e_id)
    user = response.json()

    response = requests.get(base_url + "todos/")
    todos = response.json()

    u_todo = [todo for todo in todos if todo.get("userId") == user.get("id")]

    completed = [todo for todo in u_todo if todo.get("completed")]

    user_tasks = {}
    for _ in user:
        u_id = user["id"]
        user_tasks[u_id] = []
        for todo in todos:
            if todo["userId"] == u_id:
                todo_info = {
                    "username": user["username"],
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                user_tasks[u_id].append(todo_info)

    with open("todo_all_employees.json", 'w') as file:
        json.dump(user_tasks, file)


if __name__ == "__main__":
    do_requests()
