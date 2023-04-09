#!/usr/bin/python3
"""
given employee ID, returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == '__main__':

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    user_data = requests.get(user_url).json()
    data = {}

    for user in user_data:
        user_id = user['id']
        todos = requests.get(todo_url, params={"userId": user_id}).json()
        user_todos = [
            {"username": user["username"],
             "task": todo["title"],
             "completed": todo["completed"]}
            for todo in todos]
        data[user_id] = user_todos

    with open("todo_all_employees.json".format(user_id), mode='w') as json_file:
        json.dump(data, json_file)
