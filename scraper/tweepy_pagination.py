import tweepy
from credentials import bearer_token

client = tweepy.Client(bearer_token=bearer_token)

# Replace with your own search query
query = "ichbinsophiescholl"
corpus_txt = open("/home/lukel/projekte/twittersmh/data/tweepy_v2_pag_test.txt", "a+")

# Replace the limit=1000 with the maximum number of Tweets you want
for tweet in tweepy.Paginator(
    client.search_recent_tweets,
    query=query,
    tweet_fields=["context_annotations", "created_at"],
    max_results=10,
).flatten():
    print(tweet.data)
    corpus_txt.write(f"{tweet.data}\n")
