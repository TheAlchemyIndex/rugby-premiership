from srs.premiership.main.wikipedia.constants import StringSplitter
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.formatters.matchDetailsFormatter.util.ExtractMatchDetails import \
    extract_match_details
from srs.premiership.main.wikipedia.scraper.formatters.matchDetailsFormatter.util.VenueFormatter import venue_formatter


def match_details_formatter(match_details_data: str):
    """Extracts the venue and referee data and returns it as a key: value dictionary.

    :param match_details_data: Data about the match that was scraped from Wikipedia
    :return: A key: value dictionary of the venue and referee of the match
    """
    venue_unformatted: str
    referee: str
    venue_unformatted, referee = extract_match_details(match_details_data, StringSplitter.BR_REPLACE)

    # Cleans and formats match venue
    venue: str = venue_formatter(venue_unformatted)

    formatted_match_details = {OriginalColumns.VENUE: venue, OriginalColumns.REFEREE: referee}

    return formatted_match_details
