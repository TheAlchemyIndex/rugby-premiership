def calculate_result(team1_score, team2_score):

    try:
        if int(team1_score) > int(team2_score):
            result = "W"
            result_flipped = "L"
        elif int(team1_score) < int(team2_score):
            result = "L"
            result_flipped = "W"
        else:
            result = "D"
            result_flipped = "D"
    except ValueError:
        result = "N/A"
        result_flipped = "N/A"

    return result, result_flipped
