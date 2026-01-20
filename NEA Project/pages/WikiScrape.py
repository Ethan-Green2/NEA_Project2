import streamlit as st
from scrape import scrape_website

st.title("Wikipedia Scraper")

topic = st.text_input("Enter a Wikipedia topic:")

if st.button("Scrape Wikipedia"):
    if topic:
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}" #Converts inputted topic as a valid URL for wikipedia
        st.write(f"Scraping: {url}")

        html = scrape_website(url)

        # Display preview or process it further
        st.text_area("Raw HTML (preview)", html[:5000], height=1000)
    else:
        st.warning("Please enter a topic.")
