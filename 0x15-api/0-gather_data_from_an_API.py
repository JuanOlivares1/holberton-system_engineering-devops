#!/usr/bin/python3
"""Python script that gets data from API"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(url, argv[1]))
    todos = requests.get('{}/todos?userId={}'.format(url, argv[1]))
    tasks = len([task for task in todos.json()
                 if task.get('completed') is True])
    print('Employee {} is done with tasks({}/{}):'
          .format(user.json().get('name'), tasks, len(todos.json())))
    for task in todos.json():
        if task.get('completed') is True:
            print('\t {}'.format(task.get('title')))
