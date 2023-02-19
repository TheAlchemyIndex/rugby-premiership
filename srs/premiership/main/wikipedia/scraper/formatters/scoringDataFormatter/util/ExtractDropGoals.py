import re


def extract_drop_goals(scoring_data_string: str) -> str:
    """Extracts the number of drop goals scored in a match by a team.

    :rtype: str
    :param scoring_data_string: Scoring information for a team
    :return: The number of drop goals that were scored by a team
    """
    # Checks if the team scored any drop goals
    if "Drop: " in scoring_data_string:
        scoring_data_split_drops: list[str] = scoring_data_string.split("Drop: ")

        # Splits out the drop goal information and replaces + symbols for drop goals scored in added time
        drops_split: str = scoring_data_split_drops[1].replace("+", "").replace(" ", "")

        # Counts how many drop goals scored by counting the time stamps for when they were scored
        drop_goals: int = len(re.findall("[0-9]'|[0-9][0-9]'|[0-9][0-9][0-9]'", drops_split))
    else:
        drop_goals: int = 0

    return str(drop_goals)
