#!/usr/bin/python3
"""
This module provides a function to retrieve the number of subscribers
for a given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or an error occurs, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get('data', {}).get('subscribers', 0)
        return 0
    except Exception:
        return 0

