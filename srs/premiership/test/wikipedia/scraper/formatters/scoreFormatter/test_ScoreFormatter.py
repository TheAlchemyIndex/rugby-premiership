import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.ScoreFormatter import score_formatter

valid_score_string_1: str = "30 – 20"
valid_score_string_2: str = "20 – 30"
valid_score_string_3: str = "10 – 10"
valid_score_string_4: str = "30 – 20[j]"
valid_score_string_5: str = "[j]20 – 30"
valid_score_string_6: str = "10 [j]– 10"
valid_score_string_7: str = "30xXxa.e.t. – 20"
valid_score_string_8: str = "30 – 20xXxa.e.t."

invalid_score_string: str = "N/A"
invalid_score_type_int: int = 10
invalid_score_type_float: float = 1.0
invalid_score_type_bool: bool = True

valid_expected_formatted_score_1: dict[str, str] = {"team1Points": "30",
                                                    "team2Points": "20",
                                                    "totalPoints": "50",
                                                    "result": ["W", "L"],
                                                    "extraTime": "N"}

valid_expected_formatted_score_2: dict[str, str] = {"team1Points": "20",
                                                    "team2Points": "30",
                                                    "totalPoints": "50",
                                                    "result": ["L", "W"],
                                                    "extraTime": "N"}

valid_expected_formatted_score_3: dict[str, str] = {"team1Points": "10",
                                                    "team2Points": "10",
                                                    "totalPoints": "20",
                                                    "result": ["D", "D"],
                                                    "extraTime": "N"}

valid_expected_formatted_score_4: dict[str, str] = {"team1Points": "30",
                                                    "team2Points": "20",
                                                    "totalPoints": "50",
                                                    "result": ["W", "L"],
                                                    "extraTime": "Y"}

invalid_expected_formatted_score: dict[str, str] = {"team1Points": "N/A",
                                                    "team2Points": "N/A",
                                                    "totalPoints": "N/A",
                                                    "result": ["N/A", "N/A"],
                                                    "extraTime": "N/A"}


class ScoreFormatterTest(unittest.TestCase):

    def test_valid_score_string_1(self):
        self.assertEqual(
            score_formatter(valid_score_string_1), valid_expected_formatted_score_1
        )

    def test_valid_score_string_2(self):
        self.assertEqual(
            score_formatter(valid_score_string_2), valid_expected_formatted_score_2
        )

    def test_valid_score_string_3(self):
        self.assertEqual(
            score_formatter(valid_score_string_3), valid_expected_formatted_score_3
        )

    def test_valid_score_string_4(self):
        self.assertEqual(
            score_formatter(valid_score_string_4), valid_expected_formatted_score_1
        )

    def test_valid_score_string_5(self):
        self.assertEqual(
            score_formatter(valid_score_string_5), valid_expected_formatted_score_2
        )

    def test_valid_score_string_6(self):
        self.assertEqual(
            score_formatter(valid_score_string_6), valid_expected_formatted_score_3
        )

    def test_valid_score_string_7(self):
        self.assertEqual(
            score_formatter(valid_score_string_7), valid_expected_formatted_score_4
        )

    def test_valid_score_string_8(self):
        self.assertEqual(
            score_formatter(valid_score_string_7), valid_expected_formatted_score_4
        )

    def test_invalid_score_string(self):
        self.assertEqual(
            score_formatter(invalid_score_string), invalid_expected_formatted_score
        )

    def test_invalid_type_1(self):
        self.assertEqual(
            score_formatter(invalid_score_type_bool), invalid_expected_formatted_score
        )

    def test_invalid_type_2(self):
        self.assertEqual(
            score_formatter(invalid_score_type_int), invalid_expected_formatted_score
        )

    def test_invalid_type_3(self):
        self.assertEqual(
            score_formatter(invalid_score_type_float), invalid_expected_formatted_score
        )


if __name__ == '__main__':
    unittest.main()
