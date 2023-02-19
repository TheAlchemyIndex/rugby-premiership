import re


def extract_penalties(scoring_data_string: str) -> str:
    """Extracts the number of penalties scored in a match by a team.

    :rtype: str
    :param scoring_data_string: Scoring information for a team
    :return: The number of penalties that were scored by a team
    """
    # Checks if the team scored any penalties
    if "Pen: " in scoring_data_string:
        scoring_data_split_pens: list[str] = scoring_data_string.split("Pen: ")

        # Splits out the penalties information and replaces + symbols for penalties scored in added time
        pens_split: str = scoring_data_split_pens[1].split("Drop: ")[0].replace("+", "").replace(" ", "")

        # Gets how many penalties were scored by extracting the first digits of the success rate (i.e., 2/3)
        # list is generated as there may be more than 1 kicker
        pens_list: list[str] = re.findall("[0-9]/|[0-9][0-9]/", pens_split)

        # Removes / from values in pens_list and sums to find the number of penalties scored
        penalties_summed: int = sum(list(map(lambda v: int(v.split("/")[0]), pens_list)))

        # Some matches don't show success rate, so counting timestamps of pens scored is used
        if penalties_summed == 0:
            penalties: int = len(re.findall("[0-9]'|[0-9][0-9]'|[0-9][0-9][0-9]'", pens_split))
        else:
            penalties: int = penalties_summed
    else:
        penalties: int = 0

    return str(penalties)
