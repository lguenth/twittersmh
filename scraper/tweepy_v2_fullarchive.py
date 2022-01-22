#!/usr/bin/env python3

import tweepy
import pandas as pd
from time import sleep
from credentials import bearer_token

client = tweepy.Client(
    bearer_token=bearer_token,
    wait_on_rate_limit=True,  # see: https://developer.twitter.com/en/docs/twitter-api/rate-limits
)

query = "Sophie Scholl OR Weiße Rose OR ichbinsophiescholl OR teamsoffer OR nichtsophiescholl OR SophieScholl OR WeißeRose OR Ich bin Sophie Scholl OR sophiescholl100 OR Ich bin nicht Sophie Scholl OR 100JahreSophieScholl"

tweet_fields = [
    "id",
    "text",
    "author_id",
    "conversation_id",
    "created_at",
    "entities",
    "geo",
    "lang",
    "in_reply_to_user_id",
    "referenced_tweets",
    "public_metrics",
]

user_fields = [
    "id",
    "name",
    "username",
]

expansions = [
    "author_id",
    "geo.place_id",
    "entities.mentions.username",
    "referenced_tweets.id.author_id",
]

corpus = []
expansion_list = []

responses = tweepy.Paginator(
    client.search_all_tweets,
    query=query,
    start_time="2021-01-01T00:00:00+00:00",
    tweet_fields=tweet_fields,
    expansions=expansions,
    user_fields=user_fields,
    max_results=100,
)

count = 1
for response in responses:
    for tweet in response.data:

        if tweet.id:
            tweet_id = tweet.id
        if tweet.conversation_id:
            conversation_id = tweet.conversation_id
        if tweet.author_id:
            author_id = tweet.author_id
        if tweet.entities:
            entities = tweet.entities
        if tweet.public_metrics:
            public_metrics = tweet.public_metrics
        if tweet.text:
            text = tweet.text
        if tweet.lang:
            lang = tweet.lang
        if tweet.referenced_tweets:
            referenced_tweets = tweet.referenced_tweets
        if tweet.created_at:
            created_at = tweet.created_at

        line = {
            "created_at": created_at,
            "tweet_id": tweet_id,
            "text": text,
            "conversation_id": conversation_id,
            "author_id": author_id,
            "entities": entities,
            "public_metrics": public_metrics,
            "referenced_tweets": referenced_tweets,
            "lang": lang,
        }

        corpus.append(line)
        print(count)
        print(line)

    count += 1
    expansion_list.append(response.includes)
    print("Sleeping...")
    sleep(1)

corpus_df = pd.DataFrame(corpus)
expansions_df = pd.DataFrame(expansion_list)

corpus_df.to_csv(
    "/home/lukel/projekte/twittersmh/data/tweepy_corpus_raw.csv",
    mode="a",
    index=False,
    header=False,
    sep=";",
)

expansions_df.to_csv(
    "/home/lukel/projekte/twittersmh/data/tweepy_expansions.csv",
    mode="a",
    index=False,
    header=False,
    sep=";",
)
