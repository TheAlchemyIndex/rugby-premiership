def calculate_total_score(team1_score: str, team2_score: str) -> str:
    """
    Calculates the total points scored in the match by adding team1_score and team2_score.
    :rtype: str
    :param team1_score: Points scored by team1
    :param team2_score: Points scored by team2
    :return: String containing the total number of points scored in the match
    """
    try:
        total_score: str = str(int(team1_score) + int(team2_score))
    except ValueError:
        total_score: str = "N/A"

    return total_score
