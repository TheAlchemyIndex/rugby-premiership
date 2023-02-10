import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.FormatDate import format_date

valid_unformatted_date_1 = "10 January 2023"
expected_formatted_date_1 = "10/Jan/2023"

valid_unformatted_date_missing_year_1 = "19 June"
expected_formatted_date_missing_year_1 = "19/Jun/2021"

valid_unformatted_date_missing_year_2 = "26 June"
expected_formatted_date_missing_year_2 = "26/Jun/2021"

invalid_unformatted_date = "18-June-2021"
invalid_unformatted_date_missing_year = "10 June"


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
            format_date(invalid_unformatted_date), "N/A"
        )
        self.assertEqual(
            format_date(invalid_unformatted_date_missing_year), "N/A"
        )


if __name__ == '__main__':
    unittest.main()
