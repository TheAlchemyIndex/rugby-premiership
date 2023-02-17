import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.FormatExtraTime import format_extra_time

valid_team1_score_1: str = "30xXxa.e.t."
valid_team1_score_2: str = "30"
valid_expected_team1_score: str = "30"
invalid_team1_score: str = "N/A"

valid_team2_score_1: str = "20xXxa.e.t."
valid_team2_score_2: str = "20"
valid_expected_team2_score: str = "20"
invalid_team2_score: str = "N/A"

valid_expected_extra_time_status_1 = "Y"
valid_expected_extra_time_status_2 = "N"

valid_string_splitter: str = "xXx"
invalid_string_splitter: str = "XXX"
invalid_expected_na: str = "N/A"


class FormatExtraTimeTest(unittest.TestCase):

    def test_valid_score_strings_with_et_tags(self):
        actual_team1_score, actual_team2_score, actual_extra_time_status = format_extra_time(valid_team1_score_1,
                                                                                             valid_team2_score_1,
                                                                                             valid_string_splitter)

        self.assertEqual(
            actual_team1_score, valid_expected_team1_score
        )

        self.assertEqual(
            actual_team2_score, valid_expected_team2_score
        )

        self.assertEqual(
            actual_extra_time_status, valid_expected_extra_time_status_1
        )

    def test_valid_score_strings_without_et_tags(self):
        actual_team1_score, actual_team2_score, actual_extra_time_status = format_extra_time(valid_team1_score_2,
                                                                                             valid_team2_score_2,
                                                                                             valid_string_splitter)

        self.assertEqual(
            actual_team1_score, valid_expected_team1_score
        )

        self.assertEqual(
            actual_team2_score, valid_expected_team2_score
        )

        self.assertEqual(
            actual_extra_time_status, valid_expected_extra_time_status_2
        )

    def test_invalid_score_strings_both_teams_na(self):
        actual_team1_score, actual_team2_score, actual_extra_time_status = format_extra_time(invalid_team1_score,
                                                                                             invalid_team2_score,
                                                                                             valid_string_splitter)

        self.assertEqual(
            actual_team1_score, invalid_expected_na
        )

        self.assertEqual(
            actual_team2_score, invalid_expected_na
        )

        self.assertEqual(
            actual_extra_time_status, invalid_expected_na
        )

    def test_invalid_score_strings_team1_na(self):
        actual_team1_score, actual_team2_score, actual_extra_time_status = format_extra_time(invalid_team1_score,
                                                                                             valid_team2_score_1,
                                                                                             valid_string_splitter)

        self.assertEqual(
            actual_team1_score, invalid_expected_na
        )

        self.assertEqual(
            actual_team2_score, invalid_expected_na
        )

        self.assertEqual(
            actual_extra_time_status, invalid_expected_na
        )

    def test_invalid_score_strings_team2_na(self):
        actual_team1_score, actual_team2_score, actual_extra_time_status = format_extra_time(valid_team1_score_1,
                                                                                             invalid_team2_score,
                                                                                             valid_string_splitter)

        self.assertEqual(
            actual_team1_score, invalid_expected_na
        )

        self.assertEqual(
            actual_team2_score, invalid_expected_na
        )

        self.assertEqual(
            actual_extra_time_status, invalid_expected_na
        )

    def test_invalid_string_splitter(self):
        actual_team1_score, actual_team2_score, actual_extra_time_status = format_extra_time(valid_team1_score_1,
                                                                                             valid_team2_score_1,
                                                                                             invalid_string_splitter)

        self.assertEqual(
            actual_team1_score, invalid_expected_na
        )

        self.assertEqual(
            actual_team2_score, invalid_expected_na
        )

        self.assertEqual(
            actual_extra_time_status, invalid_expected_na
        )


if __name__ == '__main__':
    unittest.main()
