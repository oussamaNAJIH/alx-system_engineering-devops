#!/usr/bin/python3
"""
python file to print the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            print("No posts found in this subreddit.")
        else:
            for post in posts:
                print(post['data']['title'])
    else:
        print("Invalid subreddit.")
