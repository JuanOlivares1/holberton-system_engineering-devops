#!/usr/bin/python3
"""Request data to Reddit API"""
import requests


def top_ten(subreddit):
    """get the top ten hot post"""
    url = 'https://www.reddit.com/r/' + subreddit + "/hot.json"
    head = {'User-Agent': 'valaak'}
    response = requests.get(url, headers=head, allow_redirects=False)
    if response.status_code == 200:
        json = response.json()
        if 'data' in json:
            for post in json.get("data").get("children"):
                print(post.get("data").get("title"))
        else:
            print(None)
    else:
        print(None)
