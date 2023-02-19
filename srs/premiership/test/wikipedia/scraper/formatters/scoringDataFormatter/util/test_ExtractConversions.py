import unittest

from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.util.ExtractConversions import \
    extract_conversions

valid_scoring_data_string_1 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxFurbank (1/1) 80+1'xXxPen: J. Grayson (2/2) " \
                              "38', 61'"
valid_scoring_data_string_2 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/3) 10', 56'xXxPen: J. Grayson (2/2) " \
                              "38', 61'"
valid_scoring_data_string_3 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/2) 10', 56'xXxPen: J. Grayson (2/2) 38', 61'"
valid_scoring_data_string_4 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72' " \
                              "cxXxCon: J. Grayson (2/2) 10', 56'"
valid_scoring_data_string_5 = "Try: Augustus 9' cxXxO. Sleightholme 52' mxXxMitchell 55' cxXxFurbank 72'"

valid_expected_conversions_1 = "3"
valid_expected_conversions_2 = "2"
valid_expected_conversions_3 = "0"


class ExtractConversionsTest(unittest.TestCase):

    def test_valid_scoring_data_string_1(self):
        self.assertEqual(
            extract_conversions(valid_scoring_data_string_1), valid_expected_conversions_1
        )

    def test_valid_scoring_data_string_2(self):
        self.assertEqual(
            extract_conversions(valid_scoring_data_string_2), valid_expected_conversions_2
        )

    def test_valid_scoring_data_string_3(self):
        self.assertEqual(
            extract_conversions(valid_scoring_data_string_3), valid_expected_conversions_2
        )

    def test_valid_scoring_data_string_4(self):
        self.assertEqual(
            extract_conversions(valid_scoring_data_string_4), valid_expected_conversions_2
        )

    def test_valid_scoring_data_string_5(self):
        self.assertEqual(
            extract_conversions(valid_scoring_data_string_5), valid_expected_conversions_3
        )


if __name__ == '__main__':
    unittest.main()
