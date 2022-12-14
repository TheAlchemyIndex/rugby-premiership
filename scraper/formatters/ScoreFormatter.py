import re

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


# Function for formatting the score information
def score_formatter(score):
    score = re.sub("\[(.*?)\]", "", score, flags=re.DOTALL).strip()

    team1_score = ""
    team2_score = ""
    winner = ""

    if "Cancelled" in score:
        team1_score = "Cancelled"
        team2_score = "Cancelled"
    elif ("P – P" in score) or ("P-P" in score) or ("P–P" in score):
        team1_score = "Postponed"
        team2_score = "Postponed"
    elif score == "v":
        team1_score = "Upcoming"
        team2_score = "Upcoming"
    elif " – " in score:
        score_split = score.split(" – ")
        team1_score = score_split[0]
        team2_score = score_split[1]
    elif "–" in score:
        score_split = score.split("–")
        team1_score = score_split[0]
        team2_score = score_split[1]
    elif "-" in score:
        score_split = score.split("-")
        team1_score = score_split[0]
        team2_score = score_split[1]

    if ("a.e.t" in team1_score) | ("a.e.t." in team2_score):
        team1_score = int(team1_score.split(BR_REPLACE)[0])
        team2_score = int(team2_score.split(BR_REPLACE)[0])
        extra_time = "Y"
    else:
        extra_time = "N"

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

    formatted_scores = {"team1_score": team1_score, "team2_score": team2_score,
                        "total_score": total_score, "winner": winner, "extraTime": extra_time}

    return formatted_scores
