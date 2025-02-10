#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress."""

#!/usr/bin/python3
"""
Script that exports an employee's TODO list data to a CSV file.
"""

import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"


    user_res = requests.get(f"{base_url}/users/{user_id}")
    if user_res.status_code != 200:
        print("Error: User not found")
        sys.exit(1)

    user_data = user_res.json()
    username = user_data.get("username")


    todos_res = requests.get(f"{base_url}/todos?userId={user_id}")
    todos = todos_res.json()


    filename = f"{user_id}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"), task.get("title")])

    print(f"Data exported to {filename}")
