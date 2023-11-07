#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid rate limiting
    headers = {
        "User-Agent": "MyRedditBot/1.0 (by YourUsername)"
    }

    try:
        # Send a GET request to the API without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Extract and return the number of subscribers
            return data["data"]["subscribers"]
        else:
            # If the status code is not 200, it may indicate an invalid subreddit
            return 0
    except Exception as e:
        # Handle any exceptions that may occur
        print(f"An error occurred: {str(e)}")
        return 0

# Example usage:
subreddit = "python"
subscribers = number_of_subscribers(subreddit)
if subscribers > 0:
    print(f"The subreddit r/{subreddit} has {subscribers} subscribers.")
else:
    print(f"The subreddit r/{subreddit} is not valid or does not exist.")
