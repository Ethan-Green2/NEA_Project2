import requests

def get_wki_sum(topic, lang="en"):
    search_url = f"https://{lang}.wikipedia.org/w/api.php"

    search_param = {
        "action": "query",       # queryies wikipedias database
        "list": "search",        # uses wikipedias search engine
        "srsearch": topic,       # the search term entered by the user
        "format": "json"         # Request data in JSON format
    }

    search_response = requests.get(search_url, params=search_param).json() #sends the request to wikipedia and converts the response into JSON

    if not search_response["query"]["search"]:
        return None

    page_title = search_response["query"]["search"][0]["title"]

    summary_param = {
        "action": "query",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": page_title,
        "format": "json"
    }

    summary_response = requests.get(search_url, params=summary_param).json()
    page = next(iter(summary_response["query"]["pages"].values()))

    return {
        "title": page_title,
        "summary": page.get("extract", "No summary available")
    }