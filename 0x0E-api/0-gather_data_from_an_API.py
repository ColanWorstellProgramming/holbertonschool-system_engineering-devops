#!/usr/bin/python3
import requests

def get_employee_todo_list_progress(employee_id):
    # Make request to API
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    # Parse response JSON
    todos = response.json()

    # Count number of completed tasks
    num_completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Print employee TODO list progress
    employee_name = todos[0]['name']
    total_num_tasks = len(todos)
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

    # Print titles of completed tasks
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

# Example usage
get_employee_todo_list_progress(1)
