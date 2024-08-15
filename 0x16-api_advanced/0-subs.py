#!/usr/bin/python3
""" 0. How many subs? """
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number of
    subscribers for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    """
    if not is_valid_subreddit(subreddit):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {'User-Agent': 'python:no_of_subs:v1.0 (by /u/Albieo_YGO)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json()
    return data['data']['subscribers']


def is_valid_subreddit(subreddit):
    """
    Checks if the subreddit is valid.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'python:check_it:v1.0 (by /u/Albieo_YGO)'}

    if requests.get(url, headers=headers).status_code == 200:
        return bool(subreddit)

    return False
