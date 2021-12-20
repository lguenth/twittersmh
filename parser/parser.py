# corpus = []

# for result in search_results.data:
    # created_at = result.created_at
    # tweet_id = result.id
    # lang = result.lang
    # text = result.text
    # line = {"created_at": created_at, "tweet_id": tweet_id, "text": text}
    # corpus.append(line)
    #     # "user_screen_name": user_screen_name, "user_id": user_id, "hashtags": hashtags, "user_mentions": user_mentions, "lang": lang}

    # df = pd.DataFrame(corpus).sort_values(by="created_at")
    # df["datetime"] = pd.to_datetime(df["created_at"], format="%d/%m/%Y %H:%M:%S")
    # print(df["lang"])
    # df.to_csv("../data/tweepy_corpus.csv", mode="a", index=False, header=False)
