#!/usr/bin/python3


"""
2-recurse
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles

    Args:
        subreddit (str): The name of the subreddit to search.
        hot_list (list): A list to store the titles of hot articles.
        after (str): A parameter used to fetch next page

    Returns:
        list: A list containing the titles of hot articles
    """
    # Base case: if subreddit is invalid or no more pages of results
    if not subreddit:
        return None

    # Construct the URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'AlxBot/1.0 (by wamboo_bazenga)'}

    # Add 'after' parameter for pagination if available
    if after:
        url += f'&after={after}'

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        if posts:
            # Append titles of hot articles to the list
            for post in posts:
                hot_list.append(post['data']['title'])

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        hot_articles = recurse(subreddit)

        if hot_articles is not None:
            print(len(hot_articles))
        else:
            print("None")
