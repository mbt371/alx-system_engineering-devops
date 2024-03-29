#!/usr/bin/python3
"""This module makes a request to reddit api"""
import requests as req

url = 'https://www.reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    """This function fetches reddit and returns the number of subscribers"""
    agent = {'User-Agent': 'My User Agent 1.0'}
    res = req.get(url.format(subreddit), headers=agent, allow_redirects=False)
    body = res.json().get('data', {})
    return body.get('subscribers', 0)
