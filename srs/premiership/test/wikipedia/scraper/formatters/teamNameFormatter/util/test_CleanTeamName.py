import unittest

from srs.premiership.main.wikipedia.scraper.formatters.teamNameFormatter.util.CleanTeamName import clean_team_name

valid_unclean_team_name_1 = "(1 BP) London Irish"
valid_unclean_team_name_2 = "(2 BPs) London Irish"
valid_unclean_team_name_3 = "London Irish (1 BP)"
valid_unclean_team_name_4 = "London Irish (2 BPs)"

valid_expected_team_name = "London Irish"

invalid_type_1 = 10
invalid_type_2 = 10.0
invalid_type_3 = True


class CleanTeamNameTest(unittest.TestCase):

    def test_valid_unclean_team_name_1(self):
        self.assertEqual(
            clean_team_name(valid_unclean_team_name_1), valid_expected_team_name
        )

    def test_valid_unclean_team_name_2(self):
        self.assertEqual(
            clean_team_name(valid_unclean_team_name_2), valid_expected_team_name
        )

    def test_valid_unclean_team_name_3(self):
        self.assertEqual(
            clean_team_name(valid_unclean_team_name_3), valid_expected_team_name
        )

    def test_valid_unclean_team_name_4(self):
        self.assertEqual(
            clean_team_name(valid_unclean_team_name_4), valid_expected_team_name
        )

    def test_invalid_types(self):
        self.assertEqual(
            clean_team_name(invalid_type_1), "N/A"
        )
        self.assertEqual(
            clean_team_name(invalid_type_2), "N/A"
        )
        self.assertEqual(
            clean_team_name(invalid_type_3), "N/A"
        )


if __name__ == '__main__':
    unittest.main()
