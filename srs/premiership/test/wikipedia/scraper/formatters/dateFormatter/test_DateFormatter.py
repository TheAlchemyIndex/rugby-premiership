import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.DateFormatter import date_formatter

valid_date_time_string_1: str = "8 January 2021xXx19:45"
valid_date_time_string_2: str = "8 January 2021xXx[j]19:45"
valid_url: str = "https://en.wikipedia.org/wiki/2020-21_Premiership_Rugby"

invalid_date_time_string: str = "8 January 2021XXX19:45"
invalid_url: str = "https://en.wikipedia.org/wiki/202021PremiershipRugby"
invalid_date_time_type_int: int = 10
invalid_date_time_type_float: float = 1.0
invalid_date_time_type_bool: bool = True

valid_expected_formatted_date: dict[str, str] = {"date": "08/Jan/2021",
                                                 "time": "19:45",
                                                 "hour": "19",
                                                 "day": "Fri",
                                                 "month": "Jan",
                                                 "year": "2021",
                                                 "season": "2020-21"}

invalid_expected_formatted_date: dict[str, str] = {"date": "N/A",
                                                   "time": "N/A",
                                                   "hour": "N/A",
                                                   "day": "N/A",
                                                   "month": "N/A",
                                                   "year": "N/A",
                                                   "season": "N/A"}

invalid_expected_formatted_date_valid_url: dict[str, str] = {"date": "N/A",
                                                             "time": "N/A",
                                                             "hour": "N/A",
                                                             "day": "N/A",
                                                             "month": "N/A",
                                                             "year": "N/A",
                                                             "season": "2020-21"}


class DateFormatterTest(unittest.TestCase):

    def test_valid_date_time_string(self):
        self.assertEqual(
            date_formatter(valid_date_time_string_1, valid_url), valid_expected_formatted_date
        )

    def test_valid_date_time_string_with_brackets(self):
        self.assertEqual(
            date_formatter(valid_date_time_string_2, valid_url), valid_expected_formatted_date
        )

    def test_invalid_date_time_string(self):
        self.assertEqual(
            date_formatter(invalid_date_time_string, invalid_url), invalid_expected_formatted_date
        )

    def test_invalid_date_time_type_int(self):
        self.assertEqual(
            date_formatter(invalid_date_time_type_int, invalid_url), invalid_expected_formatted_date
        )

    def test_invalid_date_time_type_int_valid_url(self):
        self.assertEqual(
            date_formatter(invalid_date_time_type_int, valid_url), invalid_expected_formatted_date_valid_url
        )

    def test_invalid_date_time_type_float(self):
        self.assertEqual(
            date_formatter(invalid_date_time_type_float, invalid_url), invalid_expected_formatted_date
        )

    def test_invalid_date_time_type_float_valid_url(self):
        self.assertEqual(
            date_formatter(invalid_date_time_type_float, valid_url), invalid_expected_formatted_date_valid_url
        )

    def test_invalid_date_time_type_bool(self):
        self.assertEqual(
            date_formatter(invalid_date_time_type_bool, invalid_url), invalid_expected_formatted_date
        )

    def test_invalid_date_time_type_bool_valid_url(self):
        self.assertEqual(
            date_formatter(invalid_date_time_type_bool, valid_url), invalid_expected_formatted_date_valid_url
        )


if __name__ == '__main__':
    unittest.main()
