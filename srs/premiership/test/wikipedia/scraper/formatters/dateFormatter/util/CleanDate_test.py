import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.CleanDate import clean_date

valid_date_time_string_1: str = "8 January 2021xXx[j]19:45"
valid_date_time_string_2: str = "[j]8 January 2021xXx19:45"
valid_date_time_string_3: str = "8 January 2021xXx19:45[j]"
valid_expected_cleaned_date_time_string: str = "8 January 2021xXx19:45"

invalid_date_time_type_int: int = 10
invalid_date_time_type_float: float = 1.0
invalid_date_time_type_bool: bool = True


class CleanDateTest(unittest.TestCase):

    def test_valid_date_time_string_1(self):
        self.assertEqual(
            clean_date(valid_date_time_string_1), valid_expected_cleaned_date_time_string
        )

    def test_valid_date_time_string_2(self):
        self.assertEqual(
            clean_date(valid_date_time_string_2), valid_expected_cleaned_date_time_string
        )

    def test_valid_date_time_string_3(self):
        self.assertEqual(
            clean_date(valid_date_time_string_3), valid_expected_cleaned_date_time_string
        )

    def test_invalid_date_time_type_int(self):
        self.assertEqual(
            clean_date(invalid_date_time_type_int), "N/A"
        )

    def test_invalid_date_time_type_float(self):
        self.assertEqual(
            clean_date(invalid_date_time_type_float), "N/A"
        )

    def test_invalid_date_time_type_bool(self):
        self.assertEqual(
            clean_date(invalid_date_time_type_bool), "N/A"
        )


if __name__ == '__main__':
    unittest.main()
