import pandas as pd
import requests
import streamlit as st
import tweepy
import json
import plotly.graph_objects as go
import numpy as np


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
            max_results=20
        )

        tweets = [tweet.text for tweet in tweets.data]

        sentiment = []
        negatif = 0
        positif = 0

        for data in tweets:
            response = requests.post("https://oneclick.shinyq.my.id/predict", data=json.dumps({'text': data}))
            response = response.json().get('data')

            if response.get('predict') == 'Positif':
                positif += 1
            else:
                negatif += 1

            confidence = response.get('confidence')[1]

            if response.get('confidence')[0] > response.get('confidence')[1]:
                confidence = response.get('confidence')[0]

            sentiment.append([data, response.get('preprocess'), confidence, response.get('predict')])

        df = pd.DataFrame(
            columns=['Tweet', 'Preprocessing', 'Confidence', 'Prediction'],
            data=np.array(sentiment)
        )

        st.table(df)

        fig = go.Figure(data=[go.Pie(labels=["Positif", "Negatif"], values=[positif, negatif])])
        fig.update_traces(textposition='inside', textinfo='percent+label+value', marker=dict(colors=['green', 'red']), )
        fig.update_layout(
            height=500,
            width=900,
            title=f'Persentase Sentimen Dari Keyword "{keyword}"',
            font=dict(
                size=16,
            )
        )

        st.plotly_chart(fig)
