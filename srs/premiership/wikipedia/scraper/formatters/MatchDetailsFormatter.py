from re import search
from srs.premiership.wikipedia.constants import OriginalColumns

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"

# Constant list values representing various venue strings that require reformatting
HARLEQUINS_STADIUM = ["Twickenham Stoop, London", "The Twickenham Stoop", "The Stoop"]
LEICESTER_STADIUM = ["Mattioli Welford Road", "Mattioli Woods Welford Road", "Welford Road, Leicester"]
NORTHAMPTON_STADIUM = ["cinch Stadium at Franklin's Gardens", "Frankin's Gardens", "Franklin’s Gardens"]
TWICKENHAM_STADIUM = ["Twickenham, London", "Twickenham"]


def match_details_formatter(match_details_data):
    """Extracts the venue and referee data and returns it as a key: value dictionary.

    :param match_details_data: Data about the match that was scraped from Wikipedia
    :return: A key: value dictionary of the venue and referee of the match
    """
    details_split = match_details_data.split(BR_REPLACE)
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
        return "Twickenham Stoop"
    elif venue in NORTHAMPTON_STADIUM:
        return "Franklin's Gardens"
    elif venue in LEICESTER_STADIUM:
        return "Welford Road"
    elif venue in TWICKENHAM_STADIUM:
        return "Twickenham Stadium"
    elif venue == "Kingsholm Stadium":
        return "Kingsholm"
    elif venue == "Reebok Stadium, Horwich":
        return "Reebok Stadium"
    elif venue == "Sixways Stadium":
        return "Sixways"
    elif venue == "Stadium mk, Milton Keynes":
        return "Stadium mk"
    elif venue == "Talen Energy Stadium, Philadelphia":
        return "Talen Energy Stadium"
    elif venue == "The Rec":
        return "The Recreation Ground"
    else:
        return venue
