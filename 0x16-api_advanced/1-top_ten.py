#!/usr/bin/python3
""" 1. Top Ten """
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    params = {
        'limit': 10,
        }

    headers = {
        'User-Agent': 'python:top_ten:v1.0 (by /u/Albieo_YGO)',
        }

    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
