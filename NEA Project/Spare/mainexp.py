import streamlit as st
from deep_translator import GoogleTranslator
from scrape import scrape_website
# Optional Languages
LANGUAGES = {
    'af': 'Afrikaans',
    'en': 'English',
    'de': 'German',
    'ja': 'Japanese',
    'ru': 'Russian',
    'es': 'Spanish',
    'fr': 'French'
}
# Sidebar UI
st.sidebar.title("Settings")
language_code = st.sidebar.selectbox(
    "Select language",
    list(LANGUAGES.keys()),
    format_func=lambda k: f"{LANGUAGES[k]} ({k})"
)

# Cache translator to speed up repeated use
@st.cache_resource

def get_translator(target_lang):
    return GoogleTranslator(source='auto', target=target_lang)

def translate_text(text: str, dest: str) -> str:
    # Translate string using deep-translator
    if not text or dest == 'en':
        return text
    try:
        translator = get_translator(dest)
        return translator.translate(text)
    except Exception as e:
        st.sidebar.error(f"Translation failed: {e}")
        return text

# cleaner UI code
t = lambda s: translate_text(s, language_code)

# Page UI
st.title(t("AI WebCrawler"))
url = st.text_input(t("Enter a website URL:"))

if st.button(t("Scrape Site")):
    st.write(t("Scraping the website..."))
    result = scrape_website(url)
    print(result)

if st.button(t("Enter a Topic to Scrape")):
    st.write(t("Scraping Topic"))





