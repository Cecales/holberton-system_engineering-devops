#!/usr/bin/python3
"""
This is a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests

def number_of_subscribers(subreddit):
    """number of subscribers subreddit"""
    url = 'https://www.reddit.com/requests/' + subreddit + 'about/json'
    headers = {
            'User-Agent': ''
            }
    req = requests.get(url, header=headers)
    data = req.json().get('data').get('subscribers')
    return data if data is not None
