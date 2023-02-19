import re


def extract_conversions(scoring_data_string: str) -> str:
    """Extracts the number of conversions scored in a match by a team.

    :rtype: str
    :param scoring_data_string: Scoring information for a team
    :return: The number of conversions that were scored by a team
    """
    # Checks if the team scored any conversions
    if "Con: " in scoring_data_string:
        scoring_data_split_cons: list[str] = scoring_data_string.split("Con: ")

        # Splits out the conversion information and replaces + symbols for conversions scored in added time
        cons_split: str = scoring_data_split_cons[1].split("Pen: ")[0].split("Drop: ")[0] \
            .replace("+", "").replace(" ", "")

        # Gets list of how many conversions were scored by extracting the first digits of the success rate
        # (i.e., 2/3) - list is generated as there may be more than 1 kicker
        cons_list: list[str] = re.findall("[0-9]/|[0-9][0-9]/", cons_split)

        # Removes / from values in cons_list and sums to find the number of conversions scored
        conversions: int = sum(list(map(lambda v: int(v.split("/")[0]), cons_list)))
    else:
        conversions: int = 0

    return str(conversions)
