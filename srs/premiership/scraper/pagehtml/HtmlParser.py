import requests
from bs4 import BeautifulSoup

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


def parse(url):
    """Scrapes and parses html data from a url and returns div tags that match 'vevent summary'.

    :param url: The url to be scraped
    :return: A ResultSet of div tags
    """
    # Get data from url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser", from_encoding="iso-8859-8")

    # Replaces br tags with custom string
    for br in soup('br'):
        br.replace_with(BR_REPLACE)

    # Gets div tags that match class of "vevent summary"
    divs = soup.find_all("div", {"class": "vevent summary"})

    return divs
