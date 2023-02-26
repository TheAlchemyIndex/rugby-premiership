from bs4 import BeautifulSoup, ResultSet


def get_divs(soup: BeautifulSoup, class_name: str) -> ResultSet[str]:
    """Returns collection of div tags that match a specified div class name.

    :rtype: ResultSet[str]
    :param soup: BeautifulSoup object to extract div tags from
    :param class_name: Class name of the div tags to extract
    :return: ResultSet[str] of div tags that match a specified class name
    """
    return soup.find_all("div", {"class": class_name})
