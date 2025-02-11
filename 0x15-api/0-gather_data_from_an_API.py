#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress."""
import requests
import sys

def fetch_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data")
        return

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    num_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        fetch_todo_list(int(sys.argv[1]))

