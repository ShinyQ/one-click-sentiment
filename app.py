import streamlit as st
from views import home
from views import sentiment

st.set_page_config(
    page_title='OneClick Sentiment - Data Science Associate Microcredential',
    page_icon='https://telkomuniversity.ac.id/wp-content/uploads/2019/07/cropped-favicon-2-32x32.png',
    layout='wide'
)

PAGES = {
    "🌎 Halaman Utama": home,
    "💡 Halaman Sentiment Kalimat": sentiment,
}

st.sidebar.subheader('Navigasi')

page = st.sidebar.selectbox("Pindah Halaman", list(PAGES.keys()))
page = PAGES[page]
page.app()
