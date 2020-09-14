#!/usr/bin/python3
"""Python script that gets data from API"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users/' + argv[1]
    todo_url = url + 'todos'

    response = requests.get(user_url)
    username = response.json().get('username')

    response = requests.get(todo_url)
    todos = []
    for task in response.json():
        if task.get('userId') == int(argv[1]):
            todos.append(task)

    with open('{}.csv'.format(argv[1]), 'w') as file:
        columns = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(file, fieldnames=columns,
                                quoting=csv.QUOTE_ALL)

        for task in todos:
            task['username'] = username
            del task['id']
            writer.writerow(task)
