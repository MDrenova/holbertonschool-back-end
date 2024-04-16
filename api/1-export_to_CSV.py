#!/usr/bin/python3
"""Using what you did in the task #0
extend a python script to export data in the CSV format"""


import csv
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

    with open(f"{e_id}.csv", 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in u_todo:
            writer.writerow([todo["userId"], user["username"],
                             todo["completed"], todo["title"]])


if __name__ == "__main__":
    do_requests()
