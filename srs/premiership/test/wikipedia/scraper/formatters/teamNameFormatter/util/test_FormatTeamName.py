import unittest

from srs.premiership.main.wikipedia.scraper.formatters.teamNameFormatter.util.FormatTeamName import format_team_name

valid_unformatted_team_name_bath = "Bath Rugby"
valid_unformatted_team_name_bristol = "Bristol Bears"
valid_unformatted_team_name_exeter = "Exeter Chiefs"
valid_unformatted_team_name_leeds = "Leeds Carnegie"
valid_unformatted_team_name_leicester = "Leicester Tigers"
valid_unformatted_team_name_gloucester = "Gloucester Rugby"
valid_unformatted_team_name_newcastle = "Newcastle Falcons"
valid_unformatted_team_name_northampton = "Northampton Saints"
valid_unformatted_team_name_sale = "Sale Sharks"
valid_unformatted_team_name_wasps = "London Wasps"
valid_unformatted_team_name_worcester = "Worcester Warriors"
valid_unformatted_team_name_other = "Saracens"

valid_expected_team_name_bath = "Bath"
valid_expected_team_name_bristol = "Bristol"
valid_expected_team_name_exeter = "Exeter"
valid_expected_team_name_leeds = "Leeds"
valid_expected_team_name_leicester = "Leicester"
valid_expected_team_name_gloucester = "Gloucester"
valid_expected_team_name_newcastle = "Newcastle"
valid_expected_team_name_northampton = "Northampton"
valid_expected_team_name_sale = "Sale"
valid_expected_team_name_wasps = "Wasps"
valid_expected_team_name_worcester = "Worcester"
valid_expected_team_name_other = "Saracens"


class FormatTeamNameTest(unittest.TestCase):

    def test_valid_unformatted_team_name_bath(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_bath), valid_expected_team_name_bath
        )

    def test_valid_unformatted_team_name_bristol(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_bristol), valid_expected_team_name_bristol
        )

    def test_valid_unformatted_team_name_exeter(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_exeter), valid_expected_team_name_exeter
        )

    def test_valid_unformatted_team_name_leeds(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_leeds), valid_expected_team_name_leeds
        )

    def test_valid_unformatted_team_name_leicester(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_leicester), valid_expected_team_name_leicester
        )

    def test_valid_unformatted_team_name_gloucester(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_gloucester), valid_expected_team_name_gloucester
        )

    def test_valid_unformatted_team_name_newcastle(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_newcastle), valid_expected_team_name_newcastle
        )

    def test_valid_unformatted_team_name_northampton(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_northampton), valid_expected_team_name_northampton
        )

    def test_valid_unformatted_team_name_sale(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_sale), valid_expected_team_name_sale
        )

    def test_valid_unformatted_team_name_wasps(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_wasps), valid_expected_team_name_wasps
        )

    def test_valid_unformatted_team_name_worcester(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_worcester), valid_expected_team_name_worcester
        )

    def test_valid_unformatted_team_name_other(self):
        self.assertEqual(
            format_team_name(valid_unformatted_team_name_other), valid_expected_team_name_other
        )


if __name__ == '__main__':
    unittest.main()
