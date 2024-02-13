#!/usr/bin/python3
"""
python file returns a list containing the titles of
all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            hot_list.extend(post['data']['title'] for post in posts)
            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
