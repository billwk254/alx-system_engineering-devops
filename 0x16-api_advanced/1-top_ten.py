#!/usr/bin/python3


"""
1-top_ten
"""


import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.

    Returns:
        None
    """
    # Construct the URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'AlxBot/1.0 (by wamboo_bazenga)'}

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if len(posts) == 0:
            print("No hot posts found in the subreddit.")
        else:
            # Print the titles of the hot posts
            for i, post in enumerate(posts):
                print(f"{i + 1}. {post['data']['title']}")
    else:
        print("None")


if __name__ == '__main':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
