import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.ScoringDataFormatter import \
    scoring_data_formatter

valid_scoring_data_string_1 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 73'xXxPen: J. Grayson (2/2) " \
                              "38', 61'"
valid_scoring_data_string_2 = "Try: G. McGuigan (2) 12' m, 58' cxXxRadwan 30' mxXxEarle 39' cxXxMulipola 65' " \
                              "cxXxCon: Connon (3/5) 40+1', 60', 66'"
valid_scoring_data_string_3 = "Pen: Sheedy (2/2) 10', 53'"
valid_scoring_data_string_4 = "Try: Sheedy 20' cxXxBradbury 60' cxXxCon: Sheedy (2/2) 21', 61'xXxPen: " \
                              "Sheedy (2/2) 10', 53'xXxDrop: Sheedy (1/1) 77'"

valid_expected_formatted_score_1: dict[str, str] = {"tries": "4",
                                                    "conversions": "3",
                                                    "penalties": "2",
                                                    "dropGoals": "0"}

valid_expected_formatted_score_2: dict[str, str] = {"tries": "5",
                                                    "conversions": "3",
                                                    "penalties": "0",
                                                    "dropGoals": "0"}

valid_expected_formatted_score_3: dict[str, str] = {"tries": "0",
                                                    "conversions": "0",
                                                    "penalties": "2",
                                                    "dropGoals": "0"}

valid_expected_formatted_score_4: dict[str, str] = {"tries": "2",
                                                    "conversions": "2",
                                                    "penalties": "2",
                                                    "dropGoals": "1"}


class MyTestCase(unittest.TestCase):

    def test_valid_scoring_data_string_1(self):
        self.assertEqual(
            scoring_data_formatter(valid_scoring_data_string_1), valid_expected_formatted_score_1
        )

    def test_valid_scoring_data_string_2(self):
        self.assertEqual(
            scoring_data_formatter(valid_scoring_data_string_2), valid_expected_formatted_score_2
        )

    def test_valid_scoring_data_string_3(self):
        self.assertEqual(
            scoring_data_formatter(valid_scoring_data_string_3), valid_expected_formatted_score_3
        )

    def test_valid_scoring_data_string_4(self):
        self.assertEqual(
            scoring_data_formatter(valid_scoring_data_string_4), valid_expected_formatted_score_4
        )


if __name__ == '__main__':
    unittest.main()
