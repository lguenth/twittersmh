import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from gspread_pandas import Spread, Client
import pickle

spread = Spread("tags_ichbinsophiescholl")
df = spread.sheet_to_df(sheet="Archive")

df.columns
df.to_csv("../data/tags_corpus.csv")
df.to_pickle("../data/tags_corpus.pkl")

df = pd.read_csv("../data/tags_corpus.csv")
df.rename(columns={"time": "datetime"}, inplace=True)

df["date"] = pd.to_datetime(df["datetime"], format="%d/%m/%Y %H:%M:%S")
df["day"] = df["date"].dt.date
df["time"] = df["date"].dt.time
df.sort_values(by="day", inplace=True, ignore_index=True)

pd.concat([df.head(1), df.tail(1)])


df["day_without_year"] = df["date"].dt.strftime("%d.%m.")
tweets_per_day = df.groupby(["day", "day_without_year"], as_index=False)[
    "text"].count()
tweets_per_day.rename(columns={"text": "tweet_count"}, inplace=True)
tweets_per_day.head()

sns.set_theme(rc={"figure.figsize": (25, 10)},
              style="ticks", palette="pastel")

X = tweets_per_day["day_without_year"]
Y = tweets_per_day["tweet_count"]

tpd = sns.barplot(data=tweets_per_day, x=X, y=Y)
tpd.set_xticklabels(tpd.get_xticklabels(), rotation=45, ha="center")
tpd.set(xlabel="Datum", ylabel="Anzahl Tweets")

fig = tpd.get_figure()
fig.savefig('../output/tags/tweets_per_day.png', bbox_inches='tight')