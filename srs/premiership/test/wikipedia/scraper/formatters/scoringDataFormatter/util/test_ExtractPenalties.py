import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.util.ExtractPenalties import \
    extract_penalties

valid_scoring_data_string_1 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 73'xXxPen: J. Grayson (2/2) " \
                              "38', 61'"
valid_scoring_data_string_2 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 73'xXxPen: J. Grayson (2/2) " \
                              "38', 61'xXxFurbank (2/2) 69', 77'"
valid_scoring_data_string_3 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 73'xXxPen: J. Grayson (1/2) " \
                              "38'xXxFurbank (1/2) 69'"
valid_scoring_data_string_4 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 73'"
valid_scoring_data_string_5 = "Pen: Sheedy (2/2) 10', 53'"
valid_scoring_data_string_6 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 73'xXxPen: Sheedy 43', 56'"

valid_expected_penalties_1 = "2"
valid_expected_penalties_2 = "4"
valid_expected_penalties_3 = "0"


class ExtractPenaltiesTest(unittest.TestCase):

    def test_valid_scoring_data_string_1(self):
        self.assertEqual(
            extract_penalties(valid_scoring_data_string_1), valid_expected_penalties_1
        )

    def test_valid_scoring_data_string_2(self):
        self.assertEqual(
            extract_penalties(valid_scoring_data_string_2), valid_expected_penalties_2
        )

    def test_valid_scoring_data_string_3(self):
        self.assertEqual(
            extract_penalties(valid_scoring_data_string_3), valid_expected_penalties_1
        )

    def test_valid_scoring_data_string_4(self):
        self.assertEqual(
            extract_penalties(valid_scoring_data_string_4), valid_expected_penalties_3
        )

    def test_valid_scoring_data_string_5(self):
        self.assertEqual(
            extract_penalties(valid_scoring_data_string_5), valid_expected_penalties_1
        )

    def test_valid_scoring_data_string_6(self):
        self.assertEqual(
            extract_penalties(valid_scoring_data_string_6), valid_expected_penalties_1
        )


if __name__ == '__main__':
    unittest.main()
