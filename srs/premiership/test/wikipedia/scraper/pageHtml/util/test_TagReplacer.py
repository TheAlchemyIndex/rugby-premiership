import pathlib
import unittest

from bs4 import BeautifulSoup

from srs.premiership.main.wikipedia.scraper.pageHtml.util.TagReplacer import replace_tags

parent_path: str = str(pathlib.Path(__file__).resolve().parent.parent.parent.parent.parent)

valid_html_page: str = parent_path + "/resources/test_web_page.html"
with open(valid_html_page, 'r', encoding="utf8") as f:
    expected_html_opened = f.read()

valid_soup: BeautifulSoup = BeautifulSoup(expected_html_opened, "html.parser")

expected_tag_replace_html_page: str = parent_path + "/resources/expected_tag_replace.html"
with open(expected_tag_replace_html_page, 'r', encoding="utf8") as f:
    expected_html_opened = f.read()

expected_soup: BeautifulSoup = BeautifulSoup(expected_html_opened, "html.parser")

valid_target_tag = "br"
valid_string_splitter = "xXx"


class TagReplacerTest(unittest.TestCase):

    def test_tag_replacer(self):
        self.assertEqual(
            str(replace_tags(valid_soup, valid_target_tag, valid_string_splitter)), str(expected_soup)
        )


if __name__ == '__main__':
    unittest.main()
