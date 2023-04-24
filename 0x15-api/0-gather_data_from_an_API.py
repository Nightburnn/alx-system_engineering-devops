#!/usr/bin/python3
"""This script sends a request to an api and prints the
response
"""
import requests
from sys import argv


def gather_data(emp_id: int):
    """returns data about and employee from an api"""

    url_todo = "https://jsonplaceholder.typicode.com/todos/"
    url_users = "https://jsonplaceholder.typicode.com/users/"

    try:
        completed = 0
        payload1 = {"userId": emp_id}
        payload2 = {"id": emp_id}

        # make requests via the APIs
        resp_todo = requests.get(url_todo, params=payload1)
        resp_user = requests.get(url_users, params=payload2)

        # deserialize the responses
        emp_todo = resp_todo.json()
        emp_info = resp_user.json()[0]

        # get the total number of tasks for employee and the employee's name
        total_todo = len(emp_todo)
        emp_name = emp_info.get("name")

        # get the number of completed tasks
        for task in emp_todo:
            if task.get("completed"):
                completed += 1
        # output
        first_line = "Employee {} is done with tasks({}/{}):"
        print(first_line.format(emp_name, completed, total_todo))

        # print the title of the completed tasks
        for task in emp_todo:
            if task.get("completed"):
                print("\t {}".format(task.get("title")))
    except requests.exceptions.RequestException:
        print(resp_todo.status_code)


if __name__ == "__main__":
    try:
        emp_id = argv[1]

        if emp_id.isdigit():
            emp_id = int(emp_id)
            gather_data(emp_id)
    except IndexError:
        pass
