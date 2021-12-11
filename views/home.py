import streamlit as st
import pandas as pd
import tweepy
import plotly
from models import preprocessing

from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def convert_input_to_sequences(text, max_length, model):
    tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
    tokenizer.fit_on_texts(text)

    sequence = tokenizer.texts_to_sequences(text)
    sequence_pad = pad_sequences(sequence, maxlen=max_length, padding="post")

    return text, (model.predict(sequence_pad))


def app():
    st.write("# **One-Click Sentiment**")
    st.write("Cari topik yang anda inginkan untuk mendapatkan review sentimen dengan sekali klik.")
    st.write("")

    keyword = st.text_input("Cari Topik Yang Diinginkan")

    if keyword:
        client = tweepy.Client(
            bearer_token='AAAAAAAAAAAAAAAAAAAAAM01KwEAAAAAC3RY1heL2TfLbYd9%2BgQuZ%2Fe2mic%3DFXDtI2duLTYTSl7xwkcnRMmgmo1X0nw5OOyKPYZNIRWqTUiBle')

        query = f'{keyword} lang:id -is:retweet'

        tweets = client.search_recent_tweets(
            query=query, tweet_fields=['context_annotations', 'created_at'],
            max_results=100
        )

        tweets = [tweet.text for tweet in tweets.data]

        sentiment = []
        model = load_model('./models/model.h5')

        # for i in range(len(tweets)):
        #     text = preprocessing.preprocessing_data(tweets[i])
        #     text, result = convert_input_to_sequences([text], 35, model)
        #
        #     if result[0][0] > result[0][1]:
        #         result = 0
        #     else:
        #         result = 1
        #
        #     sentiment.append([text[0], result])
        text = preprocessing.preprocessing_data("dia buat konten buka buka area privatnya di depan orang lain itu sama saja dengan lakilaki yang nunjukin area bawahnya sambil ngocok di depan perempuan yang lagi lewat siskaeee ini sebenernya memang sudah harus masuk bui dari dulu")
        text, result = convert_input_to_sequences([text], 35, model)

        st.write(result)
        st.write(text)
