import re
from srs.premiership.main.wikipedia.constants.matchData import Teams


def team_name_formatter(team_name_data):
    """Takes team information and reformats it.

    :param team_name_data: Team name information from a match
    :return: A list of the reformatted version of the team name and the number of bonus points they scored
    """
    # Removes any brackets and characters in between if found in the date
    formatted_team_name = re.sub("\((.*?)\)", "", team_name_data, flags=re.DOTALL).strip()

    # Sets number of bonus points as 0 as default
    bps = 0

    # Checks if bonus point data was included in the team name
    try:
        match = re.search(r'\(.*?\)', team_name_data)
        if "BP" in match.group():
            bps = re.search("[0-9]", match.group()).group()
        else:
            bps = 0
    except AttributeError:
        bps = 0

    # Reformats team names
    if formatted_team_name == "Bath Rugby":
        return [Teams.BATH, bps]
    elif formatted_team_name == "Bristol Bears":
        return [Teams.BRISTOL, bps]
    elif formatted_team_name == "Exeter Chiefs":
        return [Teams.EXETER, bps]
    elif formatted_team_name == "Leeds Carnegie":
        return [Teams.LEEDS, bps]
    elif formatted_team_name == "Leicester Tigers":
        return [Teams.LEICESTER, bps]
    elif formatted_team_name == "Gloucester Rugby":
        return [Teams.GLOUCESTER, bps]
    elif formatted_team_name == "Newcastle Falcons":
        return [Teams.NEWCASTLE, bps]
    elif formatted_team_name == "Northampton Saints":
        return [Teams.NORTHAMPTON, bps]
    elif formatted_team_name == "Sale Sharks":
        return [Teams.SALE, bps]
    elif formatted_team_name == "London Wasps":
        return [Teams.WASPS, bps]
    elif formatted_team_name == "Worcester Warriors":
        return [Teams.WORCESTER, bps]
    else:
        return [formatted_team_name, bps]
