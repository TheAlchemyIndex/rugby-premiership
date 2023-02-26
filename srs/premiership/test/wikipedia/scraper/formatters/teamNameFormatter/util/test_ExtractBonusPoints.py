import unittest

from srs.premiership.main.wikipedia.scraper.formatters.teamNameFormatter.util.ExtractBonusPoints import \
    extract_bonus_points

valid_bp_string_1 = "(1 BP) London Irish"
valid_bp_string_2 = "(2 BPs) London Irish"
valid_bp_string_3 = "London Irish (1 BP)"
valid_bp_string_4 = "London Irish (2 BPs)"
valid_bp_string_5 = "London Irish"

valid_expected_bps_1 = "1"
valid_expected_bps_2 = "2"
valid_expected_bps_3 = "0"


class ExtractBonusPointsTest(unittest.TestCase):

    def test_valid_bp_string_1(self):
        self.assertEqual(
            extract_bonus_points(valid_bp_string_1), valid_expected_bps_1
        )

    def test_valid_bp_string_2(self):
        self.assertEqual(
            extract_bonus_points(valid_bp_string_2), valid_expected_bps_2
        )

    def test_valid_bp_string_3(self):
        self.assertEqual(
            extract_bonus_points(valid_bp_string_3), valid_expected_bps_1
        )

    def test_valid_bp_string_4(self):
        self.assertEqual(
            extract_bonus_points(valid_bp_string_4), valid_expected_bps_2
        )

    def test_valid_bp_string_5(self):
        self.assertEqual(
            extract_bonus_points(valid_bp_string_5), valid_expected_bps_3
        )


if __name__ == '__main__':
    unittest.main()
