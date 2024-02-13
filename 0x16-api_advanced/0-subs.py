#!/usr/bin/python3
"""
python file to returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
