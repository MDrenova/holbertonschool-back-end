#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format"""
import json
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com/"


def do_requests():

    response = requests.get(base_url + "users/")
    users = response.json()

    response = requests.get(base_url + "todos/")
    todos = response.json()

    user_tasks = {}
    for user in users:
        u_id = user["id"]
        user_list = []
        for todo in todos:
            if todo["userId"] == u_id:
                todo_info = {
                    "username": user["username"],
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
                user_list.append(todo_info)
        user_tasks[u_id] = user_list

    with open("todo_all_employees.json", 'w') as file:
        json.dump(user_tasks, file)


if __name__ == "__main__":
    do_requests()
