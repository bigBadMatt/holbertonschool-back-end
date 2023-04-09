#!/usr/bin/python3
"""
given employee ID, returns information about his/her TODO list progress
"""
import csv
import requests
import sys


if __name__ == '__main__':

    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    todo_list = requests.get(
        todo_url,
        params={"userId": sys.argv[1]}
    ).json()

    user_name = requests.get(user_url).json().get("username")

    with open("{}.csv".format(user_id), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            writer.writerow([
                user_id,
                user_name,
                task['completed'],
                task['title']
            ])
