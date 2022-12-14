import re


def team_name_formatter(team_name):
    formatted_team_name = re.sub("\((.*?)\)", "", team_name, flags=re.DOTALL).strip()

    if formatted_team_name == "Bath Rugby":
        return "Bath"
    elif formatted_team_name == "Bristol Bears":
        return "Bristol"
    elif formatted_team_name == "Gloucester Rugby":
        return "Gloucester"
    elif formatted_team_name == "London Wasps":
        return "Wasps"
    else:
        return formatted_team_name
