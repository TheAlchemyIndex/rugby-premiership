import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.CalculateResult import calculate_result

valid_team1_score_1 = "30"
valid_team2_score_1 = "20"

valid_team1_score_2 = "20"
valid_team2_score_2 = "30"

valid_team1_score_3 = "10"
valid_team2_score_3 = "10"

invalid_team1_score = "N/A"
invalid_team2_score = "N/A"

valid_expected_result_1 = "W"
valid_expected_result_flipped_1 = "L"
valid_expected_result_2 = "L"
valid_expected_result_flipped_2 = "W"
valid_expected_result_3 = "D"
valid_expected_result_flipped_3 = "D"
invalid_expected_result = "N/A"
invalid_expected_result_flipped = "N/A"


class MyTestCase(unittest.TestCase):

    def test_valid_calculate_result_1(self):
        actual_result, actual_result_flipped = calculate_result(valid_team1_score_1, valid_team2_score_1)

        self.assertEqual(
            actual_result, valid_expected_result_1
        )

        self.assertEqual(
            actual_result_flipped, valid_expected_result_flipped_1
        )

    def test_valid_calculate_result_2(self):
        actual_result, actual_result_flipped = calculate_result(valid_team1_score_2, valid_team2_score_2)

        self.assertEqual(
            actual_result, valid_expected_result_2
        )

        self.assertEqual(
            actual_result_flipped, valid_expected_result_flipped_2
        )

    def test_valid_calculate_result_3(self):
        actual_result, actual_result_flipped = calculate_result(valid_team1_score_3, valid_team2_score_3)

        self.assertEqual(
            actual_result, valid_expected_result_3
        )

        self.assertEqual(
            actual_result_flipped, valid_expected_result_flipped_3
        )

    def test_invalid_calculate_result(self):
        actual_result, actual_result_flipped = calculate_result(invalid_team1_score, invalid_team2_score)

        self.assertEqual(
            actual_result, invalid_expected_result
        )

        self.assertEqual(
            actual_result_flipped, invalid_expected_result
        )


if __name__ == '__main__':
    unittest.main()
