import streamlit as st

st.title("My App")

tab1, tab2 = st.tabs(["Window 1", "Window 2"])

with tab1:
    st.write("Content for first window")

with tab2:
    st.write("Content for second window")