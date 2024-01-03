import streamlit as st
import pyshorteners as pyst
import pyperclip
shortener = pyst.Shortener()
def copying():
    pyperclip.copy(shortened_url)
st.markdown("## :violet[URL Shortener]")

with st.form("URLs"):
    url=st.text_input("Enter URL here")
    btn=st.form_submit_button("Shorten")

    if btn:
        #shortened_url=shortener.tinyurl.short(url)
        shortened_url=shortener.dagd.short(url)
        st.success(":bold[Shortened URL :] " + shortened_url)
        st.form_submit_button("Copy Shortened URL", on_click=copying())