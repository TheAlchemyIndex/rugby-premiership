import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.FormatScore import format_score

valid_score_string_1: str = "36 – 40"
valid_score_string_2: str = "36–40"
valid_score_string_3: str = "36-40"
valid_score_string_cancelled: str = "Cancelled"
valid_score_string_postponed_1: str = "P – P"
valid_score_string_postponed_2: str = "P–P"
valid_score_string_postponed_3: str = "P-P"
valid_score_string_upcoming: str = "v"
invalid_score_string_1: str = "test"
invalid_score_string_2: str = "N/A"

valid_expected_team1_score: str = "36"
valid_expected_team2_score: str = "40"
valid_expected_cancelled: str = "Cancelled"
valid_expected_postponed: str = "Postponed"
valid_expected_upcoming: str = "Upcoming"
invalid_expected_na: str = "N/A"


class FormatScoreTest(unittest.TestCase):

    def test_valid_score_string_1(self):
        actual_team1_score, actual_team2_score = format_score(valid_score_string_1)

        self.assertEqual(
            actual_team1_score, valid_expected_team1_score
        )
        self.assertEqual(
            actual_team2_score, valid_expected_team2_score
        )

    def test_valid_score_string_2(self):
        actual_team1_score, actual_team2_score = format_score(valid_score_string_2)

        self.assertEqual(
            actual_team1_score, valid_expected_team1_score
        )
        self.assertEqual(
            actual_team2_score, valid_expected_team2_score
        )

    def test_valid_score_string_3(self):
        actual_team1_score, actual_team2_score = format_score(valid_score_string_3)

        self.assertEqual(
            actual_team1_score, valid_expected_team1_score
        )
        self.assertEqual(
            actual_team2_score, valid_expected_team2_score
        )

    def test_valid_score_string_cancelled(self):
        actual_team1_score, actual_team2_score = format_score(valid_score_string_cancelled)

        self.assertEqual(
            actual_team1_score, valid_expected_cancelled
        )
        self.assertEqual(
            actual_team2_score, valid_expected_cancelled
        )

    def test_valid_score_string_postponed_1(self):
        actual_team1_score, actual_team2_score = format_score(valid_score_string_postponed_1)

        self.assertEqual(
            actual_team1_score, valid_expected_postponed
        )
        self.assertEqual(
            actual_team2_score, valid_expected_postponed
        )

    def test_valid_score_string_postponed_2(self):
        actual_team1_score, actual_team2_score = format_score(valid_score_string_postponed_2)

        self.assertEqual(
            actual_team1_score, valid_expected_postponed
        )
        self.assertEqual(
            actual_team2_score, valid_expected_postponed
        )

    def test_valid_score_string_postponed_3(self):
        actual_team1_score, actual_team2_score = format_score(valid_score_string_postponed_3)

        self.assertEqual(
            actual_team1_score, valid_expected_postponed
        )
        self.assertEqual(
            actual_team2_score, valid_expected_postponed
        )

    def test_valid_score_string_upcoming(self):
        actual_team1_score, actual_team2_score = format_score(valid_score_string_upcoming)

        self.assertEqual(
            actual_team1_score, valid_expected_upcoming
        )
        self.assertEqual(
            actual_team2_score, valid_expected_upcoming
        )

    def test_invalid_score_string_1(self):
        actual_team1_score, actual_team2_score = format_score(invalid_score_string_1)

        self.assertEqual(
            actual_team1_score, invalid_expected_na
        )
        self.assertEqual(
            actual_team2_score, invalid_expected_na
        )

    def test_invalid_score_string_2(self):
        actual_team1_score, actual_team2_score = format_score(invalid_score_string_2)

        self.assertEqual(
            actual_team1_score, invalid_expected_na
        )
        self.assertEqual(
            actual_team2_score, invalid_expected_na
        )


if __name__ == '__main__':
    unittest.main()
