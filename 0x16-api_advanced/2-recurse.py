#!/usr/bin/python3
"""
This is a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ all hot articles of a subreddit """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {
            'User-Agent': 'Cecales'
            }
    if after is None:
        return hot_list
    req = requests.get(url, headers=headers,
                       allow_redirects=False,
                       params={'after': after})
    if req.status_code != 200:
        return None
    data = req.json().get('data').get('children')
    hot_list += data
    after = req.json().get('data').get('after')
    return recurse(subreddit, hot_list, after)
