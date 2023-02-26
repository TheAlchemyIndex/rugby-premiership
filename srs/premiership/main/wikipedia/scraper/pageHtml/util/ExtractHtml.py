import requests
from bs4 import BeautifulSoup
from requests import Response


def extract_html(url: str) -> BeautifulSoup:
    """Extracts and parses html data from a url using BeautifulSoup.

    :rtype: BeautifulSoup
    :param url:
    :return: BeautifulSoup object containing parsed html data
    """
    page: Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser", from_encoding="iso-8859-8")

    return soup
