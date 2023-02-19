import unittest

from srs.premiership.main.wikipedia.scraper.formatters.matchDetailsFormatter.util.ExtractMatchDetails import \
    extract_match_details

valid_match_details_string_1: str = "Sandy ParkxXxAttendance: 9,579xXxReferee: Christophe Ridley"
valid_expected_venue_1: str = "Sandy Park"
valid_expected_referee_1: str = "Christophe Ridley"

valid_match_details_string_2: str = "Ashton GatexXxReferee: Karl Dickson"
valid_expected_venue_2: str = "Ashton Gate"
valid_expected_referee_2: str = "Karl Dickson"

valid_match_details_string_3: str = "Sixways"
valid_expected_venue_3: str = "Sixways"
valid_expected_referee_3: str = "N/A"

valid_match_details_string_4: str = "StoneX StadiumxXxAttendance: 9,019"
valid_expected_venue_4: str = "StoneX Stadium"
valid_expected_referee_4: str = "N/A"

valid_string_splitter: str = "xXx"

invalid_string_splitter: str = "XXX"
invalid_expected_venue: str = "Sandy ParkxXxAttendance: 9,579xXxReferee: Christophe Ridley"
invalid_expected_referee: str = "N/A"


class ExtractMatchDetailsTest(unittest.TestCase):

    def test_valid_match_details_string_1(self):
        actual_venue_1, actual_referee_1 = extract_match_details(valid_match_details_string_1, valid_string_splitter)

        self.assertEqual(
            actual_venue_1, valid_expected_venue_1
        )
        self.assertEqual(
            actual_referee_1, valid_expected_referee_1
        )

    def test_valid_match_details_string_2(self):
        actual_venue_2, actual_referee_2 = extract_match_details(valid_match_details_string_2, valid_string_splitter)

        self.assertEqual(
            actual_venue_2, valid_expected_venue_2
        )
        self.assertEqual(
            actual_referee_2, valid_expected_referee_2
        )

    def test_valid_match_details_string_3(self):
        actual_venue_3, actual_referee_3 = extract_match_details(valid_match_details_string_3, valid_string_splitter)

        self.assertEqual(
            actual_venue_3, valid_expected_venue_3
        )
        self.assertEqual(
            actual_referee_3, valid_expected_referee_3
        )

    def test_valid_match_details_string_4(self):
        actual_venue_4, actual_referee_4 = extract_match_details(valid_match_details_string_4, valid_string_splitter)

        self.assertEqual(
            actual_venue_4, valid_expected_venue_4
        )
        self.assertEqual(
            actual_referee_4, valid_expected_referee_4
        )

    def test_invalid_string_splitter(self):
        actual_venue, actual_referee = extract_match_details(valid_match_details_string_1, invalid_string_splitter)

        self.assertEqual(
            actual_venue, invalid_expected_venue
        )
        self.assertEqual(
            actual_referee, invalid_expected_referee
        )


if __name__ == '__main__':
    unittest.main()
