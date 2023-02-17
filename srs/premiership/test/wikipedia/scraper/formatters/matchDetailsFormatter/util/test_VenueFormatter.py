import unittest

from srs.premiership.main.wikipedia.scraper.formatters.matchDetailsFormatter.util.VenueFormatter import venue_formatter

valid_harlequins_venue_1: str = "Twickenham Stoop, London"
valid_harlequins_venue_2: str = "The Twickenham Stoop"
valid_harlequins_venue_3: str = "The Stoop"
valid_expected_harlequins_venue: str = "Twickenham Stoop"

valid_leicester_venue_1: str = "Mattioli Welford Road"
valid_leicester_venue_2: str = "Mattioli Woods Welford Road"
valid_leicester_venue_3: str = "Welford Road, Leicester"
valid_expected_leicester_venue: str = "Welford Road"

valid_northampton_venue_1: str = "cinch Stadium at Franklin's Gardens"
valid_northampton_venue_2: str = "Frankin's Gardens"
valid_northampton_venue_3: str = "Franklin’s Gardens"
valid_expected_northampton_venue: str = "Franklin's Gardens"

valid_twickenham_venue_1: str = "Twickenham, London"
valid_twickenham_venue_2: str = "Twickenham"
valid_expected_twickenham_venue: str = "Twickenham Stadium"

valid_kingsholm_venue: str = "Kingsholm Stadium"
valid_expected_kingsholm_venue: str = "Kingsholm"

valid_reebok_venue: str = "Reebok Stadium, Horwich"
valid_expected_reebok_venue: str = "Reebok Stadium"

valid_sixways_venue: str = "Sixways Stadium"
valid_expected_sixways_venue: str = "Sixways"

valid_mk_venue: str = "Stadium mk, Milton Keynes"
valid_expected_mk_venue: str = "Stadium mk"

valid_talen_venue: str = "Talen Energy Stadium, Philadelphia"
valid_expected_talen_venue: str = "Talen Energy Stadium"

valid_rec_venue: str = "The Rec"
valid_expected_rec_venue: str = "The Recreation Ground"

valid_test_venue: str = "Test Venue"
valid_expected_test_venue: str = "Test Venue"


class VenueFormatterTest(unittest.TestCase):

    def test_valid_harlequins_venue(self):
        self.assertEqual(
            venue_formatter(valid_harlequins_venue_1), valid_expected_harlequins_venue
        )
        self.assertEqual(
            venue_formatter(valid_harlequins_venue_2), valid_expected_harlequins_venue
        )
        self.assertEqual(
            venue_formatter(valid_harlequins_venue_3), valid_expected_harlequins_venue
        )

    def test_valid_leicester_venue(self):
        self.assertEqual(
            venue_formatter(valid_leicester_venue_1), valid_expected_leicester_venue
        )
        self.assertEqual(
            venue_formatter(valid_leicester_venue_2), valid_expected_leicester_venue
        )
        self.assertEqual(
            venue_formatter(valid_leicester_venue_3), valid_expected_leicester_venue
        )

    def test_valid_northampton_venue(self):
        self.assertEqual(
            venue_formatter(valid_northampton_venue_1), valid_expected_northampton_venue
        )
        self.assertEqual(
            venue_formatter(valid_northampton_venue_2), valid_expected_northampton_venue
        )
        self.assertEqual(
            venue_formatter(valid_northampton_venue_3), valid_expected_northampton_venue
        )

    def test_valid_twickenham_venue(self):
        self.assertEqual(
            venue_formatter(valid_twickenham_venue_1), valid_expected_twickenham_venue
        )
        self.assertEqual(
            venue_formatter(valid_twickenham_venue_2), valid_expected_twickenham_venue
        )

    def test_valid_kingsholm_venue(self):
        self.assertEqual(
            venue_formatter(valid_kingsholm_venue), valid_expected_kingsholm_venue
        )

    def test_valid_reebok_venue(self):
        self.assertEqual(
            venue_formatter(valid_reebok_venue), valid_expected_reebok_venue
        )

    def test_valid_sixways_venue(self):
        self.assertEqual(
            venue_formatter(valid_sixways_venue), valid_expected_sixways_venue
        )

    def test_valid_mk_venue(self):
        self.assertEqual(
            venue_formatter(valid_mk_venue), valid_expected_mk_venue
        )

    def test_valid_talen_venue(self):
        self.assertEqual(
            venue_formatter(valid_talen_venue), valid_expected_talen_venue
        )

    def test_valid_rec_venue(self):
        self.assertEqual(
            venue_formatter(valid_rec_venue), valid_expected_rec_venue
        )

    def test_valid_test_venue(self):
        self.assertEqual(
            venue_formatter(valid_test_venue), valid_expected_test_venue
        )


if __name__ == '__main__':
    unittest.main()
