#!/usr/bin/python3
"""Gather data from an API
"""

import requests
import sys

url = "https://jsonplaceholder.typicode.com/"


def fetch_employee_progress(employee_id):
    """
    given employee ID, returns information about his/her TODO list progress.

    The script must display on the standard output the employee TODO list
    progress in this exact format:
        First line: Employee EMPLOYEE_NAME is done with tasks
        (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is
                                   the sum of completed and non-completed tasks
        Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
    """
    base_url = url + "users/{}".format(employee_id)
    todos_url = url + "todos?userId={}".format(employee_id)

    user_response = requests.get(base_url)
    user_data = user_response.json()
    name = user_data.get("name")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task["completed"]]
    todos_done = len(completed_tasks)
    todos_count = len(todos_data)

    output = "Employee {} is done with tasks({}/{}):".format(
        name, todos_done, todos_count
    )
    print(output)

    for task in completed_tasks:
        print(f"    {task['title']}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    fetch_employee_progress(employee_id)
