import pathlib
import unittest

from bs4 import BeautifulSoup

from srs.premiership.main.wikipedia.scraper.pageHtml.util.DivFinder import get_divs

parent_path: str = str(pathlib.Path(__file__).resolve().parent.parent.parent.parent.parent)

valid_html_page: str = parent_path + "/resources/test_web_page.html"
with open(valid_html_page, 'r', encoding="utf8") as f:
    valid_html_opened = f.read()

valid_soup: BeautifulSoup = BeautifulSoup(valid_html_opened, "html.parser")

expected_div_tags: str = parent_path + "/resources/expected_div_tags.txt"
with open(expected_div_tags, 'r', encoding="utf8") as f:
    expected_div_tags_text = f.read()


class DivFinderTest(unittest.TestCase):

    def test_div_finder(self):
        self.assertEqual(
            str(get_divs(valid_soup, "vevent summary")), expected_div_tags_text
        )


if __name__ == '__main__':
    unittest.main()
