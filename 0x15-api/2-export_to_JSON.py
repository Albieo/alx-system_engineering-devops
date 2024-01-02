#!/usr/bin/python3
"""Export to JSON"""

import json
import requests
import sys


url = "https://jsonplaceholder.typicode.com/"


def export_to_json(employee_id):
    """
    given employee ID, returns information about his/her TODO list progress.

    Extend your Python script to export data in the JSON format.
        Records all tasks that are owned by this employee
        Format must be: { "USER_ID": [{"task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
                {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"}, ... ]}
        File name must be: USER_ID.json
    """
    base_url = url + "users/{}".format(employee_id)
    todos_url = url + "todos?userId={}".format(employee_id)

    user_response = requests.get(base_url)
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    user_tasks = []

    for task in todos_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        user_tasks.append(task_info)

    user_json = {"{}".format(employee_id): user_tasks}

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(user_json, json_file, indent=2)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
