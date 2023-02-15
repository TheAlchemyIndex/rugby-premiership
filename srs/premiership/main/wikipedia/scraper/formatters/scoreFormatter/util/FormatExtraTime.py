def format_extra_time(team1_score: str, team2_score: str, string_splitter: str) -> tuple[str, str, str]:
    """Takes score strings, removes extra time tags and returns them, along with the extra time status of a match.

    :param team1_score: The points scored by team1
    :param team2_score: The points scored by team2
    :param string_splitter: The unique character string that will be used to split the score strings
    :return: The points scored by team1 and team2 without extra time tags, along with the extra time status of the match
    """
    if team1_score != "N/A" and team2_score != "N/A":
        if ("a.e.t" in team1_score) | ("a.e.t." in team2_score):
            team1_score_split: list[str] = team1_score.split(string_splitter)
            team2_score_split: list[str] = team2_score.split(string_splitter)

            if (len(team1_score_split) != 1) | (len(team2_score_split) != 1):
                team1_score: str = team1_score_split[0]
                team2_score: str = team2_score_split[0]
                extra_time: str = "Y"
            else:
                team1_score: str = "N/A"
                team2_score: str = "N/A"
                extra_time: str = "N/A"
        else:
            extra_time: str = "N"
    else:
        team1_score: str = "N/A"
        team2_score: str = "N/A"
        extra_time: str = "N/A"

    return team1_score, team2_score, extra_time
