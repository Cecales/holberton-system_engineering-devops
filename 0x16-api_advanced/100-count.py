#!/usr/bin/python3
"""
This is a recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords (case-
insensitive, delimited by spaces. Javascript should count as javascript,
but java should not).
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Return count of words in word_list in the titles of the subreddit"""

    sub_info = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            params={'after': after},
                            headers={'User-Agent': 'Cecales'},
                            allow_redirects=False)
    if sub_info.status_code != 200:
        return None

    info = sub_info.json()

    hot_l = [child.get('data').get('title')
             for child in info
             .get('data')
             .get('children')]
    if not hot_l:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_l:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not info.get('data').get('after'):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           info.get('data').get('after'))
