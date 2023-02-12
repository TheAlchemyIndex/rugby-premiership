import requests
from bs4 import BeautifulSoup

from srs.premiership.main.wikipedia.constants import StringSplitter


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
        br.replace_with(StringSplitter.BR_REPLACE)

    # Gets div tags that match class of "vevent summary"
    divs = soup.find_all("div", {"class": "vevent summary"})

    return divs
