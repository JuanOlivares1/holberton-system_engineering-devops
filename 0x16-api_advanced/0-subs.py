#!/usr/bin/python3
"""Gets data form reddit api"""
import requests


def number_of_subscribers(subreddit):
    """gets number of subscribers from a specific subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + "/about.json"
    head = {'User-Agent': "valaak"}
    response = requests.get(url, headers=head, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
