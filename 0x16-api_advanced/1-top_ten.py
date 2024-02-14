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

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            if posts:
                return [post['data']['title'] for post in posts]
    except requests.HTTPError as e:
        print(f"Error fetching data: {e}")
    except requests.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []
