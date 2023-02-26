from typing import Union

from bs4 import BeautifulSoup, PageElement


def replace_tags(soup: BeautifulSoup, target_tag: str, string_splitter: str) -> BeautifulSoup:
    """Replaces specified html tags in a BeautifulSoup object with a customer character string.

    :rtype: BeautifulSoup
    :param soup: BeautifulSoup object containing html
    :param target_tag: Html tags to be replaced
    :param string_splitter: Customer character string used to replace tags with
    :return: BeautifulSoup object with specified html tags replaced with a customer character string
    """
    tag: Union[PageElement, str]
    for tag in soup(target_tag):
        tag.replace_with(string_splitter)

    return soup
