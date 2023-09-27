#!/usr/bin/python3
"""
This script fetches all tasks for all employees and records them in a
structured JSON file, 'todo_all_employees.json'.
"""

import json
import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def get_data(url):
    """
    Fetches data from the specified URL and returns it as a JSON object.
    If the request fails, it raises an HTTPError.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def main():
    """
    Fetches all users and their tasks, structures them according to
    requirements, and writes them to 'todo_all_employees.json' in JSON format.
    """
    users = get_data(USERS_URL)

    all_users_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        user_todos = get_data(f"{TODOS_URL}?userId={user_id}")

        user_tasks = [
            {"username": username, "task": todo.get(
                'title'
            ), "completed": todo.get('completed')}
            for todo in user_todos
        ]

        all_users_tasks[str(user_id)] = user_tasks

    for user_id in map(str, range(1, len(users) + 1)):
        all_users_tasks.setdefault(user_id, [])

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_users_tasks, f)


if __name__ == "__main__":
    main()
