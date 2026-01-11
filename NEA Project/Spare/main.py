import streamlit as st
from googletrans import Translator
import requests

#Optional Languages
LANGUAGES = {
    'af': 'afrikaans',
    'en': 'english',
    'de': 'german',
    'ja': 'japanese',
    'ru': 'russian',
}

#Website UI
st.title("AI WebCrawler")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the Wesbite")

if st.button("Enter a Topic to Scrape"):
    st.write("Scraping Topic")

language_name = st.sidebar.selectbox("Select Language", list(LANGUAGES.keys()))
target_lang = LANGUAGES[language_name]

#Language Translation Function
def translate(text,dest_lang):
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e: #Handles any exceptions during translation
        st.error(f"Translation Error: {e}")
        return text
    
# original_texts = {
#     st.title("AI WebCrawler"),  
#     url = st.text_input("Enter a website URL: "),
#     st.button("Scrape Site"),
#     st.write("Scraping the Wesbite"),
# }

# Translate content
# translated_texts = {key: translate(text, target_lang) for key, text in original_texts()}

# # Display translated content
# st.title(translated_texts["AI WebCrawler"])
# url(translated_texts["Enter a website URL: "])
# st.button(translated_texts["Scrape Site"])
# st.button(translated_texts["description"])

# print(url)

# translator = Translator()

url = 'http://localhost:8501'

page = requests.get(url)

# translated = translator.translate(page.text)

# print(translated)