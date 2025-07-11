import streamlit as st
from pathlib import Path

# Load the HTML file
def load_html():
    html_path = Path(__file__).parent / "codewithai" / "index.html"
    return html_path.read_text(encoding='utf-8')

st.set_page_config(page_title="Delicious Food", layout="wide")
st.components.v1.html(load_html(), height=1800, scrolling=True)
