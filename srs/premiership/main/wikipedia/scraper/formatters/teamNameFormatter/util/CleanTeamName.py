import re


def clean_team_name(unclean_team_name_string: str):
    """Takes a team name string and removes bracket based characters.

    :param unclean_team_name_string: A team name string that may contain bracket based characters
    :return: The team name string cleaned by removing bracket based characters
    """
    try:
        return re.sub("\((.*?)\)", "", unclean_team_name_string, flags=re.DOTALL).strip()
    except TypeError:
        return "N/A"
