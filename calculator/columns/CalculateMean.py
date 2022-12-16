from calculator.columns.ColumnHelper import *

TEAM1_NAME = "team1Name"
TEAM2_NAME = "team2Name"
TEAM1_SCORE = "team1Score"
TEAM2_SCORE = "team2Score"
TOTAL_SCORE = "totalScore"
MONTH = "month"
YEAR = "year"
SEASON = "season"


def calc_means(df):
    """Calculate the mean of the score columns.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns
    """
    df["avgHomeScore"] = df[TEAM1_SCORE].mean()
    df["avgAwayScore"] = df[TEAM2_SCORE].mean()
    df["avgTotalScore"] = df[TOTAL_SCORE].mean()
    return df


def calc_conditional_means_two_cols(df):
    """Calculate the mean of the score columns, based on the month, year and season columns.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns by month, year and
    season
    """
    # By home team scores
    avg_home_score_by_month = two_columns_mean(df, MONTH, TEAM1_SCORE, "avgHomeScoreByMonth")
    avg_home_score_by_year = two_columns_mean(df, YEAR, TEAM1_SCORE, "avgHomeScoreByYear")
    avg_home_score_by_season = two_columns_mean(df, SEASON, TEAM1_SCORE, "avgHomeScoreBySeason")
    avg_home_score_by_team = two_columns_mean(df, TEAM1_NAME, TEAM1_SCORE, "avgHomeScoreByTeam")

    # By away team scores
    avg_away_score_by_month = two_columns_mean(df, MONTH, TEAM2_SCORE, "avgAwayScoreByMonth")
    avg_away_score_by_year = two_columns_mean(df, YEAR, TEAM2_SCORE, "avgAwayScoreByYear")
    avg_away_score_by_season = two_columns_mean(df, SEASON, TEAM2_SCORE, "avgAwayScoreBySeason")
    avg_away_score_by_team = two_columns_mean(df, TEAM2_NAME, TEAM2_SCORE, "avgAwayScoreByTeam")

    # By total score
    avg_total_score_by_month = two_columns_mean(df, MONTH, TOTAL_SCORE, "avgTotalScoreByMonth")
    avg_total_score_by_year = two_columns_mean(df, YEAR, TOTAL_SCORE, "avgTotalScoreByYear")
    avg_total_score_by_season = two_columns_mean(df, SEASON, TOTAL_SCORE, "avgTotalScoreBySeason")

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, avg_home_score_by_month, on=MONTH, how="outer")
    new_df = pd.merge(new_df, avg_home_score_by_year, on=YEAR, how="outer")
    new_df = pd.merge(new_df, avg_home_score_by_season, on=SEASON, how="outer")
    new_df = pd.merge(new_df, avg_home_score_by_team, on=TEAM1_NAME, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_month, on=MONTH, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_year, on=YEAR, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_season, on=SEASON, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_team, on=TEAM2_NAME, how="outer")
    new_df = pd.merge(new_df, avg_total_score_by_month, on=MONTH, how="outer")
    new_df = pd.merge(new_df, avg_total_score_by_year, on=YEAR, how="outer")
    new_df = pd.merge(new_df, avg_total_score_by_season, on=SEASON, how="outer")
    new_df.fillna('N/A', inplace=True)
    new_df = new_df.round(2)
    return new_df


def calc_conditional_means_three_cols(df):
    """Calculate the mean of the score columns, based on the month, year and season columns, by team.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns of each team by month,
    year and season
    """
    # By home team scores
    avg_home_score_by_team_by_month = three_columns_mean(df, MONTH, TEAM1_NAME, TEAM1_SCORE,
                                                         "avgHomeScoreByTeamByMonth")
    avg_home_score_by_team_by_year = three_columns_mean(df, YEAR, TEAM1_NAME, TEAM1_SCORE,
                                                        "avgHomeScoreByTeamByYear")
    avg_home_score_by_team_by_season = three_columns_mean(df, SEASON, TEAM1_NAME, TEAM1_SCORE,
                                                          "avgHomeScoreByTeamBySeason")

    # By away team scores
    avg_away_score_by_team_by_month = three_columns_mean(df, MONTH, TEAM2_NAME, TEAM2_SCORE,
                                                         "avgAwayScoreByTeamByMonth")
    avg_away_score_by_team_by_year = three_columns_mean(df, YEAR, TEAM2_NAME, TEAM2_SCORE,
                                                        "avgAwayScoreByTeamByYear")
    avg_away_score_by_team_by_season = three_columns_mean(df, SEASON, TEAM2_NAME, TEAM2_SCORE,
                                                          "avgAwayScoreByTeamBySeason")

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, avg_home_score_by_team_by_month, on=[TEAM1_NAME, MONTH], how="left")
    new_df = pd.merge(new_df, avg_home_score_by_team_by_year, on=[TEAM1_NAME, YEAR], how="left")
    new_df = pd.merge(new_df, avg_home_score_by_team_by_season, on=[TEAM1_NAME, SEASON], how="left")
    new_df = pd.merge(new_df, avg_away_score_by_team_by_month, on=[TEAM2_NAME, MONTH], how="left")
    new_df = pd.merge(new_df, avg_away_score_by_team_by_year, on=[TEAM2_NAME, YEAR], how="left")
    new_df = pd.merge(new_df, avg_away_score_by_team_by_season, on=[TEAM2_NAME, SEASON], how="left")
    new_df.fillna('N/A', inplace=True)
    new_df = new_df.round(2)
    return new_df


def calc_previous_5_scores_mean(df):
    """Calculate the mean of the score columns, based on the last 5 or fewer scores.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns, based on the last
    5 or fewer scores
    """
    # By home team scores
    avg_home_score_last_5_results = mean_previous_5_scores(df, TEAM1_NAME, TEAM1_SCORE,
                                                           "avgHomeLast5Results")
    # By away team scores
    avg_away_score_last_5_results = mean_previous_5_scores(df, TEAM2_NAME, TEAM2_SCORE,
                                                           "avgAwayLast5Results")

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, avg_home_score_last_5_results, on=TEAM1_NAME, how="outer")
    new_df = pd.merge(new_df, avg_away_score_last_5_results, on=TEAM2_NAME, how="outer")
    new_df.fillna('N/A', inplace=True)
    new_df = new_df.round(2)
    return new_df


def calc_previous_3_scores_mean_opposition(df):
    """Calculate the mean of the score columns, based on the last 3 or fewer scores, by opposing teams.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns, based on the last
    3 or fewer scores, by opposing teams
    """
    # By home team scores
    avg_home_score_last_3_results_opposition = mean_previous_3_scores_opposition(df, TEAM1_NAME,
                                                                                 TEAM2_NAME, TEAM1_SCORE,
                                                                                 "avgHomeLast3ResultsAgainstOpponent")
    # By away team scores
    avg_away_score_last_3_results_opposition = mean_previous_3_scores_opposition(df, TEAM2_NAME,
                                                                                 TEAM1_NAME, TEAM2_SCORE,
                                                                                 "avgAwayLast3ResultsAgainstOpponent")

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, avg_home_score_last_3_results_opposition, on=[TEAM1_NAME, TEAM2_NAME], how="left")
    new_df = pd.merge(new_df, avg_away_score_last_3_results_opposition, on=[TEAM2_NAME, TEAM1_NAME], how="left")
    new_df.fillna('N/A', inplace=True)
    new_df = new_df.round(2)
    return new_df
