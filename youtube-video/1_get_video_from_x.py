"""
1. [install snscrape](https://github.com/JustAnotherArchivist/snscrape)
2. /Applications/Python\ 3.X/Install\ Certificates.command to install system certificates or ```
python -m pip install certifi``` to install certifi and manually configure it.

"""

import ssl
import certifi
import snscrape.modules.twitter as sntwitter
import urllib.request
import pandas as pd

# # Patch SSL for macOS + pyenv: Set SSL context to use certifi's certificates
ssl._create_default_https_context = ssl.create_default_context
ssl._create_default_https_context().load_verify_locations(certifi.where())
print('------>', 
      certifi.where())

def get_tweets_from_user(user: str, num_tweets: int = 1000) -> pd.DataFrame:
    """
    Get tweets from a user using snscrape.
    Args:
        user (str): Twitter username without @.
        num_tweets (int): Number of tweets to scrape. Default is 1000.
    Returns:
        pd.DataFrame: DataFrame containing the tweets.
    """
    # Set SSL context to use certifi's certificates
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    ssl._create_default_https_context = ssl_context

    # Scrape tweets
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(user).get_items()):
        if i >= num_tweets:
            break
        tweets.append(tweet)

    # Create DataFrame
    df = pd.DataFrame(tweets)
    return df



print("hello")
import requests
response = requests.get("https://twitter.com", headers={'User-Agent': 'Mozilla/5.0'})
print(response.status_code)
# req = urllib.request.Request("https://twitter.com", headers={
#     'User-Agent': 'Mozilla/5.0'
# })
# response = urllib.request.urlopen(req)
# print(response.read()[:100])


# try:
#     for i, tweet in enumerate(sntwitter.TwitterUserScraper("elonmusk").get_items()):
#         if i >= 5:
#             break
#         print(tweet.content)
# except Exception as e:
#     print("Failed to fetch tweets:", e)