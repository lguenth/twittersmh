# %%
import pandas as pd

corpus = "/home/lukel/projekte/twittersmh/data/tweepy_v2_corpus.csv"
df = pd.read_csv(corpus, sep=";", header=None, dtype=object, names=[
    "created_at",
    "tweet_id",
    "text",
    "conversation_id",
    "author_id",
    "entities",
    "public_metrics",
    "referenced_tweets",
    "lang",
])

# %%
pd.set_option("display.max_colwidth", None)
df.head(5)

# %%
df.shape

# %%
pd.to_datetime(df["created_at"], errors="coerce")
print("These could not be converted:")
nan = df[df["created_at"].isna() == True]
nan

# %%
df["day"] = df["created_at"].dt.date
df["time"] = df["created_at"].dt.time
df.sort_values(by="day", inplace=True, ignore_index=True)
df.head(5)

# %%
de = df[df["lang"] == "de"]

# %%
de.head(5)
