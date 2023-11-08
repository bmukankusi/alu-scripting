#!/usr/bin/python3
"""Funtion t print hot posts on agiven Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json". format(subreddit)
    headers = {
        "User-Agent": "Linux:api.advanced:vi.0.0 (by /u/bdov_)"
    }
    parans = {
            "Limit": 10 
            }
    response = requests.get(url, headers=headers, parans=parans,
            allon_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json()get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
