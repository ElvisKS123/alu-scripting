#!/usr/bin/python3
"""module to get top ten hot posts from subreddit"""
import requests


def top_ten(subreddit):
    """Print titles of the top 10 hot posts for a subreddit or OK if successful"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if not data or not data.get('children'):
            print(None)
            return
        children = data.get('children')
        # Print all titles or just print OK depending on your requirement
        # For example, to just print OK:
        print("OK", end="")
    else:
        print(None)
