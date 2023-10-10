#!/usr/bin/python3
"""
Module with function that queries the reddit API
and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries reddit API and prints first 10 hot posts for given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        print("None")

    headers = {
        'User-Agent': 'Top ten hot posts scraper by u/deano_southafrican'
    }

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])

    else:
        print("None")
