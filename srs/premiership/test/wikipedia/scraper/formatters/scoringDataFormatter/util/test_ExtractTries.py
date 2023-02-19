import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.util.ExtractTries import extract_tries

valid_scoring_data_string_1 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 73'xXxPen: J. Grayson (2/2) " \
                              "38', 61'"
valid_scoring_data_string_2 = "Try: G. McGuigan (2) 12' m, 58' cxXxRadwan 30' mxXxEarle 39' cxXxMulipola 65' " \
                              "cxXxCon: Connon (3/5) 40+1', 60', 66'"
valid_scoring_data_string_3 = "Try: Augustus 9' mxXxO. Sleightholme 52' mxXxMitchell 55' mxXxFurbank 72' " \
                              "mxXxPen: J. Grayson (2/2) 38', 61'"
valid_scoring_data_string_4 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 73'"
valid_scoring_data_string_5 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72'"
valid_scoring_data_string_6 = "Pen: Sheedy (2/2) 10', 53'"

valid_expected_tries_1 = "4"
valid_expected_tries_2 = "5"
valid_expected_tries_3 = "0"


class MyTestCase(unittest.TestCase):

    def test_valid_scoring_data_string_1(self):
        self.assertEqual(
            extract_tries(valid_scoring_data_string_1), valid_expected_tries_1
        )

    def test_valid_scoring_data_string_2(self):
        self.assertEqual(
            extract_tries(valid_scoring_data_string_2), valid_expected_tries_2
        )

    def test_valid_scoring_data_string_3(self):
        self.assertEqual(
            extract_tries(valid_scoring_data_string_3), valid_expected_tries_1
        )

    def test_valid_scoring_data_string_4(self):
        self.assertEqual(
            extract_tries(valid_scoring_data_string_4), valid_expected_tries_1
        )

    def test_valid_scoring_data_string_5(self):
        self.assertEqual(
            extract_tries(valid_scoring_data_string_5), valid_expected_tries_1
        )

    def test_valid_scoring_data_string_6(self):
        self.assertEqual(
            extract_tries(valid_scoring_data_string_6), valid_expected_tries_3
        )


if __name__ == '__main__':
    unittest.main()
