#!/usr/bin/python3
"""documenting stuff"""
import requests


def top_ten(subreddit):
    """Docs"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if not data or 'children' not in data:
            print(None)
            return

        for post in data['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
        
