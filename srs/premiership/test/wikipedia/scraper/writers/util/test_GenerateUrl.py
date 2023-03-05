import unittest

from srs.premiership.main.wikipedia.scraper.writers.util.GenerateUrl import generate_url

valid_season_start = "2021"
valid_season_end = "22"
expected_valid_url = "https://en.wikipedia.org/wiki/2021-22_Premiership_Rugby"

invalid_season_start_greater_than = "2023"
invalid_season_start_equal_to = "2022"
expected_exception_message_greater_than = "Starting year of the season should not be greater than or equal " \
                                          "to the end year of the season.\nThe value of season_start was: " \
                                          "2023\nThe value of season_end was: 22"
expected_exception_message_equal_to = "Starting year of the season should not be greater than or equal to " \
                                      "the end year of the season.\nThe value of season_start was: 2022\n" \
                                      "The value of season_end was: 22"

invalid_season_start_larger_gap = "2020"
expected_exception_message_larger_gap = "The difference between the starting year of the season and the end " \
                                        "year of the season should not be greater than 1 year.\nThe value of " \
                                        "season_start was: 2020\nThe value of season_end was: 22"


class GenerateUrlTest(unittest.TestCase):
    def test_valid_season_data(self):
        self.assertEqual(
            generate_url(valid_season_start, valid_season_end), expected_valid_url
        )

    def test_invalid_season_data_greater_than(self):
        with self.assertRaises(Exception) as e:
            generate_url(invalid_season_start_greater_than, valid_season_end)
        self.assertEqual(str(e.exception), expected_exception_message_greater_than)

    def test_invalid_season_data_equal_to(self):
        with self.assertRaises(Exception) as e:
            generate_url(invalid_season_start_equal_to, valid_season_end)
        self.assertEqual(str(e.exception), expected_exception_message_equal_to)

    def test_invalid_season_data_larger_gap(self):
        with self.assertRaises(Exception) as e:
            generate_url(invalid_season_start_larger_gap, valid_season_end)
        self.assertEqual(str(e.exception), expected_exception_message_larger_gap)


if __name__ == '__main__':
    unittest.main()
