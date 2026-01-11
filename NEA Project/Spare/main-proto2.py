import streamlit as st
import gettext
import os

# --- Setup ---

# Languages your app supports
LANGUAGES = {
    'en': 'English',
    'de': 'German',
    'es': 'Spanish',
    'ja': 'Japanese',
    'ru': 'Russian'
}

# Create a directory for your translations (e.g. locales/)
LOCALE_DIR = os.path.join(os.path.dirname(__file__), 'locales')

# Sidebar language selector
st.sidebar.title("Settings")
language_code = st.sidebar.selectbox(
    "Select language",
    options=list(LANGUAGES.keys()),
    format_func=lambda k: f"{LANGUAGES[k]} ({k})"
)

# --- Initialize gettext translation ---
try:
    translation = gettext.translation(
        'messages', localedir=LOCALE_DIR, languages=[language_code]
    )
    translation.install()
    _ = translation.gettext
except FileNotFoundError:
    # Fallback to English if translation not found
    gettext.install('messages')
    _ = gettext.gettext

# --- Streamlit UI using gettext shorthand `_()` ---

st.title(_("AI WebCrawler"))
url = st.text_input(_("Enter a website URL:"))

if st.button(_("Scrape Site")):
    st.write(_("Scraping the website..."))

if st.button(_("Enter a Topic to Scrape")):
    st.write(_("Scraping Topic"))