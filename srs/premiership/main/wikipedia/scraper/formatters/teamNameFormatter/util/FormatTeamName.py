from srs.premiership.main.wikipedia.constants.matchData import Teams


def format_team_name(team_name_string):
    """Formats and standardises team names.

    :param team_name_string: Original unformatted team name
    :return: Formatted and standardised team name
    """
    if team_name_string == "Bath Rugby":
        return Teams.BATH
    elif team_name_string == "Bristol Bears":
        return Teams.BRISTOL
    elif team_name_string == "Exeter Chiefs":
        return Teams.EXETER
    elif team_name_string == "Leeds Carnegie":
        return Teams.LEEDS
    elif team_name_string == "Leicester Tigers":
        return Teams.LEICESTER
    elif team_name_string == "Gloucester Rugby":
        return Teams.GLOUCESTER
    elif team_name_string == "Newcastle Falcons":
        return Teams.NEWCASTLE
    elif team_name_string == "Northampton Saints":
        return Teams.NORTHAMPTON
    elif team_name_string == "Sale Sharks":
        return Teams.SALE
    elif team_name_string == "London Wasps":
        return Teams.WASPS
    elif team_name_string == "Worcester Warriors":
        return Teams.WORCESTER
    else:
        return team_name_string
