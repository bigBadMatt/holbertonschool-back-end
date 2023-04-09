#!/usr/bin/python3
"""
given employee ID, returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == '__main__':

    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    todo_list = requests.get(
        todo_url,
        params={"userId": user_id}
    ).json()

    user_name = requests.get(user_url).json().get("username")

    data = {
        user_id: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
            }
            for task in todo_list
        ]
    }

    with open("{}.json".format(user_id), mode='w') as json_file:
        json.dump(data, json_file)
