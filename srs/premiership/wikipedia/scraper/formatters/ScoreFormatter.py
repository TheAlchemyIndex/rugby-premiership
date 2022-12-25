import re
from srs.premiership.wikipedia.constants import OriginalColumns

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


def score_formatter(score_data):
    """Takes score information, reformats it and returns it in a key: value dictionary format.

    :param score_data: Score information about a match
    :return: A key: value dictionary containing the team1_score, team2_score, total_score, winner and extra
    time status of a match
    """
    # Removes any brackets and characters in between if found in the date
    score_data = re.sub("\[(.*?)\]", "", score_data, flags=re.DOTALL).strip()

    team1_score = ""
    team2_score = ""
    winner = ""

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
        team1_score = int(team1_score.split(BR_REPLACE)[0])
        team2_score = int(team2_score.split(BR_REPLACE)[0])
        extra_time = "Y"
    else:
        extra_time = "N"

    # Calculates the total score
    try:
        total_score = int(team1_score) + int(team2_score)
        if int(team1_score) > int(team2_score):
            winner = "H"
        elif int(team1_score) < int(team2_score):
            winner = "A"
        elif int(team1_score) == int(team2_score):
            winner = "D"
    except ValueError:
        total_score = "N/A"
        winner = "N/A"

    formatted_scores = {OriginalColumns.TEAM1_SCORE: team1_score, OriginalColumns.TEAM2_SCORE: team2_score,
                        OriginalColumns.TOTAL_SCORE: total_score, OriginalColumns.WINNER: winner,
                        OriginalColumns.EXTRA_TIME: extra_time}
    return formatted_scores
