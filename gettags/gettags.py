import pandas as pd
from gspread_pandas import Spread, Client
import pickle

spread = Spread("tags_ichbinsophiescholl")
df = spread.sheet_to_df(sheet="Archive")

df.to_csv("data/tags_corpus.csv")
df.to_pickle("data/tags_corpus.pkl")

# columns: 'from_user', 'text', 'created_at', 'time', 'geo_coordinates', 'user_lang', in_reply_to_user_id_str', 'in_reply_to_screen_name', 'from_user_id_str', 'in_reply_to_status_id_str', 'source', 'profile_image_url', 'user_followers_count', 'user_friends_count', 'user_location', 'status_url', 'entities_str'
