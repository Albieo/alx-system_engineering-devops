#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests


url = "https://jsonplaceholder.typicode.com/"
base_url = url + "users/"


def export_all_to_json():
    """
    given employee ID, returns information about his/her TODO list progress.

    Extend your Python script to export data in the JSON format.
        Records all tasks from all employees
        Format must be: { "USER_ID": [{"task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
                {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"}, ... ]}
        File name must be: todo_all_employees.json
    """
    employees_data = {}
    user_response = requests.get(base_url)
    user_data = user_response.json()

    for user in user_data:
        employee_id = user["id"]
        username = user["username"]

        todos_url = url + "todos?userId={}".format(employee_id)
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        user_tasks = []

        for task in todos_data:
            task_info = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            user_tasks.append(task_info)

        employees_data[employee_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(employees_data, json_file, indent=2)


if __name__ == "__main__":
    export_all_to_json()
