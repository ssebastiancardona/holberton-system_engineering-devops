#!/usr/bin/python3
"""
numero de subscriptores
"""
import requests


def number_of_subscribers(subreddit):
    '''devuelve el número de suscriptores de un subreddit determinado.'''

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "lou"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    req = response.json()
    return req['data']['subscribers']
