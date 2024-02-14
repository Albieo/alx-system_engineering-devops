#!/usr/bin/python3
""" 2. Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    A recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given
    subreddit, the function should return None
    """
    if not is_valid_subreddit(subreddit):
        return None

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    params = {'after': after}

    headers = {'User-Agent': 'python:recurse_it:v1.0 (by /u/Albieo_YGO)'}

    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    data = response.json()

    for post in data['data']['children']:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list


def is_valid_subreddit(subreddit):
    """
    Checks if the subrreddit is valid.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'python:check_it:v1.0 (by /u/Albieo_YGO)'}

    if requests.get(url, headers=headers).status_code == 200:
        return bool(subreddit)

    return False