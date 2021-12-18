#!/usr/bin/env python3

import tweepy
from credentials import bearer_token, consumer_key, consumer_secret
import pandas as pd
import datetime

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key,
                       consumer_secret=consumer_secret, wait_on_rate_limit=True)

query = "#ichbinsophiescholl"

# https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

search_results = client.search_all_tweets(
    query=query, start_time="2021-12-16", end_time="2021-12-17")
corpus = []

for result in search_results:
    corpus.append(result)

corpus_df = pd.DataFrame(corpus)
print(corpus_df.head())
