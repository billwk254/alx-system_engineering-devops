#!/usr/bin/python3


"""
100-count
"""


import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    parses titles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of keywords to count.
        after (str): A parameter used for pagination
        count_dict (dict): A dictionary to store the counts of keywords.

    Returns:
        None
    """
    # Base case: if subreddit is invalid or no more pages of results
    if not subreddit:
        return

    # Initialize the count_dict if it's None (only on the first call)
    if count_dict is None:
        count_dict = {}

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
            # Iterate through the posts and parse titles
            for post in posts:
                title = post['data']['title'].lower()

                for keyword in word_list:
                    if keyword in title:
                        if keyword not in count_dict:
                            count_dict[keyword] = 1
                        else:
                            count_dict[keyword] += 1

        if after:
            return count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")
    else:
        return


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x.lower() for x in sys.argv[2:]]

        count_words(subreddit, keywords)
