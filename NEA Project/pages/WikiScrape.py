import streamlit as st
from Wscrape import scrape_wiki_sections
from deep_translator import GoogleTranslator

# Optional Languages
LANGUAGES = {
    'en': 'English',
    'af': 'Afrikaans',
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
st.title("Wikipedia Scraper")

topic = st.text_input("Enter a Wikipedia topic:")

if st.button("Scrape Wikipedia"):
    if topic:
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}" #Converts inputted topic as a valid URL for wikipedia
        st.write(f"Scraping: {url}")

        # Display preview or process it further
        sections = scrape_wiki_sections(url)

        selected_section = st.selectbox(
        "Select a section",
        list(sections.keys())
        )

        st.subheader(selected_section)
        st.write(t(sections[selected_section]))
