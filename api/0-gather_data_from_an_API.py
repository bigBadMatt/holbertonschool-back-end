#!/usr/bin/python3
"""
given employee ID, returns information about his/her TODO list progress
"""

import sys
import requests


if __name__ == '__main__':

    user_url =
    'https://jsonplaceholder.typicode.com/users{}'.format(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    todo_list = requests.get(
        todo_url,
        params={"userId": sys.argv[1]}
    ).json()

    completed_todo = requests.get(
        todo_url,
        params={
            'completed': 'true',
            'userId': sys.argv[1]
        }
    ).json()

    EMPLOYEE_NAME = requests.get(user_url).json()
    TOTAL_NUMBER_OF_TASKS = len(todo_list)
    NUMBER_OF_DONE_TASKS = len(completed_todo)

    print('Employee {} is done with tasks({}/{}):'.format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS
    ))
    for task in completed_todo:
        print('\t ' + task['title'])
