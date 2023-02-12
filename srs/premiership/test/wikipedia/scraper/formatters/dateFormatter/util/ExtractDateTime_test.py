import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.ExtractDateTime import extract_date_time

valid_string_splitter = "xXx"

valid_date_time_string_1 = "8 January 2021xXx19:45"
valid_date_time_string_2 = "8 January 2021xXx[j]19:45"

invalid_date_time_string_1 = "8 January 2021 19:45"

valid_expected_date_time_list_1 = ["8 January 2021", "19:45"]
invalid_expected_date_time_list_1 = ["8 January 2021xXx19:45", "N/A"]
invalid_expected_date_time_list_2 = ["8 January 2021 19:45", "N/A"]


class ExtractDateTimeTest(unittest.TestCase):

    def test_valid_date_time_string(self):
        self.assertEqual(
            extract_date_time(valid_date_time_string_1, valid_string_splitter), valid_expected_date_time_list_1
        )

    def test_valid_date_time_string_with_brackets(self):
        self.assertEqual(
            extract_date_time(valid_date_time_string_2, valid_string_splitter), valid_expected_date_time_list_1
        )

    def test_valid_date_time_string_with_invalid_splitter(self):
        self.assertEqual(
            extract_date_time(valid_date_time_string_2, "XXX"), invalid_expected_date_time_list_1
        )

    def test_invalid_date_time_string_with_no_splitter(self):
        self.assertEqual(
            extract_date_time(invalid_date_time_string_1, valid_string_splitter), invalid_expected_date_time_list_2
        )


if __name__ == '__main__':
    unittest.main()
