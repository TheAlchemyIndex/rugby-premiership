import re


def extract_bonus_points(team_name_string):
    """Extracts bonus point data from a team name string.

    :param team_name_string: String containing team name and bonus point information
    :return: Bonus points scored by a team in a match
    """
    try:
        bp_match = re.search(r'\(.*?\)', team_name_string)
        if "BP" in bp_match.group():
            bps = re.search("[0-9]", bp_match.group()).group()
        else:
            bps = 0
    except AttributeError:
        bps = "N/A"

    return bps
