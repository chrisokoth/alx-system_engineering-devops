#!/usr/bin/python3
"""Module for task 1"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set custom User-Agent
    params = {"limit": 10}  # Get only the first 10 results
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)

