import re
from typing import Optional, Match


def extract_bonus_points(team_name_string) -> str:
    """Extracts bonus point data from a team name string.

    :param team_name_string: String containing team name and bonus point information
    :return: Bonus points scored by a team in a match
    """
    try:
        bracket_search: Optional[Match[str]] = re.search(r'\(.*?\)', team_name_string)
        if bracket_search is not None:
            if "BP" in bracket_search.group():
                bps: str = str(re.search("[0-9]", bracket_search.group()).group())
            else:
                bps: str = "0"
        else:
            bps: str = "0"
    except AttributeError:
        bps: str = "N/A"
    return bps
