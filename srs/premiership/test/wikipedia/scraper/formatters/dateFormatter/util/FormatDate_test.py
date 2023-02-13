import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.FormatDate import format_date

valid_unformatted_date_1: str = "8 January 2021"
expected_formatted_date_1: str = "08/Jan/2021"

valid_unformatted_date_missing_year_1: str = "19 June"
expected_formatted_date_missing_year_1: str = "19/Jun/2021"

valid_unformatted_date_missing_year_2: str = "26 June"
expected_formatted_date_missing_year_2: str = "26/Jun/2021"

invalid_unformatted_date_1: str = "8-January-2021"
invalid_unformatted_date_2: str = "8 January 2021xXx19:45"
invalid_unformatted_date_missing_year: str = "8 January"


class FormatDateTest(unittest.TestCase):

    def test_format_date_valid_date(self):
        self.assertEqual(
            format_date(valid_unformatted_date_1), expected_formatted_date_1
        )

    def test_format_date_valid_date_missing_year(self):
        self.assertEqual(
            format_date(valid_unformatted_date_missing_year_1), expected_formatted_date_missing_year_1
        )
        self.assertEqual(
            format_date(valid_unformatted_date_missing_year_2), expected_formatted_date_missing_year_2
        )

    def test_format_date_invalid_date(self):
        self.assertEqual(
            format_date(invalid_unformatted_date_1), "N/A"
        )
        self.assertEqual(
            format_date(invalid_unformatted_date_2), "N/A"
        )
        self.assertEqual(
            format_date(invalid_unformatted_date_missing_year), "N/A"
        )


if __name__ == '__main__':
    unittest.main()
