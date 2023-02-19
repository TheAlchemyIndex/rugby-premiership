from re import search


def extract_match_details(match_details_string: str, string_splitter: str) -> tuple[str, str]:
    """Extracts venue and referee information about a match.

    :param match_details_string: String containing venue, attendance and referee data about a match
    :param string_splitter: Custom character string used to split the match_details_string
    :return: Venue and referee information about a match
    """
    # Splits the match details by a specified character string (string_splitter)
    details_split = match_details_string.split(string_splitter)

    # Extracts the venue of the match
    venue = details_split[0]

    # Checks if the referee is included in details_split
    check_for_referee = list(filter(lambda v: search('^Referee', v), details_split))
    if len(check_for_referee) > 0:
        referee = check_for_referee[0].split("Referee: ")[1]
    else:
        referee = "N/A"

    return venue, referee
