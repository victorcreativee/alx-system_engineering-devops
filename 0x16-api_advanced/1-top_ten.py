#!/usr/bin/python3
"prints the titles of the first 10 hot posts listed for a given subreddit."

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    else:
