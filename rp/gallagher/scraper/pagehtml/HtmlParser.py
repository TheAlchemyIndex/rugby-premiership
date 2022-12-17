import requests
from bs4 import BeautifulSoup

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


# Function for extracting and parsing html from url
def parse(url):
    # Get data from url
    page = requests.get(url)
    # Parse html from webpage
    soup = BeautifulSoup(page.content, "html.parser", from_encoding="iso-8859-8")
    # Replaces br tags with custom string
    for br in soup('br'):
        br.replace_with(BR_REPLACE)
    # Gets div tags that match class of "vevent summary"
    divs = soup.find_all("div", {"class": "vevent summary"})

    return divs
