from srs.premiership.main.wikipedia.scraper.formatters.teamNameFormatter.util.CleanTeamName import clean_team_name
from srs.premiership.main.wikipedia.scraper.formatters.teamNameFormatter.util.ExtractBonusPoints import \
    extract_bonus_points
from srs.premiership.main.wikipedia.scraper.formatters.teamNameFormatter.util.FormatTeamName import format_team_name


def team_name_formatter(team_name_data: str) -> tuple[str, str]:
    """Takes team information and reformats it.

    :rtype: tuple[str, str]
    :param team_name_data: Team name and bonus point information for a match
    :return: A tuple[str, str] of the reformatted version of the team name and the number of bonus points
    they scored
    """
    # Removes any brackets and characters in between if found in the date
    team_name_cleaned: str = clean_team_name(team_name_data)

    # Extracts bonus point information
    bps: str = extract_bonus_points(team_name_data)

    # Reformats team names
    formatted_team_name: str = format_team_name(team_name_cleaned)

    return formatted_team_name, bps
