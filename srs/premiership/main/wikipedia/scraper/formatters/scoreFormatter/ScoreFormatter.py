import re

from srs.premiership.main.wikipedia.constants import StringSplitter
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.CleanScore import clean_score


def score_formatter(score_data):
    """Takes score information, reformats it and returns it in a key: value dictionary format.

    :param score_data: Score information about a match
    :return: A key: value dictionary containing the team1_score, team2_score, total_score, result and extra
    time status of a match
    """
    # Removes any brackets and characters in between if found in the score string
    score_data = clean_score(score_data)

    team1_score = ""
    team2_score = ""
    result = ""
    result_flipped = ""

    if "Cancelled" in score_data:
        team1_score = "Cancelled"
        team2_score = "Cancelled"
    elif ("P – P" in score_data) or ("P-P" in score_data) or ("P–P" in score_data):
        team1_score = "Postponed"
        team2_score = "Postponed"
    elif score_data == "v":
        team1_score = "Upcoming"
        team2_score = "Upcoming"
    elif " – " in score_data:
        score_split = score_data.split(" – ")
        team1_score = score_split[0]
        team2_score = score_split[1]
    elif "–" in score_data:
        score_split = score_data.split("–")
        team1_score = score_split[0]
        team2_score = score_split[1]
    elif "-" in score_data:
        score_split = score_data.split("-")
        team1_score = score_split[0]
        team2_score = score_split[1]

    # Removes any after extra time tags that exist in the score data
    if ("a.e.t" in team1_score) | ("a.e.t." in team2_score):
        team1_score = int(team1_score.split(StringSplitter.BR_REPLACE)[0])
        team2_score = int(team2_score.split(StringSplitter.BR_REPLACE)[0])
        extra_time = "Y"
    else:
        extra_time = "N"

    # Calculates the total score
    try:
        total_score = int(team1_score) + int(team2_score)
        if int(team1_score) > int(team2_score):
            result = "W"
            result_flipped = "L"
        elif int(team1_score) < int(team2_score):
            result = "L"
            result_flipped = "W"
        elif int(team1_score) == int(team2_score):
            result = "D"
            result_flipped = "D"
    except ValueError:
        total_score = "N/A"
        result = "N/A"
        result_flipped = "N/A"

    formatted_scores = {OriginalColumns.TEAM1_POINTS: team1_score, OriginalColumns.TEAM2_POINTS: team2_score,
                        OriginalColumns.TOTAL_POINTS: total_score, OriginalColumns.RESULT: [result, result_flipped],
                        OriginalColumns.EXTRA_TIME: extra_time}
    return formatted_scores
