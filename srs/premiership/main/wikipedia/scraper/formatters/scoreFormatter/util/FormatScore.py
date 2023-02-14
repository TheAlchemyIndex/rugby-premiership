def format_score(unformatted_score):
    """Takes a score string and separates it into individual scores for both teams.

    :param unformatted_score: A score string with the scores for both teams or a match status string (i.e., postponed)
    :return: Two values representing the seperated scores for both teams
    """
    if "Cancelled" in unformatted_score:
        team1_score = "Cancelled"
        team2_score = "Cancelled"
    elif ("P – P" in unformatted_score) or ("P-P" in unformatted_score) or ("P–P" in unformatted_score):
        team1_score = "Postponed"
        team2_score = "Postponed"
    elif unformatted_score == "v":
        team1_score = "Upcoming"
        team2_score = "Upcoming"
    elif " – " in unformatted_score:
        score_split = unformatted_score.split(" – ")
        team1_score = score_split[0]
        team2_score = score_split[1]
    elif "–" in unformatted_score:
        score_split = unformatted_score.split("–")
        team1_score = score_split[0]
        team2_score = score_split[1]
    elif "-" in unformatted_score:
        score_split = unformatted_score.split("-")
        team1_score = score_split[0]
        team2_score = score_split[1]
    else:
        team1_score = "N/A"
        team2_score = "N/A"

    return team1_score, team2_score
