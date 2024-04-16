#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys
import csv

base_url = "https://jsonplaceholder.typicode.com/"


def do_requests():
    e_id = sys.argv[1]

    response = requests.get(base_url + "users/" + e_id)
    user = response.json()

    response = requests.get(base_url + "todos/")
    todos = response.json()

    u_todo = [todo for todo in todos if todo.get("userId") == user.get("id")]

    with open('filve.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in u_todo:
            writer.writerow([todo["userId"], user["name"],
                             todo["completed"], todo["title"]])


if __name__ == "__main__":
    do_requests()
