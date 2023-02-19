from srs.premiership.main.wikipedia.constants.matchData import ScoringTypes
from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.util.ExtractConversions import \
    extract_conversions
from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.util.ExtractDropGoals import \
    extract_drop_goals
from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.util.ExtractPenalties import \
    extract_penalties
from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.util.ExtractTries import extract_tries


def scoring_data_formatter(scoring_data: str) -> dict[str, str]:
    """Extracts the number of tries, conversions, penalties and drop goals scored by a team.

    :rtype: dict[str, str]
    :param scoring_data: Scoring information for a team
    :return: A key: value dictionary of the number of tries, conversions, penalties and drop goals scored by a team
    """
    tries: str = extract_tries(scoring_data)
    conversions: str = extract_conversions(scoring_data)
    penalties: str = extract_penalties(scoring_data)
    drop_goals: str = extract_drop_goals(scoring_data)

    formatted_scoring_data: [str, str] = {ScoringTypes.TRIES: tries,
                                          ScoringTypes.CONVERSIONS: conversions,
                                          ScoringTypes.PENALTIES: penalties,
                                          ScoringTypes.DROP_GOALS: drop_goals}

    return formatted_scoring_data
