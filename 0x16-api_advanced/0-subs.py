#!/usr/bin/python3
"""
python file to returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
