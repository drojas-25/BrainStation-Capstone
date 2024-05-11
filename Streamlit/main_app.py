import streamlit as st
from lucas_page import show_lucas_page
from john_page import show_john_page

# Adding pages to the app
pages = {
    "Lucas": show_lucas_page,
    "John": show_john_page,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Runs the selected page function
page = pages[selection]
page()
