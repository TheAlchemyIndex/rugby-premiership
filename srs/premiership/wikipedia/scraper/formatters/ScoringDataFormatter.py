import re
from srs.premiership.wikipedia.constants.matchData import ScoringTypes

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


def scoring_data_formatter(scoring_data):
    """Extracts the number of tries, conversions, penalties and drop goals scored by a team.

    :param scoring_data: Scoring information for a team
    :return: A key: value dictionary of the number of tries, conversions, penalties and drop goals scored by a team
    """

    # Checks if the team scored any tries
    if "Try: " in scoring_data:
        scoring_data_split_tries = scoring_data.split("Try: ")
        # Splits out the try information and replaces + symbols for tries scored in added time
        tries_split = scoring_data_split_tries[1].split("Con: ")[0].split("Pen: ")[0].split("Drop: ")[0] \
            .replace("+", "").replace(" ", "")
        # Counts how many tries scored by counting the time stamps for when they were scored
        tries = len(re.findall("[0-9]'|[0-9][0-9]'|[0-9][0-9][0-9]'", tries_split))
    else:
        tries = 0

    # Checks if the team scored any conversions
    if "Con: " in scoring_data:
        scoring_data_split_cons = scoring_data.split("Con: ")
        # Splits out the conversion information and replaces + symbols for conversions scored in added time
        cons_split = scoring_data_split_cons[1].split("Pen: ")[0].split("Drop: ")[0].replace("+", "").replace(" ", "")
        # Gets how many conversions were scored by extracting the first digits of the success rate (i.e., 2/3)
        cons_list = re.findall("[0-9]/|[0-9][0-9]/", cons_split)
        # Removes / from values in cons_list and sums to find the number of conversions scored
        conversions = sum(list(map(lambda v: int(v.split("/")[0]), cons_list)))
    else:
        conversions = 0

    # Checks if the team scored any penalties
    if "Pen: " in scoring_data:
        scoring_data_split_pens = scoring_data.split("Pen: ")
        # Splits out the penalties information and replaces + symbols for penalties scored in added time
        pens_split = scoring_data_split_pens[1].split("Drop: ")[0].replace("+", "").replace(" ", "")
        # Gets how many penalties were scored by extracting the first digits of the success rate (i.e., 2/3)
        pens_list = re.findall("[0-9]/|[0-9][0-9]/", pens_split)
        # Removes / from values in pens_list and sums to find the number of penalties scored
        penalties = sum(list(map(lambda v: int(v.split("/")[0]), pens_list)))
        # Some matches don't show success rate, so counting timestamps of pens scored is used
        if penalties == 0:
            penalties = len(re.findall("[0-9]'|[0-9][0-9]'|[0-9][0-9][0-9]'", pens_split))
    else:
        penalties = 0

    # Checks if the team scored any drop goals
    if "Drop: " in scoring_data:
        scoring_data_split_drops = scoring_data.split("Drop: ")
        # Splits out the drop goal information and replaces + symbols for drop goals scored in added time
        drops_split = scoring_data_split_drops[1].replace("+", "").replace(" ", "")
        # Counts how many drop goals scored by counting the time stamps for when they were scored
        drop_goals = len(re.findall("[0-9]'|[0-9][0-9]'|[0-9][0-9][0-9]'", drops_split))
    else:
        drop_goals = 0

    formatted_scoring_data = {ScoringTypes.TRIES: tries, ScoringTypes.CONVERSIONS: conversions,
                              ScoringTypes.PENALTIES: penalties, ScoringTypes.DROP_GOALS: drop_goals}
    return formatted_scoring_data
