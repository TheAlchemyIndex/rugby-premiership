from re import search

from srs.premiership.main.wikipedia.constants import StringSplitter
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.formatters.matchDetailsFormatter.util.VenueFormatter import venue_formatter


def match_details_formatter(match_details_data):
    """Extracts the venue and referee data and returns it as a key: value dictionary.

    :param match_details_data: Data about the match that was scraped from Wikipedia
    :return: A key: value dictionary of the venue and referee of the match
    """
    details_split = match_details_data.split(StringSplitter.BR_REPLACE)
    venue: str = venue_formatter(details_split[0])

    # Checks if the referee is included in match_data
    check_for_referee = list(filter(lambda v: search('^Referee', v), details_split))
    if len(check_for_referee) > 0:
        referee = check_for_referee[0].split("Referee: ")[1]
    else:
        referee = "Unknown"

    formatted_match_details = {OriginalColumns.VENUE: venue, OriginalColumns.REFEREE: referee}
    return formatted_match_details
