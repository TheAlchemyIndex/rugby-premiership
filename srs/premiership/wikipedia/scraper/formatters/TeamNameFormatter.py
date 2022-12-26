import re


def team_name_formatter(team_name_data):
    """Takes team information and reformats it.

    :param team_name_data: Team name information about a match
    :return: A reformatted version of the team name
    """
    # Removes any brackets and characters in between if found in the date
    formatted_team_name = re.sub("\((.*?)\)", "", team_name_data, flags=re.DOTALL).strip()

    bps = 0

    try:
        match = re.search(r'\(.*?\)', team_name_data)
        if "BP" in match.group():
            bps = re.search("[0-9]", match.group()).group()
        else:
            bps = 0
    except AttributeError:
        bps = 0

    if formatted_team_name == "Bath Rugby":
        return ["Bath", bps]
    elif formatted_team_name == "Bristol Bears":
        return ["Bristol", bps]
    elif formatted_team_name == "Exeter Chiefs":
        return ["Exeter", bps]
    elif formatted_team_name == "Leeds Carnegie":
        return ["Leeds", bps]
    elif formatted_team_name == "Leicester Tigers":
        return ["Leicester", bps]
    elif formatted_team_name == "Gloucester Rugby":
        return ["Gloucester", bps]
    elif formatted_team_name == "Newcastle Falcons":
        return ["Newcastle", bps]
    elif formatted_team_name == "Northampton Saints":
        return ["Northampton", bps]
    elif formatted_team_name == "Sale Sharks":
        return ["Sale", bps]
    elif formatted_team_name == "London Wasps":
        return ["Wasps", bps]
    elif formatted_team_name == "Worcester Warriors":
        return ["Worcester", bps]
    else:
        return [formatted_team_name, bps]
