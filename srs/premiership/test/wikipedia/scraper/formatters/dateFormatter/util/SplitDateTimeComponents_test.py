import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.SplitDateTimeComponents import \
    split_date_time_components

valid_date: str = "08/Jan/2021"
valid_time: str = "19:45"
valid_url: str = "https://en.wikipedia.org/wiki/2020-21_Premiership_Rugby"

valid_expected_date_time_components: list[str] = ["19", "Fri", "Jan", "2021", "2020-21"]

invalid_date: str = "N/A"
invalid_time: str = "N/A"
invalid_url: str = "https://en.wikipedia.org/wiki/202021PremiershipRugby"

invalid_expected_date_time_components: list[str] = ["N/A", "N/A", "N/A", "N/A", "N/A"]


class SplitDateTimeComponentsTest(unittest.TestCase):

    def test_format_date_valid_components(self):
        self.assertEqual(
            split_date_time_components(valid_date, valid_time, valid_url), valid_expected_date_time_components
        )

    def test_format_date_invalid_components(self):
        self.assertEqual(
            split_date_time_components(invalid_date, invalid_time, invalid_url), invalid_expected_date_time_components
        )


if __name__ == '__main__':
    unittest.main()
