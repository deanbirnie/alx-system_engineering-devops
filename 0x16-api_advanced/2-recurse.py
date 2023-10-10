#!/usr/bin/python3
"""
Module for querying Reddit API and separating pages of responses
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Query reddit API and return list of hot posts.
    """
    headers = {
        'User-Agent': 'script to scrape post titles by u/deano_southafrican'
        }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list += [post['data']['title'] for post in data['children']]

    if data['after']:
        return recurse(subreddit, hot_list, data['after'])

    return hot_list
