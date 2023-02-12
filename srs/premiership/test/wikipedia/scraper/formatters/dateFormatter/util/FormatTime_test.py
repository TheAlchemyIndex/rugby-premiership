import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.FormatTime import format_time

valid_unformatted_time_1 = "19.45"
valid_unformatted_time_2 = "19.45pm"
valid_unformatted_time_3 = "19:45pm"
valid_unformatted_time_4 = "07.45am"
valid_unformatted_time_5 = "07:45am"
valid_unformatted_time_6 = "7.45pm"
valid_unformatted_time_7 = "7:45pm"

invalid_unformatted_time_1 = "745"
invalid_unformatted_time_2 = "745pm"

expected_formatted_time_1 = "19:45"
expected_formatted_time_2 = "07:45"


class FormatTimeTest(unittest.TestCase):

    def test_format_time_valid_time(self):
        self.assertEqual(
            format_time(valid_unformatted_time_1), expected_formatted_time_1
        )

    def test_format_time_valid_time_with_am_pm_24(self):
        self.assertEqual(
            format_time(valid_unformatted_time_2), expected_formatted_time_1
        )
        self.assertEqual(
            format_time(valid_unformatted_time_3), expected_formatted_time_1
        )
        self.assertEqual(
            format_time(valid_unformatted_time_4), expected_formatted_time_2
        )
        self.assertEqual(
            format_time(valid_unformatted_time_5), expected_formatted_time_2
        )

    def test_format_time_valid_time_with_am_pm_12(self):
        self.assertEqual(
            format_time(valid_unformatted_time_6), expected_formatted_time_1
        )
        self.assertEqual(
            format_time(valid_unformatted_time_7), expected_formatted_time_1
        )

    def test_format_time_invalid_time(self):
        self.assertEqual(
            format_time(invalid_unformatted_time_1), "N/A"
        )
        self.assertEqual(
            format_time(invalid_unformatted_time_2), "N/A"
        )


if __name__ == '__main__':
    unittest.main()
