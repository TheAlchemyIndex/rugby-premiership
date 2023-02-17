import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.CalculateTotalScore import \
    calculate_total_score

valid_team1_score = "30"
valid_team2_score = "20"

invalid_team1_score = "N/A"
invalid_team2_score = "N/A"

valid_expected_total_score = "50"
invalid_expected_total_score = "N/A"


class CalculateTotalScoreTest(unittest.TestCase):

    def test_valid_calculate_total_score(self):
        self.assertEqual(
            calculate_total_score(valid_team1_score, valid_team2_score), valid_expected_total_score
        )

    def test_invalid_calculate_total_score(self):
        self.assertEqual(
            calculate_total_score(invalid_team1_score, invalid_team2_score), invalid_expected_total_score
        )


if __name__ == '__main__':
    unittest.main()
