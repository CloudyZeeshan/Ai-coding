import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Delicious Food", layout="wide")

# Read HTML file
def load_html():
    with open("static/index.html", "r", encoding="utf-8") as file:
        return file.read()

# Render HTML inside Streamlit
st.components.v1.html(load_html(), height=2000, scrolling=True)
