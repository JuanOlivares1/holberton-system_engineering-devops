#!/usr/bin/python3
"""Python script that gets data from API"""
"""get data and saves it in a json"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(url, argv[1])).json()
    todo = requests.get('{}/todos?userId={}'.format(url, argv[1])).json()
    user_id = user.get('id')

    with open('{}.json'.format(argv[1]), "w") as file:
        json_dict = {user_id: []}
        for i in todo:
            dict_ = {
                'task': i.get('title'),
                'completed': i.get('completed'),
                'username': user.get('username')}
            json_dict.get(user.get('id')).append(dict_)
        json.dump(json_dict, file)
