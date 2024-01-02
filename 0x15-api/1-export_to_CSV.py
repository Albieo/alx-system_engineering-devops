#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
import sys


url = "https://jsonplaceholder.typicode.com/"


def fetch_employee_progress(employee_id):
    """
    given employee ID, returns information about his/her TODO list progress.

    Extend your Python script to export data in the CSV format.
        Records all tasks that are owned by this employee
        Format must be: "USER_ID","USERNAME",
                        "TASK_COMPLETED_STATUS","TASK_TITLE"
        File name must be: USER_ID.csv
    """
    base_url = url + "users/{}".format(employee_id)
    todos_url = url + "todos?userId={}".format(employee_id)

    user_response = requests.get(base_url)
    user_data = user_response.json()
    name = user_data.get("name")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    with open(f"{employee_id}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow(
                [employee_id, name, task.get("completed"), task.get("title")]
            )


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    fetch_employee_progress(employee_id)
