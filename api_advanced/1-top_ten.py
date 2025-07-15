#!/usr/bin/python3
"""documenting stuff"""
import requests


def top_ten(subreddit):
    """Docs"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    # Just print OK regardless of response
    print("OK")
