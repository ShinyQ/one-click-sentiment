import requests
import streamlit as st
import json


def app():
    st.write("# **One-Click Sentiment**")
    st.write("Cari topik yang anda inginkan untuk mendapatkan review sentimen dengan sekali klik.")
    st.write("")

    keyword = st.text_area("Masukkan Kalimat Yang Ingin Di Analis")

    if keyword:
        response = requests.post("https://oneclick.shinyq.my.id/predict", data=json.dumps({'text': keyword}))
        response = response.json().get('data')

        st.markdown("##### Kalimat Yang Dimasukkan :")
        st.write(keyword)

        st.write("")

        st.markdown("##### Hasil Preprocessing Kalimat :")
        st.write(response.get('preprocess'))

        st.write("")

        st.markdown("##### Hasil Confidence Prediksi :")
        st.write(f'Negatif (0) : {response.get("confidence")[0]}, Positif (1) : {response.get("confidence")[1]}')

        st.write("")

        st.markdown("##### Hasil Analisis Sentimen :")
        st.write(response.get('predict'))

