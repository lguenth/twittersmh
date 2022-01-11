import streamlit as st
import pandas as pd

# TODO Tags implementieren, siehe: https://github.com/gagan3012/streamlit-tags


def main():
    corpus = "/home/lukel/projekte/twittersmh/data/tweepy_corpus_cleaned.csv"

    if "index" not in st.session_state:
        st.session_state.index = 0
    if "keep" not in st.session_state:
        st.session_state.keep = []
    if "keep_df" not in st.session_state:
        st.session_state.keep_df = pd.DataFrame(columns=["tweets_saved"])
    if "discard" not in st.session_state:
        st.session_state.discard = []
    if "discard_df" not in st.session_state:
        st.session_state.discard_df = pd.DataFrame(columns=["tweets_discarded"])
    if "df" not in st.session_state:
        st.session_state.df = pd.read_csv(corpus, sep=";", dtype=object)

    st.title("Tweetsort – Korpus filtern leichtgemacht")
    st.text(
        "Hinweise:\n- C drücken, um Cache zu leeren,\n- R drücken, um Programm neu zu laden"
    )

    if st.session_state.index <= st.session_state.df.shape[0]:
        st.write(f"Tweet in Zeile {st.session_state.index}:")

        st.write(st.session_state.df["text_clean"].iloc[st.session_state.index])

        if st.button("Behalten"):
            st.session_state.keep.append(
                st.session_state.df["text_clean"].iloc[st.session_state.index]
            )
            st.session_state.keep_df.loc[
                len(st.session_state.keep_df.index)
            ] = st.session_state.df["text_clean"].iloc[st.session_state.index]

        if st.button("Aussortieren"):
            st.session_state.discard.append(
                st.session_state.df["text_clean"].iloc[st.session_state.index]
            )
            st.session_state.discard_df.loc[
                len(st.session_state.discard_df.index)
            ] = st.session_state.df["text_clean"].iloc[st.session_state.index]

        if st.button("Speichern"):
            st.session_state.keep_df.to_csv(
                "/home/lukel/projekte/twittersmh/data/tweepy_corpus_saved_tweets.csv"
            )
            st.session_state.discard_df.to_csv(
                "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded_tweets.csv"
            )
            st.write("Tweets gespeichert!")

    elif st.session_state.index == st.session_state.df.shape[0]("Speichern"):
        st.write("Alle Tweets sortiert und gespeichert!")
        st.session_state.keep_df.to_csv(
            "/home/lukel/projekte/twittersmh/data/tweepy_corpus_saved_tweets.csv"
        )
        st.session_state.discard_df.to_csv(
            "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded_tweets.csv"
        )

    st.markdown("## Aussortiert")
    st.expander("Aussortiert")
    st.write(st.session_state.discard)

    st.markdown("## Gespeichert")
    st.expander("Gespeichert")
    st.write(st.session_state.keep)
    st.session_state.index += 1


if __name__ == "__main__":
    main()

    #
    # "/home/lukel/projekte/twittersmh/data/tweepy_corpus_discarded.csv"
