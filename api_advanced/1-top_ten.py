#!/usr/bin/python3
"""documenting stuff"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(reddit_url, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return  

        data = response.json().get('data')
        if not data or 'children' not in data:
            return  

        for post in data['children']:
            print(post['data']['title'])

    except requests.RequestException:
        return
