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

old_corpus = pd.read_csv("corpus.csv")
new_corpus = []

for result in search_results.data:
    created_at = result.created_at
    tweet_id = result.id
    lang = result.lang
    text = result.text
    hashtags = result.entities.hashtags
    user_mentions = result.entities.mentions.username
    user_id = result.author_id
    user_name = result.author_id.username
    user_screen_name = result.author_id.name

    # For API V 1.1:
    # created_at = result._json["created_at"]
    # text = result._json["full_text"]
    # hashtags = result._json["entities"]["hashtags"]
    # user_mentions = result._json["entities"]["user_mentions"]
    # user_id = result._json["user"]["id"]
    # user_screen_name = result._json["user"]["screen_name"]
    # user_name = result._json["user"]["name"]
    # lang = result._json["lang"]

    line = {"created_at": created_at, "tweet_id": tweet_id, "text": text, "user_name": user_name, "user_screen_name": user_screen_name, "user_id": user_id, "hashtags": hashtags, "user_mentions": user_mentions, "lang": lang}

    # if line not in new_corpus and line not in old_corpus:
    #     new_corpus.append(line)

# corpus_df = pd.DataFrame(new_corpus)
# corpus_df = df.sort_values(by="created_at")
# corpus_df.to_csv("data/corpus.csv", mode="a", index=False, header=False)
#
# print(corpus_df.head())

# TODO Implement lists of urls, users etc; catch exception if empty
# urls = result._json["entities"]["urls"][LISTELEMENT]
# user_mentions_by_name = result._json["entities"]["user_mentions"][LISTELEMENT]["name"] # or "screen_name"
# user_mentions_by_id = result._json["entities"]["user_mentions"][LISTELEMENT]["id"]
# in_reply_to_user_id and/or in_reply_to_screen_name would be nice too

# V1.1 keys in search_tweets._json: created_at, id, id_str, full_text, truncated, display_text_range, entities, metadata, source, in_reply_to_status_id, in_reply_to_status_id_str, in_reply_to_user_id, in_reply_to_user_id_str, in_reply_to_screen_name, user, geo, coordinates, place, contributors, is_quote_status, retweet_count, favorite_count, favorited, retweeted, lang

# V2 parameters for search_recent_tweets: [query,start_time,end_time,since_id,until_id,max_results,next_token,expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields]
