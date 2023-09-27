#!/usr/bin/python3
"""Script to fetch employee TODO list progress from an API and export to CSV"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to retrieve data for employee ID: {}".format(
            employee_id
        ))
        exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get('username')
    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, username, task.get(
                'completed'
            ), task.get('title')])
