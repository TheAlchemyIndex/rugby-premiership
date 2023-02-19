import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.util.ExtractDropGoals import \
    extract_drop_goals

valid_scoring_data_string_1 = "Try: Sheedy 20' cxXxBradbury 60' cxXxCon: Sheedy (2/2) 21', 61'xXxPen: " \
                              "Sheedy (2/2) 10', 53'xXxDrop: Sheedy (1/1) 77'"
valid_scoring_data_string_2 = "Try: Sheedy 20' cxXxBradbury 60' cxXxCon: Sheedy (2/2) 21', 61'xXxPen: " \
                              "Sheedy (2/2) 10', 53'"
valid_scoring_data_string_3 = "Try: Sheedy 20' cxXxBradbury 60' cxXxCon: Sheedy (2/2) 21', 61'xXxPen: " \
                              "Sheedy (2/2) 10', 53'xXxDrop: Sheedy (2/2) 77', 79'"
valid_scoring_data_string_4 = "Pen: Sheedy (2/2) 10', 53'xXxDrop: Sheedy (1/1) 77'"
valid_scoring_data_string_5 = "Pen: Sheedy (2/2) 10', 53'"

valid_expected_drop_goals_1 = "1"
valid_expected_drop_goals_2 = "2"
valid_expected_drop_goals_3 = "0"


class ExtractDropGoalsTest(unittest.TestCase):

    def test_valid_scoring_data_string_1(self):
        self.assertEqual(
            extract_drop_goals(valid_scoring_data_string_1), valid_expected_drop_goals_1
        )

    def test_valid_scoring_data_string_2(self):
        self.assertEqual(
            extract_drop_goals(valid_scoring_data_string_2), valid_expected_drop_goals_3
        )

    def test_valid_scoring_data_string_3(self):
        self.assertEqual(
            extract_drop_goals(valid_scoring_data_string_3), valid_expected_drop_goals_2
        )

    def test_valid_scoring_data_string_4(self):
        self.assertEqual(
            extract_drop_goals(valid_scoring_data_string_4), valid_expected_drop_goals_1
        )

    def test_valid_scoring_data_string_5(self):
        self.assertEqual(
            extract_drop_goals(valid_scoring_data_string_5), valid_expected_drop_goals_3
        )


if __name__ == '__main__':
    unittest.main()
