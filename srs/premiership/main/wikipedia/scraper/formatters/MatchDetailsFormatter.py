from re import search

from srs.premiership.main.wikipedia.constants import StringSplitter
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.constants.matchData import Venues

# Constant list values representing various venue strings that require reformatting
HARLEQUINS_STADIUM = ["Twickenham Stoop, London", "The Twickenham Stoop", "The Stoop"]
LEICESTER_STADIUM = ["Mattioli Welford Road", "Mattioli Woods Welford Road", "Welford Road, Leicester"]
NORTHAMPTON_STADIUM = ["cinch Stadium at Franklin's Gardens", "Frankin's Gardens", "Franklin’s Gardens"]
TWICKENHAM = ["Twickenham, London", "Twickenham"]


def match_details_formatter(match_details_data):
    """Extracts the venue and referee data and returns it as a key: value dictionary.

    :param match_details_data: Data about the match that was scraped from Wikipedia
    :return: A key: value dictionary of the venue and referee of the match
    """
    details_split = match_details_data.split(StringSplitter.BR_REPLACE)
    venue = venue_formatter(details_split[0])

    # Checks if the referee is included in match_data
    check_for_referee = list(filter(lambda v: search('^Referee', v), details_split))
    if len(check_for_referee) > 0:
        referee = check_for_referee[0].split("Referee: ")[1]
    else:
        referee = "Unknown"

    formatted_match_details = {OriginalColumns.VENUE: venue, OriginalColumns.REFEREE: referee}
    return formatted_match_details


def venue_formatter(venue):
    """Formats and returns a string value representing the venue.

    :param venue: The original venue string scraped from Wikipedia
    :return: The formatted string for the venue
    """
    if venue in HARLEQUINS_STADIUM:
        return Venues.TWICKENHAM_STOOP
    elif venue in NORTHAMPTON_STADIUM:
        return Venues.FRANKLINS_GARDENS
    elif venue in LEICESTER_STADIUM:
        return Venues.WELFORD_ROAD
    elif venue in TWICKENHAM:
        return Venues.TWICKENHAM_STADIUM
    elif venue == "Kingsholm Stadium":
        return Venues.KINGSHOLM
    elif venue == "Reebok Stadium, Horwich":
        return Venues.REEBOK_STADIUM
    elif venue == "Sixways Stadium":
        return Venues.SIXWAYS
    elif venue == "Stadium mk, Milton Keynes":
        return Venues.STADIUM_MK
    elif venue == "Talen Energy Stadium, Philadelphia":
        return Venues.TALEN_ENERGY_STADIUM
    elif venue == "The Rec":
        return Venues.THE_RECREATION_GROUND
    else:
        return venue
