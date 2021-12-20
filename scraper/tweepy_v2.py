#!/usr/bin/env python3

from datetime import date, timezone, datetime
import tweepy
from tweepy import user
from credentials import bearer_token, consumer_key, consumer_secret
import pandas as pd
import json

status = json.load("../data/current_status.json")
current_id = status.current_id

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key,
                       consumer_secret=consumer_secret, wait_on_rate_limit=True)

query = "Sophie Scholl OR Weiße Rose OR ichbinsophiescholl OR teamsoffer OR nichtsophiescholl OR SophieScholl OR WeißeRose OR 'Ich bin Sophie Scholl' OR sophiescholl100 OR 'Ich bin nicht Sophie Scholl' OR 100JahreSophieScholl"

tweet_fields = ["id", "text", "author_id", "conversation_id", "created_at", "entities",
                "geo", "lang", "in_reply_to_user_id", "referenced_tweets", "public_metrics", "organic_metrics"]
user_fields = ["id", "name", "username", "public_metrics", "protected"]
expansions = ["author_id", "referenced_tweets.id", "in_reply_to_user_id", "attachments.media_keys",
              "attachments.poll_ids", "geo.place_id", "entities.mentions.username", "referenced_tweets.id.author_id"]
place_fields = ["full_name", "id", "country_code", "place_type", "geo"]
media_fields = [""]

now = datetime.now(timezone.utc).astimezone().isoformat()

# This uses the https://api.twitter.com/2/tweets/search/all endpoint:
search_results = client.search_all_tweets(
    query=query, start_time="2021-01-01T00:00:00+01:00", end_time=now, tweet_fields=tweet_fields, expansions=expansions, media_fields=media_fields, user_fields=user_fields, place_fields=place_fields, since_id=current_id)
