#!/usr/bin/python3
"""
This is a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers subreddit"""
    req = requests.get('https://www.reddit.com/requests/{}/about/json'
                       .format(subreddit),
                       headers={'User-Agent': 'Cecales'},
                       allow_redirects=False)
    if req.status_code >= 300:
        return 0
    return req.json().get('data').get('subscribers')
