#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
from sys import argv


def to_csv():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_STATUS_TITLE = []

    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for task in todos.json():
        if task.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((task.get('completed'),
                                      task.get('title')))

    """export to csv"""
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    to_csv()
