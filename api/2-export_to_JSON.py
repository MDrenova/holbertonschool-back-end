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
    tasks = []
    for todo in u_todo:
        todo_info = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"],
            }
        tasks.append(todo_info)

    with open(f"{e_id}.json", 'w') as file:
        json.dump({e_id: tasks}, file)


if __name__ == "__main__":
    do_requests()
