import streamlit as st
import pandas as pd

# TODO Tags implementieren, siehe: https://github.com/gagan3012/streamlit-tags
# TODO Pfade implementieren
# TODO Heroku deployen
# TODO Index in CSV schreiben


def main():
    corpus = "/home/lukel/projekte/twittersmh/data/tweepy_corpus_cleaned.csv"

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

    st.title("Tweetsort: Korpus filtern leichtgemacht")

    keep = st.session_state.keep
    keep_df = st.session_state.keep_df
    discard = st.session_state.discard
    discard_df = st.session_state.discard_df

    if st.session_state.index <= st.session_state.df.shape[0]:
        st.write(f"Tweet mit Index {st.session_state.index}:")

        st.markdown(
            f'> "{st.session_state.df["text_clean"].iloc[st.session_state.index]}"'
        )

        if st.button("Behalten"):
            keep.append(
                st.session_state.df["text_clean"].iloc[st.session_state.index - 1]
            )
            keep_df.loc[len(keep_df.index)] = st.session_state.df["text_clean"].iloc[
                st.session_state.index - 1
            ]

        if st.button("Aussortieren"):
            discard.append(
                st.session_state.df["text_clean"].iloc[st.session_state.index - 1]
            )
            discard_df.loc[len(discard_df.index)] = st.session_state.df[
                "text_clean"
            ].iloc[st.session_state.index - 1]

        if st.button("Speichern"):
            keep_df = keep_df.drop_duplicates()
            discard_df = discard_df.drop_duplicates()
            keep_df.to_csv(
                "/home/lukel/projekte/twittersmh/data/tweepy_corpus_saved_tweets.csv"
            )
            discard_df.to_csv(
                "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded_tweets.csv"
            )
            st.write("Tweets gespeichert!")
            st.session_state.index -= 1

        if st.button("Cache leeren und Seite neu laden"):
            st.legacy_caching.clear_cache()
            st.session_state.index = 0
            keep = []
            discard = []
            keep_df = keep_df.drop_duplicates()
            discard_df = discard_df.drop_duplicates()
            st.experimental_rerun()

    elif st.session_state.index == st.session_state.df.shape[0]("Speichern"):
        st.write("Alle Tweets sortiert und gespeichert!")
        keep_df.to_csv(
            "/home/lukel/projekte/twittersmh/data/tweepy_corpus_saved_tweets.csv"
        )
        discard_df.to_csv(
            "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded_tweets.csv"
        )

    st.markdown("## Aussortiert")
    st.expander("aussortiert")
    st.write(list(set(discard)))

    st.markdown("## Behalten")
    st.expander("behalten")
    st.write(set(keep))
    st.session_state.index += 1


if __name__ == "__main__":
    main()

    #
    # "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded.csv"
