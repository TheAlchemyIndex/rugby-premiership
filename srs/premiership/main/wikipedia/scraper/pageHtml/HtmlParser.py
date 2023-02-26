from bs4 import BeautifulSoup, ResultSet

from srs.premiership.main.wikipedia.constants import StringSplitter
from srs.premiership.main.wikipedia.scraper.pageHtml.util import TagReplacer, DivFinder
from srs.premiership.main.wikipedia.scraper.pageHtml.util.ExtractHtml import extract_html


def parse(url: str) -> ResultSet[str]:
    """Scrapes and parses html data from a url and returns div tags that match 'vevent summary'.

    :param url: The url to be scraped
    :return: A ResultSet of div tags
    """
    # Get html data from url
    soup = extract_html(url)

    # Replaces br tags with a custom character string
    soup_br_replaced: BeautifulSoup = TagReplacer.replace_tags(soup, "br", StringSplitter.BR_REPLACE)

    # Gets div tags that match class of "vevent summary"
    divs: ResultSet[str] = DivFinder.get_divs(soup_br_replaced, "vevent summary")
    print(divs)

    return divs
