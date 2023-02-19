import re


def extract_tries(scoring_data_string: str) -> str:
    """Extracts the number of tries scored in a match by a team.

    :rtype: str
    :param scoring_data_string: Scoring information for a team
    :return: The number of tries that were scored by a team
    """
    # Checks if the team scored any tries
    if "Try: " in scoring_data_string:
        scoring_data_split_tries: list[str] = scoring_data_string.split("Try: ")

        # Splits out the try information and replaces + symbols for tries scored in added time
        tries_split: str = scoring_data_split_tries[1].split("Con: ")[0].split("Pen: ")[0].split("Drop: ")[0] \
            .replace("+", "").replace(" ", "")

        # Counts how many tries scored by counting the time stamps for when they were scored
        tries: int = len(re.findall("[0-9]'|[0-9][0-9]'|[0-9][0-9][0-9]'", tries_split))
    else:
        tries: int = 0

    return str(tries)
