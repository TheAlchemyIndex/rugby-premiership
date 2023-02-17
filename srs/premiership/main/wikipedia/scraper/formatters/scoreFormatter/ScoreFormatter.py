from srs.premiership.main.wikipedia.constants import StringSplitter
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.CalculateResult import calculate_result
from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.CalculateTotalScore import \
    calculate_total_score
from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.CleanScore import clean_score
from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.FormatExtraTime import format_extra_time
from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.util.FormatScore import format_score


def score_formatter(score_data: str) -> dict[str, str]:
    """Takes score information, reformats it and returns it in a key: value dictionary format.

    :param score_data: Score information about a match
    :return: A key: value dictionary containing the team1_score, team2_score, total_score, result and extra
    time status of a match
    """
    # Removes any brackets and characters in between if found in the score string
    score_cleaned: str = clean_score(score_data)

    # Extracts points scored by both teams
    team1_score: str
    team2_score: str
    team1_score, team2_score = format_score(score_cleaned)

    # Removes any after extra time tags that exist in the score data
    team1_score: str
    team2_score: str
    extra_time: str
    team1_score, team2_score, extra_time = format_extra_time(team1_score, team2_score, StringSplitter.BR_REPLACE)

    # Calculates the total score
    total_score: str = calculate_total_score(team1_score, team2_score)

    # Calculates the result (W, L, D)
    result: str
    result_flipped: str
    result, result_flipped = calculate_result(team1_score, team2_score)

    formatted_scores: dict[str, str] = {OriginalColumns.TEAM1_POINTS: team1_score,
                                        OriginalColumns.TEAM2_POINTS: team2_score,
                                        OriginalColumns.TOTAL_POINTS: total_score,
                                        OriginalColumns.RESULT: [result, result_flipped],
                                        OriginalColumns.EXTRA_TIME: extra_time}

    return formatted_scores
