import pathlib
import unittest

from bs4 import BeautifulSoup, ResultSet
from srs.premiership.main.wikipedia.scraper.pageHtml.TagExtractor import extract_tags

parent_path: str = str(pathlib.Path(__file__).resolve().parent.parent.parent.parent)

expected_div_tags: str = parent_path + "/resources/expected_div_tags.txt"
with open(expected_div_tags, 'r', encoding="utf8") as f:
    expected_div_tags_text = f.read()

valid_divs: ResultSet[str] = BeautifulSoup(expected_div_tags_text, "html.parser").find_all("div")

expected_extracted_tags_file: str = parent_path + "/resources/expected_match_data.txt"
with open(expected_extracted_tags_file, 'r', encoding="utf8") as f:
    expected_extracted_tags_text = f.read()


class TagExtractorTest(unittest.TestCase):

    def test_tag_extractor(self):
        self.assertEqual(
            str(extract_tags(valid_divs)), str(expected_extracted_tags_text)
        )


if __name__ == '__main__':
    unittest.main()
