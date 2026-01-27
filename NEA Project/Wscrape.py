import requests
from bs4 import BeautifulSoup

def scrape_wiki_sections(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (WikipediaScraper/1.0; educational project)"
    }
     
    response = requests.get(url, headers=headers)
    response.raise_for_status() #Used to check if the HTTP request for successful or not
    # if not response.raise_for_status():
    #          raise ValueError("Wikipedia content not found")
    

    soup = BeautifulSoup(response.text, "html.parser")

    content_div = soup.find("div", {"id": "mw-content-text"}) #Finds the main content area of a Wikipedia page, everything meaningful like h1-3 headings and paragraphs is found there
    if not content_div:
        raise ValueError("Wikipedia content not found") #Appears to stop any confusing error messages into a clear one


    sections = {}
    current_title = None
    current_content = []

    for element in content_div.find_all(["h2", "h3", "p", "ul"]):
        #section headings
        if element.name in ["h2", "h3"]: #Detects any new headings
            if current_title and current_content:
                sections[current_title] = (current_content) = "\n".join(current_content) #Saves the previous section of the page and joins all paragraphs into readable string

            current_title = element.get_text().replace("[edit]", "").strip() # 
            current_content = []

        # Section content
        elif current_title:
            current_content.append(element.get_text()) #Add the paragraph or list text to the current section   

    # Saves last section
    if current_title and current_content:
        sections[current_title] = "\n".join(current_content)

    return sections
