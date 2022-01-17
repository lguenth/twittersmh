#!/usr/bin/env python3

import tweepy
import pandas as pd
from time import sleep
from credentials import bearer_token

# https://developer.twitter.com/en/docs/twitter-api/conversation-id

client = tweepy.Client(
    bearer_token=bearer_token,
    wait_on_rate_limit=True,
)

corpus = "/home/lukel/projekte/twittersmh/data/tweepy_corpus_raw.csv"

corpus_df = pd.read_csv(
    corpus,
    sep=";",
    header=None,
    dtype=object,
    names=[
        "created_at",
        "tweet_id",
        "text",
        "conversation_id",
        "author_id",
        "entities",
        "public_metrics",
        "referenced_tweets",
        "lang",
    ],
)

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

corpus = []

for conversation_id in corpus_df["conversation_id"]:
    query = f"conversation_id:{conversation_id}"

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

        threads.append(line)
        print(count)
        print(line)

    count += 1
    print("Sleeping...")
    sleep(1)

thread_df = pd.DataFrame(threads)
thread_df.groupby(["conversation_id"])

thread_df.to_csv(
    "/home/lukel/projekte/twittersmh/data/tweepy_corpus_threads.csv",
    mode="a",
    index=False,
    header=False,
    sep=";",
)
