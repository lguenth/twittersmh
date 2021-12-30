#!/usr/bin/env python3

import tweepy
from credentials import (
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
)
import pandas as pd
import datetime

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(
    auth,
    wait_on_rate_limit=True,
)

query = "Sophie Scholl OR Weiße Rose OR ichbinsophiescholl OR teamsoffer OR nichtsophiescholl"

# https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

search_results = api.search_full_archive(
    label="fulldev",
    query=query,
    fromDate="202101010000",
    toDate="202101020000",
    maxResults=10,
)
corpus = []

for result in search_results:
    created_at = result._json["created_at"]
    text = result._json["text"]
    hashtags = result._json["entities"]["hashtags"]
    user_mentions = result._json["entities"]["user_mentions"]
    user_id = result._json["user"]["id"]
    user_screen_name = result._json["user"]["screen_name"]
    user_name = result._json["user"]["name"]
    lang = result._json["lang"]

    line = {
        "created_at": created_at,
        "text": text,
        "user_name": user_name,
        "user_screen_name": user_screen_name,
        "user_id": user_id,
        "hashtags": hashtags,
        "user_mentions": user_mentions,
        "lang": lang,
    }

    if (not result.retweeted) and ("RT @" not in result.text):
        corpus.append(line)

corpus_df = pd.DataFrame(corpus)
corpus_df.to_csv("data/tweepy_v1_fa_corpus.csv", mode="a", index=False, header=False)
