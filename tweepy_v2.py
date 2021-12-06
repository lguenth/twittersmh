#!/usr/bin/env python3

import tweepy
from credentials import bearer_token, consumer_key, consumer_secret, access_token, access_token_secret
import pandas as pd
import datetime

api = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, wait_on_rate_limit=True)

query = "Sophie Scholl OR #ichbinsophiescholl"

now = datetime.datetime.now(datetime.timezone.utc)
# Timestamp 15 minutes ago (if we ever hit the rate limit)
end_time = now - datetime.timedelta(seconds=900)
# Converting to the correct standard (see also: https://ijmacd.github.io/rfc3339-iso8601/)
end_time = end_time.isoformat(sep="T", timespec="seconds")

# https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
tweet_fields = ["author_id", "created_at", "lang", "text", "entities", "in_reply_to_user_id"]
user_fields = []
expansions = ["author_id"]

search_results = api.search_recent_tweets(query=query, tweet_fields=tweet_fields, end_time=end_time)

old_corpus = pd.read_csv("data/corpus.csv")
new_corpus = []

for result in search_results.data:
    created_at = result.created_at
    tweet_id = result.id
    lang = result.lang
    text = result.text
    # hashtags = result.entities.hashtags
    # user_mentions = result.entities.mentions.username
    # user_id = result.author_id
    # user_name = result.author_id.username
    # user_screen_name = result.author_id.name

    line = {"created_at": created_at, "tweet_id": tweet_id, "text": text, "user_name": user_name, "user_screen_name": user_screen_name, "user_id": user_id, "hashtags": hashtags, "user_mentions": user_mentions, "lang": lang}

    if line not in new_corpus and line not in old_corpus:
    	new_corpus.append(line)

corpus_df = pd.DataFrame(new_corpus)
corpus_df = df.sort_values(by="created_at")
corpus_df.to_csv("data/corpus.csv", mode="a", index=False, header=False)

print(corpus_df.head())
# V2 parameters for search_recent_tweets: [query,start_time,end_time,since_id,until_id,max_results,next_token,expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields]
