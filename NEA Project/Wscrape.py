import requests
from bs4 import BeautifulSoup

def scrape_wiki_sections(url):
    response = requests.get(url)
    response.raise_for_status #Used to check if the HTTP request for successful or not

    soup = BeautifulSoup(response.text, "html.parser")

    content_div = soup.find("div", {"id": "mw-content-text"})

    section = {}
    current_title = None
    current_content = []

    for element in content_div.find_all(["h2", "h3", "p1", "ul"]):
        #section headings
        if element.name in ["h2", "h3"]:
            if current_title and current_content:
                sections[current_title] = (current_content)