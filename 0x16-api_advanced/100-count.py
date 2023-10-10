#!/usr/bin/python3
"""
Module for querying reddit API to parse data from subreddits and posts
"""

from collections import defaultdict
import requests


def count_words(subreddit, word_list, after=None,
                word_counts=defaultdict(int)):
    """
    Queries reddit API and parses the title of all hot articles,
    prints a sorted count of given keywords.
    """
    headers = {'User-Agent': 'script to parse all titles by u/deano_southafrican'}
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    if after:
        url += "?after={}".format(after)
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        if after is None:
            return
        else:
            sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                if count > 0:
                    print("{}: {}".format(word, count))
            return

    data = response.json()['data']
    titles = [post['data']['title'] for post in data['children']]

    for title in titles:
        title_words = title.split()
        for word in word_list:
            word_counts[word.lower()] += title_words.count(word)
            for title_word in title_words:
                if title_word.lower().rstrip('!?.') == word.lower():
                    word_counts[word.lower()] += 1

    if data['after']:
        return count_words(subreddit, word_list, data['after'], word_counts)
    else:
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print("{}: {}".format(word, count))
