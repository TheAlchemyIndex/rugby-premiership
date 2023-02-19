import unittest

from srs.premiership.main.wikipedia.scraper.formatters.matchDetailsFormatter.MatchDetailsFormatter import \
    match_details_formatter

valid_match_details_string_1 = "Mattioli Welford RoadxXxAttendance: 9,579xXxReferee: Christophe Ridley"
valid_match_details_string_2 = "Mattioli Welford RoadxXxReferee: Christophe Ridley"
valid_match_details_string_3 = "Mattioli Welford Road"
valid_match_details_string_4 = "Mattioli Welford RoadxXxAttendance: 9,019"

valid_expected_formatted_match_details_1: dict[str, str] = {"venue": "Welford Road",
                                                            "referee": "Christophe Ridley"}

valid_expected_formatted_match_details_2: dict[str, str] = {"venue": "Welford Road",
                                                            "referee": "N/A"}


class MyTestCase(unittest.TestCase):

    def test_valid_match_details_string_1(self):
        self.assertEqual(
            match_details_formatter(valid_match_details_string_1), valid_expected_formatted_match_details_1
        )

    def test_valid_match_details_string_2(self):
        self.assertEqual(
            match_details_formatter(valid_match_details_string_2), valid_expected_formatted_match_details_1
        )

    def test_valid_match_details_string_3(self):
        self.assertEqual(
            match_details_formatter(valid_match_details_string_3), valid_expected_formatted_match_details_2
        )

    def test_valid_match_details_string_4(self):
        self.assertEqual(
            match_details_formatter(valid_match_details_string_4), valid_expected_formatted_match_details_2
        )


if __name__ == '__main__':
    unittest.main()
