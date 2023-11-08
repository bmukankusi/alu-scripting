#!/usr/bin/python
"""A function to query a list of all hot..."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Return a list.."""
    url = "https://www.reddit.com/r/{}/hot/.json". format(subreddit)
    headers = {
        "User-Agent": "Linux:api.advanced:vi.0.0 (by /u/bdov_)"
    }
    parans = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(url, headers=headers, parans=parans,
            allon_redirects=False)
    if response.status_code == 404:
        return None

     results = response.json()get("data")
     after = results.get("after")
     count = results.get("dist")
     for c in results.get("children"):
         hot_list.append(c.get("data").get("title"))

         if after is not None:
             return recurse(subreddit, hot_list, after, count)
         return hot_list
