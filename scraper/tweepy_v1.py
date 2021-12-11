#!/usr/bin/env python3

import tweepy
from credentials import bearer_token, consumer_key, consumer_secret, access_token, access_token_secret
import pandas as pd
import datetime

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

query = "Sophie Scholl OR #ichbinsophiescholl"

# https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

search_results = api.search_tweets(q=query, tweet_mode="extended")
corpus = []

for result in search_results:
    created_at = result._json["created_at"]
    text = result._json["full_text"]
    hashtags = result._json["entities"]["hashtags"]
    user_mentions = result._json["entities"]["user_mentions"]
    user_id = result._json["user"]["id"]
    user_screen_name = result._json["user"]["screen_name"]
    user_name = result._json["user"]["name"]
    lang = result._json["lang"]

    line = {"created_at": created_at, "text": text, "user_name": user_name, "user_screen_name": user_screen_name,
            "user_id": user_id, "hashtags": hashtags, "user_mentions": user_mentions, "lang": lang}

    corpus.append(line)

corpus_df = pd.DataFrame(corpus)
corpus_df.to_csv("data/tweepy_corpus.csv", mode="a", index=False, header=False)
print(corpus_df.head())


# TODO Implement lists of urls, users etc; catch exception if empty
# urls = result._json["entities"]["urls"][LISTELEMENT]
# user_mentions_by_name = result._json["entities"]["user_mentions"][LISTELEMENT]["name"] # or "screen_name"
# user_mentions_by_id = result._json["entities"]["user_mentions"][LISTELEMENT]["id"]
# in_reply_to_user_id and/or in_reply_to_screen_name would be nice too

# V1.1 keys in search_tweets._json: created_at, id, id_str, full_text, truncated, display_text_range, entities, metadata, source, in_reply_to_status_id, in_reply_to_status_id_str, in_reply_to_user_id, in_reply_to_user_id_str, in_reply_to_screen_name, user, geo, coordinates, place, contributors, is_quote_status, retweet_count, favorite_count, favorited, retweeted, lang

# V2 parameters for search_recent_tweets: [query,start_time,end_time,since_id,until_id,max_results,next_token,expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields]
