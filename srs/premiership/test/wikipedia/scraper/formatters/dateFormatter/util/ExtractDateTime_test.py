import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.ExtractDateTime import extract_date_time

valid_string_splitter: str = "xXx"

valid_date_time_string: str = "8 January 2021xXx19:45"
valid_expected_date_time_list: list[str] = ["8 January 2021", "19:45"]

invalid_date_time_string: str = "8 January 2021 19:45"
invalid_expected_date_time_list_1: list[str] = ["8 January 2021xXx19:45", "N/A"]
invalid_expected_date_time_list_2: list[str] = ["8 January 2021 19:45", "N/A"]


class ExtractDateTimeTest(unittest.TestCase):

    def test_valid_date_time_string(self):
        self.assertEqual(
            extract_date_time(valid_date_time_string, valid_string_splitter), valid_expected_date_time_list
        )

    def test_valid_date_time_string_with_invalid_splitter(self):
        self.assertEqual(
            extract_date_time(valid_date_time_string, "XXX"), invalid_expected_date_time_list_1
        )

    def test_invalid_date_time_string_with_no_splitter(self):
        self.assertEqual(
            extract_date_time(invalid_date_time_string, valid_string_splitter), invalid_expected_date_time_list_2
        )


if __name__ == '__main__':
    unittest.main()
