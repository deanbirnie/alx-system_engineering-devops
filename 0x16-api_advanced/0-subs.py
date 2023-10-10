#!/usr/bin/python3
"""
Module for function that queries reddit API and returns
subscriber count of subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns number of subs for the given subreddit.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    headers = {
        'User-Agent': 'subscriber count scraper by u/deano_southafrican'
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
