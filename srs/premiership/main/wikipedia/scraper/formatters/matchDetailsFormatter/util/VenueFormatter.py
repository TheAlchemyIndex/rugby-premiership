from srs.premiership.main.wikipedia.constants.matchData import Venues

# Constant list values representing various venue strings that require reformatting
HARLEQUINS_STADIUM: list[str] = ["Twickenham Stoop, London", "The Twickenham Stoop", "The Stoop"]
LEICESTER_STADIUM: list[str] = ["Mattioli Welford Road", "Mattioli Woods Welford Road", "Welford Road, Leicester"]
NORTHAMPTON_STADIUM: list[str] = ["cinch Stadium at Franklin's Gardens", "Frankin's Gardens", "Franklin’s Gardens"]
TWICKENHAM: list[str] = ["Twickenham, London", "Twickenham"]


def venue_formatter(venue: str):
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
