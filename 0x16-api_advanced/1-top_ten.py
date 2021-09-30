#!/usr/bin/python3
"""
1. Top diez
"""
import requests


def top_ten(subreddit):
    '''imprime los títulos de las primeras 10 publicaciones calientes
    enumerado para un subreddit determinado.'''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    HEADERS = {"User-Agent": "lou"}
    response = requests.get(url, HEADERS=HEADERS, allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        req = response.json()
        for item in req['data']['children']:
            print(item['data']['title'])