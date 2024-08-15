#!/usr/bin/python3
""" 0. How many subs? """
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number of
    subscribers for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {'User-Agent': 'python:no_of_subs:v1.0 (by /u/Albieo_YGO)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return str(data['data']['subscribers'])

    return 0
