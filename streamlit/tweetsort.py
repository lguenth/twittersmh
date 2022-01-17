import streamlit as st
import pandas as pd

# TODO Tags implementieren, siehe: https://github.com/gagan3012/streamlit-tags
# TODO Pfade implementieren
# TODO Heroku deployen
# TODO Index in CSV schreiben


def main():
    corpus = "/home/lukel/projekte/twittersmh/data/tweepy_corpus_de_cleaned.csv"

    if "index" not in st.session_state:
        st.session_state.index = 0
    if "keep" not in st.session_state:
        st.session_state.keep = []
    if "keep_df" not in st.session_state:
        st.session_state.keep_df = pd.DataFrame(
            columns=["index", "tweets_saved", "tags"]
        )
    if "discard" not in st.session_state:
        st.session_state.discard = []
    if "discard_df" not in st.session_state:
        st.session_state.discard_df = pd.DataFrame(
            columns=["index", "tweets_discarded"]
        )
    if "df" not in st.session_state:
        st.session_state.df = pd.read_csv(corpus, sep=";", dtype=object)

    st.title("Tweetsort – Korpus filtern leichtgemacht")

    if st.session_state.index <= st.session_state.df.shape[0]:
        st.write(f"Tweet mit Index {st.session_state.index}:")

        st.markdown(
            f'> "{st.session_state.df["text_clean"].iloc[st.session_state.index]}"'
        )

        if st.button("Behalten"):
            st.session_state.keep.append(
                st.session_state.df["text_clean"].iloc[st.session_state.index - 1]
            )
            st.session_state.keep_df.loc[
                len(st.session_state.keep_df.index)
            ] = st.session_state.df["text_clean"].iloc[st.session_state.index - 1]

        if st.button("Aussortieren"):
            st.session_state.discard.append(
                st.session_state.df["text_clean"].iloc[st.session_state.index - 1]
            )
            st.session_state.discard_df.loc[
                len(st.session_state.discard_df.index)
            ] = st.session_state.df["text_clean"].iloc[st.session_state.index - 1]

        if st.button("Speichern"):
            st.session_state.keep_df = st.session_state.keep_df.drop_duplicates()
            st.session_state.discard_df = st.session_state.discard_df.drop_duplicates()
            st.session_state.keep_df.to_csv(
                "/home/lukel/projekte/twittersmh/data/tweepy_corpus_saved_tweets.csv"
            )
            st.session_state.discard_df.to_csv(
                "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded_tweets.csv"
            )
            st.write("Tweets gespeichert!")
            st.session_state.index -= 1

        if st.button("Cache leeren und Seite neu laden"):
            st.legacy_caching.clear_cache()
            st.session_state.index = 0
            st.session_state.keep = []
            st.session_state.discard = []
            st.session_state.keep_df = st.session_state.keep_df.drop_duplicates()
            st.session_state.discard_df = st.session_state.discard_df.drop_duplicates()
            st.experimental_rerun()

    elif st.session_state.index == st.session_state.df.shape[0]("Speichern"):
        st.write("Alle Tweets sortiert und gespeichert!")
        st.session_state.keep_df.to_csv(
            "/home/lukel/projekte/twittersmh/data/tweepy_corpus_saved_tweets.csv"
        )
        st.session_state.discard_df.to_csv(
            "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded_tweets.csv"
        )

    st.markdown("## Aussortiert")
    st.expander("aussortiert")
    st.write(st.session_state.discard)

    st.markdown("## Behalten")
    st.expander("behalten")
    st.write(st.session_state.keep)
    st.session_state.index += 1


if __name__ == "__main__":
    main()

    #
    # "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded.csv"
