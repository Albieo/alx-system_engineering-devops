#!/usr/bin/python3
""" 1. Top Ten """
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of
    the first 10 hot-posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/Albieo_YGO)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and \
       response.headers.get('Content-Type') == 'application/json':
        data = response.json()

        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
