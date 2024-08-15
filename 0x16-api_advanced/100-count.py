#!/usr/bin/python3
"""
3. Count it!
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    a recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    """
    try:
        if not is_valid_subreddit(subreddit):
            print(None)
        
        if counts is None:
            counts = {}

        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

        params = {'after': after}

        headers = {'User-Agent': 'python:recurse_it:v1.0 (by /u/Albieo_YGO)'}

        response = requests.get(url, params=params, headers=headers,
                                allow_redirects=False)

        data = response.json()

        for post in data['data']['children']:
            title = post['data']['title']
            title = title.lower()

            for word in word_list:
                word_count = title.count(word.lower())
                if word.lower() in counts:
                    counts[word.lower()] += word_count
                else:
                    counts[word.lower()] = word_count

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)

        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print("{}: {}".format(word, count))

    except Exception:
        return (None)


def is_valid_subreddit(subreddit):
    """
    Checks if the subrreddit is valid.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'python:check_it:v1.0 (by /u/Albieo_YGO)'}

    if requests.get(url, headers=headers).status_code == 200:
        return bool(subreddit)

    return (False)
