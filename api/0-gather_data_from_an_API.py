#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com/"


def do_requests():

    if len(sys.argv) < 2:
        print("Correcct usage ", __file__, "<employee_id>")

    e_id = sys.argv[1]

    response = requests.get(base_url + "users/" + e_id)

    if response.status_code == 404:
        return print("Error not found the requested link")
    if response.status_code != 200:
        return print("Error with code", response.status_code)

    user = response.json()

    response = requests.get(base_url + "todos/")
    if response.status_code == 404:
        return print("Error not found the requested link")
    if response.status_code != 200:
        return print("Error with code", response.status_code)

    todos = response.json()

    user_todo = []
    for todo in todos:
        if todo.get("userId") == user.get("id"):
            user_todo.append(todo)

    completed = [todo for todo in user_todo if todo.get("completed")]

    print(
        f"Employee {user.get('name')} is done with tasks "
        f"({len(completed)}/{len(user_todo)})"
    )

    for task in completed:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    do_requests()
